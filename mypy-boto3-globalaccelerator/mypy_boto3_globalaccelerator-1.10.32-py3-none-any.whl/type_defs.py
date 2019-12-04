"Main interface for globalaccelerator service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientCreateAcceleratorResponseAcceleratorTypeDef",
    "ClientCreateAcceleratorResponseTypeDef",
    "ClientCreateEndpointGroupEndpointConfigurationsTypeDef",
    "ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientCreateEndpointGroupResponseEndpointGroupTypeDef",
    "ClientCreateEndpointGroupResponseTypeDef",
    "ClientCreateListenerPortRangesTypeDef",
    "ClientCreateListenerResponseListenerPortRangesTypeDef",
    "ClientCreateListenerResponseListenerTypeDef",
    "ClientCreateListenerResponseTypeDef",
    "ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    "ClientDescribeAcceleratorAttributesResponseTypeDef",
    "ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientDescribeAcceleratorResponseAcceleratorTypeDef",
    "ClientDescribeAcceleratorResponseTypeDef",
    "ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientDescribeEndpointGroupResponseEndpointGroupTypeDef",
    "ClientDescribeEndpointGroupResponseTypeDef",
    "ClientDescribeListenerResponseListenerPortRangesTypeDef",
    "ClientDescribeListenerResponseListenerTypeDef",
    "ClientDescribeListenerResponseTypeDef",
    "ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef",
    "ClientListAcceleratorsResponseAcceleratorsTypeDef",
    "ClientListAcceleratorsResponseTypeDef",
    "ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef",
    "ClientListEndpointGroupsResponseEndpointGroupsTypeDef",
    "ClientListEndpointGroupsResponseTypeDef",
    "ClientListListenersResponseListenersPortRangesTypeDef",
    "ClientListListenersResponseListenersTypeDef",
    "ClientListListenersResponseTypeDef",
    "ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    "ClientUpdateAcceleratorAttributesResponseTypeDef",
    "ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientUpdateAcceleratorResponseAcceleratorTypeDef",
    "ClientUpdateAcceleratorResponseTypeDef",
    "ClientUpdateEndpointGroupEndpointConfigurationsTypeDef",
    "ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientUpdateEndpointGroupResponseEndpointGroupTypeDef",
    "ClientUpdateEndpointGroupResponseTypeDef",
    "ClientUpdateListenerPortRangesTypeDef",
    "ClientUpdateListenerResponseListenerPortRangesTypeDef",
    "ClientUpdateListenerResponseListenerTypeDef",
    "ClientUpdateListenerResponseTypeDef",
    "ListAcceleratorsPaginatePaginationConfigTypeDef",
    "ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef",
    "ListAcceleratorsPaginateResponseAcceleratorsTypeDef",
    "ListAcceleratorsPaginateResponseTypeDef",
    "ListEndpointGroupsPaginatePaginationConfigTypeDef",
    "ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef",
    "ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef",
    "ListEndpointGroupsPaginateResponseTypeDef",
    "ListListenersPaginatePaginationConfigTypeDef",
    "ListListenersPaginateResponseListenersPortRangesTypeDef",
    "ListListenersPaginateResponseListenersTypeDef",
    "ListListenersPaginateResponseTypeDef",
)


_ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "_ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef(
    _ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef
):
    pass


_ClientCreateAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "_ClientCreateAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientCreateAcceleratorResponseAcceleratorTypeDef(
    _ClientCreateAcceleratorResponseAcceleratorTypeDef
):
    """
    - **Accelerator** *(dict) --*

      The accelerator that is created by specifying a listener and the supported IP address types.
      - **AcceleratorArn** *(string) --*

        The Amazon Resource Name (ARN) of the accelerator.
    """


_ClientCreateAcceleratorResponseTypeDef = TypedDict(
    "_ClientCreateAcceleratorResponseTypeDef",
    {"Accelerator": ClientCreateAcceleratorResponseAcceleratorTypeDef},
    total=False,
)


class ClientCreateAcceleratorResponseTypeDef(_ClientCreateAcceleratorResponseTypeDef):
    """
    - *(dict) --*

      - **Accelerator** *(dict) --*

        The accelerator that is created by specifying a listener and the supported IP address types.
        - **AcceleratorArn** *(string) --*

          The Amazon Resource Name (ARN) of the accelerator.
    """


_ClientCreateEndpointGroupEndpointConfigurationsTypeDef = TypedDict(
    "_ClientCreateEndpointGroupEndpointConfigurationsTypeDef",
    {"EndpointId": str, "Weight": int, "ClientIPPreservationEnabled": bool},
    total=False,
)


class ClientCreateEndpointGroupEndpointConfigurationsTypeDef(
    _ClientCreateEndpointGroupEndpointConfigurationsTypeDef
):
    """
    - *(dict) --*

      A complex type for endpoints.
      - **EndpointId** *(string) --*

        An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
        Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
        Elastic IP address, this is the Elastic IP address allocation ID.
    """


_ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "_ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef(
    _ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
):
    pass


_ClientCreateEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "_ClientCreateEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ClientCreateEndpointGroupResponseEndpointGroupTypeDef(
    _ClientCreateEndpointGroupResponseEndpointGroupTypeDef
):
    """
    - **EndpointGroup** *(dict) --*

      The information about the endpoint group that was created.
      - **EndpointGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint group.
    """


_ClientCreateEndpointGroupResponseTypeDef = TypedDict(
    "_ClientCreateEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientCreateEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)


class ClientCreateEndpointGroupResponseTypeDef(_ClientCreateEndpointGroupResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointGroup** *(dict) --*

        The information about the endpoint group that was created.
        - **EndpointGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the endpoint group.
    """


_ClientCreateListenerPortRangesTypeDef = TypedDict(
    "_ClientCreateListenerPortRangesTypeDef", {"FromPort": int, "ToPort": int}, total=False
)


class ClientCreateListenerPortRangesTypeDef(_ClientCreateListenerPortRangesTypeDef):
    """
    - *(dict) --*

      A complex type for a range of ports for a listener.
      - **FromPort** *(integer) --*

        The first port in the range of ports, inclusive.
    """


_ClientCreateListenerResponseListenerPortRangesTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientCreateListenerResponseListenerPortRangesTypeDef(
    _ClientCreateListenerResponseListenerPortRangesTypeDef
):
    pass


_ClientCreateListenerResponseListenerTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientCreateListenerResponseListenerPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)


class ClientCreateListenerResponseListenerTypeDef(_ClientCreateListenerResponseListenerTypeDef):
    """
    - **Listener** *(dict) --*

      The listener that you've created.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_ClientCreateListenerResponseTypeDef = TypedDict(
    "_ClientCreateListenerResponseTypeDef",
    {"Listener": ClientCreateListenerResponseListenerTypeDef},
    total=False,
)


class ClientCreateListenerResponseTypeDef(_ClientCreateListenerResponseTypeDef):
    """
    - *(dict) --*

      - **Listener** *(dict) --*

        The listener that you've created.
        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.
    """


_ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef = TypedDict(
    "_ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
    total=False,
)


class ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef(
    _ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef
):
    """
    - **AcceleratorAttributes** *(dict) --*

      The attributes of the accelerator.
      - **FlowLogsEnabled** *(boolean) --*

        Indicates whether flow logs are enabled. The default value is false. If the value is true,
        ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.
        For more information, see `Flow Logs
        <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__
        in the *AWS Global Accelerator Developer Guide* .
    """


_ClientDescribeAcceleratorAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef
    },
    total=False,
)


class ClientDescribeAcceleratorAttributesResponseTypeDef(
    _ClientDescribeAcceleratorAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **AcceleratorAttributes** *(dict) --*

        The attributes of the accelerator.
        - **FlowLogsEnabled** *(boolean) --*

          Indicates whether flow logs are enabled. The default value is false. If the value is true,
          ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.
          For more information, see `Flow Logs
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__
          in the *AWS Global Accelerator Developer Guide* .
    """


_ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "_ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef(
    _ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef
):
    pass


_ClientDescribeAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "_ClientDescribeAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientDescribeAcceleratorResponseAcceleratorTypeDef(
    _ClientDescribeAcceleratorResponseAcceleratorTypeDef
):
    """
    - **Accelerator** *(dict) --*

      The description of the accelerator.
      - **AcceleratorArn** *(string) --*

        The Amazon Resource Name (ARN) of the accelerator.
    """


_ClientDescribeAcceleratorResponseTypeDef = TypedDict(
    "_ClientDescribeAcceleratorResponseTypeDef",
    {"Accelerator": ClientDescribeAcceleratorResponseAcceleratorTypeDef},
    total=False,
)


class ClientDescribeAcceleratorResponseTypeDef(_ClientDescribeAcceleratorResponseTypeDef):
    """
    - *(dict) --*

      - **Accelerator** *(dict) --*

        The description of the accelerator.
        - **AcceleratorArn** *(string) --*

          The Amazon Resource Name (ARN) of the accelerator.
    """


_ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "_ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef(
    _ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
):
    pass


_ClientDescribeEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "_ClientDescribeEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ClientDescribeEndpointGroupResponseEndpointGroupTypeDef(
    _ClientDescribeEndpointGroupResponseEndpointGroupTypeDef
):
    """
    - **EndpointGroup** *(dict) --*

      The description of an endpoint group.
      - **EndpointGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint group.
    """


_ClientDescribeEndpointGroupResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientDescribeEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)


class ClientDescribeEndpointGroupResponseTypeDef(_ClientDescribeEndpointGroupResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointGroup** *(dict) --*

        The description of an endpoint group.
        - **EndpointGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the endpoint group.
    """


_ClientDescribeListenerResponseListenerPortRangesTypeDef = TypedDict(
    "_ClientDescribeListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientDescribeListenerResponseListenerPortRangesTypeDef(
    _ClientDescribeListenerResponseListenerPortRangesTypeDef
):
    pass


_ClientDescribeListenerResponseListenerTypeDef = TypedDict(
    "_ClientDescribeListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientDescribeListenerResponseListenerPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)


class ClientDescribeListenerResponseListenerTypeDef(_ClientDescribeListenerResponseListenerTypeDef):
    """
    - **Listener** *(dict) --*

      The description of a listener.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_ClientDescribeListenerResponseTypeDef = TypedDict(
    "_ClientDescribeListenerResponseTypeDef",
    {"Listener": ClientDescribeListenerResponseListenerTypeDef},
    total=False,
)


class ClientDescribeListenerResponseTypeDef(_ClientDescribeListenerResponseTypeDef):
    """
    - *(dict) --*

      - **Listener** *(dict) --*

        The description of a listener.
        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.
    """


_ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef = TypedDict(
    "_ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef(
    _ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef
):
    pass


_ClientListAcceleratorsResponseAcceleratorsTypeDef = TypedDict(
    "_ClientListAcceleratorsResponseAcceleratorsTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientListAcceleratorsResponseAcceleratorsTypeDef(
    _ClientListAcceleratorsResponseAcceleratorsTypeDef
):
    """
    - *(dict) --*

      An accelerator is a complex type that includes one or more listeners that process inbound
      connections and then direct traffic to one or more endpoint groups, each of which includes
      endpoints, such as load balancers.
      - **AcceleratorArn** *(string) --*

        The Amazon Resource Name (ARN) of the accelerator.
    """


_ClientListAcceleratorsResponseTypeDef = TypedDict(
    "_ClientListAcceleratorsResponseTypeDef",
    {"Accelerators": List[ClientListAcceleratorsResponseAcceleratorsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAcceleratorsResponseTypeDef(_ClientListAcceleratorsResponseTypeDef):
    """
    - *(dict) --*

      - **Accelerators** *(list) --*

        The list of accelerators for a customer account.
        - *(dict) --*

          An accelerator is a complex type that includes one or more listeners that process inbound
          connections and then direct traffic to one or more endpoint groups, each of which includes
          endpoints, such as load balancers.
          - **AcceleratorArn** *(string) --*

            The Amazon Resource Name (ARN) of the accelerator.
    """


_ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef = TypedDict(
    "_ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef(
    _ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef
):
    pass


_ClientListEndpointGroupsResponseEndpointGroupsTypeDef = TypedDict(
    "_ClientListEndpointGroupsResponseEndpointGroupsTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ClientListEndpointGroupsResponseEndpointGroupsTypeDef(
    _ClientListEndpointGroupsResponseEndpointGroupsTypeDef
):
    """
    - *(dict) --*

      A complex type for the endpoint group. An AWS Region can have only one endpoint group for a
      specific listener.
      - **EndpointGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint group.
    """


_ClientListEndpointGroupsResponseTypeDef = TypedDict(
    "_ClientListEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List[ClientListEndpointGroupsResponseEndpointGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEndpointGroupsResponseTypeDef(_ClientListEndpointGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointGroups** *(list) --*

        The list of the endpoint groups associated with a listener.
        - *(dict) --*

          A complex type for the endpoint group. An AWS Region can have only one endpoint group for
          a specific listener.
          - **EndpointGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the endpoint group.
    """


_ClientListListenersResponseListenersPortRangesTypeDef = TypedDict(
    "_ClientListListenersResponseListenersPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientListListenersResponseListenersPortRangesTypeDef(
    _ClientListListenersResponseListenersPortRangesTypeDef
):
    pass


_ClientListListenersResponseListenersTypeDef = TypedDict(
    "_ClientListListenersResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientListListenersResponseListenersPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)


class ClientListListenersResponseListenersTypeDef(_ClientListListenersResponseListenersTypeDef):
    """
    - *(dict) --*

      A complex type for a listener.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_ClientListListenersResponseTypeDef = TypedDict(
    "_ClientListListenersResponseTypeDef",
    {"Listeners": List[ClientListListenersResponseListenersTypeDef], "NextToken": str},
    total=False,
)


class ClientListListenersResponseTypeDef(_ClientListListenersResponseTypeDef):
    """
    - *(dict) --*

      - **Listeners** *(list) --*

        The list of listeners for an accelerator.
        - *(dict) --*

          A complex type for a listener.
          - **ListenerArn** *(string) --*

            The Amazon Resource Name (ARN) of the listener.
    """


_ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef = TypedDict(
    "_ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
    total=False,
)


class ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef(
    _ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef
):
    """
    - **AcceleratorAttributes** *(dict) --*

      Updated attributes for the accelerator.
      - **FlowLogsEnabled** *(boolean) --*

        Indicates whether flow logs are enabled. The default value is false. If the value is true,
        ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.
        For more information, see `Flow Logs
        <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__
        in the *AWS Global Accelerator Developer Guide* .
    """


_ClientUpdateAcceleratorAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef
    },
    total=False,
)


class ClientUpdateAcceleratorAttributesResponseTypeDef(
    _ClientUpdateAcceleratorAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **AcceleratorAttributes** *(dict) --*

        Updated attributes for the accelerator.
        - **FlowLogsEnabled** *(boolean) --*

          Indicates whether flow logs are enabled. The default value is false. If the value is true,
          ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.
          For more information, see `Flow Logs
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__
          in the *AWS Global Accelerator Developer Guide* .
    """


_ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "_ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef(
    _ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef
):
    pass


_ClientUpdateAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "_ClientUpdateAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientUpdateAcceleratorResponseAcceleratorTypeDef(
    _ClientUpdateAcceleratorResponseAcceleratorTypeDef
):
    """
    - **Accelerator** *(dict) --*

      Information about the updated accelerator.
      - **AcceleratorArn** *(string) --*

        The Amazon Resource Name (ARN) of the accelerator.
    """


_ClientUpdateAcceleratorResponseTypeDef = TypedDict(
    "_ClientUpdateAcceleratorResponseTypeDef",
    {"Accelerator": ClientUpdateAcceleratorResponseAcceleratorTypeDef},
    total=False,
)


class ClientUpdateAcceleratorResponseTypeDef(_ClientUpdateAcceleratorResponseTypeDef):
    """
    - *(dict) --*

      - **Accelerator** *(dict) --*

        Information about the updated accelerator.
        - **AcceleratorArn** *(string) --*

          The Amazon Resource Name (ARN) of the accelerator.
    """


_ClientUpdateEndpointGroupEndpointConfigurationsTypeDef = TypedDict(
    "_ClientUpdateEndpointGroupEndpointConfigurationsTypeDef",
    {"EndpointId": str, "Weight": int, "ClientIPPreservationEnabled": bool},
    total=False,
)


class ClientUpdateEndpointGroupEndpointConfigurationsTypeDef(
    _ClientUpdateEndpointGroupEndpointConfigurationsTypeDef
):
    """
    - *(dict) --*

      A complex type for endpoints.
      - **EndpointId** *(string) --*

        An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
        Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
        Elastic IP address, this is the Elastic IP address allocation ID.
    """


_ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "_ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef(
    _ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
):
    pass


_ClientUpdateEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "_ClientUpdateEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ClientUpdateEndpointGroupResponseEndpointGroupTypeDef(
    _ClientUpdateEndpointGroupResponseEndpointGroupTypeDef
):
    """
    - **EndpointGroup** *(dict) --*

      The information about the endpoint group that was updated.
      - **EndpointGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint group.
    """


_ClientUpdateEndpointGroupResponseTypeDef = TypedDict(
    "_ClientUpdateEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientUpdateEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)


class ClientUpdateEndpointGroupResponseTypeDef(_ClientUpdateEndpointGroupResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointGroup** *(dict) --*

        The information about the endpoint group that was updated.
        - **EndpointGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the endpoint group.
    """


_ClientUpdateListenerPortRangesTypeDef = TypedDict(
    "_ClientUpdateListenerPortRangesTypeDef", {"FromPort": int, "ToPort": int}, total=False
)


class ClientUpdateListenerPortRangesTypeDef(_ClientUpdateListenerPortRangesTypeDef):
    """
    - *(dict) --*

      A complex type for a range of ports for a listener.
      - **FromPort** *(integer) --*

        The first port in the range of ports, inclusive.
    """


_ClientUpdateListenerResponseListenerPortRangesTypeDef = TypedDict(
    "_ClientUpdateListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientUpdateListenerResponseListenerPortRangesTypeDef(
    _ClientUpdateListenerResponseListenerPortRangesTypeDef
):
    pass


_ClientUpdateListenerResponseListenerTypeDef = TypedDict(
    "_ClientUpdateListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientUpdateListenerResponseListenerPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)


class ClientUpdateListenerResponseListenerTypeDef(_ClientUpdateListenerResponseListenerTypeDef):
    """
    - **Listener** *(dict) --*

      Information for the updated listener.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_ClientUpdateListenerResponseTypeDef = TypedDict(
    "_ClientUpdateListenerResponseTypeDef",
    {"Listener": ClientUpdateListenerResponseListenerTypeDef},
    total=False,
)


class ClientUpdateListenerResponseTypeDef(_ClientUpdateListenerResponseTypeDef):
    """
    - *(dict) --*

      - **Listener** *(dict) --*

        Information for the updated listener.
        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.
    """


_ListAcceleratorsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAcceleratorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAcceleratorsPaginatePaginationConfigTypeDef(
    _ListAcceleratorsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef = TypedDict(
    "_ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef(
    _ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef
):
    pass


_ListAcceleratorsPaginateResponseAcceleratorsTypeDef = TypedDict(
    "_ListAcceleratorsPaginateResponseAcceleratorsTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ListAcceleratorsPaginateResponseAcceleratorsTypeDef(
    _ListAcceleratorsPaginateResponseAcceleratorsTypeDef
):
    """
    - *(dict) --*

      An accelerator is a complex type that includes one or more listeners that process inbound
      connections and then direct traffic to one or more endpoint groups, each of which includes
      endpoints, such as load balancers.
      - **AcceleratorArn** *(string) --*

        The Amazon Resource Name (ARN) of the accelerator.
    """


_ListAcceleratorsPaginateResponseTypeDef = TypedDict(
    "_ListAcceleratorsPaginateResponseTypeDef",
    {"Accelerators": List[ListAcceleratorsPaginateResponseAcceleratorsTypeDef]},
    total=False,
)


class ListAcceleratorsPaginateResponseTypeDef(_ListAcceleratorsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Accelerators** *(list) --*

        The list of accelerators for a customer account.
        - *(dict) --*

          An accelerator is a complex type that includes one or more listeners that process inbound
          connections and then direct traffic to one or more endpoint groups, each of which includes
          endpoints, such as load balancers.
          - **AcceleratorArn** *(string) --*

            The Amazon Resource Name (ARN) of the accelerator.
    """


_ListEndpointGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEndpointGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEndpointGroupsPaginatePaginationConfigTypeDef(
    _ListEndpointGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef = TypedDict(
    "_ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef(
    _ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef
):
    pass


_ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef = TypedDict(
    "_ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": Any,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef(
    _ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef
):
    """
    - *(dict) --*

      A complex type for the endpoint group. An AWS Region can have only one endpoint group for a
      specific listener.
      - **EndpointGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint group.
    """


_ListEndpointGroupsPaginateResponseTypeDef = TypedDict(
    "_ListEndpointGroupsPaginateResponseTypeDef",
    {"EndpointGroups": List[ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef]},
    total=False,
)


class ListEndpointGroupsPaginateResponseTypeDef(_ListEndpointGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointGroups** *(list) --*

        The list of the endpoint groups associated with a listener.
        - *(dict) --*

          A complex type for the endpoint group. An AWS Region can have only one endpoint group for
          a specific listener.
          - **EndpointGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the endpoint group.
    """


_ListListenersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListListenersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListListenersPaginatePaginationConfigTypeDef(_ListListenersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListListenersPaginateResponseListenersPortRangesTypeDef = TypedDict(
    "_ListListenersPaginateResponseListenersPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ListListenersPaginateResponseListenersPortRangesTypeDef(
    _ListListenersPaginateResponseListenersPortRangesTypeDef
):
    pass


_ListListenersPaginateResponseListenersTypeDef = TypedDict(
    "_ListListenersPaginateResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ListListenersPaginateResponseListenersPortRangesTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)


class ListListenersPaginateResponseListenersTypeDef(_ListListenersPaginateResponseListenersTypeDef):
    """
    - *(dict) --*

      A complex type for a listener.
      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.
    """


_ListListenersPaginateResponseTypeDef = TypedDict(
    "_ListListenersPaginateResponseTypeDef",
    {"Listeners": List[ListListenersPaginateResponseListenersTypeDef]},
    total=False,
)


class ListListenersPaginateResponseTypeDef(_ListListenersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Listeners** *(list) --*

        The list of listeners for an accelerator.
        - *(dict) --*

          A complex type for a listener.
          - **ListenerArn** *(string) --*

            The Amazon Resource Name (ARN) of the listener.
    """
