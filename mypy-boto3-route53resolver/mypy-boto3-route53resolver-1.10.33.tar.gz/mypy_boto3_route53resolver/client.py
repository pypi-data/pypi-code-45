"Main interface for route53resolver service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_route53resolver.client as client_scope

# pylint: disable=import-self
import mypy_boto3_route53resolver.paginator as paginator_scope
from mypy_boto3_route53resolver.type_defs import (
    ClientAssociateResolverEndpointIpAddressIpAddressTypeDef,
    ClientAssociateResolverEndpointIpAddressResponseTypeDef,
    ClientAssociateResolverRuleResponseTypeDef,
    ClientCreateResolverEndpointIpAddressesTypeDef,
    ClientCreateResolverEndpointResponseTypeDef,
    ClientCreateResolverEndpointTagsTypeDef,
    ClientCreateResolverRuleResponseTypeDef,
    ClientCreateResolverRuleTagsTypeDef,
    ClientCreateResolverRuleTargetIpsTypeDef,
    ClientDeleteResolverEndpointResponseTypeDef,
    ClientDeleteResolverRuleResponseTypeDef,
    ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef,
    ClientDisassociateResolverEndpointIpAddressResponseTypeDef,
    ClientDisassociateResolverRuleResponseTypeDef,
    ClientGetResolverEndpointResponseTypeDef,
    ClientGetResolverRuleAssociationResponseTypeDef,
    ClientGetResolverRulePolicyResponseTypeDef,
    ClientGetResolverRuleResponseTypeDef,
    ClientListResolverEndpointIpAddressesResponseTypeDef,
    ClientListResolverEndpointsFiltersTypeDef,
    ClientListResolverEndpointsResponseTypeDef,
    ClientListResolverRuleAssociationsFiltersTypeDef,
    ClientListResolverRuleAssociationsResponseTypeDef,
    ClientListResolverRulesFiltersTypeDef,
    ClientListResolverRulesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutResolverRulePolicyResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateResolverEndpointResponseTypeDef,
    ClientUpdateResolverRuleConfigTypeDef,
    ClientUpdateResolverRuleResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [Route53Resolver.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_resolver_endpoint_ip_address(
        self,
        ResolverEndpointId: str,
        IpAddress: ClientAssociateResolverEndpointIpAddressIpAddressTypeDef,
    ) -> ClientAssociateResolverEndpointIpAddressResponseTypeDef:
        """
        [Client.associate_resolver_endpoint_ip_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_endpoint_ip_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_resolver_rule(
        self, ResolverRuleId: str, VPCId: str, Name: str = None
    ) -> ClientAssociateResolverRuleResponseTypeDef:
        """
        [Client.associate_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resolver_endpoint(
        self,
        CreatorRequestId: str,
        SecurityGroupIds: List[str],
        Direction: Literal["INBOUND", "OUTBOUND"],
        IpAddresses: List[ClientCreateResolverEndpointIpAddressesTypeDef],
        Name: str = None,
        Tags: List[ClientCreateResolverEndpointTagsTypeDef] = None,
    ) -> ClientCreateResolverEndpointResponseTypeDef:
        """
        [Client.create_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resolver_rule(
        self,
        CreatorRequestId: str,
        RuleType: Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        DomainName: str,
        Name: str = None,
        TargetIps: List[ClientCreateResolverRuleTargetIpsTypeDef] = None,
        ResolverEndpointId: str = None,
        Tags: List[ClientCreateResolverRuleTagsTypeDef] = None,
    ) -> ClientCreateResolverRuleResponseTypeDef:
        """
        [Client.create_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resolver_endpoint(
        self, ResolverEndpointId: str
    ) -> ClientDeleteResolverEndpointResponseTypeDef:
        """
        [Client.delete_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resolver_rule(self, ResolverRuleId: str) -> ClientDeleteResolverRuleResponseTypeDef:
        """
        [Client.delete_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_resolver_endpoint_ip_address(
        self,
        ResolverEndpointId: str,
        IpAddress: ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef,
    ) -> ClientDisassociateResolverEndpointIpAddressResponseTypeDef:
        """
        [Client.disassociate_resolver_endpoint_ip_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_endpoint_ip_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_resolver_rule(
        self, VPCId: str, ResolverRuleId: str
    ) -> ClientDisassociateResolverRuleResponseTypeDef:
        """
        [Client.disassociate_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_rule)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resolver_endpoint(
        self, ResolverEndpointId: str
    ) -> ClientGetResolverEndpointResponseTypeDef:
        """
        [Client.get_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resolver_rule(self, ResolverRuleId: str) -> ClientGetResolverRuleResponseTypeDef:
        """
        [Client.get_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resolver_rule_association(
        self, ResolverRuleAssociationId: str
    ) -> ClientGetResolverRuleAssociationResponseTypeDef:
        """
        [Client.get_resolver_rule_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resolver_rule_policy(self, Arn: str) -> ClientGetResolverRulePolicyResponseTypeDef:
        """
        [Client.get_resolver_rule_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resolver_endpoint_ip_addresses(
        self, ResolverEndpointId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListResolverEndpointIpAddressesResponseTypeDef:
        """
        [Client.list_resolver_endpoint_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoint_ip_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resolver_endpoints(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListResolverEndpointsFiltersTypeDef] = None,
    ) -> ClientListResolverEndpointsResponseTypeDef:
        """
        [Client.list_resolver_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resolver_rule_associations(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListResolverRuleAssociationsFiltersTypeDef] = None,
    ) -> ClientListResolverRuleAssociationsResponseTypeDef:
        """
        [Client.list_resolver_rule_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rule_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resolver_rules(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListResolverRulesFiltersTypeDef] = None,
    ) -> ClientListResolverRulesResponseTypeDef:
        """
        [Client.list_resolver_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_resolver_rule_policy(
        self, Arn: str, ResolverRulePolicy: str
    ) -> ClientPutResolverRulePolicyResponseTypeDef:
        """
        [Client.put_resolver_rule_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.put_resolver_rule_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resolver_endpoint(
        self, ResolverEndpointId: str, Name: str = None
    ) -> ClientUpdateResolverEndpointResponseTypeDef:
        """
        [Client.update_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resolver_rule(
        self, ResolverRuleId: str, Config: ClientUpdateResolverRuleConfigTypeDef
    ) -> ClientUpdateResolverRuleResponseTypeDef:
        """
        [Client.update_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_rule)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53resolver.html#Route53Resolver.Paginator.ListTagsForResource)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidPolicyDocument: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidTagException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnknownResourceException: Boto3ClientError
