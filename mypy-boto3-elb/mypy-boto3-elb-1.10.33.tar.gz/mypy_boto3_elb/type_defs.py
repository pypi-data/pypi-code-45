"Main interface for elb service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


AnyInstanceInServiceWaitInstancesTypeDef = TypedDict(
    "AnyInstanceInServiceWaitInstancesTypeDef", {"InstanceId": str}, total=False
)

AnyInstanceInServiceWaitWaiterConfigTypeDef = TypedDict(
    "AnyInstanceInServiceWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

_RequiredClientAddTagsTagsTypeDef = TypedDict("_RequiredClientAddTagsTagsTypeDef", {"Key": str})
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    pass


ClientApplySecurityGroupsToLoadBalancerResponseTypeDef = TypedDict(
    "ClientApplySecurityGroupsToLoadBalancerResponseTypeDef",
    {"SecurityGroups": List[str]},
    total=False,
)

ClientAttachLoadBalancerToSubnetsResponseTypeDef = TypedDict(
    "ClientAttachLoadBalancerToSubnetsResponseTypeDef", {"Subnets": List[str]}, total=False
)

_RequiredClientConfigureHealthCheckHealthCheckTypeDef = TypedDict(
    "_RequiredClientConfigureHealthCheckHealthCheckTypeDef", {"Target": str}
)
_OptionalClientConfigureHealthCheckHealthCheckTypeDef = TypedDict(
    "_OptionalClientConfigureHealthCheckHealthCheckTypeDef",
    {"Interval": int, "Timeout": int, "UnhealthyThreshold": int, "HealthyThreshold": int},
    total=False,
)


class ClientConfigureHealthCheckHealthCheckTypeDef(
    _RequiredClientConfigureHealthCheckHealthCheckTypeDef,
    _OptionalClientConfigureHealthCheckHealthCheckTypeDef,
):
    pass


ClientConfigureHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "ClientConfigureHealthCheckResponseHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)

ClientConfigureHealthCheckResponseTypeDef = TypedDict(
    "ClientConfigureHealthCheckResponseTypeDef",
    {"HealthCheck": ClientConfigureHealthCheckResponseHealthCheckTypeDef},
    total=False,
)

_RequiredClientCreateLoadBalancerListenersListenersTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerListenersListenersTypeDef", {"Protocol": str}
)
_OptionalClientCreateLoadBalancerListenersListenersTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerListenersListenersTypeDef",
    {
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)


class ClientCreateLoadBalancerListenersListenersTypeDef(
    _RequiredClientCreateLoadBalancerListenersListenersTypeDef,
    _OptionalClientCreateLoadBalancerListenersListenersTypeDef,
):
    pass


_RequiredClientCreateLoadBalancerListenersTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerListenersTypeDef", {"Protocol": str}
)
_OptionalClientCreateLoadBalancerListenersTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerListenersTypeDef",
    {
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)


class ClientCreateLoadBalancerListenersTypeDef(
    _RequiredClientCreateLoadBalancerListenersTypeDef,
    _OptionalClientCreateLoadBalancerListenersTypeDef,
):
    pass


ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef = TypedDict(
    "ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef",
    {"AttributeName": str, "AttributeValue": str},
    total=False,
)

ClientCreateLoadBalancerResponseTypeDef = TypedDict(
    "ClientCreateLoadBalancerResponseTypeDef", {"DNSName": str}, total=False
)

_RequiredClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLoadBalancerTagsTypeDef(
    _RequiredClientCreateLoadBalancerTagsTypeDef, _OptionalClientCreateLoadBalancerTagsTypeDef
):
    pass


ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef = TypedDict(
    "ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef", {"InstanceId": str}, total=False
)

ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef = TypedDict(
    "ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)

ClientDeregisterInstancesFromLoadBalancerResponseTypeDef = TypedDict(
    "ClientDeregisterInstancesFromLoadBalancerResponseTypeDef",
    {"Instances": List[ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef]},
    total=False,
)

ClientDescribeAccountLimitsResponseLimitsTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseLimitsTypeDef", {"Name": str, "Max": str}, total=False
)

ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseTypeDef",
    {"Limits": List[ClientDescribeAccountLimitsResponseLimitsTypeDef], "NextMarker": str},
    total=False,
)

ClientDescribeInstanceHealthInstancesTypeDef = TypedDict(
    "ClientDescribeInstanceHealthInstancesTypeDef", {"InstanceId": str}, total=False
)

ClientDescribeInstanceHealthResponseInstanceStatesTypeDef = TypedDict(
    "ClientDescribeInstanceHealthResponseInstanceStatesTypeDef",
    {"InstanceId": str, "State": str, "ReasonCode": str, "Description": str},
    total=False,
)

ClientDescribeInstanceHealthResponseTypeDef = TypedDict(
    "ClientDescribeInstanceHealthResponseTypeDef",
    {"InstanceStates": List[ClientDescribeInstanceHealthResponseInstanceStatesTypeDef]},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    {
        "LoadBalancerAttributes": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef
    },
    total=False,
)

ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef",
    {"AttributeName": str, "AttributeValue": str},
    total=False,
)

ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef",
    {
        "PolicyName": str,
        "PolicyTypeName": str,
        "PolicyAttributeDescriptions": List[
            ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeLoadBalancerPoliciesResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPoliciesResponseTypeDef",
    {
        "PolicyDescriptions": List[
            ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef
        ]
    },
    total=False,
)

ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef",
    {
        "AttributeName": str,
        "AttributeType": str,
        "Description": str,
        "DefaultValue": str,
        "Cardinality": str,
    },
    total=False,
)

ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef",
    {
        "PolicyTypeName": str,
        "Description": str,
        "PolicyAttributeTypeDescriptions": List[
            ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeLoadBalancerPolicyTypesResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerPolicyTypesResponseTypeDef",
    {
        "PolicyTypeDescriptions": List[
            ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef
        ]
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    {"InstancePort": int, "PolicyNames": List[str]},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    {
        "Listener": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef,
        "PolicyNames": List[str],
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieName": str},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieExpirationPeriod": int},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
        ],
        "LBCookieStickinessPolicies": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
        ],
        "OtherPolicies": List[str],
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    {"OwnerAlias": str, "GroupName": str},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef",
    {
        "LoadBalancerName": str,
        "DNSName": str,
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "ListenerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
        ],
        "Policies": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef,
        "BackendServerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
        ],
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "VPCId": str,
        "Instances": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef
        ],
        "HealthCheck": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef,
        "SourceSecurityGroup": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef,
        "SecurityGroups": List[str],
        "CreatedTime": datetime,
        "Scheme": str,
    },
    total=False,
)

ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeTagsResponseTagDescriptionsTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeTagsResponseTagDescriptionsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    {"LoadBalancerName": str, "Tags": List[ClientDescribeTagsResponseTagDescriptionsTagsTypeDef]},
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"TagDescriptions": List[ClientDescribeTagsResponseTagDescriptionsTypeDef]},
    total=False,
)

ClientDetachLoadBalancerFromSubnetsResponseTypeDef = TypedDict(
    "ClientDetachLoadBalancerFromSubnetsResponseTypeDef", {"Subnets": List[str]}, total=False
)

ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef = TypedDict(
    "ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef",
    {"AvailabilityZones": List[str]},
    total=False,
)

ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef = TypedDict(
    "ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef",
    {"AvailabilityZones": List[str]},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
)

ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)

ClientModifyLoadBalancerAttributesResponseTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef,
    },
    total=False,
)

ClientRegisterInstancesWithLoadBalancerInstancesTypeDef = TypedDict(
    "ClientRegisterInstancesWithLoadBalancerInstancesTypeDef", {"InstanceId": str}, total=False
)

ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef = TypedDict(
    "ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)

ClientRegisterInstancesWithLoadBalancerResponseTypeDef = TypedDict(
    "ClientRegisterInstancesWithLoadBalancerResponseTypeDef",
    {"Instances": List[ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef]},
    total=False,
)

ClientRemoveTagsTagsTypeDef = TypedDict("ClientRemoveTagsTagsTypeDef", {"Key": str}, total=False)

DescribeAccountLimitsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAccountLimitsPaginateResponseLimitsTypeDef = TypedDict(
    "DescribeAccountLimitsPaginateResponseLimitsTypeDef", {"Name": str, "Max": str}, total=False
)

DescribeAccountLimitsPaginateResponseTypeDef = TypedDict(
    "DescribeAccountLimitsPaginateResponseTypeDef",
    {"Limits": List[DescribeAccountLimitsPaginateResponseLimitsTypeDef], "NextToken": str},
    total=False,
)

DescribeLoadBalancersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    {"InstancePort": int, "PolicyNames": List[str]},
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    {
        "Listener": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef,
        "PolicyNames": List[str],
    },
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieName": str},
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieExpirationPeriod": int},
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
        ],
        "LBCookieStickinessPolicies": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
        ],
        "OtherPolicies": List[str],
    },
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    {"OwnerAlias": str, "GroupName": str},
    total=False,
)

DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef",
    {
        "LoadBalancerName": str,
        "DNSName": str,
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "ListenerDescriptions": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
        ],
        "Policies": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef,
        "BackendServerDescriptions": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
        ],
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "VPCId": str,
        "Instances": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef
        ],
        "HealthCheck": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef,
        "SourceSecurityGroup": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef,
        "SecurityGroups": List[str],
        "CreatedTime": datetime,
        "Scheme": str,
    },
    total=False,
)

DescribeLoadBalancersPaginateResponseTypeDef = TypedDict(
    "DescribeLoadBalancersPaginateResponseTypeDef",
    {
        "LoadBalancerDescriptions": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

InstanceDeregisteredWaitInstancesTypeDef = TypedDict(
    "InstanceDeregisteredWaitInstancesTypeDef", {"InstanceId": str}, total=False
)

InstanceDeregisteredWaitWaiterConfigTypeDef = TypedDict(
    "InstanceDeregisteredWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

InstanceInServiceWaitInstancesTypeDef = TypedDict(
    "InstanceInServiceWaitInstancesTypeDef", {"InstanceId": str}, total=False
)

InstanceInServiceWaitWaiterConfigTypeDef = TypedDict(
    "InstanceInServiceWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
