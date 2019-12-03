"Main interface for elb service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "AnyInstanceInServiceWaitInstancesTypeDef",
    "AnyInstanceInServiceWaitWaiterConfigTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientApplySecurityGroupsToLoadBalancerResponseTypeDef",
    "ClientAttachLoadBalancerToSubnetsResponseTypeDef",
    "ClientConfigureHealthCheckHealthCheckTypeDef",
    "ClientConfigureHealthCheckResponseHealthCheckTypeDef",
    "ClientConfigureHealthCheckResponseTypeDef",
    "ClientCreateLoadBalancerListenersListenersTypeDef",
    "ClientCreateLoadBalancerListenersTypeDef",
    "ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef",
    "ClientCreateLoadBalancerResponseTypeDef",
    "ClientCreateLoadBalancerTagsTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerResponseTypeDef",
    "ClientDescribeAccountLimitsResponseLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeInstanceHealthInstancesTypeDef",
    "ClientDescribeInstanceHealthResponseInstanceStatesTypeDef",
    "ClientDescribeInstanceHealthResponseTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponseTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDetachLoadBalancerFromSubnetsResponseTypeDef",
    "ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef",
    "ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    "ClientRegisterInstancesWithLoadBalancerInstancesTypeDef",
    "ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef",
    "ClientRegisterInstancesWithLoadBalancerResponseTypeDef",
    "ClientRemoveTagsTagsTypeDef",
    "DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    "DescribeAccountLimitsPaginateResponseLimitsTypeDef",
    "DescribeAccountLimitsPaginateResponseTypeDef",
    "DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef",
    "DescribeLoadBalancersPaginateResponseTypeDef",
    "InstanceDeregisteredWaitInstancesTypeDef",
    "InstanceDeregisteredWaitWaiterConfigTypeDef",
    "InstanceInServiceWaitInstancesTypeDef",
    "InstanceInServiceWaitWaiterConfigTypeDef",
)


_AnyInstanceInServiceWaitInstancesTypeDef = TypedDict(
    "_AnyInstanceInServiceWaitInstancesTypeDef", {"InstanceId": str}, total=False
)


class AnyInstanceInServiceWaitInstancesTypeDef(_AnyInstanceInServiceWaitInstancesTypeDef):
    """
    - *(dict) --*

      The ID of an EC2 instance.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_AnyInstanceInServiceWaitWaiterConfigTypeDef = TypedDict(
    "_AnyInstanceInServiceWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class AnyInstanceInServiceWaitWaiterConfigTypeDef(_AnyInstanceInServiceWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
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


_ClientApplySecurityGroupsToLoadBalancerResponseTypeDef = TypedDict(
    "_ClientApplySecurityGroupsToLoadBalancerResponseTypeDef",
    {"SecurityGroups": List[str]},
    total=False,
)


class ClientApplySecurityGroupsToLoadBalancerResponseTypeDef(
    _ClientApplySecurityGroupsToLoadBalancerResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of ApplySecurityGroupsToLoadBalancer.
      - **SecurityGroups** *(list) --*

        The IDs of the security groups associated with the load balancer.
        - *(string) --*
    """


_ClientAttachLoadBalancerToSubnetsResponseTypeDef = TypedDict(
    "_ClientAttachLoadBalancerToSubnetsResponseTypeDef", {"Subnets": List[str]}, total=False
)


class ClientAttachLoadBalancerToSubnetsResponseTypeDef(
    _ClientAttachLoadBalancerToSubnetsResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of AttachLoadBalancerToSubnets.
      - **Subnets** *(list) --*

        The IDs of the subnets attached to the load balancer.
        - *(string) --*
    """


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
    """
    The configuration information.
    - **Target** *(string) --***[REQUIRED]**

      The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of
      valid ports is one (1) through 65535.
      TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a
      health check simply attempts to open a TCP connection to the instance on the specified port.
      Failure to connect within the configured timeout is considered unhealthy.
      SSL is also specified as SSL: port pair, for example, SSL:5000.
      For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
      HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this case, a
      HTTP GET request is issued to the instance on the given port and path. Any answer other than
      "200 OK" within the timeout period is considered unhealthy.
      The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.
    """


_ClientConfigureHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "_ClientConfigureHealthCheckResponseHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)


class ClientConfigureHealthCheckResponseHealthCheckTypeDef(
    _ClientConfigureHealthCheckResponseHealthCheckTypeDef
):
    """
    - **HealthCheck** *(dict) --*

      The updated health check.
      - **Target** *(string) --*

        The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of
        valid ports is one (1) through 65535.
        TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a
        health check simply attempts to open a TCP connection to the instance on the specified port.
        Failure to connect within the configured timeout is considered unhealthy.
        SSL is also specified as SSL: port pair, for example, SSL:5000.
        For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
        HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this case,
        a HTTP GET request is issued to the instance on the given port and path. Any answer other
        than "200 OK" within the timeout period is considered unhealthy.
        The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.
    """


_ClientConfigureHealthCheckResponseTypeDef = TypedDict(
    "_ClientConfigureHealthCheckResponseTypeDef",
    {"HealthCheck": ClientConfigureHealthCheckResponseHealthCheckTypeDef},
    total=False,
)


class ClientConfigureHealthCheckResponseTypeDef(_ClientConfigureHealthCheckResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of ConfigureHealthCheck.
      - **HealthCheck** *(dict) --*

        The updated health check.
        - **Target** *(string) --*

          The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of
          valid ports is one (1) through 65535.
          TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a
          health check simply attempts to open a TCP connection to the instance on the specified
          port. Failure to connect within the configured timeout is considered unhealthy.
          SSL is also specified as SSL: port pair, for example, SSL:5000.
          For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
          HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
          case, a HTTP GET request is issued to the instance on the given port and path. Any answer
          other than "200 OK" within the timeout period is considered unhealthy.
          The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.
    """


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
    """
    - *(dict) --*

      Information about a listener.
      For information about the protocols and the ports supported by Elastic Load Balancing, see
      `Listeners for Your Classic Load Balancer
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html>`__
      in the *Classic Load Balancers Guide* .
      - **Protocol** *(string) --***[REQUIRED]**

        The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
    """


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
    """
    - *(dict) --*

      Information about a listener.
      For information about the protocols and the ports supported by Elastic Load Balancing, see
      `Listeners for Your Classic Load Balancer
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html>`__
      in the *Classic Load Balancers Guide* .
      - **Protocol** *(string) --***[REQUIRED]**

        The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
    """


_ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef = TypedDict(
    "_ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef",
    {"AttributeName": str, "AttributeValue": str},
    total=False,
)


class ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef(
    _ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef
):
    """
    - *(dict) --*

      Information about a policy attribute.
      - **AttributeName** *(string) --*

        The name of the attribute.
    """


_ClientCreateLoadBalancerResponseTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseTypeDef", {"DNSName": str}, total=False
)


class ClientCreateLoadBalancerResponseTypeDef(_ClientCreateLoadBalancerResponseTypeDef):
    """
    - *(dict) --*

      Contains the output for CreateLoadBalancer.
      - **DNSName** *(string) --*

        The DNS name of the load balancer.
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


_ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef = TypedDict(
    "_ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef", {"InstanceId": str}, total=False
)


class ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef(
    _ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef
):
    """
    - *(dict) --*

      The ID of an EC2 instance.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef = TypedDict(
    "_ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef(
    _ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef
):
    """
    - *(dict) --*

      The ID of an EC2 instance.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_ClientDeregisterInstancesFromLoadBalancerResponseTypeDef = TypedDict(
    "_ClientDeregisterInstancesFromLoadBalancerResponseTypeDef",
    {"Instances": List[ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef]},
    total=False,
)


class ClientDeregisterInstancesFromLoadBalancerResponseTypeDef(
    _ClientDeregisterInstancesFromLoadBalancerResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of DeregisterInstancesFromLoadBalancer.
      - **Instances** *(list) --*

        The remaining instances registered with the load balancer.
        - *(dict) --*

          The ID of an EC2 instance.
          - **InstanceId** *(string) --*

            The instance ID.
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
        * classic-listeners
        * classic-load-balancers
        * classic-registered-instances
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
            * classic-listeners
            * classic-load-balancers
            * classic-registered-instances
    """


_ClientDescribeInstanceHealthInstancesTypeDef = TypedDict(
    "_ClientDescribeInstanceHealthInstancesTypeDef", {"InstanceId": str}, total=False
)


class ClientDescribeInstanceHealthInstancesTypeDef(_ClientDescribeInstanceHealthInstancesTypeDef):
    """
    - *(dict) --*

      The ID of an EC2 instance.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_ClientDescribeInstanceHealthResponseInstanceStatesTypeDef = TypedDict(
    "_ClientDescribeInstanceHealthResponseInstanceStatesTypeDef",
    {"InstanceId": str, "State": str, "ReasonCode": str, "Description": str},
    total=False,
)


class ClientDescribeInstanceHealthResponseInstanceStatesTypeDef(
    _ClientDescribeInstanceHealthResponseInstanceStatesTypeDef
):
    """
    - *(dict) --*

      Information about the state of an EC2 instance.
      - **InstanceId** *(string) --*

        The ID of the instance.
    """


_ClientDescribeInstanceHealthResponseTypeDef = TypedDict(
    "_ClientDescribeInstanceHealthResponseTypeDef",
    {"InstanceStates": List[ClientDescribeInstanceHealthResponseInstanceStatesTypeDef]},
    total=False,
)


class ClientDescribeInstanceHealthResponseTypeDef(_ClientDescribeInstanceHealthResponseTypeDef):
    """
    - *(dict) --*

      Contains the output for DescribeInstanceHealth.
      - **InstanceStates** *(list) --*

        Information about the health of the instances.
        - *(dict) --*

          Information about the state of an EC2 instance.
          - **InstanceId** *(string) --*

            The ID of the instance.
    """


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef
):
    pass


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
):
    pass


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef
):
    pass


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef
):
    pass


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef
):
    """
    - **CrossZoneLoadBalancing** *(dict) --*

      If enabled, the load balancer routes the request traffic evenly across all instances
      regardless of the Availability Zones.
      For more information, see `Configure Cross-Zone Load Balancing
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
      in the *Classic Load Balancers Guide* .
      - **Enabled** *(boolean) --*

        Specifies whether cross-zone load balancing is enabled for the load balancer.
    """


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
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


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef
):
    """
    - **LoadBalancerAttributes** *(dict) --*

      Information about the load balancer attributes.
      - **CrossZoneLoadBalancing** *(dict) --*

        If enabled, the load balancer routes the request traffic evenly across all instances
        regardless of the Availability Zones.
        For more information, see `Configure Cross-Zone Load Balancing
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
        in the *Classic Load Balancers Guide* .
        - **Enabled** *(boolean) --*

          Specifies whether cross-zone load balancing is enabled for the load balancer.
    """


_ClientDescribeLoadBalancerAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseTypeDef",
    {
        "LoadBalancerAttributes": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef
    },
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of DescribeLoadBalancerAttributes.
      - **LoadBalancerAttributes** *(dict) --*

        Information about the load balancer attributes.
        - **CrossZoneLoadBalancing** *(dict) --*

          If enabled, the load balancer routes the request traffic evenly across all instances
          regardless of the Availability Zones.
          For more information, see `Configure Cross-Zone Load Balancing
          <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
          in the *Classic Load Balancers Guide* .
          - **Enabled** *(boolean) --*

            Specifies whether cross-zone load balancing is enabled for the load balancer.
    """


_ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef",
    {"AttributeName": str, "AttributeValue": str},
    total=False,
)


class ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef(
    _ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef
):
    pass


_ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef",
    {
        "PolicyName": str,
        "PolicyTypeName": str,
        "PolicyAttributeDescriptions": List[
            ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef(
    _ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef
):
    """
    - *(dict) --*

      Information about a policy.
      - **PolicyName** *(string) --*

        The name of the policy.
    """


_ClientDescribeLoadBalancerPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPoliciesResponseTypeDef",
    {
        "PolicyDescriptions": List[
            ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeLoadBalancerPoliciesResponseTypeDef(
    _ClientDescribeLoadBalancerPoliciesResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of DescribeLoadBalancerPolicies.
      - **PolicyDescriptions** *(list) --*

        Information about the policies.
        - *(dict) --*

          Information about a policy.
          - **PolicyName** *(string) --*

            The name of the policy.
    """


_ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef",
    {
        "AttributeName": str,
        "AttributeType": str,
        "Description": str,
        "DefaultValue": str,
        "Cardinality": str,
    },
    total=False,
)


class ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef(
    _ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef
):
    pass


_ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef",
    {
        "PolicyTypeName": str,
        "Description": str,
        "PolicyAttributeTypeDescriptions": List[
            ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef(
    _ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef
):
    """
    - *(dict) --*

      Information about a policy type.
      - **PolicyTypeName** *(string) --*

        The name of the policy type.
    """


_ClientDescribeLoadBalancerPolicyTypesResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPolicyTypesResponseTypeDef",
    {
        "PolicyTypeDescriptions": List[
            ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeLoadBalancerPolicyTypesResponseTypeDef(
    _ClientDescribeLoadBalancerPolicyTypesResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of DescribeLoadBalancerPolicyTypes.
      - **PolicyTypeDescriptions** *(list) --*

        Information about the policy types.
        - *(dict) --*

          Information about a policy type.
          - **PolicyTypeName** *(string) --*

            The name of the policy type.
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    {"InstancePort": int, "PolicyNames": List[str]},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    {
        "Listener": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef,
        "PolicyNames": List[str],
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieName": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieExpirationPeriod": int},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef",
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


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    {"OwnerAlias": str, "GroupName": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef
):
    pass


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef",
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


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef
):
    """
    - *(dict) --*

      Information about a load balancer.
      - **LoadBalancerName** *(string) --*

        The name of the load balancer.
    """


_ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseTypeDef(_ClientDescribeLoadBalancersResponseTypeDef):
    """
    - *(dict) --*

      Contains the parameters for DescribeLoadBalancers.
      - **LoadBalancerDescriptions** *(list) --*

        Information about the load balancers.
        - *(dict) --*

          Information about a load balancer.
          - **LoadBalancerName** *(string) --*

            The name of the load balancer.
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
    {"LoadBalancerName": str, "Tags": List[ClientDescribeTagsResponseTagDescriptionsTagsTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTagDescriptionsTypeDef(
    _ClientDescribeTagsResponseTagDescriptionsTypeDef
):
    """
    - *(dict) --*

      The tags associated with a load balancer.
      - **LoadBalancerName** *(string) --*

        The name of the load balancer.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"TagDescriptions": List[ClientDescribeTagsResponseTagDescriptionsTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      Contains the output for DescribeTags.
      - **TagDescriptions** *(list) --*

        Information about the tags.
        - *(dict) --*

          The tags associated with a load balancer.
          - **LoadBalancerName** *(string) --*

            The name of the load balancer.
    """


_ClientDetachLoadBalancerFromSubnetsResponseTypeDef = TypedDict(
    "_ClientDetachLoadBalancerFromSubnetsResponseTypeDef", {"Subnets": List[str]}, total=False
)


class ClientDetachLoadBalancerFromSubnetsResponseTypeDef(
    _ClientDetachLoadBalancerFromSubnetsResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of DetachLoadBalancerFromSubnets.
      - **Subnets** *(list) --*

        The IDs of the remaining subnets for the load balancer.
        - *(string) --*
    """


_ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef = TypedDict(
    "_ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef",
    {"AvailabilityZones": List[str]},
    total=False,
)


class ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef(
    _ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output for DisableAvailabilityZonesForLoadBalancer.
      - **AvailabilityZones** *(list) --*

        The remaining Availability Zones for the load balancer.
        - *(string) --*
    """


_ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef = TypedDict(
    "_ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef",
    {"AvailabilityZones": List[str]},
    total=False,
)


class ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef(
    _ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of EnableAvailabilityZonesForLoadBalancer.
      - **AvailabilityZones** *(list) --*

        The updated list of Availability Zones for the load balancer.
        - *(string) --*
    """


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef
):
    """
    - **CrossZoneLoadBalancing** *(dict) --*

      If enabled, the load balancer routes the request traffic evenly across all instances
      regardless of the Availability Zones.
      For more information, see `Configure Cross-Zone Load Balancing
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
      in the *Classic Load Balancers Guide* .
      - **Enabled** *(boolean) --***[REQUIRED]**

        Specifies whether cross-zone load balancing is enabled for the load balancer.
    """


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef",
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


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef
):
    """
    The attributes for the load balancer.
    - **CrossZoneLoadBalancing** *(dict) --*

      If enabled, the load balancer routes the request traffic evenly across all instances
      regardless of the Availability Zones.
      For more information, see `Configure Cross-Zone Load Balancing
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
      in the *Classic Load Balancers Guide* .
      - **Enabled** *(boolean) --***[REQUIRED]**

        Specifies whether cross-zone load balancing is enabled for the load balancer.
    """


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
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


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef
):
    pass


_ClientModifyLoadBalancerAttributesResponseTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef,
    },
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseTypeDef(
    _ClientModifyLoadBalancerAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of ModifyLoadBalancerAttributes.
      - **LoadBalancerName** *(string) --*

        The name of the load balancer.
    """


_ClientRegisterInstancesWithLoadBalancerInstancesTypeDef = TypedDict(
    "_ClientRegisterInstancesWithLoadBalancerInstancesTypeDef", {"InstanceId": str}, total=False
)


class ClientRegisterInstancesWithLoadBalancerInstancesTypeDef(
    _ClientRegisterInstancesWithLoadBalancerInstancesTypeDef
):
    """
    - *(dict) --*

      The ID of an EC2 instance.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef = TypedDict(
    "_ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef(
    _ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef
):
    """
    - *(dict) --*

      The ID of an EC2 instance.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_ClientRegisterInstancesWithLoadBalancerResponseTypeDef = TypedDict(
    "_ClientRegisterInstancesWithLoadBalancerResponseTypeDef",
    {"Instances": List[ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef]},
    total=False,
)


class ClientRegisterInstancesWithLoadBalancerResponseTypeDef(
    _ClientRegisterInstancesWithLoadBalancerResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of RegisterInstancesWithLoadBalancer.
      - **Instances** *(list) --*

        The updated list of instances for the load balancer.
        - *(dict) --*

          The ID of an EC2 instance.
          - **InstanceId** *(string) --*

            The instance ID.
    """


_ClientRemoveTagsTagsTypeDef = TypedDict("_ClientRemoveTagsTagsTypeDef", {"Key": str}, total=False)


class ClientRemoveTagsTagsTypeDef(_ClientRemoveTagsTagsTypeDef):
    """
    - *(dict) --*

      The key of a tag.
      - **Key** *(string) --*

        The name of the key.
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
        * classic-listeners
        * classic-load-balancers
        * classic-registered-instances
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
            * classic-listeners
            * classic-load-balancers
            * classic-registered-instances
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


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    {"InstancePort": int, "PolicyNames": List[str]},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    {
        "Listener": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef,
        "PolicyNames": List[str],
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieName": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieExpirationPeriod": int},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef",
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


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    {"OwnerAlias": str, "GroupName": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef
):
    pass


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef",
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


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef
):
    """
    - *(dict) --*

      Information about a load balancer.
      - **LoadBalancerName** *(string) --*

        The name of the load balancer.
    """


_DescribeLoadBalancersPaginateResponseTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseTypeDef",
    {
        "LoadBalancerDescriptions": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseTypeDef(_DescribeLoadBalancersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the parameters for DescribeLoadBalancers.
      - **LoadBalancerDescriptions** *(list) --*

        Information about the load balancers.
        - *(dict) --*

          Information about a load balancer.
          - **LoadBalancerName** *(string) --*

            The name of the load balancer.
    """


_InstanceDeregisteredWaitInstancesTypeDef = TypedDict(
    "_InstanceDeregisteredWaitInstancesTypeDef", {"InstanceId": str}, total=False
)


class InstanceDeregisteredWaitInstancesTypeDef(_InstanceDeregisteredWaitInstancesTypeDef):
    """
    - *(dict) --*

      The ID of an EC2 instance.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_InstanceDeregisteredWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceDeregisteredWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class InstanceDeregisteredWaitWaiterConfigTypeDef(_InstanceDeregisteredWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_InstanceInServiceWaitInstancesTypeDef = TypedDict(
    "_InstanceInServiceWaitInstancesTypeDef", {"InstanceId": str}, total=False
)


class InstanceInServiceWaitInstancesTypeDef(_InstanceInServiceWaitInstancesTypeDef):
    """
    - *(dict) --*

      The ID of an EC2 instance.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_InstanceInServiceWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceInServiceWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class InstanceInServiceWaitWaiterConfigTypeDef(_InstanceInServiceWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """
