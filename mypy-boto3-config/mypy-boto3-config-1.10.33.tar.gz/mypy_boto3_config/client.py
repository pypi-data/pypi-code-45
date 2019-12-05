"Main interface for config service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_config.client as client_scope

# pylint: disable=import-self
import mypy_boto3_config.paginator as paginator_scope
from mypy_boto3_config.type_defs import (
    ClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef,
    ClientBatchGetAggregateResourceConfigResponseTypeDef,
    ClientBatchGetResourceConfigResourceKeysTypeDef,
    ClientBatchGetResourceConfigResponseTypeDef,
    ClientDeleteRemediationExceptionsResourceKeysTypeDef,
    ClientDeleteRemediationExceptionsResponseTypeDef,
    ClientDeliverConfigSnapshotResponseTypeDef,
    ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef,
    ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef,
    ClientDescribeAggregationAuthorizationsResponseTypeDef,
    ClientDescribeComplianceByConfigRuleResponseTypeDef,
    ClientDescribeComplianceByResourceResponseTypeDef,
    ClientDescribeConfigRuleEvaluationStatusResponseTypeDef,
    ClientDescribeConfigRulesResponseTypeDef,
    ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef,
    ClientDescribeConfigurationAggregatorsResponseTypeDef,
    ClientDescribeConfigurationRecorderStatusResponseTypeDef,
    ClientDescribeConfigurationRecordersResponseTypeDef,
    ClientDescribeConformancePackComplianceFiltersTypeDef,
    ClientDescribeConformancePackComplianceResponseTypeDef,
    ClientDescribeConformancePackStatusResponseTypeDef,
    ClientDescribeConformancePacksResponseTypeDef,
    ClientDescribeDeliveryChannelStatusResponseTypeDef,
    ClientDescribeDeliveryChannelsResponseTypeDef,
    ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef,
    ClientDescribeOrganizationConfigRulesResponseTypeDef,
    ClientDescribeOrganizationConformancePackStatusesResponseTypeDef,
    ClientDescribeOrganizationConformancePacksResponseTypeDef,
    ClientDescribePendingAggregationRequestsResponseTypeDef,
    ClientDescribeRemediationConfigurationsResponseTypeDef,
    ClientDescribeRemediationExceptionsResourceKeysTypeDef,
    ClientDescribeRemediationExceptionsResponseTypeDef,
    ClientDescribeRemediationExecutionStatusResourceKeysTypeDef,
    ClientDescribeRemediationExecutionStatusResponseTypeDef,
    ClientDescribeRetentionConfigurationsResponseTypeDef,
    ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef,
    ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef,
    ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef,
    ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef,
    ClientGetAggregateDiscoveredResourceCountsResponseTypeDef,
    ClientGetAggregateResourceConfigResourceIdentifierTypeDef,
    ClientGetAggregateResourceConfigResponseTypeDef,
    ClientGetComplianceDetailsByConfigRuleResponseTypeDef,
    ClientGetComplianceDetailsByResourceResponseTypeDef,
    ClientGetComplianceSummaryByConfigRuleResponseTypeDef,
    ClientGetComplianceSummaryByResourceTypeResponseTypeDef,
    ClientGetConformancePackComplianceDetailsFiltersTypeDef,
    ClientGetConformancePackComplianceDetailsResponseTypeDef,
    ClientGetConformancePackComplianceSummaryResponseTypeDef,
    ClientGetDiscoveredResourceCountsResponseTypeDef,
    ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef,
    ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef,
    ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef,
    ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef,
    ClientGetResourceConfigHistoryResponseTypeDef,
    ClientListAggregateDiscoveredResourcesFiltersTypeDef,
    ClientListAggregateDiscoveredResourcesResponseTypeDef,
    ClientListDiscoveredResourcesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutAggregationAuthorizationResponseTypeDef,
    ClientPutAggregationAuthorizationTagsTypeDef,
    ClientPutConfigRuleConfigRuleTypeDef,
    ClientPutConfigRuleTagsTypeDef,
    ClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef,
    ClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef,
    ClientPutConfigurationAggregatorResponseTypeDef,
    ClientPutConfigurationAggregatorTagsTypeDef,
    ClientPutConfigurationRecorderConfigurationRecorderTypeDef,
    ClientPutConformancePackConformancePackInputParametersTypeDef,
    ClientPutConformancePackResponseTypeDef,
    ClientPutDeliveryChannelDeliveryChannelTypeDef,
    ClientPutEvaluationsEvaluationsTypeDef,
    ClientPutEvaluationsResponseTypeDef,
    ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef,
    ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef,
    ClientPutOrganizationConfigRuleResponseTypeDef,
    ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef,
    ClientPutOrganizationConformancePackResponseTypeDef,
    ClientPutRemediationConfigurationsRemediationConfigurationsTypeDef,
    ClientPutRemediationConfigurationsResponseTypeDef,
    ClientPutRemediationExceptionsResourceKeysTypeDef,
    ClientPutRemediationExceptionsResponseTypeDef,
    ClientPutRetentionConfigurationResponseTypeDef,
    ClientSelectResourceConfigResponseTypeDef,
    ClientStartRemediationExecutionResourceKeysTypeDef,
    ClientStartRemediationExecutionResponseTypeDef,
    ClientTagResourceTagsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [ConfigService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_aggregate_resource_config(
        self,
        ConfigurationAggregatorName: str,
        ResourceIdentifiers: List[ClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef],
    ) -> ClientBatchGetAggregateResourceConfigResponseTypeDef:
        """
        [Client.batch_get_aggregate_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.batch_get_aggregate_resource_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_resource_config(
        self, resourceKeys: List[ClientBatchGetResourceConfigResourceKeysTypeDef]
    ) -> ClientBatchGetResourceConfigResponseTypeDef:
        """
        [Client.batch_get_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.batch_get_resource_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_aggregation_authorization(
        self, AuthorizedAccountId: str, AuthorizedAwsRegion: str
    ) -> None:
        """
        [Client.delete_aggregation_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_aggregation_authorization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_config_rule(self, ConfigRuleName: str) -> None:
        """
        [Client.delete_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_config_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_aggregator(self, ConfigurationAggregatorName: str) -> None:
        """
        [Client.delete_configuration_aggregator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_configuration_aggregator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_recorder(self, ConfigurationRecorderName: str) -> None:
        """
        [Client.delete_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_configuration_recorder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_conformance_pack(self, ConformancePackName: str) -> None:
        """
        [Client.delete_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_conformance_pack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_delivery_channel(self, DeliveryChannelName: str) -> None:
        """
        [Client.delete_delivery_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_delivery_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_evaluation_results(self, ConfigRuleName: str) -> Dict[str, Any]:
        """
        [Client.delete_evaluation_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_evaluation_results)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_organization_config_rule(self, OrganizationConfigRuleName: str) -> None:
        """
        [Client.delete_organization_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_organization_config_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_organization_conformance_pack(self, OrganizationConformancePackName: str) -> None:
        """
        [Client.delete_organization_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_organization_conformance_pack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_pending_aggregation_request(
        self, RequesterAccountId: str, RequesterAwsRegion: str
    ) -> None:
        """
        [Client.delete_pending_aggregation_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_pending_aggregation_request)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_remediation_configuration(
        self, ConfigRuleName: str, ResourceType: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_remediation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_remediation_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_remediation_exceptions(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[ClientDeleteRemediationExceptionsResourceKeysTypeDef],
    ) -> ClientDeleteRemediationExceptionsResponseTypeDef:
        """
        [Client.delete_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_remediation_exceptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_config(self, ResourceType: str, ResourceId: str) -> None:
        """
        [Client.delete_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_resource_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_retention_configuration(self, RetentionConfigurationName: str) -> None:
        """
        [Client.delete_retention_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.delete_retention_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deliver_config_snapshot(
        self, deliveryChannelName: str
    ) -> ClientDeliverConfigSnapshotResponseTypeDef:
        """
        [Client.deliver_config_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.deliver_config_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_aggregate_compliance_by_config_rules(
        self,
        ConfigurationAggregatorName: str,
        Filters: ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef:
        """
        [Client.describe_aggregate_compliance_by_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_aggregate_compliance_by_config_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_aggregation_authorizations(
        self, Limit: int = None, NextToken: str = None
    ) -> ClientDescribeAggregationAuthorizationsResponseTypeDef:
        """
        [Client.describe_aggregation_authorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_aggregation_authorizations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_compliance_by_config_rule(
        self,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        NextToken: str = None,
    ) -> ClientDescribeComplianceByConfigRuleResponseTypeDef:
        """
        [Client.describe_compliance_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_compliance_by_config_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_compliance_by_resource(
        self,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeComplianceByResourceResponseTypeDef:
        """
        [Client.describe_compliance_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_compliance_by_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_config_rule_evaluation_status(
        self, ConfigRuleNames: List[str] = None, NextToken: str = None, Limit: int = None
    ) -> ClientDescribeConfigRuleEvaluationStatusResponseTypeDef:
        """
        [Client.describe_config_rule_evaluation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_config_rule_evaluation_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_config_rules(
        self, ConfigRuleNames: List[str] = None, NextToken: str = None
    ) -> ClientDescribeConfigRulesResponseTypeDef:
        """
        [Client.describe_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_config_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration_aggregator_sources_status(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[Literal["FAILED", "SUCCEEDED", "OUTDATED"]] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef:
        """
        [Client.describe_configuration_aggregator_sources_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_configuration_aggregator_sources_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration_aggregators(
        self,
        ConfigurationAggregatorNames: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ClientDescribeConfigurationAggregatorsResponseTypeDef:
        """
        [Client.describe_configuration_aggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_configuration_aggregators)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration_recorder_status(
        self, ConfigurationRecorderNames: List[str] = None
    ) -> ClientDescribeConfigurationRecorderStatusResponseTypeDef:
        """
        [Client.describe_configuration_recorder_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_configuration_recorder_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration_recorders(
        self, ConfigurationRecorderNames: List[str] = None
    ) -> ClientDescribeConfigurationRecordersResponseTypeDef:
        """
        [Client.describe_configuration_recorders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_configuration_recorders)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_conformance_pack_compliance(
        self,
        ConformancePackName: str,
        Filters: ClientDescribeConformancePackComplianceFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeConformancePackComplianceResponseTypeDef:
        """
        [Client.describe_conformance_pack_compliance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_conformance_pack_compliance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_conformance_pack_status(
        self, ConformancePackNames: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> ClientDescribeConformancePackStatusResponseTypeDef:
        """
        [Client.describe_conformance_pack_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_conformance_pack_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_conformance_packs(
        self, ConformancePackNames: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> ClientDescribeConformancePacksResponseTypeDef:
        """
        [Client.describe_conformance_packs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_conformance_packs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_delivery_channel_status(
        self, DeliveryChannelNames: List[str] = None
    ) -> ClientDescribeDeliveryChannelStatusResponseTypeDef:
        """
        [Client.describe_delivery_channel_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_delivery_channel_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_delivery_channels(
        self, DeliveryChannelNames: List[str] = None
    ) -> ClientDescribeDeliveryChannelsResponseTypeDef:
        """
        [Client.describe_delivery_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_delivery_channels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_organization_config_rule_statuses(
        self,
        OrganizationConfigRuleNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef:
        """
        [Client.describe_organization_config_rule_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_organization_config_rule_statuses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_organization_config_rules(
        self,
        OrganizationConfigRuleNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeOrganizationConfigRulesResponseTypeDef:
        """
        [Client.describe_organization_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_organization_config_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_organization_conformance_pack_statuses(
        self,
        OrganizationConformancePackNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeOrganizationConformancePackStatusesResponseTypeDef:
        """
        [Client.describe_organization_conformance_pack_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_organization_conformance_pack_statuses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_organization_conformance_packs(
        self,
        OrganizationConformancePackNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeOrganizationConformancePacksResponseTypeDef:
        """
        [Client.describe_organization_conformance_packs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_organization_conformance_packs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pending_aggregation_requests(
        self, Limit: int = None, NextToken: str = None
    ) -> ClientDescribePendingAggregationRequestsResponseTypeDef:
        """
        [Client.describe_pending_aggregation_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_pending_aggregation_requests)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_remediation_configurations(
        self, ConfigRuleNames: List[str]
    ) -> ClientDescribeRemediationConfigurationsResponseTypeDef:
        """
        [Client.describe_remediation_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_remediation_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_remediation_exceptions(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[ClientDescribeRemediationExceptionsResourceKeysTypeDef] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeRemediationExceptionsResponseTypeDef:
        """
        [Client.describe_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_remediation_exceptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_remediation_execution_status(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[ClientDescribeRemediationExecutionStatusResourceKeysTypeDef] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeRemediationExecutionStatusResponseTypeDef:
        """
        [Client.describe_remediation_execution_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_remediation_execution_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_retention_configurations(
        self, RetentionConfigurationNames: List[str] = None, NextToken: str = None
    ) -> ClientDescribeRetentionConfigurationsResponseTypeDef:
        """
        [Client.describe_retention_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.describe_retention_configurations)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_aggregate_compliance_details_by_config_rule(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef:
        """
        [Client.get_aggregate_compliance_details_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_aggregate_compliance_details_by_config_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_aggregate_config_rule_compliance_summary(
        self,
        ConfigurationAggregatorName: str,
        Filters: ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef = None,
        GroupByKey: Literal["ACCOUNT_ID", "AWS_REGION"] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef:
        """
        [Client.get_aggregate_config_rule_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_aggregate_config_rule_compliance_summary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_aggregate_discovered_resource_counts(
        self,
        ConfigurationAggregatorName: str,
        Filters: ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef = None,
        GroupByKey: Literal["RESOURCE_TYPE", "ACCOUNT_ID", "AWS_REGION"] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientGetAggregateDiscoveredResourceCountsResponseTypeDef:
        """
        [Client.get_aggregate_discovered_resource_counts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_aggregate_discovered_resource_counts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_aggregate_resource_config(
        self,
        ConfigurationAggregatorName: str,
        ResourceIdentifier: ClientGetAggregateResourceConfigResourceIdentifierTypeDef,
    ) -> ClientGetAggregateResourceConfigResponseTypeDef:
        """
        [Client.get_aggregate_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_aggregate_resource_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_compliance_details_by_config_rule(
        self,
        ConfigRuleName: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientGetComplianceDetailsByConfigRuleResponseTypeDef:
        """
        [Client.get_compliance_details_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_compliance_details_by_config_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_compliance_details_by_resource(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        NextToken: str = None,
    ) -> ClientGetComplianceDetailsByResourceResponseTypeDef:
        """
        [Client.get_compliance_details_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_compliance_details_by_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_compliance_summary_by_config_rule(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetComplianceSummaryByConfigRuleResponseTypeDef:
        """
        [Client.get_compliance_summary_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_compliance_summary_by_config_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_compliance_summary_by_resource_type(
        self, ResourceTypes: List[str] = None
    ) -> ClientGetComplianceSummaryByResourceTypeResponseTypeDef:
        """
        [Client.get_compliance_summary_by_resource_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_compliance_summary_by_resource_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_conformance_pack_compliance_details(
        self,
        ConformancePackName: str,
        Filters: ClientGetConformancePackComplianceDetailsFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientGetConformancePackComplianceDetailsResponseTypeDef:
        """
        [Client.get_conformance_pack_compliance_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_conformance_pack_compliance_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_conformance_pack_compliance_summary(
        self, ConformancePackNames: List[str], Limit: int = None, NextToken: str = None
    ) -> ClientGetConformancePackComplianceSummaryResponseTypeDef:
        """
        [Client.get_conformance_pack_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_conformance_pack_compliance_summary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_discovered_resource_counts(
        self, resourceTypes: List[str] = None, limit: int = None, nextToken: str = None
    ) -> ClientGetDiscoveredResourceCountsResponseTypeDef:
        """
        [Client.get_discovered_resource_counts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_discovered_resource_counts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_organization_config_rule_detailed_status(
        self,
        OrganizationConfigRuleName: str,
        Filters: ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef:
        """
        [Client.get_organization_config_rule_detailed_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_organization_config_rule_detailed_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_organization_conformance_pack_detailed_status(
        self,
        OrganizationConformancePackName: str,
        Filters: ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef:
        """
        [Client.get_organization_conformance_pack_detailed_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_organization_conformance_pack_detailed_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_config_history(
        self,
        resourceType: Literal[
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
        resourceId: str,
        laterTime: datetime = None,
        earlierTime: datetime = None,
        chronologicalOrder: Literal["Reverse", "Forward"] = None,
        limit: int = None,
        nextToken: str = None,
    ) -> ClientGetResourceConfigHistoryResponseTypeDef:
        """
        [Client.get_resource_config_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.get_resource_config_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aggregate_discovered_resources(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: Literal[
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
        Filters: ClientListAggregateDiscoveredResourcesFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientListAggregateDiscoveredResourcesResponseTypeDef:
        """
        [Client.list_aggregate_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.list_aggregate_discovered_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_discovered_resources(
        self,
        resourceType: Literal[
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
        resourceIds: List[str] = None,
        resourceName: str = None,
        limit: int = None,
        includeDeletedResources: bool = None,
        nextToken: str = None,
    ) -> ClientListDiscoveredResourcesResponseTypeDef:
        """
        [Client.list_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.list_discovered_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str, Limit: int = None, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_aggregation_authorization(
        self,
        AuthorizedAccountId: str,
        AuthorizedAwsRegion: str,
        Tags: List[ClientPutAggregationAuthorizationTagsTypeDef] = None,
    ) -> ClientPutAggregationAuthorizationResponseTypeDef:
        """
        [Client.put_aggregation_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_aggregation_authorization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_config_rule(
        self,
        ConfigRule: ClientPutConfigRuleConfigRuleTypeDef,
        Tags: List[ClientPutConfigRuleTagsTypeDef] = None,
    ) -> None:
        """
        [Client.put_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_config_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_configuration_aggregator(
        self,
        ConfigurationAggregatorName: str,
        AccountAggregationSources: List[
            ClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef
        ] = None,
        OrganizationAggregationSource: ClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef = None,
        Tags: List[ClientPutConfigurationAggregatorTagsTypeDef] = None,
    ) -> ClientPutConfigurationAggregatorResponseTypeDef:
        """
        [Client.put_configuration_aggregator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_configuration_aggregator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_configuration_recorder(
        self, ConfigurationRecorder: ClientPutConfigurationRecorderConfigurationRecorderTypeDef
    ) -> None:
        """
        [Client.put_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_configuration_recorder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_conformance_pack(
        self,
        ConformancePackName: str,
        DeliveryS3Bucket: str,
        TemplateS3Uri: str = None,
        TemplateBody: str = None,
        DeliveryS3KeyPrefix: str = None,
        ConformancePackInputParameters: List[
            ClientPutConformancePackConformancePackInputParametersTypeDef
        ] = None,
    ) -> ClientPutConformancePackResponseTypeDef:
        """
        [Client.put_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_conformance_pack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_delivery_channel(
        self, DeliveryChannel: ClientPutDeliveryChannelDeliveryChannelTypeDef
    ) -> None:
        """
        [Client.put_delivery_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_delivery_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_evaluations(
        self,
        ResultToken: str,
        Evaluations: List[ClientPutEvaluationsEvaluationsTypeDef] = None,
        TestMode: bool = None,
    ) -> ClientPutEvaluationsResponseTypeDef:
        """
        [Client.put_evaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_evaluations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_organization_config_rule(
        self,
        OrganizationConfigRuleName: str,
        OrganizationManagedRuleMetadata: ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef = None,
        OrganizationCustomRuleMetadata: ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef = None,
        ExcludedAccounts: List[str] = None,
    ) -> ClientPutOrganizationConfigRuleResponseTypeDef:
        """
        [Client.put_organization_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_organization_config_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_organization_conformance_pack(
        self,
        OrganizationConformancePackName: str,
        DeliveryS3Bucket: str,
        TemplateS3Uri: str = None,
        TemplateBody: str = None,
        DeliveryS3KeyPrefix: str = None,
        ConformancePackInputParameters: List[
            ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef
        ] = None,
        ExcludedAccounts: List[str] = None,
    ) -> ClientPutOrganizationConformancePackResponseTypeDef:
        """
        [Client.put_organization_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_organization_conformance_pack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_remediation_configurations(
        self,
        RemediationConfigurations: List[
            ClientPutRemediationConfigurationsRemediationConfigurationsTypeDef
        ],
    ) -> ClientPutRemediationConfigurationsResponseTypeDef:
        """
        [Client.put_remediation_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_remediation_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_remediation_exceptions(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[ClientPutRemediationExceptionsResourceKeysTypeDef],
        Message: str = None,
        ExpirationTime: datetime = None,
    ) -> ClientPutRemediationExceptionsResponseTypeDef:
        """
        [Client.put_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_remediation_exceptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_resource_config(
        self,
        ResourceType: str,
        SchemaVersionId: str,
        ResourceId: str,
        Configuration: str,
        ResourceName: str = None,
        Tags: Dict[str, str] = None,
    ) -> None:
        """
        [Client.put_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_resource_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_retention_configuration(
        self, RetentionPeriodInDays: int
    ) -> ClientPutRetentionConfigurationResponseTypeDef:
        """
        [Client.put_retention_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.put_retention_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def select_resource_config(
        self, Expression: str, Limit: int = None, NextToken: str = None
    ) -> ClientSelectResourceConfigResponseTypeDef:
        """
        [Client.select_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.select_resource_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_config_rules_evaluation(self, ConfigRuleNames: List[str] = None) -> Dict[str, Any]:
        """
        [Client.start_config_rules_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.start_config_rules_evaluation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_configuration_recorder(self, ConfigurationRecorderName: str) -> None:
        """
        [Client.start_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.start_configuration_recorder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_remediation_execution(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[ClientStartRemediationExecutionResourceKeysTypeDef],
    ) -> ClientStartRemediationExecutionResponseTypeDef:
        """
        [Client.start_remediation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.start_remediation_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_configuration_recorder(self, ConfigurationRecorderName: str) -> None:
        """
        [Client.stop_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.stop_configuration_recorder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Client.untag_resource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_aggregate_compliance_by_config_rules"]
    ) -> paginator_scope.DescribeAggregateComplianceByConfigRulesPaginator:
        """
        [Paginator.DescribeAggregateComplianceByConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_aggregation_authorizations"]
    ) -> paginator_scope.DescribeAggregationAuthorizationsPaginator:
        """
        [Paginator.DescribeAggregationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_compliance_by_config_rule"]
    ) -> paginator_scope.DescribeComplianceByConfigRulePaginator:
        """
        [Paginator.DescribeComplianceByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_compliance_by_resource"]
    ) -> paginator_scope.DescribeComplianceByResourcePaginator:
        """
        [Paginator.DescribeComplianceByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_config_rule_evaluation_status"]
    ) -> paginator_scope.DescribeConfigRuleEvaluationStatusPaginator:
        """
        [Paginator.DescribeConfigRuleEvaluationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_config_rules"]
    ) -> paginator_scope.DescribeConfigRulesPaginator:
        """
        [Paginator.DescribeConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_configuration_aggregator_sources_status"]
    ) -> paginator_scope.DescribeConfigurationAggregatorSourcesStatusPaginator:
        """
        [Paginator.DescribeConfigurationAggregatorSourcesStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_configuration_aggregators"]
    ) -> paginator_scope.DescribeConfigurationAggregatorsPaginator:
        """
        [Paginator.DescribeConfigurationAggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_pending_aggregation_requests"]
    ) -> paginator_scope.DescribePendingAggregationRequestsPaginator:
        """
        [Paginator.DescribePendingAggregationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_remediation_execution_status"]
    ) -> paginator_scope.DescribeRemediationExecutionStatusPaginator:
        """
        [Paginator.DescribeRemediationExecutionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_retention_configurations"]
    ) -> paginator_scope.DescribeRetentionConfigurationsPaginator:
        """
        [Paginator.DescribeRetentionConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_aggregate_compliance_details_by_config_rule"]
    ) -> paginator_scope.GetAggregateComplianceDetailsByConfigRulePaginator:
        """
        [Paginator.GetAggregateComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_compliance_details_by_config_rule"]
    ) -> paginator_scope.GetComplianceDetailsByConfigRulePaginator:
        """
        [Paginator.GetComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_compliance_details_by_resource"]
    ) -> paginator_scope.GetComplianceDetailsByResourcePaginator:
        """
        [Paginator.GetComplianceDetailsByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_resource_config_history"]
    ) -> paginator_scope.GetResourceConfigHistoryPaginator:
        """
        [Paginator.GetResourceConfigHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aggregate_discovered_resources"]
    ) -> paginator_scope.ListAggregateDiscoveredResourcesPaginator:
        """
        [Paginator.ListAggregateDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_discovered_resources"]
    ) -> paginator_scope.ListDiscoveredResourcesPaginator:
        """
        [Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConformancePackTemplateValidationException: Boto3ClientError
    InsufficientDeliveryPolicyException: Boto3ClientError
    InsufficientPermissionsException: Boto3ClientError
    InvalidConfigurationRecorderNameException: Boto3ClientError
    InvalidDeliveryChannelNameException: Boto3ClientError
    InvalidExpressionException: Boto3ClientError
    InvalidLimitException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidRecordingGroupException: Boto3ClientError
    InvalidResultTokenException: Boto3ClientError
    InvalidRoleException: Boto3ClientError
    InvalidS3KeyPrefixException: Boto3ClientError
    InvalidSNSTopicARNException: Boto3ClientError
    InvalidTimeRangeException: Boto3ClientError
    LastDeliveryChannelDeleteFailedException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MaxActiveResourcesExceededException: Boto3ClientError
    MaxNumberOfConfigRulesExceededException: Boto3ClientError
    MaxNumberOfConfigurationRecordersExceededException: Boto3ClientError
    MaxNumberOfConformancePacksExceededException: Boto3ClientError
    MaxNumberOfDeliveryChannelsExceededException: Boto3ClientError
    MaxNumberOfOrganizationConfigRulesExceededException: Boto3ClientError
    MaxNumberOfOrganizationConformancePacksExceededException: Boto3ClientError
    MaxNumberOfRetentionConfigurationsExceededException: Boto3ClientError
    NoAvailableConfigurationRecorderException: Boto3ClientError
    NoAvailableDeliveryChannelException: Boto3ClientError
    NoAvailableOrganizationException: Boto3ClientError
    NoRunningConfigurationRecorderException: Boto3ClientError
    NoSuchBucketException: Boto3ClientError
    NoSuchConfigRuleException: Boto3ClientError
    NoSuchConfigRuleInConformancePackException: Boto3ClientError
    NoSuchConfigurationAggregatorException: Boto3ClientError
    NoSuchConfigurationRecorderException: Boto3ClientError
    NoSuchConformancePackException: Boto3ClientError
    NoSuchDeliveryChannelException: Boto3ClientError
    NoSuchOrganizationConfigRuleException: Boto3ClientError
    NoSuchOrganizationConformancePackException: Boto3ClientError
    NoSuchRemediationConfigurationException: Boto3ClientError
    NoSuchRemediationExceptionException: Boto3ClientError
    NoSuchRetentionConfigurationException: Boto3ClientError
    OrganizationAccessDeniedException: Boto3ClientError
    OrganizationAllFeaturesNotEnabledException: Boto3ClientError
    OrganizationConformancePackTemplateValidationException: Boto3ClientError
    OversizedConfigurationItemException: Boto3ClientError
    RemediationInProgressException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotDiscoveredException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    ValidationException: Boto3ClientError
