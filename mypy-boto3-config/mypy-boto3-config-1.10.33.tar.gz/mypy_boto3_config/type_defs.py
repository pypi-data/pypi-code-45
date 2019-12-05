"Main interface for config service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


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
    pass


ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef = TypedDict(
    "ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef",
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

ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef = TypedDict(
    "ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef",
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

ClientBatchGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "ClientBatchGetAggregateResourceConfigResponseTypeDef",
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
    pass


ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef = TypedDict(
    "ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef",
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

ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef = TypedDict(
    "ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef",
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

ClientBatchGetResourceConfigResponseTypeDef = TypedDict(
    "ClientBatchGetResourceConfigResponseTypeDef",
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

ClientDeleteRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "ClientDeleteRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)

ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)

ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef = TypedDict(
    "ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[
            ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef
        ],
    },
    total=False,
)

ClientDeleteRemediationExceptionsResponseTypeDef = TypedDict(
    "ClientDeleteRemediationExceptionsResponseTypeDef",
    {"FailedBatches": List[ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef]},
    total=False,
)

ClientDeliverConfigSnapshotResponseTypeDef = TypedDict(
    "ClientDeliverConfigSnapshotResponseTypeDef", {"configSnapshotId": str}, total=False
)

ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef = TypedDict(
    "ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef",
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

ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)

ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef = TypedDict(
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef = TypedDict(
    "ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List[
            ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef = TypedDict(
    "ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeAggregationAuthorizationsResponseTypeDef = TypedDict(
    "ClientDescribeAggregationAuthorizationsResponseTypeDef",
    {
        "AggregationAuthorizations": List[
            ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)

ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef = TypedDict(
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef,
    },
    total=False,
)

ClientDescribeComplianceByConfigRuleResponseTypeDef = TypedDict(
    "ClientDescribeComplianceByConfigRuleResponseTypeDef",
    {
        "ComplianceByConfigRules": List[
            ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef = TypedDict(
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef = TypedDict(
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)

ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef = TypedDict(
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef,
    },
    total=False,
)

ClientDescribeComplianceByResourceResponseTypeDef = TypedDict(
    "ClientDescribeComplianceByResourceResponseTypeDef",
    {
        "ComplianceByResources": List[
            ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef = TypedDict(
    "ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef",
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

ClientDescribeConfigRuleEvaluationStatusResponseTypeDef = TypedDict(
    "ClientDescribeConfigRuleEvaluationStatusResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List[
            ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef = TypedDict(
    "ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)

ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef = TypedDict(
    "ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef",
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

ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef = TypedDict(
    "ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef",
    {
        "Owner": Literal["CUSTOM_LAMBDA", "AWS"],
        "SourceIdentifier": str,
        "SourceDetails": List[
            ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef
        ],
    },
    total=False,
)

ClientDescribeConfigRulesResponseConfigRulesTypeDef = TypedDict(
    "ClientDescribeConfigRulesResponseConfigRulesTypeDef",
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

ClientDescribeConfigRulesResponseTypeDef = TypedDict(
    "ClientDescribeConfigRulesResponseTypeDef",
    {"ConfigRules": List[ClientDescribeConfigRulesResponseConfigRulesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef = TypedDict(
    "ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef",
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

ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    {
        "AggregatedSourceStatusList": List[
            ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef = TypedDict(
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)

ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef = TypedDict(
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)

ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef = TypedDict(
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef",
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

ClientDescribeConfigurationAggregatorsResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationAggregatorsResponseTypeDef",
    {
        "ConfigurationAggregators": List[
            ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef = TypedDict(
    "ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef",
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

ClientDescribeConfigurationRecorderStatusResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationRecorderStatusResponseTypeDef",
    {
        "ConfigurationRecordersStatus": List[
            ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef
        ]
    },
    total=False,
)

ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef = TypedDict(
    "ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef",
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

ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef = TypedDict(
    "ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef,
    },
    total=False,
)

ClientDescribeConfigurationRecordersResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationRecordersResponseTypeDef",
    {
        "ConfigurationRecorders": List[
            ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef
        ]
    },
    total=False,
)

ClientDescribeConformancePackComplianceFiltersTypeDef = TypedDict(
    "ClientDescribeConformancePackComplianceFiltersTypeDef",
    {"ConfigRuleNames": List[str], "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"]},
    total=False,
)

ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef = TypedDict(
    "ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef",
    {"ConfigRuleName": str, "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"]},
    total=False,
)

ClientDescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "ClientDescribeConformancePackComplianceResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List[
            ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef = TypedDict(
    "ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef",
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

ClientDescribeConformancePackStatusResponseTypeDef = TypedDict(
    "ClientDescribeConformancePackStatusResponseTypeDef",
    {
        "ConformancePackStatusDetails": List[
            ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef = TypedDict(
    "ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)

ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef = TypedDict(
    "ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef",
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

ClientDescribeConformancePacksResponseTypeDef = TypedDict(
    "ClientDescribeConformancePacksResponseTypeDef",
    {
        "ConformancePackDetails": List[
            ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef = TypedDict(
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef",
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

ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef = TypedDict(
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef",
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

ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef = TypedDict(
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": Literal["Success", "Failure", "Not_Applicable"],
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef = TypedDict(
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef",
    {
        "name": str,
        "configSnapshotDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef,
        "configHistoryDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef,
        "configStreamDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryChannelStatusResponseTypeDef = TypedDict(
    "ClientDescribeDeliveryChannelStatusResponseTypeDef",
    {
        "DeliveryChannelsStatus": List[
            ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef
        ]
    },
    total=False,
)

ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    },
    total=False,
)

ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef = TypedDict(
    "ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryChannelsResponseTypeDef = TypedDict(
    "ClientDescribeDeliveryChannelsResponseTypeDef",
    {"DeliveryChannels": List[ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef]},
    total=False,
)

ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef = TypedDict(
    "ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef",
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

ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef = TypedDict(
    "ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List[
            ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef",
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

ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef",
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

ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef = TypedDict(
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef",
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

ClientDescribeOrganizationConfigRulesResponseTypeDef = TypedDict(
    "ClientDescribeOrganizationConfigRulesResponseTypeDef",
    {
        "OrganizationConfigRules": List[
            ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef = TypedDict(
    "ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef",
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

ClientDescribeOrganizationConformancePackStatusesResponseTypeDef = TypedDict(
    "ClientDescribeOrganizationConformancePackStatusesResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List[
            ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef = TypedDict(
    "ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)

ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef = TypedDict(
    "ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef",
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

ClientDescribeOrganizationConformancePacksResponseTypeDef = TypedDict(
    "ClientDescribeOrganizationConformancePacksResponseTypeDef",
    {
        "OrganizationConformancePacks": List[
            ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef = TypedDict(
    "ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef",
    {"RequesterAccountId": str, "RequesterAwsRegion": str},
    total=False,
)

ClientDescribePendingAggregationRequestsResponseTypeDef = TypedDict(
    "ClientDescribePendingAggregationRequestsResponseTypeDef",
    {
        "PendingAggregationRequests": List[
            ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef = TypedDict(
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)

ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef = TypedDict(
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef",
    {
        "SsmControls": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)

ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef = TypedDict(
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef",
    {"Value": str},
    total=False,
)

ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef = TypedDict(
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef = TypedDict(
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef",
    {
        "ResourceValue": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef,
        "StaticValue": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef,
    },
    total=False,
)

ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef = TypedDict(
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef",
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

ClientDescribeRemediationConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeRemediationConfigurationsResponseTypeDef",
    {
        "RemediationConfigurations": List[
            ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef
        ]
    },
    total=False,
)

ClientDescribeRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "ClientDescribeRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)

ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef = TypedDict(
    "ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)

ClientDescribeRemediationExceptionsResponseTypeDef = TypedDict(
    "ClientDescribeRemediationExceptionsResponseTypeDef",
    {
        "RemediationExceptions": List[
            ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

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
    pass


ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef = TypedDict(
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef",
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

ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef = TypedDict(
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef",
    {
        "Name": str,
        "State": Literal["SUCCEEDED", "PENDING", "FAILED"],
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)

ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef = TypedDict(
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef",
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

ClientDescribeRemediationExecutionStatusResponseTypeDef = TypedDict(
    "ClientDescribeRemediationExecutionStatusResponseTypeDef",
    {
        "RemediationExecutionStatuses": List[
            ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef = TypedDict(
    "ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)

ClientDescribeRetentionConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeRetentionConfigurationsResponseTypeDef",
    {
        "RetentionConfigurations": List[
            ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)

ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)

ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef = TypedDict(
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef",
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

ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "AggregateEvaluationResults": List[
            ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef",
    {"AccountId": str, "AwsRegion": str},
    total=False,
)

ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef = TypedDict(
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)

ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef = TypedDict(
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef",
    {
        "GroupName": str,
        "ComplianceSummary": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef,
    },
    total=False,
)

ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef = TypedDict(
    "ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List[
            ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef = TypedDict(
    "ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef",
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

ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef = TypedDict(
    "ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef",
    {"GroupName": str, "ResourceCount": int},
    total=False,
)

ClientGetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "ClientGetAggregateDiscoveredResourceCountsResponseTypeDef",
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
    pass


ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef = TypedDict(
    "ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef",
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

ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef = TypedDict(
    "ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef",
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

ClientGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "ClientGetAggregateResourceConfigResponseTypeDef",
    {"ConfigurationItem": ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef},
    total=False,
)

ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)

ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)

ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef = TypedDict(
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef",
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

ClientGetComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "ClientGetComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "EvaluationResults": List[
            ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)

ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)

ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef = TypedDict(
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef",
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

ClientGetComplianceDetailsByResourceResponseTypeDef = TypedDict(
    "ClientGetComplianceDetailsByResourceResponseTypeDef",
    {
        "EvaluationResults": List[
            ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef = TypedDict(
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)

ClientGetComplianceSummaryByConfigRuleResponseTypeDef = TypedDict(
    "ClientGetComplianceSummaryByConfigRuleResponseTypeDef",
    {"ComplianceSummary": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef},
    total=False,
)

ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef = TypedDict(
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)

ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef = TypedDict(
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef",
    {
        "ResourceType": str,
        "ComplianceSummary": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef,
    },
    total=False,
)

ClientGetComplianceSummaryByResourceTypeResponseTypeDef = TypedDict(
    "ClientGetComplianceSummaryByResourceTypeResponseTypeDef",
    {
        "ComplianceSummariesByResourceType": List[
            ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef
        ]
    },
    total=False,
)

ClientGetConformancePackComplianceDetailsFiltersTypeDef = TypedDict(
    "ClientGetConformancePackComplianceDetailsFiltersTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ResourceType": str,
        "ResourceIds": List[str],
    },
    total=False,
)

ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)

ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)

ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef = TypedDict(
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef",
    {
        "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"],
        "EvaluationResultIdentifier": ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
        "Annotation": str,
    },
    total=False,
)

ClientGetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "ClientGetConformancePackComplianceDetailsResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleEvaluationResults": List[
            ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef = TypedDict(
    "ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
    },
    total=False,
)

ClientGetConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "ClientGetConformancePackComplianceSummaryResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List[
            ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef = TypedDict(
    "ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef",
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

ClientGetDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "ClientGetDiscoveredResourceCountsResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List[ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef = TypedDict(
    "ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef",
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

ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef = TypedDict(
    "ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef",
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

ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef = TypedDict(
    "ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    {
        "OrganizationConfigRuleDetailedStatus": List[
            ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef = TypedDict(
    "ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef",
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

ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef = TypedDict(
    "ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef",
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

ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef = TypedDict(
    "ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef = TypedDict(
    "ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef",
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

ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef = TypedDict(
    "ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef",
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

ClientGetResourceConfigHistoryResponseTypeDef = TypedDict(
    "ClientGetResourceConfigHistoryResponseTypeDef",
    {
        "configurationItems": List[ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListAggregateDiscoveredResourcesFiltersTypeDef = TypedDict(
    "ClientListAggregateDiscoveredResourcesFiltersTypeDef",
    {"AccountId": str, "ResourceId": str, "ResourceName": str, "Region": str},
    total=False,
)

ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef",
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

ClientListAggregateDiscoveredResourcesResponseTypeDef = TypedDict(
    "ClientListAggregateDiscoveredResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef = TypedDict(
    "ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef",
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

ClientListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ClientListDiscoveredResourcesResponseTypeDef",
    {
        "resourceIdentifiers": List[
            ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef = TypedDict(
    "ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)

ClientPutAggregationAuthorizationResponseTypeDef = TypedDict(
    "ClientPutAggregationAuthorizationResponseTypeDef",
    {
        "AggregationAuthorization": ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef
    },
    total=False,
)

ClientPutAggregationAuthorizationTagsTypeDef = TypedDict(
    "ClientPutAggregationAuthorizationTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientPutConfigRuleConfigRuleScopeTypeDef = TypedDict(
    "ClientPutConfigRuleConfigRuleScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)

ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef = TypedDict(
    "ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef",
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

ClientPutConfigRuleConfigRuleSourceTypeDef = TypedDict(
    "ClientPutConfigRuleConfigRuleSourceTypeDef",
    {
        "Owner": Literal["CUSTOM_LAMBDA", "AWS"],
        "SourceIdentifier": str,
        "SourceDetails": List[ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef],
    },
    total=False,
)

ClientPutConfigRuleConfigRuleTypeDef = TypedDict(
    "ClientPutConfigRuleConfigRuleTypeDef",
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

ClientPutConfigRuleTagsTypeDef = TypedDict(
    "ClientPutConfigRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

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
    pass


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
    pass


ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef = TypedDict(
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)

ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef = TypedDict(
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)

ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef = TypedDict(
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef",
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

ClientPutConfigurationAggregatorResponseTypeDef = TypedDict(
    "ClientPutConfigurationAggregatorResponseTypeDef",
    {
        "ConfigurationAggregator": ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef
    },
    total=False,
)

ClientPutConfigurationAggregatorTagsTypeDef = TypedDict(
    "ClientPutConfigurationAggregatorTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef = TypedDict(
    "ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef",
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

ClientPutConfigurationRecorderConfigurationRecorderTypeDef = TypedDict(
    "ClientPutConfigurationRecorderConfigurationRecorderTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef,
    },
    total=False,
)

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
    pass


ClientPutConformancePackResponseTypeDef = TypedDict(
    "ClientPutConformancePackResponseTypeDef", {"ConformancePackArn": str}, total=False
)

ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    },
    total=False,
)

ClientPutDeliveryChannelDeliveryChannelTypeDef = TypedDict(
    "ClientPutDeliveryChannelDeliveryChannelTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef,
    },
    total=False,
)

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
    pass


ClientPutEvaluationsResponseFailedEvaluationsTypeDef = TypedDict(
    "ClientPutEvaluationsResponseFailedEvaluationsTypeDef",
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

ClientPutEvaluationsResponseTypeDef = TypedDict(
    "ClientPutEvaluationsResponseTypeDef",
    {"FailedEvaluations": List[ClientPutEvaluationsResponseFailedEvaluationsTypeDef]},
    total=False,
)

ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef",
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

ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef",
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

ClientPutOrganizationConfigRuleResponseTypeDef = TypedDict(
    "ClientPutOrganizationConfigRuleResponseTypeDef",
    {"OrganizationConfigRuleArn": str},
    total=False,
)

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
    pass


ClientPutOrganizationConformancePackResponseTypeDef = TypedDict(
    "ClientPutOrganizationConformancePackResponseTypeDef",
    {"OrganizationConformancePackArn": str},
    total=False,
)

ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)

ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef",
    {
        "SsmControls": ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)

ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef",
    {"Value": str},
    total=False,
)

ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef",
    {
        "ResourceValue": ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef,
        "StaticValue": ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef,
    },
    total=False,
)

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
    pass


ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)

ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef",
    {
        "SsmControls": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)

ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef",
    {"Value": str},
    total=False,
)

ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef",
    {
        "ResourceValue": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef,
        "StaticValue": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef,
    },
    total=False,
)

ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef",
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

ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[
            ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef
        ],
    },
    total=False,
)

ClientPutRemediationConfigurationsResponseTypeDef = TypedDict(
    "ClientPutRemediationConfigurationsResponseTypeDef",
    {"FailedBatches": List[ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef]},
    total=False,
)

ClientPutRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "ClientPutRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)

ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)

ClientPutRemediationExceptionsResponseFailedBatchesTypeDef = TypedDict(
    "ClientPutRemediationExceptionsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef],
    },
    total=False,
)

ClientPutRemediationExceptionsResponseTypeDef = TypedDict(
    "ClientPutRemediationExceptionsResponseTypeDef",
    {"FailedBatches": List[ClientPutRemediationExceptionsResponseFailedBatchesTypeDef]},
    total=False,
)

ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef = TypedDict(
    "ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)

ClientPutRetentionConfigurationResponseTypeDef = TypedDict(
    "ClientPutRetentionConfigurationResponseTypeDef",
    {
        "RetentionConfiguration": ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef
    },
    total=False,
)

ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef = TypedDict(
    "ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef", {"Name": str}, total=False
)

ClientSelectResourceConfigResponseQueryInfoTypeDef = TypedDict(
    "ClientSelectResourceConfigResponseQueryInfoTypeDef",
    {"SelectFields": List[ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef]},
    total=False,
)

ClientSelectResourceConfigResponseTypeDef = TypedDict(
    "ClientSelectResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": ClientSelectResourceConfigResponseQueryInfoTypeDef,
        "NextToken": str,
    },
    total=False,
)

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
    pass


ClientStartRemediationExecutionResponseFailedItemsTypeDef = TypedDict(
    "ClientStartRemediationExecutionResponseFailedItemsTypeDef",
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

ClientStartRemediationExecutionResponseTypeDef = TypedDict(
    "ClientStartRemediationExecutionResponseTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[ClientStartRemediationExecutionResponseFailedItemsTypeDef],
    },
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef",
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

DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)

DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List[
            DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef
        ]
    },
    total=False,
)

DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)

DescribeAggregationAuthorizationsPaginateResponseTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsPaginateResponseTypeDef",
    {
        "AggregationAuthorizations": List[
            DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef
        ]
    },
    total=False,
)

DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)

DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef = TypedDict(
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef,
    },
    total=False,
)

DescribeComplianceByConfigRulePaginateResponseTypeDef = TypedDict(
    "DescribeComplianceByConfigRulePaginateResponseTypeDef",
    {
        "ComplianceByConfigRules": List[
            DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef
        ]
    },
    total=False,
)

DescribeComplianceByResourcePaginatePaginationConfigTypeDef = TypedDict(
    "DescribeComplianceByResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef = TypedDict(
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)

DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef = TypedDict(
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)

DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef = TypedDict(
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef,
    },
    total=False,
)

DescribeComplianceByResourcePaginateResponseTypeDef = TypedDict(
    "DescribeComplianceByResourcePaginateResponseTypeDef",
    {
        "ComplianceByResources": List[
            DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef
        ]
    },
    total=False,
)

DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef",
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

DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List[
            DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef
        ]
    },
    total=False,
)

DescribeConfigRulesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeConfigRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef = TypedDict(
    "DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)

DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef = TypedDict(
    "DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef",
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

DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef = TypedDict(
    "DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef",
    {
        "Owner": Literal["CUSTOM_LAMBDA", "AWS"],
        "SourceIdentifier": str,
        "SourceDetails": List[
            DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef
        ],
    },
    total=False,
)

DescribeConfigRulesPaginateResponseConfigRulesTypeDef = TypedDict(
    "DescribeConfigRulesPaginateResponseConfigRulesTypeDef",
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

DescribeConfigRulesPaginateResponseTypeDef = TypedDict(
    "DescribeConfigRulesPaginateResponseTypeDef",
    {"ConfigRules": List[DescribeConfigRulesPaginateResponseConfigRulesTypeDef]},
    total=False,
)

DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef",
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

DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef",
    {
        "AggregatedSourceStatusList": List[
            DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef
        ]
    },
    total=False,
)

DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)

DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)

DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef",
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

DescribeConfigurationAggregatorsPaginateResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsPaginateResponseTypeDef",
    {
        "ConfigurationAggregators": List[
            DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef
        ]
    },
    total=False,
)

DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef = TypedDict(
    "DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef",
    {"RequesterAccountId": str, "RequesterAwsRegion": str},
    total=False,
)

DescribePendingAggregationRequestsPaginateResponseTypeDef = TypedDict(
    "DescribePendingAggregationRequestsPaginateResponseTypeDef",
    {
        "PendingAggregationRequests": List[
            DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef
        ]
    },
    total=False,
)

DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

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
    pass


DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef",
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

DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef",
    {
        "Name": str,
        "State": Literal["SUCCEEDED", "PENDING", "FAILED"],
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)

DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef",
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

DescribeRemediationExecutionStatusPaginateResponseTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusPaginateResponseTypeDef",
    {
        "RemediationExecutionStatuses": List[
            DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef
        ]
    },
    total=False,
)

DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef = TypedDict(
    "DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)

DescribeRetentionConfigurationsPaginateResponseTypeDef = TypedDict(
    "DescribeRetentionConfigurationsPaginateResponseTypeDef",
    {
        "RetentionConfigurations": List[
            DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef
        ]
    },
    total=False,
)

GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)

GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)

GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef",
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

GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef",
    {
        "AggregateEvaluationResults": List[
            GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef
        ]
    },
    total=False,
)

GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)

GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)

GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef",
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

GetComplianceDetailsByConfigRulePaginateResponseTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRulePaginateResponseTypeDef",
    {
        "EvaluationResults": List[
            GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef
        ]
    },
    total=False,
)

GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef = TypedDict(
    "GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)

GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)

GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef = TypedDict(
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef",
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

GetComplianceDetailsByResourcePaginateResponseTypeDef = TypedDict(
    "GetComplianceDetailsByResourcePaginateResponseTypeDef",
    {
        "EvaluationResults": List[
            GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef
        ]
    },
    total=False,
)

GetResourceConfigHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "GetResourceConfigHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef = TypedDict(
    "GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef",
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

GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef = TypedDict(
    "GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef",
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

GetResourceConfigHistoryPaginateResponseTypeDef = TypedDict(
    "GetResourceConfigHistoryPaginateResponseTypeDef",
    {
        "configurationItems": List[
            GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListAggregateDiscoveredResourcesPaginateFiltersTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesPaginateFiltersTypeDef",
    {"AccountId": str, "ResourceId": str, "ResourceName": str, "Region": str},
    total=False,
)

ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef",
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

ListAggregateDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesPaginateResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef
        ]
    },
    total=False,
)

ListDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef = TypedDict(
    "ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef",
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

ListDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesPaginateResponseTypeDef",
    {
        "resourceIdentifiers": List[
            ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)
