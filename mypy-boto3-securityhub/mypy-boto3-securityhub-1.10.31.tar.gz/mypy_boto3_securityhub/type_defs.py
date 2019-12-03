"Main interface for securityhub service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef",
    "ClientBatchDisableStandardsResponseTypeDef",
    "ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef",
    "ClientBatchEnableStandardsResponseTypeDef",
    "ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef",
    "ClientBatchImportFindingsFindingsComplianceTypeDef",
    "ClientBatchImportFindingsFindingsMalwareTypeDef",
    "ClientBatchImportFindingsFindingsNetworkTypeDef",
    "ClientBatchImportFindingsFindingsNoteTypeDef",
    "ClientBatchImportFindingsFindingsProcessTypeDef",
    "ClientBatchImportFindingsFindingsRelatedFindingsTypeDef",
    "ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef",
    "ClientBatchImportFindingsFindingsRemediationTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef",
    "ClientBatchImportFindingsFindingsResourcesDetailsTypeDef",
    "ClientBatchImportFindingsFindingsResourcesTypeDef",
    "ClientBatchImportFindingsFindingsSeverityTypeDef",
    "ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef",
    "ClientBatchImportFindingsFindingsTypeDef",
    "ClientBatchImportFindingsResponseFailedFindingsTypeDef",
    "ClientBatchImportFindingsResponseTypeDef",
    "ClientCreateActionTargetResponseTypeDef",
    "ClientCreateInsightFiltersAwsAccountIdTypeDef",
    "ClientCreateInsightFiltersCompanyNameTypeDef",
    "ClientCreateInsightFiltersComplianceStatusTypeDef",
    "ClientCreateInsightFiltersConfidenceTypeDef",
    "ClientCreateInsightFiltersCreatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersCreatedAtTypeDef",
    "ClientCreateInsightFiltersCriticalityTypeDef",
    "ClientCreateInsightFiltersDescriptionTypeDef",
    "ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersFirstObservedAtTypeDef",
    "ClientCreateInsightFiltersGeneratorIdTypeDef",
    "ClientCreateInsightFiltersIdTypeDef",
    "ClientCreateInsightFiltersKeywordTypeDef",
    "ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersLastObservedAtTypeDef",
    "ClientCreateInsightFiltersMalwareNameTypeDef",
    "ClientCreateInsightFiltersMalwarePathTypeDef",
    "ClientCreateInsightFiltersMalwareStateTypeDef",
    "ClientCreateInsightFiltersMalwareTypeTypeDef",
    "ClientCreateInsightFiltersNetworkDestinationDomainTypeDef",
    "ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef",
    "ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef",
    "ClientCreateInsightFiltersNetworkDestinationPortTypeDef",
    "ClientCreateInsightFiltersNetworkDirectionTypeDef",
    "ClientCreateInsightFiltersNetworkProtocolTypeDef",
    "ClientCreateInsightFiltersNetworkSourceDomainTypeDef",
    "ClientCreateInsightFiltersNetworkSourceIpV4TypeDef",
    "ClientCreateInsightFiltersNetworkSourceIpV6TypeDef",
    "ClientCreateInsightFiltersNetworkSourceMacTypeDef",
    "ClientCreateInsightFiltersNetworkSourcePortTypeDef",
    "ClientCreateInsightFiltersNoteTextTypeDef",
    "ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersNoteUpdatedAtTypeDef",
    "ClientCreateInsightFiltersNoteUpdatedByTypeDef",
    "ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersProcessLaunchedAtTypeDef",
    "ClientCreateInsightFiltersProcessNameTypeDef",
    "ClientCreateInsightFiltersProcessParentPidTypeDef",
    "ClientCreateInsightFiltersProcessPathTypeDef",
    "ClientCreateInsightFiltersProcessPidTypeDef",
    "ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersProcessTerminatedAtTypeDef",
    "ClientCreateInsightFiltersProductArnTypeDef",
    "ClientCreateInsightFiltersProductFieldsTypeDef",
    "ClientCreateInsightFiltersProductNameTypeDef",
    "ClientCreateInsightFiltersRecommendationTextTypeDef",
    "ClientCreateInsightFiltersRecordStateTypeDef",
    "ClientCreateInsightFiltersRelatedFindingsIdTypeDef",
    "ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientCreateInsightFiltersResourceContainerImageIdTypeDef",
    "ClientCreateInsightFiltersResourceContainerImageNameTypeDef",
    "ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef",
    "ClientCreateInsightFiltersResourceContainerNameTypeDef",
    "ClientCreateInsightFiltersResourceDetailsOtherTypeDef",
    "ClientCreateInsightFiltersResourceIdTypeDef",
    "ClientCreateInsightFiltersResourcePartitionTypeDef",
    "ClientCreateInsightFiltersResourceRegionTypeDef",
    "ClientCreateInsightFiltersResourceTagsTypeDef",
    "ClientCreateInsightFiltersResourceTypeTypeDef",
    "ClientCreateInsightFiltersSeverityLabelTypeDef",
    "ClientCreateInsightFiltersSeverityNormalizedTypeDef",
    "ClientCreateInsightFiltersSeverityProductTypeDef",
    "ClientCreateInsightFiltersSourceUrlTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef",
    "ClientCreateInsightFiltersTitleTypeDef",
    "ClientCreateInsightFiltersTypeTypeDef",
    "ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef",
    "ClientCreateInsightFiltersUpdatedAtTypeDef",
    "ClientCreateInsightFiltersUserDefinedFieldsTypeDef",
    "ClientCreateInsightFiltersVerificationStateTypeDef",
    "ClientCreateInsightFiltersWorkflowStateTypeDef",
    "ClientCreateInsightFiltersTypeDef",
    "ClientCreateInsightResponseTypeDef",
    "ClientCreateMembersAccountDetailsTypeDef",
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    "ClientCreateMembersResponseTypeDef",
    "ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeclineInvitationsResponseTypeDef",
    "ClientDeleteActionTargetResponseTypeDef",
    "ClientDeleteInsightResponseTypeDef",
    "ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeleteInvitationsResponseTypeDef",
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    "ClientDeleteMembersResponseTypeDef",
    "ClientDescribeActionTargetsResponseActionTargetsTypeDef",
    "ClientDescribeActionTargetsResponseTypeDef",
    "ClientDescribeHubResponseTypeDef",
    "ClientDescribeProductsResponseProductsTypeDef",
    "ClientDescribeProductsResponseTypeDef",
    "ClientEnableImportFindingsForProductResponseTypeDef",
    "ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef",
    "ClientGetEnabledStandardsResponseTypeDef",
    "ClientGetFindingsFiltersAwsAccountIdTypeDef",
    "ClientGetFindingsFiltersCompanyNameTypeDef",
    "ClientGetFindingsFiltersComplianceStatusTypeDef",
    "ClientGetFindingsFiltersConfidenceTypeDef",
    "ClientGetFindingsFiltersCreatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersCreatedAtTypeDef",
    "ClientGetFindingsFiltersCriticalityTypeDef",
    "ClientGetFindingsFiltersDescriptionTypeDef",
    "ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersFirstObservedAtTypeDef",
    "ClientGetFindingsFiltersGeneratorIdTypeDef",
    "ClientGetFindingsFiltersIdTypeDef",
    "ClientGetFindingsFiltersKeywordTypeDef",
    "ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersLastObservedAtTypeDef",
    "ClientGetFindingsFiltersMalwareNameTypeDef",
    "ClientGetFindingsFiltersMalwarePathTypeDef",
    "ClientGetFindingsFiltersMalwareStateTypeDef",
    "ClientGetFindingsFiltersMalwareTypeTypeDef",
    "ClientGetFindingsFiltersNetworkDestinationDomainTypeDef",
    "ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef",
    "ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef",
    "ClientGetFindingsFiltersNetworkDestinationPortTypeDef",
    "ClientGetFindingsFiltersNetworkDirectionTypeDef",
    "ClientGetFindingsFiltersNetworkProtocolTypeDef",
    "ClientGetFindingsFiltersNetworkSourceDomainTypeDef",
    "ClientGetFindingsFiltersNetworkSourceIpV4TypeDef",
    "ClientGetFindingsFiltersNetworkSourceIpV6TypeDef",
    "ClientGetFindingsFiltersNetworkSourceMacTypeDef",
    "ClientGetFindingsFiltersNetworkSourcePortTypeDef",
    "ClientGetFindingsFiltersNoteTextTypeDef",
    "ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersNoteUpdatedAtTypeDef",
    "ClientGetFindingsFiltersNoteUpdatedByTypeDef",
    "ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersProcessLaunchedAtTypeDef",
    "ClientGetFindingsFiltersProcessNameTypeDef",
    "ClientGetFindingsFiltersProcessParentPidTypeDef",
    "ClientGetFindingsFiltersProcessPathTypeDef",
    "ClientGetFindingsFiltersProcessPidTypeDef",
    "ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersProcessTerminatedAtTypeDef",
    "ClientGetFindingsFiltersProductArnTypeDef",
    "ClientGetFindingsFiltersProductFieldsTypeDef",
    "ClientGetFindingsFiltersProductNameTypeDef",
    "ClientGetFindingsFiltersRecommendationTextTypeDef",
    "ClientGetFindingsFiltersRecordStateTypeDef",
    "ClientGetFindingsFiltersRelatedFindingsIdTypeDef",
    "ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientGetFindingsFiltersResourceContainerImageIdTypeDef",
    "ClientGetFindingsFiltersResourceContainerImageNameTypeDef",
    "ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef",
    "ClientGetFindingsFiltersResourceContainerNameTypeDef",
    "ClientGetFindingsFiltersResourceDetailsOtherTypeDef",
    "ClientGetFindingsFiltersResourceIdTypeDef",
    "ClientGetFindingsFiltersResourcePartitionTypeDef",
    "ClientGetFindingsFiltersResourceRegionTypeDef",
    "ClientGetFindingsFiltersResourceTagsTypeDef",
    "ClientGetFindingsFiltersResourceTypeTypeDef",
    "ClientGetFindingsFiltersSeverityLabelTypeDef",
    "ClientGetFindingsFiltersSeverityNormalizedTypeDef",
    "ClientGetFindingsFiltersSeverityProductTypeDef",
    "ClientGetFindingsFiltersSourceUrlTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef",
    "ClientGetFindingsFiltersTitleTypeDef",
    "ClientGetFindingsFiltersTypeTypeDef",
    "ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef",
    "ClientGetFindingsFiltersUpdatedAtTypeDef",
    "ClientGetFindingsFiltersUserDefinedFieldsTypeDef",
    "ClientGetFindingsFiltersVerificationStateTypeDef",
    "ClientGetFindingsFiltersWorkflowStateTypeDef",
    "ClientGetFindingsFiltersTypeDef",
    "ClientGetFindingsResponseFindingsComplianceTypeDef",
    "ClientGetFindingsResponseFindingsMalwareTypeDef",
    "ClientGetFindingsResponseFindingsNetworkTypeDef",
    "ClientGetFindingsResponseFindingsNoteTypeDef",
    "ClientGetFindingsResponseFindingsProcessTypeDef",
    "ClientGetFindingsResponseFindingsRelatedFindingsTypeDef",
    "ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef",
    "ClientGetFindingsResponseFindingsRemediationTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef",
    "ClientGetFindingsResponseFindingsResourcesDetailsTypeDef",
    "ClientGetFindingsResponseFindingsResourcesTypeDef",
    "ClientGetFindingsResponseFindingsSeverityTypeDef",
    "ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef",
    "ClientGetFindingsResponseFindingsTypeDef",
    "ClientGetFindingsResponseTypeDef",
    "ClientGetFindingsSortCriteriaTypeDef",
    "ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef",
    "ClientGetInsightResultsResponseInsightResultsTypeDef",
    "ClientGetInsightResultsResponseTypeDef",
    "ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef",
    "ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef",
    "ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef",
    "ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef",
    "ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersKeywordTypeDef",
    "ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef",
    "ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef",
    "ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProductArnTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef",
    "ClientGetInsightsResponseInsightsFiltersProductNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef",
    "ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef",
    "ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef",
    "ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef",
    "ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef",
    "ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef",
    "ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef",
    "ClientGetInsightsResponseInsightsFiltersTitleTypeDef",
    "ClientGetInsightsResponseInsightsFiltersTypeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef",
    "ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef",
    "ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef",
    "ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef",
    "ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef",
    "ClientGetInsightsResponseInsightsFiltersTypeDef",
    "ClientGetInsightsResponseInsightsTypeDef",
    "ClientGetInsightsResponseTypeDef",
    "ClientGetInvitationsCountResponseTypeDef",
    "ClientGetMasterAccountResponseMasterTypeDef",
    "ClientGetMasterAccountResponseTypeDef",
    "ClientGetMembersResponseMembersTypeDef",
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    "ClientGetMembersResponseTypeDef",
    "ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    "ClientInviteMembersResponseTypeDef",
    "ClientListEnabledProductsForImportResponseTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListMembersResponseMembersTypeDef",
    "ClientListMembersResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateFindingsFiltersAwsAccountIdTypeDef",
    "ClientUpdateFindingsFiltersCompanyNameTypeDef",
    "ClientUpdateFindingsFiltersComplianceStatusTypeDef",
    "ClientUpdateFindingsFiltersConfidenceTypeDef",
    "ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersCreatedAtTypeDef",
    "ClientUpdateFindingsFiltersCriticalityTypeDef",
    "ClientUpdateFindingsFiltersDescriptionTypeDef",
    "ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersFirstObservedAtTypeDef",
    "ClientUpdateFindingsFiltersGeneratorIdTypeDef",
    "ClientUpdateFindingsFiltersIdTypeDef",
    "ClientUpdateFindingsFiltersKeywordTypeDef",
    "ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersLastObservedAtTypeDef",
    "ClientUpdateFindingsFiltersMalwareNameTypeDef",
    "ClientUpdateFindingsFiltersMalwarePathTypeDef",
    "ClientUpdateFindingsFiltersMalwareStateTypeDef",
    "ClientUpdateFindingsFiltersMalwareTypeTypeDef",
    "ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef",
    "ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef",
    "ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef",
    "ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef",
    "ClientUpdateFindingsFiltersNetworkDirectionTypeDef",
    "ClientUpdateFindingsFiltersNetworkProtocolTypeDef",
    "ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef",
    "ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef",
    "ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef",
    "ClientUpdateFindingsFiltersNetworkSourceMacTypeDef",
    "ClientUpdateFindingsFiltersNetworkSourcePortTypeDef",
    "ClientUpdateFindingsFiltersNoteTextTypeDef",
    "ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef",
    "ClientUpdateFindingsFiltersNoteUpdatedByTypeDef",
    "ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef",
    "ClientUpdateFindingsFiltersProcessNameTypeDef",
    "ClientUpdateFindingsFiltersProcessParentPidTypeDef",
    "ClientUpdateFindingsFiltersProcessPathTypeDef",
    "ClientUpdateFindingsFiltersProcessPidTypeDef",
    "ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef",
    "ClientUpdateFindingsFiltersProductArnTypeDef",
    "ClientUpdateFindingsFiltersProductFieldsTypeDef",
    "ClientUpdateFindingsFiltersProductNameTypeDef",
    "ClientUpdateFindingsFiltersRecommendationTextTypeDef",
    "ClientUpdateFindingsFiltersRecordStateTypeDef",
    "ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef",
    "ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef",
    "ClientUpdateFindingsFiltersResourceContainerNameTypeDef",
    "ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef",
    "ClientUpdateFindingsFiltersResourceIdTypeDef",
    "ClientUpdateFindingsFiltersResourcePartitionTypeDef",
    "ClientUpdateFindingsFiltersResourceRegionTypeDef",
    "ClientUpdateFindingsFiltersResourceTagsTypeDef",
    "ClientUpdateFindingsFiltersResourceTypeTypeDef",
    "ClientUpdateFindingsFiltersSeverityLabelTypeDef",
    "ClientUpdateFindingsFiltersSeverityNormalizedTypeDef",
    "ClientUpdateFindingsFiltersSeverityProductTypeDef",
    "ClientUpdateFindingsFiltersSourceUrlTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef",
    "ClientUpdateFindingsFiltersTitleTypeDef",
    "ClientUpdateFindingsFiltersTypeTypeDef",
    "ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef",
    "ClientUpdateFindingsFiltersUpdatedAtTypeDef",
    "ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef",
    "ClientUpdateFindingsFiltersVerificationStateTypeDef",
    "ClientUpdateFindingsFiltersWorkflowStateTypeDef",
    "ClientUpdateFindingsFiltersTypeDef",
    "ClientUpdateFindingsNoteTypeDef",
    "ClientUpdateInsightFiltersAwsAccountIdTypeDef",
    "ClientUpdateInsightFiltersCompanyNameTypeDef",
    "ClientUpdateInsightFiltersComplianceStatusTypeDef",
    "ClientUpdateInsightFiltersConfidenceTypeDef",
    "ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersCreatedAtTypeDef",
    "ClientUpdateInsightFiltersCriticalityTypeDef",
    "ClientUpdateInsightFiltersDescriptionTypeDef",
    "ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersFirstObservedAtTypeDef",
    "ClientUpdateInsightFiltersGeneratorIdTypeDef",
    "ClientUpdateInsightFiltersIdTypeDef",
    "ClientUpdateInsightFiltersKeywordTypeDef",
    "ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersLastObservedAtTypeDef",
    "ClientUpdateInsightFiltersMalwareNameTypeDef",
    "ClientUpdateInsightFiltersMalwarePathTypeDef",
    "ClientUpdateInsightFiltersMalwareStateTypeDef",
    "ClientUpdateInsightFiltersMalwareTypeTypeDef",
    "ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef",
    "ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef",
    "ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef",
    "ClientUpdateInsightFiltersNetworkDestinationPortTypeDef",
    "ClientUpdateInsightFiltersNetworkDirectionTypeDef",
    "ClientUpdateInsightFiltersNetworkProtocolTypeDef",
    "ClientUpdateInsightFiltersNetworkSourceDomainTypeDef",
    "ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef",
    "ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef",
    "ClientUpdateInsightFiltersNetworkSourceMacTypeDef",
    "ClientUpdateInsightFiltersNetworkSourcePortTypeDef",
    "ClientUpdateInsightFiltersNoteTextTypeDef",
    "ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersNoteUpdatedAtTypeDef",
    "ClientUpdateInsightFiltersNoteUpdatedByTypeDef",
    "ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersProcessLaunchedAtTypeDef",
    "ClientUpdateInsightFiltersProcessNameTypeDef",
    "ClientUpdateInsightFiltersProcessParentPidTypeDef",
    "ClientUpdateInsightFiltersProcessPathTypeDef",
    "ClientUpdateInsightFiltersProcessPidTypeDef",
    "ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersProcessTerminatedAtTypeDef",
    "ClientUpdateInsightFiltersProductArnTypeDef",
    "ClientUpdateInsightFiltersProductFieldsTypeDef",
    "ClientUpdateInsightFiltersProductNameTypeDef",
    "ClientUpdateInsightFiltersRecommendationTextTypeDef",
    "ClientUpdateInsightFiltersRecordStateTypeDef",
    "ClientUpdateInsightFiltersRelatedFindingsIdTypeDef",
    "ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "ClientUpdateInsightFiltersResourceContainerImageIdTypeDef",
    "ClientUpdateInsightFiltersResourceContainerImageNameTypeDef",
    "ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef",
    "ClientUpdateInsightFiltersResourceContainerNameTypeDef",
    "ClientUpdateInsightFiltersResourceDetailsOtherTypeDef",
    "ClientUpdateInsightFiltersResourceIdTypeDef",
    "ClientUpdateInsightFiltersResourcePartitionTypeDef",
    "ClientUpdateInsightFiltersResourceRegionTypeDef",
    "ClientUpdateInsightFiltersResourceTagsTypeDef",
    "ClientUpdateInsightFiltersResourceTypeTypeDef",
    "ClientUpdateInsightFiltersSeverityLabelTypeDef",
    "ClientUpdateInsightFiltersSeverityNormalizedTypeDef",
    "ClientUpdateInsightFiltersSeverityProductTypeDef",
    "ClientUpdateInsightFiltersSourceUrlTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    "ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef",
    "ClientUpdateInsightFiltersTitleTypeDef",
    "ClientUpdateInsightFiltersTypeTypeDef",
    "ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef",
    "ClientUpdateInsightFiltersUpdatedAtTypeDef",
    "ClientUpdateInsightFiltersUserDefinedFieldsTypeDef",
    "ClientUpdateInsightFiltersVerificationStateTypeDef",
    "ClientUpdateInsightFiltersWorkflowStateTypeDef",
    "ClientUpdateInsightFiltersTypeDef",
    "GetEnabledStandardsPaginatePaginationConfigTypeDef",
    "GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef",
    "GetEnabledStandardsPaginateResponseTypeDef",
    "GetFindingsPaginateFiltersAwsAccountIdTypeDef",
    "GetFindingsPaginateFiltersCompanyNameTypeDef",
    "GetFindingsPaginateFiltersComplianceStatusTypeDef",
    "GetFindingsPaginateFiltersConfidenceTypeDef",
    "GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersCreatedAtTypeDef",
    "GetFindingsPaginateFiltersCriticalityTypeDef",
    "GetFindingsPaginateFiltersDescriptionTypeDef",
    "GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersFirstObservedAtTypeDef",
    "GetFindingsPaginateFiltersGeneratorIdTypeDef",
    "GetFindingsPaginateFiltersIdTypeDef",
    "GetFindingsPaginateFiltersKeywordTypeDef",
    "GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersLastObservedAtTypeDef",
    "GetFindingsPaginateFiltersMalwareNameTypeDef",
    "GetFindingsPaginateFiltersMalwarePathTypeDef",
    "GetFindingsPaginateFiltersMalwareStateTypeDef",
    "GetFindingsPaginateFiltersMalwareTypeTypeDef",
    "GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef",
    "GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef",
    "GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef",
    "GetFindingsPaginateFiltersNetworkDestinationPortTypeDef",
    "GetFindingsPaginateFiltersNetworkDirectionTypeDef",
    "GetFindingsPaginateFiltersNetworkProtocolTypeDef",
    "GetFindingsPaginateFiltersNetworkSourceDomainTypeDef",
    "GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef",
    "GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef",
    "GetFindingsPaginateFiltersNetworkSourceMacTypeDef",
    "GetFindingsPaginateFiltersNetworkSourcePortTypeDef",
    "GetFindingsPaginateFiltersNoteTextTypeDef",
    "GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersNoteUpdatedAtTypeDef",
    "GetFindingsPaginateFiltersNoteUpdatedByTypeDef",
    "GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersProcessLaunchedAtTypeDef",
    "GetFindingsPaginateFiltersProcessNameTypeDef",
    "GetFindingsPaginateFiltersProcessParentPidTypeDef",
    "GetFindingsPaginateFiltersProcessPathTypeDef",
    "GetFindingsPaginateFiltersProcessPidTypeDef",
    "GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersProcessTerminatedAtTypeDef",
    "GetFindingsPaginateFiltersProductArnTypeDef",
    "GetFindingsPaginateFiltersProductFieldsTypeDef",
    "GetFindingsPaginateFiltersProductNameTypeDef",
    "GetFindingsPaginateFiltersRecommendationTextTypeDef",
    "GetFindingsPaginateFiltersRecordStateTypeDef",
    "GetFindingsPaginateFiltersRelatedFindingsIdTypeDef",
    "GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef",
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "GetFindingsPaginateFiltersResourceContainerImageIdTypeDef",
    "GetFindingsPaginateFiltersResourceContainerImageNameTypeDef",
    "GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef",
    "GetFindingsPaginateFiltersResourceContainerNameTypeDef",
    "GetFindingsPaginateFiltersResourceDetailsOtherTypeDef",
    "GetFindingsPaginateFiltersResourceIdTypeDef",
    "GetFindingsPaginateFiltersResourcePartitionTypeDef",
    "GetFindingsPaginateFiltersResourceRegionTypeDef",
    "GetFindingsPaginateFiltersResourceTagsTypeDef",
    "GetFindingsPaginateFiltersResourceTypeTypeDef",
    "GetFindingsPaginateFiltersSeverityLabelTypeDef",
    "GetFindingsPaginateFiltersSeverityNormalizedTypeDef",
    "GetFindingsPaginateFiltersSeverityProductTypeDef",
    "GetFindingsPaginateFiltersSourceUrlTypeDef",
    "GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef",
    "GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef",
    "GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef",
    "GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef",
    "GetFindingsPaginateFiltersTitleTypeDef",
    "GetFindingsPaginateFiltersTypeTypeDef",
    "GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef",
    "GetFindingsPaginateFiltersUpdatedAtTypeDef",
    "GetFindingsPaginateFiltersUserDefinedFieldsTypeDef",
    "GetFindingsPaginateFiltersVerificationStateTypeDef",
    "GetFindingsPaginateFiltersWorkflowStateTypeDef",
    "GetFindingsPaginateFiltersTypeDef",
    "GetFindingsPaginatePaginationConfigTypeDef",
    "GetFindingsPaginateResponseFindingsComplianceTypeDef",
    "GetFindingsPaginateResponseFindingsMalwareTypeDef",
    "GetFindingsPaginateResponseFindingsNetworkTypeDef",
    "GetFindingsPaginateResponseFindingsNoteTypeDef",
    "GetFindingsPaginateResponseFindingsProcessTypeDef",
    "GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef",
    "GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef",
    "GetFindingsPaginateResponseFindingsRemediationTypeDef",
    "GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    "GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    "GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef",
    "GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef",
    "GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef",
    "GetFindingsPaginateResponseFindingsResourcesTypeDef",
    "GetFindingsPaginateResponseFindingsSeverityTypeDef",
    "GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef",
    "GetFindingsPaginateResponseFindingsTypeDef",
    "GetFindingsPaginateResponseTypeDef",
    "GetFindingsPaginateSortCriteriaTypeDef",
    "GetInsightsPaginatePaginationConfigTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersTitleTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersTypeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef",
    "GetInsightsPaginateResponseInsightsFiltersTypeDef",
    "GetInsightsPaginateResponseInsightsTypeDef",
    "GetInsightsPaginateResponseTypeDef",
    "ListEnabledProductsForImportPaginatePaginationConfigTypeDef",
    "ListEnabledProductsForImportPaginateResponseTypeDef",
    "ListInvitationsPaginatePaginationConfigTypeDef",
    "ListInvitationsPaginateResponseInvitationsTypeDef",
    "ListInvitationsPaginateResponseTypeDef",
    "ListMembersPaginatePaginationConfigTypeDef",
    "ListMembersPaginateResponseMembersTypeDef",
    "ListMembersPaginateResponseTypeDef",
)


_ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "_ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)


class ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef(
    _ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef
):
    """
    - *(dict) --*

      A resource that represents your subscription to a supported standard.
      - **StandardsSubscriptionArn** *(string) --*

        The ARN of a resource that represents your subscription to a supported standard.
    """


_ClientBatchDisableStandardsResponseTypeDef = TypedDict(
    "_ClientBatchDisableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDisableStandardsResponseTypeDef(_ClientBatchDisableStandardsResponseTypeDef):
    """
    - *(dict) --*

      - **StandardsSubscriptions** *(list) --*

        The details of the standards subscriptions that were disabled.
        - *(dict) --*

          A resource that represents your subscription to a supported standard.
          - **StandardsSubscriptionArn** *(string) --*

            The ARN of a resource that represents your subscription to a supported standard.
    """


_ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "_ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)


class ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef(
    _ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef
):
    """
    - *(dict) --*

      A resource that represents your subscription to a supported standard.
      - **StandardsSubscriptionArn** *(string) --*

        The ARN of a resource that represents your subscription to a supported standard.
    """


_ClientBatchEnableStandardsResponseTypeDef = TypedDict(
    "_ClientBatchEnableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef
        ]
    },
    total=False,
)


class ClientBatchEnableStandardsResponseTypeDef(_ClientBatchEnableStandardsResponseTypeDef):
    """
    - *(dict) --*

      - **StandardsSubscriptions** *(list) --*

        The details of the standards subscriptions that were enabled.
        - *(dict) --*

          A resource that represents your subscription to a supported standard.
          - **StandardsSubscriptionArn** *(string) --*

            The ARN of a resource that represents your subscription to a supported standard.
    """


_ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef = TypedDict(
    "_ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef",
    {"StandardsArn": str, "StandardsInput": Dict[str, str]},
    total=False,
)


class ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef(
    _ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef
):
    pass


_ClientBatchImportFindingsFindingsComplianceTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsComplianceTypeDef",
    {"Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"]},
    total=False,
)


class ClientBatchImportFindingsFindingsComplianceTypeDef(
    _ClientBatchImportFindingsFindingsComplianceTypeDef
):
    pass


_ClientBatchImportFindingsFindingsMalwareTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsMalwareTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)


class ClientBatchImportFindingsFindingsMalwareTypeDef(
    _ClientBatchImportFindingsFindingsMalwareTypeDef
):
    pass


_ClientBatchImportFindingsFindingsNetworkTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsNetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)


class ClientBatchImportFindingsFindingsNetworkTypeDef(
    _ClientBatchImportFindingsFindingsNetworkTypeDef
):
    pass


_ClientBatchImportFindingsFindingsNoteTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsNoteTypeDef",
    {"Text": str, "UpdatedBy": str, "UpdatedAt": str},
    total=False,
)


class ClientBatchImportFindingsFindingsNoteTypeDef(_ClientBatchImportFindingsFindingsNoteTypeDef):
    pass


_ClientBatchImportFindingsFindingsProcessTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsProcessTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)


class ClientBatchImportFindingsFindingsProcessTypeDef(
    _ClientBatchImportFindingsFindingsProcessTypeDef
):
    pass


_ClientBatchImportFindingsFindingsRelatedFindingsTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsRelatedFindingsTypeDef",
    {"ProductArn": str, "Id": str},
    total=False,
)


class ClientBatchImportFindingsFindingsRelatedFindingsTypeDef(
    _ClientBatchImportFindingsFindingsRelatedFindingsTypeDef
):
    pass


_ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef",
    {"Text": str, "Url": str},
    total=False,
)


class ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef(
    _ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef
):
    pass


_ClientBatchImportFindingsFindingsRemediationTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsRemediationTypeDef",
    {"Recommendation": ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef},
    total=False,
)


class ClientBatchImportFindingsFindingsRemediationTypeDef(
    _ClientBatchImportFindingsFindingsRemediationTypeDef
):
    pass


_ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)


class ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef(
    _ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef
):
    pass


_ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    {"UserName": str, "Status": Literal["Active", "Inactive"], "CreatedAt": str},
    total=False,
)


class ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef(
    _ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef
):
    pass


_ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef",
    {"OwnerId": str, "OwnerName": str},
    total=False,
)


class ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef(
    _ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef
):
    pass


_ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)


class ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef(
    _ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef
):
    pass


_ClientBatchImportFindingsFindingsResourcesDetailsTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsResourcesDetailsTypeDef",
    {
        "AwsEc2Instance": ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef,
        "AwsS3Bucket": ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef,
        "AwsIamAccessKey": ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef,
        "Container": ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)


class ClientBatchImportFindingsFindingsResourcesDetailsTypeDef(
    _ClientBatchImportFindingsFindingsResourcesDetailsTypeDef
):
    pass


_ClientBatchImportFindingsFindingsResourcesTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": ClientBatchImportFindingsFindingsResourcesDetailsTypeDef,
    },
    total=False,
)


class ClientBatchImportFindingsFindingsResourcesTypeDef(
    _ClientBatchImportFindingsFindingsResourcesTypeDef
):
    pass


_ClientBatchImportFindingsFindingsSeverityTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsSeverityTypeDef",
    {"Product": float, "Normalized": int},
    total=False,
)


class ClientBatchImportFindingsFindingsSeverityTypeDef(
    _ClientBatchImportFindingsFindingsSeverityTypeDef
):
    pass


_ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)


class ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef(
    _ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef
):
    pass


_ClientBatchImportFindingsFindingsTypeDef = TypedDict(
    "_ClientBatchImportFindingsFindingsTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": ClientBatchImportFindingsFindingsSeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": ClientBatchImportFindingsFindingsRemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[ClientBatchImportFindingsFindingsMalwareTypeDef],
        "Network": ClientBatchImportFindingsFindingsNetworkTypeDef,
        "Process": ClientBatchImportFindingsFindingsProcessTypeDef,
        "ThreatIntelIndicators": List[
            ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef
        ],
        "Resources": List[ClientBatchImportFindingsFindingsResourcesTypeDef],
        "Compliance": ClientBatchImportFindingsFindingsComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[ClientBatchImportFindingsFindingsRelatedFindingsTypeDef],
        "Note": ClientBatchImportFindingsFindingsNoteTypeDef,
    },
    total=False,
)


class ClientBatchImportFindingsFindingsTypeDef(_ClientBatchImportFindingsFindingsTypeDef):
    """
    - *(dict) --*

      Provides consistent format for the contents of the Security Hub-aggregated findings.
      ``AwsSecurityFinding`` format enables you to share findings between AWS security services and
      third-party solutions, and compliance checks.
      .. note::

        A finding is a potential security issue generated either by AWS services (Amazon GuardDuty,
        Amazon Inspector, and Amazon Macie) or by the integrated third-party solutions and
        compliance checks.
    """


_ClientBatchImportFindingsResponseFailedFindingsTypeDef = TypedDict(
    "_ClientBatchImportFindingsResponseFailedFindingsTypeDef",
    {"Id": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchImportFindingsResponseFailedFindingsTypeDef(
    _ClientBatchImportFindingsResponseFailedFindingsTypeDef
):
    pass


_ClientBatchImportFindingsResponseTypeDef = TypedDict(
    "_ClientBatchImportFindingsResponseTypeDef",
    {
        "FailedCount": int,
        "SuccessCount": int,
        "FailedFindings": List[ClientBatchImportFindingsResponseFailedFindingsTypeDef],
    },
    total=False,
)


class ClientBatchImportFindingsResponseTypeDef(_ClientBatchImportFindingsResponseTypeDef):
    """
    - *(dict) --*

      - **FailedCount** *(integer) --*

        The number of findings that failed to import.
    """


_ClientCreateActionTargetResponseTypeDef = TypedDict(
    "_ClientCreateActionTargetResponseTypeDef", {"ActionTargetArn": str}, total=False
)


class ClientCreateActionTargetResponseTypeDef(_ClientCreateActionTargetResponseTypeDef):
    """
    - *(dict) --*

      - **ActionTargetArn** *(string) --*

        The ARN for the custom action target.
    """


_ClientCreateInsightFiltersAwsAccountIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersAwsAccountIdTypeDef(_ClientCreateInsightFiltersAwsAccountIdTypeDef):
    pass


_ClientCreateInsightFiltersCompanyNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersCompanyNameTypeDef(_ClientCreateInsightFiltersCompanyNameTypeDef):
    pass


_ClientCreateInsightFiltersComplianceStatusTypeDef = TypedDict(
    "_ClientCreateInsightFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersComplianceStatusTypeDef(
    _ClientCreateInsightFiltersComplianceStatusTypeDef
):
    pass


_ClientCreateInsightFiltersConfidenceTypeDef = TypedDict(
    "_ClientCreateInsightFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientCreateInsightFiltersConfidenceTypeDef(_ClientCreateInsightFiltersConfidenceTypeDef):
    pass


_ClientCreateInsightFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)


class ClientCreateInsightFiltersCreatedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersCreatedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersCreatedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientCreateInsightFiltersCreatedAtDateRangeTypeDef},
    total=False,
)


class ClientCreateInsightFiltersCreatedAtTypeDef(_ClientCreateInsightFiltersCreatedAtTypeDef):
    pass


_ClientCreateInsightFiltersCriticalityTypeDef = TypedDict(
    "_ClientCreateInsightFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientCreateInsightFiltersCriticalityTypeDef(_ClientCreateInsightFiltersCriticalityTypeDef):
    pass


_ClientCreateInsightFiltersDescriptionTypeDef = TypedDict(
    "_ClientCreateInsightFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersDescriptionTypeDef(_ClientCreateInsightFiltersDescriptionTypeDef):
    pass


_ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersFirstObservedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersFirstObservedAtTypeDef(
    _ClientCreateInsightFiltersFirstObservedAtTypeDef
):
    pass


_ClientCreateInsightFiltersGeneratorIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersGeneratorIdTypeDef(_ClientCreateInsightFiltersGeneratorIdTypeDef):
    pass


_ClientCreateInsightFiltersIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersIdTypeDef(_ClientCreateInsightFiltersIdTypeDef):
    pass


_ClientCreateInsightFiltersKeywordTypeDef = TypedDict(
    "_ClientCreateInsightFiltersKeywordTypeDef", {"Value": str}, total=False
)


class ClientCreateInsightFiltersKeywordTypeDef(_ClientCreateInsightFiltersKeywordTypeDef):
    pass


_ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersLastObservedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersLastObservedAtTypeDef(
    _ClientCreateInsightFiltersLastObservedAtTypeDef
):
    pass


_ClientCreateInsightFiltersMalwareNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersMalwareNameTypeDef(_ClientCreateInsightFiltersMalwareNameTypeDef):
    pass


_ClientCreateInsightFiltersMalwarePathTypeDef = TypedDict(
    "_ClientCreateInsightFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersMalwarePathTypeDef(_ClientCreateInsightFiltersMalwarePathTypeDef):
    pass


_ClientCreateInsightFiltersMalwareStateTypeDef = TypedDict(
    "_ClientCreateInsightFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersMalwareStateTypeDef(_ClientCreateInsightFiltersMalwareStateTypeDef):
    pass


_ClientCreateInsightFiltersMalwareTypeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersMalwareTypeTypeDef(_ClientCreateInsightFiltersMalwareTypeTypeDef):
    pass


_ClientCreateInsightFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersNetworkDestinationDomainTypeDef(
    _ClientCreateInsightFiltersNetworkDestinationDomainTypeDef
):
    pass


_ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef(
    _ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef
):
    pass


_ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef(
    _ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef
):
    pass


_ClientCreateInsightFiltersNetworkDestinationPortTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientCreateInsightFiltersNetworkDestinationPortTypeDef(
    _ClientCreateInsightFiltersNetworkDestinationPortTypeDef
):
    pass


_ClientCreateInsightFiltersNetworkDirectionTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersNetworkDirectionTypeDef(
    _ClientCreateInsightFiltersNetworkDirectionTypeDef
):
    pass


_ClientCreateInsightFiltersNetworkProtocolTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersNetworkProtocolTypeDef(
    _ClientCreateInsightFiltersNetworkProtocolTypeDef
):
    pass


_ClientCreateInsightFiltersNetworkSourceDomainTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersNetworkSourceDomainTypeDef(
    _ClientCreateInsightFiltersNetworkSourceDomainTypeDef
):
    pass


_ClientCreateInsightFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientCreateInsightFiltersNetworkSourceIpV4TypeDef(
    _ClientCreateInsightFiltersNetworkSourceIpV4TypeDef
):
    pass


_ClientCreateInsightFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientCreateInsightFiltersNetworkSourceIpV6TypeDef(
    _ClientCreateInsightFiltersNetworkSourceIpV6TypeDef
):
    pass


_ClientCreateInsightFiltersNetworkSourceMacTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersNetworkSourceMacTypeDef(
    _ClientCreateInsightFiltersNetworkSourceMacTypeDef
):
    pass


_ClientCreateInsightFiltersNetworkSourcePortTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientCreateInsightFiltersNetworkSourcePortTypeDef(
    _ClientCreateInsightFiltersNetworkSourcePortTypeDef
):
    pass


_ClientCreateInsightFiltersNoteTextTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersNoteTextTypeDef(_ClientCreateInsightFiltersNoteTextTypeDef):
    pass


_ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersNoteUpdatedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersNoteUpdatedAtTypeDef(
    _ClientCreateInsightFiltersNoteUpdatedAtTypeDef
):
    pass


_ClientCreateInsightFiltersNoteUpdatedByTypeDef = TypedDict(
    "_ClientCreateInsightFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersNoteUpdatedByTypeDef(
    _ClientCreateInsightFiltersNoteUpdatedByTypeDef
):
    pass


_ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersProcessLaunchedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersProcessLaunchedAtTypeDef(
    _ClientCreateInsightFiltersProcessLaunchedAtTypeDef
):
    pass


_ClientCreateInsightFiltersProcessNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersProcessNameTypeDef(_ClientCreateInsightFiltersProcessNameTypeDef):
    pass


_ClientCreateInsightFiltersProcessParentPidTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientCreateInsightFiltersProcessParentPidTypeDef(
    _ClientCreateInsightFiltersProcessParentPidTypeDef
):
    pass


_ClientCreateInsightFiltersProcessPathTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersProcessPathTypeDef(_ClientCreateInsightFiltersProcessPathTypeDef):
    pass


_ClientCreateInsightFiltersProcessPidTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientCreateInsightFiltersProcessPidTypeDef(_ClientCreateInsightFiltersProcessPidTypeDef):
    pass


_ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersProcessTerminatedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersProcessTerminatedAtTypeDef(
    _ClientCreateInsightFiltersProcessTerminatedAtTypeDef
):
    pass


_ClientCreateInsightFiltersProductArnTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersProductArnTypeDef(_ClientCreateInsightFiltersProductArnTypeDef):
    """
    - *(dict) --*

      A string filter for querying findings.
      - **Value** *(string) --*

        The string filter value.
    """


_ClientCreateInsightFiltersProductFieldsTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientCreateInsightFiltersProductFieldsTypeDef(
    _ClientCreateInsightFiltersProductFieldsTypeDef
):
    pass


_ClientCreateInsightFiltersProductNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersProductNameTypeDef(_ClientCreateInsightFiltersProductNameTypeDef):
    pass


_ClientCreateInsightFiltersRecommendationTextTypeDef = TypedDict(
    "_ClientCreateInsightFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersRecommendationTextTypeDef(
    _ClientCreateInsightFiltersRecommendationTextTypeDef
):
    pass


_ClientCreateInsightFiltersRecordStateTypeDef = TypedDict(
    "_ClientCreateInsightFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersRecordStateTypeDef(_ClientCreateInsightFiltersRecordStateTypeDef):
    pass


_ClientCreateInsightFiltersRelatedFindingsIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersRelatedFindingsIdTypeDef(
    _ClientCreateInsightFiltersRelatedFindingsIdTypeDef
):
    pass


_ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "_ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef(
    _ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef(
    _ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef(
    _ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef(
    _ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef(
    _ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef(
    _ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef
):
    pass


_ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef(
    _ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef
):
    pass


_ClientCreateInsightFiltersResourceContainerImageIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceContainerImageIdTypeDef(
    _ClientCreateInsightFiltersResourceContainerImageIdTypeDef
):
    pass


_ClientCreateInsightFiltersResourceContainerImageNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceContainerImageNameTypeDef(
    _ClientCreateInsightFiltersResourceContainerImageNameTypeDef
):
    pass


_ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef(
    _ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef
):
    pass


_ClientCreateInsightFiltersResourceContainerNameTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceContainerNameTypeDef(
    _ClientCreateInsightFiltersResourceContainerNameTypeDef
):
    pass


_ClientCreateInsightFiltersResourceDetailsOtherTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientCreateInsightFiltersResourceDetailsOtherTypeDef(
    _ClientCreateInsightFiltersResourceDetailsOtherTypeDef
):
    pass


_ClientCreateInsightFiltersResourceIdTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceIdTypeDef(_ClientCreateInsightFiltersResourceIdTypeDef):
    pass


_ClientCreateInsightFiltersResourcePartitionTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourcePartitionTypeDef(
    _ClientCreateInsightFiltersResourcePartitionTypeDef
):
    pass


_ClientCreateInsightFiltersResourceRegionTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceRegionTypeDef(
    _ClientCreateInsightFiltersResourceRegionTypeDef
):
    pass


_ClientCreateInsightFiltersResourceTagsTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientCreateInsightFiltersResourceTagsTypeDef(_ClientCreateInsightFiltersResourceTagsTypeDef):
    pass


_ClientCreateInsightFiltersResourceTypeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersResourceTypeTypeDef(_ClientCreateInsightFiltersResourceTypeTypeDef):
    pass


_ClientCreateInsightFiltersSeverityLabelTypeDef = TypedDict(
    "_ClientCreateInsightFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersSeverityLabelTypeDef(
    _ClientCreateInsightFiltersSeverityLabelTypeDef
):
    pass


_ClientCreateInsightFiltersSeverityNormalizedTypeDef = TypedDict(
    "_ClientCreateInsightFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientCreateInsightFiltersSeverityNormalizedTypeDef(
    _ClientCreateInsightFiltersSeverityNormalizedTypeDef
):
    pass


_ClientCreateInsightFiltersSeverityProductTypeDef = TypedDict(
    "_ClientCreateInsightFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientCreateInsightFiltersSeverityProductTypeDef(
    _ClientCreateInsightFiltersSeverityProductTypeDef
):
    pass


_ClientCreateInsightFiltersSourceUrlTypeDef = TypedDict(
    "_ClientCreateInsightFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersSourceUrlTypeDef(_ClientCreateInsightFiltersSourceUrlTypeDef):
    pass


_ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "_ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef(
    _ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef
):
    pass


_ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef(
    _ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef
):
    pass


_ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "_ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef(
    _ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef
):
    pass


_ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "_ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef(
    _ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef
):
    pass


_ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef(
    _ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef
):
    pass


_ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "_ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef(
    _ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef
):
    pass


_ClientCreateInsightFiltersTitleTypeDef = TypedDict(
    "_ClientCreateInsightFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersTitleTypeDef(_ClientCreateInsightFiltersTitleTypeDef):
    pass


_ClientCreateInsightFiltersTypeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersTypeTypeDef(_ClientCreateInsightFiltersTypeTypeDef):
    pass


_ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)


class ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef(
    _ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef
):
    pass


_ClientCreateInsightFiltersUpdatedAtTypeDef = TypedDict(
    "_ClientCreateInsightFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)


class ClientCreateInsightFiltersUpdatedAtTypeDef(_ClientCreateInsightFiltersUpdatedAtTypeDef):
    pass


_ClientCreateInsightFiltersUserDefinedFieldsTypeDef = TypedDict(
    "_ClientCreateInsightFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientCreateInsightFiltersUserDefinedFieldsTypeDef(
    _ClientCreateInsightFiltersUserDefinedFieldsTypeDef
):
    pass


_ClientCreateInsightFiltersVerificationStateTypeDef = TypedDict(
    "_ClientCreateInsightFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersVerificationStateTypeDef(
    _ClientCreateInsightFiltersVerificationStateTypeDef
):
    pass


_ClientCreateInsightFiltersWorkflowStateTypeDef = TypedDict(
    "_ClientCreateInsightFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientCreateInsightFiltersWorkflowStateTypeDef(
    _ClientCreateInsightFiltersWorkflowStateTypeDef
):
    pass


_ClientCreateInsightFiltersTypeDef = TypedDict(
    "_ClientCreateInsightFiltersTypeDef",
    {
        "ProductArn": List[ClientCreateInsightFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientCreateInsightFiltersAwsAccountIdTypeDef],
        "Id": List[ClientCreateInsightFiltersIdTypeDef],
        "GeneratorId": List[ClientCreateInsightFiltersGeneratorIdTypeDef],
        "Type": List[ClientCreateInsightFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientCreateInsightFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientCreateInsightFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientCreateInsightFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientCreateInsightFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientCreateInsightFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientCreateInsightFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientCreateInsightFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientCreateInsightFiltersConfidenceTypeDef],
        "Criticality": List[ClientCreateInsightFiltersCriticalityTypeDef],
        "Title": List[ClientCreateInsightFiltersTitleTypeDef],
        "Description": List[ClientCreateInsightFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientCreateInsightFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientCreateInsightFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientCreateInsightFiltersProductFieldsTypeDef],
        "ProductName": List[ClientCreateInsightFiltersProductNameTypeDef],
        "CompanyName": List[ClientCreateInsightFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientCreateInsightFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientCreateInsightFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientCreateInsightFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientCreateInsightFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientCreateInsightFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientCreateInsightFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientCreateInsightFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientCreateInsightFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientCreateInsightFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientCreateInsightFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientCreateInsightFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientCreateInsightFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientCreateInsightFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientCreateInsightFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientCreateInsightFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientCreateInsightFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientCreateInsightFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientCreateInsightFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientCreateInsightFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientCreateInsightFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[
            ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientCreateInsightFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientCreateInsightFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientCreateInsightFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientCreateInsightFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientCreateInsightFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientCreateInsightFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientCreateInsightFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientCreateInsightFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientCreateInsightFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientCreateInsightFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientCreateInsightFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientCreateInsightFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientCreateInsightFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientCreateInsightFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientCreateInsightFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientCreateInsightFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientCreateInsightFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientCreateInsightFiltersKeywordTypeDef],
    },
    total=False,
)


class ClientCreateInsightFiltersTypeDef(_ClientCreateInsightFiltersTypeDef):
    """
    One or more attributes used to filter the findings included in the insight. Only findings that
    match the criteria defined in the filters are included in the insight.
    - **ProductArn** *(list) --*

      The ARN generated by Security Hub that uniquely identifies a third-party company (security
      findings provider) after this provider's product (solution that generates findings) is
      registered with Security Hub.
      - *(dict) --*

        A string filter for querying findings.
        - **Value** *(string) --*

          The string filter value.
    """


_ClientCreateInsightResponseTypeDef = TypedDict(
    "_ClientCreateInsightResponseTypeDef", {"InsightArn": str}, total=False
)


class ClientCreateInsightResponseTypeDef(_ClientCreateInsightResponseTypeDef):
    """
    - *(dict) --*

      - **InsightArn** *(string) --*

        The ARN of the insight created.
    """


_ClientCreateMembersAccountDetailsTypeDef = TypedDict(
    "_ClientCreateMembersAccountDetailsTypeDef", {"AccountId": str, "Email": str}, total=False
)


class ClientCreateMembersAccountDetailsTypeDef(_ClientCreateMembersAccountDetailsTypeDef):
    """
    - *(dict) --*

      The details of an AWS account.
      - **AccountId** *(string) --*

        The ID of an AWS account.
    """


_ClientCreateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)


class ClientCreateMembersResponseUnprocessedAccountsTypeDef(
    _ClientCreateMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Details about the account that wasn't processed.
      - **AccountId** *(string) --*

        An AWS account ID of the account that wasn't be processed.
    """


_ClientCreateMembersResponseTypeDef = TypedDict(
    "_ClientCreateMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientCreateMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientCreateMembersResponseTypeDef(_ClientCreateMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of account ID and email address pairs of the AWS accounts that weren't processed.
        - *(dict) --*

          Details about the account that wasn't processed.
          - **AccountId** *(string) --*

            An AWS account ID of the account that wasn't be processed.
    """


_ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)


class ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef(
    _ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Details about the account that wasn't processed.
      - **AccountId** *(string) --*

        An AWS account ID of the account that wasn't be processed.
    """


_ClientDeclineInvitationsResponseTypeDef = TypedDict(
    "_ClientDeclineInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientDeclineInvitationsResponseTypeDef(_ClientDeclineInvitationsResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of account ID and email address pairs of the AWS accounts that weren't processed.
        - *(dict) --*

          Details about the account that wasn't processed.
          - **AccountId** *(string) --*

            An AWS account ID of the account that wasn't be processed.
    """


_ClientDeleteActionTargetResponseTypeDef = TypedDict(
    "_ClientDeleteActionTargetResponseTypeDef", {"ActionTargetArn": str}, total=False
)


class ClientDeleteActionTargetResponseTypeDef(_ClientDeleteActionTargetResponseTypeDef):
    """
    - *(dict) --*

      - **ActionTargetArn** *(string) --*

        The ARN of the custom action target that was deleted.
    """


_ClientDeleteInsightResponseTypeDef = TypedDict(
    "_ClientDeleteInsightResponseTypeDef", {"InsightArn": str}, total=False
)


class ClientDeleteInsightResponseTypeDef(_ClientDeleteInsightResponseTypeDef):
    """
    - *(dict) --*

      - **InsightArn** *(string) --*

        The ARN of the insight that was deleted.
    """


_ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)


class ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef(
    _ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Details about the account that wasn't processed.
      - **AccountId** *(string) --*

        An AWS account ID of the account that wasn't be processed.
    """


_ClientDeleteInvitationsResponseTypeDef = TypedDict(
    "_ClientDeleteInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientDeleteInvitationsResponseTypeDef(_ClientDeleteInvitationsResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of account ID and email address pairs of the AWS accounts that invitations weren't
        deleted for.
        - *(dict) --*

          Details about the account that wasn't processed.
          - **AccountId** *(string) --*

            An AWS account ID of the account that wasn't be processed.
    """


_ClientDeleteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)


class ClientDeleteMembersResponseUnprocessedAccountsTypeDef(
    _ClientDeleteMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Details about the account that wasn't processed.
      - **AccountId** *(string) --*

        An AWS account ID of the account that wasn't be processed.
    """


_ClientDeleteMembersResponseTypeDef = TypedDict(
    "_ClientDeleteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientDeleteMembersResponseTypeDef(_ClientDeleteMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of account ID and email address pairs of the AWS accounts that weren't deleted.
        - *(dict) --*

          Details about the account that wasn't processed.
          - **AccountId** *(string) --*

            An AWS account ID of the account that wasn't be processed.
    """


_ClientDescribeActionTargetsResponseActionTargetsTypeDef = TypedDict(
    "_ClientDescribeActionTargetsResponseActionTargetsTypeDef",
    {"ActionTargetArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientDescribeActionTargetsResponseActionTargetsTypeDef(
    _ClientDescribeActionTargetsResponseActionTargetsTypeDef
):
    """
    - *(dict) --*

      An ``ActionTarget`` object.
      - **ActionTargetArn** *(string) --*

        The ARN for the target action.
    """


_ClientDescribeActionTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeActionTargetsResponseTypeDef",
    {
        "ActionTargets": List[ClientDescribeActionTargetsResponseActionTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeActionTargetsResponseTypeDef(_ClientDescribeActionTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **ActionTargets** *(list) --*

        A list of ``ActionTarget`` objects. Each object includes the ``ActionTargetArn`` ,
        ``Description`` , and ``Name`` of a custom action target available in Security Hub.
        - *(dict) --*

          An ``ActionTarget`` object.
          - **ActionTargetArn** *(string) --*

            The ARN for the target action.
    """


_ClientDescribeHubResponseTypeDef = TypedDict(
    "_ClientDescribeHubResponseTypeDef", {"HubArn": str, "SubscribedAt": str}, total=False
)


class ClientDescribeHubResponseTypeDef(_ClientDescribeHubResponseTypeDef):
    """
    - *(dict) --*

      - **HubArn** *(string) --*

        The ARN of the Hub resource retrieved.
    """


_ClientDescribeProductsResponseProductsTypeDef = TypedDict(
    "_ClientDescribeProductsResponseProductsTypeDef",
    {
        "ProductArn": str,
        "ProductName": str,
        "CompanyName": str,
        "Description": str,
        "Categories": List[str],
        "MarketplaceUrl": str,
        "ActivationUrl": str,
        "ProductSubscriptionResourcePolicy": str,
    },
    total=False,
)


class ClientDescribeProductsResponseProductsTypeDef(_ClientDescribeProductsResponseProductsTypeDef):
    """
    - *(dict) --*

      Contains details about a product.
      - **ProductArn** *(string) --*

        The ARN assigned to the product.
    """


_ClientDescribeProductsResponseTypeDef = TypedDict(
    "_ClientDescribeProductsResponseTypeDef",
    {"Products": List[ClientDescribeProductsResponseProductsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeProductsResponseTypeDef(_ClientDescribeProductsResponseTypeDef):
    """
    - *(dict) --*

      - **Products** *(list) --*

        A list of products, including details for each product.
        - *(dict) --*

          Contains details about a product.
          - **ProductArn** *(string) --*

            The ARN assigned to the product.
    """


_ClientEnableImportFindingsForProductResponseTypeDef = TypedDict(
    "_ClientEnableImportFindingsForProductResponseTypeDef",
    {"ProductSubscriptionArn": str},
    total=False,
)


class ClientEnableImportFindingsForProductResponseTypeDef(
    _ClientEnableImportFindingsForProductResponseTypeDef
):
    """
    - *(dict) --*

      - **ProductSubscriptionArn** *(string) --*

        The ARN of your subscription to the product to enable integrations for.
    """


_ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "_ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)


class ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef(
    _ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef
):
    """
    - *(dict) --*

      A resource that represents your subscription to a supported standard.
      - **StandardsSubscriptionArn** *(string) --*

        The ARN of a resource that represents your subscription to a supported standard.
    """


_ClientGetEnabledStandardsResponseTypeDef = TypedDict(
    "_ClientGetEnabledStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetEnabledStandardsResponseTypeDef(_ClientGetEnabledStandardsResponseTypeDef):
    """
    - *(dict) --*

      - **StandardsSubscriptions** *(list) --*

        A list of ``StandardsSubscriptions`` objects that include information about the enabled
        standards.
        - *(dict) --*

          A resource that represents your subscription to a supported standard.
          - **StandardsSubscriptionArn** *(string) --*

            The ARN of a resource that represents your subscription to a supported standard.
    """


_ClientGetFindingsFiltersAwsAccountIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersAwsAccountIdTypeDef(_ClientGetFindingsFiltersAwsAccountIdTypeDef):
    pass


_ClientGetFindingsFiltersCompanyNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersCompanyNameTypeDef(_ClientGetFindingsFiltersCompanyNameTypeDef):
    pass


_ClientGetFindingsFiltersComplianceStatusTypeDef = TypedDict(
    "_ClientGetFindingsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersComplianceStatusTypeDef(
    _ClientGetFindingsFiltersComplianceStatusTypeDef
):
    pass


_ClientGetFindingsFiltersConfidenceTypeDef = TypedDict(
    "_ClientGetFindingsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetFindingsFiltersConfidenceTypeDef(_ClientGetFindingsFiltersConfidenceTypeDef):
    pass


_ClientGetFindingsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)


class ClientGetFindingsFiltersCreatedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersCreatedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersCreatedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersCreatedAtDateRangeTypeDef},
    total=False,
)


class ClientGetFindingsFiltersCreatedAtTypeDef(_ClientGetFindingsFiltersCreatedAtTypeDef):
    pass


_ClientGetFindingsFiltersCriticalityTypeDef = TypedDict(
    "_ClientGetFindingsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetFindingsFiltersCriticalityTypeDef(_ClientGetFindingsFiltersCriticalityTypeDef):
    pass


_ClientGetFindingsFiltersDescriptionTypeDef = TypedDict(
    "_ClientGetFindingsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersDescriptionTypeDef(_ClientGetFindingsFiltersDescriptionTypeDef):
    pass


_ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersFirstObservedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetFindingsFiltersFirstObservedAtTypeDef(
    _ClientGetFindingsFiltersFirstObservedAtTypeDef
):
    pass


_ClientGetFindingsFiltersGeneratorIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersGeneratorIdTypeDef(_ClientGetFindingsFiltersGeneratorIdTypeDef):
    pass


_ClientGetFindingsFiltersIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersIdTypeDef(_ClientGetFindingsFiltersIdTypeDef):
    pass


_ClientGetFindingsFiltersKeywordTypeDef = TypedDict(
    "_ClientGetFindingsFiltersKeywordTypeDef", {"Value": str}, total=False
)


class ClientGetFindingsFiltersKeywordTypeDef(_ClientGetFindingsFiltersKeywordTypeDef):
    pass


_ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersLastObservedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersLastObservedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef},
    total=False,
)


class ClientGetFindingsFiltersLastObservedAtTypeDef(_ClientGetFindingsFiltersLastObservedAtTypeDef):
    pass


_ClientGetFindingsFiltersMalwareNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersMalwareNameTypeDef(_ClientGetFindingsFiltersMalwareNameTypeDef):
    pass


_ClientGetFindingsFiltersMalwarePathTypeDef = TypedDict(
    "_ClientGetFindingsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersMalwarePathTypeDef(_ClientGetFindingsFiltersMalwarePathTypeDef):
    pass


_ClientGetFindingsFiltersMalwareStateTypeDef = TypedDict(
    "_ClientGetFindingsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersMalwareStateTypeDef(_ClientGetFindingsFiltersMalwareStateTypeDef):
    pass


_ClientGetFindingsFiltersMalwareTypeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersMalwareTypeTypeDef(_ClientGetFindingsFiltersMalwareTypeTypeDef):
    pass


_ClientGetFindingsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersNetworkDestinationDomainTypeDef(
    _ClientGetFindingsFiltersNetworkDestinationDomainTypeDef
):
    pass


_ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef(
    _ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef
):
    pass


_ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef(
    _ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef
):
    pass


_ClientGetFindingsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetFindingsFiltersNetworkDestinationPortTypeDef(
    _ClientGetFindingsFiltersNetworkDestinationPortTypeDef
):
    pass


_ClientGetFindingsFiltersNetworkDirectionTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersNetworkDirectionTypeDef(
    _ClientGetFindingsFiltersNetworkDirectionTypeDef
):
    pass


_ClientGetFindingsFiltersNetworkProtocolTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersNetworkProtocolTypeDef(
    _ClientGetFindingsFiltersNetworkProtocolTypeDef
):
    pass


_ClientGetFindingsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersNetworkSourceDomainTypeDef(
    _ClientGetFindingsFiltersNetworkSourceDomainTypeDef
):
    pass


_ClientGetFindingsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientGetFindingsFiltersNetworkSourceIpV4TypeDef(
    _ClientGetFindingsFiltersNetworkSourceIpV4TypeDef
):
    pass


_ClientGetFindingsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientGetFindingsFiltersNetworkSourceIpV6TypeDef(
    _ClientGetFindingsFiltersNetworkSourceIpV6TypeDef
):
    pass


_ClientGetFindingsFiltersNetworkSourceMacTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersNetworkSourceMacTypeDef(
    _ClientGetFindingsFiltersNetworkSourceMacTypeDef
):
    pass


_ClientGetFindingsFiltersNetworkSourcePortTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetFindingsFiltersNetworkSourcePortTypeDef(
    _ClientGetFindingsFiltersNetworkSourcePortTypeDef
):
    pass


_ClientGetFindingsFiltersNoteTextTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersNoteTextTypeDef(_ClientGetFindingsFiltersNoteTextTypeDef):
    pass


_ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNoteUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef},
    total=False,
)


class ClientGetFindingsFiltersNoteUpdatedAtTypeDef(_ClientGetFindingsFiltersNoteUpdatedAtTypeDef):
    pass


_ClientGetFindingsFiltersNoteUpdatedByTypeDef = TypedDict(
    "_ClientGetFindingsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersNoteUpdatedByTypeDef(_ClientGetFindingsFiltersNoteUpdatedByTypeDef):
    pass


_ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetFindingsFiltersProcessLaunchedAtTypeDef(
    _ClientGetFindingsFiltersProcessLaunchedAtTypeDef
):
    pass


_ClientGetFindingsFiltersProcessNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersProcessNameTypeDef(_ClientGetFindingsFiltersProcessNameTypeDef):
    pass


_ClientGetFindingsFiltersProcessParentPidTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetFindingsFiltersProcessParentPidTypeDef(
    _ClientGetFindingsFiltersProcessParentPidTypeDef
):
    pass


_ClientGetFindingsFiltersProcessPathTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersProcessPathTypeDef(_ClientGetFindingsFiltersProcessPathTypeDef):
    pass


_ClientGetFindingsFiltersProcessPidTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetFindingsFiltersProcessPidTypeDef(_ClientGetFindingsFiltersProcessPidTypeDef):
    pass


_ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetFindingsFiltersProcessTerminatedAtTypeDef(
    _ClientGetFindingsFiltersProcessTerminatedAtTypeDef
):
    pass


_ClientGetFindingsFiltersProductArnTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersProductArnTypeDef(_ClientGetFindingsFiltersProductArnTypeDef):
    """
    - *(dict) --*

      A string filter for querying findings.
      - **Value** *(string) --*

        The string filter value.
    """


_ClientGetFindingsFiltersProductFieldsTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientGetFindingsFiltersProductFieldsTypeDef(_ClientGetFindingsFiltersProductFieldsTypeDef):
    pass


_ClientGetFindingsFiltersProductNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersProductNameTypeDef(_ClientGetFindingsFiltersProductNameTypeDef):
    pass


_ClientGetFindingsFiltersRecommendationTextTypeDef = TypedDict(
    "_ClientGetFindingsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersRecommendationTextTypeDef(
    _ClientGetFindingsFiltersRecommendationTextTypeDef
):
    pass


_ClientGetFindingsFiltersRecordStateTypeDef = TypedDict(
    "_ClientGetFindingsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersRecordStateTypeDef(_ClientGetFindingsFiltersRecordStateTypeDef):
    pass


_ClientGetFindingsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersRelatedFindingsIdTypeDef(
    _ClientGetFindingsFiltersRelatedFindingsIdTypeDef
):
    pass


_ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "_ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef(
    _ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef(
    _ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef(
    _ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef(
    _ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef(
    _ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef(
    _ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef
):
    pass


_ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef(
    _ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef
):
    pass


_ClientGetFindingsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceContainerImageIdTypeDef(
    _ClientGetFindingsFiltersResourceContainerImageIdTypeDef
):
    pass


_ClientGetFindingsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceContainerImageNameTypeDef(
    _ClientGetFindingsFiltersResourceContainerImageNameTypeDef
):
    pass


_ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef(
    _ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef
):
    pass


_ClientGetFindingsFiltersResourceContainerNameTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceContainerNameTypeDef(
    _ClientGetFindingsFiltersResourceContainerNameTypeDef
):
    pass


_ClientGetFindingsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientGetFindingsFiltersResourceDetailsOtherTypeDef(
    _ClientGetFindingsFiltersResourceDetailsOtherTypeDef
):
    pass


_ClientGetFindingsFiltersResourceIdTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceIdTypeDef(_ClientGetFindingsFiltersResourceIdTypeDef):
    pass


_ClientGetFindingsFiltersResourcePartitionTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourcePartitionTypeDef(
    _ClientGetFindingsFiltersResourcePartitionTypeDef
):
    pass


_ClientGetFindingsFiltersResourceRegionTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceRegionTypeDef(_ClientGetFindingsFiltersResourceRegionTypeDef):
    pass


_ClientGetFindingsFiltersResourceTagsTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientGetFindingsFiltersResourceTagsTypeDef(_ClientGetFindingsFiltersResourceTagsTypeDef):
    pass


_ClientGetFindingsFiltersResourceTypeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersResourceTypeTypeDef(_ClientGetFindingsFiltersResourceTypeTypeDef):
    pass


_ClientGetFindingsFiltersSeverityLabelTypeDef = TypedDict(
    "_ClientGetFindingsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersSeverityLabelTypeDef(_ClientGetFindingsFiltersSeverityLabelTypeDef):
    pass


_ClientGetFindingsFiltersSeverityNormalizedTypeDef = TypedDict(
    "_ClientGetFindingsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetFindingsFiltersSeverityNormalizedTypeDef(
    _ClientGetFindingsFiltersSeverityNormalizedTypeDef
):
    pass


_ClientGetFindingsFiltersSeverityProductTypeDef = TypedDict(
    "_ClientGetFindingsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetFindingsFiltersSeverityProductTypeDef(
    _ClientGetFindingsFiltersSeverityProductTypeDef
):
    pass


_ClientGetFindingsFiltersSourceUrlTypeDef = TypedDict(
    "_ClientGetFindingsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersSourceUrlTypeDef(_ClientGetFindingsFiltersSourceUrlTypeDef):
    pass


_ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "_ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef(
    _ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef
):
    pass


_ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef(
    _ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef
):
    pass


_ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "_ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef(
    _ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef
):
    pass


_ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "_ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef(
    _ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef
):
    pass


_ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef(
    _ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef
):
    pass


_ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "_ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef(
    _ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef
):
    pass


_ClientGetFindingsFiltersTitleTypeDef = TypedDict(
    "_ClientGetFindingsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersTitleTypeDef(_ClientGetFindingsFiltersTitleTypeDef):
    pass


_ClientGetFindingsFiltersTypeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersTypeTypeDef(_ClientGetFindingsFiltersTypeTypeDef):
    pass


_ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)


class ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef(
    _ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef
):
    pass


_ClientGetFindingsFiltersUpdatedAtTypeDef = TypedDict(
    "_ClientGetFindingsFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)


class ClientGetFindingsFiltersUpdatedAtTypeDef(_ClientGetFindingsFiltersUpdatedAtTypeDef):
    pass


_ClientGetFindingsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "_ClientGetFindingsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientGetFindingsFiltersUserDefinedFieldsTypeDef(
    _ClientGetFindingsFiltersUserDefinedFieldsTypeDef
):
    pass


_ClientGetFindingsFiltersVerificationStateTypeDef = TypedDict(
    "_ClientGetFindingsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersVerificationStateTypeDef(
    _ClientGetFindingsFiltersVerificationStateTypeDef
):
    pass


_ClientGetFindingsFiltersWorkflowStateTypeDef = TypedDict(
    "_ClientGetFindingsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetFindingsFiltersWorkflowStateTypeDef(_ClientGetFindingsFiltersWorkflowStateTypeDef):
    pass


_ClientGetFindingsFiltersTypeDef = TypedDict(
    "_ClientGetFindingsFiltersTypeDef",
    {
        "ProductArn": List[ClientGetFindingsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientGetFindingsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientGetFindingsFiltersIdTypeDef],
        "GeneratorId": List[ClientGetFindingsFiltersGeneratorIdTypeDef],
        "Type": List[ClientGetFindingsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientGetFindingsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientGetFindingsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientGetFindingsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientGetFindingsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientGetFindingsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientGetFindingsFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientGetFindingsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientGetFindingsFiltersConfidenceTypeDef],
        "Criticality": List[ClientGetFindingsFiltersCriticalityTypeDef],
        "Title": List[ClientGetFindingsFiltersTitleTypeDef],
        "Description": List[ClientGetFindingsFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientGetFindingsFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientGetFindingsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientGetFindingsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientGetFindingsFiltersProductNameTypeDef],
        "CompanyName": List[ClientGetFindingsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientGetFindingsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientGetFindingsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientGetFindingsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientGetFindingsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientGetFindingsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientGetFindingsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientGetFindingsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientGetFindingsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientGetFindingsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientGetFindingsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientGetFindingsFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientGetFindingsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientGetFindingsFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientGetFindingsFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientGetFindingsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientGetFindingsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientGetFindingsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientGetFindingsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientGetFindingsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientGetFindingsFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef],
        "ThreatIntelIndicatorCategory": List[
            ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientGetFindingsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientGetFindingsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientGetFindingsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientGetFindingsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientGetFindingsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientGetFindingsFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientGetFindingsFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientGetFindingsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientGetFindingsFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientGetFindingsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientGetFindingsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientGetFindingsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientGetFindingsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef],
        "RelatedFindingsId": List[ClientGetFindingsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientGetFindingsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientGetFindingsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientGetFindingsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientGetFindingsFiltersKeywordTypeDef],
    },
    total=False,
)


class ClientGetFindingsFiltersTypeDef(_ClientGetFindingsFiltersTypeDef):
    """
    The findings attributes used to define a condition to filter the findings returned.
    - **ProductArn** *(list) --*

      The ARN generated by Security Hub that uniquely identifies a third-party company (security
      findings provider) after this provider's product (solution that generates findings) is
      registered with Security Hub.
      - *(dict) --*

        A string filter for querying findings.
        - **Value** *(string) --*

          The string filter value.
    """


_ClientGetFindingsResponseFindingsComplianceTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsComplianceTypeDef",
    {"Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"]},
    total=False,
)


class ClientGetFindingsResponseFindingsComplianceTypeDef(
    _ClientGetFindingsResponseFindingsComplianceTypeDef
):
    pass


_ClientGetFindingsResponseFindingsMalwareTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsMalwareTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)


class ClientGetFindingsResponseFindingsMalwareTypeDef(
    _ClientGetFindingsResponseFindingsMalwareTypeDef
):
    pass


_ClientGetFindingsResponseFindingsNetworkTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsNetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsNetworkTypeDef(
    _ClientGetFindingsResponseFindingsNetworkTypeDef
):
    pass


_ClientGetFindingsResponseFindingsNoteTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsNoteTypeDef",
    {"Text": str, "UpdatedBy": str, "UpdatedAt": str},
    total=False,
)


class ClientGetFindingsResponseFindingsNoteTypeDef(_ClientGetFindingsResponseFindingsNoteTypeDef):
    pass


_ClientGetFindingsResponseFindingsProcessTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsProcessTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsProcessTypeDef(
    _ClientGetFindingsResponseFindingsProcessTypeDef
):
    pass


_ClientGetFindingsResponseFindingsRelatedFindingsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsRelatedFindingsTypeDef",
    {"ProductArn": str, "Id": str},
    total=False,
)


class ClientGetFindingsResponseFindingsRelatedFindingsTypeDef(
    _ClientGetFindingsResponseFindingsRelatedFindingsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef",
    {"Text": str, "Url": str},
    total=False,
)


class ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef(
    _ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef
):
    pass


_ClientGetFindingsResponseFindingsRemediationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsRemediationTypeDef",
    {"Recommendation": ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef},
    total=False,
)


class ClientGetFindingsResponseFindingsRemediationTypeDef(
    _ClientGetFindingsResponseFindingsRemediationTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef(
    _ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    {"UserName": str, "Status": Literal["Active", "Inactive"], "CreatedAt": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef(
    _ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef",
    {"OwnerId": str, "OwnerName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef(
    _ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef(
    _ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourcesDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourcesDetailsTypeDef",
    {
        "AwsEc2Instance": ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef,
        "AwsS3Bucket": ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef,
        "AwsIamAccessKey": ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef,
        "Container": ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourcesDetailsTypeDef(
    _ClientGetFindingsResponseFindingsResourcesDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourcesTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": ClientGetFindingsResponseFindingsResourcesDetailsTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourcesTypeDef(
    _ClientGetFindingsResponseFindingsResourcesTypeDef
):
    pass


_ClientGetFindingsResponseFindingsSeverityTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsSeverityTypeDef",
    {"Product": float, "Normalized": int},
    total=False,
)


class ClientGetFindingsResponseFindingsSeverityTypeDef(
    _ClientGetFindingsResponseFindingsSeverityTypeDef
):
    pass


_ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef(
    _ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": ClientGetFindingsResponseFindingsSeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": ClientGetFindingsResponseFindingsRemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[ClientGetFindingsResponseFindingsMalwareTypeDef],
        "Network": ClientGetFindingsResponseFindingsNetworkTypeDef,
        "Process": ClientGetFindingsResponseFindingsProcessTypeDef,
        "ThreatIntelIndicators": List[
            ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef
        ],
        "Resources": List[ClientGetFindingsResponseFindingsResourcesTypeDef],
        "Compliance": ClientGetFindingsResponseFindingsComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[ClientGetFindingsResponseFindingsRelatedFindingsTypeDef],
        "Note": ClientGetFindingsResponseFindingsNoteTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsTypeDef(_ClientGetFindingsResponseFindingsTypeDef):
    """
    - *(dict) --*

      Provides consistent format for the contents of the Security Hub-aggregated findings.
      ``AwsSecurityFinding`` format enables you to share findings between AWS security services and
      third-party solutions, and compliance checks.
      .. note::

        A finding is a potential security issue generated either by AWS services (Amazon GuardDuty,
        Amazon Inspector, and Amazon Macie) or by the integrated third-party solutions and
        compliance checks.
    """


_ClientGetFindingsResponseTypeDef = TypedDict(
    "_ClientGetFindingsResponseTypeDef",
    {"Findings": List[ClientGetFindingsResponseFindingsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetFindingsResponseTypeDef(_ClientGetFindingsResponseTypeDef):
    """
    - *(dict) --*

      - **Findings** *(list) --*

        The findings that matched the filters specified in the request.
        - *(dict) --*

          Provides consistent format for the contents of the Security Hub-aggregated findings.
          ``AwsSecurityFinding`` format enables you to share findings between AWS security services
          and third-party solutions, and compliance checks.
          .. note::

            A finding is a potential security issue generated either by AWS services (Amazon
            GuardDuty, Amazon Inspector, and Amazon Macie) or by the integrated third-party
            solutions and compliance checks.
    """


_ClientGetFindingsSortCriteriaTypeDef = TypedDict(
    "_ClientGetFindingsSortCriteriaTypeDef",
    {"Field": str, "SortOrder": Literal["asc", "desc"]},
    total=False,
)


class ClientGetFindingsSortCriteriaTypeDef(_ClientGetFindingsSortCriteriaTypeDef):
    """
    - *(dict) --*

      A collection of finding attributes used to sort findings.
      - **Field** *(string) --*

        The finding attribute used to sort findings.
    """


_ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef = TypedDict(
    "_ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef",
    {"GroupByAttributeValue": str, "Count": int},
    total=False,
)


class ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef(
    _ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef
):
    pass


_ClientGetInsightResultsResponseInsightResultsTypeDef = TypedDict(
    "_ClientGetInsightResultsResponseInsightResultsTypeDef",
    {
        "InsightArn": str,
        "GroupByAttribute": str,
        "ResultValues": List[ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef],
    },
    total=False,
)


class ClientGetInsightResultsResponseInsightResultsTypeDef(
    _ClientGetInsightResultsResponseInsightResultsTypeDef
):
    """
    - **InsightResults** *(dict) --*

      The insight results returned by the operation.
      - **InsightArn** *(string) --*

        The ARN of the insight whose results are returned by the ``GetInsightResults`` operation.
    """


_ClientGetInsightResultsResponseTypeDef = TypedDict(
    "_ClientGetInsightResultsResponseTypeDef",
    {"InsightResults": ClientGetInsightResultsResponseInsightResultsTypeDef},
    total=False,
)


class ClientGetInsightResultsResponseTypeDef(_ClientGetInsightResultsResponseTypeDef):
    """
    - *(dict) --*

      - **InsightResults** *(dict) --*

        The insight results returned by the operation.
        - **InsightArn** *(string) --*

          The ARN of the insight whose results are returned by the ``GetInsightResults`` operation.
    """


_ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef(
    _ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef(
    _ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef(
    _ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef(
    _ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersKeywordTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersKeywordTypeDef", {"Value": str}, total=False
)


class ClientGetInsightsResponseInsightsFiltersKeywordTypeDef(
    _ClientGetInsightsResponseInsightsFiltersKeywordTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef(
    _ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef(
    _ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef",
    {"Cidr": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef",
    {"Cidr": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef(
    _ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProductArnTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProductArnTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProductArnTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersProductNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersProductNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersProductNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef(
    _ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef(
    _ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef(
    _ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef(
    _ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef(
    _ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef(
    _ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef(
    _ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef(
    _ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef(
    _ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef(
    _ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef(
    _ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersTitleTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersTitleTypeDef(
    _ClientGetInsightsResponseInsightsFiltersTitleTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersTypeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersTypeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersTypeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef(
    _ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef(
    _ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef(
    _ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef(
    _ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef(
    _ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef
):
    pass


_ClientGetInsightsResponseInsightsFiltersTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsFiltersTypeDef",
    {
        "ProductArn": List[ClientGetInsightsResponseInsightsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientGetInsightsResponseInsightsFiltersIdTypeDef],
        "GeneratorId": List[ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef],
        "Type": List[ClientGetInsightsResponseInsightsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[
            ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef
        ],
        "SeverityLabel": List[ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef],
        "Criticality": List[ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef],
        "Title": List[ClientGetInsightsResponseInsightsFiltersTitleTypeDef],
        "Description": List[ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef],
        "RecommendationText": List[
            ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef
        ],
        "SourceUrl": List[ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientGetInsightsResponseInsightsFiltersProductNameTypeDef],
        "CompanyName": List[ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[
            ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef
        ],
        "NetworkSourceMac": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef
        ],
        "NetworkDestinationIpV6": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef
        ],
        "NetworkDestinationPort": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef
        ],
        "NetworkDestinationDomain": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef
        ],
        "ProcessName": List[ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[
            ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef
        ],
        "ThreatIntelIndicatorType": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef
        ],
        "ThreatIntelIndicatorValue": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef
        ],
        "ResourceContainerImageId": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef
        ],
        "ResourceContainerImageName": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[
            ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef
        ],
        "ComplianceStatus": List[ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientGetInsightsResponseInsightsFiltersKeywordTypeDef],
    },
    total=False,
)


class ClientGetInsightsResponseInsightsFiltersTypeDef(
    _ClientGetInsightsResponseInsightsFiltersTypeDef
):
    pass


_ClientGetInsightsResponseInsightsTypeDef = TypedDict(
    "_ClientGetInsightsResponseInsightsTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": ClientGetInsightsResponseInsightsFiltersTypeDef,
        "GroupByAttribute": str,
    },
    total=False,
)


class ClientGetInsightsResponseInsightsTypeDef(_ClientGetInsightsResponseInsightsTypeDef):
    """
    - *(dict) --*

      Contains information about a Security Hub insight.
      - **InsightArn** *(string) --*

        The ARN of a Security Hub insight.
    """


_ClientGetInsightsResponseTypeDef = TypedDict(
    "_ClientGetInsightsResponseTypeDef",
    {"Insights": List[ClientGetInsightsResponseInsightsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetInsightsResponseTypeDef(_ClientGetInsightsResponseTypeDef):
    """
    - *(dict) --*

      - **Insights** *(list) --*

        The insights returned by the operation.
        - *(dict) --*

          Contains information about a Security Hub insight.
          - **InsightArn** *(string) --*

            The ARN of a Security Hub insight.
    """


_ClientGetInvitationsCountResponseTypeDef = TypedDict(
    "_ClientGetInvitationsCountResponseTypeDef", {"InvitationsCount": int}, total=False
)


class ClientGetInvitationsCountResponseTypeDef(_ClientGetInvitationsCountResponseTypeDef):
    """
    - *(dict) --*

      - **InvitationsCount** *(integer) --*

        The number of all membership invitations sent to this Security Hub member account, not
        including the currently accepted invitation.
    """


_ClientGetMasterAccountResponseMasterTypeDef = TypedDict(
    "_ClientGetMasterAccountResponseMasterTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)


class ClientGetMasterAccountResponseMasterTypeDef(_ClientGetMasterAccountResponseMasterTypeDef):
    """
    - **Master** *(dict) --*

      A list of details about the Security Hub master account for the current member account.
      - **AccountId** *(string) --*

        The account ID of the Security Hub master account that the invitation was sent from.
    """


_ClientGetMasterAccountResponseTypeDef = TypedDict(
    "_ClientGetMasterAccountResponseTypeDef",
    {"Master": ClientGetMasterAccountResponseMasterTypeDef},
    total=False,
)


class ClientGetMasterAccountResponseTypeDef(_ClientGetMasterAccountResponseTypeDef):
    """
    - *(dict) --*

      - **Master** *(dict) --*

        A list of details about the Security Hub master account for the current member account.
        - **AccountId** *(string) --*

          The account ID of the Security Hub master account that the invitation was sent from.
    """


_ClientGetMembersResponseMembersTypeDef = TypedDict(
    "_ClientGetMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)


class ClientGetMembersResponseMembersTypeDef(_ClientGetMembersResponseMembersTypeDef):
    """
    - *(dict) --*

      The details about a member account.
      - **AccountId** *(string) --*

        The AWS account ID of the member account.
    """


_ClientGetMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientGetMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)


class ClientGetMembersResponseUnprocessedAccountsTypeDef(
    _ClientGetMembersResponseUnprocessedAccountsTypeDef
):
    pass


_ClientGetMembersResponseTypeDef = TypedDict(
    "_ClientGetMembersResponseTypeDef",
    {
        "Members": List[ClientGetMembersResponseMembersTypeDef],
        "UnprocessedAccounts": List[ClientGetMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)


class ClientGetMembersResponseTypeDef(_ClientGetMembersResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        A list of details about the Security Hub member accounts.
        - *(dict) --*

          The details about a member account.
          - **AccountId** *(string) --*

            The AWS account ID of the member account.
    """


_ClientInviteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)


class ClientInviteMembersResponseUnprocessedAccountsTypeDef(
    _ClientInviteMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Details about the account that wasn't processed.
      - **AccountId** *(string) --*

        An AWS account ID of the account that wasn't be processed.
    """


_ClientInviteMembersResponseTypeDef = TypedDict(
    "_ClientInviteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientInviteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientInviteMembersResponseTypeDef(_ClientInviteMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of account ID and email address pairs of the AWS accounts that couldn't be processed.
        - *(dict) --*

          Details about the account that wasn't processed.
          - **AccountId** *(string) --*

            An AWS account ID of the account that wasn't be processed.
    """


_ClientListEnabledProductsForImportResponseTypeDef = TypedDict(
    "_ClientListEnabledProductsForImportResponseTypeDef",
    {"ProductSubscriptions": List[str], "NextToken": str},
    total=False,
)


class ClientListEnabledProductsForImportResponseTypeDef(
    _ClientListEnabledProductsForImportResponseTypeDef
):
    """
    - *(dict) --*

      - **ProductSubscriptions** *(list) --*

        A list of ARNs for the resources that represent your subscriptions to products.
        - *(string) --*
    """


_ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "_ClientListInvitationsResponseInvitationsTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)


class ClientListInvitationsResponseInvitationsTypeDef(
    _ClientListInvitationsResponseInvitationsTypeDef
):
    """
    - *(dict) --*

      Details about an invitation.
      - **AccountId** *(string) --*

        The account ID of the Security Hub master account that the invitation was sent from.
    """


_ClientListInvitationsResponseTypeDef = TypedDict(
    "_ClientListInvitationsResponseTypeDef",
    {"Invitations": List[ClientListInvitationsResponseInvitationsTypeDef], "NextToken": str},
    total=False,
)


class ClientListInvitationsResponseTypeDef(_ClientListInvitationsResponseTypeDef):
    """
    - *(dict) --*

      - **Invitations** *(list) --*

        The details of the invitations returned by the operation.
        - *(dict) --*

          Details about an invitation.
          - **AccountId** *(string) --*

            The account ID of the Security Hub master account that the invitation was sent from.
    """


_ClientListMembersResponseMembersTypeDef = TypedDict(
    "_ClientListMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)


class ClientListMembersResponseMembersTypeDef(_ClientListMembersResponseMembersTypeDef):
    """
    - *(dict) --*

      The details about a member account.
      - **AccountId** *(string) --*

        The AWS account ID of the member account.
    """


_ClientListMembersResponseTypeDef = TypedDict(
    "_ClientListMembersResponseTypeDef",
    {"Members": List[ClientListMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)


class ClientListMembersResponseTypeDef(_ClientListMembersResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        Member details returned by the operation.
        - *(dict) --*

          The details about a member account.
          - **AccountId** *(string) --*

            The AWS account ID of the member account.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The tags associated with a resource.
        - *(string) --*

          - *(string) --*
    """


_ClientUpdateFindingsFiltersAwsAccountIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersAwsAccountIdTypeDef(
    _ClientUpdateFindingsFiltersAwsAccountIdTypeDef
):
    pass


_ClientUpdateFindingsFiltersCompanyNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersCompanyNameTypeDef(_ClientUpdateFindingsFiltersCompanyNameTypeDef):
    pass


_ClientUpdateFindingsFiltersComplianceStatusTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersComplianceStatusTypeDef(
    _ClientUpdateFindingsFiltersComplianceStatusTypeDef
):
    pass


_ClientUpdateFindingsFiltersConfidenceTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateFindingsFiltersConfidenceTypeDef(_ClientUpdateFindingsFiltersConfidenceTypeDef):
    pass


_ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersCreatedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef},
    total=False,
)


class ClientUpdateFindingsFiltersCreatedAtTypeDef(_ClientUpdateFindingsFiltersCreatedAtTypeDef):
    pass


_ClientUpdateFindingsFiltersCriticalityTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateFindingsFiltersCriticalityTypeDef(_ClientUpdateFindingsFiltersCriticalityTypeDef):
    pass


_ClientUpdateFindingsFiltersDescriptionTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersDescriptionTypeDef(_ClientUpdateFindingsFiltersDescriptionTypeDef):
    pass


_ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersFirstObservedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersFirstObservedAtTypeDef(
    _ClientUpdateFindingsFiltersFirstObservedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersGeneratorIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersGeneratorIdTypeDef(_ClientUpdateFindingsFiltersGeneratorIdTypeDef):
    pass


_ClientUpdateFindingsFiltersIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersIdTypeDef(_ClientUpdateFindingsFiltersIdTypeDef):
    pass


_ClientUpdateFindingsFiltersKeywordTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersKeywordTypeDef", {"Value": str}, total=False
)


class ClientUpdateFindingsFiltersKeywordTypeDef(_ClientUpdateFindingsFiltersKeywordTypeDef):
    pass


_ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersLastObservedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersLastObservedAtTypeDef(
    _ClientUpdateFindingsFiltersLastObservedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersMalwareNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersMalwareNameTypeDef(_ClientUpdateFindingsFiltersMalwareNameTypeDef):
    pass


_ClientUpdateFindingsFiltersMalwarePathTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersMalwarePathTypeDef(_ClientUpdateFindingsFiltersMalwarePathTypeDef):
    pass


_ClientUpdateFindingsFiltersMalwareStateTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersMalwareStateTypeDef(
    _ClientUpdateFindingsFiltersMalwareStateTypeDef
):
    pass


_ClientUpdateFindingsFiltersMalwareTypeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersMalwareTypeTypeDef(_ClientUpdateFindingsFiltersMalwareTypeTypeDef):
    pass


_ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef(
    _ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef(
    _ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef(
    _ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef(
    _ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkDirectionTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersNetworkDirectionTypeDef(
    _ClientUpdateFindingsFiltersNetworkDirectionTypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkProtocolTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersNetworkProtocolTypeDef(
    _ClientUpdateFindingsFiltersNetworkProtocolTypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef(
    _ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef(
    _ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef(
    _ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkSourceMacTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersNetworkSourceMacTypeDef(
    _ClientUpdateFindingsFiltersNetworkSourceMacTypeDef
):
    pass


_ClientUpdateFindingsFiltersNetworkSourcePortTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateFindingsFiltersNetworkSourcePortTypeDef(
    _ClientUpdateFindingsFiltersNetworkSourcePortTypeDef
):
    pass


_ClientUpdateFindingsFiltersNoteTextTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersNoteTextTypeDef(_ClientUpdateFindingsFiltersNoteTextTypeDef):
    pass


_ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef(
    _ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersNoteUpdatedByTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersNoteUpdatedByTypeDef(
    _ClientUpdateFindingsFiltersNoteUpdatedByTypeDef
):
    pass


_ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef(
    _ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersProcessNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersProcessNameTypeDef(_ClientUpdateFindingsFiltersProcessNameTypeDef):
    pass


_ClientUpdateFindingsFiltersProcessParentPidTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateFindingsFiltersProcessParentPidTypeDef(
    _ClientUpdateFindingsFiltersProcessParentPidTypeDef
):
    pass


_ClientUpdateFindingsFiltersProcessPathTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersProcessPathTypeDef(_ClientUpdateFindingsFiltersProcessPathTypeDef):
    pass


_ClientUpdateFindingsFiltersProcessPidTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateFindingsFiltersProcessPidTypeDef(_ClientUpdateFindingsFiltersProcessPidTypeDef):
    pass


_ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef(
    _ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersProductArnTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersProductArnTypeDef(_ClientUpdateFindingsFiltersProductArnTypeDef):
    """
    - *(dict) --*

      A string filter for querying findings.
      - **Value** *(string) --*

        The string filter value.
    """


_ClientUpdateFindingsFiltersProductFieldsTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientUpdateFindingsFiltersProductFieldsTypeDef(
    _ClientUpdateFindingsFiltersProductFieldsTypeDef
):
    pass


_ClientUpdateFindingsFiltersProductNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersProductNameTypeDef(_ClientUpdateFindingsFiltersProductNameTypeDef):
    pass


_ClientUpdateFindingsFiltersRecommendationTextTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersRecommendationTextTypeDef(
    _ClientUpdateFindingsFiltersRecommendationTextTypeDef
):
    pass


_ClientUpdateFindingsFiltersRecordStateTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersRecordStateTypeDef(_ClientUpdateFindingsFiltersRecordStateTypeDef):
    pass


_ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef(
    _ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef
):
    pass


_ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef(
    _ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef(
    _ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef(
    _ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef(
    _ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef(
    _ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceContainerNameTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceContainerNameTypeDef(
    _ClientUpdateFindingsFiltersResourceContainerNameTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef(
    _ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceIdTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceIdTypeDef(_ClientUpdateFindingsFiltersResourceIdTypeDef):
    pass


_ClientUpdateFindingsFiltersResourcePartitionTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourcePartitionTypeDef(
    _ClientUpdateFindingsFiltersResourcePartitionTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceRegionTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceRegionTypeDef(
    _ClientUpdateFindingsFiltersResourceRegionTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceTagsTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientUpdateFindingsFiltersResourceTagsTypeDef(
    _ClientUpdateFindingsFiltersResourceTagsTypeDef
):
    pass


_ClientUpdateFindingsFiltersResourceTypeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersResourceTypeTypeDef(
    _ClientUpdateFindingsFiltersResourceTypeTypeDef
):
    pass


_ClientUpdateFindingsFiltersSeverityLabelTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersSeverityLabelTypeDef(
    _ClientUpdateFindingsFiltersSeverityLabelTypeDef
):
    pass


_ClientUpdateFindingsFiltersSeverityNormalizedTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateFindingsFiltersSeverityNormalizedTypeDef(
    _ClientUpdateFindingsFiltersSeverityNormalizedTypeDef
):
    pass


_ClientUpdateFindingsFiltersSeverityProductTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateFindingsFiltersSeverityProductTypeDef(
    _ClientUpdateFindingsFiltersSeverityProductTypeDef
):
    pass


_ClientUpdateFindingsFiltersSourceUrlTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersSourceUrlTypeDef(_ClientUpdateFindingsFiltersSourceUrlTypeDef):
    pass


_ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef(
    _ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef
):
    pass


_ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef(
    _ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef
):
    pass


_ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef(
    _ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef
):
    pass


_ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef(
    _ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef
):
    pass


_ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef(
    _ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef
):
    pass


_ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef(
    _ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef
):
    pass


_ClientUpdateFindingsFiltersTitleTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersTitleTypeDef(_ClientUpdateFindingsFiltersTitleTypeDef):
    pass


_ClientUpdateFindingsFiltersTypeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersTypeTypeDef(_ClientUpdateFindingsFiltersTypeTypeDef):
    pass


_ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef(
    _ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef
):
    pass


_ClientUpdateFindingsFiltersUpdatedAtTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)


class ClientUpdateFindingsFiltersUpdatedAtTypeDef(_ClientUpdateFindingsFiltersUpdatedAtTypeDef):
    pass


_ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef(
    _ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef
):
    pass


_ClientUpdateFindingsFiltersVerificationStateTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersVerificationStateTypeDef(
    _ClientUpdateFindingsFiltersVerificationStateTypeDef
):
    pass


_ClientUpdateFindingsFiltersWorkflowStateTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateFindingsFiltersWorkflowStateTypeDef(
    _ClientUpdateFindingsFiltersWorkflowStateTypeDef
):
    pass


_ClientUpdateFindingsFiltersTypeDef = TypedDict(
    "_ClientUpdateFindingsFiltersTypeDef",
    {
        "ProductArn": List[ClientUpdateFindingsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientUpdateFindingsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientUpdateFindingsFiltersIdTypeDef],
        "GeneratorId": List[ClientUpdateFindingsFiltersGeneratorIdTypeDef],
        "Type": List[ClientUpdateFindingsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientUpdateFindingsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientUpdateFindingsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientUpdateFindingsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientUpdateFindingsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientUpdateFindingsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientUpdateFindingsFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientUpdateFindingsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientUpdateFindingsFiltersConfidenceTypeDef],
        "Criticality": List[ClientUpdateFindingsFiltersCriticalityTypeDef],
        "Title": List[ClientUpdateFindingsFiltersTitleTypeDef],
        "Description": List[ClientUpdateFindingsFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientUpdateFindingsFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientUpdateFindingsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientUpdateFindingsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientUpdateFindingsFiltersProductNameTypeDef],
        "CompanyName": List[ClientUpdateFindingsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientUpdateFindingsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientUpdateFindingsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientUpdateFindingsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientUpdateFindingsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientUpdateFindingsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientUpdateFindingsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientUpdateFindingsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientUpdateFindingsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[
            ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef
        ],
        "ProcessName": List[ClientUpdateFindingsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientUpdateFindingsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientUpdateFindingsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientUpdateFindingsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef
        ],
        "ThreatIntelIndicatorValue": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientUpdateFindingsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientUpdateFindingsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientUpdateFindingsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientUpdateFindingsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientUpdateFindingsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientUpdateFindingsFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[
            ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef
        ],
        "ResourceContainerImageName": List[
            ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientUpdateFindingsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientUpdateFindingsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientUpdateFindingsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientUpdateFindingsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientUpdateFindingsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientUpdateFindingsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientUpdateFindingsFiltersKeywordTypeDef],
    },
    total=False,
)


class ClientUpdateFindingsFiltersTypeDef(_ClientUpdateFindingsFiltersTypeDef):
    """
    A collection of attributes that specify which findings you want to update.
    - **ProductArn** *(list) --*

      The ARN generated by Security Hub that uniquely identifies a third-party company (security
      findings provider) after this provider's product (solution that generates findings) is
      registered with Security Hub.
      - *(dict) --*

        A string filter for querying findings.
        - **Value** *(string) --*

          The string filter value.
    """


_RequiredClientUpdateFindingsNoteTypeDef = TypedDict(
    "_RequiredClientUpdateFindingsNoteTypeDef", {"Text": str}
)
_OptionalClientUpdateFindingsNoteTypeDef = TypedDict(
    "_OptionalClientUpdateFindingsNoteTypeDef", {"UpdatedBy": str}, total=False
)


class ClientUpdateFindingsNoteTypeDef(
    _RequiredClientUpdateFindingsNoteTypeDef, _OptionalClientUpdateFindingsNoteTypeDef
):
    """
    The updated note for the finding.
    - **Text** *(string) --***[REQUIRED]**

      The updated note text.
    """


_ClientUpdateInsightFiltersAwsAccountIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersAwsAccountIdTypeDef(_ClientUpdateInsightFiltersAwsAccountIdTypeDef):
    pass


_ClientUpdateInsightFiltersCompanyNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersCompanyNameTypeDef(_ClientUpdateInsightFiltersCompanyNameTypeDef):
    pass


_ClientUpdateInsightFiltersComplianceStatusTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersComplianceStatusTypeDef(
    _ClientUpdateInsightFiltersComplianceStatusTypeDef
):
    pass


_ClientUpdateInsightFiltersConfidenceTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateInsightFiltersConfidenceTypeDef(_ClientUpdateInsightFiltersConfidenceTypeDef):
    pass


_ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)


class ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersCreatedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef},
    total=False,
)


class ClientUpdateInsightFiltersCreatedAtTypeDef(_ClientUpdateInsightFiltersCreatedAtTypeDef):
    pass


_ClientUpdateInsightFiltersCriticalityTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateInsightFiltersCriticalityTypeDef(_ClientUpdateInsightFiltersCriticalityTypeDef):
    pass


_ClientUpdateInsightFiltersDescriptionTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersDescriptionTypeDef(_ClientUpdateInsightFiltersDescriptionTypeDef):
    pass


_ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersFirstObservedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersFirstObservedAtTypeDef(
    _ClientUpdateInsightFiltersFirstObservedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersGeneratorIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersGeneratorIdTypeDef(_ClientUpdateInsightFiltersGeneratorIdTypeDef):
    pass


_ClientUpdateInsightFiltersIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersIdTypeDef(_ClientUpdateInsightFiltersIdTypeDef):
    pass


_ClientUpdateInsightFiltersKeywordTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersKeywordTypeDef", {"Value": str}, total=False
)


class ClientUpdateInsightFiltersKeywordTypeDef(_ClientUpdateInsightFiltersKeywordTypeDef):
    pass


_ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersLastObservedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersLastObservedAtTypeDef(
    _ClientUpdateInsightFiltersLastObservedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersMalwareNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersMalwareNameTypeDef(_ClientUpdateInsightFiltersMalwareNameTypeDef):
    pass


_ClientUpdateInsightFiltersMalwarePathTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersMalwarePathTypeDef(_ClientUpdateInsightFiltersMalwarePathTypeDef):
    pass


_ClientUpdateInsightFiltersMalwareStateTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersMalwareStateTypeDef(_ClientUpdateInsightFiltersMalwareStateTypeDef):
    pass


_ClientUpdateInsightFiltersMalwareTypeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersMalwareTypeTypeDef(_ClientUpdateInsightFiltersMalwareTypeTypeDef):
    pass


_ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef(
    _ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef(
    _ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef(
    _ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkDestinationPortTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateInsightFiltersNetworkDestinationPortTypeDef(
    _ClientUpdateInsightFiltersNetworkDestinationPortTypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkDirectionTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersNetworkDirectionTypeDef(
    _ClientUpdateInsightFiltersNetworkDirectionTypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkProtocolTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersNetworkProtocolTypeDef(
    _ClientUpdateInsightFiltersNetworkProtocolTypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkSourceDomainTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersNetworkSourceDomainTypeDef(
    _ClientUpdateInsightFiltersNetworkSourceDomainTypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)


class ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef(
    _ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)


class ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef(
    _ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkSourceMacTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersNetworkSourceMacTypeDef(
    _ClientUpdateInsightFiltersNetworkSourceMacTypeDef
):
    pass


_ClientUpdateInsightFiltersNetworkSourcePortTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateInsightFiltersNetworkSourcePortTypeDef(
    _ClientUpdateInsightFiltersNetworkSourcePortTypeDef
):
    pass


_ClientUpdateInsightFiltersNoteTextTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersNoteTextTypeDef(_ClientUpdateInsightFiltersNoteTextTypeDef):
    pass


_ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersNoteUpdatedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersNoteUpdatedAtTypeDef(
    _ClientUpdateInsightFiltersNoteUpdatedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersNoteUpdatedByTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersNoteUpdatedByTypeDef(
    _ClientUpdateInsightFiltersNoteUpdatedByTypeDef
):
    pass


_ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersProcessLaunchedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersProcessLaunchedAtTypeDef(
    _ClientUpdateInsightFiltersProcessLaunchedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersProcessNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersProcessNameTypeDef(_ClientUpdateInsightFiltersProcessNameTypeDef):
    pass


_ClientUpdateInsightFiltersProcessParentPidTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateInsightFiltersProcessParentPidTypeDef(
    _ClientUpdateInsightFiltersProcessParentPidTypeDef
):
    pass


_ClientUpdateInsightFiltersProcessPathTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersProcessPathTypeDef(_ClientUpdateInsightFiltersProcessPathTypeDef):
    pass


_ClientUpdateInsightFiltersProcessPidTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateInsightFiltersProcessPidTypeDef(_ClientUpdateInsightFiltersProcessPidTypeDef):
    pass


_ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersProcessTerminatedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersProcessTerminatedAtTypeDef(
    _ClientUpdateInsightFiltersProcessTerminatedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersProductArnTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersProductArnTypeDef(_ClientUpdateInsightFiltersProductArnTypeDef):
    """
    - *(dict) --*

      A string filter for querying findings.
      - **Value** *(string) --*

        The string filter value.
    """


_ClientUpdateInsightFiltersProductFieldsTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientUpdateInsightFiltersProductFieldsTypeDef(
    _ClientUpdateInsightFiltersProductFieldsTypeDef
):
    pass


_ClientUpdateInsightFiltersProductNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersProductNameTypeDef(_ClientUpdateInsightFiltersProductNameTypeDef):
    pass


_ClientUpdateInsightFiltersRecommendationTextTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersRecommendationTextTypeDef(
    _ClientUpdateInsightFiltersRecommendationTextTypeDef
):
    pass


_ClientUpdateInsightFiltersRecordStateTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersRecordStateTypeDef(_ClientUpdateInsightFiltersRecordStateTypeDef):
    pass


_ClientUpdateInsightFiltersRelatedFindingsIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersRelatedFindingsIdTypeDef(
    _ClientUpdateInsightFiltersRelatedFindingsIdTypeDef
):
    pass


_ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef(
    _ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef(
    _ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef(
    _ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef(
    _ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef(
    _ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef(
    _ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef(
    _ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceContainerImageIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceContainerImageIdTypeDef(
    _ClientUpdateInsightFiltersResourceContainerImageIdTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceContainerImageNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceContainerImageNameTypeDef(
    _ClientUpdateInsightFiltersResourceContainerImageNameTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef(
    _ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceContainerNameTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceContainerNameTypeDef(
    _ClientUpdateInsightFiltersResourceContainerNameTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceDetailsOtherTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientUpdateInsightFiltersResourceDetailsOtherTypeDef(
    _ClientUpdateInsightFiltersResourceDetailsOtherTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceIdTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceIdTypeDef(_ClientUpdateInsightFiltersResourceIdTypeDef):
    pass


_ClientUpdateInsightFiltersResourcePartitionTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourcePartitionTypeDef(
    _ClientUpdateInsightFiltersResourcePartitionTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceRegionTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceRegionTypeDef(
    _ClientUpdateInsightFiltersResourceRegionTypeDef
):
    pass


_ClientUpdateInsightFiltersResourceTagsTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientUpdateInsightFiltersResourceTagsTypeDef(_ClientUpdateInsightFiltersResourceTagsTypeDef):
    pass


_ClientUpdateInsightFiltersResourceTypeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersResourceTypeTypeDef(_ClientUpdateInsightFiltersResourceTypeTypeDef):
    pass


_ClientUpdateInsightFiltersSeverityLabelTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersSeverityLabelTypeDef(
    _ClientUpdateInsightFiltersSeverityLabelTypeDef
):
    pass


_ClientUpdateInsightFiltersSeverityNormalizedTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateInsightFiltersSeverityNormalizedTypeDef(
    _ClientUpdateInsightFiltersSeverityNormalizedTypeDef
):
    pass


_ClientUpdateInsightFiltersSeverityProductTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class ClientUpdateInsightFiltersSeverityProductTypeDef(
    _ClientUpdateInsightFiltersSeverityProductTypeDef
):
    pass


_ClientUpdateInsightFiltersSourceUrlTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersSourceUrlTypeDef(_ClientUpdateInsightFiltersSourceUrlTypeDef):
    pass


_ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef(
    _ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef
):
    pass


_ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef(
    _ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef
):
    pass


_ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef(
    _ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef
):
    pass


_ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef(
    _ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef
):
    pass


_ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef(
    _ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef
):
    pass


_ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef(
    _ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef
):
    pass


_ClientUpdateInsightFiltersTitleTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersTitleTypeDef(_ClientUpdateInsightFiltersTitleTypeDef):
    pass


_ClientUpdateInsightFiltersTypeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersTypeTypeDef(_ClientUpdateInsightFiltersTypeTypeDef):
    pass


_ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)


class ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef(
    _ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef
):
    pass


_ClientUpdateInsightFiltersUpdatedAtTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)


class ClientUpdateInsightFiltersUpdatedAtTypeDef(_ClientUpdateInsightFiltersUpdatedAtTypeDef):
    pass


_ClientUpdateInsightFiltersUserDefinedFieldsTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class ClientUpdateInsightFiltersUserDefinedFieldsTypeDef(
    _ClientUpdateInsightFiltersUserDefinedFieldsTypeDef
):
    pass


_ClientUpdateInsightFiltersVerificationStateTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersVerificationStateTypeDef(
    _ClientUpdateInsightFiltersVerificationStateTypeDef
):
    pass


_ClientUpdateInsightFiltersWorkflowStateTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class ClientUpdateInsightFiltersWorkflowStateTypeDef(
    _ClientUpdateInsightFiltersWorkflowStateTypeDef
):
    pass


_ClientUpdateInsightFiltersTypeDef = TypedDict(
    "_ClientUpdateInsightFiltersTypeDef",
    {
        "ProductArn": List[ClientUpdateInsightFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientUpdateInsightFiltersAwsAccountIdTypeDef],
        "Id": List[ClientUpdateInsightFiltersIdTypeDef],
        "GeneratorId": List[ClientUpdateInsightFiltersGeneratorIdTypeDef],
        "Type": List[ClientUpdateInsightFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientUpdateInsightFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientUpdateInsightFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientUpdateInsightFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientUpdateInsightFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientUpdateInsightFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientUpdateInsightFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientUpdateInsightFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientUpdateInsightFiltersConfidenceTypeDef],
        "Criticality": List[ClientUpdateInsightFiltersCriticalityTypeDef],
        "Title": List[ClientUpdateInsightFiltersTitleTypeDef],
        "Description": List[ClientUpdateInsightFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientUpdateInsightFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientUpdateInsightFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientUpdateInsightFiltersProductFieldsTypeDef],
        "ProductName": List[ClientUpdateInsightFiltersProductNameTypeDef],
        "CompanyName": List[ClientUpdateInsightFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientUpdateInsightFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientUpdateInsightFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientUpdateInsightFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientUpdateInsightFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientUpdateInsightFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientUpdateInsightFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientUpdateInsightFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientUpdateInsightFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientUpdateInsightFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientUpdateInsightFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientUpdateInsightFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientUpdateInsightFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientUpdateInsightFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientUpdateInsightFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientUpdateInsightFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientUpdateInsightFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientUpdateInsightFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientUpdateInsightFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientUpdateInsightFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientUpdateInsightFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientUpdateInsightFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientUpdateInsightFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientUpdateInsightFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientUpdateInsightFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientUpdateInsightFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientUpdateInsightFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientUpdateInsightFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientUpdateInsightFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientUpdateInsightFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientUpdateInsightFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientUpdateInsightFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientUpdateInsightFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientUpdateInsightFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientUpdateInsightFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientUpdateInsightFiltersKeywordTypeDef],
    },
    total=False,
)


class ClientUpdateInsightFiltersTypeDef(_ClientUpdateInsightFiltersTypeDef):
    """
    The updated filters that define this insight.
    - **ProductArn** *(list) --*

      The ARN generated by Security Hub that uniquely identifies a third-party company (security
      findings provider) after this provider's product (solution that generates findings) is
      registered with Security Hub.
      - *(dict) --*

        A string filter for querying findings.
        - **Value** *(string) --*

          The string filter value.
    """


_GetEnabledStandardsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetEnabledStandardsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetEnabledStandardsPaginatePaginationConfigTypeDef(
    _GetEnabledStandardsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef = TypedDict(
    "_GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)


class GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef(
    _GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef
):
    """
    - *(dict) --*

      A resource that represents your subscription to a supported standard.
      - **StandardsSubscriptionArn** *(string) --*

        The ARN of a resource that represents your subscription to a supported standard.
    """


_GetEnabledStandardsPaginateResponseTypeDef = TypedDict(
    "_GetEnabledStandardsPaginateResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef
        ]
    },
    total=False,
)


class GetEnabledStandardsPaginateResponseTypeDef(_GetEnabledStandardsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **StandardsSubscriptions** *(list) --*

        A list of ``StandardsSubscriptions`` objects that include information about the enabled
        standards.
        - *(dict) --*

          A resource that represents your subscription to a supported standard.
          - **StandardsSubscriptionArn** *(string) --*

            The ARN of a resource that represents your subscription to a supported standard.
    """


_GetFindingsPaginateFiltersAwsAccountIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersAwsAccountIdTypeDef(_GetFindingsPaginateFiltersAwsAccountIdTypeDef):
    pass


_GetFindingsPaginateFiltersCompanyNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersCompanyNameTypeDef(_GetFindingsPaginateFiltersCompanyNameTypeDef):
    pass


_GetFindingsPaginateFiltersComplianceStatusTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersComplianceStatusTypeDef(
    _GetFindingsPaginateFiltersComplianceStatusTypeDef
):
    pass


_GetFindingsPaginateFiltersConfidenceTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetFindingsPaginateFiltersConfidenceTypeDef(_GetFindingsPaginateFiltersConfidenceTypeDef):
    pass


_GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)


class GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersCreatedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef},
    total=False,
)


class GetFindingsPaginateFiltersCreatedAtTypeDef(_GetFindingsPaginateFiltersCreatedAtTypeDef):
    pass


_GetFindingsPaginateFiltersCriticalityTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetFindingsPaginateFiltersCriticalityTypeDef(_GetFindingsPaginateFiltersCriticalityTypeDef):
    pass


_GetFindingsPaginateFiltersDescriptionTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersDescriptionTypeDef(_GetFindingsPaginateFiltersDescriptionTypeDef):
    pass


_GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersFirstObservedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersFirstObservedAtTypeDef(
    _GetFindingsPaginateFiltersFirstObservedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersGeneratorIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersGeneratorIdTypeDef(_GetFindingsPaginateFiltersGeneratorIdTypeDef):
    pass


_GetFindingsPaginateFiltersIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersIdTypeDef(_GetFindingsPaginateFiltersIdTypeDef):
    pass


_GetFindingsPaginateFiltersKeywordTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersKeywordTypeDef", {"Value": str}, total=False
)


class GetFindingsPaginateFiltersKeywordTypeDef(_GetFindingsPaginateFiltersKeywordTypeDef):
    pass


_GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersLastObservedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersLastObservedAtTypeDef(
    _GetFindingsPaginateFiltersLastObservedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersMalwareNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersMalwareNameTypeDef(_GetFindingsPaginateFiltersMalwareNameTypeDef):
    pass


_GetFindingsPaginateFiltersMalwarePathTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersMalwarePathTypeDef(_GetFindingsPaginateFiltersMalwarePathTypeDef):
    pass


_GetFindingsPaginateFiltersMalwareStateTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersMalwareStateTypeDef(_GetFindingsPaginateFiltersMalwareStateTypeDef):
    pass


_GetFindingsPaginateFiltersMalwareTypeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersMalwareTypeTypeDef(_GetFindingsPaginateFiltersMalwareTypeTypeDef):
    pass


_GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef(
    _GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)


class GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef(
    _GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)


class GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef(
    _GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkDestinationPortTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetFindingsPaginateFiltersNetworkDestinationPortTypeDef(
    _GetFindingsPaginateFiltersNetworkDestinationPortTypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkDirectionTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersNetworkDirectionTypeDef(
    _GetFindingsPaginateFiltersNetworkDirectionTypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkProtocolTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersNetworkProtocolTypeDef(
    _GetFindingsPaginateFiltersNetworkProtocolTypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkSourceDomainTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersNetworkSourceDomainTypeDef(
    _GetFindingsPaginateFiltersNetworkSourceDomainTypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)


class GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef(
    _GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)


class GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef(
    _GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkSourceMacTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersNetworkSourceMacTypeDef(
    _GetFindingsPaginateFiltersNetworkSourceMacTypeDef
):
    pass


_GetFindingsPaginateFiltersNetworkSourcePortTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetFindingsPaginateFiltersNetworkSourcePortTypeDef(
    _GetFindingsPaginateFiltersNetworkSourcePortTypeDef
):
    pass


_GetFindingsPaginateFiltersNoteTextTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersNoteTextTypeDef(_GetFindingsPaginateFiltersNoteTextTypeDef):
    pass


_GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersNoteUpdatedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersNoteUpdatedAtTypeDef(
    _GetFindingsPaginateFiltersNoteUpdatedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersNoteUpdatedByTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersNoteUpdatedByTypeDef(
    _GetFindingsPaginateFiltersNoteUpdatedByTypeDef
):
    pass


_GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersProcessLaunchedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersProcessLaunchedAtTypeDef(
    _GetFindingsPaginateFiltersProcessLaunchedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersProcessNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersProcessNameTypeDef(_GetFindingsPaginateFiltersProcessNameTypeDef):
    pass


_GetFindingsPaginateFiltersProcessParentPidTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetFindingsPaginateFiltersProcessParentPidTypeDef(
    _GetFindingsPaginateFiltersProcessParentPidTypeDef
):
    pass


_GetFindingsPaginateFiltersProcessPathTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersProcessPathTypeDef(_GetFindingsPaginateFiltersProcessPathTypeDef):
    pass


_GetFindingsPaginateFiltersProcessPidTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetFindingsPaginateFiltersProcessPidTypeDef(_GetFindingsPaginateFiltersProcessPidTypeDef):
    pass


_GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersProcessTerminatedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersProcessTerminatedAtTypeDef(
    _GetFindingsPaginateFiltersProcessTerminatedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersProductArnTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersProductArnTypeDef(_GetFindingsPaginateFiltersProductArnTypeDef):
    """
    - *(dict) --*

      A string filter for querying findings.
      - **Value** *(string) --*

        The string filter value.
    """


_GetFindingsPaginateFiltersProductFieldsTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class GetFindingsPaginateFiltersProductFieldsTypeDef(
    _GetFindingsPaginateFiltersProductFieldsTypeDef
):
    pass


_GetFindingsPaginateFiltersProductNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersProductNameTypeDef(_GetFindingsPaginateFiltersProductNameTypeDef):
    pass


_GetFindingsPaginateFiltersRecommendationTextTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersRecommendationTextTypeDef(
    _GetFindingsPaginateFiltersRecommendationTextTypeDef
):
    pass


_GetFindingsPaginateFiltersRecordStateTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersRecordStateTypeDef(_GetFindingsPaginateFiltersRecordStateTypeDef):
    pass


_GetFindingsPaginateFiltersRelatedFindingsIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersRelatedFindingsIdTypeDef(
    _GetFindingsPaginateFiltersRelatedFindingsIdTypeDef
):
    pass


_GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef(
    _GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef(
    _GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef(
    _GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef(
    _GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef(
    _GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef(
    _GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef(
    _GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceContainerImageIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceContainerImageIdTypeDef(
    _GetFindingsPaginateFiltersResourceContainerImageIdTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceContainerImageNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceContainerImageNameTypeDef(
    _GetFindingsPaginateFiltersResourceContainerImageNameTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef(
    _GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceContainerNameTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceContainerNameTypeDef(
    _GetFindingsPaginateFiltersResourceContainerNameTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceDetailsOtherTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class GetFindingsPaginateFiltersResourceDetailsOtherTypeDef(
    _GetFindingsPaginateFiltersResourceDetailsOtherTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceIdTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceIdTypeDef(_GetFindingsPaginateFiltersResourceIdTypeDef):
    pass


_GetFindingsPaginateFiltersResourcePartitionTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourcePartitionTypeDef(
    _GetFindingsPaginateFiltersResourcePartitionTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceRegionTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceRegionTypeDef(
    _GetFindingsPaginateFiltersResourceRegionTypeDef
):
    pass


_GetFindingsPaginateFiltersResourceTagsTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class GetFindingsPaginateFiltersResourceTagsTypeDef(_GetFindingsPaginateFiltersResourceTagsTypeDef):
    pass


_GetFindingsPaginateFiltersResourceTypeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersResourceTypeTypeDef(_GetFindingsPaginateFiltersResourceTypeTypeDef):
    pass


_GetFindingsPaginateFiltersSeverityLabelTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersSeverityLabelTypeDef(
    _GetFindingsPaginateFiltersSeverityLabelTypeDef
):
    pass


_GetFindingsPaginateFiltersSeverityNormalizedTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetFindingsPaginateFiltersSeverityNormalizedTypeDef(
    _GetFindingsPaginateFiltersSeverityNormalizedTypeDef
):
    pass


_GetFindingsPaginateFiltersSeverityProductTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetFindingsPaginateFiltersSeverityProductTypeDef(
    _GetFindingsPaginateFiltersSeverityProductTypeDef
):
    pass


_GetFindingsPaginateFiltersSourceUrlTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersSourceUrlTypeDef(_GetFindingsPaginateFiltersSourceUrlTypeDef):
    pass


_GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef(
    _GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef
):
    pass


_GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef(
    _GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef
):
    pass


_GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef(
    _GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef
):
    pass


_GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef(
    _GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef
):
    pass


_GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef(
    _GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef
):
    pass


_GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef(
    _GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef
):
    pass


_GetFindingsPaginateFiltersTitleTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersTitleTypeDef(_GetFindingsPaginateFiltersTitleTypeDef):
    pass


_GetFindingsPaginateFiltersTypeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersTypeTypeDef(_GetFindingsPaginateFiltersTypeTypeDef):
    pass


_GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)


class GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef(
    _GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef
):
    pass


_GetFindingsPaginateFiltersUpdatedAtTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)


class GetFindingsPaginateFiltersUpdatedAtTypeDef(_GetFindingsPaginateFiltersUpdatedAtTypeDef):
    pass


_GetFindingsPaginateFiltersUserDefinedFieldsTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class GetFindingsPaginateFiltersUserDefinedFieldsTypeDef(
    _GetFindingsPaginateFiltersUserDefinedFieldsTypeDef
):
    pass


_GetFindingsPaginateFiltersVerificationStateTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersVerificationStateTypeDef(
    _GetFindingsPaginateFiltersVerificationStateTypeDef
):
    pass


_GetFindingsPaginateFiltersWorkflowStateTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetFindingsPaginateFiltersWorkflowStateTypeDef(
    _GetFindingsPaginateFiltersWorkflowStateTypeDef
):
    pass


_GetFindingsPaginateFiltersTypeDef = TypedDict(
    "_GetFindingsPaginateFiltersTypeDef",
    {
        "ProductArn": List[GetFindingsPaginateFiltersProductArnTypeDef],
        "AwsAccountId": List[GetFindingsPaginateFiltersAwsAccountIdTypeDef],
        "Id": List[GetFindingsPaginateFiltersIdTypeDef],
        "GeneratorId": List[GetFindingsPaginateFiltersGeneratorIdTypeDef],
        "Type": List[GetFindingsPaginateFiltersTypeTypeDef],
        "FirstObservedAt": List[GetFindingsPaginateFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[GetFindingsPaginateFiltersLastObservedAtTypeDef],
        "CreatedAt": List[GetFindingsPaginateFiltersCreatedAtTypeDef],
        "UpdatedAt": List[GetFindingsPaginateFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[GetFindingsPaginateFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[GetFindingsPaginateFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[GetFindingsPaginateFiltersSeverityLabelTypeDef],
        "Confidence": List[GetFindingsPaginateFiltersConfidenceTypeDef],
        "Criticality": List[GetFindingsPaginateFiltersCriticalityTypeDef],
        "Title": List[GetFindingsPaginateFiltersTitleTypeDef],
        "Description": List[GetFindingsPaginateFiltersDescriptionTypeDef],
        "RecommendationText": List[GetFindingsPaginateFiltersRecommendationTextTypeDef],
        "SourceUrl": List[GetFindingsPaginateFiltersSourceUrlTypeDef],
        "ProductFields": List[GetFindingsPaginateFiltersProductFieldsTypeDef],
        "ProductName": List[GetFindingsPaginateFiltersProductNameTypeDef],
        "CompanyName": List[GetFindingsPaginateFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[GetFindingsPaginateFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[GetFindingsPaginateFiltersMalwareNameTypeDef],
        "MalwareType": List[GetFindingsPaginateFiltersMalwareTypeTypeDef],
        "MalwarePath": List[GetFindingsPaginateFiltersMalwarePathTypeDef],
        "MalwareState": List[GetFindingsPaginateFiltersMalwareStateTypeDef],
        "NetworkDirection": List[GetFindingsPaginateFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[GetFindingsPaginateFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[GetFindingsPaginateFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[GetFindingsPaginateFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[GetFindingsPaginateFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[GetFindingsPaginateFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[GetFindingsPaginateFiltersProcessNameTypeDef],
        "ProcessPath": List[GetFindingsPaginateFiltersProcessPathTypeDef],
        "ProcessPid": List[GetFindingsPaginateFiltersProcessPidTypeDef],
        "ProcessParentPid": List[GetFindingsPaginateFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[GetFindingsPaginateFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[GetFindingsPaginateFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[GetFindingsPaginateFiltersResourceTypeTypeDef],
        "ResourceId": List[GetFindingsPaginateFiltersResourceIdTypeDef],
        "ResourcePartition": List[GetFindingsPaginateFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[GetFindingsPaginateFiltersResourceRegionTypeDef],
        "ResourceTags": List[GetFindingsPaginateFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[GetFindingsPaginateFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[GetFindingsPaginateFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            GetFindingsPaginateFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[GetFindingsPaginateFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[GetFindingsPaginateFiltersComplianceStatusTypeDef],
        "VerificationState": List[GetFindingsPaginateFiltersVerificationStateTypeDef],
        "WorkflowState": List[GetFindingsPaginateFiltersWorkflowStateTypeDef],
        "RecordState": List[GetFindingsPaginateFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[GetFindingsPaginateFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[GetFindingsPaginateFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[GetFindingsPaginateFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[GetFindingsPaginateFiltersNoteUpdatedByTypeDef],
        "Keyword": List[GetFindingsPaginateFiltersKeywordTypeDef],
    },
    total=False,
)


class GetFindingsPaginateFiltersTypeDef(_GetFindingsPaginateFiltersTypeDef):
    """
    The findings attributes used to define a condition to filter the findings returned.
    - **ProductArn** *(list) --*

      The ARN generated by Security Hub that uniquely identifies a third-party company (security
      findings provider) after this provider's product (solution that generates findings) is
      registered with Security Hub.
      - *(dict) --*

        A string filter for querying findings.
        - **Value** *(string) --*

          The string filter value.
    """


_GetFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetFindingsPaginatePaginationConfigTypeDef(_GetFindingsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetFindingsPaginateResponseFindingsComplianceTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsComplianceTypeDef",
    {"Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"]},
    total=False,
)


class GetFindingsPaginateResponseFindingsComplianceTypeDef(
    _GetFindingsPaginateResponseFindingsComplianceTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsMalwareTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsMalwareTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)


class GetFindingsPaginateResponseFindingsMalwareTypeDef(
    _GetFindingsPaginateResponseFindingsMalwareTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsNetworkTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsNetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)


class GetFindingsPaginateResponseFindingsNetworkTypeDef(
    _GetFindingsPaginateResponseFindingsNetworkTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsNoteTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsNoteTypeDef",
    {"Text": str, "UpdatedBy": str, "UpdatedAt": str},
    total=False,
)


class GetFindingsPaginateResponseFindingsNoteTypeDef(
    _GetFindingsPaginateResponseFindingsNoteTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsProcessTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsProcessTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)


class GetFindingsPaginateResponseFindingsProcessTypeDef(
    _GetFindingsPaginateResponseFindingsProcessTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef",
    {"ProductArn": str, "Id": str},
    total=False,
)


class GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef(
    _GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef",
    {"Text": str, "Url": str},
    total=False,
)


class GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef(
    _GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsRemediationTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsRemediationTypeDef",
    {"Recommendation": GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef},
    total=False,
)


class GetFindingsPaginateResponseFindingsRemediationTypeDef(
    _GetFindingsPaginateResponseFindingsRemediationTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)


class GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef(
    _GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    {"UserName": str, "Status": Literal["Active", "Inactive"], "CreatedAt": str},
    total=False,
)


class GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef(
    _GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef",
    {"OwnerId": str, "OwnerName": str},
    total=False,
)


class GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef(
    _GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)


class GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef(
    _GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef",
    {
        "AwsEc2Instance": GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef,
        "AwsS3Bucket": GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef,
        "AwsIamAccessKey": GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef,
        "Container": GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)


class GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef(
    _GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsResourcesTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef,
    },
    total=False,
)


class GetFindingsPaginateResponseFindingsResourcesTypeDef(
    _GetFindingsPaginateResponseFindingsResourcesTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsSeverityTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsSeverityTypeDef",
    {"Product": float, "Normalized": int},
    total=False,
)


class GetFindingsPaginateResponseFindingsSeverityTypeDef(
    _GetFindingsPaginateResponseFindingsSeverityTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)


class GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef(
    _GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef
):
    pass


_GetFindingsPaginateResponseFindingsTypeDef = TypedDict(
    "_GetFindingsPaginateResponseFindingsTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": GetFindingsPaginateResponseFindingsSeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": GetFindingsPaginateResponseFindingsRemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[GetFindingsPaginateResponseFindingsMalwareTypeDef],
        "Network": GetFindingsPaginateResponseFindingsNetworkTypeDef,
        "Process": GetFindingsPaginateResponseFindingsProcessTypeDef,
        "ThreatIntelIndicators": List[
            GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef
        ],
        "Resources": List[GetFindingsPaginateResponseFindingsResourcesTypeDef],
        "Compliance": GetFindingsPaginateResponseFindingsComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef],
        "Note": GetFindingsPaginateResponseFindingsNoteTypeDef,
    },
    total=False,
)


class GetFindingsPaginateResponseFindingsTypeDef(_GetFindingsPaginateResponseFindingsTypeDef):
    """
    - *(dict) --*

      Provides consistent format for the contents of the Security Hub-aggregated findings.
      ``AwsSecurityFinding`` format enables you to share findings between AWS security services and
      third-party solutions, and compliance checks.
      .. note::

        A finding is a potential security issue generated either by AWS services (Amazon GuardDuty,
        Amazon Inspector, and Amazon Macie) or by the integrated third-party solutions and
        compliance checks.
    """


_GetFindingsPaginateResponseTypeDef = TypedDict(
    "_GetFindingsPaginateResponseTypeDef",
    {"Findings": List[GetFindingsPaginateResponseFindingsTypeDef]},
    total=False,
)


class GetFindingsPaginateResponseTypeDef(_GetFindingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Findings** *(list) --*

        The findings that matched the filters specified in the request.
        - *(dict) --*

          Provides consistent format for the contents of the Security Hub-aggregated findings.
          ``AwsSecurityFinding`` format enables you to share findings between AWS security services
          and third-party solutions, and compliance checks.
          .. note::

            A finding is a potential security issue generated either by AWS services (Amazon
            GuardDuty, Amazon Inspector, and Amazon Macie) or by the integrated third-party
            solutions and compliance checks.
    """


_GetFindingsPaginateSortCriteriaTypeDef = TypedDict(
    "_GetFindingsPaginateSortCriteriaTypeDef",
    {"Field": str, "SortOrder": Literal["asc", "desc"]},
    total=False,
)


class GetFindingsPaginateSortCriteriaTypeDef(_GetFindingsPaginateSortCriteriaTypeDef):
    """
    - *(dict) --*

      A collection of finding attributes used to sort findings.
      - **Field** *(string) --*

        The finding attribute used to sort findings.
    """


_GetInsightsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetInsightsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetInsightsPaginatePaginationConfigTypeDef(_GetInsightsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef", {"Value": str}, total=False
)


class GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef",
    {"Cidr": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef",
    {"Cidr": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef",
    {"Cidr": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef",
    {"Cidr": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersTitleTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersTitleTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersTitleTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersTypeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersTypeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersTypeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsFiltersTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsFiltersTypeDef",
    {
        "ProductArn": List[GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef],
        "AwsAccountId": List[GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef],
        "Id": List[GetInsightsPaginateResponseInsightsFiltersIdTypeDef],
        "GeneratorId": List[GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef],
        "Type": List[GetInsightsPaginateResponseInsightsFiltersTypeTypeDef],
        "FirstObservedAt": List[GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[
            GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef
        ],
        "SeverityLabel": List[GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef],
        "Confidence": List[GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef],
        "Criticality": List[GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef],
        "Title": List[GetInsightsPaginateResponseInsightsFiltersTitleTypeDef],
        "Description": List[GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef],
        "RecommendationText": List[
            GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef
        ],
        "SourceUrl": List[GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef],
        "ProductFields": List[GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef],
        "ProductName": List[GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef],
        "CompanyName": List[GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[
            GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef
        ],
        "MalwareName": List[GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef],
        "MalwareType": List[GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef],
        "MalwareState": List[GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef
        ],
        "NetworkSourceIpV6": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef
        ],
        "NetworkSourcePort": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef
        ],
        "NetworkSourceDomain": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef
        ],
        "NetworkSourceMac": List[GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef
        ],
        "NetworkDestinationIpV6": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef
        ],
        "NetworkDestinationPort": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef
        ],
        "NetworkDestinationDomain": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef
        ],
        "ProcessName": List[GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef],
        "ProcessPath": List[GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef],
        "ProcessPid": List[GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[
            GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef
        ],
        "ProcessTerminatedAt": List[
            GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef
        ],
        "ThreatIntelIndicatorType": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef
        ],
        "ThreatIntelIndicatorValue": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef],
        "ResourceId": List[GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef],
        "ResourcePartition": List[
            GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef
        ],
        "ResourceRegion": List[GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef],
        "ResourceTags": List[GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef
        ],
        "ResourceContainerImageId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef
        ],
        "ResourceContainerImageName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[
            GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef
        ],
        "ComplianceStatus": List[GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef],
        "VerificationState": List[
            GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef
        ],
        "WorkflowState": List[GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef],
        "RecordState": List[GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[
            GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef
        ],
        "NoteText": List[GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef],
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsFiltersTypeDef(
    _GetInsightsPaginateResponseInsightsFiltersTypeDef
):
    pass


_GetInsightsPaginateResponseInsightsTypeDef = TypedDict(
    "_GetInsightsPaginateResponseInsightsTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": GetInsightsPaginateResponseInsightsFiltersTypeDef,
        "GroupByAttribute": str,
    },
    total=False,
)


class GetInsightsPaginateResponseInsightsTypeDef(_GetInsightsPaginateResponseInsightsTypeDef):
    """
    - *(dict) --*

      Contains information about a Security Hub insight.
      - **InsightArn** *(string) --*

        The ARN of a Security Hub insight.
    """


_GetInsightsPaginateResponseTypeDef = TypedDict(
    "_GetInsightsPaginateResponseTypeDef",
    {"Insights": List[GetInsightsPaginateResponseInsightsTypeDef]},
    total=False,
)


class GetInsightsPaginateResponseTypeDef(_GetInsightsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Insights** *(list) --*

        The insights returned by the operation.
        - *(dict) --*

          Contains information about a Security Hub insight.
          - **InsightArn** *(string) --*

            The ARN of a Security Hub insight.
    """


_ListEnabledProductsForImportPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEnabledProductsForImportPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEnabledProductsForImportPaginatePaginationConfigTypeDef(
    _ListEnabledProductsForImportPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEnabledProductsForImportPaginateResponseTypeDef = TypedDict(
    "_ListEnabledProductsForImportPaginateResponseTypeDef",
    {"ProductSubscriptions": List[str]},
    total=False,
)


class ListEnabledProductsForImportPaginateResponseTypeDef(
    _ListEnabledProductsForImportPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ProductSubscriptions** *(list) --*

        A list of ARNs for the resources that represent your subscriptions to products.
        - *(string) --*
    """


_ListInvitationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInvitationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInvitationsPaginatePaginationConfigTypeDef(
    _ListInvitationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInvitationsPaginateResponseInvitationsTypeDef = TypedDict(
    "_ListInvitationsPaginateResponseInvitationsTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)


class ListInvitationsPaginateResponseInvitationsTypeDef(
    _ListInvitationsPaginateResponseInvitationsTypeDef
):
    """
    - *(dict) --*

      Details about an invitation.
      - **AccountId** *(string) --*

        The account ID of the Security Hub master account that the invitation was sent from.
    """


_ListInvitationsPaginateResponseTypeDef = TypedDict(
    "_ListInvitationsPaginateResponseTypeDef",
    {"Invitations": List[ListInvitationsPaginateResponseInvitationsTypeDef]},
    total=False,
)


class ListInvitationsPaginateResponseTypeDef(_ListInvitationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Invitations** *(list) --*

        The details of the invitations returned by the operation.
        - *(dict) --*

          Details about an invitation.
          - **AccountId** *(string) --*

            The account ID of the Security Hub master account that the invitation was sent from.
    """


_ListMembersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMembersPaginatePaginationConfigTypeDef(_ListMembersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMembersPaginateResponseMembersTypeDef = TypedDict(
    "_ListMembersPaginateResponseMembersTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)


class ListMembersPaginateResponseMembersTypeDef(_ListMembersPaginateResponseMembersTypeDef):
    """
    - *(dict) --*

      The details about a member account.
      - **AccountId** *(string) --*

        The AWS account ID of the member account.
    """


_ListMembersPaginateResponseTypeDef = TypedDict(
    "_ListMembersPaginateResponseTypeDef",
    {"Members": List[ListMembersPaginateResponseMembersTypeDef]},
    total=False,
)


class ListMembersPaginateResponseTypeDef(_ListMembersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        Member details returned by the operation.
        - *(dict) --*

          The details about a member account.
          - **AccountId** *(string) --*

            The AWS account ID of the member account.
    """
