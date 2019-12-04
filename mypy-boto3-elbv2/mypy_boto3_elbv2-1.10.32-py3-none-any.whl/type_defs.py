"Main interface for elbv2 service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddListenerCertificatesCertificatesTypeDef",
    "ClientAddListenerCertificatesResponseCertificatesTypeDef",
    "ClientAddListenerCertificatesResponseTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCreateListenerCertificatesTypeDef",
    "ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTypeDef",
    "ClientCreateListenerDefaultActionsRedirectConfigTypeDef",
    "ClientCreateListenerDefaultActionsTypeDef",
    "ClientCreateListenerResponseListenersCertificatesTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsTypeDef",
    "ClientCreateListenerResponseListenersTypeDef",
    "ClientCreateListenerResponseTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersTypeDef",
    "ClientCreateLoadBalancerResponseTypeDef",
    "ClientCreateLoadBalancerSubnetMappingsTypeDef",
    "ClientCreateLoadBalancerTagsTypeDef",
    "ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateRuleActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateRuleActionsFixedResponseConfigTypeDef",
    "ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateRuleActionsForwardConfigTypeDef",
    "ClientCreateRuleActionsRedirectConfigTypeDef",
    "ClientCreateRuleActionsTypeDef",
    "ClientCreateRuleConditionsHostHeaderConfigTypeDef",
    "ClientCreateRuleConditionsHttpHeaderConfigTypeDef",
    "ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef",
    "ClientCreateRuleConditionsPathPatternConfigTypeDef",
    "ClientCreateRuleConditionsQueryStringConfigValuesTypeDef",
    "ClientCreateRuleConditionsQueryStringConfigTypeDef",
    "ClientCreateRuleConditionsSourceIpConfigTypeDef",
    "ClientCreateRuleConditionsTypeDef",
    "ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsTypeDef",
    "ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsTypeDef",
    "ClientCreateRuleResponseRulesTypeDef",
    "ClientCreateRuleResponseTypeDef",
    "ClientCreateTargetGroupMatcherTypeDef",
    "ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef",
    "ClientCreateTargetGroupResponseTargetGroupsTypeDef",
    "ClientCreateTargetGroupResponseTypeDef",
    "ClientDeregisterTargetsTargetsTypeDef",
    "ClientDescribeAccountLimitsResponseLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeListenerCertificatesResponseCertificatesTypeDef",
    "ClientDescribeListenerCertificatesResponseTypeDef",
    "ClientDescribeListenersResponseListenersCertificatesTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsTypeDef",
    "ClientDescribeListenersResponseListenersTypeDef",
    "ClientDescribeListenersResponseTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsTypeDef",
    "ClientDescribeRulesResponseRulesTypeDef",
    "ClientDescribeRulesResponseTypeDef",
    "ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef",
    "ClientDescribeSslPoliciesResponseSslPoliciesTypeDef",
    "ClientDescribeSslPoliciesResponseTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeTargetGroupAttributesResponseAttributesTypeDef",
    "ClientDescribeTargetGroupAttributesResponseTypeDef",
    "ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef",
    "ClientDescribeTargetGroupsResponseTargetGroupsTypeDef",
    "ClientDescribeTargetGroupsResponseTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef",
    "ClientDescribeTargetHealthResponseTypeDef",
    "ClientDescribeTargetHealthTargetsTypeDef",
    "ClientModifyListenerCertificatesTypeDef",
    "ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTypeDef",
    "ClientModifyListenerDefaultActionsRedirectConfigTypeDef",
    "ClientModifyListenerDefaultActionsTypeDef",
    "ClientModifyListenerResponseListenersCertificatesTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsTypeDef",
    "ClientModifyListenerResponseListenersTypeDef",
    "ClientModifyListenerResponseTypeDef",
    "ClientModifyLoadBalancerAttributesAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    "ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyRuleActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyRuleActionsFixedResponseConfigTypeDef",
    "ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyRuleActionsForwardConfigTypeDef",
    "ClientModifyRuleActionsRedirectConfigTypeDef",
    "ClientModifyRuleActionsTypeDef",
    "ClientModifyRuleConditionsHostHeaderConfigTypeDef",
    "ClientModifyRuleConditionsHttpHeaderConfigTypeDef",
    "ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef",
    "ClientModifyRuleConditionsPathPatternConfigTypeDef",
    "ClientModifyRuleConditionsQueryStringConfigValuesTypeDef",
    "ClientModifyRuleConditionsQueryStringConfigTypeDef",
    "ClientModifyRuleConditionsSourceIpConfigTypeDef",
    "ClientModifyRuleConditionsTypeDef",
    "ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsTypeDef",
    "ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsTypeDef",
    "ClientModifyRuleResponseRulesTypeDef",
    "ClientModifyRuleResponseTypeDef",
    "ClientModifyTargetGroupAttributesAttributesTypeDef",
    "ClientModifyTargetGroupAttributesResponseAttributesTypeDef",
    "ClientModifyTargetGroupAttributesResponseTypeDef",
    "ClientModifyTargetGroupMatcherTypeDef",
    "ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef",
    "ClientModifyTargetGroupResponseTargetGroupsTypeDef",
    "ClientModifyTargetGroupResponseTypeDef",
    "ClientRegisterTargetsTargetsTypeDef",
    "ClientRemoveListenerCertificatesCertificatesTypeDef",
    "ClientSetIpAddressTypeResponseTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsTypeDef",
    "ClientSetRulePrioritiesResponseRulesTypeDef",
    "ClientSetRulePrioritiesResponseTypeDef",
    "ClientSetRulePrioritiesRulePrioritiesTypeDef",
    "ClientSetSecurityGroupsResponseTypeDef",
    "ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientSetSubnetsResponseAvailabilityZonesTypeDef",
    "ClientSetSubnetsResponseTypeDef",
    "ClientSetSubnetsSubnetMappingsTypeDef",
    "DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    "DescribeAccountLimitsPaginateResponseLimitsTypeDef",
    "DescribeAccountLimitsPaginateResponseTypeDef",
    "DescribeListenerCertificatesPaginatePaginationConfigTypeDef",
    "DescribeListenerCertificatesPaginateResponseCertificatesTypeDef",
    "DescribeListenerCertificatesPaginateResponseTypeDef",
    "DescribeListenersPaginatePaginationConfigTypeDef",
    "DescribeListenersPaginateResponseListenersCertificatesTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsTypeDef",
    "DescribeListenersPaginateResponseListenersTypeDef",
    "DescribeListenersPaginateResponseTypeDef",
    "DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    "DescribeLoadBalancersPaginateResponseTypeDef",
    "DescribeRulesPaginatePaginationConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsTypeDef",
    "DescribeRulesPaginateResponseRulesTypeDef",
    "DescribeRulesPaginateResponseTypeDef",
    "DescribeSSLPoliciesPaginatePaginationConfigTypeDef",
    "DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef",
    "DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef",
    "DescribeSSLPoliciesPaginateResponseTypeDef",
    "DescribeTargetGroupsPaginatePaginationConfigTypeDef",
    "DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef",
    "DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef",
    "DescribeTargetGroupsPaginateResponseTypeDef",
    "LoadBalancerAvailableWaitWaiterConfigTypeDef",
    "LoadBalancerExistsWaitWaiterConfigTypeDef",
    "LoadBalancersDeletedWaitWaiterConfigTypeDef",
    "TargetDeregisteredWaitTargetsTypeDef",
    "TargetDeregisteredWaitWaiterConfigTypeDef",
    "TargetInServiceWaitTargetsTypeDef",
    "TargetInServiceWaitWaiterConfigTypeDef",
)


_ClientAddListenerCertificatesCertificatesTypeDef = TypedDict(
    "_ClientAddListenerCertificatesCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientAddListenerCertificatesCertificatesTypeDef(
    _ClientAddListenerCertificatesCertificatesTypeDef
):
    """
    - *(dict) --*

      Information about an SSL server certificate.
      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate.
    """


_ClientAddListenerCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientAddListenerCertificatesResponseCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientAddListenerCertificatesResponseCertificatesTypeDef(
    _ClientAddListenerCertificatesResponseCertificatesTypeDef
):
    """
    - *(dict) --*

      Information about an SSL server certificate.
      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate.
    """


_ClientAddListenerCertificatesResponseTypeDef = TypedDict(
    "_ClientAddListenerCertificatesResponseTypeDef",
    {"Certificates": List[ClientAddListenerCertificatesResponseCertificatesTypeDef]},
    total=False,
)


class ClientAddListenerCertificatesResponseTypeDef(_ClientAddListenerCertificatesResponseTypeDef):
    """
    - *(dict) --*

      - **Certificates** *(list) --*

        Information about the certificates in the certificate list.
        - *(dict) --*

          Information about an SSL server certificate.
          - **CertificateArn** *(string) --*

            The Amazon Resource Name (ARN) of the certificate.
    """


_RequiredClientAddTagsTagsTypeDef = TypedDict("_RequiredClientAddTagsTagsTypeDef", {"Key": str})
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientCreateListenerCertificatesTypeDef = TypedDict(
    "_ClientCreateListenerCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientCreateListenerCertificatesTypeDef(_ClientCreateListenerCertificatesTypeDef):
    """
    - *(dict) --*

      Information about an SSL server certificate.
      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate.
    """


_ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef(
    _ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef(
    _ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef(
    _ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef
):
    pass


_ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientCreateListenerDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerDefaultActionsForwardConfigTypeDef(
    _ClientCreateListenerDefaultActionsForwardConfigTypeDef
):
    pass


_ClientCreateListenerDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientCreateListenerDefaultActionsRedirectConfigTypeDef(
    _ClientCreateListenerDefaultActionsRedirectConfigTypeDef
):
    pass


_RequiredClientCreateListenerDefaultActionsTypeDef = TypedDict(
    "_RequiredClientCreateListenerDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalClientCreateListenerDefaultActionsTypeDef = TypedDict(
    "_OptionalClientCreateListenerDefaultActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateListenerDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateListenerDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerDefaultActionsTypeDef(
    _RequiredClientCreateListenerDefaultActionsTypeDef,
    _OptionalClientCreateListenerDefaultActionsTypeDef,
):
    """
    - *(dict) --*

      Information about an action.
      - **Type** *(string) --***[REQUIRED]**

        The type of action.
    """


_ClientCreateListenerResponseListenersCertificatesTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientCreateListenerResponseListenersCertificatesTypeDef(
    _ClientCreateListenerResponseListenersCertificatesTypeDef
):
    pass


_ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef
):
    pass


_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef
):
    pass


_ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef
):
    pass


_ClientCreateListenerResponseListenersDefaultActionsTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsTypeDef
):
    pass


_ClientCreateListenerResponseListenersTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List[ClientCreateListenerResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[ClientCreateListenerResponseListenersDefaultActionsTypeDef],
    },
    total=False,
)


class ClientCreateListenerResponseListenersTypeDef(_ClientCreateListenerResponseListenersTypeDef):
    """
    - *(dict) --*

      Information about a listener.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_ClientCreateListenerResponseTypeDef = TypedDict(
    "_ClientCreateListenerResponseTypeDef",
    {"Listeners": List[ClientCreateListenerResponseListenersTypeDef]},
    total=False,
)


class ClientCreateListenerResponseTypeDef(_ClientCreateListenerResponseTypeDef):
    """
    - *(dict) --*

      - **Listeners** *(list) --*

        Information about the listener.
        - *(dict) --*

          Information about a listener.
          - **ListenerArn** *(string) --*

            The Amazon Resource Name (ARN) of the listener.
    """


_ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)


class ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef(
    _ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
):
    pass


_ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)


class ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef(
    _ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef
):
    pass


_ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef",
    {"Code": Literal["active", "provisioning", "active_impaired", "failed"], "Reason": str},
    total=False,
)


class ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef(
    _ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef
):
    pass


_ClientCreateLoadBalancerResponseLoadBalancersTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseLoadBalancersTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": Literal["internet-facing", "internal"],
        "VpcId": str,
        "State": ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef,
        "Type": Literal["application", "network"],
        "AvailabilityZones": List[
            ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef
        ],
        "SecurityGroups": List[str],
        "IpAddressType": Literal["ipv4", "dualstack"],
    },
    total=False,
)


class ClientCreateLoadBalancerResponseLoadBalancersTypeDef(
    _ClientCreateLoadBalancerResponseLoadBalancersTypeDef
):
    """
    - *(dict) --*

      Information about a load balancer.
      - **LoadBalancerArn** *(string) --*

        The Amazon Resource Name (ARN) of the load balancer.
    """


_ClientCreateLoadBalancerResponseTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseTypeDef",
    {"LoadBalancers": List[ClientCreateLoadBalancerResponseLoadBalancersTypeDef]},
    total=False,
)


class ClientCreateLoadBalancerResponseTypeDef(_ClientCreateLoadBalancerResponseTypeDef):
    """
    - *(dict) --*

      - **LoadBalancers** *(list) --*

        Information about the load balancer.
        - *(dict) --*

          Information about a load balancer.
          - **LoadBalancerArn** *(string) --*

            The Amazon Resource Name (ARN) of the load balancer.
    """


_ClientCreateLoadBalancerSubnetMappingsTypeDef = TypedDict(
    "_ClientCreateLoadBalancerSubnetMappingsTypeDef",
    {"SubnetId": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)


class ClientCreateLoadBalancerSubnetMappingsTypeDef(_ClientCreateLoadBalancerSubnetMappingsTypeDef):
    """
    - *(dict) --*

      Information about a subnet mapping.
      - **SubnetId** *(string) --*

        The ID of the subnet.
    """


_RequiredClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLoadBalancerTagsTypeDef(
    _RequiredClientCreateLoadBalancerTagsTypeDef, _OptionalClientCreateLoadBalancerTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef(
    _ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientCreateRuleActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientCreateRuleActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientCreateRuleActionsAuthenticateOidcConfigTypeDef(
    _ClientCreateRuleActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientCreateRuleActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientCreateRuleActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientCreateRuleActionsFixedResponseConfigTypeDef(
    _ClientCreateRuleActionsFixedResponseConfigTypeDef
):
    pass


_ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef(
    _ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientCreateRuleActionsForwardConfigTypeDef = TypedDict(
    "_ClientCreateRuleActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleActionsForwardConfigTypeDef(_ClientCreateRuleActionsForwardConfigTypeDef):
    pass


_ClientCreateRuleActionsRedirectConfigTypeDef = TypedDict(
    "_ClientCreateRuleActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientCreateRuleActionsRedirectConfigTypeDef(_ClientCreateRuleActionsRedirectConfigTypeDef):
    pass


_RequiredClientCreateRuleActionsTypeDef = TypedDict(
    "_RequiredClientCreateRuleActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalClientCreateRuleActionsTypeDef = TypedDict(
    "_OptionalClientCreateRuleActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateRuleActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateRuleActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateRuleActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateRuleActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleActionsTypeDef(
    _RequiredClientCreateRuleActionsTypeDef, _OptionalClientCreateRuleActionsTypeDef
):
    """
    - *(dict) --*

      Information about an action.
      - **Type** *(string) --***[REQUIRED]**

        The type of action.
    """


_ClientCreateRuleConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsHostHeaderConfigTypeDef", {"Values": List[str]}, total=False
)


class ClientCreateRuleConditionsHostHeaderConfigTypeDef(
    _ClientCreateRuleConditionsHostHeaderConfigTypeDef
):
    pass


_ClientCreateRuleConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientCreateRuleConditionsHttpHeaderConfigTypeDef(
    _ClientCreateRuleConditionsHttpHeaderConfigTypeDef
):
    pass


_ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef", {"Values": List[str]}, total=False
)


class ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef(
    _ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef
):
    pass


_ClientCreateRuleConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsPathPatternConfigTypeDef", {"Values": List[str]}, total=False
)


class ClientCreateRuleConditionsPathPatternConfigTypeDef(
    _ClientCreateRuleConditionsPathPatternConfigTypeDef
):
    pass


_ClientCreateRuleConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientCreateRuleConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateRuleConditionsQueryStringConfigValuesTypeDef(
    _ClientCreateRuleConditionsQueryStringConfigValuesTypeDef
):
    pass


_ClientCreateRuleConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientCreateRuleConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class ClientCreateRuleConditionsQueryStringConfigTypeDef(
    _ClientCreateRuleConditionsQueryStringConfigTypeDef
):
    pass


_ClientCreateRuleConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsSourceIpConfigTypeDef", {"Values": List[str]}, total=False
)


class ClientCreateRuleConditionsSourceIpConfigTypeDef(
    _ClientCreateRuleConditionsSourceIpConfigTypeDef
):
    pass


_ClientCreateRuleConditionsTypeDef = TypedDict(
    "_ClientCreateRuleConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientCreateRuleConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientCreateRuleConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientCreateRuleConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientCreateRuleConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientCreateRuleConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleConditionsTypeDef(_ClientCreateRuleConditionsTypeDef):
    """
    - *(dict) --*

      Information about a condition for a rule.
      - **Field** *(string) --*

        The field in the HTTP request. The following are the possible values:
        * ``http-header``
        * ``http-request-method``
        * ``host-header``
        * ``path-pattern``
        * ``query-string``
        * ``source-ip``
    """


_ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientCreateRuleResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsForwardConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsForwardConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesActionsTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateRuleResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsTypeDef(_ClientCreateRuleResponseRulesActionsTypeDef):
    pass


_ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    pass


_ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef
):
    pass


_ClientCreateRuleResponseRulesConditionsTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleResponseRulesConditionsTypeDef(
    _ClientCreateRuleResponseRulesConditionsTypeDef
):
    pass


_ClientCreateRuleResponseRulesTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientCreateRuleResponseRulesConditionsTypeDef],
        "Actions": List[ClientCreateRuleResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class ClientCreateRuleResponseRulesTypeDef(_ClientCreateRuleResponseRulesTypeDef):
    """
    - *(dict) --*

      Information about a rule.
      - **RuleArn** *(string) --*

        The Amazon Resource Name (ARN) of the rule.
    """


_ClientCreateRuleResponseTypeDef = TypedDict(
    "_ClientCreateRuleResponseTypeDef",
    {"Rules": List[ClientCreateRuleResponseRulesTypeDef]},
    total=False,
)


class ClientCreateRuleResponseTypeDef(_ClientCreateRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        Information about the rule.
        - *(dict) --*

          Information about a rule.
          - **RuleArn** *(string) --*

            The Amazon Resource Name (ARN) of the rule.
    """


_ClientCreateTargetGroupMatcherTypeDef = TypedDict(
    "_ClientCreateTargetGroupMatcherTypeDef", {"HttpCode": str}
)


class ClientCreateTargetGroupMatcherTypeDef(_ClientCreateTargetGroupMatcherTypeDef):
    """
    [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a
    target.
    - **HttpCode** *(string) --***[REQUIRED]**

      The HTTP codes.
      For Application Load Balancers, you can specify values between 200 and 499, and the default
      value is 200. You can specify multiple values (for example, "200,202") or a range of values
      (for example, "200-299").
      For Network Load Balancers, this is 200–399.
    """


_ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef = TypedDict(
    "_ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef", {"HttpCode": str}, total=False
)


class ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef(
    _ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef
):
    pass


_ClientCreateTargetGroupResponseTargetGroupsTypeDef = TypedDict(
    "_ClientCreateTargetGroupResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
    },
    total=False,
)


class ClientCreateTargetGroupResponseTargetGroupsTypeDef(
    _ClientCreateTargetGroupResponseTargetGroupsTypeDef
):
    """
    - *(dict) --*

      Information about a target group.
      - **TargetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the target group.
    """


_ClientCreateTargetGroupResponseTypeDef = TypedDict(
    "_ClientCreateTargetGroupResponseTypeDef",
    {"TargetGroups": List[ClientCreateTargetGroupResponseTargetGroupsTypeDef]},
    total=False,
)


class ClientCreateTargetGroupResponseTypeDef(_ClientCreateTargetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **TargetGroups** *(list) --*

        Information about the target group.
        - *(dict) --*

          Information about a target group.
          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.
    """


_RequiredClientDeregisterTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientDeregisterTargetsTargetsTypeDef", {"Id": str}
)
_OptionalClientDeregisterTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientDeregisterTargetsTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientDeregisterTargetsTargetsTypeDef(
    _RequiredClientDeregisterTargetsTargetsTypeDef, _OptionalClientDeregisterTargetsTargetsTypeDef
):
    """
    - *(dict) --*

      Information about a target.
      - **Id** *(string) --***[REQUIRED]**

        The ID of the target. If the target type of the target group is ``instance`` , specify an
        instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
        ``lambda`` , specify the ARN of the Lambda function.
    """


_ClientDescribeAccountLimitsResponseLimitsTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseLimitsTypeDef", {"Name": str, "Max": str}, total=False
)


class ClientDescribeAccountLimitsResponseLimitsTypeDef(
    _ClientDescribeAccountLimitsResponseLimitsTypeDef
):
    """
    - *(dict) --*

      Information about an Elastic Load Balancing resource limit for your AWS account.
      - **Name** *(string) --*

        The name of the limit. The possible values are:
        * application-load-balancers
        * listeners-per-application-load-balancer
        * listeners-per-network-load-balancer
        * network-load-balancers
        * rules-per-application-load-balancer
        * target-groups
        * target-groups-per-action-on-application-load-balancer
        * target-groups-per-action-on-network-load-balancer
        * target-groups-per-application-load-balancer
        * targets-per-application-load-balancer
        * targets-per-availability-zone-per-network-load-balancer
        * targets-per-network-load-balancer
    """


_ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseTypeDef",
    {"Limits": List[ClientDescribeAccountLimitsResponseLimitsTypeDef], "NextMarker": str},
    total=False,
)


class ClientDescribeAccountLimitsResponseTypeDef(_ClientDescribeAccountLimitsResponseTypeDef):
    """
    - *(dict) --*

      - **Limits** *(list) --*

        Information about the limits.
        - *(dict) --*

          Information about an Elastic Load Balancing resource limit for your AWS account.
          - **Name** *(string) --*

            The name of the limit. The possible values are:
            * application-load-balancers
            * listeners-per-application-load-balancer
            * listeners-per-network-load-balancer
            * network-load-balancers
            * rules-per-application-load-balancer
            * target-groups
            * target-groups-per-action-on-application-load-balancer
            * target-groups-per-action-on-network-load-balancer
            * target-groups-per-application-load-balancer
            * targets-per-application-load-balancer
            * targets-per-availability-zone-per-network-load-balancer
            * targets-per-network-load-balancer
    """


_ClientDescribeListenerCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientDescribeListenerCertificatesResponseCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientDescribeListenerCertificatesResponseCertificatesTypeDef(
    _ClientDescribeListenerCertificatesResponseCertificatesTypeDef
):
    """
    - *(dict) --*

      Information about an SSL server certificate.
      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate.
    """


_ClientDescribeListenerCertificatesResponseTypeDef = TypedDict(
    "_ClientDescribeListenerCertificatesResponseTypeDef",
    {
        "Certificates": List[ClientDescribeListenerCertificatesResponseCertificatesTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeListenerCertificatesResponseTypeDef(
    _ClientDescribeListenerCertificatesResponseTypeDef
):
    """
    - *(dict) --*

      - **Certificates** *(list) --*

        Information about the certificates.
        - *(dict) --*

          Information about an SSL server certificate.
          - **CertificateArn** *(string) --*

            The Amazon Resource Name (ARN) of the certificate.
    """


_ClientDescribeListenersResponseListenersCertificatesTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientDescribeListenersResponseListenersCertificatesTypeDef(
    _ClientDescribeListenersResponseListenersCertificatesTypeDef
):
    pass


_ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef
):
    pass


_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef
):
    pass


_ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef
):
    pass


_ClientDescribeListenersResponseListenersDefaultActionsTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsTypeDef
):
    pass


_ClientDescribeListenersResponseListenersTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List[ClientDescribeListenersResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[ClientDescribeListenersResponseListenersDefaultActionsTypeDef],
    },
    total=False,
)


class ClientDescribeListenersResponseListenersTypeDef(
    _ClientDescribeListenersResponseListenersTypeDef
):
    """
    - *(dict) --*

      Information about a listener.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_ClientDescribeListenersResponseTypeDef = TypedDict(
    "_ClientDescribeListenersResponseTypeDef",
    {"Listeners": List[ClientDescribeListenersResponseListenersTypeDef], "NextMarker": str},
    total=False,
)


class ClientDescribeListenersResponseTypeDef(_ClientDescribeListenersResponseTypeDef):
    """
    - *(dict) --*

      - **Listeners** *(list) --*

        Information about the listeners.
        - *(dict) --*

          Information about a listener.
          - **ListenerArn** *(string) --*

            The Amazon Resource Name (ARN) of the listener.
    """


_ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      Information about a load balancer attribute.
      - **Key** *(string) --*

        The name of the attribute.
        The following attributes are supported by both Application Load Balancers and Network Load
        Balancers:
        * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
        ``true`` or ``false`` . The default is ``false`` .
        * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This attribute
        is required if access logs are enabled. The bucket must exist in the same region as the load
        balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to
        the bucket.
        * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access
        logs.
        * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The
        value is ``true`` or ``false`` . The default is ``false`` .
        The following attributes are supported by only Application Load Balancers:
        * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range is
        1-4000 seconds. The default is 60 seconds.
        * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers with
        invalid header fields are removed by the load balancer (``true`` ) or routed to targets
        (``false`` ). The default is ``false`` .
        * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true`` or
        ``false`` . The default is ``true`` .
        The following attributes are supported by only Network Load Balancers:
        * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
        enabled. The value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientDescribeLoadBalancerAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        Information about the load balancer attributes.
        - *(dict) --*

          Information about a load balancer attribute.
          - **Key** *(string) --*

            The name of the attribute.
            The following attributes are supported by both Application Load Balancers and Network
            Load Balancers:
            * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
            ``true`` or ``false`` . The default is ``false`` .
            * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This
            attribute is required if access logs are enabled. The bucket must exist in the same
            region as the load balancer and have a bucket policy that grants Elastic Load Balancing
            permissions to write to the bucket.
            * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the
            access logs.
            * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled.
            The value is ``true`` or ``false`` . The default is ``false`` .
            The following attributes are supported by only Application Load Balancers:
            * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range
            is 1-4000 seconds. The default is 60 seconds.
            * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers
            with invalid header fields are removed by the load balancer (``true`` ) or routed to
            targets (``false`` ). The default is ``false`` .
            * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true``
            or ``false`` . The default is ``true`` .
            The following attributes are supported by only Network Load Balancers:
            * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
            enabled. The value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef",
    {"Code": Literal["active", "provisioning", "active_impaired", "failed"], "Reason": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancersTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": Literal["internet-facing", "internal"],
        "VpcId": str,
        "State": ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef,
        "Type": Literal["application", "network"],
        "AvailabilityZones": List[
            ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef
        ],
        "SecurityGroups": List[str],
        "IpAddressType": Literal["ipv4", "dualstack"],
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersTypeDef
):
    """
    - *(dict) --*

      Information about a load balancer.
      - **LoadBalancerArn** *(string) --*

        The Amazon Resource Name (ARN) of the load balancer.
    """


_ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List[ClientDescribeLoadBalancersResponseLoadBalancersTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseTypeDef(_ClientDescribeLoadBalancersResponseTypeDef):
    """
    - *(dict) --*

      - **LoadBalancers** *(list) --*

        Information about the load balancers.
        - *(dict) --*

          Information about a load balancer.
          - **LoadBalancerArn** *(string) --*

            The Amazon Resource Name (ARN) of the load balancer.
    """


_ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesActionsTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsTypeDef(
    _ClientDescribeRulesResponseRulesActionsTypeDef
):
    pass


_ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    pass


_ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef
):
    pass


_ClientDescribeRulesResponseRulesConditionsTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsTypeDef(
    _ClientDescribeRulesResponseRulesConditionsTypeDef
):
    pass


_ClientDescribeRulesResponseRulesTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientDescribeRulesResponseRulesConditionsTypeDef],
        "Actions": List[ClientDescribeRulesResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesTypeDef(_ClientDescribeRulesResponseRulesTypeDef):
    """
    - *(dict) --*

      Information about a rule.
      - **RuleArn** *(string) --*

        The Amazon Resource Name (ARN) of the rule.
    """


_ClientDescribeRulesResponseTypeDef = TypedDict(
    "_ClientDescribeRulesResponseTypeDef",
    {"Rules": List[ClientDescribeRulesResponseRulesTypeDef], "NextMarker": str},
    total=False,
)


class ClientDescribeRulesResponseTypeDef(_ClientDescribeRulesResponseTypeDef):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        Information about the rules.
        - *(dict) --*

          Information about a rule.
          - **RuleArn** *(string) --*

            The Amazon Resource Name (ARN) of the rule.
    """


_ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef = TypedDict(
    "_ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef",
    {"Name": str, "Priority": int},
    total=False,
)


class ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef(
    _ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef
):
    pass


_ClientDescribeSslPoliciesResponseSslPoliciesTypeDef = TypedDict(
    "_ClientDescribeSslPoliciesResponseSslPoliciesTypeDef",
    {
        "SslProtocols": List[str],
        "Ciphers": List[ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef],
        "Name": str,
    },
    total=False,
)


class ClientDescribeSslPoliciesResponseSslPoliciesTypeDef(
    _ClientDescribeSslPoliciesResponseSslPoliciesTypeDef
):
    """
    - *(dict) --*

      Information about a policy used for SSL negotiation.
      - **SslProtocols** *(list) --*

        The protocols.
        - *(string) --*
    """


_ClientDescribeSslPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeSslPoliciesResponseTypeDef",
    {"SslPolicies": List[ClientDescribeSslPoliciesResponseSslPoliciesTypeDef], "NextMarker": str},
    total=False,
)


class ClientDescribeSslPoliciesResponseTypeDef(_ClientDescribeSslPoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **SslPolicies** *(list) --*

        Information about the policies.
        - *(dict) --*

          Information about a policy used for SSL negotiation.
          - **SslProtocols** *(list) --*

            The protocols.
            - *(string) --*
    """


_ClientDescribeTagsResponseTagDescriptionsTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagDescriptionsTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeTagsResponseTagDescriptionsTagsTypeDef(
    _ClientDescribeTagsResponseTagDescriptionsTagsTypeDef
):
    pass


_ClientDescribeTagsResponseTagDescriptionsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagDescriptionsTypeDef",
    {"ResourceArn": str, "Tags": List[ClientDescribeTagsResponseTagDescriptionsTagsTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTagDescriptionsTypeDef(
    _ClientDescribeTagsResponseTagDescriptionsTypeDef
):
    """
    - *(dict) --*

      The tags associated with a resource.
      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"TagDescriptions": List[ClientDescribeTagsResponseTagDescriptionsTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      - **TagDescriptions** *(list) --*

        Information about the tags.
        - *(dict) --*

          The tags associated with a resource.
          - **ResourceArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource.
    """


_ClientDescribeTargetGroupAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientDescribeTargetGroupAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeTargetGroupAttributesResponseAttributesTypeDef(
    _ClientDescribeTargetGroupAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      Information about a target group attribute.
      - **Key** *(string) --*

        The name of the attribute.
        The following attribute is supported by both Application Load Balancers and Network Load
        Balancers:
        * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
        Load Balancing to wait before changing the state of a deregistering target from ``draining``
        to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. If the target
        is a Lambda function, this attribute is not supported.
        The following attributes are supported by Application Load Balancers if the target is not a
        Lambda function:
        * ``load_balancing.algorithm.type`` - The load balancing algorithm determines how the load
        balancer selects targets when routing requests. The value is ``round_robin`` or
        ``least_outstanding_requests`` . The default is ``round_robin`` .
        * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
        registered target receives a linearly increasing share of the traffic to the target group.
        After this time period ends, the target receives its full share of traffic. The range is
        30-900 seconds (15 minutes). Slow start mode is disabled by default.
        * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
        ``true`` or ``false`` . The default is ``false`` .
        * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` .
        * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
        requests from a client should be routed to the same target. After this time period expires,
        the load balancer-generated cookie is considered stale. The range is 1 second to 1 week
        (604800 seconds). The default value is 1 day (86400 seconds).
        The following attribute is supported only if the target is a Lambda function.
        * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
        headers exchanged between the load balancer and the Lambda function include arrays of values
        or strings. The value is ``true`` or ``false`` . The default is ``false`` . If the value is
        ``false`` and the request contains a duplicate header field name or query parameter key, the
        load balancer uses the last value sent by the client.
        The following attribute is supported only by Network Load Balancers:
        * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled. The
        value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientDescribeTargetGroupAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeTargetGroupAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeTargetGroupAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientDescribeTargetGroupAttributesResponseTypeDef(
    _ClientDescribeTargetGroupAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        Information about the target group attributes
        - *(dict) --*

          Information about a target group attribute.
          - **Key** *(string) --*

            The name of the attribute.
            The following attribute is supported by both Application Load Balancers and Network Load
            Balancers:
            * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
            Load Balancing to wait before changing the state of a deregistering target from
            ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300
            seconds. If the target is a Lambda function, this attribute is not supported.
            The following attributes are supported by Application Load Balancers if the target is
            not a Lambda function:
            * ``load_balancing.algorithm.type`` - The load balancing algorithm determines how the
            load balancer selects targets when routing requests. The value is ``round_robin`` or
            ``least_outstanding_requests`` . The default is ``round_robin`` .
            * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
            registered target receives a linearly increasing share of the traffic to the target
            group. After this time period ends, the target receives its full share of traffic. The
            range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.
            * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
            ``true`` or ``false`` . The default is ``false`` .
            * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie``
            .
            * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
            requests from a client should be routed to the same target. After this time period
            expires, the load balancer-generated cookie is considered stale. The range is 1 second
            to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
            The following attribute is supported only if the target is a Lambda function.
            * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
            headers exchanged between the load balancer and the Lambda function include arrays of
            values or strings. The value is ``true`` or ``false`` . The default is ``false`` . If
            the value is ``false`` and the request contains a duplicate header field name or query
            parameter key, the load balancer uses the last value sent by the client.
            The following attribute is supported only by Network Load Balancers:
            * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled.
            The value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef = TypedDict(
    "_ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef", {"HttpCode": str}, total=False
)


class ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef(
    _ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef
):
    pass


_ClientDescribeTargetGroupsResponseTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeTargetGroupsResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
    },
    total=False,
)


class ClientDescribeTargetGroupsResponseTargetGroupsTypeDef(
    _ClientDescribeTargetGroupsResponseTargetGroupsTypeDef
):
    """
    - *(dict) --*

      Information about a target group.
      - **TargetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the target group.
    """


_ClientDescribeTargetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List[ClientDescribeTargetGroupsResponseTargetGroupsTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeTargetGroupsResponseTypeDef(_ClientDescribeTargetGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **TargetGroups** *(list) --*

        Information about the target groups.
        - *(dict) --*

          Information about a target group.
          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.
    """


_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef = TypedDict(
    "_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef",
    {
        "State": Literal["initial", "healthy", "unhealthy", "unused", "draining", "unavailable"],
        "Reason": Literal[
            "Elb.RegistrationInProgress",
            "Elb.InitialHealthChecking",
            "Target.ResponseCodeMismatch",
            "Target.Timeout",
            "Target.FailedHealthChecks",
            "Target.NotRegistered",
            "Target.NotInUse",
            "Target.DeregistrationInProgress",
            "Target.InvalidState",
            "Target.IpUnusable",
            "Target.HealthCheckDisabled",
            "Elb.InternalError",
        ],
        "Description": str,
    },
    total=False,
)


class ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef(
    _ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef
):
    pass


_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef = TypedDict(
    "_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef",
    {"Id": str, "Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef(
    _ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef
):
    """
    - **Target** *(dict) --*

      The description of the target.
      - **Id** *(string) --*

        The ID of the target. If the target type of the target group is ``instance`` , specify an
        instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
        ``lambda`` , specify the ARN of the Lambda function.
    """


_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef = TypedDict(
    "_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef",
    {
        "Target": ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef,
        "HealthCheckPort": str,
        "TargetHealth": ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef,
    },
    total=False,
)


class ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef(
    _ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef
):
    """
    - *(dict) --*

      Information about the health of a target.
      - **Target** *(dict) --*

        The description of the target.
        - **Id** *(string) --*

          The ID of the target. If the target type of the target group is ``instance`` , specify an
          instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
          ``lambda`` , specify the ARN of the Lambda function.
    """


_ClientDescribeTargetHealthResponseTypeDef = TypedDict(
    "_ClientDescribeTargetHealthResponseTypeDef",
    {
        "TargetHealthDescriptions": List[
            ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeTargetHealthResponseTypeDef(_ClientDescribeTargetHealthResponseTypeDef):
    """
    - *(dict) --*

      - **TargetHealthDescriptions** *(list) --*

        Information about the health of the targets.
        - *(dict) --*

          Information about the health of a target.
          - **Target** *(dict) --*

            The description of the target.
            - **Id** *(string) --*

              The ID of the target. If the target type of the target group is ``instance`` , specify
              an instance ID. If the target type is ``ip`` , specify an IP address. If the target
              type is ``lambda`` , specify the ARN of the Lambda function.
    """


_RequiredClientDescribeTargetHealthTargetsTypeDef = TypedDict(
    "_RequiredClientDescribeTargetHealthTargetsTypeDef", {"Id": str}
)
_OptionalClientDescribeTargetHealthTargetsTypeDef = TypedDict(
    "_OptionalClientDescribeTargetHealthTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientDescribeTargetHealthTargetsTypeDef(
    _RequiredClientDescribeTargetHealthTargetsTypeDef,
    _OptionalClientDescribeTargetHealthTargetsTypeDef,
):
    """
    - *(dict) --*

      Information about a target.
      - **Id** *(string) --***[REQUIRED]**

        The ID of the target. If the target type of the target group is ``instance`` , specify an
        instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
        ``lambda`` , specify the ARN of the Lambda function.
    """


_ClientModifyListenerCertificatesTypeDef = TypedDict(
    "_ClientModifyListenerCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientModifyListenerCertificatesTypeDef(_ClientModifyListenerCertificatesTypeDef):
    """
    - *(dict) --*

      Information about an SSL server certificate.
      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate.
    """


_ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef(
    _ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef(
    _ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef(
    _ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef
):
    pass


_ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientModifyListenerDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerDefaultActionsForwardConfigTypeDef(
    _ClientModifyListenerDefaultActionsForwardConfigTypeDef
):
    pass


_ClientModifyListenerDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientModifyListenerDefaultActionsRedirectConfigTypeDef(
    _ClientModifyListenerDefaultActionsRedirectConfigTypeDef
):
    pass


_RequiredClientModifyListenerDefaultActionsTypeDef = TypedDict(
    "_RequiredClientModifyListenerDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalClientModifyListenerDefaultActionsTypeDef = TypedDict(
    "_OptionalClientModifyListenerDefaultActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyListenerDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyListenerDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerDefaultActionsTypeDef(
    _RequiredClientModifyListenerDefaultActionsTypeDef,
    _OptionalClientModifyListenerDefaultActionsTypeDef,
):
    """
    - *(dict) --*

      Information about an action.
      - **Type** *(string) --***[REQUIRED]**

        The type of action.
    """


_ClientModifyListenerResponseListenersCertificatesTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientModifyListenerResponseListenersCertificatesTypeDef(
    _ClientModifyListenerResponseListenersCertificatesTypeDef
):
    pass


_ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef
):
    pass


_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef
):
    pass


_ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef
):
    pass


_ClientModifyListenerResponseListenersDefaultActionsTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsTypeDef
):
    pass


_ClientModifyListenerResponseListenersTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List[ClientModifyListenerResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[ClientModifyListenerResponseListenersDefaultActionsTypeDef],
    },
    total=False,
)


class ClientModifyListenerResponseListenersTypeDef(_ClientModifyListenerResponseListenersTypeDef):
    """
    - *(dict) --*

      Information about a listener.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_ClientModifyListenerResponseTypeDef = TypedDict(
    "_ClientModifyListenerResponseTypeDef",
    {"Listeners": List[ClientModifyListenerResponseListenersTypeDef]},
    total=False,
)


class ClientModifyListenerResponseTypeDef(_ClientModifyListenerResponseTypeDef):
    """
    - *(dict) --*

      - **Listeners** *(list) --*

        Information about the modified listener.
        - *(dict) --*

          Information about a listener.
          - **ListenerArn** *(string) --*

            The Amazon Resource Name (ARN) of the listener.
    """


_ClientModifyLoadBalancerAttributesAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesAttributesTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientModifyLoadBalancerAttributesAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesAttributesTypeDef
):
    """
    - *(dict) --*

      Information about a load balancer attribute.
      - **Key** *(string) --*

        The name of the attribute.
        The following attributes are supported by both Application Load Balancers and Network Load
        Balancers:
        * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
        ``true`` or ``false`` . The default is ``false`` .
        * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This attribute
        is required if access logs are enabled. The bucket must exist in the same region as the load
        balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to
        the bucket.
        * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access
        logs.
        * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The
        value is ``true`` or ``false`` . The default is ``false`` .
        The following attributes are supported by only Application Load Balancers:
        * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range is
        1-4000 seconds. The default is 60 seconds.
        * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers with
        invalid header fields are removed by the load balancer (``true`` ) or routed to targets
        (``false`` ). The default is ``false`` .
        * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true`` or
        ``false`` . The default is ``true`` .
        The following attributes are supported by only Network Load Balancers:
        * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
        enabled. The value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientModifyLoadBalancerAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      Information about a load balancer attribute.
      - **Key** *(string) --*

        The name of the attribute.
        The following attributes are supported by both Application Load Balancers and Network Load
        Balancers:
        * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
        ``true`` or ``false`` . The default is ``false`` .
        * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This attribute
        is required if access logs are enabled. The bucket must exist in the same region as the load
        balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to
        the bucket.
        * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access
        logs.
        * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The
        value is ``true`` or ``false`` . The default is ``false`` .
        The following attributes are supported by only Application Load Balancers:
        * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range is
        1-4000 seconds. The default is 60 seconds.
        * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers with
        invalid header fields are removed by the load balancer (``true`` ) or routed to targets
        (``false`` ). The default is ``false`` .
        * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true`` or
        ``false`` . The default is ``true`` .
        The following attributes are supported by only Network Load Balancers:
        * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
        enabled. The value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientModifyLoadBalancerAttributesResponseTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseTypeDef",
    {"Attributes": List[ClientModifyLoadBalancerAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseTypeDef(
    _ClientModifyLoadBalancerAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        Information about the load balancer attributes.
        - *(dict) --*

          Information about a load balancer attribute.
          - **Key** *(string) --*

            The name of the attribute.
            The following attributes are supported by both Application Load Balancers and Network
            Load Balancers:
            * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
            ``true`` or ``false`` . The default is ``false`` .
            * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This
            attribute is required if access logs are enabled. The bucket must exist in the same
            region as the load balancer and have a bucket policy that grants Elastic Load Balancing
            permissions to write to the bucket.
            * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the
            access logs.
            * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled.
            The value is ``true`` or ``false`` . The default is ``false`` .
            The following attributes are supported by only Application Load Balancers:
            * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range
            is 1-4000 seconds. The default is 60 seconds.
            * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers
            with invalid header fields are removed by the load balancer (``true`` ) or routed to
            targets (``false`` ). The default is ``false`` .
            * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true``
            or ``false`` . The default is ``true`` .
            The following attributes are supported by only Network Load Balancers:
            * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
            enabled. The value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef(
    _ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientModifyRuleActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientModifyRuleActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientModifyRuleActionsAuthenticateOidcConfigTypeDef(
    _ClientModifyRuleActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientModifyRuleActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientModifyRuleActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientModifyRuleActionsFixedResponseConfigTypeDef(
    _ClientModifyRuleActionsFixedResponseConfigTypeDef
):
    pass


_ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef(
    _ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientModifyRuleActionsForwardConfigTypeDef = TypedDict(
    "_ClientModifyRuleActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleActionsForwardConfigTypeDef(_ClientModifyRuleActionsForwardConfigTypeDef):
    pass


_ClientModifyRuleActionsRedirectConfigTypeDef = TypedDict(
    "_ClientModifyRuleActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientModifyRuleActionsRedirectConfigTypeDef(_ClientModifyRuleActionsRedirectConfigTypeDef):
    pass


_RequiredClientModifyRuleActionsTypeDef = TypedDict(
    "_RequiredClientModifyRuleActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalClientModifyRuleActionsTypeDef = TypedDict(
    "_OptionalClientModifyRuleActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyRuleActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyRuleActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyRuleActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyRuleActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleActionsTypeDef(
    _RequiredClientModifyRuleActionsTypeDef, _OptionalClientModifyRuleActionsTypeDef
):
    """
    - *(dict) --*

      Information about an action.
      - **Type** *(string) --***[REQUIRED]**

        The type of action.
    """


_ClientModifyRuleConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsHostHeaderConfigTypeDef", {"Values": List[str]}, total=False
)


class ClientModifyRuleConditionsHostHeaderConfigTypeDef(
    _ClientModifyRuleConditionsHostHeaderConfigTypeDef
):
    pass


_ClientModifyRuleConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientModifyRuleConditionsHttpHeaderConfigTypeDef(
    _ClientModifyRuleConditionsHttpHeaderConfigTypeDef
):
    pass


_ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef", {"Values": List[str]}, total=False
)


class ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef(
    _ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef
):
    pass


_ClientModifyRuleConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsPathPatternConfigTypeDef", {"Values": List[str]}, total=False
)


class ClientModifyRuleConditionsPathPatternConfigTypeDef(
    _ClientModifyRuleConditionsPathPatternConfigTypeDef
):
    pass


_ClientModifyRuleConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientModifyRuleConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyRuleConditionsQueryStringConfigValuesTypeDef(
    _ClientModifyRuleConditionsQueryStringConfigValuesTypeDef
):
    pass


_ClientModifyRuleConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientModifyRuleConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class ClientModifyRuleConditionsQueryStringConfigTypeDef(
    _ClientModifyRuleConditionsQueryStringConfigTypeDef
):
    pass


_ClientModifyRuleConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsSourceIpConfigTypeDef", {"Values": List[str]}, total=False
)


class ClientModifyRuleConditionsSourceIpConfigTypeDef(
    _ClientModifyRuleConditionsSourceIpConfigTypeDef
):
    pass


_ClientModifyRuleConditionsTypeDef = TypedDict(
    "_ClientModifyRuleConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientModifyRuleConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientModifyRuleConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientModifyRuleConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientModifyRuleConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientModifyRuleConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleConditionsTypeDef(_ClientModifyRuleConditionsTypeDef):
    """
    - *(dict) --*

      Information about a condition for a rule.
      - **Field** *(string) --*

        The field in the HTTP request. The following are the possible values:
        * ``http-header``
        * ``http-request-method``
        * ``host-header``
        * ``path-pattern``
        * ``query-string``
        * ``source-ip``
    """


_ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientModifyRuleResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsForwardConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsForwardConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesActionsTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyRuleResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsTypeDef(_ClientModifyRuleResponseRulesActionsTypeDef):
    pass


_ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    pass


_ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef
):
    pass


_ClientModifyRuleResponseRulesConditionsTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleResponseRulesConditionsTypeDef(
    _ClientModifyRuleResponseRulesConditionsTypeDef
):
    pass


_ClientModifyRuleResponseRulesTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientModifyRuleResponseRulesConditionsTypeDef],
        "Actions": List[ClientModifyRuleResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class ClientModifyRuleResponseRulesTypeDef(_ClientModifyRuleResponseRulesTypeDef):
    """
    - *(dict) --*

      Information about a rule.
      - **RuleArn** *(string) --*

        The Amazon Resource Name (ARN) of the rule.
    """


_ClientModifyRuleResponseTypeDef = TypedDict(
    "_ClientModifyRuleResponseTypeDef",
    {"Rules": List[ClientModifyRuleResponseRulesTypeDef]},
    total=False,
)


class ClientModifyRuleResponseTypeDef(_ClientModifyRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        Information about the modified rule.
        - *(dict) --*

          Information about a rule.
          - **RuleArn** *(string) --*

            The Amazon Resource Name (ARN) of the rule.
    """


_ClientModifyTargetGroupAttributesAttributesTypeDef = TypedDict(
    "_ClientModifyTargetGroupAttributesAttributesTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientModifyTargetGroupAttributesAttributesTypeDef(
    _ClientModifyTargetGroupAttributesAttributesTypeDef
):
    """
    - *(dict) --*

      Information about a target group attribute.
      - **Key** *(string) --*

        The name of the attribute.
        The following attribute is supported by both Application Load Balancers and Network Load
        Balancers:
        * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
        Load Balancing to wait before changing the state of a deregistering target from ``draining``
        to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. If the target
        is a Lambda function, this attribute is not supported.
        The following attributes are supported by Application Load Balancers if the target is not a
        Lambda function:
        * ``load_balancing.algorithm.type`` - The load balancing algorithm determines how the load
        balancer selects targets when routing requests. The value is ``round_robin`` or
        ``least_outstanding_requests`` . The default is ``round_robin`` .
        * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
        registered target receives a linearly increasing share of the traffic to the target group.
        After this time period ends, the target receives its full share of traffic. The range is
        30-900 seconds (15 minutes). Slow start mode is disabled by default.
        * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
        ``true`` or ``false`` . The default is ``false`` .
        * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` .
        * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
        requests from a client should be routed to the same target. After this time period expires,
        the load balancer-generated cookie is considered stale. The range is 1 second to 1 week
        (604800 seconds). The default value is 1 day (86400 seconds).
        The following attribute is supported only if the target is a Lambda function.
        * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
        headers exchanged between the load balancer and the Lambda function include arrays of values
        or strings. The value is ``true`` or ``false`` . The default is ``false`` . If the value is
        ``false`` and the request contains a duplicate header field name or query parameter key, the
        load balancer uses the last value sent by the client.
        The following attribute is supported only by Network Load Balancers:
        * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled. The
        value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientModifyTargetGroupAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientModifyTargetGroupAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyTargetGroupAttributesResponseAttributesTypeDef(
    _ClientModifyTargetGroupAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      Information about a target group attribute.
      - **Key** *(string) --*

        The name of the attribute.
        The following attribute is supported by both Application Load Balancers and Network Load
        Balancers:
        * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
        Load Balancing to wait before changing the state of a deregistering target from ``draining``
        to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. If the target
        is a Lambda function, this attribute is not supported.
        The following attributes are supported by Application Load Balancers if the target is not a
        Lambda function:
        * ``load_balancing.algorithm.type`` - The load balancing algorithm determines how the load
        balancer selects targets when routing requests. The value is ``round_robin`` or
        ``least_outstanding_requests`` . The default is ``round_robin`` .
        * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
        registered target receives a linearly increasing share of the traffic to the target group.
        After this time period ends, the target receives its full share of traffic. The range is
        30-900 seconds (15 minutes). Slow start mode is disabled by default.
        * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
        ``true`` or ``false`` . The default is ``false`` .
        * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` .
        * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
        requests from a client should be routed to the same target. After this time period expires,
        the load balancer-generated cookie is considered stale. The range is 1 second to 1 week
        (604800 seconds). The default value is 1 day (86400 seconds).
        The following attribute is supported only if the target is a Lambda function.
        * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
        headers exchanged between the load balancer and the Lambda function include arrays of values
        or strings. The value is ``true`` or ``false`` . The default is ``false`` . If the value is
        ``false`` and the request contains a duplicate header field name or query parameter key, the
        load balancer uses the last value sent by the client.
        The following attribute is supported only by Network Load Balancers:
        * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled. The
        value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientModifyTargetGroupAttributesResponseTypeDef = TypedDict(
    "_ClientModifyTargetGroupAttributesResponseTypeDef",
    {"Attributes": List[ClientModifyTargetGroupAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientModifyTargetGroupAttributesResponseTypeDef(
    _ClientModifyTargetGroupAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        Information about the attributes.
        - *(dict) --*

          Information about a target group attribute.
          - **Key** *(string) --*

            The name of the attribute.
            The following attribute is supported by both Application Load Balancers and Network Load
            Balancers:
            * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
            Load Balancing to wait before changing the state of a deregistering target from
            ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300
            seconds. If the target is a Lambda function, this attribute is not supported.
            The following attributes are supported by Application Load Balancers if the target is
            not a Lambda function:
            * ``load_balancing.algorithm.type`` - The load balancing algorithm determines how the
            load balancer selects targets when routing requests. The value is ``round_robin`` or
            ``least_outstanding_requests`` . The default is ``round_robin`` .
            * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
            registered target receives a linearly increasing share of the traffic to the target
            group. After this time period ends, the target receives its full share of traffic. The
            range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.
            * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
            ``true`` or ``false`` . The default is ``false`` .
            * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie``
            .
            * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
            requests from a client should be routed to the same target. After this time period
            expires, the load balancer-generated cookie is considered stale. The range is 1 second
            to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
            The following attribute is supported only if the target is a Lambda function.
            * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
            headers exchanged between the load balancer and the Lambda function include arrays of
            values or strings. The value is ``true`` or ``false`` . The default is ``false`` . If
            the value is ``false`` and the request contains a duplicate header field name or query
            parameter key, the load balancer uses the last value sent by the client.
            The following attribute is supported only by Network Load Balancers:
            * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled.
            The value is ``true`` or ``false`` . The default is ``false`` .
    """


_ClientModifyTargetGroupMatcherTypeDef = TypedDict(
    "_ClientModifyTargetGroupMatcherTypeDef", {"HttpCode": str}
)


class ClientModifyTargetGroupMatcherTypeDef(_ClientModifyTargetGroupMatcherTypeDef):
    """
    [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a
    target.
    With Network Load Balancers, you can't modify this setting.
    - **HttpCode** *(string) --***[REQUIRED]**

      The HTTP codes.
      For Application Load Balancers, you can specify values between 200 and 499, and the default
      value is 200. You can specify multiple values (for example, "200,202") or a range of values
      (for example, "200-299").
      For Network Load Balancers, this is 200–399.
    """


_ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef = TypedDict(
    "_ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef", {"HttpCode": str}, total=False
)


class ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef(
    _ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef
):
    pass


_ClientModifyTargetGroupResponseTargetGroupsTypeDef = TypedDict(
    "_ClientModifyTargetGroupResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
    },
    total=False,
)


class ClientModifyTargetGroupResponseTargetGroupsTypeDef(
    _ClientModifyTargetGroupResponseTargetGroupsTypeDef
):
    """
    - *(dict) --*

      Information about a target group.
      - **TargetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the target group.
    """


_ClientModifyTargetGroupResponseTypeDef = TypedDict(
    "_ClientModifyTargetGroupResponseTypeDef",
    {"TargetGroups": List[ClientModifyTargetGroupResponseTargetGroupsTypeDef]},
    total=False,
)


class ClientModifyTargetGroupResponseTypeDef(_ClientModifyTargetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **TargetGroups** *(list) --*

        Information about the modified target group.
        - *(dict) --*

          Information about a target group.
          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.
    """


_RequiredClientRegisterTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientRegisterTargetsTargetsTypeDef", {"Id": str}
)
_OptionalClientRegisterTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientRegisterTargetsTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientRegisterTargetsTargetsTypeDef(
    _RequiredClientRegisterTargetsTargetsTypeDef, _OptionalClientRegisterTargetsTargetsTypeDef
):
    """
    - *(dict) --*

      Information about a target.
      - **Id** *(string) --***[REQUIRED]**

        The ID of the target. If the target type of the target group is ``instance`` , specify an
        instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
        ``lambda`` , specify the ARN of the Lambda function.
    """


_ClientRemoveListenerCertificatesCertificatesTypeDef = TypedDict(
    "_ClientRemoveListenerCertificatesCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientRemoveListenerCertificatesCertificatesTypeDef(
    _ClientRemoveListenerCertificatesCertificatesTypeDef
):
    """
    - *(dict) --*

      Information about an SSL server certificate.
      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate.
    """


_ClientSetIpAddressTypeResponseTypeDef = TypedDict(
    "_ClientSetIpAddressTypeResponseTypeDef",
    {"IpAddressType": Literal["ipv4", "dualstack"]},
    total=False,
)


class ClientSetIpAddressTypeResponseTypeDef(_ClientSetIpAddressTypeResponseTypeDef):
    """
    - *(dict) --*

      - **IpAddressType** *(string) --*

        The IP address type.
    """


_ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesActionsTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesConditionsTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsTypeDef
):
    pass


_ClientSetRulePrioritiesResponseRulesTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientSetRulePrioritiesResponseRulesConditionsTypeDef],
        "Actions": List[ClientSetRulePrioritiesResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesTypeDef(_ClientSetRulePrioritiesResponseRulesTypeDef):
    """
    - *(dict) --*

      Information about a rule.
      - **RuleArn** *(string) --*

        The Amazon Resource Name (ARN) of the rule.
    """


_ClientSetRulePrioritiesResponseTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseTypeDef",
    {"Rules": List[ClientSetRulePrioritiesResponseRulesTypeDef]},
    total=False,
)


class ClientSetRulePrioritiesResponseTypeDef(_ClientSetRulePrioritiesResponseTypeDef):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        Information about the rules.
        - *(dict) --*

          Information about a rule.
          - **RuleArn** *(string) --*

            The Amazon Resource Name (ARN) of the rule.
    """


_ClientSetRulePrioritiesRulePrioritiesTypeDef = TypedDict(
    "_ClientSetRulePrioritiesRulePrioritiesTypeDef", {"RuleArn": str, "Priority": int}, total=False
)


class ClientSetRulePrioritiesRulePrioritiesTypeDef(_ClientSetRulePrioritiesRulePrioritiesTypeDef):
    """
    - *(dict) --*

      Information about the priorities for the rules for a listener.
      - **RuleArn** *(string) --*

        The Amazon Resource Name (ARN) of the rule.
    """


_ClientSetSecurityGroupsResponseTypeDef = TypedDict(
    "_ClientSetSecurityGroupsResponseTypeDef", {"SecurityGroupIds": List[str]}, total=False
)


class ClientSetSecurityGroupsResponseTypeDef(_ClientSetSecurityGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **SecurityGroupIds** *(list) --*

        The IDs of the security groups associated with the load balancer.
        - *(string) --*
    """


_ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "_ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)


class ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef(
    _ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef
):
    pass


_ClientSetSubnetsResponseAvailabilityZonesTypeDef = TypedDict(
    "_ClientSetSubnetsResponseAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)


class ClientSetSubnetsResponseAvailabilityZonesTypeDef(
    _ClientSetSubnetsResponseAvailabilityZonesTypeDef
):
    """
    - *(dict) --*

      Information about an Availability Zone.
      - **ZoneName** *(string) --*

        The name of the Availability Zone.
    """


_ClientSetSubnetsResponseTypeDef = TypedDict(
    "_ClientSetSubnetsResponseTypeDef",
    {"AvailabilityZones": List[ClientSetSubnetsResponseAvailabilityZonesTypeDef]},
    total=False,
)


class ClientSetSubnetsResponseTypeDef(_ClientSetSubnetsResponseTypeDef):
    """
    - *(dict) --*

      - **AvailabilityZones** *(list) --*

        Information about the subnet and Availability Zone.
        - *(dict) --*

          Information about an Availability Zone.
          - **ZoneName** *(string) --*

            The name of the Availability Zone.
    """


_ClientSetSubnetsSubnetMappingsTypeDef = TypedDict(
    "_ClientSetSubnetsSubnetMappingsTypeDef",
    {"SubnetId": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)


class ClientSetSubnetsSubnetMappingsTypeDef(_ClientSetSubnetsSubnetMappingsTypeDef):
    """
    - *(dict) --*

      Information about a subnet mapping.
      - **SubnetId** *(string) --*

        The ID of the subnet.
    """


_DescribeAccountLimitsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAccountLimitsPaginatePaginationConfigTypeDef(
    _DescribeAccountLimitsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAccountLimitsPaginateResponseLimitsTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginateResponseLimitsTypeDef", {"Name": str, "Max": str}, total=False
)


class DescribeAccountLimitsPaginateResponseLimitsTypeDef(
    _DescribeAccountLimitsPaginateResponseLimitsTypeDef
):
    """
    - *(dict) --*

      Information about an Elastic Load Balancing resource limit for your AWS account.
      - **Name** *(string) --*

        The name of the limit. The possible values are:
        * application-load-balancers
        * listeners-per-application-load-balancer
        * listeners-per-network-load-balancer
        * network-load-balancers
        * rules-per-application-load-balancer
        * target-groups
        * target-groups-per-action-on-application-load-balancer
        * target-groups-per-action-on-network-load-balancer
        * target-groups-per-application-load-balancer
        * targets-per-application-load-balancer
        * targets-per-availability-zone-per-network-load-balancer
        * targets-per-network-load-balancer
    """


_DescribeAccountLimitsPaginateResponseTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginateResponseTypeDef",
    {"Limits": List[DescribeAccountLimitsPaginateResponseLimitsTypeDef], "NextToken": str},
    total=False,
)


class DescribeAccountLimitsPaginateResponseTypeDef(_DescribeAccountLimitsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Limits** *(list) --*

        Information about the limits.
        - *(dict) --*

          Information about an Elastic Load Balancing resource limit for your AWS account.
          - **Name** *(string) --*

            The name of the limit. The possible values are:
            * application-load-balancers
            * listeners-per-application-load-balancer
            * listeners-per-network-load-balancer
            * network-load-balancers
            * rules-per-application-load-balancer
            * target-groups
            * target-groups-per-action-on-application-load-balancer
            * target-groups-per-action-on-network-load-balancer
            * target-groups-per-application-load-balancer
            * targets-per-application-load-balancer
            * targets-per-availability-zone-per-network-load-balancer
            * targets-per-network-load-balancer
    """


_DescribeListenerCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeListenerCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeListenerCertificatesPaginatePaginationConfigTypeDef(
    _DescribeListenerCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeListenerCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "_DescribeListenerCertificatesPaginateResponseCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class DescribeListenerCertificatesPaginateResponseCertificatesTypeDef(
    _DescribeListenerCertificatesPaginateResponseCertificatesTypeDef
):
    """
    - *(dict) --*

      Information about an SSL server certificate.
      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate.
    """


_DescribeListenerCertificatesPaginateResponseTypeDef = TypedDict(
    "_DescribeListenerCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[DescribeListenerCertificatesPaginateResponseCertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeListenerCertificatesPaginateResponseTypeDef(
    _DescribeListenerCertificatesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Certificates** *(list) --*

        Information about the certificates.
        - *(dict) --*

          Information about an SSL server certificate.
          - **CertificateArn** *(string) --*

            The Amazon Resource Name (ARN) of the certificate.
    """


_DescribeListenersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeListenersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeListenersPaginatePaginationConfigTypeDef(
    _DescribeListenersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeListenersPaginateResponseListenersCertificatesTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class DescribeListenersPaginateResponseListenersCertificatesTypeDef(
    _DescribeListenersPaginateResponseListenersCertificatesTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersDefaultActionsTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsTypeDef
):
    pass


_DescribeListenersPaginateResponseListenersTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List[DescribeListenersPaginateResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[DescribeListenersPaginateResponseListenersDefaultActionsTypeDef],
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersTypeDef(
    _DescribeListenersPaginateResponseListenersTypeDef
):
    """
    - *(dict) --*

      Information about a listener.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_DescribeListenersPaginateResponseTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseTypeDef",
    {"Listeners": List[DescribeListenersPaginateResponseListenersTypeDef], "NextToken": str},
    total=False,
)


class DescribeListenersPaginateResponseTypeDef(_DescribeListenersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Listeners** *(list) --*

        Information about the listeners.
        - *(dict) --*

          Information about a listener.
          - **ListenerArn** *(string) --*

            The Amazon Resource Name (ARN) of the listener.
    """


_DescribeLoadBalancersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLoadBalancersPaginatePaginationConfigTypeDef(
    _DescribeLoadBalancersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef",
    {"Code": Literal["active", "provisioning", "active_impaired", "failed"], "Reason": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": Literal["internet-facing", "internal"],
        "VpcId": str,
        "State": DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef,
        "Type": Literal["application", "network"],
        "AvailabilityZones": List[
            DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef
        ],
        "SecurityGroups": List[str],
        "IpAddressType": Literal["ipv4", "dualstack"],
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef
):
    """
    - *(dict) --*

      Information about a load balancer.
      - **LoadBalancerArn** *(string) --*

        The Amazon Resource Name (ARN) of the load balancer.
    """


_DescribeLoadBalancersPaginateResponseTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseTypeDef",
    {
        "LoadBalancers": List[DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseTypeDef(_DescribeLoadBalancersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **LoadBalancers** *(list) --*

        Information about the load balancers.
        - *(dict) --*

          Information about a load balancer.
          - **LoadBalancerArn** *(string) --*

            The Amazon Resource Name (ARN) of the load balancer.
    """


_DescribeRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeRulesPaginatePaginationConfigTypeDef(_DescribeRulesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesActionsTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsTypeDef(
    _DescribeRulesPaginateResponseRulesActionsTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesConditionsTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsTypeDef
):
    pass


_DescribeRulesPaginateResponseRulesTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[DescribeRulesPaginateResponseRulesConditionsTypeDef],
        "Actions": List[DescribeRulesPaginateResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesTypeDef(_DescribeRulesPaginateResponseRulesTypeDef):
    """
    - *(dict) --*

      Information about a rule.
      - **RuleArn** *(string) --*

        The Amazon Resource Name (ARN) of the rule.
    """


_DescribeRulesPaginateResponseTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseTypeDef",
    {"Rules": List[DescribeRulesPaginateResponseRulesTypeDef], "NextToken": str},
    total=False,
)


class DescribeRulesPaginateResponseTypeDef(_DescribeRulesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        Information about the rules.
        - *(dict) --*

          Information about a rule.
          - **RuleArn** *(string) --*

            The Amazon Resource Name (ARN) of the rule.
    """


_DescribeSSLPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSSLPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSSLPoliciesPaginatePaginationConfigTypeDef(
    _DescribeSSLPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef = TypedDict(
    "_DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef",
    {"Name": str, "Priority": int},
    total=False,
)


class DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef(
    _DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef
):
    pass


_DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef = TypedDict(
    "_DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef",
    {
        "SslProtocols": List[str],
        "Ciphers": List[DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef],
        "Name": str,
    },
    total=False,
)


class DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef(
    _DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef
):
    """
    - *(dict) --*

      Information about a policy used for SSL negotiation.
      - **SslProtocols** *(list) --*

        The protocols.
        - *(string) --*
    """


_DescribeSSLPoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribeSSLPoliciesPaginateResponseTypeDef",
    {"SslPolicies": List[DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef], "NextToken": str},
    total=False,
)


class DescribeSSLPoliciesPaginateResponseTypeDef(_DescribeSSLPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SslPolicies** *(list) --*

        Information about the policies.
        - *(dict) --*

          Information about a policy used for SSL negotiation.
          - **SslProtocols** *(list) --*

            The protocols.
            - *(string) --*
    """


_DescribeTargetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTargetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTargetGroupsPaginatePaginationConfigTypeDef(
    _DescribeTargetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef = TypedDict(
    "_DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef",
    {"HttpCode": str},
    total=False,
)


class DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef(
    _DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef
):
    pass


_DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef = TypedDict(
    "_DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
    },
    total=False,
)


class DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef(
    _DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef
):
    """
    - *(dict) --*

      Information about a target group.
      - **TargetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the target group.
    """


_DescribeTargetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeTargetGroupsPaginateResponseTypeDef",
    {
        "TargetGroups": List[DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeTargetGroupsPaginateResponseTypeDef(_DescribeTargetGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TargetGroups** *(list) --*

        Information about the target groups.
        - *(dict) --*

          Information about a target group.
          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.
    """


_LoadBalancerAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_LoadBalancerAvailableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class LoadBalancerAvailableWaitWaiterConfigTypeDef(_LoadBalancerAvailableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_LoadBalancerExistsWaitWaiterConfigTypeDef = TypedDict(
    "_LoadBalancerExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class LoadBalancerExistsWaitWaiterConfigTypeDef(_LoadBalancerExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_LoadBalancersDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_LoadBalancersDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class LoadBalancersDeletedWaitWaiterConfigTypeDef(_LoadBalancersDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_RequiredTargetDeregisteredWaitTargetsTypeDef = TypedDict(
    "_RequiredTargetDeregisteredWaitTargetsTypeDef", {"Id": str}
)
_OptionalTargetDeregisteredWaitTargetsTypeDef = TypedDict(
    "_OptionalTargetDeregisteredWaitTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class TargetDeregisteredWaitTargetsTypeDef(
    _RequiredTargetDeregisteredWaitTargetsTypeDef, _OptionalTargetDeregisteredWaitTargetsTypeDef
):
    """
    - *(dict) --*

      Information about a target.
      - **Id** *(string) --***[REQUIRED]**

        The ID of the target. If the target type of the target group is ``instance`` , specify an
        instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
        ``lambda`` , specify the ARN of the Lambda function.
    """


_TargetDeregisteredWaitWaiterConfigTypeDef = TypedDict(
    "_TargetDeregisteredWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class TargetDeregisteredWaitWaiterConfigTypeDef(_TargetDeregisteredWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_RequiredTargetInServiceWaitTargetsTypeDef = TypedDict(
    "_RequiredTargetInServiceWaitTargetsTypeDef", {"Id": str}
)
_OptionalTargetInServiceWaitTargetsTypeDef = TypedDict(
    "_OptionalTargetInServiceWaitTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class TargetInServiceWaitTargetsTypeDef(
    _RequiredTargetInServiceWaitTargetsTypeDef, _OptionalTargetInServiceWaitTargetsTypeDef
):
    """
    - *(dict) --*

      Information about a target.
      - **Id** *(string) --***[REQUIRED]**

        The ID of the target. If the target type of the target group is ``instance`` , specify an
        instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
        ``lambda`` , specify the ARN of the Lambda function.
    """


_TargetInServiceWaitWaiterConfigTypeDef = TypedDict(
    "_TargetInServiceWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class TargetInServiceWaitWaiterConfigTypeDef(_TargetInServiceWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """
