"Main interface for config service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef",
    "ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef",
    "ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef",
    "ClientBatchGetAggregateResourceConfigResponseTypeDef",
    "ClientBatchGetResourceConfigResourceKeysTypeDef",
    "ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef",
    "ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef",
    "ClientBatchGetResourceConfigResponseTypeDef",
    "ClientDeleteRemediationExceptionsResourceKeysTypeDef",
    "ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    "ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef",
    "ClientDeleteRemediationExceptionsResponseTypeDef",
    "ClientDeliverConfigSnapshotResponseTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef",
    "ClientDescribeAggregationAuthorizationsResponseTypeDef",
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef",
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef",
    "ClientDescribeComplianceByConfigRuleResponseTypeDef",
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef",
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef",
    "ClientDescribeComplianceByResourceResponseTypeDef",
    "ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef",
    "ClientDescribeConfigRuleEvaluationStatusResponseTypeDef",
    "ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef",
    "ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef",
    "ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef",
    "ClientDescribeConfigRulesResponseConfigRulesTypeDef",
    "ClientDescribeConfigRulesResponseTypeDef",
    "ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef",
    "ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef",
    "ClientDescribeConfigurationAggregatorsResponseTypeDef",
    "ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef",
    "ClientDescribeConfigurationRecorderStatusResponseTypeDef",
    "ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef",
    "ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef",
    "ClientDescribeConfigurationRecordersResponseTypeDef",
    "ClientDescribeConformancePackComplianceFiltersTypeDef",
    "ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef",
    "ClientDescribeConformancePackComplianceResponseTypeDef",
    "ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef",
    "ClientDescribeConformancePackStatusResponseTypeDef",
    "ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef",
    "ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef",
    "ClientDescribeConformancePacksResponseTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseTypeDef",
    "ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef",
    "ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef",
    "ClientDescribeDeliveryChannelsResponseTypeDef",
    "ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef",
    "ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef",
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef",
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef",
    "ClientDescribeOrganizationConfigRulesResponseTypeDef",
    "ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef",
    "ClientDescribeOrganizationConformancePackStatusesResponseTypeDef",
    "ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef",
    "ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef",
    "ClientDescribeOrganizationConformancePacksResponseTypeDef",
    "ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef",
    "ClientDescribePendingAggregationRequestsResponseTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef",
    "ClientDescribeRemediationConfigurationsResponseTypeDef",
    "ClientDescribeRemediationExceptionsResourceKeysTypeDef",
    "ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef",
    "ClientDescribeRemediationExceptionsResponseTypeDef",
    "ClientDescribeRemediationExecutionStatusResourceKeysTypeDef",
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef",
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef",
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef",
    "ClientDescribeRemediationExecutionStatusResponseTypeDef",
    "ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef",
    "ClientDescribeRetentionConfigurationsResponseTypeDef",
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef",
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef",
    "ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef",
    "ClientGetAggregateDiscoveredResourceCountsResponseTypeDef",
    "ClientGetAggregateResourceConfigResourceIdentifierTypeDef",
    "ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef",
    "ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef",
    "ClientGetAggregateResourceConfigResponseTypeDef",
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef",
    "ClientGetComplianceDetailsByConfigRuleResponseTypeDef",
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef",
    "ClientGetComplianceDetailsByResourceResponseTypeDef",
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef",
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef",
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef",
    "ClientGetComplianceSummaryByConfigRuleResponseTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseTypeDef",
    "ClientGetConformancePackComplianceDetailsFiltersTypeDef",
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef",
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef",
    "ClientGetConformancePackComplianceDetailsResponseTypeDef",
    "ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef",
    "ClientGetConformancePackComplianceSummaryResponseTypeDef",
    "ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef",
    "ClientGetDiscoveredResourceCountsResponseTypeDef",
    "ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef",
    "ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef",
    "ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef",
    "ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef",
    "ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef",
    "ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef",
    "ClientGetResourceConfigHistoryResponseTypeDef",
    "ClientListAggregateDiscoveredResourcesFiltersTypeDef",
    "ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef",
    "ClientListAggregateDiscoveredResourcesResponseTypeDef",
    "ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef",
    "ClientListDiscoveredResourcesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef",
    "ClientPutAggregationAuthorizationResponseTypeDef",
    "ClientPutAggregationAuthorizationTagsTypeDef",
    "ClientPutConfigRuleConfigRuleScopeTypeDef",
    "ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef",
    "ClientPutConfigRuleConfigRuleSourceTypeDef",
    "ClientPutConfigRuleConfigRuleTypeDef",
    "ClientPutConfigRuleTagsTypeDef",
    "ClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef",
    "ClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef",
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef",
    "ClientPutConfigurationAggregatorResponseTypeDef",
    "ClientPutConfigurationAggregatorTagsTypeDef",
    "ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef",
    "ClientPutConfigurationRecorderConfigurationRecorderTypeDef",
    "ClientPutConformancePackConformancePackInputParametersTypeDef",
    "ClientPutConformancePackResponseTypeDef",
    "ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef",
    "ClientPutDeliveryChannelDeliveryChannelTypeDef",
    "ClientPutEvaluationsEvaluationsTypeDef",
    "ClientPutEvaluationsResponseFailedEvaluationsTypeDef",
    "ClientPutEvaluationsResponseTypeDef",
    "ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef",
    "ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef",
    "ClientPutOrganizationConfigRuleResponseTypeDef",
    "ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef",
    "ClientPutOrganizationConformancePackResponseTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef",
    "ClientPutRemediationConfigurationsResponseTypeDef",
    "ClientPutRemediationExceptionsResourceKeysTypeDef",
    "ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    "ClientPutRemediationExceptionsResponseFailedBatchesTypeDef",
    "ClientPutRemediationExceptionsResponseTypeDef",
    "ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef",
    "ClientPutRetentionConfigurationResponseTypeDef",
    "ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef",
    "ClientSelectResourceConfigResponseQueryInfoTypeDef",
    "ClientSelectResourceConfigResponseTypeDef",
    "ClientStartRemediationExecutionResourceKeysTypeDef",
    "ClientStartRemediationExecutionResponseFailedItemsTypeDef",
    "ClientStartRemediationExecutionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef",
    "DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef",
    "DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef",
    "DescribeAggregationAuthorizationsPaginateResponseTypeDef",
    "DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef",
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef",
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef",
    "DescribeComplianceByConfigRulePaginateResponseTypeDef",
    "DescribeComplianceByResourcePaginatePaginationConfigTypeDef",
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef",
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef",
    "DescribeComplianceByResourcePaginateResponseTypeDef",
    "DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef",
    "DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef",
    "DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef",
    "DescribeConfigRulesPaginatePaginationConfigTypeDef",
    "DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef",
    "DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef",
    "DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef",
    "DescribeConfigRulesPaginateResponseConfigRulesTypeDef",
    "DescribeConfigRulesPaginateResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef",
    "DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef",
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef",
    "DescribeConfigurationAggregatorsPaginateResponseTypeDef",
    "DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef",
    "DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef",
    "DescribePendingAggregationRequestsPaginateResponseTypeDef",
    "DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef",
    "DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef",
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef",
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef",
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef",
    "DescribeRemediationExecutionStatusPaginateResponseTypeDef",
    "DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef",
    "DescribeRetentionConfigurationsPaginateResponseTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef",
    "GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef",
    "GetComplianceDetailsByConfigRulePaginateResponseTypeDef",
    "GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef",
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef",
    "GetComplianceDetailsByResourcePaginateResponseTypeDef",
    "GetResourceConfigHistoryPaginatePaginationConfigTypeDef",
    "GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef",
    "GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef",
    "GetResourceConfigHistoryPaginateResponseTypeDef",
    "ListAggregateDiscoveredResourcesPaginateFiltersTypeDef",
    "ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef",
    "ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef",
    "ListAggregateDiscoveredResourcesPaginateResponseTypeDef",
    "ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    "ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef",
    "ListDiscoveredResourcesPaginateResponseTypeDef",
)


_RequiredClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef = TypedDict(
    "_RequiredClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef",
    {"SourceAccountId": str},
)
_OptionalClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef = TypedDict(
    "_OptionalClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef",
    {
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "ResourceName": str,
    },
    total=False,
)


class ClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef(
    _RequiredClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef,
    _OptionalClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef,
):
    """
    - *(dict) --*

      The details that identify a resource that is collected by AWS Config aggregator, including the
      resource type, ID, (if available) the custom resource name, the source account, and source
      region.
      - **SourceAccountId** *(string) --***[REQUIRED]**

        The 12-digit account ID of the source account.
    """


_ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef = TypedDict(
    "_ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": Literal[
            "OK",
            "ResourceDiscovered",
            "ResourceNotRecorded",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
        ],
        "configurationStateId": str,
        "arn": str,
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef(
    _ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef
):
    """
    - *(dict) --*

      The detailed configuration of a specified resource.
      - **version** *(string) --*

        The version number of the resource configuration.
    """


_ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef = TypedDict(
    "_ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "ResourceName": str,
    },
    total=False,
)


class ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef(
    _ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef
):
    pass


_ClientBatchGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "_ClientBatchGetAggregateResourceConfigResponseTypeDef",
    {
        "BaseConfigurationItems": List[
            ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef
        ],
        "UnprocessedResourceIdentifiers": List[
            ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetAggregateResourceConfigResponseTypeDef(
    _ClientBatchGetAggregateResourceConfigResponseTypeDef
):
    """
    - *(dict) --*

      - **BaseConfigurationItems** *(list) --*

        A list that contains the current configuration of one or more resources.
        - *(dict) --*

          The detailed configuration of a specified resource.
          - **version** *(string) --*

            The version number of the resource configuration.
    """


_RequiredClientBatchGetResourceConfigResourceKeysTypeDef = TypedDict(
    "_RequiredClientBatchGetResourceConfigResourceKeysTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ]
    },
)
_OptionalClientBatchGetResourceConfigResourceKeysTypeDef = TypedDict(
    "_OptionalClientBatchGetResourceConfigResourceKeysTypeDef", {"resourceId": str}, total=False
)


class ClientBatchGetResourceConfigResourceKeysTypeDef(
    _RequiredClientBatchGetResourceConfigResourceKeysTypeDef,
    _OptionalClientBatchGetResourceConfigResourceKeysTypeDef,
):
    """
    - *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **resourceType** *(string) --***[REQUIRED]**

        The resource type.
    """


_ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef = TypedDict(
    "_ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": Literal[
            "OK",
            "ResourceDiscovered",
            "ResourceNotRecorded",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
        ],
        "configurationStateId": str,
        "arn": str,
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef(
    _ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef
):
    """
    - *(dict) --*

      The detailed configuration of a specified resource.
      - **version** *(string) --*

        The version number of the resource configuration.
    """


_ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef = TypedDict(
    "_ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
    },
    total=False,
)


class ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef(
    _ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef
):
    pass


_ClientBatchGetResourceConfigResponseTypeDef = TypedDict(
    "_ClientBatchGetResourceConfigResponseTypeDef",
    {
        "baseConfigurationItems": List[
            ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef
        ],
        "unprocessedResourceKeys": List[
            ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetResourceConfigResponseTypeDef(_ClientBatchGetResourceConfigResponseTypeDef):
    """
    - *(dict) --*

      - **baseConfigurationItems** *(list) --*

        A list that contains the current configuration of one or more resources.
        - *(dict) --*

          The detailed configuration of a specified resource.
          - **version** *(string) --*

            The version number of the resource configuration.
    """


_ClientDeleteRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "_ClientDeleteRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientDeleteRemediationExceptionsResourceKeysTypeDef(
    _ClientDeleteRemediationExceptionsResourceKeysTypeDef
):
    """
    - *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **ResourceType** *(string) --*

        The type of a resource.
    """


_ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "_ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef(
    _ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef
):
    pass


_ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef = TypedDict(
    "_ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[
            ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef(
    _ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef
):
    """
    - *(dict) --*

      List of each of the failed delete remediation exceptions with specific reasons.
      - **FailureMessage** *(string) --*

        Returns a failure message for delete remediation exception. For example, AWS Config creates
        an exception due to an internal error.
    """


_ClientDeleteRemediationExceptionsResponseTypeDef = TypedDict(
    "_ClientDeleteRemediationExceptionsResponseTypeDef",
    {"FailedBatches": List[ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef]},
    total=False,
)


class ClientDeleteRemediationExceptionsResponseTypeDef(
    _ClientDeleteRemediationExceptionsResponseTypeDef
):
    """
    - *(dict) --*

      - **FailedBatches** *(list) --*

        Returns a list of failed delete remediation exceptions batch objects. Each object in the
        batch consists of a list of failed items and failure messages.
        - *(dict) --*

          List of each of the failed delete remediation exceptions with specific reasons.
          - **FailureMessage** *(string) --*

            Returns a failure message for delete remediation exception. For example, AWS Config
            creates an exception due to an internal error.
    """


_ClientDeliverConfigSnapshotResponseTypeDef = TypedDict(
    "_ClientDeliverConfigSnapshotResponseTypeDef", {"configSnapshotId": str}, total=False
)


class ClientDeliverConfigSnapshotResponseTypeDef(_ClientDeliverConfigSnapshotResponseTypeDef):
    """
    - *(dict) --*

      The output for the  DeliverConfigSnapshot action, in JSON format.
      - **configSnapshotId** *(string) --*

        The ID of the snapshot that is being created.
    """


_ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef
):
    """
    Filters the results by ConfigRuleComplianceFilters object.
    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.
    """


_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef
):
    pass


_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef
):
    pass


_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef
):
    """
    - *(dict) --*

      Indicates whether an AWS Config rule is compliant based on account ID, region, compliance, and
      rule name.
      A rule is compliant if all of the resources that the rule evaluated comply with it. It is
      noncompliant if any of these resources do not comply.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule.
    """


_ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List[
            ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregateComplianceByConfigRules** *(list) --*

        Returns a list of AggregateComplianceByConfigRule object.
        - *(dict) --*

          Indicates whether an AWS Config rule is compliant based on account ID, region, compliance,
          and rule name.
          A rule is compliant if all of the resources that the rule evaluated comply with it. It is
          noncompliant if any of these resources do not comply.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.
    """


_ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef = TypedDict(
    "_ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef(
    _ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef
):
    """
    - *(dict) --*

      An object that represents the authorizations granted to aggregator accounts and regions.
      - **AggregationAuthorizationArn** *(string) --*

        The Amazon Resource Name (ARN) of the aggregation object.
    """


_ClientDescribeAggregationAuthorizationsResponseTypeDef = TypedDict(
    "_ClientDescribeAggregationAuthorizationsResponseTypeDef",
    {
        "AggregationAuthorizations": List[
            ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAggregationAuthorizationsResponseTypeDef(
    _ClientDescribeAggregationAuthorizationsResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregationAuthorizations** *(list) --*

        Returns a list of authorizations granted to various aggregator accounts and regions.
        - *(dict) --*

          An object that represents the authorizations granted to aggregator accounts and regions.
          - **AggregationAuthorizationArn** *(string) --*

            The Amazon Resource Name (ARN) of the aggregation object.
    """


_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef(
    _ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef
):
    pass


_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef(
    _ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef
):
    pass


_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef = TypedDict(
    "_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef,
    },
    total=False,
)


class ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef(
    _ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef
):
    """
    - *(dict) --*

      Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the resources
      that the rule evaluated comply with it. A rule is noncompliant if any of these resources do
      not comply.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule.
    """


_ClientDescribeComplianceByConfigRuleResponseTypeDef = TypedDict(
    "_ClientDescribeComplianceByConfigRuleResponseTypeDef",
    {
        "ComplianceByConfigRules": List[
            ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeComplianceByConfigRuleResponseTypeDef(
    _ClientDescribeComplianceByConfigRuleResponseTypeDef
):
    """
    - *(dict) --*

      - **ComplianceByConfigRules** *(list) --*

        Indicates whether each of the specified AWS Config rules is compliant.
        - *(dict) --*

          Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the
          resources that the rule evaluated comply with it. A rule is noncompliant if any of these
          resources do not comply.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.
    """


_ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef(
    _ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef
):
    pass


_ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef = TypedDict(
    "_ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef(
    _ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef
):
    pass


_ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef = TypedDict(
    "_ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef,
    },
    total=False,
)


class ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef(
    _ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef
):
    """
    - *(dict) --*

      Indicates whether an AWS resource that is evaluated according to one or more AWS Config rules
      is compliant. A resource is compliant if it complies with all of the rules that evaluate it. A
      resource is noncompliant if it does not comply with one or more of these rules.
      - **ResourceType** *(string) --*

        The type of the AWS resource that was evaluated.
    """


_ClientDescribeComplianceByResourceResponseTypeDef = TypedDict(
    "_ClientDescribeComplianceByResourceResponseTypeDef",
    {
        "ComplianceByResources": List[
            ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeComplianceByResourceResponseTypeDef(
    _ClientDescribeComplianceByResourceResponseTypeDef
):
    """
    - *(dict) --*

      - **ComplianceByResources** *(list) --*

        Indicates whether the specified AWS resource complies with all of the AWS Config rules that
        evaluate it.
        - *(dict) --*

          Indicates whether an AWS resource that is evaluated according to one or more AWS Config
          rules is compliant. A resource is compliant if it complies with all of the rules that
          evaluate it. A resource is noncompliant if it does not comply with one or more of these
          rules.
          - **ResourceType** *(string) --*

            The type of the AWS resource that was evaluated.
    """


_ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef = TypedDict(
    "_ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "LastSuccessfulInvocationTime": datetime,
        "LastFailedInvocationTime": datetime,
        "LastSuccessfulEvaluationTime": datetime,
        "LastFailedEvaluationTime": datetime,
        "FirstActivatedTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
        "FirstEvaluationStarted": bool,
    },
    total=False,
)


class ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef(
    _ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef
):
    """
    - *(dict) --*

      Status information for your AWS managed Config rules. The status includes information such as
      the last time the rule ran, the last time it failed, and the related error for the last
      failure.
      This action does not return status information about custom AWS Config rules.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule.
    """


_ClientDescribeConfigRuleEvaluationStatusResponseTypeDef = TypedDict(
    "_ClientDescribeConfigRuleEvaluationStatusResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List[
            ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConfigRuleEvaluationStatusResponseTypeDef(
    _ClientDescribeConfigRuleEvaluationStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **ConfigRulesEvaluationStatus** *(list) --*

        Status information about your AWS managed Config rules.
        - *(dict) --*

          Status information for your AWS managed Config rules. The status includes information such
          as the last time the rule ran, the last time it failed, and the related error for the last
          failure.
          This action does not return status information about custom AWS Config rules.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.
    """


_ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)


class ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef(
    _ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef
):
    pass


_ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef",
    {
        "EventSource": str,
        "MessageType": Literal[
            "ConfigurationItemChangeNotification",
            "ConfigurationSnapshotDeliveryCompleted",
            "ScheduledNotification",
            "OversizedConfigurationItemChangeNotification",
        ],
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
    },
    total=False,
)


class ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef(
    _ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef
):
    pass


_ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef",
    {
        "Owner": Literal["CUSTOM_LAMBDA", "AWS"],
        "SourceIdentifier": str,
        "SourceDetails": List[
            ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef(
    _ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef
):
    pass


_ClientDescribeConfigRulesResponseConfigRulesTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef,
        "Source": ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef,
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ConfigRuleState": Literal["ACTIVE", "DELETING", "DELETING_RESULTS", "EVALUATING"],
        "CreatedBy": str,
    },
    total=False,
)


class ClientDescribeConfigRulesResponseConfigRulesTypeDef(
    _ClientDescribeConfigRulesResponseConfigRulesTypeDef
):
    """
    - *(dict) --*

      An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a
      predefined function for an AWS managed rule. The function evaluates configuration items to
      assess whether your AWS resources comply with your desired configurations. This function can
      run when AWS Config detects a configuration change to an AWS resource and at a periodic
      frequency that you choose (for example, every 24 hours).
      .. note::

        You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations
        for your resources when AWS Config delivers the configuration snapshot. For more
        information, see  ConfigSnapshotDeliveryProperties .
    """


_ClientDescribeConfigRulesResponseTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseTypeDef",
    {"ConfigRules": List[ClientDescribeConfigRulesResponseConfigRulesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeConfigRulesResponseTypeDef(_ClientDescribeConfigRulesResponseTypeDef):
    """
    - *(dict) --*

      - **ConfigRules** *(list) --*

        The details about your AWS Config rules.
        - *(dict) --*

          An AWS Config rule represents an AWS Lambda function that you create for a custom rule or
          a predefined function for an AWS managed rule. The function evaluates configuration items
          to assess whether your AWS resources comply with your desired configurations. This
          function can run when AWS Config detects a configuration change to an AWS resource and at
          a periodic frequency that you choose (for example, every 24 hours).
          .. note::

            You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers
            evaluations for your resources when AWS Config delivers the configuration snapshot. For
            more information, see  ConfigSnapshotDeliveryProperties .
    """


_ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef",
    {
        "SourceId": str,
        "SourceType": Literal["ACCOUNT", "ORGANIZATION"],
        "AwsRegion": str,
        "LastUpdateStatus": Literal["FAILED", "SUCCEEDED", "OUTDATED"],
        "LastUpdateTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
    },
    total=False,
)


class ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef(
    _ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef
):
    """
    - *(dict) --*

      The current sync status between the source and the aggregator account.
      - **SourceId** *(string) --*

        The source account ID or an organization.
    """


_ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    {
        "AggregatedSourceStatusList": List[
            ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef(
    _ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregatedSourceStatusList** *(list) --*

        Returns an AggregatedSourceStatus object.
        - *(dict) --*

          The current sync status between the source and the aggregator account.
          - **SourceId** *(string) --*

            The source account ID or an organization.
    """


_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef(
    _ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef
):
    pass


_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef(
    _ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef
):
    pass


_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List[
            ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef
        ],
        "OrganizationAggregationSource": ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef(
    _ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef
):
    """
    - *(dict) --*

      The details about the configuration aggregator, including information about source accounts,
      regions, and metadata of the aggregator.
      - **ConfigurationAggregatorName** *(string) --*

        The name of the aggregator.
    """


_ClientDescribeConfigurationAggregatorsResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorsResponseTypeDef",
    {
        "ConfigurationAggregators": List[
            ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConfigurationAggregatorsResponseTypeDef(
    _ClientDescribeConfigurationAggregatorsResponseTypeDef
):
    """
    - *(dict) --*

      - **ConfigurationAggregators** *(list) --*

        Returns a ConfigurationAggregators object.
        - *(dict) --*

          The details about the configuration aggregator, including information about source
          accounts, regions, and metadata of the aggregator.
          - **ConfigurationAggregatorName** *(string) --*

            The name of the aggregator.
    """


_ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef",
    {
        "name": str,
        "lastStartTime": datetime,
        "lastStopTime": datetime,
        "recording": bool,
        "lastStatus": Literal["Pending", "Success", "Failure"],
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)


class ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef(
    _ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef
):
    """
    - *(dict) --*

      The current status of the configuration recorder.
      - **name** *(string) --*

        The name of the configuration recorder.
    """


_ClientDescribeConfigurationRecorderStatusResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecorderStatusResponseTypeDef",
    {
        "ConfigurationRecordersStatus": List[
            ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConfigurationRecorderStatusResponseTypeDef(
    _ClientDescribeConfigurationRecorderStatusResponseTypeDef
):
    """
    - *(dict) --*

      The output for the  DescribeConfigurationRecorderStatus action, in JSON format.
      - **ConfigurationRecordersStatus** *(list) --*

        A list that contains status of the specified recorders.
        - *(dict) --*

          The current status of the configuration recorder.
          - **name** *(string) --*

            The name of the configuration recorder.
    """


_ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": List[
            Literal[
                "AWS::EC2::CustomerGateway",
                "AWS::EC2::EIP",
                "AWS::EC2::Host",
                "AWS::EC2::Instance",
                "AWS::EC2::InternetGateway",
                "AWS::EC2::NetworkAcl",
                "AWS::EC2::NetworkInterface",
                "AWS::EC2::RouteTable",
                "AWS::EC2::SecurityGroup",
                "AWS::EC2::Subnet",
                "AWS::CloudTrail::Trail",
                "AWS::EC2::Volume",
                "AWS::EC2::VPC",
                "AWS::EC2::VPNConnection",
                "AWS::EC2::VPNGateway",
                "AWS::EC2::RegisteredHAInstance",
                "AWS::EC2::NatGateway",
                "AWS::EC2::EgressOnlyInternetGateway",
                "AWS::EC2::VPCEndpoint",
                "AWS::EC2::VPCEndpointService",
                "AWS::EC2::FlowLog",
                "AWS::EC2::VPCPeeringConnection",
                "AWS::IAM::Group",
                "AWS::IAM::Policy",
                "AWS::IAM::Role",
                "AWS::IAM::User",
                "AWS::ElasticLoadBalancingV2::LoadBalancer",
                "AWS::ACM::Certificate",
                "AWS::RDS::DBInstance",
                "AWS::RDS::DBParameterGroup",
                "AWS::RDS::DBOptionGroup",
                "AWS::RDS::DBSubnetGroup",
                "AWS::RDS::DBSecurityGroup",
                "AWS::RDS::DBSnapshot",
                "AWS::RDS::DBCluster",
                "AWS::RDS::DBClusterParameterGroup",
                "AWS::RDS::DBClusterSnapshot",
                "AWS::RDS::EventSubscription",
                "AWS::S3::Bucket",
                "AWS::S3::AccountPublicAccessBlock",
                "AWS::Redshift::Cluster",
                "AWS::Redshift::ClusterSnapshot",
                "AWS::Redshift::ClusterParameterGroup",
                "AWS::Redshift::ClusterSecurityGroup",
                "AWS::Redshift::ClusterSubnetGroup",
                "AWS::Redshift::EventSubscription",
                "AWS::SSM::ManagedInstanceInventory",
                "AWS::CloudWatch::Alarm",
                "AWS::CloudFormation::Stack",
                "AWS::ElasticLoadBalancing::LoadBalancer",
                "AWS::AutoScaling::AutoScalingGroup",
                "AWS::AutoScaling::LaunchConfiguration",
                "AWS::AutoScaling::ScalingPolicy",
                "AWS::AutoScaling::ScheduledAction",
                "AWS::DynamoDB::Table",
                "AWS::CodeBuild::Project",
                "AWS::WAF::RateBasedRule",
                "AWS::WAF::Rule",
                "AWS::WAF::RuleGroup",
                "AWS::WAF::WebACL",
                "AWS::WAFRegional::RateBasedRule",
                "AWS::WAFRegional::Rule",
                "AWS::WAFRegional::RuleGroup",
                "AWS::WAFRegional::WebACL",
                "AWS::CloudFront::Distribution",
                "AWS::CloudFront::StreamingDistribution",
                "AWS::Lambda::Alias",
                "AWS::Lambda::Function",
                "AWS::ElasticBeanstalk::Application",
                "AWS::ElasticBeanstalk::ApplicationVersion",
                "AWS::ElasticBeanstalk::Environment",
                "AWS::MobileHub::Project",
                "AWS::XRay::EncryptionConfig",
                "AWS::SSM::AssociationCompliance",
                "AWS::SSM::PatchCompliance",
                "AWS::Shield::Protection",
                "AWS::ShieldRegional::Protection",
                "AWS::Config::ResourceCompliance",
                "AWS::LicenseManager::LicenseConfiguration",
                "AWS::ApiGateway::DomainName",
                "AWS::ApiGateway::Method",
                "AWS::ApiGateway::Stage",
                "AWS::ApiGateway::RestApi",
                "AWS::ApiGatewayV2::DomainName",
                "AWS::ApiGatewayV2::Stage",
                "AWS::ApiGatewayV2::Api",
                "AWS::CodePipeline::Pipeline",
                "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
                "AWS::ServiceCatalog::CloudFormationProduct",
                "AWS::ServiceCatalog::Portfolio",
            ]
        ],
    },
    total=False,
)


class ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef(
    _ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef
):
    pass


_ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef,
    },
    total=False,
)


class ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef(
    _ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef
):
    """
    - *(dict) --*

      An object that represents the recording of configuration changes of an AWS resource.
      - **name** *(string) --*

        The name of the recorder. By default, AWS Config automatically assigns the name "default"
        when creating the configuration recorder. You cannot change the assigned name.
    """


_ClientDescribeConfigurationRecordersResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecordersResponseTypeDef",
    {
        "ConfigurationRecorders": List[
            ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConfigurationRecordersResponseTypeDef(
    _ClientDescribeConfigurationRecordersResponseTypeDef
):
    """
    - *(dict) --*

      The output for the  DescribeConfigurationRecorders action.
      - **ConfigurationRecorders** *(list) --*

        A list that contains the descriptions of the specified configuration recorders.
        - *(dict) --*

          An object that represents the recording of configuration changes of an AWS resource.
          - **name** *(string) --*

            The name of the recorder. By default, AWS Config automatically assigns the name
            "default" when creating the configuration recorder. You cannot change the assigned name.
    """


_ClientDescribeConformancePackComplianceFiltersTypeDef = TypedDict(
    "_ClientDescribeConformancePackComplianceFiltersTypeDef",
    {"ConfigRuleNames": List[str], "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"]},
    total=False,
)


class ClientDescribeConformancePackComplianceFiltersTypeDef(
    _ClientDescribeConformancePackComplianceFiltersTypeDef
):
    """
    A ``ConformancePackComplianceFilters`` object.
    - **ConfigRuleNames** *(list) --*

      Filters the results by AWS Config rule names.
      - *(string) --*
    """


_ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef = TypedDict(
    "_ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef",
    {"ConfigRuleName": str, "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"]},
    total=False,
)


class ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef(
    _ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef
):
    pass


_ClientDescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "_ClientDescribeConformancePackComplianceResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List[
            ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConformancePackComplianceResponseTypeDef(
    _ClientDescribeConformancePackComplianceResponseTypeDef
):
    """
    - *(dict) --*

      - **ConformancePackName** *(string) --*

        Name of the conformance pack.
    """


_ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef = TypedDict(
    "_ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackId": str,
        "ConformancePackArn": str,
        "ConformancePackState": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
        ],
        "StackArn": str,
        "ConformancePackStatusReason": str,
        "LastUpdateRequestedTime": datetime,
        "LastUpdateCompletedTime": datetime,
    },
    total=False,
)


class ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef(
    _ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef
):
    """
    - *(dict) --*

      Status details of a conformance pack.
      - **ConformancePackName** *(string) --*

        Name of the conformance pack.
    """


_ClientDescribeConformancePackStatusResponseTypeDef = TypedDict(
    "_ClientDescribeConformancePackStatusResponseTypeDef",
    {
        "ConformancePackStatusDetails": List[
            ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConformancePackStatusResponseTypeDef(
    _ClientDescribeConformancePackStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **ConformancePackStatusDetails** *(list) --*

        A list of ``ConformancePackStatusDetail`` objects.
        - *(dict) --*

          Status details of a conformance pack.
          - **ConformancePackName** *(string) --*

            Name of the conformance pack.
    """


_ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef = TypedDict(
    "_ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef(
    _ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef
):
    pass


_ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef = TypedDict(
    "_ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackArn": str,
        "ConformancePackId": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List[
            ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef
        ],
        "LastUpdateRequestedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)


class ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef(
    _ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef
):
    """
    - *(dict) --*

      Returns details of a conformance pack. A conformance pack is a collection of AWS Config rules
      and remediation actions that can be easily deployed in an account and a region.
      - **ConformancePackName** *(string) --*

        Name of the conformance pack.
    """


_ClientDescribeConformancePacksResponseTypeDef = TypedDict(
    "_ClientDescribeConformancePacksResponseTypeDef",
    {
        "ConformancePackDetails": List[
            ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConformancePacksResponseTypeDef(_ClientDescribeConformancePacksResponseTypeDef):
    """
    - *(dict) --*

      - **ConformancePackDetails** *(list) --*

        Returns a list of ``ConformancePackDetail`` objects.
        - *(dict) --*

          Returns details of a conformance pack. A conformance pack is a collection of AWS Config
          rules and remediation actions that can be easily deployed in an account and a region.
          - **ConformancePackName** *(string) --*

            Name of the conformance pack.
    """


_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef",
    {
        "lastStatus": Literal["Success", "Failure", "Not_Applicable"],
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastAttemptTime": datetime,
        "lastSuccessfulTime": datetime,
        "nextDeliveryTime": datetime,
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef
):
    pass


_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef",
    {
        "lastStatus": Literal["Success", "Failure", "Not_Applicable"],
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastAttemptTime": datetime,
        "lastSuccessfulTime": datetime,
        "nextDeliveryTime": datetime,
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef
):
    pass


_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": Literal["Success", "Failure", "Not_Applicable"],
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef
):
    pass


_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef",
    {
        "name": str,
        "configSnapshotDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef,
        "configHistoryDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef,
        "configStreamDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef
):
    """
    - *(dict) --*

      The status of a specified delivery channel.
      Valid values: ``Success`` | ``Failure``
      - **name** *(string) --*

        The name of the delivery channel.
    """


_ClientDescribeDeliveryChannelStatusResponseTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseTypeDef",
    {
        "DeliveryChannelsStatus": List[
            ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef
        ]
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseTypeDef
):
    """
    - *(dict) --*

      The output for the  DescribeDeliveryChannelStatus action.
      - **DeliveryChannelsStatus** *(list) --*

        A list that contains the status of a specified delivery channel.
        - *(dict) --*

          The status of a specified delivery channel.
          Valid values: ``Success`` | ``Failure``
          - **name** *(string) --*

            The name of the delivery channel.
    """


_ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    },
    total=False,
)


class ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef(
    _ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef
):
    pass


_ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef(
    _ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef
):
    """
    - *(dict) --*

      The channel through which AWS Config delivers notifications and updated configuration states.
      - **name** *(string) --*

        The name of the delivery channel. By default, AWS Config assigns the name "default" when
        creating the delivery channel. To change the delivery channel name, you must use the
        DeleteDeliveryChannel action to delete your current delivery channel, and then you must use
        the PutDeliveryChannel command to create a delivery channel that has the desired name.
    """


_ClientDescribeDeliveryChannelsResponseTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelsResponseTypeDef",
    {"DeliveryChannels": List[ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef]},
    total=False,
)


class ClientDescribeDeliveryChannelsResponseTypeDef(_ClientDescribeDeliveryChannelsResponseTypeDef):
    """
    - *(dict) --*

      The output for the  DescribeDeliveryChannels action.
      - **DeliveryChannels** *(list) --*

        A list that contains the descriptions of the specified delivery channel.
        - *(dict) --*

          The channel through which AWS Config delivers notifications and updated configuration
          states.
          - **name** *(string) --*

            The name of the delivery channel. By default, AWS Config assigns the name "default" when
            creating the delivery channel. To change the delivery channel name, you must use the
            DeleteDeliveryChannel action to delete your current delivery channel, and then you must
            use the PutDeliveryChannel command to create a delivery channel that has the desired
            name.
    """


_ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationRuleStatus": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef(
    _ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef
):
    """
    - *(dict) --*

      Returns the status for an organization config rule in an organization.
      - **OrganizationConfigRuleName** *(string) --*

        The name that you assign to organization config rule.
    """


_ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List[
            ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef(
    _ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationConfigRuleStatuses** *(list) --*

        A list of ``OrganizationConfigRuleStatus`` objects.
        - *(dict) --*

          Returns the status for an organization config rule in an organization.
          - **OrganizationConfigRuleName** *(string) --*

            The name that you assign to organization config rule.
    """


_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef",
    {
        "Description": str,
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[
            Literal[
                "ConfigurationItemChangeNotification",
                "OversizedConfigurationItemChangeNotification",
                "ScheduledNotification",
            ]
        ],
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef(
    _ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef
):
    pass


_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef",
    {
        "Description": str,
        "RuleIdentifier": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef(
    _ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef
):
    pass


_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationConfigRuleArn": str,
        "OrganizationManagedRuleMetadata": ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef,
        "OrganizationCustomRuleMetadata": ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef,
        "ExcludedAccounts": List[str],
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef(
    _ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef
):
    """
    - *(dict) --*

      An organization config rule that has information about config rules that AWS Config creates in
      member accounts.
      - **OrganizationConfigRuleName** *(string) --*

        The name that you assign to organization config rule.
    """


_ClientDescribeOrganizationConfigRulesResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRulesResponseTypeDef",
    {
        "OrganizationConfigRules": List[
            ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRulesResponseTypeDef(
    _ClientDescribeOrganizationConfigRulesResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationConfigRules** *(list) --*

        Returns a list of ``OrganizationConfigRule`` objects.
        - *(dict) --*

          An organization config rule that has information about config rules that AWS Config
          creates in member accounts.
          - **OrganizationConfigRuleName** *(string) --*

            The name that you assign to organization config rule.
    """


_ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Status": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef(
    _ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef
):
    """
    - *(dict) --*

      Returns the status for an organization conformance pack in an organization.
      - **OrganizationConformancePackName** *(string) --*

        The name that you assign to organization conformance pack.
    """


_ClientDescribeOrganizationConformancePackStatusesResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePackStatusesResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List[
            ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeOrganizationConformancePackStatusesResponseTypeDef(
    _ClientDescribeOrganizationConformancePackStatusesResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationConformancePackStatuses** *(list) --*

        A list of ``OrganizationConformancePackStatus`` objects.
        - *(dict) --*

          Returns the status for an organization conformance pack in an organization.
          - **OrganizationConformancePackName** *(string) --*

            The name that you assign to organization conformance pack.
    """


_ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef(
    _ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef
):
    pass


_ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef",
    {
        "OrganizationConformancePackName": str,
        "OrganizationConformancePackArn": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List[
            ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef
        ],
        "ExcludedAccounts": List[str],
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef(
    _ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef
):
    """
    - *(dict) --*

      An organization conformance pack that has information about conformance packs that AWS Config
      creates in member accounts.
      - **OrganizationConformancePackName** *(string) --*

        The name you assign to an organization conformance pack.
    """


_ClientDescribeOrganizationConformancePacksResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePacksResponseTypeDef",
    {
        "OrganizationConformancePacks": List[
            ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeOrganizationConformancePacksResponseTypeDef(
    _ClientDescribeOrganizationConformancePacksResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationConformancePacks** *(list) --*

        Returns a list of OrganizationConformancePacks objects.
        - *(dict) --*

          An organization conformance pack that has information about conformance packs that AWS
          Config creates in member accounts.
          - **OrganizationConformancePackName** *(string) --*

            The name you assign to an organization conformance pack.
    """


_ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef = TypedDict(
    "_ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef",
    {"RequesterAccountId": str, "RequesterAwsRegion": str},
    total=False,
)


class ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef(
    _ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef
):
    """
    - *(dict) --*

      An object that represents the account ID and region of an aggregator account that is
      requesting authorization but is not yet authorized.
      - **RequesterAccountId** *(string) --*

        The 12-digit account ID of the account requesting to aggregate data.
    """


_ClientDescribePendingAggregationRequestsResponseTypeDef = TypedDict(
    "_ClientDescribePendingAggregationRequestsResponseTypeDef",
    {
        "PendingAggregationRequests": List[
            ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribePendingAggregationRequestsResponseTypeDef(
    _ClientDescribePendingAggregationRequestsResponseTypeDef
):
    """
    - *(dict) --*

      - **PendingAggregationRequests** *(list) --*

        Returns a PendingAggregationRequests object.
        - *(dict) --*

          An object that represents the account ID and region of an aggregator account that is
          requesting authorization but is not yet authorized.
          - **RequesterAccountId** *(string) --*

            The 12-digit account ID of the account requesting to aggregate data.
    """


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef
):
    pass


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef",
    {
        "SsmControls": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef
):
    pass


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef",
    {"Value": str},
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef
):
    pass


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef
):
    pass


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef",
    {
        "ResourceValue": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef,
        "StaticValue": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef,
    },
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef
):
    pass


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": str,
        "TargetId": str,
        "TargetVersion": str,
        "Parameters": Dict[
            str,
            ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef,
        ],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef,
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef
):
    """
    - *(dict) --*

      An object that represents the details about the remediation configuration that includes the
      remediation action, parameters, and data to execute the action.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule.
    """


_ClientDescribeRemediationConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseTypeDef",
    {
        "RemediationConfigurations": List[
            ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseTypeDef(
    _ClientDescribeRemediationConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **RemediationConfigurations** *(list) --*

        Returns a remediation configuration object.
        - *(dict) --*

          An object that represents the details about the remediation configuration that includes
          the remediation action, parameters, and data to execute the action.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.
    """


_ClientDescribeRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "_ClientDescribeRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientDescribeRemediationExceptionsResourceKeysTypeDef(
    _ClientDescribeRemediationExceptionsResourceKeysTypeDef
):
    """
    - *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **ResourceType** *(string) --*

        The type of a resource.
    """


_ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef = TypedDict(
    "_ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)


class ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef(
    _ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef
):
    """
    - *(dict) --*

      An object that represents the details about the remediation exception. The details include the
      rule name, an explanation of an exception, the time when the exception will be deleted, the
      resource ID, and resource type.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule.
    """


_ClientDescribeRemediationExceptionsResponseTypeDef = TypedDict(
    "_ClientDescribeRemediationExceptionsResponseTypeDef",
    {
        "RemediationExceptions": List[
            ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeRemediationExceptionsResponseTypeDef(
    _ClientDescribeRemediationExceptionsResponseTypeDef
):
    """
    - *(dict) --*

      - **RemediationExceptions** *(list) --*

        Returns a list of remediation exception objects.
        - *(dict) --*

          An object that represents the details about the remediation exception. The details include
          the rule name, an explanation of an exception, the time when the exception will be
          deleted, the resource ID, and resource type.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.
    """


_RequiredClientDescribeRemediationExecutionStatusResourceKeysTypeDef = TypedDict(
    "_RequiredClientDescribeRemediationExecutionStatusResourceKeysTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ]
    },
)
_OptionalClientDescribeRemediationExecutionStatusResourceKeysTypeDef = TypedDict(
    "_OptionalClientDescribeRemediationExecutionStatusResourceKeysTypeDef",
    {"resourceId": str},
    total=False,
)


class ClientDescribeRemediationExecutionStatusResourceKeysTypeDef(
    _RequiredClientDescribeRemediationExecutionStatusResourceKeysTypeDef,
    _OptionalClientDescribeRemediationExecutionStatusResourceKeysTypeDef,
):
    """
    - *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **resourceType** *(string) --***[REQUIRED]**

        The resource type.
    """


_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
    },
    total=False,
)


class ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef(
    _ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef
):
    """
    - **ResourceKey** *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **resourceType** *(string) --*

        The resource type.
    """


_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef",
    {
        "Name": str,
        "State": Literal["SUCCEEDED", "PENDING", "FAILED"],
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)


class ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef(
    _ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef
):
    pass


_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef",
    {
        "ResourceKey": ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef,
        "State": Literal["QUEUED", "IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StepDetails": List[
            ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef
        ],
        "InvocationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef(
    _ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef
):
    """
    - *(dict) --*

      Provides details of the current status of the invoked remediation action for that resource.
      - **ResourceKey** *(dict) --*

        The details that identify a resource within AWS Config, including the resource type and
        resource ID.
        - **resourceType** *(string) --*

          The resource type.
    """


_ClientDescribeRemediationExecutionStatusResponseTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResponseTypeDef",
    {
        "RemediationExecutionStatuses": List[
            ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeRemediationExecutionStatusResponseTypeDef(
    _ClientDescribeRemediationExecutionStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **RemediationExecutionStatuses** *(list) --*

        Returns a list of remediation execution statuses objects.
        - *(dict) --*

          Provides details of the current status of the invoked remediation action for that
          resource.
          - **ResourceKey** *(dict) --*

            The details that identify a resource within AWS Config, including the resource type and
            resource ID.
            - **resourceType** *(string) --*

              The resource type.
    """


_ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef = TypedDict(
    "_ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)


class ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef(
    _ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef
):
    """
    - *(dict) --*

      An object with the name of the retention configuration and the retention period in days. The
      object stores the configuration for data retention in AWS Config.
      - **Name** *(string) --*

        The name of the retention configuration object.
    """


_ClientDescribeRetentionConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeRetentionConfigurationsResponseTypeDef",
    {
        "RetentionConfigurations": List[
            ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeRetentionConfigurationsResponseTypeDef(
    _ClientDescribeRetentionConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **RetentionConfigurations** *(list) --*

        Returns a retention configuration object.
        - *(dict) --*

          An object with the name of the retention configuration and the retention period in days.
          The object stores the configuration for data retention in AWS Config.
          - **Name** *(string) --*

            The name of the retention configuration object.
    """


_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
      of the evaluated resource.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef(
    _ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.
      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
        of the evaluated resource.
        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef = TypedDict(
    "_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef(
    _ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      The details of an AWS Config evaluation for an account ID and region in an aggregator.
      Provides the AWS resource that was evaluated, the compliance of the resource, related time
      stamps, and supplementary information.
      - **EvaluationResultIdentifier** *(dict) --*

        Uniquely identifies the evaluation result.
        - **EvaluationResultQualifier** *(dict) --*

          Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and
          ID of the evaluated resource.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "_ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "AggregateEvaluationResults": List[
            ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef(
    _ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregateEvaluationResults** *(list) --*

        Returns an AggregateEvaluationResults object.
        - *(dict) --*

          The details of an AWS Config evaluation for an account ID and region in an aggregator.
          Provides the AWS resource that was evaluated, the compliance of the resource, related time
          stamps, and supplementary information.
          - **EvaluationResultIdentifier** *(dict) --*

            Uniquely identifies the evaluation result.
            - **EvaluationResultQualifier** *(dict) --*

              Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
              and ID of the evaluated resource.
              - **ConfigRuleName** *(string) --*

                The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef",
    {"AccountId": str, "AwsRegion": str},
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef
):
    """
    Filters the results based on the ConfigRuleComplianceSummaryFilters object.
    - **AccountId** *(string) --*

      The 12-digit account ID of the source account.
    """


_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef
):
    pass


_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef
):
    pass


_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef
):
    pass


_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef",
    {
        "GroupName": str,
        "ComplianceSummary": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef,
    },
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef
):
    pass


_ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List[
            ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef
):
    """
    - *(dict) --*

      - **GroupByKey** *(string) --*

        Groups the result based on ACCOUNT_ID or AWS_REGION.
    """


_ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef = TypedDict(
    "_ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef",
    {
        "ResourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "AccountId": str,
        "Region": str,
    },
    total=False,
)


class ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef(
    _ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef
):
    """
    Filters the results based on the ``ResourceCountFilters`` object.
    - **ResourceType** *(string) --*

      The type of the AWS resource.
    """


_ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef = TypedDict(
    "_ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef",
    {"GroupName": str, "ResourceCount": int},
    total=False,
)


class ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef(
    _ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef
):
    pass


_ClientGetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "_ClientGetAggregateDiscoveredResourceCountsResponseTypeDef",
    {
        "TotalDiscoveredResources": int,
        "GroupByKey": str,
        "GroupedResourceCounts": List[
            ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetAggregateDiscoveredResourceCountsResponseTypeDef(
    _ClientGetAggregateDiscoveredResourceCountsResponseTypeDef
):
    """
    - *(dict) --*

      - **TotalDiscoveredResources** *(integer) --*

        The total number of resources that are present in an aggregator with the filters that you
        provide.
    """


_RequiredClientGetAggregateResourceConfigResourceIdentifierTypeDef = TypedDict(
    "_RequiredClientGetAggregateResourceConfigResourceIdentifierTypeDef", {"SourceAccountId": str}
)
_OptionalClientGetAggregateResourceConfigResourceIdentifierTypeDef = TypedDict(
    "_OptionalClientGetAggregateResourceConfigResourceIdentifierTypeDef",
    {
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "ResourceName": str,
    },
    total=False,
)


class ClientGetAggregateResourceConfigResourceIdentifierTypeDef(
    _RequiredClientGetAggregateResourceConfigResourceIdentifierTypeDef,
    _OptionalClientGetAggregateResourceConfigResourceIdentifierTypeDef,
):
    """
    An object that identifies aggregate resource.
    - **SourceAccountId** *(string) --***[REQUIRED]**

      The 12-digit account ID of the source account.
    """


_ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef = TypedDict(
    "_ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)


class ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef(
    _ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef
):
    pass


_ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef = TypedDict(
    "_ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": Literal[
            "OK",
            "ResourceDiscovered",
            "ResourceNotRecorded",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
        ],
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List[
            ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef
        ],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef(
    _ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef
):
    """
    - **ConfigurationItem** *(dict) --*

      Returns a ``ConfigurationItem`` object.
      - **version** *(string) --*

        The version number of the resource configuration.
    """


_ClientGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "_ClientGetAggregateResourceConfigResponseTypeDef",
    {"ConfigurationItem": ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef},
    total=False,
)


class ClientGetAggregateResourceConfigResponseTypeDef(
    _ClientGetAggregateResourceConfigResponseTypeDef
):
    """
    - *(dict) --*

      - **ConfigurationItem** *(dict) --*

        Returns a ``ConfigurationItem`` object.
        - **version** *(string) --*

          The version number of the resource configuration.
    """


_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
      of the evaluated resource.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef(
    _ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.
      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
        of the evaluated resource.
        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)


class ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef(
    _ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
      compliance of the resource, related time stamps, and supplementary information.
      - **EvaluationResultIdentifier** *(dict) --*

        Uniquely identifies the evaluation result.
        - **EvaluationResultQualifier** *(dict) --*

          Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and
          ID of the evaluated resource.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "EvaluationResults": List[
            ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetComplianceDetailsByConfigRuleResponseTypeDef(
    _ClientGetComplianceDetailsByConfigRuleResponseTypeDef
):
    """
    - *(dict) --*

      - **EvaluationResults** *(list) --*

        Indicates whether the AWS resource complies with the specified AWS Config rule.
        - *(dict) --*

          The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
          compliance of the resource, related time stamps, and supplementary information.
          - **EvaluationResultIdentifier** *(dict) --*

            Uniquely identifies the evaluation result.
            - **EvaluationResultQualifier** *(dict) --*

              Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
              and ID of the evaluated resource.
              - **ConfigRuleName** *(string) --*

                The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
      of the evaluated resource.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef(
    _ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.
      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
        of the evaluated resource.
        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)


class ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef(
    _ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
      compliance of the resource, related time stamps, and supplementary information.
      - **EvaluationResultIdentifier** *(dict) --*

        Uniquely identifies the evaluation result.
        - **EvaluationResultQualifier** *(dict) --*

          Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and
          ID of the evaluated resource.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetComplianceDetailsByResourceResponseTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByResourceResponseTypeDef",
    {
        "EvaluationResults": List[
            ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetComplianceDetailsByResourceResponseTypeDef(
    _ClientGetComplianceDetailsByResourceResponseTypeDef
):
    """
    - *(dict) --*

      - **EvaluationResults** *(list) --*

        Indicates whether the specified AWS resource complies each AWS Config rule.
        - *(dict) --*

          The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
          compliance of the resource, related time stamps, and supplementary information.
          - **EvaluationResultIdentifier** *(dict) --*

            Uniquely identifies the evaluation result.
            - **EvaluationResultQualifier** *(dict) --*

              Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
              and ID of the evaluated resource.
              - **ConfigRuleName** *(string) --*

                The name of the AWS Config rule that was used in the evaluation.
    """


_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef(
    _ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef
):
    """
    - **CompliantResourceCount** *(dict) --*

      The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for
      rules and 100 for resources.
      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current compliance of
        the item.
    """


_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef(
    _ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef
):
    pass


_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)


class ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef(
    _ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef
):
    """
    - **ComplianceSummary** *(dict) --*

      The number of AWS Config rules that are compliant and the number that are noncompliant, up to
      a maximum of 25 for each.
      - **CompliantResourceCount** *(dict) --*

        The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25
        for rules and 100 for resources.
        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current compliance of
          the item.
    """


_ClientGetComplianceSummaryByConfigRuleResponseTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByConfigRuleResponseTypeDef",
    {"ComplianceSummary": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef},
    total=False,
)


class ClientGetComplianceSummaryByConfigRuleResponseTypeDef(
    _ClientGetComplianceSummaryByConfigRuleResponseTypeDef
):
    """
    - *(dict) --*

      - **ComplianceSummary** *(dict) --*

        The number of AWS Config rules that are compliant and the number that are noncompliant, up
        to a maximum of 25 for each.
        - **CompliantResourceCount** *(dict) --*

          The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25
          for rules and 100 for resources.
          - **CappedCount** *(integer) --*

            The number of AWS resources or AWS Config rules responsible for the current compliance
            of the item.
    """


_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef
):
    pass


_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef
):
    pass


_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef
):
    pass


_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef",
    {
        "ResourceType": str,
        "ComplianceSummary": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef,
    },
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef
):
    """
    - *(dict) --*

      The number of AWS resources of a specific type that are compliant or noncompliant, up to a
      maximum of 100 for each.
      - **ResourceType** *(string) --*

        The type of AWS resource.
    """


_ClientGetComplianceSummaryByResourceTypeResponseTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseTypeDef",
    {
        "ComplianceSummariesByResourceType": List[
            ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef
        ]
    },
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseTypeDef
):
    """
    - *(dict) --*

      - **ComplianceSummariesByResourceType** *(list) --*

        The number of resources that are compliant and the number that are noncompliant. If one or
        more resource types were provided with the request, the numbers are returned for each
        resource type. The maximum number returned is 100.
        - *(dict) --*

          The number of AWS resources of a specific type that are compliant or noncompliant, up to a
          maximum of 100 for each.
          - **ResourceType** *(string) --*

            The type of AWS resource.
    """


_ClientGetConformancePackComplianceDetailsFiltersTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsFiltersTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ResourceType": str,
        "ResourceIds": List[str],
    },
    total=False,
)


class ClientGetConformancePackComplianceDetailsFiltersTypeDef(
    _ClientGetConformancePackComplianceDetailsFiltersTypeDef
):
    """
    A ``ConformancePackEvaluationFilters`` object.
    - **ConfigRuleNames** *(list) --*

      Filters the results by AWS Config rule names.
      - *(string) --*
    """


_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    pass


_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef(
    _ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef
):
    pass


_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef",
    {
        "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"],
        "EvaluationResultIdentifier": ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
        "Annotation": str,
    },
    total=False,
)


class ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef(
    _ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef
):
    pass


_ClientGetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleEvaluationResults": List[
            ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetConformancePackComplianceDetailsResponseTypeDef(
    _ClientGetConformancePackComplianceDetailsResponseTypeDef
):
    """
    - *(dict) --*

      - **ConformancePackName** *(string) --*

        Name of the conformance pack.
    """


_ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
    },
    total=False,
)


class ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef(
    _ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef
):
    """
    - *(dict) --*

      Summary includes the name and status of the conformance pack.
      - **ConformancePackName** *(string) --*

        The name of the conformance pack name.
    """


_ClientGetConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceSummaryResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List[
            ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetConformancePackComplianceSummaryResponseTypeDef(
    _ClientGetConformancePackComplianceSummaryResponseTypeDef
):
    """
    - *(dict) --*

      - **ConformancePackComplianceSummaryList** *(list) --*

        A list of ``ConformancePackComplianceSummary`` objects.
        - *(dict) --*

          Summary includes the name and status of the conformance pack.
          - **ConformancePackName** *(string) --*

            The name of the conformance pack name.
    """


_ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef = TypedDict(
    "_ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "count": int,
    },
    total=False,
)


class ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef(
    _ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef
):
    pass


_ClientGetDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "_ClientGetDiscoveredResourceCountsResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List[ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetDiscoveredResourceCountsResponseTypeDef(
    _ClientGetDiscoveredResourceCountsResponseTypeDef
):
    """
    - *(dict) --*

      - **totalDiscoveredResources** *(integer) --*

        The total number of resources that AWS Config is recording in the region for your account.
        If you specify resource types in the request, AWS Config returns only the total number of
        resources for those resource types.

          **Example**
    """


_ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef = TypedDict(
    "_ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef",
    {
        "AccountId": str,
        "MemberAccountRuleStatus": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
    },
    total=False,
)


class ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef(
    _ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef
):
    """
    A ``StatusDetailFilters`` object.
    - **AccountId** *(string) --*

      The 12-digit account ID of the member account within an organization.
    """


_ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef = TypedDict(
    "_ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef",
    {
        "AccountId": str,
        "ConfigRuleName": str,
        "MemberAccountRuleStatus": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef(
    _ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef
):
    """
    - *(dict) --*

      Organization config rule creation or deletion status in each member account. This includes the
      name of the rule, the status, error code and error message when the rule creation or deletion
      failed.
      - **AccountId** *(string) --*

        The 12-digit account ID of a member account.
    """


_ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef = TypedDict(
    "_ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    {
        "OrganizationConfigRuleDetailedStatus": List[
            ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef(
    _ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationConfigRuleDetailedStatus** *(list) --*

        A list of ``MemberAccountStatus`` objects.
        - *(dict) --*

          Organization config rule creation or deletion status in each member account. This includes
          the name of the rule, the status, error code and error message when the rule creation or
          deletion failed.
          - **AccountId** *(string) --*

            The 12-digit account ID of a member account.
    """


_ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef = TypedDict(
    "_ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef",
    {
        "AccountId": str,
        "Status": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
    },
    total=False,
)


class ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef(
    _ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef
):
    """
    An ``OrganizationResourceDetailedStatusFilters`` object.
    - **AccountId** *(string) --*

      The 12-digit account ID of the member account within an organization.
    """


_ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef = TypedDict(
    "_ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef",
    {
        "AccountId": str,
        "ConformancePackName": str,
        "Status": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef(
    _ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef
):
    """
    - *(dict) --*

      Organization conformance pack creation or deletion status in each member account. This
      includes the name of the conformance pack, the status, error code and error message when the
      conformance pack creation or deletion failed.
      - **AccountId** *(string) --*

        The 12-digit account ID of a member account.
    """


_ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef = TypedDict(
    "_ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef(
    _ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationConformancePackDetailedStatuses** *(list) --*

        A list of ``OrganizationConformancePackDetailedStatus`` objects.
        - *(dict) --*

          Organization conformance pack creation or deletion status in each member account. This
          includes the name of the conformance pack, the status, error code and error message when
          the conformance pack creation or deletion failed.
          - **AccountId** *(string) --*

            The 12-digit account ID of a member account.
    """


_ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef = TypedDict(
    "_ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)


class ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef(
    _ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef
):
    pass


_ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef = TypedDict(
    "_ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": Literal[
            "OK",
            "ResourceDiscovered",
            "ResourceNotRecorded",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
        ],
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List[
            ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef
        ],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef(
    _ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef
):
    """
    - *(dict) --*

      A list that contains detailed configurations of a specified resource.
      - **version** *(string) --*

        The version number of the resource configuration.
    """


_ClientGetResourceConfigHistoryResponseTypeDef = TypedDict(
    "_ClientGetResourceConfigHistoryResponseTypeDef",
    {
        "configurationItems": List[ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetResourceConfigHistoryResponseTypeDef(_ClientGetResourceConfigHistoryResponseTypeDef):
    """
    - *(dict) --*

      The output for the  GetResourceConfigHistory action.
      - **configurationItems** *(list) --*

        A list that contains the configuration history of one or more resources.
        - *(dict) --*

          A list that contains detailed configurations of a specified resource.
          - **version** *(string) --*

            The version number of the resource configuration.
    """


_ClientListAggregateDiscoveredResourcesFiltersTypeDef = TypedDict(
    "_ClientListAggregateDiscoveredResourcesFiltersTypeDef",
    {"AccountId": str, "ResourceId": str, "ResourceName": str, "Region": str},
    total=False,
)


class ClientListAggregateDiscoveredResourcesFiltersTypeDef(
    _ClientListAggregateDiscoveredResourcesFiltersTypeDef
):
    """
    Filters the results based on the ``ResourceFilters`` object.
    - **AccountId** *(string) --*

      The 12-digit source account ID.
    """


_ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "_ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "ResourceName": str,
    },
    total=False,
)


class ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef(
    _ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef
):
    """
    - *(dict) --*

      The details that identify a resource that is collected by AWS Config aggregator, including the
      resource type, ID, (if available) the custom resource name, the source account, and source
      region.
      - **SourceAccountId** *(string) --*

        The 12-digit account ID of the source account.
    """


_ClientListAggregateDiscoveredResourcesResponseTypeDef = TypedDict(
    "_ClientListAggregateDiscoveredResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListAggregateDiscoveredResourcesResponseTypeDef(
    _ClientListAggregateDiscoveredResourcesResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceIdentifiers** *(list) --*

        Returns a list of ``ResourceIdentifiers`` objects.
        - *(dict) --*

          The details that identify a resource that is collected by AWS Config aggregator, including
          the resource type, ID, (if available) the custom resource name, the source account, and
          source region.
          - **SourceAccountId** *(string) --*

            The 12-digit account ID of the source account.
    """


_ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef = TypedDict(
    "_ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "resourceDeletionTime": datetime,
    },
    total=False,
)


class ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef(
    _ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef
):
    """
    - *(dict) --*

      The details that identify a resource that is discovered by AWS Config, including the resource
      type, ID, and (if available) the custom resource name.
      - **resourceType** *(string) --*

        The type of resource.
    """


_ClientListDiscoveredResourcesResponseTypeDef = TypedDict(
    "_ClientListDiscoveredResourcesResponseTypeDef",
    {
        "resourceIdentifiers": List[
            ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDiscoveredResourcesResponseTypeDef(_ClientListDiscoveredResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **resourceIdentifiers** *(list) --*

        The details that identify a resource that is discovered by AWS Config, including the
        resource type, ID, and (if available) the custom resource name.
        - *(dict) --*

          The details that identify a resource that is discovered by AWS Config, including the
          resource type, ID, and (if available) the custom resource name.
          - **resourceType** *(string) --*

            The type of resource.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      The tags for the resource. The metadata that you apply to a resource to help you categorize
      and organize them. Each tag consists of a key and an optional value, both of which you define.
      Tag keys can have a maximum character length of 128 characters, and tag values can have a
      maximum length of 256 characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A key is a general label that acts like a
        category for more specific tag values.
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

        The tags for the resource.
        - *(dict) --*

          The tags for the resource. The metadata that you apply to a resource to help you
          categorize and organize them. Each tag consists of a key and an optional value, both of
          which you define. Tag keys can have a maximum character length of 128 characters, and tag
          values can have a maximum length of 256 characters.
          - **Key** *(string) --*

            One part of a key-value pair that make up a tag. A key is a general label that acts like
            a category for more specific tag values.
    """


_ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef = TypedDict(
    "_ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef(
    _ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef
):
    """
    - **AggregationAuthorization** *(dict) --*

      Returns an AggregationAuthorization object.
      - **AggregationAuthorizationArn** *(string) --*

        The Amazon Resource Name (ARN) of the aggregation object.
    """


_ClientPutAggregationAuthorizationResponseTypeDef = TypedDict(
    "_ClientPutAggregationAuthorizationResponseTypeDef",
    {
        "AggregationAuthorization": ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef
    },
    total=False,
)


class ClientPutAggregationAuthorizationResponseTypeDef(
    _ClientPutAggregationAuthorizationResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregationAuthorization** *(dict) --*

        Returns an AggregationAuthorization object.
        - **AggregationAuthorizationArn** *(string) --*

          The Amazon Resource Name (ARN) of the aggregation object.
    """


_ClientPutAggregationAuthorizationTagsTypeDef = TypedDict(
    "_ClientPutAggregationAuthorizationTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutAggregationAuthorizationTagsTypeDef(_ClientPutAggregationAuthorizationTagsTypeDef):
    """
    - *(dict) --*

      The tags for the resource. The metadata that you apply to a resource to help you categorize
      and organize them. Each tag consists of a key and an optional value, both of which you define.
      Tag keys can have a maximum character length of 128 characters, and tag values can have a
      maximum length of 256 characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A key is a general label that acts like a
        category for more specific tag values.
    """


_ClientPutConfigRuleConfigRuleScopeTypeDef = TypedDict(
    "_ClientPutConfigRuleConfigRuleScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)


class ClientPutConfigRuleConfigRuleScopeTypeDef(_ClientPutConfigRuleConfigRuleScopeTypeDef):
    pass


_ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef = TypedDict(
    "_ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef",
    {
        "EventSource": str,
        "MessageType": Literal[
            "ConfigurationItemChangeNotification",
            "ConfigurationSnapshotDeliveryCompleted",
            "ScheduledNotification",
            "OversizedConfigurationItemChangeNotification",
        ],
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
    },
    total=False,
)


class ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef(
    _ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef
):
    pass


_ClientPutConfigRuleConfigRuleSourceTypeDef = TypedDict(
    "_ClientPutConfigRuleConfigRuleSourceTypeDef",
    {
        "Owner": Literal["CUSTOM_LAMBDA", "AWS"],
        "SourceIdentifier": str,
        "SourceDetails": List[ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef],
    },
    total=False,
)


class ClientPutConfigRuleConfigRuleSourceTypeDef(_ClientPutConfigRuleConfigRuleSourceTypeDef):
    pass


_ClientPutConfigRuleConfigRuleTypeDef = TypedDict(
    "_ClientPutConfigRuleConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": ClientPutConfigRuleConfigRuleScopeTypeDef,
        "Source": ClientPutConfigRuleConfigRuleSourceTypeDef,
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ConfigRuleState": Literal["ACTIVE", "DELETING", "DELETING_RESULTS", "EVALUATING"],
        "CreatedBy": str,
    },
    total=False,
)


class ClientPutConfigRuleConfigRuleTypeDef(_ClientPutConfigRuleConfigRuleTypeDef):
    """
    The rule that you want to add to your account.
    - **ConfigRuleName** *(string) --*

      The name that you assign to the AWS Config rule. The name is required if you are adding a new
      rule.
    """


_ClientPutConfigRuleTagsTypeDef = TypedDict(
    "_ClientPutConfigRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutConfigRuleTagsTypeDef(_ClientPutConfigRuleTagsTypeDef):
    """
    - *(dict) --*

      The tags for the resource. The metadata that you apply to a resource to help you categorize
      and organize them. Each tag consists of a key and an optional value, both of which you define.
      Tag keys can have a maximum character length of 128 characters, and tag values can have a
      maximum length of 256 characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A key is a general label that acts like a
        category for more specific tag values.
    """


_RequiredClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef = TypedDict(
    "_RequiredClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str]},
)
_OptionalClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef = TypedDict(
    "_OptionalClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef",
    {"AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class ClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef(
    _RequiredClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef,
    _OptionalClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef,
):
    """
    - *(dict) --*

      A collection of accounts and regions.
      - **AccountIds** *(list) --***[REQUIRED]**

        The 12-digit account ID of the account being aggregated.
        - *(string) --*
    """


_RequiredClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef = TypedDict(
    "_RequiredClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    {"RoleArn": str},
)
_OptionalClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef = TypedDict(
    "_OptionalClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    {"AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class ClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef(
    _RequiredClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef,
    _OptionalClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef,
):
    """
    An OrganizationAggregationSource object.
    - **RoleArn** *(string) --***[REQUIRED]**

      ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator
      account.
    """


_ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef(
    _ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef
):
    pass


_ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef(
    _ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef
):
    pass


_ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List[
            ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef
        ],
        "OrganizationAggregationSource": ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef(
    _ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef
):
    """
    - **ConfigurationAggregator** *(dict) --*

      Returns a ConfigurationAggregator object.
      - **ConfigurationAggregatorName** *(string) --*

        The name of the aggregator.
    """


_ClientPutConfigurationAggregatorResponseTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorResponseTypeDef",
    {
        "ConfigurationAggregator": ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef
    },
    total=False,
)


class ClientPutConfigurationAggregatorResponseTypeDef(
    _ClientPutConfigurationAggregatorResponseTypeDef
):
    """
    - *(dict) --*

      - **ConfigurationAggregator** *(dict) --*

        Returns a ConfigurationAggregator object.
        - **ConfigurationAggregatorName** *(string) --*

          The name of the aggregator.
    """


_ClientPutConfigurationAggregatorTagsTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutConfigurationAggregatorTagsTypeDef(_ClientPutConfigurationAggregatorTagsTypeDef):
    """
    - *(dict) --*

      The tags for the resource. The metadata that you apply to a resource to help you categorize
      and organize them. Each tag consists of a key and an optional value, both of which you define.
      Tag keys can have a maximum character length of 128 characters, and tag values can have a
      maximum length of 256 characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A key is a general label that acts like a
        category for more specific tag values.
    """


_ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef = TypedDict(
    "_ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": List[
            Literal[
                "AWS::EC2::CustomerGateway",
                "AWS::EC2::EIP",
                "AWS::EC2::Host",
                "AWS::EC2::Instance",
                "AWS::EC2::InternetGateway",
                "AWS::EC2::NetworkAcl",
                "AWS::EC2::NetworkInterface",
                "AWS::EC2::RouteTable",
                "AWS::EC2::SecurityGroup",
                "AWS::EC2::Subnet",
                "AWS::CloudTrail::Trail",
                "AWS::EC2::Volume",
                "AWS::EC2::VPC",
                "AWS::EC2::VPNConnection",
                "AWS::EC2::VPNGateway",
                "AWS::EC2::RegisteredHAInstance",
                "AWS::EC2::NatGateway",
                "AWS::EC2::EgressOnlyInternetGateway",
                "AWS::EC2::VPCEndpoint",
                "AWS::EC2::VPCEndpointService",
                "AWS::EC2::FlowLog",
                "AWS::EC2::VPCPeeringConnection",
                "AWS::IAM::Group",
                "AWS::IAM::Policy",
                "AWS::IAM::Role",
                "AWS::IAM::User",
                "AWS::ElasticLoadBalancingV2::LoadBalancer",
                "AWS::ACM::Certificate",
                "AWS::RDS::DBInstance",
                "AWS::RDS::DBParameterGroup",
                "AWS::RDS::DBOptionGroup",
                "AWS::RDS::DBSubnetGroup",
                "AWS::RDS::DBSecurityGroup",
                "AWS::RDS::DBSnapshot",
                "AWS::RDS::DBCluster",
                "AWS::RDS::DBClusterParameterGroup",
                "AWS::RDS::DBClusterSnapshot",
                "AWS::RDS::EventSubscription",
                "AWS::S3::Bucket",
                "AWS::S3::AccountPublicAccessBlock",
                "AWS::Redshift::Cluster",
                "AWS::Redshift::ClusterSnapshot",
                "AWS::Redshift::ClusterParameterGroup",
                "AWS::Redshift::ClusterSecurityGroup",
                "AWS::Redshift::ClusterSubnetGroup",
                "AWS::Redshift::EventSubscription",
                "AWS::SSM::ManagedInstanceInventory",
                "AWS::CloudWatch::Alarm",
                "AWS::CloudFormation::Stack",
                "AWS::ElasticLoadBalancing::LoadBalancer",
                "AWS::AutoScaling::AutoScalingGroup",
                "AWS::AutoScaling::LaunchConfiguration",
                "AWS::AutoScaling::ScalingPolicy",
                "AWS::AutoScaling::ScheduledAction",
                "AWS::DynamoDB::Table",
                "AWS::CodeBuild::Project",
                "AWS::WAF::RateBasedRule",
                "AWS::WAF::Rule",
                "AWS::WAF::RuleGroup",
                "AWS::WAF::WebACL",
                "AWS::WAFRegional::RateBasedRule",
                "AWS::WAFRegional::Rule",
                "AWS::WAFRegional::RuleGroup",
                "AWS::WAFRegional::WebACL",
                "AWS::CloudFront::Distribution",
                "AWS::CloudFront::StreamingDistribution",
                "AWS::Lambda::Alias",
                "AWS::Lambda::Function",
                "AWS::ElasticBeanstalk::Application",
                "AWS::ElasticBeanstalk::ApplicationVersion",
                "AWS::ElasticBeanstalk::Environment",
                "AWS::MobileHub::Project",
                "AWS::XRay::EncryptionConfig",
                "AWS::SSM::AssociationCompliance",
                "AWS::SSM::PatchCompliance",
                "AWS::Shield::Protection",
                "AWS::ShieldRegional::Protection",
                "AWS::Config::ResourceCompliance",
                "AWS::LicenseManager::LicenseConfiguration",
                "AWS::ApiGateway::DomainName",
                "AWS::ApiGateway::Method",
                "AWS::ApiGateway::Stage",
                "AWS::ApiGateway::RestApi",
                "AWS::ApiGatewayV2::DomainName",
                "AWS::ApiGatewayV2::Stage",
                "AWS::ApiGatewayV2::Api",
                "AWS::CodePipeline::Pipeline",
                "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
                "AWS::ServiceCatalog::CloudFormationProduct",
                "AWS::ServiceCatalog::Portfolio",
            ]
        ],
    },
    total=False,
)


class ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef(
    _ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef
):
    pass


_ClientPutConfigurationRecorderConfigurationRecorderTypeDef = TypedDict(
    "_ClientPutConfigurationRecorderConfigurationRecorderTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef,
    },
    total=False,
)


class ClientPutConfigurationRecorderConfigurationRecorderTypeDef(
    _ClientPutConfigurationRecorderConfigurationRecorderTypeDef
):
    """
    The configuration recorder object that records each configuration change made to the resources.
    - **name** *(string) --*

      The name of the recorder. By default, AWS Config automatically assigns the name "default" when
      creating the configuration recorder. You cannot change the assigned name.
    """


_RequiredClientPutConformancePackConformancePackInputParametersTypeDef = TypedDict(
    "_RequiredClientPutConformancePackConformancePackInputParametersTypeDef", {"ParameterName": str}
)
_OptionalClientPutConformancePackConformancePackInputParametersTypeDef = TypedDict(
    "_OptionalClientPutConformancePackConformancePackInputParametersTypeDef",
    {"ParameterValue": str},
    total=False,
)


class ClientPutConformancePackConformancePackInputParametersTypeDef(
    _RequiredClientPutConformancePackConformancePackInputParametersTypeDef,
    _OptionalClientPutConformancePackConformancePackInputParametersTypeDef,
):
    """
    - *(dict) --*

      Input parameters in the form of key-value pairs for the conformance pack, both of which you
      define. Keys can have a maximum character length of 128 characters, and values can have a
      maximum length of 256 characters.
      - **ParameterName** *(string) --***[REQUIRED]**

        One part of a key-value pair.
    """


_ClientPutConformancePackResponseTypeDef = TypedDict(
    "_ClientPutConformancePackResponseTypeDef", {"ConformancePackArn": str}, total=False
)


class ClientPutConformancePackResponseTypeDef(_ClientPutConformancePackResponseTypeDef):
    """
    - *(dict) --*

      - **ConformancePackArn** *(string) --*

        ARN of the conformance pack.
    """


_ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "_ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    },
    total=False,
)


class ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef(
    _ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef
):
    pass


_ClientPutDeliveryChannelDeliveryChannelTypeDef = TypedDict(
    "_ClientPutDeliveryChannelDeliveryChannelTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef,
    },
    total=False,
)


class ClientPutDeliveryChannelDeliveryChannelTypeDef(
    _ClientPutDeliveryChannelDeliveryChannelTypeDef
):
    """
    The configuration delivery channel object that delivers the configuration information to an
    Amazon S3 bucket and to an Amazon SNS topic.
    - **name** *(string) --*

      The name of the delivery channel. By default, AWS Config assigns the name "default" when
      creating the delivery channel. To change the delivery channel name, you must use the
      DeleteDeliveryChannel action to delete your current delivery channel, and then you must use
      the PutDeliveryChannel command to create a delivery channel that has the desired name.
    """


_RequiredClientPutEvaluationsEvaluationsTypeDef = TypedDict(
    "_RequiredClientPutEvaluationsEvaluationsTypeDef", {"ComplianceResourceType": str}
)
_OptionalClientPutEvaluationsEvaluationsTypeDef = TypedDict(
    "_OptionalClientPutEvaluationsEvaluationsTypeDef",
    {
        "ComplianceResourceId": str,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "Annotation": str,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientPutEvaluationsEvaluationsTypeDef(
    _RequiredClientPutEvaluationsEvaluationsTypeDef, _OptionalClientPutEvaluationsEvaluationsTypeDef
):
    """
    - *(dict) --*

      Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it
      was evaluated against.
      - **ComplianceResourceType** *(string) --***[REQUIRED]**

        The type of AWS resource that was evaluated.
    """


_ClientPutEvaluationsResponseFailedEvaluationsTypeDef = TypedDict(
    "_ClientPutEvaluationsResponseFailedEvaluationsTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "Annotation": str,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientPutEvaluationsResponseFailedEvaluationsTypeDef(
    _ClientPutEvaluationsResponseFailedEvaluationsTypeDef
):
    """
    - *(dict) --*

      Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it
      was evaluated against.
      - **ComplianceResourceType** *(string) --*

        The type of AWS resource that was evaluated.
    """


_ClientPutEvaluationsResponseTypeDef = TypedDict(
    "_ClientPutEvaluationsResponseTypeDef",
    {"FailedEvaluations": List[ClientPutEvaluationsResponseFailedEvaluationsTypeDef]},
    total=False,
)


class ClientPutEvaluationsResponseTypeDef(_ClientPutEvaluationsResponseTypeDef):
    """
    - *(dict) --*

      - **FailedEvaluations** *(list) --*

        Requests that failed because of a client or server error.
        - *(dict) --*

          Identifies an AWS resource and indicates whether it complies with the AWS Config rule that
          it was evaluated against.
          - **ComplianceResourceType** *(string) --*

            The type of AWS resource that was evaluated.
    """


_ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef",
    {
        "Description": str,
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[
            Literal[
                "ConfigurationItemChangeNotification",
                "OversizedConfigurationItemChangeNotification",
                "ScheduledNotification",
            ]
        ],
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef(
    _ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef
):
    """
    An ``OrganizationCustomRuleMetadata`` object.
    - **Description** *(string) --*

      The description that you provide for organization config rule.
    """


_ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef",
    {
        "Description": str,
        "RuleIdentifier": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef(
    _ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef
):
    """
    An ``OrganizationManagedRuleMetadata`` object.
    - **Description** *(string) --*

      The description that you provide for organization config rule.
    """


_ClientPutOrganizationConfigRuleResponseTypeDef = TypedDict(
    "_ClientPutOrganizationConfigRuleResponseTypeDef",
    {"OrganizationConfigRuleArn": str},
    total=False,
)


class ClientPutOrganizationConfigRuleResponseTypeDef(
    _ClientPutOrganizationConfigRuleResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationConfigRuleArn** *(string) --*

        The Amazon Resource Name (ARN) of an organization config rule.
    """


_RequiredClientPutOrganizationConformancePackConformancePackInputParametersTypeDef = TypedDict(
    "_RequiredClientPutOrganizationConformancePackConformancePackInputParametersTypeDef",
    {"ParameterName": str},
)
_OptionalClientPutOrganizationConformancePackConformancePackInputParametersTypeDef = TypedDict(
    "_OptionalClientPutOrganizationConformancePackConformancePackInputParametersTypeDef",
    {"ParameterValue": str},
    total=False,
)


class ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef(
    _RequiredClientPutOrganizationConformancePackConformancePackInputParametersTypeDef,
    _OptionalClientPutOrganizationConformancePackConformancePackInputParametersTypeDef,
):
    """
    - *(dict) --*

      Input parameters in the form of key-value pairs for the conformance pack, both of which you
      define. Keys can have a maximum character length of 128 characters, and values can have a
      maximum length of 256 characters.
      - **ParameterName** *(string) --***[REQUIRED]**

        One part of a key-value pair.
    """


_ClientPutOrganizationConformancePackResponseTypeDef = TypedDict(
    "_ClientPutOrganizationConformancePackResponseTypeDef",
    {"OrganizationConformancePackArn": str},
    total=False,
)


class ClientPutOrganizationConformancePackResponseTypeDef(
    _ClientPutOrganizationConformancePackResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationConformancePackArn** *(string) --*

        ARN of the organization conformance pack.
    """


_ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef
):
    pass


_ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef",
    {
        "SsmControls": ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef
):
    pass


_ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef",
    {"Value": str},
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef
):
    pass


_ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef
):
    pass


_ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef",
    {
        "ResourceValue": ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef,
        "StaticValue": ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef,
    },
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef
):
    pass


_RequiredClientPutRemediationConfigurationsRemediationConfigurationsTypeDef = TypedDict(
    "_RequiredClientPutRemediationConfigurationsRemediationConfigurationsTypeDef",
    {"ConfigRuleName": str},
)
_OptionalClientPutRemediationConfigurationsRemediationConfigurationsTypeDef = TypedDict(
    "_OptionalClientPutRemediationConfigurationsRemediationConfigurationsTypeDef",
    {
        "TargetType": str,
        "TargetId": str,
        "TargetVersion": str,
        "Parameters": Dict[
            str, ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef
        ],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef,
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsTypeDef(
    _RequiredClientPutRemediationConfigurationsRemediationConfigurationsTypeDef,
    _OptionalClientPutRemediationConfigurationsRemediationConfigurationsTypeDef,
):
    """
    - *(dict) --*

      An object that represents the details about the remediation configuration that includes the
      remediation action, parameters, and data to execute the action.
      - **ConfigRuleName** *(string) --***[REQUIRED]**

        The name of the AWS Config rule.
    """


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef
):
    pass


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef",
    {
        "SsmControls": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef
):
    pass


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef",
    {"Value": str},
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef
):
    pass


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef
):
    pass


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef",
    {
        "ResourceValue": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef,
        "StaticValue": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef,
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef
):
    pass


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": str,
        "TargetId": str,
        "TargetVersion": str,
        "Parameters": Dict[
            str, ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef
        ],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef,
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef
):
    pass


_ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[
            ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef
):
    """
    - *(dict) --*

      List of each of the failed remediations with specific reasons.
      - **FailureMessage** *(string) --*

        Returns a failure message. For example, the resource is already compliant.
    """


_ClientPutRemediationConfigurationsResponseTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseTypeDef",
    {"FailedBatches": List[ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef]},
    total=False,
)


class ClientPutRemediationConfigurationsResponseTypeDef(
    _ClientPutRemediationConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **FailedBatches** *(list) --*

        Returns a list of failed remediation batch objects.
        - *(dict) --*

          List of each of the failed remediations with specific reasons.
          - **FailureMessage** *(string) --*

            Returns a failure message. For example, the resource is already compliant.
    """


_ClientPutRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "_ClientPutRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientPutRemediationExceptionsResourceKeysTypeDef(
    _ClientPutRemediationExceptionsResourceKeysTypeDef
):
    """
    - *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **ResourceType** *(string) --*

        The type of a resource.
    """


_ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "_ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)


class ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef(
    _ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef
):
    pass


_ClientPutRemediationExceptionsResponseFailedBatchesTypeDef = TypedDict(
    "_ClientPutRemediationExceptionsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef],
    },
    total=False,
)


class ClientPutRemediationExceptionsResponseFailedBatchesTypeDef(
    _ClientPutRemediationExceptionsResponseFailedBatchesTypeDef
):
    """
    - *(dict) --*

      List of each of the failed remediation exceptions with specific reasons.
      - **FailureMessage** *(string) --*

        Returns a failure message. For example, the auto-remediation has failed.
    """


_ClientPutRemediationExceptionsResponseTypeDef = TypedDict(
    "_ClientPutRemediationExceptionsResponseTypeDef",
    {"FailedBatches": List[ClientPutRemediationExceptionsResponseFailedBatchesTypeDef]},
    total=False,
)


class ClientPutRemediationExceptionsResponseTypeDef(_ClientPutRemediationExceptionsResponseTypeDef):
    """
    - *(dict) --*

      - **FailedBatches** *(list) --*

        Returns a list of failed remediation exceptions batch objects. Each object in the batch
        consists of a list of failed items and failure messages.
        - *(dict) --*

          List of each of the failed remediation exceptions with specific reasons.
          - **FailureMessage** *(string) --*

            Returns a failure message. For example, the auto-remediation has failed.
    """


_ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef = TypedDict(
    "_ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)


class ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef(
    _ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef
):
    """
    - **RetentionConfiguration** *(dict) --*

      Returns a retention configuration object.
      - **Name** *(string) --*

        The name of the retention configuration object.
    """


_ClientPutRetentionConfigurationResponseTypeDef = TypedDict(
    "_ClientPutRetentionConfigurationResponseTypeDef",
    {
        "RetentionConfiguration": ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef
    },
    total=False,
)


class ClientPutRetentionConfigurationResponseTypeDef(
    _ClientPutRetentionConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **RetentionConfiguration** *(dict) --*

        Returns a retention configuration object.
        - **Name** *(string) --*

          The name of the retention configuration object.
    """


_ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef = TypedDict(
    "_ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef", {"Name": str}, total=False
)


class ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef(
    _ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef
):
    pass


_ClientSelectResourceConfigResponseQueryInfoTypeDef = TypedDict(
    "_ClientSelectResourceConfigResponseQueryInfoTypeDef",
    {"SelectFields": List[ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef]},
    total=False,
)


class ClientSelectResourceConfigResponseQueryInfoTypeDef(
    _ClientSelectResourceConfigResponseQueryInfoTypeDef
):
    pass


_ClientSelectResourceConfigResponseTypeDef = TypedDict(
    "_ClientSelectResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": ClientSelectResourceConfigResponseQueryInfoTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientSelectResourceConfigResponseTypeDef(_ClientSelectResourceConfigResponseTypeDef):
    """
    - *(dict) --*

      - **Results** *(list) --*

        Returns the results for the SQL query.
        - *(string) --*
    """


_RequiredClientStartRemediationExecutionResourceKeysTypeDef = TypedDict(
    "_RequiredClientStartRemediationExecutionResourceKeysTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ]
    },
)
_OptionalClientStartRemediationExecutionResourceKeysTypeDef = TypedDict(
    "_OptionalClientStartRemediationExecutionResourceKeysTypeDef", {"resourceId": str}, total=False
)


class ClientStartRemediationExecutionResourceKeysTypeDef(
    _RequiredClientStartRemediationExecutionResourceKeysTypeDef,
    _OptionalClientStartRemediationExecutionResourceKeysTypeDef,
):
    """
    - *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **resourceType** *(string) --***[REQUIRED]**

        The resource type.
    """


_ClientStartRemediationExecutionResponseFailedItemsTypeDef = TypedDict(
    "_ClientStartRemediationExecutionResponseFailedItemsTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
    },
    total=False,
)


class ClientStartRemediationExecutionResponseFailedItemsTypeDef(
    _ClientStartRemediationExecutionResponseFailedItemsTypeDef
):
    pass


_ClientStartRemediationExecutionResponseTypeDef = TypedDict(
    "_ClientStartRemediationExecutionResponseTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[ClientStartRemediationExecutionResponseFailedItemsTypeDef],
    },
    total=False,
)


class ClientStartRemediationExecutionResponseTypeDef(
    _ClientStartRemediationExecutionResponseTypeDef
):
    """
    - *(dict) --*

      - **FailureMessage** *(string) --*

        Returns a failure message. For example, the resource is already compliant.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      The tags for the resource. The metadata that you apply to a resource to help you categorize
      and organize them. Each tag consists of a key and an optional value, both of which you define.
      Tag keys can have a maximum character length of 128 characters, and tag values can have a
      maximum length of 256 characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A key is a general label that acts like a
        category for more specific tag values.
    """


_DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef
):
    """
    Filters the results by ConfigRuleComplianceFilters object.
    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.
    """


_DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef
):
    pass


_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef
):
    pass


_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef
):
    """
    - *(dict) --*

      Indicates whether an AWS Config rule is compliant based on account ID, region, compliance, and
      rule name.
      A rule is compliant if all of the resources that the rule evaluated comply with it. It is
      noncompliant if any of these resources do not comply.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule.
    """


_DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List[
            DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef
        ]
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregateComplianceByConfigRules** *(list) --*

        Returns a list of AggregateComplianceByConfigRule object.
        - *(dict) --*

          Indicates whether an AWS Config rule is compliant based on account ID, region, compliance,
          and rule name.
          A rule is compliant if all of the resources that the rule evaluated comply with it. It is
          noncompliant if any of these resources do not comply.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.
    """


_DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef(
    _DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef = TypedDict(
    "_DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)


class DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef(
    _DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef
):
    """
    - *(dict) --*

      An object that represents the authorizations granted to aggregator accounts and regions.
      - **AggregationAuthorizationArn** *(string) --*

        The Amazon Resource Name (ARN) of the aggregation object.
    """


_DescribeAggregationAuthorizationsPaginateResponseTypeDef = TypedDict(
    "_DescribeAggregationAuthorizationsPaginateResponseTypeDef",
    {
        "AggregationAuthorizations": List[
            DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef
        ]
    },
    total=False,
)


class DescribeAggregationAuthorizationsPaginateResponseTypeDef(
    _DescribeAggregationAuthorizationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregationAuthorizations** *(list) --*

        Returns a list of authorizations granted to various aggregator accounts and regions.
        - *(dict) --*

          An object that represents the authorizations granted to aggregator accounts and regions.
          - **AggregationAuthorizationArn** *(string) --*

            The Amazon Resource Name (ARN) of the aggregation object.
    """


_DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef(
    _DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef(
    _DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef
):
    pass


_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef(
    _DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef
):
    pass


_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef,
    },
    total=False,
)


class DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef(
    _DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef
):
    """
    - *(dict) --*

      Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the resources
      that the rule evaluated comply with it. A rule is noncompliant if any of these resources do
      not comply.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule.
    """


_DescribeComplianceByConfigRulePaginateResponseTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginateResponseTypeDef",
    {
        "ComplianceByConfigRules": List[
            DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef
        ]
    },
    total=False,
)


class DescribeComplianceByConfigRulePaginateResponseTypeDef(
    _DescribeComplianceByConfigRulePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ComplianceByConfigRules** *(list) --*

        Indicates whether each of the specified AWS Config rules is compliant.
        - *(dict) --*

          Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the
          resources that the rule evaluated comply with it. A rule is noncompliant if any of these
          resources do not comply.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.
    """


_DescribeComplianceByResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeComplianceByResourcePaginatePaginationConfigTypeDef(
    _DescribeComplianceByResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef(
    _DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef
):
    pass


_DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef(
    _DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef
):
    pass


_DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef,
    },
    total=False,
)


class DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef(
    _DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef
):
    """
    - *(dict) --*

      Indicates whether an AWS resource that is evaluated according to one or more AWS Config rules
      is compliant. A resource is compliant if it complies with all of the rules that evaluate it. A
      resource is noncompliant if it does not comply with one or more of these rules.
      - **ResourceType** *(string) --*

        The type of the AWS resource that was evaluated.
    """


_DescribeComplianceByResourcePaginateResponseTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginateResponseTypeDef",
    {
        "ComplianceByResources": List[
            DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef
        ]
    },
    total=False,
)


class DescribeComplianceByResourcePaginateResponseTypeDef(
    _DescribeComplianceByResourcePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ComplianceByResources** *(list) --*

        Indicates whether the specified AWS resource complies with all of the AWS Config rules that
        evaluate it.
        - *(dict) --*

          Indicates whether an AWS resource that is evaluated according to one or more AWS Config
          rules is compliant. A resource is compliant if it complies with all of the rules that
          evaluate it. A resource is noncompliant if it does not comply with one or more of these
          rules.
          - **ResourceType** *(string) --*

            The type of the AWS resource that was evaluated.
    """


_DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef(
    _DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef = TypedDict(
    "_DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "LastSuccessfulInvocationTime": datetime,
        "LastFailedInvocationTime": datetime,
        "LastSuccessfulEvaluationTime": datetime,
        "LastFailedEvaluationTime": datetime,
        "FirstActivatedTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
        "FirstEvaluationStarted": bool,
    },
    total=False,
)


class DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef(
    _DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef
):
    """
    - *(dict) --*

      Status information for your AWS managed Config rules. The status includes information such as
      the last time the rule ran, the last time it failed, and the related error for the last
      failure.
      This action does not return status information about custom AWS Config rules.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule.
    """


_DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List[
            DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef
        ]
    },
    total=False,
)


class DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef(
    _DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ConfigRulesEvaluationStatus** *(list) --*

        Status information about your AWS managed Config rules.
        - *(dict) --*

          Status information for your AWS managed Config rules. The status includes information such
          as the last time the rule ran, the last time it failed, and the related error for the last
          failure.
          This action does not return status information about custom AWS Config rules.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.
    """


_DescribeConfigRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConfigRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeConfigRulesPaginatePaginationConfigTypeDef(
    _DescribeConfigRulesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)


class DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef(
    _DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef
):
    pass


_DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef",
    {
        "EventSource": str,
        "MessageType": Literal[
            "ConfigurationItemChangeNotification",
            "ConfigurationSnapshotDeliveryCompleted",
            "ScheduledNotification",
            "OversizedConfigurationItemChangeNotification",
        ],
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
    },
    total=False,
)


class DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef(
    _DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef
):
    pass


_DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef",
    {
        "Owner": Literal["CUSTOM_LAMBDA", "AWS"],
        "SourceIdentifier": str,
        "SourceDetails": List[
            DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef
        ],
    },
    total=False,
)


class DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef(
    _DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef
):
    pass


_DescribeConfigRulesPaginateResponseConfigRulesTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef,
        "Source": DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef,
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ConfigRuleState": Literal["ACTIVE", "DELETING", "DELETING_RESULTS", "EVALUATING"],
        "CreatedBy": str,
    },
    total=False,
)


class DescribeConfigRulesPaginateResponseConfigRulesTypeDef(
    _DescribeConfigRulesPaginateResponseConfigRulesTypeDef
):
    """
    - *(dict) --*

      An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a
      predefined function for an AWS managed rule. The function evaluates configuration items to
      assess whether your AWS resources comply with your desired configurations. This function can
      run when AWS Config detects a configuration change to an AWS resource and at a periodic
      frequency that you choose (for example, every 24 hours).
      .. note::

        You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations
        for your resources when AWS Config delivers the configuration snapshot. For more
        information, see  ConfigSnapshotDeliveryProperties .
    """


_DescribeConfigRulesPaginateResponseTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseTypeDef",
    {"ConfigRules": List[DescribeConfigRulesPaginateResponseConfigRulesTypeDef]},
    total=False,
)


class DescribeConfigRulesPaginateResponseTypeDef(_DescribeConfigRulesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ConfigRules** *(list) --*

        The details about your AWS Config rules.
        - *(dict) --*

          An AWS Config rule represents an AWS Lambda function that you create for a custom rule or
          a predefined function for an AWS managed rule. The function evaluates configuration items
          to assess whether your AWS resources comply with your desired configurations. This
          function can run when AWS Config detects a configuration change to an AWS resource and at
          a periodic frequency that you choose (for example, every 24 hours).
          .. note::

            You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers
            evaluations for your resources when AWS Config delivers the configuration snapshot. For
            more information, see  ConfigSnapshotDeliveryProperties .
    """


_DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef(
    _DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef",
    {
        "SourceId": str,
        "SourceType": Literal["ACCOUNT", "ORGANIZATION"],
        "AwsRegion": str,
        "LastUpdateStatus": Literal["FAILED", "SUCCEEDED", "OUTDATED"],
        "LastUpdateTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
    },
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef(
    _DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef
):
    """
    - *(dict) --*

      The current sync status between the source and the aggregator account.
      - **SourceId** *(string) --*

        The source account ID or an organization.
    """


_DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef",
    {
        "AggregatedSourceStatusList": List[
            DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef
        ]
    },
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef(
    _DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregatedSourceStatusList** *(list) --*

        Returns an AggregatedSourceStatus object.
        - *(dict) --*

          The current sync status between the source and the aggregator account.
          - **SourceId** *(string) --*

            The source account ID or an organization.
    """


_DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef(
    _DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef(
    _DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef
):
    pass


_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef(
    _DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef
):
    pass


_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List[
            DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef
        ],
        "OrganizationAggregationSource": DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef(
    _DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef
):
    """
    - *(dict) --*

      The details about the configuration aggregator, including information about source accounts,
      regions, and metadata of the aggregator.
      - **ConfigurationAggregatorName** *(string) --*

        The name of the aggregator.
    """


_DescribeConfigurationAggregatorsPaginateResponseTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginateResponseTypeDef",
    {
        "ConfigurationAggregators": List[
            DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef
        ]
    },
    total=False,
)


class DescribeConfigurationAggregatorsPaginateResponseTypeDef(
    _DescribeConfigurationAggregatorsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ConfigurationAggregators** *(list) --*

        Returns a ConfigurationAggregators object.
        - *(dict) --*

          The details about the configuration aggregator, including information about source
          accounts, regions, and metadata of the aggregator.
          - **ConfigurationAggregatorName** *(string) --*

            The name of the aggregator.
    """


_DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef(
    _DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef = TypedDict(
    "_DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef",
    {"RequesterAccountId": str, "RequesterAwsRegion": str},
    total=False,
)


class DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef(
    _DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef
):
    """
    - *(dict) --*

      An object that represents the account ID and region of an aggregator account that is
      requesting authorization but is not yet authorized.
      - **RequesterAccountId** *(string) --*

        The 12-digit account ID of the account requesting to aggregate data.
    """


_DescribePendingAggregationRequestsPaginateResponseTypeDef = TypedDict(
    "_DescribePendingAggregationRequestsPaginateResponseTypeDef",
    {
        "PendingAggregationRequests": List[
            DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef
        ]
    },
    total=False,
)


class DescribePendingAggregationRequestsPaginateResponseTypeDef(
    _DescribePendingAggregationRequestsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **PendingAggregationRequests** *(list) --*

        Returns a PendingAggregationRequests object.
        - *(dict) --*

          An object that represents the account ID and region of an aggregator account that is
          requesting authorization but is not yet authorized.
          - **RequesterAccountId** *(string) --*

            The 12-digit account ID of the account requesting to aggregate data.
    """


_DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef(
    _DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_RequiredDescribeRemediationExecutionStatusPaginateResourceKeysTypeDef = TypedDict(
    "_RequiredDescribeRemediationExecutionStatusPaginateResourceKeysTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ]
    },
)
_OptionalDescribeRemediationExecutionStatusPaginateResourceKeysTypeDef = TypedDict(
    "_OptionalDescribeRemediationExecutionStatusPaginateResourceKeysTypeDef",
    {"resourceId": str},
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef(
    _RequiredDescribeRemediationExecutionStatusPaginateResourceKeysTypeDef,
    _OptionalDescribeRemediationExecutionStatusPaginateResourceKeysTypeDef,
):
    """
    - *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **resourceType** *(string) --***[REQUIRED]**

        The resource type.
    """


_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
    },
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef(
    _DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef
):
    """
    - **ResourceKey** *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.
      - **resourceType** *(string) --*

        The resource type.
    """


_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef",
    {
        "Name": str,
        "State": Literal["SUCCEEDED", "PENDING", "FAILED"],
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef(
    _DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef
):
    pass


_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef",
    {
        "ResourceKey": DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef,
        "State": Literal["QUEUED", "IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StepDetails": List[
            DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef
        ],
        "InvocationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef(
    _DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef
):
    """
    - *(dict) --*

      Provides details of the current status of the invoked remediation action for that resource.
      - **ResourceKey** *(dict) --*

        The details that identify a resource within AWS Config, including the resource type and
        resource ID.
        - **resourceType** *(string) --*

          The resource type.
    """


_DescribeRemediationExecutionStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResponseTypeDef",
    {
        "RemediationExecutionStatuses": List[
            DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef
        ]
    },
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResponseTypeDef(
    _DescribeRemediationExecutionStatusPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **RemediationExecutionStatuses** *(list) --*

        Returns a list of remediation execution statuses objects.
        - *(dict) --*

          Provides details of the current status of the invoked remediation action for that
          resource.
          - **ResourceKey** *(dict) --*

            The details that identify a resource within AWS Config, including the resource type and
            resource ID.
            - **resourceType** *(string) --*

              The resource type.
    """


_DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef = TypedDict(
    "_DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)


class DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef(
    _DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef
):
    """
    - *(dict) --*

      An object with the name of the retention configuration and the retention period in days. The
      object stores the configuration for data retention in AWS Config.
      - **Name** *(string) --*

        The name of the retention configuration object.
    """


_DescribeRetentionConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeRetentionConfigurationsPaginateResponseTypeDef",
    {
        "RetentionConfigurations": List[
            DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef
        ]
    },
    total=False,
)


class DescribeRetentionConfigurationsPaginateResponseTypeDef(
    _DescribeRetentionConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **RetentionConfigurations** *(list) --*

        Returns a retention configuration object.
        - *(dict) --*

          An object with the name of the retention configuration and the retention period in days.
          The object stores the configuration for data retention in AWS Config.
          - **Name** *(string) --*

            The name of the retention configuration object.
    """


_GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
      of the evaluated resource.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.
    """


_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.
      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
        of the evaluated resource.
        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.
    """


_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      The details of an AWS Config evaluation for an account ID and region in an aggregator.
      Provides the AWS resource that was evaluated, the compliance of the resource, related time
      stamps, and supplementary information.
      - **EvaluationResultIdentifier** *(dict) --*

        Uniquely identifies the evaluation result.
        - **EvaluationResultQualifier** *(dict) --*

          Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and
          ID of the evaluated resource.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule that was used in the evaluation.
    """


_GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef",
    {
        "AggregateEvaluationResults": List[
            GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef
        ]
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AggregateEvaluationResults** *(list) --*

        Returns an AggregateEvaluationResults object.
        - *(dict) --*

          The details of an AWS Config evaluation for an account ID and region in an aggregator.
          Provides the AWS resource that was evaluated, the compliance of the resource, related time
          stamps, and supplementary information.
          - **EvaluationResultIdentifier** *(dict) --*

            Uniquely identifies the evaluation result.
            - **EvaluationResultQualifier** *(dict) --*

              Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
              and ID of the evaluated resource.
              - **ConfigRuleName** *(string) --*

                The name of the AWS Config rule that was used in the evaluation.
    """


_GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef(
    _GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
      of the evaluated resource.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.
    """


_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef(
    _GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.
      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
        of the evaluated resource.
        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.
    """


_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)


class GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef(
    _GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
      compliance of the resource, related time stamps, and supplementary information.
      - **EvaluationResultIdentifier** *(dict) --*

        Uniquely identifies the evaluation result.
        - **EvaluationResultQualifier** *(dict) --*

          Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and
          ID of the evaluated resource.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule that was used in the evaluation.
    """


_GetComplianceDetailsByConfigRulePaginateResponseTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginateResponseTypeDef",
    {
        "EvaluationResults": List[
            GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef
        ]
    },
    total=False,
)


class GetComplianceDetailsByConfigRulePaginateResponseTypeDef(
    _GetComplianceDetailsByConfigRulePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EvaluationResults** *(list) --*

        Indicates whether the AWS resource complies with the specified AWS Config rule.
        - *(dict) --*

          The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
          compliance of the resource, related time stamps, and supplementary information.
          - **EvaluationResultIdentifier** *(dict) --*

            Uniquely identifies the evaluation result.
            - **EvaluationResultQualifier** *(dict) --*

              Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
              and ID of the evaluated resource.
              - **ConfigRuleName** *(string) --*

                The name of the AWS Config rule that was used in the evaluation.
    """


_GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef(
    _GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
      of the evaluated resource.
      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.
    """


_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef(
    _GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.
      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID
        of the evaluated resource.
        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.
    """


_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)


class GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef(
    _GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
      compliance of the resource, related time stamps, and supplementary information.
      - **EvaluationResultIdentifier** *(dict) --*

        Uniquely identifies the evaluation result.
        - **EvaluationResultQualifier** *(dict) --*

          Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and
          ID of the evaluated resource.
          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule that was used in the evaluation.
    """


_GetComplianceDetailsByResourcePaginateResponseTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginateResponseTypeDef",
    {
        "EvaluationResults": List[
            GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef
        ]
    },
    total=False,
)


class GetComplianceDetailsByResourcePaginateResponseTypeDef(
    _GetComplianceDetailsByResourcePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EvaluationResults** *(list) --*

        Indicates whether the specified AWS resource complies each AWS Config rule.
        - *(dict) --*

          The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
          compliance of the resource, related time stamps, and supplementary information.
          - **EvaluationResultIdentifier** *(dict) --*

            Uniquely identifies the evaluation result.
            - **EvaluationResultQualifier** *(dict) --*

              Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
              and ID of the evaluated resource.
              - **ConfigRuleName** *(string) --*

                The name of the AWS Config rule that was used in the evaluation.
    """


_GetResourceConfigHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourceConfigHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourceConfigHistoryPaginatePaginationConfigTypeDef(
    _GetResourceConfigHistoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef = TypedDict(
    "_GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)


class GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef(
    _GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef
):
    pass


_GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef = TypedDict(
    "_GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": Literal[
            "OK",
            "ResourceDiscovered",
            "ResourceNotRecorded",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
        ],
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List[
            GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef
        ],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef(
    _GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef
):
    """
    - *(dict) --*

      A list that contains detailed configurations of a specified resource.
      - **version** *(string) --*

        The version number of the resource configuration.
    """


_GetResourceConfigHistoryPaginateResponseTypeDef = TypedDict(
    "_GetResourceConfigHistoryPaginateResponseTypeDef",
    {
        "configurationItems": List[
            GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetResourceConfigHistoryPaginateResponseTypeDef(
    _GetResourceConfigHistoryPaginateResponseTypeDef
):
    """
    - *(dict) --*

      The output for the  GetResourceConfigHistory action.
      - **configurationItems** *(list) --*

        A list that contains the configuration history of one or more resources.
        - *(dict) --*

          A list that contains detailed configurations of a specified resource.
          - **version** *(string) --*

            The version number of the resource configuration.
    """


_ListAggregateDiscoveredResourcesPaginateFiltersTypeDef = TypedDict(
    "_ListAggregateDiscoveredResourcesPaginateFiltersTypeDef",
    {"AccountId": str, "ResourceId": str, "ResourceName": str, "Region": str},
    total=False,
)


class ListAggregateDiscoveredResourcesPaginateFiltersTypeDef(
    _ListAggregateDiscoveredResourcesPaginateFiltersTypeDef
):
    """
    Filters the results based on the ``ResourceFilters`` object.
    - **AccountId** *(string) --*

      The 12-digit source account ID.
    """


_ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef(
    _ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef = TypedDict(
    "_ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "ResourceName": str,
    },
    total=False,
)


class ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef(
    _ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef
):
    """
    - *(dict) --*

      The details that identify a resource that is collected by AWS Config aggregator, including the
      resource type, ID, (if available) the custom resource name, the source account, and source
      region.
      - **SourceAccountId** *(string) --*

        The 12-digit account ID of the source account.
    """


_ListAggregateDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "_ListAggregateDiscoveredResourcesPaginateResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef
        ]
    },
    total=False,
)


class ListAggregateDiscoveredResourcesPaginateResponseTypeDef(
    _ListAggregateDiscoveredResourcesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceIdentifiers** *(list) --*

        Returns a list of ``ResourceIdentifiers`` objects.
        - *(dict) --*

          The details that identify a resource that is collected by AWS Config aggregator, including
          the resource type, ID, (if available) the custom resource name, the source account, and
          source region.
          - **SourceAccountId** *(string) --*

            The 12-digit account ID of the source account.
    """


_ListDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDiscoveredResourcesPaginatePaginationConfigTypeDef(
    _ListDiscoveredResourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef",
    {
        "resourceType": Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        "resourceId": str,
        "resourceName": str,
        "resourceDeletionTime": datetime,
    },
    total=False,
)


class ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef(
    _ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef
):
    """
    - *(dict) --*

      The details that identify a resource that is discovered by AWS Config, including the resource
      type, ID, and (if available) the custom resource name.
      - **resourceType** *(string) --*

        The type of resource.
    """


_ListDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginateResponseTypeDef",
    {
        "resourceIdentifiers": List[
            ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDiscoveredResourcesPaginateResponseTypeDef(
    _ListDiscoveredResourcesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceIdentifiers** *(list) --*

        The details that identify a resource that is discovered by AWS Config, including the
        resource type, ID, and (if available) the custom resource name.
        - *(dict) --*

          The details that identify a resource that is discovered by AWS Config, including the
          resource type, ID, and (if available) the custom resource name.
          - **resourceType** *(string) --*

            The type of resource.
    """
