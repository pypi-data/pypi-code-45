"Main interface for dax service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientCreateClusterResponseClusterNodesEndpointTypeDef",
    "ClientCreateClusterResponseClusterNodesTypeDef",
    "ClientCreateClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientCreateClusterResponseClusterParameterGroupTypeDef",
    "ClientCreateClusterResponseClusterSSEDescriptionTypeDef",
    "ClientCreateClusterResponseClusterSecurityGroupsTypeDef",
    "ClientCreateClusterResponseClusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateClusterSSESpecificationTypeDef",
    "ClientCreateClusterTagsTypeDef",
    "ClientCreateParameterGroupResponseParameterGroupTypeDef",
    "ClientCreateParameterGroupResponseTypeDef",
    "ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    "ClientCreateSubnetGroupResponseSubnetGroupTypeDef",
    "ClientCreateSubnetGroupResponseTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNodesTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    "ClientDecreaseReplicationFactorResponseClusterTypeDef",
    "ClientDecreaseReplicationFactorResponseTypeDef",
    "ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientDeleteClusterResponseClusterNodesEndpointTypeDef",
    "ClientDeleteClusterResponseClusterNodesTypeDef",
    "ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientDeleteClusterResponseClusterParameterGroupTypeDef",
    "ClientDeleteClusterResponseClusterSSEDescriptionTypeDef",
    "ClientDeleteClusterResponseClusterSecurityGroupsTypeDef",
    "ClientDeleteClusterResponseClusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteParameterGroupResponseTypeDef",
    "ClientDeleteSubnetGroupResponseTypeDef",
    "ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef",
    "ClientDescribeClustersResponseClustersNodesEndpointTypeDef",
    "ClientDescribeClustersResponseClustersNodesTypeDef",
    "ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef",
    "ClientDescribeClustersResponseClustersParameterGroupTypeDef",
    "ClientDescribeClustersResponseClustersSSEDescriptionTypeDef",
    "ClientDescribeClustersResponseClustersSecurityGroupsTypeDef",
    "ClientDescribeClustersResponseClustersTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    "ClientDescribeDefaultParametersResponseParametersTypeDef",
    "ClientDescribeDefaultParametersResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeParameterGroupsResponseParameterGroupsTypeDef",
    "ClientDescribeParameterGroupsResponseTypeDef",
    "ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    "ClientDescribeParametersResponseParametersTypeDef",
    "ClientDescribeParametersResponseTypeDef",
    "ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef",
    "ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef",
    "ClientDescribeSubnetGroupsResponseTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNodesTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    "ClientIncreaseReplicationFactorResponseClusterTypeDef",
    "ClientIncreaseReplicationFactorResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientRebootNodeResponseClusterNodesEndpointTypeDef",
    "ClientRebootNodeResponseClusterNodesTypeDef",
    "ClientRebootNodeResponseClusterNotificationConfigurationTypeDef",
    "ClientRebootNodeResponseClusterParameterGroupTypeDef",
    "ClientRebootNodeResponseClusterSSEDescriptionTypeDef",
    "ClientRebootNodeResponseClusterSecurityGroupsTypeDef",
    "ClientRebootNodeResponseClusterTypeDef",
    "ClientRebootNodeResponseTypeDef",
    "ClientTagResourceResponseTagsTypeDef",
    "ClientTagResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUntagResourceResponseTagsTypeDef",
    "ClientUntagResourceResponseTypeDef",
    "ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    "ClientUpdateClusterResponseClusterNodesEndpointTypeDef",
    "ClientUpdateClusterResponseClusterNodesTypeDef",
    "ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef",
    "ClientUpdateClusterResponseClusterParameterGroupTypeDef",
    "ClientUpdateClusterResponseClusterSSEDescriptionTypeDef",
    "ClientUpdateClusterResponseClusterSecurityGroupsTypeDef",
    "ClientUpdateClusterResponseClusterTypeDef",
    "ClientUpdateClusterResponseTypeDef",
    "ClientUpdateParameterGroupParameterNameValuesTypeDef",
    "ClientUpdateParameterGroupResponseParameterGroupTypeDef",
    "ClientUpdateParameterGroupResponseTypeDef",
    "ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    "ClientUpdateSubnetGroupResponseSubnetGroupTypeDef",
    "ClientUpdateSubnetGroupResponseTypeDef",
    "DescribeClustersPaginatePaginationConfigTypeDef",
    "DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef",
    "DescribeClustersPaginateResponseClustersNodesEndpointTypeDef",
    "DescribeClustersPaginateResponseClustersNodesTypeDef",
    "DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef",
    "DescribeClustersPaginateResponseClustersParameterGroupTypeDef",
    "DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef",
    "DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef",
    "DescribeClustersPaginateResponseClustersTypeDef",
    "DescribeClustersPaginateResponseTypeDef",
    "DescribeDefaultParametersPaginatePaginationConfigTypeDef",
    "DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef",
    "DescribeDefaultParametersPaginateResponseParametersTypeDef",
    "DescribeDefaultParametersPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef",
    "DescribeParameterGroupsPaginateResponseTypeDef",
    "DescribeParametersPaginatePaginationConfigTypeDef",
    "DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef",
    "DescribeParametersPaginateResponseParametersTypeDef",
    "DescribeParametersPaginateResponseTypeDef",
    "DescribeSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef",
    "DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef",
    "DescribeSubnetGroupsPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagsTypeDef",
    "ListTagsPaginateResponseTypeDef",
)


_ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef
):
    pass


_ClientCreateClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateClusterResponseClusterNodesEndpointTypeDef(
    _ClientCreateClusterResponseClusterNodesEndpointTypeDef
):
    pass


_ClientCreateClusterResponseClusterNodesTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientCreateClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientCreateClusterResponseClusterNodesTypeDef(
    _ClientCreateClusterResponseClusterNodesTypeDef
):
    pass


_ClientCreateClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientCreateClusterResponseClusterNotificationConfigurationTypeDef(
    _ClientCreateClusterResponseClusterNotificationConfigurationTypeDef
):
    pass


_ClientCreateClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)


class ClientCreateClusterResponseClusterParameterGroupTypeDef(
    _ClientCreateClusterResponseClusterParameterGroupTypeDef
):
    pass


_ClientCreateClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)


class ClientCreateClusterResponseClusterSSEDescriptionTypeDef(
    _ClientCreateClusterResponseClusterSSEDescriptionTypeDef
):
    pass


_ClientCreateClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientCreateClusterResponseClusterSecurityGroupsTypeDef(
    _ClientCreateClusterResponseClusterSecurityGroupsTypeDef
):
    pass


_ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientCreateClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientCreateClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientCreateClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientCreateClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientCreateClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientCreateClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientCreateClusterResponseClusterTypeDef(_ClientCreateClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      A description of the DAX cluster that you have created.
      - **ClusterName** *(string) --*

        The name of the DAX cluster.
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef",
    {"Cluster": ClientCreateClusterResponseClusterTypeDef},
    total=False,
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        A description of the DAX cluster that you have created.
        - **ClusterName** *(string) --*

          The name of the DAX cluster.
    """


_ClientCreateClusterSSESpecificationTypeDef = TypedDict(
    "_ClientCreateClusterSSESpecificationTypeDef", {"Enabled": bool}
)


class ClientCreateClusterSSESpecificationTypeDef(_ClientCreateClusterSSESpecificationTypeDef):
    """
    Represents the settings used to enable server-side encryption on the cluster.
    - **Enabled** *(boolean) --***[REQUIRED]**

      Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.
    """


_ClientCreateClusterTagsTypeDef = TypedDict(
    "_ClientCreateClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateClusterTagsTypeDef(_ClientCreateClusterTagsTypeDef):
    """
    - *(dict) --*

      A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single
      DAX cluster.
      AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
      user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
      User-assigned tag names have the prefix ``user:`` .
      You cannot backdate the application of a tag.
      - **Key** *(string) --*

        The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
        with the same key. If you try to add an existing tag (same key), the existing tag value will
        be updated to the new value.
    """


_ClientCreateParameterGroupResponseParameterGroupTypeDef = TypedDict(
    "_ClientCreateParameterGroupResponseParameterGroupTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)


class ClientCreateParameterGroupResponseParameterGroupTypeDef(
    _ClientCreateParameterGroupResponseParameterGroupTypeDef
):
    """
    - **ParameterGroup** *(dict) --*

      Represents the output of a *CreateParameterGroup* action.
      - **ParameterGroupName** *(string) --*

        The name of the parameter group.
    """


_ClientCreateParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateParameterGroupResponseTypeDef",
    {"ParameterGroup": ClientCreateParameterGroupResponseParameterGroupTypeDef},
    total=False,
)


class ClientCreateParameterGroupResponseTypeDef(_ClientCreateParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ParameterGroup** *(dict) --*

        Represents the output of a *CreateParameterGroup* action.
        - **ParameterGroupName** *(string) --*

          The name of the parameter group.
    """


_ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)


class ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef(
    _ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef
):
    pass


_ClientCreateSubnetGroupResponseSubnetGroupTypeDef = TypedDict(
    "_ClientCreateSubnetGroupResponseSubnetGroupTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientCreateSubnetGroupResponseSubnetGroupSubnetsTypeDef],
    },
    total=False,
)


class ClientCreateSubnetGroupResponseSubnetGroupTypeDef(
    _ClientCreateSubnetGroupResponseSubnetGroupTypeDef
):
    """
    - **SubnetGroup** *(dict) --*

      Represents the output of a *CreateSubnetGroup* operation.
      - **SubnetGroupName** *(string) --*

        The name of the subnet group.
    """


_ClientCreateSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateSubnetGroupResponseTypeDef",
    {"SubnetGroup": ClientCreateSubnetGroupResponseSubnetGroupTypeDef},
    total=False,
)


class ClientCreateSubnetGroupResponseTypeDef(_ClientCreateSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **SubnetGroup** *(dict) --*

        Represents the output of a *CreateSubnetGroup* operation.
        - **SubnetGroupName** *(string) --*

          The name of the subnet group.
    """


_ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef
):
    pass


_ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef
):
    pass


_ClientDecreaseReplicationFactorResponseClusterNodesTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDecreaseReplicationFactorResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterNodesTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterNodesTypeDef
):
    pass


_ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef
):
    pass


_ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef
):
    pass


_ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef
):
    pass


_ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef
):
    pass


_ClientDecreaseReplicationFactorResponseClusterTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDecreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDecreaseReplicationFactorResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDecreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientDecreaseReplicationFactorResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientDecreaseReplicationFactorResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientDecreaseReplicationFactorResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientDecreaseReplicationFactorResponseClusterTypeDef(
    _ClientDecreaseReplicationFactorResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      A description of the DAX cluster, after you have decreased its replication factor.
      - **ClusterName** *(string) --*

        The name of the DAX cluster.
    """


_ClientDecreaseReplicationFactorResponseTypeDef = TypedDict(
    "_ClientDecreaseReplicationFactorResponseTypeDef",
    {"Cluster": ClientDecreaseReplicationFactorResponseClusterTypeDef},
    total=False,
)


class ClientDecreaseReplicationFactorResponseTypeDef(
    _ClientDecreaseReplicationFactorResponseTypeDef
):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        A description of the DAX cluster, after you have decreased its replication factor.
        - **ClusterName** *(string) --*

          The name of the DAX cluster.
    """


_ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef
):
    pass


_ClientDeleteClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteClusterResponseClusterNodesEndpointTypeDef(
    _ClientDeleteClusterResponseClusterNodesEndpointTypeDef
):
    pass


_ClientDeleteClusterResponseClusterNodesTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDeleteClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterNodesTypeDef(
    _ClientDeleteClusterResponseClusterNodesTypeDef
):
    pass


_ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef(
    _ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef
):
    pass


_ClientDeleteClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)


class ClientDeleteClusterResponseClusterParameterGroupTypeDef(
    _ClientDeleteClusterResponseClusterParameterGroupTypeDef
):
    pass


_ClientDeleteClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)


class ClientDeleteClusterResponseClusterSSEDescriptionTypeDef(
    _ClientDeleteClusterResponseClusterSSEDescriptionTypeDef
):
    pass


_ClientDeleteClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientDeleteClusterResponseClusterSecurityGroupsTypeDef(
    _ClientDeleteClusterResponseClusterSecurityGroupsTypeDef
):
    pass


_ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDeleteClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDeleteClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDeleteClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientDeleteClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientDeleteClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientDeleteClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterTypeDef(_ClientDeleteClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      A description of the DAX cluster that is being deleted.
      - **ClusterName** *(string) --*

        The name of the DAX cluster.
    """


_ClientDeleteClusterResponseTypeDef = TypedDict(
    "_ClientDeleteClusterResponseTypeDef",
    {"Cluster": ClientDeleteClusterResponseClusterTypeDef},
    total=False,
)


class ClientDeleteClusterResponseTypeDef(_ClientDeleteClusterResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        A description of the DAX cluster that is being deleted.
        - **ClusterName** *(string) --*

          The name of the DAX cluster.
    """


_ClientDeleteParameterGroupResponseTypeDef = TypedDict(
    "_ClientDeleteParameterGroupResponseTypeDef", {"DeletionMessage": str}, total=False
)


class ClientDeleteParameterGroupResponseTypeDef(_ClientDeleteParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DeletionMessage** *(string) --*

        A user-specified message for this action (i.e., a reason for deleting the parameter group).
    """


_ClientDeleteSubnetGroupResponseTypeDef = TypedDict(
    "_ClientDeleteSubnetGroupResponseTypeDef", {"DeletionMessage": str}, total=False
)


class ClientDeleteSubnetGroupResponseTypeDef(_ClientDeleteSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **DeletionMessage** *(string) --*

        A user-specified message for this action (i.e., a reason for deleting the subnet group).
    """


_ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef(
    _ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef
):
    pass


_ClientDescribeClustersResponseClustersNodesEndpointTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeClustersResponseClustersNodesEndpointTypeDef(
    _ClientDescribeClustersResponseClustersNodesEndpointTypeDef
):
    pass


_ClientDescribeClustersResponseClustersNodesTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientDescribeClustersResponseClustersNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersNodesTypeDef(
    _ClientDescribeClustersResponseClustersNodesTypeDef
):
    pass


_ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef(
    _ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef
):
    pass


_ClientDescribeClustersResponseClustersParameterGroupTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)


class ClientDescribeClustersResponseClustersParameterGroupTypeDef(
    _ClientDescribeClustersResponseClustersParameterGroupTypeDef
):
    pass


_ClientDescribeClustersResponseClustersSSEDescriptionTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)


class ClientDescribeClustersResponseClustersSSEDescriptionTypeDef(
    _ClientDescribeClustersResponseClustersSSEDescriptionTypeDef
):
    pass


_ClientDescribeClustersResponseClustersSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientDescribeClustersResponseClustersSecurityGroupsTypeDef(
    _ClientDescribeClustersResponseClustersSecurityGroupsTypeDef
):
    pass


_ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientDescribeClustersResponseClustersClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientDescribeClustersResponseClustersNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientDescribeClustersResponseClustersNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientDescribeClustersResponseClustersSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientDescribeClustersResponseClustersParameterGroupTypeDef,
        "SSEDescription": ClientDescribeClustersResponseClustersSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersTypeDef(_ClientDescribeClustersResponseClustersTypeDef):
    pass


_ClientDescribeClustersResponseTypeDef = TypedDict(
    "_ClientDescribeClustersResponseTypeDef",
    {"NextToken": str, "Clusters": List[ClientDescribeClustersResponseClustersTypeDef]},
    total=False,
)


class ClientDescribeClustersResponseTypeDef(_ClientDescribeClustersResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "_ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)


class ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef(
    _ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef
):
    pass


_ClientDescribeDefaultParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeDefaultParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": Literal["DEFAULT", "NODE_TYPE_SPECIFIC"],
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            ClientDescribeDefaultParametersResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "ChangeType": Literal["IMMEDIATE", "REQUIRES_REBOOT"],
    },
    total=False,
)


class ClientDescribeDefaultParametersResponseParametersTypeDef(
    _ClientDescribeDefaultParametersResponseParametersTypeDef
):
    pass


_ClientDescribeDefaultParametersResponseTypeDef = TypedDict(
    "_ClientDescribeDefaultParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List[ClientDescribeDefaultParametersResponseParametersTypeDef],
    },
    total=False,
)


class ClientDescribeDefaultParametersResponseTypeDef(
    _ClientDescribeDefaultParametersResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceName": str,
        "SourceType": Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"],
        "Message": str,
        "Date": datetime,
    },
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(_ClientDescribeEventsResponseEventsTypeDef):
    pass


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"NextToken": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeParameterGroupsResponseParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeParameterGroupsResponseParameterGroupsTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)


class ClientDescribeParameterGroupsResponseParameterGroupsTypeDef(
    _ClientDescribeParameterGroupsResponseParameterGroupsTypeDef
):
    pass


_ClientDescribeParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeParameterGroupsResponseTypeDef",
    {
        "NextToken": str,
        "ParameterGroups": List[ClientDescribeParameterGroupsResponseParameterGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeParameterGroupsResponseTypeDef(_ClientDescribeParameterGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "_ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)


class ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef(
    _ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef
):
    pass


_ClientDescribeParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": Literal["DEFAULT", "NODE_TYPE_SPECIFIC"],
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            ClientDescribeParametersResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "ChangeType": Literal["IMMEDIATE", "REQUIRES_REBOOT"],
    },
    total=False,
)


class ClientDescribeParametersResponseParametersTypeDef(
    _ClientDescribeParametersResponseParametersTypeDef
):
    pass


_ClientDescribeParametersResponseTypeDef = TypedDict(
    "_ClientDescribeParametersResponseTypeDef",
    {"NextToken": str, "Parameters": List[ClientDescribeParametersResponseParametersTypeDef]},
    total=False,
)


class ClientDescribeParametersResponseTypeDef(_ClientDescribeParametersResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)


class ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef(
    _ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef
):
    pass


_ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientDescribeSubnetGroupsResponseSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)


class ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef(
    _ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef
):
    pass


_ClientDescribeSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeSubnetGroupsResponseTypeDef",
    {"NextToken": str, "SubnetGroups": List[ClientDescribeSubnetGroupsResponseSubnetGroupsTypeDef]},
    total=False,
)


class ClientDescribeSubnetGroupsResponseTypeDef(_ClientDescribeSubnetGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef
):
    pass


_ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef
):
    pass


_ClientIncreaseReplicationFactorResponseClusterNodesTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientIncreaseReplicationFactorResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterNodesTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterNodesTypeDef
):
    pass


_ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef
):
    pass


_ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef
):
    pass


_ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef
):
    pass


_ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef
):
    pass


_ClientIncreaseReplicationFactorResponseClusterTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientIncreaseReplicationFactorResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientIncreaseReplicationFactorResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientIncreaseReplicationFactorResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientIncreaseReplicationFactorResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientIncreaseReplicationFactorResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientIncreaseReplicationFactorResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientIncreaseReplicationFactorResponseClusterTypeDef(
    _ClientIncreaseReplicationFactorResponseClusterTypeDef
):
    """
    - **Cluster** *(dict) --*

      A description of the DAX cluster. with its new replication factor.
      - **ClusterName** *(string) --*

        The name of the DAX cluster.
    """


_ClientIncreaseReplicationFactorResponseTypeDef = TypedDict(
    "_ClientIncreaseReplicationFactorResponseTypeDef",
    {"Cluster": ClientIncreaseReplicationFactorResponseClusterTypeDef},
    total=False,
)


class ClientIncreaseReplicationFactorResponseTypeDef(
    _ClientIncreaseReplicationFactorResponseTypeDef
):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        A description of the DAX cluster. with its new replication factor.
        - **ClusterName** *(string) --*

          The name of the DAX cluster.
    """


_ClientListTagsResponseTagsTypeDef = TypedDict(
    "_ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagsTypeDef(_ClientListTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single
      DAX cluster.
      AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
      user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
      User-assigned tag names have the prefix ``user:`` .
      You cannot backdate the application of a tag.
      - **Key** *(string) --*

        The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
        with the same key. If you try to add an existing tag (same key), the existing tag value will
        be updated to the new value.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        A list of tags currently associated with the DAX cluster.
        - *(dict) --*

          A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
          single DAX cluster.
          AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which
          the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
          User-assigned tag names have the prefix ``user:`` .
          You cannot backdate the application of a tag.
          - **Key** *(string) --*

            The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one
            tag with the same key. If you try to add an existing tag (same key), the existing tag
            value will be updated to the new value.
    """


_ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef
):
    pass


_ClientRebootNodeResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRebootNodeResponseClusterNodesEndpointTypeDef(
    _ClientRebootNodeResponseClusterNodesEndpointTypeDef
):
    pass


_ClientRebootNodeResponseClusterNodesTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientRebootNodeResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientRebootNodeResponseClusterNodesTypeDef(_ClientRebootNodeResponseClusterNodesTypeDef):
    pass


_ClientRebootNodeResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientRebootNodeResponseClusterNotificationConfigurationTypeDef(
    _ClientRebootNodeResponseClusterNotificationConfigurationTypeDef
):
    pass


_ClientRebootNodeResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)


class ClientRebootNodeResponseClusterParameterGroupTypeDef(
    _ClientRebootNodeResponseClusterParameterGroupTypeDef
):
    pass


_ClientRebootNodeResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)


class ClientRebootNodeResponseClusterSSEDescriptionTypeDef(
    _ClientRebootNodeResponseClusterSSEDescriptionTypeDef
):
    pass


_ClientRebootNodeResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientRebootNodeResponseClusterSecurityGroupsTypeDef(
    _ClientRebootNodeResponseClusterSecurityGroupsTypeDef
):
    pass


_ClientRebootNodeResponseClusterTypeDef = TypedDict(
    "_ClientRebootNodeResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientRebootNodeResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientRebootNodeResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientRebootNodeResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientRebootNodeResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientRebootNodeResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientRebootNodeResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientRebootNodeResponseClusterTypeDef(_ClientRebootNodeResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      A description of the DAX cluster after a node has been rebooted.
      - **ClusterName** *(string) --*

        The name of the DAX cluster.
    """


_ClientRebootNodeResponseTypeDef = TypedDict(
    "_ClientRebootNodeResponseTypeDef",
    {"Cluster": ClientRebootNodeResponseClusterTypeDef},
    total=False,
)


class ClientRebootNodeResponseTypeDef(_ClientRebootNodeResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        A description of the DAX cluster after a node has been rebooted.
        - **ClusterName** *(string) --*

          The name of the DAX cluster.
    """


_ClientTagResourceResponseTagsTypeDef = TypedDict(
    "_ClientTagResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceResponseTagsTypeDef(_ClientTagResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single
      DAX cluster.
      AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
      user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
      User-assigned tag names have the prefix ``user:`` .
      You cannot backdate the application of a tag.
      - **Key** *(string) --*

        The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
        with the same key. If you try to add an existing tag (same key), the existing tag value will
        be updated to the new value.
    """


_ClientTagResourceResponseTypeDef = TypedDict(
    "_ClientTagResourceResponseTypeDef",
    {"Tags": List[ClientTagResourceResponseTagsTypeDef]},
    total=False,
)


class ClientTagResourceResponseTypeDef(_ClientTagResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The list of tags that are associated with the DAX resource.
        - *(dict) --*

          A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
          single DAX cluster.
          AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which
          the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
          User-assigned tag names have the prefix ``user:`` .
          You cannot backdate the application of a tag.
          - **Key** *(string) --*

            The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one
            tag with the same key. If you try to add an existing tag (same key), the existing tag
            value will be updated to the new value.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single
      DAX cluster.
      AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
      user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
      User-assigned tag names have the prefix ``user:`` .
      You cannot backdate the application of a tag.
      - **Key** *(string) --*

        The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
        with the same key. If you try to add an existing tag (same key), the existing tag value will
        be updated to the new value.
    """


_ClientUntagResourceResponseTagsTypeDef = TypedDict(
    "_ClientUntagResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUntagResourceResponseTagsTypeDef(_ClientUntagResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single
      DAX cluster.
      AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
      user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
      User-assigned tag names have the prefix ``user:`` .
      You cannot backdate the application of a tag.
      - **Key** *(string) --*

        The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
        with the same key. If you try to add an existing tag (same key), the existing tag value will
        be updated to the new value.
    """


_ClientUntagResourceResponseTypeDef = TypedDict(
    "_ClientUntagResourceResponseTypeDef",
    {"Tags": List[ClientUntagResourceResponseTagsTypeDef]},
    total=False,
)


class ClientUntagResourceResponseTypeDef(_ClientUntagResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tag keys that have been removed from the cluster.
        - *(dict) --*

          A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
          single DAX cluster.
          AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which
          the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
          User-assigned tag names have the prefix ``user:`` .
          You cannot backdate the application of a tag.
          - **Key** *(string) --*

            The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one
            tag with the same key. If you try to add an existing tag (same key), the existing tag
            value will be updated to the new value.
    """


_ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef(
    _ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef
):
    pass


_ClientUpdateClusterResponseClusterNodesEndpointTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientUpdateClusterResponseClusterNodesEndpointTypeDef(
    _ClientUpdateClusterResponseClusterNodesEndpointTypeDef
):
    pass


_ClientUpdateClusterResponseClusterNodesTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": ClientUpdateClusterResponseClusterNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class ClientUpdateClusterResponseClusterNodesTypeDef(
    _ClientUpdateClusterResponseClusterNodesTypeDef
):
    pass


_ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef(
    _ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef
):
    pass


_ClientUpdateClusterResponseClusterParameterGroupTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)


class ClientUpdateClusterResponseClusterParameterGroupTypeDef(
    _ClientUpdateClusterResponseClusterParameterGroupTypeDef
):
    pass


_ClientUpdateClusterResponseClusterSSEDescriptionTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)


class ClientUpdateClusterResponseClusterSSEDescriptionTypeDef(
    _ClientUpdateClusterResponseClusterSSEDescriptionTypeDef
):
    pass


_ClientUpdateClusterResponseClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class ClientUpdateClusterResponseClusterSecurityGroupsTypeDef(
    _ClientUpdateClusterResponseClusterSecurityGroupsTypeDef
):
    pass


_ClientUpdateClusterResponseClusterTypeDef = TypedDict(
    "_ClientUpdateClusterResponseClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": ClientUpdateClusterResponseClusterClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[ClientUpdateClusterResponseClusterNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": ClientUpdateClusterResponseClusterNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[ClientUpdateClusterResponseClusterSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": ClientUpdateClusterResponseClusterParameterGroupTypeDef,
        "SSEDescription": ClientUpdateClusterResponseClusterSSEDescriptionTypeDef,
    },
    total=False,
)


class ClientUpdateClusterResponseClusterTypeDef(_ClientUpdateClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      A description of the DAX cluster, after it has been modified.
      - **ClusterName** *(string) --*

        The name of the DAX cluster.
    """


_ClientUpdateClusterResponseTypeDef = TypedDict(
    "_ClientUpdateClusterResponseTypeDef",
    {"Cluster": ClientUpdateClusterResponseClusterTypeDef},
    total=False,
)


class ClientUpdateClusterResponseTypeDef(_ClientUpdateClusterResponseTypeDef):
    """
    - *(dict) --*

      - **Cluster** *(dict) --*

        A description of the DAX cluster, after it has been modified.
        - **ClusterName** *(string) --*

          The name of the DAX cluster.
    """


_ClientUpdateParameterGroupParameterNameValuesTypeDef = TypedDict(
    "_ClientUpdateParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientUpdateParameterGroupParameterNameValuesTypeDef(
    _ClientUpdateParameterGroupParameterNameValuesTypeDef
):
    """
    - *(dict) --*

      An individual DAX parameter.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_ClientUpdateParameterGroupResponseParameterGroupTypeDef = TypedDict(
    "_ClientUpdateParameterGroupResponseParameterGroupTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)


class ClientUpdateParameterGroupResponseParameterGroupTypeDef(
    _ClientUpdateParameterGroupResponseParameterGroupTypeDef
):
    """
    - **ParameterGroup** *(dict) --*

      The parameter group that has been modified.
      - **ParameterGroupName** *(string) --*

        The name of the parameter group.
    """


_ClientUpdateParameterGroupResponseTypeDef = TypedDict(
    "_ClientUpdateParameterGroupResponseTypeDef",
    {"ParameterGroup": ClientUpdateParameterGroupResponseParameterGroupTypeDef},
    total=False,
)


class ClientUpdateParameterGroupResponseTypeDef(_ClientUpdateParameterGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ParameterGroup** *(dict) --*

        The parameter group that has been modified.
        - **ParameterGroupName** *(string) --*

          The name of the parameter group.
    """


_ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)


class ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef(
    _ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef
):
    pass


_ClientUpdateSubnetGroupResponseSubnetGroupTypeDef = TypedDict(
    "_ClientUpdateSubnetGroupResponseSubnetGroupTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[ClientUpdateSubnetGroupResponseSubnetGroupSubnetsTypeDef],
    },
    total=False,
)


class ClientUpdateSubnetGroupResponseSubnetGroupTypeDef(
    _ClientUpdateSubnetGroupResponseSubnetGroupTypeDef
):
    """
    - **SubnetGroup** *(dict) --*

      The subnet group that has been modified.
      - **SubnetGroupName** *(string) --*

        The name of the subnet group.
    """


_ClientUpdateSubnetGroupResponseTypeDef = TypedDict(
    "_ClientUpdateSubnetGroupResponseTypeDef",
    {"SubnetGroup": ClientUpdateSubnetGroupResponseSubnetGroupTypeDef},
    total=False,
)


class ClientUpdateSubnetGroupResponseTypeDef(_ClientUpdateSubnetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **SubnetGroup** *(dict) --*

        The subnet group that has been modified.
        - **SubnetGroupName** *(string) --*

          The name of the subnet group.
    """


_DescribeClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeClustersPaginatePaginationConfigTypeDef(
    _DescribeClustersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef(
    _DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersNodesEndpointTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeClustersPaginateResponseClustersNodesEndpointTypeDef(
    _DescribeClustersPaginateResponseClustersNodesEndpointTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersNodesTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersNodesTypeDef",
    {
        "NodeId": str,
        "Endpoint": DescribeClustersPaginateResponseClustersNodesEndpointTypeDef,
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersNodesTypeDef(
    _DescribeClustersPaginateResponseClustersNodesTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef(
    _DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersParameterGroupTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersParameterGroupTypeDef",
    {"ParameterGroupName": str, "ParameterApplyStatus": str, "NodeIdsToReboot": List[str]},
    total=False,
)


class DescribeClustersPaginateResponseClustersParameterGroupTypeDef(
    _DescribeClustersPaginateResponseClustersParameterGroupTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef",
    {"Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"]},
    total=False,
)


class DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef(
    _DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef",
    {"SecurityGroupIdentifier": str, "Status": str},
    total=False,
)


class DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef(
    _DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": DescribeClustersPaginateResponseClustersClusterDiscoveryEndpointTypeDef,
        "NodeIdsToRemove": List[str],
        "Nodes": List[DescribeClustersPaginateResponseClustersNodesTypeDef],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": DescribeClustersPaginateResponseClustersNotificationConfigurationTypeDef,
        "SubnetGroup": str,
        "SecurityGroups": List[DescribeClustersPaginateResponseClustersSecurityGroupsTypeDef],
        "IamRoleArn": str,
        "ParameterGroup": DescribeClustersPaginateResponseClustersParameterGroupTypeDef,
        "SSEDescription": DescribeClustersPaginateResponseClustersSSEDescriptionTypeDef,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersTypeDef(
    _DescribeClustersPaginateResponseClustersTypeDef
):
    """
    - *(dict) --*

      Contains all of the attributes of a specific DAX cluster.
      - **ClusterName** *(string) --*

        The name of the DAX cluster.
    """


_DescribeClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseTypeDef",
    {"Clusters": List[DescribeClustersPaginateResponseClustersTypeDef]},
    total=False,
)


class DescribeClustersPaginateResponseTypeDef(_DescribeClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Clusters** *(list) --*

        The descriptions of your DAX clusters, in response to a *DescribeClusters* request.
        - *(dict) --*

          Contains all of the attributes of a specific DAX cluster.
          - **ClusterName** *(string) --*

            The name of the DAX cluster.
    """


_DescribeDefaultParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDefaultParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDefaultParametersPaginatePaginationConfigTypeDef(
    _DescribeDefaultParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "_DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)


class DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef(
    _DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef
):
    pass


_DescribeDefaultParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeDefaultParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": Literal["DEFAULT", "NODE_TYPE_SPECIFIC"],
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            DescribeDefaultParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "ChangeType": Literal["IMMEDIATE", "REQUIRES_REBOOT"],
    },
    total=False,
)


class DescribeDefaultParametersPaginateResponseParametersTypeDef(
    _DescribeDefaultParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      Describes an individual setting that controls some aspect of DAX behavior.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_DescribeDefaultParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeDefaultParametersPaginateResponseTypeDef",
    {"Parameters": List[DescribeDefaultParametersPaginateResponseParametersTypeDef]},
    total=False,
)


class DescribeDefaultParametersPaginateResponseTypeDef(
    _DescribeDefaultParametersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of parameters. Each element in the list represents one parameter.
        - *(dict) --*

          Describes an individual setting that controls some aspect of DAX behavior.
          - **ParameterName** *(string) --*

            The name of the parameter.
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(_DescribeEventsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseEventsTypeDef",
    {
        "SourceName": str,
        "SourceType": Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"],
        "Message": str,
        "Date": datetime,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(_DescribeEventsPaginateResponseEventsTypeDef):
    """
    - *(dict) --*

      Represents a single occurrence of something interesting within the system. Some examples of
      events are creating a DAX cluster, adding or removing a node, or rebooting a node.
      - **SourceName** *(string) --*

        The source of the event. For example, if the event occurred at the node level, the source
        would be the node ID.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Events** *(list) --*

        An array of events. Each element in the array represents one event.
        - *(dict) --*

          Represents a single occurrence of something interesting within the system. Some examples
          of events are creating a DAX cluster, adding or removing a node, or rebooting a node.
          - **SourceName** *(string) --*

            The source of the event. For example, if the event occurred at the node level, the
            source would be the node ID.
    """


_DescribeParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef = TypedDict(
    "_DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef",
    {"ParameterGroupName": str, "Description": str},
    total=False,
)


class DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef(
    _DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef
):
    """
    - *(dict) --*

      A named set of parameters that are applied to all of the nodes in a DAX cluster.
      - **ParameterGroupName** *(string) --*

        The name of the parameter group.
    """


_DescribeParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeParameterGroupsPaginateResponseTypeDef",
    {"ParameterGroups": List[DescribeParameterGroupsPaginateResponseParameterGroupsTypeDef]},
    total=False,
)


class DescribeParameterGroupsPaginateResponseTypeDef(
    _DescribeParameterGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ParameterGroups** *(list) --*

        An array of parameter groups. Each element in the array represents one parameter group.
        - *(dict) --*

          A named set of parameters that are applied to all of the nodes in a DAX cluster.
          - **ParameterGroupName** *(string) --*

            The name of the parameter group.
    """


_DescribeParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeParametersPaginatePaginationConfigTypeDef(
    _DescribeParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef",
    {"NodeType": str, "Value": str},
    total=False,
)


class DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef(
    _DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef
):
    pass


_DescribeParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterType": Literal["DEFAULT", "NODE_TYPE_SPECIFIC"],
        "ParameterValue": str,
        "NodeTypeSpecificValues": List[
            DescribeParametersPaginateResponseParametersNodeTypeSpecificValuesTypeDef
        ],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "ChangeType": Literal["IMMEDIATE", "REQUIRES_REBOOT"],
    },
    total=False,
)


class DescribeParametersPaginateResponseParametersTypeDef(
    _DescribeParametersPaginateResponseParametersTypeDef
):
    """
    - *(dict) --*

      Describes an individual setting that controls some aspect of DAX behavior.
      - **ParameterName** *(string) --*

        The name of the parameter.
    """


_DescribeParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeParametersPaginateResponseTypeDef",
    {"Parameters": List[DescribeParametersPaginateResponseParametersTypeDef]},
    total=False,
)


class DescribeParametersPaginateResponseTypeDef(_DescribeParametersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Parameters** *(list) --*

        A list of parameters within a parameter group. Each element in the list represents one
        parameter.
        - *(dict) --*

          Describes an individual setting that controls some aspect of DAX behavior.
          - **ParameterName** *(string) --*

            The name of the parameter.
    """


_DescribeSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef",
    {"SubnetIdentifier": str, "SubnetAvailabilityZone": str},
    total=False,
)


class DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef(
    _DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef
):
    pass


_DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef = TypedDict(
    "_DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List[DescribeSubnetGroupsPaginateResponseSubnetGroupsSubnetsTypeDef],
    },
    total=False,
)


class DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef(
    _DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef
):
    """
    - *(dict) --*

      Represents the output of one of the following actions:
      * *CreateSubnetGroup*
      * *ModifySubnetGroup*
      - **SubnetGroupName** *(string) --*

        The name of the subnet group.
    """


_DescribeSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeSubnetGroupsPaginateResponseTypeDef",
    {"SubnetGroups": List[DescribeSubnetGroupsPaginateResponseSubnetGroupsTypeDef]},
    total=False,
)


class DescribeSubnetGroupsPaginateResponseTypeDef(_DescribeSubnetGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SubnetGroups** *(list) --*

        An array of subnet groups. Each element in the array represents a single subnet group.
        - *(dict) --*

          Represents the output of one of the following actions:
          * *CreateSubnetGroup*
          * *ModifySubnetGroup*
          - **SubnetGroupName** *(string) --*

            The name of the subnet group.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsPaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagsTypeDef(_ListTagsPaginateResponseTagsTypeDef):
    """
    - *(dict) --*

      A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single
      DAX cluster.
      AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the
      user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
      User-assigned tag names have the prefix ``user:`` .
      You cannot backdate the application of a tag.
      - **Key** *(string) --*

        The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag
        with the same key. If you try to add an existing tag (same key), the existing tag value will
        be updated to the new value.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"Tags": List[ListTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        A list of tags currently associated with the DAX cluster.
        - *(dict) --*

          A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a
          single DAX cluster.
          AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which
          the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50.
          User-assigned tag names have the prefix ``user:`` .
          You cannot backdate the application of a tag.
          - **Key** *(string) --*

            The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one
            tag with the same key. If you try to add an existing tag (same key), the existing tag
            value will be updated to the new value.
    """
