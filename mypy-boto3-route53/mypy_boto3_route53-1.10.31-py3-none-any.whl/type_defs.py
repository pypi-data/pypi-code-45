"Main interface for route53 service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef",
    "ClientAssociateVpcWithHostedZoneResponseTypeDef",
    "ClientAssociateVpcWithHostedZoneVPCTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchTypeDef",
    "ClientChangeResourceRecordSetsResponseChangeInfoTypeDef",
    "ClientChangeResourceRecordSetsResponseTypeDef",
    "ClientChangeTagsForResourceAddTagsTypeDef",
    "ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientCreateHealthCheckHealthCheckConfigTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckTypeDef",
    "ClientCreateHealthCheckResponseTypeDef",
    "ClientCreateHostedZoneHostedZoneConfigTypeDef",
    "ClientCreateHostedZoneResponseChangeInfoTypeDef",
    "ClientCreateHostedZoneResponseDelegationSetTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneConfigTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneTypeDef",
    "ClientCreateHostedZoneResponseVPCTypeDef",
    "ClientCreateHostedZoneResponseTypeDef",
    "ClientCreateHostedZoneVPCTypeDef",
    "ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    "ClientCreateQueryLoggingConfigResponseTypeDef",
    "ClientCreateReusableDelegationSetResponseDelegationSetTypeDef",
    "ClientCreateReusableDelegationSetResponseTypeDef",
    "ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientCreateTrafficPolicyInstanceResponseTypeDef",
    "ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef",
    "ClientCreateTrafficPolicyResponseTypeDef",
    "ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef",
    "ClientCreateTrafficPolicyVersionResponseTypeDef",
    "ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef",
    "ClientCreateVpcAssociationAuthorizationResponseTypeDef",
    "ClientCreateVpcAssociationAuthorizationVPCTypeDef",
    "ClientDeleteHostedZoneResponseChangeInfoTypeDef",
    "ClientDeleteHostedZoneResponseTypeDef",
    "ClientDeleteVpcAssociationAuthorizationVPCTypeDef",
    "ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef",
    "ClientDisassociateVpcFromHostedZoneResponseTypeDef",
    "ClientDisassociateVpcFromHostedZoneVPCTypeDef",
    "ClientGetAccountLimitResponseLimitTypeDef",
    "ClientGetAccountLimitResponseTypeDef",
    "ClientGetChangeResponseChangeInfoTypeDef",
    "ClientGetChangeResponseTypeDef",
    "ClientGetCheckerIpRangesResponseTypeDef",
    "ClientGetGeoLocationResponseGeoLocationDetailsTypeDef",
    "ClientGetGeoLocationResponseTypeDef",
    "ClientGetHealthCheckCountResponseTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseTypeDef",
    "ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientGetHealthCheckResponseHealthCheckTypeDef",
    "ClientGetHealthCheckResponseTypeDef",
    "ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef",
    "ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef",
    "ClientGetHealthCheckStatusResponseTypeDef",
    "ClientGetHostedZoneCountResponseTypeDef",
    "ClientGetHostedZoneLimitResponseLimitTypeDef",
    "ClientGetHostedZoneLimitResponseTypeDef",
    "ClientGetHostedZoneResponseDelegationSetTypeDef",
    "ClientGetHostedZoneResponseHostedZoneConfigTypeDef",
    "ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    "ClientGetHostedZoneResponseHostedZoneTypeDef",
    "ClientGetHostedZoneResponseVPCsTypeDef",
    "ClientGetHostedZoneResponseTypeDef",
    "ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    "ClientGetQueryLoggingConfigResponseTypeDef",
    "ClientGetReusableDelegationSetLimitResponseLimitTypeDef",
    "ClientGetReusableDelegationSetLimitResponseTypeDef",
    "ClientGetReusableDelegationSetResponseDelegationSetTypeDef",
    "ClientGetReusableDelegationSetResponseTypeDef",
    "ClientGetTrafficPolicyInstanceCountResponseTypeDef",
    "ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientGetTrafficPolicyInstanceResponseTypeDef",
    "ClientGetTrafficPolicyResponseTrafficPolicyTypeDef",
    "ClientGetTrafficPolicyResponseTypeDef",
    "ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef",
    "ClientListGeoLocationsResponseTypeDef",
    "ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    "ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef",
    "ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef",
    "ClientListHealthChecksResponseHealthChecksTypeDef",
    "ClientListHealthChecksResponseTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesTypeDef",
    "ClientListHostedZonesByNameResponseTypeDef",
    "ClientListHostedZonesResponseHostedZonesConfigTypeDef",
    "ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef",
    "ClientListHostedZonesResponseHostedZonesTypeDef",
    "ClientListHostedZonesResponseTypeDef",
    "ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef",
    "ClientListQueryLoggingConfigsResponseTypeDef",
    "ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef",
    "ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef",
    "ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef",
    "ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef",
    "ClientListResourceRecordSetsResponseTypeDef",
    "ClientListReusableDelegationSetsResponseDelegationSetsTypeDef",
    "ClientListReusableDelegationSetsResponseTypeDef",
    "ClientListTagsForResourceResponseResourceTagSetTagsTypeDef",
    "ClientListTagsForResourceResponseResourceTagSetTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef",
    "ClientListTagsForResourcesResponseResourceTagSetsTypeDef",
    "ClientListTagsForResourcesResponseTypeDef",
    "ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef",
    "ClientListTrafficPoliciesResponseTypeDef",
    "ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesResponseTypeDef",
    "ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef",
    "ClientListTrafficPolicyVersionsResponseTypeDef",
    "ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef",
    "ClientListVpcAssociationAuthorizationsResponseTypeDef",
    "ClientTestDnsAnswerResponseTypeDef",
    "ClientUpdateHealthCheckAlarmIdentifierTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckTypeDef",
    "ClientUpdateHealthCheckResponseTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef",
    "ClientUpdateHostedZoneCommentResponseTypeDef",
    "ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef",
    "ClientUpdateTrafficPolicyCommentResponseTypeDef",
    "ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientUpdateTrafficPolicyInstanceResponseTypeDef",
    "ListHealthChecksPaginatePaginationConfigTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksTypeDef",
    "ListHealthChecksPaginateResponseTypeDef",
    "ListHostedZonesPaginatePaginationConfigTypeDef",
    "ListHostedZonesPaginateResponseHostedZonesConfigTypeDef",
    "ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef",
    "ListHostedZonesPaginateResponseHostedZonesTypeDef",
    "ListHostedZonesPaginateResponseTypeDef",
    "ListQueryLoggingConfigsPaginatePaginationConfigTypeDef",
    "ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef",
    "ListQueryLoggingConfigsPaginateResponseTypeDef",
    "ListResourceRecordSetsPaginatePaginationConfigTypeDef",
    "ListResourceRecordSetsPaginateResponseResourceRecordSetsAliasTargetTypeDef",
    "ListResourceRecordSetsPaginateResponseResourceRecordSetsGeoLocationTypeDef",
    "ListResourceRecordSetsPaginateResponseResourceRecordSetsResourceRecordsTypeDef",
    "ListResourceRecordSetsPaginateResponseResourceRecordSetsTypeDef",
    "ListResourceRecordSetsPaginateResponseTypeDef",
    "ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef",
    "ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef",
    "ListVPCAssociationAuthorizationsPaginateResponseTypeDef",
    "ResourceRecordSetsChangedWaitWaiterConfigTypeDef",
)


_ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "_ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef(
    _ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef
):
    """
    - **ChangeInfo** *(dict) --*

      A complex type that describes the changes made to your hosted zone.
      - **Id** *(string) --*

        The ID of the request.
    """


_ClientAssociateVpcWithHostedZoneResponseTypeDef = TypedDict(
    "_ClientAssociateVpcWithHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef},
    total=False,
)


class ClientAssociateVpcWithHostedZoneResponseTypeDef(
    _ClientAssociateVpcWithHostedZoneResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the ``AssociateVPCWithHostedZone``
      request.
      - **ChangeInfo** *(dict) --*

        A complex type that describes the changes made to your hosted zone.
        - **Id** *(string) --*

          The ID of the request.
    """


_ClientAssociateVpcWithHostedZoneVPCTypeDef = TypedDict(
    "_ClientAssociateVpcWithHostedZoneVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientAssociateVpcWithHostedZoneVPCTypeDef(_ClientAssociateVpcWithHostedZoneVPCTypeDef):
    """
    A complex type that contains information about the VPC that you want to associate with a private
    hosted zone.
    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.
    """


_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef",
    {"HostedZoneId": str, "DNSName": str, "EvaluateTargetHealth": bool},
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef(
    _ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef
):
    pass


_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef",
    {"ContinentCode": str, "CountryCode": str, "SubdivisionCode": str},
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef(
    _ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef
):
    pass


_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef",
    {"Value": str},
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef(
    _ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef
):
    pass


_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "SetIdentifier": str,
        "Weight": int,
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-north-1",
            "cn-northwest-1",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
        ],
        "GeoLocation": ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef,
        "Failover": Literal["PRIMARY", "SECONDARY"],
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List[
            ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetResourceRecordsTypeDef
        ],
        "AliasTarget": ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetAliasTargetTypeDef,
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef(
    _ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef
):
    pass


_ClientChangeResourceRecordSetsChangeBatchChangesTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsChangeBatchChangesTypeDef",
    {
        "Action": Literal["CREATE", "DELETE", "UPSERT"],
        "ResourceRecordSet": ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef,
    },
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchChangesTypeDef(
    _ClientChangeResourceRecordSetsChangeBatchChangesTypeDef
):
    pass


_ClientChangeResourceRecordSetsChangeBatchTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsChangeBatchTypeDef",
    {"Comment": str, "Changes": List[ClientChangeResourceRecordSetsChangeBatchChangesTypeDef]},
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchTypeDef(
    _ClientChangeResourceRecordSetsChangeBatchTypeDef
):
    """
    A complex type that contains an optional comment and the ``Changes`` element.
    - **Comment** *(string) --*

      *Optional:* Any comments you want to include about a change batch request.
    """


_ClientChangeResourceRecordSetsResponseChangeInfoTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientChangeResourceRecordSetsResponseChangeInfoTypeDef(
    _ClientChangeResourceRecordSetsResponseChangeInfoTypeDef
):
    """
    - **ChangeInfo** *(dict) --*

      A complex type that contains information about changes made to your hosted zone.
      This element contains an ID that you use when performing a `GetChange
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to get
      detailed information about the change.
      - **Id** *(string) --*

        The ID of the request.
    """


_ClientChangeResourceRecordSetsResponseTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsResponseTypeDef",
    {"ChangeInfo": ClientChangeResourceRecordSetsResponseChangeInfoTypeDef},
    total=False,
)


class ClientChangeResourceRecordSetsResponseTypeDef(_ClientChangeResourceRecordSetsResponseTypeDef):
    """
    - *(dict) --*

      A complex type containing the response for the request.
      - **ChangeInfo** *(dict) --*

        A complex type that contains information about changes made to your hosted zone.
        This element contains an ID that you use when performing a `GetChange
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
        get detailed information about the change.
        - **Id** *(string) --*

          The ID of the request.
    """


_ClientChangeTagsForResourceAddTagsTypeDef = TypedDict(
    "_ClientChangeTagsForResourceAddTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientChangeTagsForResourceAddTagsTypeDef(_ClientChangeTagsForResourceAddTagsTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about a tag that you want to add or edit for the
      specified health check or hosted zone.
      - **Key** *(string) --*

        The value of ``Key`` depends on the operation that you want to perform:
        * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want to give
        the new tag.
        * **Edit a tag** : ``Key`` is the name of the tag that you want to change the ``Value`` for.
        * **Delete a key** : ``Key`` is the name of the tag you want to remove.
        * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon Route 53
        console, the list of your health checks includes a **Name** column that lets you see the
        name that you've given to each health check.
    """


_ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)


class ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef
):
    pass


_ClientCreateHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_ClientCreateHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)


class ClientCreateHealthCheckHealthCheckConfigTypeDef(
    _ClientCreateHealthCheckHealthCheckConfigTypeDef
):
    """
    A complex type that contains settings for a new health check.
    - **IPAddress** *(string) --*

      The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health
      checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS request to
      resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that
      you specify in ``RequestInterval`` . Using an IP address returned by DNS, Route 53 then checks
      the health of the endpoint.
      Use one of the following formats for the value of ``IPAddress`` :
      * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example,
      ``192.0.2.44`` .
      * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for
      example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as
      described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .
      If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
      associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` .
      This ensures that the IP address of your instance will never change.
      For more information, see `FullyQualifiedDomainName
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
      .
      Constraints: Route 53 can't check the health of endpoints for which the IP address is in
      local, private, non-routable, or multicast ranges. For more information about IP addresses for
      which you can't create health checks, see the following documents:
      * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__
      * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
      <https://tools.ietf.org/html/rfc6598>`__
      * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__
      When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .
    """


_ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
):
    pass


_ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef
):
    pass


_ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef
):
    pass


_ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef
):
    pass


_ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef
):
    pass


_ClientCreateHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckTypeDef
):
    """
    - **HealthCheck** *(dict) --*

      A complex type that contains identifying information about the health check.
      - **Id** *(string) --*

        The identifier that Amazon Route 53assigned to the health check when you created it. When
        you add or update a resource record set, you use this value to specify which health check to
        use. The value can be up to 64 characters long.
    """


_ClientCreateHealthCheckResponseTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseTypeDef",
    {"HealthCheck": ClientCreateHealthCheckResponseHealthCheckTypeDef, "Location": str},
    total=False,
)


class ClientCreateHealthCheckResponseTypeDef(_ClientCreateHealthCheckResponseTypeDef):
    """
    - *(dict) --*

      A complex type containing the response information for the new health check.
      - **HealthCheck** *(dict) --*

        A complex type that contains identifying information about the health check.
        - **Id** *(string) --*

          The identifier that Amazon Route 53assigned to the health check when you created it. When
          you add or update a resource record set, you use this value to specify which health check
          to use. The value can be up to 64 characters long.
    """


_ClientCreateHostedZoneHostedZoneConfigTypeDef = TypedDict(
    "_ClientCreateHostedZoneHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientCreateHostedZoneHostedZoneConfigTypeDef(_ClientCreateHostedZoneHostedZoneConfigTypeDef):
    """
    (Optional) A complex type that contains the following optional values:
    * For public and private hosted zones, an optional comment
    * For private hosted zones, an optional ``PrivateZone`` element
    If you don't specify a comment or the ``PrivateZone`` element, omit ``HostedZoneConfig`` and the
    other elements.
    - **Comment** *(string) --*

      Any comments that you want to include about the hosted zone.
    """


_ClientCreateHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientCreateHostedZoneResponseChangeInfoTypeDef(
    _ClientCreateHostedZoneResponseChangeInfoTypeDef
):
    pass


_ClientCreateHostedZoneResponseDelegationSetTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientCreateHostedZoneResponseDelegationSetTypeDef(
    _ClientCreateHostedZoneResponseDelegationSetTypeDef
):
    pass


_ClientCreateHostedZoneResponseHostedZoneConfigTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientCreateHostedZoneResponseHostedZoneConfigTypeDef(
    _ClientCreateHostedZoneResponseHostedZoneConfigTypeDef
):
    pass


_ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef(
    _ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef
):
    pass


_ClientCreateHostedZoneResponseHostedZoneTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientCreateHostedZoneResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)


class ClientCreateHostedZoneResponseHostedZoneTypeDef(
    _ClientCreateHostedZoneResponseHostedZoneTypeDef
):
    """
    - **HostedZone** *(dict) --*

      A complex type that contains general information about the hosted zone.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientCreateHostedZoneResponseVPCTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientCreateHostedZoneResponseVPCTypeDef(_ClientCreateHostedZoneResponseVPCTypeDef):
    pass


_ClientCreateHostedZoneResponseTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseTypeDef",
    {
        "HostedZone": ClientCreateHostedZoneResponseHostedZoneTypeDef,
        "ChangeInfo": ClientCreateHostedZoneResponseChangeInfoTypeDef,
        "DelegationSet": ClientCreateHostedZoneResponseDelegationSetTypeDef,
        "VPC": ClientCreateHostedZoneResponseVPCTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateHostedZoneResponseTypeDef(_ClientCreateHostedZoneResponseTypeDef):
    """
    - *(dict) --*

      A complex type containing the response information for the hosted zone.
      - **HostedZone** *(dict) --*

        A complex type that contains general information about the hosted zone.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientCreateHostedZoneVPCTypeDef = TypedDict(
    "_ClientCreateHostedZoneVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientCreateHostedZoneVPCTypeDef(_ClientCreateHostedZoneVPCTypeDef):
    """
    (Private hosted zones only) A complex type that contains information about the Amazon VPC that
    you're associating with this hosted zone.
    You can specify only one Amazon VPC when you create a private hosted zone. To associate
    additional Amazon VPCs with the hosted zone, use `AssociateVPCWithHostedZone
    <https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html>`__
    after you create a hosted zone.
    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.
    """


_ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef = TypedDict(
    "_ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)


class ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef(
    _ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef
):
    """
    - **QueryLoggingConfig** *(dict) --*

      A complex type that contains the ID for a query logging configuration, the ID of the hosted
      zone that you want to log queries for, and the ARN for the log group that you want Amazon
      Route 53 to send query logs to.
      - **Id** *(string) --*

        The ID for a configuration for DNS query logging.
    """


_ClientCreateQueryLoggingConfigResponseTypeDef = TypedDict(
    "_ClientCreateQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateQueryLoggingConfigResponseTypeDef(_ClientCreateQueryLoggingConfigResponseTypeDef):
    """
    - *(dict) --*

      - **QueryLoggingConfig** *(dict) --*

        A complex type that contains the ID for a query logging configuration, the ID of the hosted
        zone that you want to log queries for, and the ARN for the log group that you want Amazon
        Route 53 to send query logs to.
        - **Id** *(string) --*

          The ID for a configuration for DNS query logging.
    """


_ClientCreateReusableDelegationSetResponseDelegationSetTypeDef = TypedDict(
    "_ClientCreateReusableDelegationSetResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientCreateReusableDelegationSetResponseDelegationSetTypeDef(
    _ClientCreateReusableDelegationSetResponseDelegationSetTypeDef
):
    """
    - **DelegationSet** *(dict) --*

      A complex type that contains name server information.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigns to a reusable delegation set.
    """


_ClientCreateReusableDelegationSetResponseTypeDef = TypedDict(
    "_ClientCreateReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": ClientCreateReusableDelegationSetResponseDelegationSetTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateReusableDelegationSetResponseTypeDef(
    _ClientCreateReusableDelegationSetResponseTypeDef
):
    """
    - *(dict) --*

      - **DelegationSet** *(dict) --*

        A complex type that contains name server information.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigns to a reusable delegation set.
    """


_ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)


class ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef(
    _ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
):
    """
    - **TrafficPolicyInstance** *(dict) --*

      A complex type that contains settings for the new traffic policy instance.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientCreateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyInstanceResponseTypeDef(
    _ClientCreateTrafficPolicyInstanceResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the ``CreateTrafficPolicyInstance``
      request.
      - **TrafficPolicyInstance** *(dict) --*

        A complex type that contains settings for the new traffic policy instance.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef(
    _ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef
):
    """
    - **TrafficPolicy** *(dict) --*

      A complex type that contains settings for the new traffic policy.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientCreateTrafficPolicyResponseTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyResponseTypeDef",
    {"TrafficPolicy": ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef, "Location": str},
    total=False,
)


class ClientCreateTrafficPolicyResponseTypeDef(_ClientCreateTrafficPolicyResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response information for the ``CreateTrafficPolicy`` request.
      - **TrafficPolicy** *(dict) --*

        A complex type that contains settings for the new traffic policy.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef(
    _ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef
):
    """
    - **TrafficPolicy** *(dict) --*

      A complex type that contains settings for the new version of the traffic policy.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientCreateTrafficPolicyVersionResponseTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyVersionResponseTypeDef",
    {
        "TrafficPolicy": ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyVersionResponseTypeDef(
    _ClientCreateTrafficPolicyVersionResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the ``CreateTrafficPolicyVersion``
      request.
      - **TrafficPolicy** *(dict) --*

        A complex type that contains settings for the new version of the traffic policy.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef = TypedDict(
    "_ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef(
    _ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef
):
    pass


_ClientCreateVpcAssociationAuthorizationResponseTypeDef = TypedDict(
    "_ClientCreateVpcAssociationAuthorizationResponseTypeDef",
    {"HostedZoneId": str, "VPC": ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef},
    total=False,
)


class ClientCreateVpcAssociationAuthorizationResponseTypeDef(
    _ClientCreateVpcAssociationAuthorizationResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information from a
      ``CreateVPCAssociationAuthorization`` request.
      - **HostedZoneId** *(string) --*

        The ID of the hosted zone that you authorized associating a VPC with.
    """


_ClientCreateVpcAssociationAuthorizationVPCTypeDef = TypedDict(
    "_ClientCreateVpcAssociationAuthorizationVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientCreateVpcAssociationAuthorizationVPCTypeDef(
    _ClientCreateVpcAssociationAuthorizationVPCTypeDef
):
    """
    A complex type that contains the VPC ID and region for the VPC that you want to authorize
    associating with your hosted zone.
    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.
    """


_ClientDeleteHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "_ClientDeleteHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientDeleteHostedZoneResponseChangeInfoTypeDef(
    _ClientDeleteHostedZoneResponseChangeInfoTypeDef
):
    """
    - **ChangeInfo** *(dict) --*

      A complex type that contains the ID, the status, and the date and time of a request to delete
      a hosted zone.
      - **Id** *(string) --*

        The ID of the request.
    """


_ClientDeleteHostedZoneResponseTypeDef = TypedDict(
    "_ClientDeleteHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientDeleteHostedZoneResponseChangeInfoTypeDef},
    total=False,
)


class ClientDeleteHostedZoneResponseTypeDef(_ClientDeleteHostedZoneResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to a ``DeleteHostedZone`` request.
      - **ChangeInfo** *(dict) --*

        A complex type that contains the ID, the status, and the date and time of a request to
        delete a hosted zone.
        - **Id** *(string) --*

          The ID of the request.
    """


_ClientDeleteVpcAssociationAuthorizationVPCTypeDef = TypedDict(
    "_ClientDeleteVpcAssociationAuthorizationVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientDeleteVpcAssociationAuthorizationVPCTypeDef(
    _ClientDeleteVpcAssociationAuthorizationVPCTypeDef
):
    """
    When removing authorization to associate a VPC that was created by one AWS account with a hosted
    zone that was created with a different AWS account, a complex type that includes the ID and
    region of the VPC.
    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.
    """


_ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "_ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef(
    _ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef
):
    """
    - **ChangeInfo** *(dict) --*

      A complex type that describes the changes made to the specified private hosted zone.
      - **Id** *(string) --*

        The ID of the request.
    """


_ClientDisassociateVpcFromHostedZoneResponseTypeDef = TypedDict(
    "_ClientDisassociateVpcFromHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef},
    total=False,
)


class ClientDisassociateVpcFromHostedZoneResponseTypeDef(
    _ClientDisassociateVpcFromHostedZoneResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the disassociate request.
      - **ChangeInfo** *(dict) --*

        A complex type that describes the changes made to the specified private hosted zone.
        - **Id** *(string) --*

          The ID of the request.
    """


_ClientDisassociateVpcFromHostedZoneVPCTypeDef = TypedDict(
    "_ClientDisassociateVpcFromHostedZoneVPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientDisassociateVpcFromHostedZoneVPCTypeDef(_ClientDisassociateVpcFromHostedZoneVPCTypeDef):
    """
    A complex type that contains information about the VPC that you're disassociating from the
    specified hosted zone.
    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.
    """


_ClientGetAccountLimitResponseLimitTypeDef = TypedDict(
    "_ClientGetAccountLimitResponseLimitTypeDef",
    {
        "Type": Literal[
            "MAX_HEALTH_CHECKS_BY_OWNER",
            "MAX_HOSTED_ZONES_BY_OWNER",
            "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER",
            "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER",
            "MAX_TRAFFIC_POLICIES_BY_OWNER",
        ],
        "Value": int,
    },
    total=False,
)


class ClientGetAccountLimitResponseLimitTypeDef(_ClientGetAccountLimitResponseLimitTypeDef):
    """
    - **Limit** *(dict) --*

      The current setting for the specified limit. For example, if you specified
      ``MAX_HEALTH_CHECKS_BY_OWNER`` for the value of ``Type`` in the request, the value of
      ``Limit`` is the maximum number of health checks that you can create using the current
      account.
      - **Type** *(string) --*

        The limit that you requested. Valid values include the following:
        * **MAX_HEALTH_CHECKS_BY_OWNER** : The maximum number of health checks that you can create
        using the current account.
        * **MAX_HOSTED_ZONES_BY_OWNER** : The maximum number of hosted zones that you can create
        using the current account.
        * **MAX_REUSABLE_DELEGATION_SETS_BY_OWNER** : The maximum number of reusable delegation sets
        that you can create using the current account.
        * **MAX_TRAFFIC_POLICIES_BY_OWNER** : The maximum number of traffic policies that you can
        create using the current account.
        * **MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER** : The maximum number of traffic policy instances
        that you can create using the current account. (Traffic policy instances are referred to as
        traffic flow policy records in the Amazon Route 53 console.)
    """


_ClientGetAccountLimitResponseTypeDef = TypedDict(
    "_ClientGetAccountLimitResponseTypeDef",
    {"Limit": ClientGetAccountLimitResponseLimitTypeDef, "Count": int},
    total=False,
)


class ClientGetAccountLimitResponseTypeDef(_ClientGetAccountLimitResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the requested limit.
      - **Limit** *(dict) --*

        The current setting for the specified limit. For example, if you specified
        ``MAX_HEALTH_CHECKS_BY_OWNER`` for the value of ``Type`` in the request, the value of
        ``Limit`` is the maximum number of health checks that you can create using the current
        account.
        - **Type** *(string) --*

          The limit that you requested. Valid values include the following:
          * **MAX_HEALTH_CHECKS_BY_OWNER** : The maximum number of health checks that you can create
          using the current account.
          * **MAX_HOSTED_ZONES_BY_OWNER** : The maximum number of hosted zones that you can create
          using the current account.
          * **MAX_REUSABLE_DELEGATION_SETS_BY_OWNER** : The maximum number of reusable delegation
          sets that you can create using the current account.
          * **MAX_TRAFFIC_POLICIES_BY_OWNER** : The maximum number of traffic policies that you can
          create using the current account.
          * **MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER** : The maximum number of traffic policy
          instances that you can create using the current account. (Traffic policy instances are
          referred to as traffic flow policy records in the Amazon Route 53 console.)
    """


_ClientGetChangeResponseChangeInfoTypeDef = TypedDict(
    "_ClientGetChangeResponseChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientGetChangeResponseChangeInfoTypeDef(_ClientGetChangeResponseChangeInfoTypeDef):
    """
    - **ChangeInfo** *(dict) --*

      A complex type that contains information about the specified change batch.
      - **Id** *(string) --*

        The ID of the request.
    """


_ClientGetChangeResponseTypeDef = TypedDict(
    "_ClientGetChangeResponseTypeDef",
    {"ChangeInfo": ClientGetChangeResponseChangeInfoTypeDef},
    total=False,
)


class ClientGetChangeResponseTypeDef(_ClientGetChangeResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the ``ChangeInfo`` element.
      - **ChangeInfo** *(dict) --*

        A complex type that contains information about the specified change batch.
        - **Id** *(string) --*

          The ID of the request.
    """


_ClientGetCheckerIpRangesResponseTypeDef = TypedDict(
    "_ClientGetCheckerIpRangesResponseTypeDef", {"CheckerIpRanges": List[str]}, total=False
)


class ClientGetCheckerIpRangesResponseTypeDef(_ClientGetCheckerIpRangesResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the ``CheckerIpRanges`` element.
      - **CheckerIpRanges** *(list) --*

        A complex type that contains sorted list of IP ranges in CIDR format for Amazon Route 53
        health checkers.
        - *(string) --*
    """


_ClientGetGeoLocationResponseGeoLocationDetailsTypeDef = TypedDict(
    "_ClientGetGeoLocationResponseGeoLocationDetailsTypeDef",
    {
        "ContinentCode": str,
        "ContinentName": str,
        "CountryCode": str,
        "CountryName": str,
        "SubdivisionCode": str,
        "SubdivisionName": str,
    },
    total=False,
)


class ClientGetGeoLocationResponseGeoLocationDetailsTypeDef(
    _ClientGetGeoLocationResponseGeoLocationDetailsTypeDef
):
    """
    - **GeoLocationDetails** *(dict) --*

      A complex type that contains the codes and full continent, country, and subdivision names for
      the specified geolocation code.
      - **ContinentCode** *(string) --*

        The two-letter code for the continent.
    """


_ClientGetGeoLocationResponseTypeDef = TypedDict(
    "_ClientGetGeoLocationResponseTypeDef",
    {"GeoLocationDetails": ClientGetGeoLocationResponseGeoLocationDetailsTypeDef},
    total=False,
)


class ClientGetGeoLocationResponseTypeDef(_ClientGetGeoLocationResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response information for the specified geolocation code.
      - **GeoLocationDetails** *(dict) --*

        A complex type that contains the codes and full continent, country, and subdivision names
        for the specified geolocation code.
        - **ContinentCode** *(string) --*

          The two-letter code for the continent.
    """


_ClientGetHealthCheckCountResponseTypeDef = TypedDict(
    "_ClientGetHealthCheckCountResponseTypeDef", {"HealthCheckCount": int}, total=False
)


class ClientGetHealthCheckCountResponseTypeDef(_ClientGetHealthCheckCountResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to a ``GetHealthCheckCount`` request.
      - **HealthCheckCount** *(integer) --*

        The number of health checks associated with the current AWS account.
    """


_ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef = TypedDict(
    "_ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef",
    {"Status": str, "CheckedTime": datetime},
    total=False,
)


class ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef(
    _ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef
):
    pass


_ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef = TypedDict(
    "_ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
        ],
        "IPAddress": str,
        "StatusReport": ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef,
    },
    total=False,
)


class ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef(
    _ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the last failure reason as reported by one Amazon Route 53 health
      checker.
      - **Region** *(string) --*

        The region of the Amazon Route 53 health checker that provided the status in
        ``StatusReport`` .
    """


_ClientGetHealthCheckLastFailureReasonResponseTypeDef = TypedDict(
    "_ClientGetHealthCheckLastFailureReasonResponseTypeDef",
    {
        "HealthCheckObservations": List[
            ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef
        ]
    },
    total=False,
)


class ClientGetHealthCheckLastFailureReasonResponseTypeDef(
    _ClientGetHealthCheckLastFailureReasonResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response to a ``GetHealthCheckLastFailureReason`` request.
      - **HealthCheckObservations** *(list) --*

        A list that contains one ``Observation`` element for each Amazon Route 53 health checker
        that is reporting a last failure reason.
        - *(dict) --*

          A complex type that contains the last failure reason as reported by one Amazon Route 53
          health checker.
          - **Region** *(string) --*

            The region of the Amazon Route 53 health checker that provided the status in
            ``StatusReport`` .
    """


_ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
):
    pass


_ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef(
    _ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef
):
    pass


_ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef
):
    pass


_ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef(
    _ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef
):
    pass


_ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef(
    _ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef
):
    pass


_ClientGetHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckTypeDef(
    _ClientGetHealthCheckResponseHealthCheckTypeDef
):
    """
    - **HealthCheck** *(dict) --*

      A complex type that contains information about one health check that is associated with the
      current AWS account.
      - **Id** *(string) --*

        The identifier that Amazon Route 53assigned to the health check when you created it. When
        you add or update a resource record set, you use this value to specify which health check to
        use. The value can be up to 64 characters long.
    """


_ClientGetHealthCheckResponseTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseTypeDef",
    {"HealthCheck": ClientGetHealthCheckResponseHealthCheckTypeDef},
    total=False,
)


class ClientGetHealthCheckResponseTypeDef(_ClientGetHealthCheckResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to a ``GetHealthCheck`` request.
      - **HealthCheck** *(dict) --*

        A complex type that contains information about one health check that is associated with the
        current AWS account.
        - **Id** *(string) --*

          The identifier that Amazon Route 53assigned to the health check when you created it. When
          you add or update a resource record set, you use this value to specify which health check
          to use. The value can be up to 64 characters long.
    """


_ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef = TypedDict(
    "_ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef",
    {"Status": str, "CheckedTime": datetime},
    total=False,
)


class ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef(
    _ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef
):
    pass


_ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef = TypedDict(
    "_ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
        ],
        "IPAddress": str,
        "StatusReport": ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef,
    },
    total=False,
)


class ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef(
    _ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the last failure reason as reported by one Amazon Route 53 health
      checker.
      - **Region** *(string) --*

        The region of the Amazon Route 53 health checker that provided the status in
        ``StatusReport`` .
    """


_ClientGetHealthCheckStatusResponseTypeDef = TypedDict(
    "_ClientGetHealthCheckStatusResponseTypeDef",
    {
        "HealthCheckObservations": List[
            ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef
        ]
    },
    total=False,
)


class ClientGetHealthCheckStatusResponseTypeDef(_ClientGetHealthCheckStatusResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to a ``GetHealthCheck`` request.
      - **HealthCheckObservations** *(list) --*

        A list that contains one ``HealthCheckObservation`` element for each Amazon Route 53 health
        checker that is reporting a status about the health check endpoint.
        - *(dict) --*

          A complex type that contains the last failure reason as reported by one Amazon Route 53
          health checker.
          - **Region** *(string) --*

            The region of the Amazon Route 53 health checker that provided the status in
            ``StatusReport`` .
    """


_ClientGetHostedZoneCountResponseTypeDef = TypedDict(
    "_ClientGetHostedZoneCountResponseTypeDef", {"HostedZoneCount": int}, total=False
)


class ClientGetHostedZoneCountResponseTypeDef(_ClientGetHostedZoneCountResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to a ``GetHostedZoneCount`` request.
      - **HostedZoneCount** *(integer) --*

        The total number of public and private hosted zones that are associated with the current AWS
        account.
    """


_ClientGetHostedZoneLimitResponseLimitTypeDef = TypedDict(
    "_ClientGetHostedZoneLimitResponseLimitTypeDef",
    {"Type": Literal["MAX_RRSETS_BY_ZONE", "MAX_VPCS_ASSOCIATED_BY_ZONE"], "Value": int},
    total=False,
)


class ClientGetHostedZoneLimitResponseLimitTypeDef(_ClientGetHostedZoneLimitResponseLimitTypeDef):
    """
    - **Limit** *(dict) --*

      The current setting for the specified limit. For example, if you specified
      ``MAX_RRSETS_BY_ZONE`` for the value of ``Type`` in the request, the value of ``Limit`` is the
      maximum number of records that you can create in the specified hosted zone.
      - **Type** *(string) --*

        The limit that you requested. Valid values include the following:
        * **MAX_RRSETS_BY_ZONE** : The maximum number of records that you can create in the
        specified hosted zone.
        * **MAX_VPCS_ASSOCIATED_BY_ZONE** : The maximum number of Amazon VPCs that you can associate
        with the specified private hosted zone.
    """


_ClientGetHostedZoneLimitResponseTypeDef = TypedDict(
    "_ClientGetHostedZoneLimitResponseTypeDef",
    {"Limit": ClientGetHostedZoneLimitResponseLimitTypeDef, "Count": int},
    total=False,
)


class ClientGetHostedZoneLimitResponseTypeDef(_ClientGetHostedZoneLimitResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the requested limit.
      - **Limit** *(dict) --*

        The current setting for the specified limit. For example, if you specified
        ``MAX_RRSETS_BY_ZONE`` for the value of ``Type`` in the request, the value of ``Limit`` is
        the maximum number of records that you can create in the specified hosted zone.
        - **Type** *(string) --*

          The limit that you requested. Valid values include the following:
          * **MAX_RRSETS_BY_ZONE** : The maximum number of records that you can create in the
          specified hosted zone.
          * **MAX_VPCS_ASSOCIATED_BY_ZONE** : The maximum number of Amazon VPCs that you can
          associate with the specified private hosted zone.
    """


_ClientGetHostedZoneResponseDelegationSetTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientGetHostedZoneResponseDelegationSetTypeDef(
    _ClientGetHostedZoneResponseDelegationSetTypeDef
):
    pass


_ClientGetHostedZoneResponseHostedZoneConfigTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientGetHostedZoneResponseHostedZoneConfigTypeDef(
    _ClientGetHostedZoneResponseHostedZoneConfigTypeDef
):
    pass


_ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef(
    _ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef
):
    pass


_ClientGetHostedZoneResponseHostedZoneTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientGetHostedZoneResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)


class ClientGetHostedZoneResponseHostedZoneTypeDef(_ClientGetHostedZoneResponseHostedZoneTypeDef):
    """
    - **HostedZone** *(dict) --*

      A complex type that contains general information about the specified hosted zone.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientGetHostedZoneResponseVPCsTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseVPCsTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientGetHostedZoneResponseVPCsTypeDef(_ClientGetHostedZoneResponseVPCsTypeDef):
    pass


_ClientGetHostedZoneResponseTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseTypeDef",
    {
        "HostedZone": ClientGetHostedZoneResponseHostedZoneTypeDef,
        "DelegationSet": ClientGetHostedZoneResponseDelegationSetTypeDef,
        "VPCs": List[ClientGetHostedZoneResponseVPCsTypeDef],
    },
    total=False,
)


class ClientGetHostedZoneResponseTypeDef(_ClientGetHostedZoneResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contain the response to a ``GetHostedZone`` request.
      - **HostedZone** *(dict) --*

        A complex type that contains general information about the specified hosted zone.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef = TypedDict(
    "_ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)


class ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef(
    _ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef
):
    """
    - **QueryLoggingConfig** *(dict) --*

      A complex type that contains information about the query logging configuration that you
      specified in a `GetQueryLoggingConfig
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html>`__
      request.
      - **Id** *(string) --*

        The ID for a configuration for DNS query logging.
    """


_ClientGetQueryLoggingConfigResponseTypeDef = TypedDict(
    "_ClientGetQueryLoggingConfigResponseTypeDef",
    {"QueryLoggingConfig": ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef},
    total=False,
)


class ClientGetQueryLoggingConfigResponseTypeDef(_ClientGetQueryLoggingConfigResponseTypeDef):
    """
    - *(dict) --*

      - **QueryLoggingConfig** *(dict) --*

        A complex type that contains information about the query logging configuration that you
        specified in a `GetQueryLoggingConfig
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html>`__
        request.
        - **Id** *(string) --*

          The ID for a configuration for DNS query logging.
    """


_ClientGetReusableDelegationSetLimitResponseLimitTypeDef = TypedDict(
    "_ClientGetReusableDelegationSetLimitResponseLimitTypeDef",
    {"Type": str, "Value": int},
    total=False,
)


class ClientGetReusableDelegationSetLimitResponseLimitTypeDef(
    _ClientGetReusableDelegationSetLimitResponseLimitTypeDef
):
    """
    - **Limit** *(dict) --*

      The current setting for the limit on hosted zones that you can associate with the specified
      reusable delegation set.
      - **Type** *(string) --*

        The limit that you requested: ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` , the maximum number
        of hosted zones that you can associate with the specified reusable delegation set.
    """


_ClientGetReusableDelegationSetLimitResponseTypeDef = TypedDict(
    "_ClientGetReusableDelegationSetLimitResponseTypeDef",
    {"Limit": ClientGetReusableDelegationSetLimitResponseLimitTypeDef, "Count": int},
    total=False,
)


class ClientGetReusableDelegationSetLimitResponseTypeDef(
    _ClientGetReusableDelegationSetLimitResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the requested limit.
      - **Limit** *(dict) --*

        The current setting for the limit on hosted zones that you can associate with the specified
        reusable delegation set.
        - **Type** *(string) --*

          The limit that you requested: ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` , the maximum
          number of hosted zones that you can associate with the specified reusable delegation set.
    """


_ClientGetReusableDelegationSetResponseDelegationSetTypeDef = TypedDict(
    "_ClientGetReusableDelegationSetResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientGetReusableDelegationSetResponseDelegationSetTypeDef(
    _ClientGetReusableDelegationSetResponseDelegationSetTypeDef
):
    """
    - **DelegationSet** *(dict) --*

      A complex type that contains information about the reusable delegation set.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigns to a reusable delegation set.
    """


_ClientGetReusableDelegationSetResponseTypeDef = TypedDict(
    "_ClientGetReusableDelegationSetResponseTypeDef",
    {"DelegationSet": ClientGetReusableDelegationSetResponseDelegationSetTypeDef},
    total=False,
)


class ClientGetReusableDelegationSetResponseTypeDef(_ClientGetReusableDelegationSetResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to the ``GetReusableDelegationSet`` request.
      - **DelegationSet** *(dict) --*

        A complex type that contains information about the reusable delegation set.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigns to a reusable delegation set.
    """


_ClientGetTrafficPolicyInstanceCountResponseTypeDef = TypedDict(
    "_ClientGetTrafficPolicyInstanceCountResponseTypeDef",
    {"TrafficPolicyInstanceCount": int},
    total=False,
)


class ClientGetTrafficPolicyInstanceCountResponseTypeDef(
    _ClientGetTrafficPolicyInstanceCountResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about the resource record sets that Amazon Route 53
      created based on a specified traffic policy.
      - **TrafficPolicyInstanceCount** *(integer) --*

        The number of traffic policy instances that are associated with the current AWS account.
    """


_ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "_ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)


class ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef(
    _ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
):
    """
    - **TrafficPolicyInstance** *(dict) --*

      A complex type that contains settings for the traffic policy instance.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientGetTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "_ClientGetTrafficPolicyInstanceResponseTypeDef",
    {"TrafficPolicyInstance": ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef},
    total=False,
)


class ClientGetTrafficPolicyInstanceResponseTypeDef(_ClientGetTrafficPolicyInstanceResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about the resource record sets that Amazon Route 53
      created based on a specified traffic policy.
      - **TrafficPolicyInstance** *(dict) --*

        A complex type that contains settings for the traffic policy instance.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientGetTrafficPolicyResponseTrafficPolicyTypeDef = TypedDict(
    "_ClientGetTrafficPolicyResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientGetTrafficPolicyResponseTrafficPolicyTypeDef(
    _ClientGetTrafficPolicyResponseTrafficPolicyTypeDef
):
    """
    - **TrafficPolicy** *(dict) --*

      A complex type that contains settings for the specified traffic policy.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientGetTrafficPolicyResponseTypeDef = TypedDict(
    "_ClientGetTrafficPolicyResponseTypeDef",
    {"TrafficPolicy": ClientGetTrafficPolicyResponseTrafficPolicyTypeDef},
    total=False,
)


class ClientGetTrafficPolicyResponseTypeDef(_ClientGetTrafficPolicyResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **TrafficPolicy** *(dict) --*

        A complex type that contains settings for the specified traffic policy.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef = TypedDict(
    "_ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef",
    {
        "ContinentCode": str,
        "ContinentName": str,
        "CountryCode": str,
        "CountryName": str,
        "SubdivisionCode": str,
        "SubdivisionName": str,
    },
    total=False,
)


class ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef(
    _ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the codes and full continent, country, and subdivision names for
      the specified ``geolocation`` code.
      - **ContinentCode** *(string) --*

        The two-letter code for the continent.
    """


_ClientListGeoLocationsResponseTypeDef = TypedDict(
    "_ClientListGeoLocationsResponseTypeDef",
    {
        "GeoLocationDetailsList": List[ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef],
        "IsTruncated": bool,
        "NextContinentCode": str,
        "NextCountryCode": str,
        "NextSubdivisionCode": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListGeoLocationsResponseTypeDef(_ClientListGeoLocationsResponseTypeDef):
    """
    - *(dict) --*

      A complex type containing the response information for the request.
      - **GeoLocationDetailsList** *(list) --*

        A complex type that contains one ``GeoLocationDetails`` element for each location that
        Amazon Route 53 supports for geolocation.
        - *(dict) --*

          A complex type that contains the codes and full continent, country, and subdivision names
          for the specified ``geolocation`` code.
          - **ContinentCode** *(string) --*

            The two-letter code for the continent.
    """


_ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
):
    pass


_ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef(
    _ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef
):
    pass


_ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)


class ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef
):
    pass


_ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)


class ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef(
    _ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef
):
    pass


_ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef(
    _ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef
):
    pass


_ClientListHealthChecksResponseHealthChecksTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef,
        "HealthCheckConfig": ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ClientListHealthChecksResponseHealthChecksTypeDef(
    _ClientListHealthChecksResponseHealthChecksTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about one health check that is associated with the
      current AWS account.
      - **Id** *(string) --*

        The identifier that Amazon Route 53assigned to the health check when you created it. When
        you add or update a resource record set, you use this value to specify which health check to
        use. The value can be up to 64 characters long.
    """


_ClientListHealthChecksResponseTypeDef = TypedDict(
    "_ClientListHealthChecksResponseTypeDef",
    {
        "HealthChecks": List[ClientListHealthChecksResponseHealthChecksTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListHealthChecksResponseTypeDef(_ClientListHealthChecksResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to a ``ListHealthChecks`` request.
      - **HealthChecks** *(list) --*

        A complex type that contains one ``HealthCheck`` element for each health check that is
        associated with the current AWS account.
        - *(dict) --*

          A complex type that contains information about one health check that is associated with
          the current AWS account.
          - **Id** *(string) --*

            The identifier that Amazon Route 53assigned to the health check when you created it.
            When you add or update a resource record set, you use this value to specify which health
            check to use. The value can be up to 64 characters long.
    """


_ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef = TypedDict(
    "_ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef(
    _ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef
):
    pass


_ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef = TypedDict(
    "_ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef(
    _ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef
):
    pass


_ClientListHostedZonesByNameResponseHostedZonesTypeDef = TypedDict(
    "_ClientListHostedZonesByNameResponseHostedZonesTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef,
    },
    total=False,
)


class ClientListHostedZonesByNameResponseHostedZonesTypeDef(
    _ClientListHostedZonesByNameResponseHostedZonesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains general information about the hosted zone.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientListHostedZonesByNameResponseTypeDef = TypedDict(
    "_ClientListHostedZonesByNameResponseTypeDef",
    {
        "HostedZones": List[ClientListHostedZonesByNameResponseHostedZonesTypeDef],
        "DNSName": str,
        "HostedZoneId": str,
        "IsTruncated": bool,
        "NextDNSName": str,
        "NextHostedZoneId": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListHostedZonesByNameResponseTypeDef(_ClientListHostedZonesByNameResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **HostedZones** *(list) --*

        A complex type that contains general information about the hosted zone.
        - *(dict) --*

          A complex type that contains general information about the hosted zone.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientListHostedZonesResponseHostedZonesConfigTypeDef = TypedDict(
    "_ClientListHostedZonesResponseHostedZonesConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientListHostedZonesResponseHostedZonesConfigTypeDef(
    _ClientListHostedZonesResponseHostedZonesConfigTypeDef
):
    pass


_ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef = TypedDict(
    "_ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef(
    _ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef
):
    pass


_ClientListHostedZonesResponseHostedZonesTypeDef = TypedDict(
    "_ClientListHostedZonesResponseHostedZonesTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientListHostedZonesResponseHostedZonesConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef,
    },
    total=False,
)


class ClientListHostedZonesResponseHostedZonesTypeDef(
    _ClientListHostedZonesResponseHostedZonesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains general information about the hosted zone.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientListHostedZonesResponseTypeDef = TypedDict(
    "_ClientListHostedZonesResponseTypeDef",
    {
        "HostedZones": List[ClientListHostedZonesResponseHostedZonesTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListHostedZonesResponseTypeDef(_ClientListHostedZonesResponseTypeDef):
    """
    - *(dict) --*

      - **HostedZones** *(list) --*

        A complex type that contains general information about the hosted zone.
        - *(dict) --*

          A complex type that contains general information about the hosted zone.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef = TypedDict(
    "_ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)


class ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef(
    _ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about a configuration for DNS query logging.
      - **Id** *(string) --*

        The ID for a configuration for DNS query logging.
    """


_ClientListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "_ClientListQueryLoggingConfigsResponseTypeDef",
    {
        "QueryLoggingConfigs": List[
            ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListQueryLoggingConfigsResponseTypeDef(_ClientListQueryLoggingConfigsResponseTypeDef):
    """
    - *(dict) --*

      - **QueryLoggingConfigs** *(list) --*

        An array that contains one `QueryLoggingConfig
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html>`__
        element for each configuration for DNS query logging that is associated with the current AWS
        account.
        - *(dict) --*

          A complex type that contains information about a configuration for DNS query logging.
          - **Id** *(string) --*

            The ID for a configuration for DNS query logging.
    """


_ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef = TypedDict(
    "_ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef",
    {"HostedZoneId": str, "DNSName": str, "EvaluateTargetHealth": bool},
    total=False,
)


class ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef(
    _ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef
):
    pass


_ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef = TypedDict(
    "_ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef",
    {"ContinentCode": str, "CountryCode": str, "SubdivisionCode": str},
    total=False,
)


class ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef(
    _ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef
):
    pass


_ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef = TypedDict(
    "_ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef",
    {"Value": str},
    total=False,
)


class ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef(
    _ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef
):
    pass


_ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef = TypedDict(
    "_ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "SetIdentifier": str,
        "Weight": int,
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-north-1",
            "cn-northwest-1",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
        ],
        "GeoLocation": ClientListResourceRecordSetsResponseResourceRecordSetsGeoLocationTypeDef,
        "Failover": Literal["PRIMARY", "SECONDARY"],
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List[
            ClientListResourceRecordSetsResponseResourceRecordSetsResourceRecordsTypeDef
        ],
        "AliasTarget": ClientListResourceRecordSetsResponseResourceRecordSetsAliasTargetTypeDef,
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)


class ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef(
    _ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef
):
    """
    - *(dict) --*

      Information about the resource record set to create or delete.
      - **Name** *(string) --*

        For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create,
        update, or delete. For ``ListResourceRecordSets`` responses, the name of a record in the
        specified hosted zone.

          **ChangeResourceRecordSets Only**
    """


_ClientListResourceRecordSetsResponseTypeDef = TypedDict(
    "_ClientListResourceRecordSetsResponseTypeDef",
    {
        "ResourceRecordSets": List[ClientListResourceRecordSetsResponseResourceRecordSetsTypeDef],
        "IsTruncated": bool,
        "NextRecordName": str,
        "NextRecordType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "NextRecordIdentifier": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListResourceRecordSetsResponseTypeDef(_ClientListResourceRecordSetsResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains list information for the resource record set.
      - **ResourceRecordSets** *(list) --*

        Information about multiple resource record sets.
        - *(dict) --*

          Information about the resource record set to create or delete.
          - **Name** *(string) --*

            For ``ChangeResourceRecordSets`` requests, the name of the record that you want to
            create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a
            record in the specified hosted zone.

              **ChangeResourceRecordSets Only**
    """


_ClientListReusableDelegationSetsResponseDelegationSetsTypeDef = TypedDict(
    "_ClientListReusableDelegationSetsResponseDelegationSetsTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientListReusableDelegationSetsResponseDelegationSetsTypeDef(
    _ClientListReusableDelegationSetsResponseDelegationSetsTypeDef
):
    """
    - *(dict) --*

      A complex type that lists the name servers in a delegation set, as well as the
      ``CallerReference`` and the ``ID`` for the delegation set.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigns to a reusable delegation set.
    """


_ClientListReusableDelegationSetsResponseTypeDef = TypedDict(
    "_ClientListReusableDelegationSetsResponseTypeDef",
    {
        "DelegationSets": List[ClientListReusableDelegationSetsResponseDelegationSetsTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListReusableDelegationSetsResponseTypeDef(
    _ClientListReusableDelegationSetsResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about the reusable delegation sets that are
      associated with the current AWS account.
      - **DelegationSets** *(list) --*

        A complex type that contains one ``DelegationSet`` element for each reusable delegation set
        that was created by the current AWS account.
        - *(dict) --*

          A complex type that lists the name servers in a delegation set, as well as the
          ``CallerReference`` and the ``ID`` for the delegation set.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigns to a reusable delegation set.
    """


_ClientListTagsForResourceResponseResourceTagSetTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseResourceTagSetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseResourceTagSetTagsTypeDef(
    _ClientListTagsForResourceResponseResourceTagSetTagsTypeDef
):
    pass


_ClientListTagsForResourceResponseResourceTagSetTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseResourceTagSetTypeDef",
    {
        "ResourceType": Literal["healthcheck", "hostedzone"],
        "ResourceId": str,
        "Tags": List[ClientListTagsForResourceResponseResourceTagSetTagsTypeDef],
    },
    total=False,
)


class ClientListTagsForResourceResponseResourceTagSetTypeDef(
    _ClientListTagsForResourceResponseResourceTagSetTypeDef
):
    """
    - **ResourceTagSet** *(dict) --*

      A ``ResourceTagSet`` containing tags associated with the specified resource.
      - **ResourceType** *(string) --*

        The type of the resource.
        * The resource type for health checks is ``healthcheck`` .
        * The resource type for hosted zones is ``hostedzone`` .
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"ResourceTagSet": ClientListTagsForResourceResponseResourceTagSetTypeDef},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about the health checks or hosted zones for which you
      want to list tags.
      - **ResourceTagSet** *(dict) --*

        A ``ResourceTagSet`` containing tags associated with the specified resource.
        - **ResourceType** *(string) --*

          The type of the resource.
          * The resource type for health checks is ``healthcheck`` .
          * The resource type for hosted zones is ``hostedzone`` .
    """


_ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef = TypedDict(
    "_ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef(
    _ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef
):
    pass


_ClientListTagsForResourcesResponseResourceTagSetsTypeDef = TypedDict(
    "_ClientListTagsForResourcesResponseResourceTagSetsTypeDef",
    {
        "ResourceType": Literal["healthcheck", "hostedzone"],
        "ResourceId": str,
        "Tags": List[ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef],
    },
    total=False,
)


class ClientListTagsForResourcesResponseResourceTagSetsTypeDef(
    _ClientListTagsForResourcesResponseResourceTagSetsTypeDef
):
    """
    - *(dict) --*

      A complex type containing a resource and its associated tags.
      - **ResourceType** *(string) --*

        The type of the resource.
        * The resource type for health checks is ``healthcheck`` .
        * The resource type for hosted zones is ``hostedzone`` .
    """


_ClientListTagsForResourcesResponseTypeDef = TypedDict(
    "_ClientListTagsForResourcesResponseTypeDef",
    {"ResourceTagSets": List[ClientListTagsForResourcesResponseResourceTagSetsTypeDef]},
    total=False,
)


class ClientListTagsForResourcesResponseTypeDef(_ClientListTagsForResourcesResponseTypeDef):
    """
    - *(dict) --*

      A complex type containing tags for the specified resources.
      - **ResourceTagSets** *(list) --*

        A list of ``ResourceTagSet`` s containing tags associated with the specified resources.
        - *(dict) --*

          A complex type containing a resource and its associated tags.
          - **ResourceType** *(string) --*

            The type of the resource.
            * The resource type for health checks is ``healthcheck`` .
            * The resource type for hosted zones is ``hostedzone`` .
    """


_ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef = TypedDict(
    "_ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "LatestVersion": int,
        "TrafficPolicyCount": int,
    },
    total=False,
)


class ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef(
    _ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about the latest version of one traffic policy that
      is associated with the current AWS account.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the traffic policy when you created it.
    """


_ClientListTrafficPoliciesResponseTypeDef = TypedDict(
    "_ClientListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicySummaries": List[
            ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef
        ],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPoliciesResponseTypeDef(_ClientListTrafficPoliciesResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **TrafficPolicySummaries** *(list) --*

        A list that contains one ``TrafficPolicySummary`` element for each traffic policy that was
        created by the current AWS account.
        - *(dict) --*

          A complex type that contains information about the latest version of one traffic policy
          that is associated with the current AWS account.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigned to the traffic policy when you created it.
    """


_ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)


class ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef(
    _ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains settings for the new traffic policy instance.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef
        ],
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef(
    _ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **TrafficPolicyInstances** *(list) --*

        A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance
        that matches the elements in the request.
        - *(dict) --*

          A complex type that contains settings for the new traffic policy instance.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)


class ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef(
    _ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains settings for the new traffic policy instance.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef
        ],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesByPolicyResponseTypeDef(
    _ClientListTrafficPolicyInstancesByPolicyResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **TrafficPolicyInstances** *(list) --*

        A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance
        that matches the elements in the request.
        - *(dict) --*

          A complex type that contains settings for the new traffic policy instance.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)


class ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef(
    _ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains settings for the new traffic policy instance.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef
        ],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesResponseTypeDef(
    _ClientListTrafficPolicyInstancesResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **TrafficPolicyInstances** *(list) --*

        A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance
        that matches the elements in the request.
        - *(dict) --*

          A complex type that contains settings for the new traffic policy instance.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef = TypedDict(
    "_ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef(
    _ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains settings for a traffic policy.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientListTrafficPolicyVersionsResponseTypeDef = TypedDict(
    "_ClientListTrafficPolicyVersionsResponseTypeDef",
    {
        "TrafficPolicies": List[ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPolicyVersionsResponseTypeDef(
    _ClientListTrafficPolicyVersionsResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **TrafficPolicies** *(list) --*

        A list that contains one ``TrafficPolicy`` element for each traffic policy version that is
        associated with the specified traffic policy.
        - *(dict) --*

          A complex type that contains settings for a traffic policy.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef = TypedDict(
    "_ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef(
    _ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef
):
    pass


_ClientListVpcAssociationAuthorizationsResponseTypeDef = TypedDict(
    "_ClientListVpcAssociationAuthorizationsResponseTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": str,
        "VPCs": List[ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef],
    },
    total=False,
)


class ClientListVpcAssociationAuthorizationsResponseTypeDef(
    _ClientListVpcAssociationAuthorizationsResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **HostedZoneId** *(string) --*

        The ID of the hosted zone that you can associate the listed VPCs with.
    """


_ClientTestDnsAnswerResponseTypeDef = TypedDict(
    "_ClientTestDnsAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
    },
    total=False,
)


class ClientTestDnsAnswerResponseTypeDef(_ClientTestDnsAnswerResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to a ``TestDNSAnswer`` request.
      - **Nameserver** *(string) --*

        The Amazon Route 53 name server used to respond to the request.
    """


_RequiredClientUpdateHealthCheckAlarmIdentifierTypeDef = TypedDict(
    "_RequiredClientUpdateHealthCheckAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ]
    },
)
_OptionalClientUpdateHealthCheckAlarmIdentifierTypeDef = TypedDict(
    "_OptionalClientUpdateHealthCheckAlarmIdentifierTypeDef", {"Name": str}, total=False
)


class ClientUpdateHealthCheckAlarmIdentifierTypeDef(
    _RequiredClientUpdateHealthCheckAlarmIdentifierTypeDef,
    _OptionalClientUpdateHealthCheckAlarmIdentifierTypeDef,
):
    """
    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
    checkers to use to determine whether the specified health check is healthy.
    - **Region** *(string) --***[REQUIRED]**

      For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether
      this health check is healthy, the region that the alarm was created in.
      For the current list of CloudWatch regions, see `Amazon CloudWatch
      <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and
      Endpoints* chapter of the *Amazon Web Services General Reference* .
    """


_ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
):
    pass


_ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef
):
    pass


_ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef
):
    pass


_ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef
):
    pass


_ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef
):
    pass


_ClientUpdateHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckTypeDef
):
    """
    - **HealthCheck** *(dict) --*

      A complex type that contains the response to an ``UpdateHealthCheck`` request.
      - **Id** *(string) --*

        The identifier that Amazon Route 53assigned to the health check when you created it. When
        you add or update a resource record set, you use this value to specify which health check to
        use. The value can be up to 64 characters long.
    """


_ClientUpdateHealthCheckResponseTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseTypeDef",
    {"HealthCheck": ClientUpdateHealthCheckResponseHealthCheckTypeDef},
    total=False,
)


class ClientUpdateHealthCheckResponseTypeDef(_ClientUpdateHealthCheckResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to the ``UpdateHealthCheck`` request.
      - **HealthCheck** *(dict) --*

        A complex type that contains the response to an ``UpdateHealthCheck`` request.
        - **Id** *(string) --*

          The identifier that Amazon Route 53assigned to the health check when you created it. When
          you add or update a resource record set, you use this value to specify which health check
          to use. The value can be up to 64 characters long.
    """


_ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef = TypedDict(
    "_ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef(
    _ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef
):
    pass


_ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "_ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef(
    _ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef
):
    pass


_ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef = TypedDict(
    "_ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)


class ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef(
    _ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef
):
    """
    - **HostedZone** *(dict) --*

      A complex type that contains the response to the ``UpdateHostedZoneComment`` request.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientUpdateHostedZoneCommentResponseTypeDef = TypedDict(
    "_ClientUpdateHostedZoneCommentResponseTypeDef",
    {"HostedZone": ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef},
    total=False,
)


class ClientUpdateHostedZoneCommentResponseTypeDef(_ClientUpdateHostedZoneCommentResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to the ``UpdateHostedZoneComment`` request.
      - **HostedZone** *(dict) --*

        A complex type that contains the response to the ``UpdateHostedZoneComment`` request.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef = TypedDict(
    "_ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef(
    _ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef
):
    """
    - **TrafficPolicy** *(dict) --*

      A complex type that contains settings for the specified traffic policy.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientUpdateTrafficPolicyCommentResponseTypeDef = TypedDict(
    "_ClientUpdateTrafficPolicyCommentResponseTypeDef",
    {"TrafficPolicy": ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef},
    total=False,
)


class ClientUpdateTrafficPolicyCommentResponseTypeDef(
    _ClientUpdateTrafficPolicyCommentResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the traffic policy.
      - **TrafficPolicy** *(dict) --*

        A complex type that contains settings for the specified traffic policy.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to a traffic policy when you created it.
    """


_ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "_ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
    },
    total=False,
)


class ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef(
    _ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
):
    """
    - **TrafficPolicyInstance** *(dict) --*

      A complex type that contains settings for the updated traffic policy instance.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ClientUpdateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "_ClientUpdateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
    },
    total=False,
)


class ClientUpdateTrafficPolicyInstanceResponseTypeDef(
    _ClientUpdateTrafficPolicyInstanceResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about the resource record sets that Amazon Route 53
      created based on a specified traffic policy.
      - **TrafficPolicyInstance** *(dict) --*

        A complex type that contains settings for the updated traffic policy instance.
        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the new traffic policy instance.
    """


_ListHealthChecksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHealthChecksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHealthChecksPaginatePaginationConfigTypeDef(
    _ListHealthChecksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
):
    pass


_ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
        "Dimensions": List[
            ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef
):
    pass


_ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
        ],
        "Name": str,
    },
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef
):
    pass


_ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ],
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
    },
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef
):
    pass


_ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef
):
    pass


_ListHealthChecksPaginateResponseHealthChecksTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef,
        "HealthCheckConfig": ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about one health check that is associated with the
      current AWS account.
      - **Id** *(string) --*

        The identifier that Amazon Route 53assigned to the health check when you created it. When
        you add or update a resource record set, you use this value to specify which health check to
        use. The value can be up to 64 characters long.
    """


_ListHealthChecksPaginateResponseTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseTypeDef",
    {
        "HealthChecks": List[ListHealthChecksPaginateResponseHealthChecksTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
        "NextToken": str,
    },
    total=False,
)


class ListHealthChecksPaginateResponseTypeDef(_ListHealthChecksPaginateResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains the response to a ``ListHealthChecks`` request.
      - **HealthChecks** *(list) --*

        A complex type that contains one ``HealthCheck`` element for each health check that is
        associated with the current AWS account.
        - *(dict) --*

          A complex type that contains information about one health check that is associated with
          the current AWS account.
          - **Id** *(string) --*

            The identifier that Amazon Route 53assigned to the health check when you created it.
            When you add or update a resource record set, you use this value to specify which health
            check to use. The value can be up to 64 characters long.
    """


_ListHostedZonesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHostedZonesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHostedZonesPaginatePaginationConfigTypeDef(
    _ListHostedZonesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHostedZonesPaginateResponseHostedZonesConfigTypeDef = TypedDict(
    "_ListHostedZonesPaginateResponseHostedZonesConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ListHostedZonesPaginateResponseHostedZonesConfigTypeDef(
    _ListHostedZonesPaginateResponseHostedZonesConfigTypeDef
):
    pass


_ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef = TypedDict(
    "_ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef(
    _ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef
):
    pass


_ListHostedZonesPaginateResponseHostedZonesTypeDef = TypedDict(
    "_ListHostedZonesPaginateResponseHostedZonesTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ListHostedZonesPaginateResponseHostedZonesConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef,
    },
    total=False,
)


class ListHostedZonesPaginateResponseHostedZonesTypeDef(
    _ListHostedZonesPaginateResponseHostedZonesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains general information about the hosted zone.
      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ListHostedZonesPaginateResponseTypeDef = TypedDict(
    "_ListHostedZonesPaginateResponseTypeDef",
    {
        "HostedZones": List[ListHostedZonesPaginateResponseHostedZonesTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
        "NextToken": str,
    },
    total=False,
)


class ListHostedZonesPaginateResponseTypeDef(_ListHostedZonesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **HostedZones** *(list) --*

        A complex type that contains general information about the hosted zone.
        - *(dict) --*

          A complex type that contains general information about the hosted zone.
          - **Id** *(string) --*

            The ID that Amazon Route 53 assigned to the hosted zone when you created it.
    """


_ListQueryLoggingConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQueryLoggingConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQueryLoggingConfigsPaginatePaginationConfigTypeDef(
    _ListQueryLoggingConfigsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef = TypedDict(
    "_ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)


class ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef(
    _ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about a configuration for DNS query logging.
      - **Id** *(string) --*

        The ID for a configuration for DNS query logging.
    """


_ListQueryLoggingConfigsPaginateResponseTypeDef = TypedDict(
    "_ListQueryLoggingConfigsPaginateResponseTypeDef",
    {
        "QueryLoggingConfigs": List[
            ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef
        ]
    },
    total=False,
)


class ListQueryLoggingConfigsPaginateResponseTypeDef(
    _ListQueryLoggingConfigsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **QueryLoggingConfigs** *(list) --*

        An array that contains one `QueryLoggingConfig
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html>`__
        element for each configuration for DNS query logging that is associated with the current AWS
        account.
        - *(dict) --*

          A complex type that contains information about a configuration for DNS query logging.
          - **Id** *(string) --*

            The ID for a configuration for DNS query logging.
    """


_ListResourceRecordSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceRecordSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceRecordSetsPaginatePaginationConfigTypeDef(
    _ListResourceRecordSetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourceRecordSetsPaginateResponseResourceRecordSetsAliasTargetTypeDef = TypedDict(
    "_ListResourceRecordSetsPaginateResponseResourceRecordSetsAliasTargetTypeDef",
    {"HostedZoneId": str, "DNSName": str, "EvaluateTargetHealth": bool},
    total=False,
)


class ListResourceRecordSetsPaginateResponseResourceRecordSetsAliasTargetTypeDef(
    _ListResourceRecordSetsPaginateResponseResourceRecordSetsAliasTargetTypeDef
):
    pass


_ListResourceRecordSetsPaginateResponseResourceRecordSetsGeoLocationTypeDef = TypedDict(
    "_ListResourceRecordSetsPaginateResponseResourceRecordSetsGeoLocationTypeDef",
    {"ContinentCode": str, "CountryCode": str, "SubdivisionCode": str},
    total=False,
)


class ListResourceRecordSetsPaginateResponseResourceRecordSetsGeoLocationTypeDef(
    _ListResourceRecordSetsPaginateResponseResourceRecordSetsGeoLocationTypeDef
):
    pass


_ListResourceRecordSetsPaginateResponseResourceRecordSetsResourceRecordsTypeDef = TypedDict(
    "_ListResourceRecordSetsPaginateResponseResourceRecordSetsResourceRecordsTypeDef",
    {"Value": str},
    total=False,
)


class ListResourceRecordSetsPaginateResponseResourceRecordSetsResourceRecordsTypeDef(
    _ListResourceRecordSetsPaginateResponseResourceRecordSetsResourceRecordsTypeDef
):
    pass


_ListResourceRecordSetsPaginateResponseResourceRecordSetsTypeDef = TypedDict(
    "_ListResourceRecordSetsPaginateResponseResourceRecordSetsTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        "SetIdentifier": str,
        "Weight": int,
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-north-1",
            "cn-northwest-1",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
        ],
        "GeoLocation": ListResourceRecordSetsPaginateResponseResourceRecordSetsGeoLocationTypeDef,
        "Failover": Literal["PRIMARY", "SECONDARY"],
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List[
            ListResourceRecordSetsPaginateResponseResourceRecordSetsResourceRecordsTypeDef
        ],
        "AliasTarget": ListResourceRecordSetsPaginateResponseResourceRecordSetsAliasTargetTypeDef,
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)


class ListResourceRecordSetsPaginateResponseResourceRecordSetsTypeDef(
    _ListResourceRecordSetsPaginateResponseResourceRecordSetsTypeDef
):
    """
    - *(dict) --*

      Information about the resource record set to create or delete.
      - **Name** *(string) --*

        For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create,
        update, or delete. For ``ListResourceRecordSets`` responses, the name of a record in the
        specified hosted zone.

          **ChangeResourceRecordSets Only**
    """


_ListResourceRecordSetsPaginateResponseTypeDef = TypedDict(
    "_ListResourceRecordSetsPaginateResponseTypeDef",
    {
        "ResourceRecordSets": List[ListResourceRecordSetsPaginateResponseResourceRecordSetsTypeDef],
        "IsTruncated": bool,
        "MaxItems": str,
        "NextToken": str,
    },
    total=False,
)


class ListResourceRecordSetsPaginateResponseTypeDef(_ListResourceRecordSetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      A complex type that contains list information for the resource record set.
      - **ResourceRecordSets** *(list) --*

        Information about multiple resource record sets.
        - *(dict) --*

          Information about the resource record set to create or delete.
          - **Name** *(string) --*

            For ``ChangeResourceRecordSets`` requests, the name of the record that you want to
            create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a
            record in the specified hosted zone.

              **ChangeResourceRecordSets Only**
    """


_ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef(
    _ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef = TypedDict(
    "_ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
        ],
        "VPCId": str,
    },
    total=False,
)


class ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef(
    _ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef
):
    pass


_ListVPCAssociationAuthorizationsPaginateResponseTypeDef = TypedDict(
    "_ListVPCAssociationAuthorizationsPaginateResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPCs": List[ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef],
    },
    total=False,
)


class ListVPCAssociationAuthorizationsPaginateResponseTypeDef(
    _ListVPCAssociationAuthorizationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      A complex type that contains the response information for the request.
      - **HostedZoneId** *(string) --*

        The ID of the hosted zone that you can associate the listed VPCs with.
    """


_ResourceRecordSetsChangedWaitWaiterConfigTypeDef = TypedDict(
    "_ResourceRecordSetsChangedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ResourceRecordSetsChangedWaitWaiterConfigTypeDef(
    _ResourceRecordSetsChangedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """
