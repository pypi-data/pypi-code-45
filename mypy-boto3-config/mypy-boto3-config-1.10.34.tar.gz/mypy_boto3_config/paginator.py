"Main interface for config service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_config.type_defs import (
    DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef,
    DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef,
    DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef,
    DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef,
    DescribeAggregationAuthorizationsPaginateResponseTypeDef,
    DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef,
    DescribeComplianceByConfigRulePaginateResponseTypeDef,
    DescribeComplianceByResourcePaginatePaginationConfigTypeDef,
    DescribeComplianceByResourcePaginateResponseTypeDef,
    DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef,
    DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef,
    DescribeConfigRulesPaginatePaginationConfigTypeDef,
    DescribeConfigRulesPaginateResponseTypeDef,
    DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef,
    DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef,
    DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef,
    DescribeConfigurationAggregatorsPaginateResponseTypeDef,
    DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef,
    DescribePendingAggregationRequestsPaginateResponseTypeDef,
    DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef,
    DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef,
    DescribeRemediationExecutionStatusPaginateResponseTypeDef,
    DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef,
    DescribeRetentionConfigurationsPaginateResponseTypeDef,
    GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef,
    GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef,
    GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef,
    GetComplianceDetailsByConfigRulePaginateResponseTypeDef,
    GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef,
    GetComplianceDetailsByResourcePaginateResponseTypeDef,
    GetResourceConfigHistoryPaginatePaginationConfigTypeDef,
    GetResourceConfigHistoryPaginateResponseTypeDef,
    ListAggregateDiscoveredResourcesPaginateFiltersTypeDef,
    ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef,
    ListAggregateDiscoveredResourcesPaginateResponseTypeDef,
    ListDiscoveredResourcesPaginatePaginationConfigTypeDef,
    ListDiscoveredResourcesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAggregateComplianceByConfigRulesPaginator",
    "DescribeAggregationAuthorizationsPaginator",
    "DescribeComplianceByConfigRulePaginator",
    "DescribeComplianceByResourcePaginator",
    "DescribeConfigRuleEvaluationStatusPaginator",
    "DescribeConfigRulesPaginator",
    "DescribeConfigurationAggregatorSourcesStatusPaginator",
    "DescribeConfigurationAggregatorsPaginator",
    "DescribePendingAggregationRequestsPaginator",
    "DescribeRemediationExecutionStatusPaginator",
    "DescribeRetentionConfigurationsPaginator",
    "GetAggregateComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByResourcePaginator",
    "GetResourceConfigHistoryPaginator",
    "ListAggregateDiscoveredResourcesPaginator",
    "ListDiscoveredResourcesPaginator",
)


class DescribeAggregateComplianceByConfigRulesPaginator(Boto3Paginator):
    """
    Paginator for `describe_aggregate_compliance_by_config_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        Filters: DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef = None,
        PaginationConfig: DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef:
        """
        [DescribeAggregateComplianceByConfigRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules.paginate)
        """


class DescribeAggregationAuthorizationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_aggregation_authorizations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAggregationAuthorizationsPaginateResponseTypeDef:
        """
        [DescribeAggregationAuthorizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations.paginate)
        """


class DescribeComplianceByConfigRulePaginator(Boto3Paginator):
    """
    Paginator for `describe_compliance_by_config_rule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        PaginationConfig: DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef = None,
    ) -> DescribeComplianceByConfigRulePaginateResponseTypeDef:
        """
        [DescribeComplianceByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule.paginate)
        """


class DescribeComplianceByResourcePaginator(Boto3Paginator):
    """
    Paginator for `describe_compliance_by_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        PaginationConfig: DescribeComplianceByResourcePaginatePaginationConfigTypeDef = None,
    ) -> DescribeComplianceByResourcePaginateResponseTypeDef:
        """
        [DescribeComplianceByResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource.paginate)
        """


class DescribeConfigRuleEvaluationStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_config_rule_evaluation_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        PaginationConfig: DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef:
        """
        [DescribeConfigRuleEvaluationStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus.paginate)
        """


class DescribeConfigRulesPaginator(Boto3Paginator):
    """
    Paginator for `describe_config_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        PaginationConfig: DescribeConfigRulesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConfigRulesPaginateResponseTypeDef:
        """
        [DescribeConfigRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules.paginate)
        """


class DescribeConfigurationAggregatorSourcesStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_configuration_aggregator_sources_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[Literal["FAILED", "SUCCEEDED", "OUTDATED"]] = None,
        PaginationConfig: DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef:
        """
        [DescribeConfigurationAggregatorSourcesStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus.paginate)
        """


class DescribeConfigurationAggregatorsPaginator(Boto3Paginator):
    """
    Paginator for `describe_configuration_aggregators`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorNames: List[str] = None,
        PaginationConfig: DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConfigurationAggregatorsPaginateResponseTypeDef:
        """
        [DescribeConfigurationAggregators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators.paginate)
        """


class DescribePendingAggregationRequestsPaginator(Boto3Paginator):
    """
    Paginator for `describe_pending_aggregation_requests`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePendingAggregationRequestsPaginateResponseTypeDef:
        """
        [DescribePendingAggregationRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests.paginate)
        """


class DescribeRemediationExecutionStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_remediation_execution_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef] = None,
        PaginationConfig: DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRemediationExecutionStatusPaginateResponseTypeDef:
        """
        [DescribeRemediationExecutionStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus.paginate)
        """


class DescribeRetentionConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_retention_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RetentionConfigurationNames: List[str] = None,
        PaginationConfig: DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRetentionConfigurationsPaginateResponseTypeDef:
        """
        [DescribeRetentionConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations.paginate)
        """


class GetAggregateComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    Paginator for `get_aggregate_compliance_details_by_config_rule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ] = None,
        PaginationConfig: GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = None,
    ) -> GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef:
        """
        [GetAggregateComplianceDetailsByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule.paginate)
        """


class GetComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    Paginator for `get_compliance_details_by_config_rule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleName: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        PaginationConfig: GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = None,
    ) -> GetComplianceDetailsByConfigRulePaginateResponseTypeDef:
        """
        [GetComplianceDetailsByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule.paginate)
        """


class GetComplianceDetailsByResourcePaginator(Boto3Paginator):
    """
    Paginator for `get_compliance_details_by_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        PaginationConfig: GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef = None,
    ) -> GetComplianceDetailsByResourcePaginateResponseTypeDef:
        """
        [GetComplianceDetailsByResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource.paginate)
        """


class GetResourceConfigHistoryPaginator(Boto3Paginator):
    """
    Paginator for `get_resource_config_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
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
        PaginationConfig: GetResourceConfigHistoryPaginatePaginationConfigTypeDef = None,
    ) -> GetResourceConfigHistoryPaginateResponseTypeDef:
        """
        [GetResourceConfigHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory.paginate)
        """


class ListAggregateDiscoveredResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_aggregate_discovered_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
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
        Filters: ListAggregateDiscoveredResourcesPaginateFiltersTypeDef = None,
        PaginationConfig: ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListAggregateDiscoveredResourcesPaginateResponseTypeDef:
        """
        [ListAggregateDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources.paginate)
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_discovered_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
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
        PaginationConfig: ListDiscoveredResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListDiscoveredResourcesPaginateResponseTypeDef:
        """
        [ListDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources.paginate)
        """
