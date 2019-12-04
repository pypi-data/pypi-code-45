"Main interface for kafka service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientCreateClusterBrokerNodeGroupInfoTypeDef",
    "ClientCreateClusterClientAuthenticationTlsTypeDef",
    "ClientCreateClusterClientAuthenticationTypeDef",
    "ClientCreateClusterConfigurationInfoTypeDef",
    "ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef",
    "ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef",
    "ClientCreateClusterEncryptionInfoTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    "ClientCreateConfigurationResponseTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef",
    "ClientDescribeClusterOperationResponseTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef",
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef",
    "ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    "ClientDescribeConfigurationResponseTypeDef",
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    "ClientGetBootstrapBrokersResponseTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTypeDef",
    "ClientListClusterOperationsResponseTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    "ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef",
    "ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef",
    "ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef",
    "ClientListClustersResponseClusterInfoListTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    "ClientListConfigurationRevisionsResponseTypeDef",
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    "ClientListConfigurationsResponseConfigurationsTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef",
    "ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef",
    "ClientListNodesResponseNodeInfoListTypeDef",
    "ClientListNodesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateBrokerCountResponseTypeDef",
    "ClientUpdateBrokerStorageResponseTypeDef",
    "ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef",
    "ClientUpdateClusterConfigurationConfigurationInfoTypeDef",
    "ClientUpdateClusterConfigurationResponseTypeDef",
    "ListClusterOperationsPaginatePaginationConfigTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef",
    "ListClusterOperationsPaginateResponseTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef",
    "ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef",
    "ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef",
    "ListClustersPaginateResponseClusterInfoListTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListConfigurationRevisionsPaginatePaginationConfigTypeDef",
    "ListConfigurationRevisionsPaginateResponseRevisionsTypeDef",
    "ListConfigurationRevisionsPaginateResponseTypeDef",
    "ListConfigurationsPaginatePaginationConfigTypeDef",
    "ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef",
    "ListConfigurationsPaginateResponseConfigurationsTypeDef",
    "ListConfigurationsPaginateResponseTypeDef",
    "ListNodesPaginatePaginationConfigTypeDef",
    "ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    "ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef",
    "ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef",
    "ListNodesPaginateResponseNodeInfoListTypeDef",
    "ListNodesPaginateResponseTypeDef",
)


_ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "_ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)


class ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef(
    _ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
):
    pass


_ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "_ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef",
    {"EbsStorageInfo": ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef},
    total=False,
)


class ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef(
    _ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef
):
    pass


_ClientCreateClusterBrokerNodeGroupInfoTypeDef = TypedDict(
    "_ClientCreateClusterBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)


class ClientCreateClusterBrokerNodeGroupInfoTypeDef(_ClientCreateClusterBrokerNodeGroupInfoTypeDef):
    """
    Information about the broker nodes in the cluster.
    - **BrokerAZDistribution** *(string) --*

      The distribution of broker nodes across Availability Zones. This is an optional parameter. If
      you don't specify it, Amazon MSK gives it the value DEFAULT. You can also explicitly set this
      parameter to the value DEFAULT. No other values are currently allowed.
      Amazon MSK distributes the broker nodes evenly across the Availability Zones that correspond
      to the subnets you provide when you create the cluster.
    """


_ClientCreateClusterClientAuthenticationTlsTypeDef = TypedDict(
    "_ClientCreateClusterClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)


class ClientCreateClusterClientAuthenticationTlsTypeDef(
    _ClientCreateClusterClientAuthenticationTlsTypeDef
):
    """
    - **Tls** *(dict) --*

      Details for ClientAuthentication using TLS.
      - **CertificateAuthorityArnList** *(list) --*

        List of ACM Certificate Authority ARNs.
        - *(string) --*
    """


_ClientCreateClusterClientAuthenticationTypeDef = TypedDict(
    "_ClientCreateClusterClientAuthenticationTypeDef",
    {"Tls": ClientCreateClusterClientAuthenticationTlsTypeDef},
    total=False,
)


class ClientCreateClusterClientAuthenticationTypeDef(
    _ClientCreateClusterClientAuthenticationTypeDef
):
    """
    Includes all client authentication related information.
    - **Tls** *(dict) --*

      Details for ClientAuthentication using TLS.
      - **CertificateAuthorityArnList** *(list) --*

        List of ACM Certificate Authority ARNs.
        - *(string) --*
    """


_RequiredClientCreateClusterConfigurationInfoTypeDef = TypedDict(
    "_RequiredClientCreateClusterConfigurationInfoTypeDef", {"Arn": str}
)
_OptionalClientCreateClusterConfigurationInfoTypeDef = TypedDict(
    "_OptionalClientCreateClusterConfigurationInfoTypeDef", {"Revision": int}, total=False
)


class ClientCreateClusterConfigurationInfoTypeDef(
    _RequiredClientCreateClusterConfigurationInfoTypeDef,
    _OptionalClientCreateClusterConfigurationInfoTypeDef,
):
    """
    Represents the configuration that you want MSK to use for the brokers in a cluster.
    - **Arn** *(string) --***[REQUIRED]**

      ARN of the configuration to use.
    """


_ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "_ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef", {"DataVolumeKMSKeyId": str}
)


class ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef(
    _ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef
):
    """
    - **EncryptionAtRest** *(dict) --*

      The data-volume encryption details.
      - **DataVolumeKMSKeyId** *(string) --***[REQUIRED]**

        The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key, MSK
        creates one for you and uses it.
    """


_ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "_ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)


class ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef(
    _ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef
):
    pass


_ClientCreateClusterEncryptionInfoTypeDef = TypedDict(
    "_ClientCreateClusterEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)


class ClientCreateClusterEncryptionInfoTypeDef(_ClientCreateClusterEncryptionInfoTypeDef):
    """
    Includes all encryption-related information.
    - **EncryptionAtRest** *(dict) --*

      The data-volume encryption details.
      - **DataVolumeKMSKeyId** *(string) --***[REQUIRED]**

        The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key, MSK
        creates one for you and uses it.
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
    },
    total=False,
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) of the cluster.
    """


_ClientCreateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientCreateConfigurationResponseLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientCreateConfigurationResponseLatestRevisionTypeDef(
    _ClientCreateConfigurationResponseLatestRevisionTypeDef
):
    pass


_ClientCreateConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": ClientCreateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ClientCreateConfigurationResponseTypeDef(_ClientCreateConfigurationResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration.
    """


_ClientDeleteClusterResponseTypeDef = TypedDict(
    "_ClientDeleteClusterResponseTypeDef",
    {"ClusterArn": str, "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"]},
    total=False,
)


class ClientDeleteClusterResponseTypeDef(_ClientDeleteClusterResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) of the cluster.
    """


_ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef
):
    pass


_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef
):
    pass


_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef
):
    pass


_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef
):
    pass


_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef
):
    pass


_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef
):
    pass


_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef
):
    pass


_ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef,
        "TargetClusterInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef,
    },
    total=False,
)


class ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef(
    _ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef
):
    """
    - **ClusterOperationInfo** *(dict) --*

      Cluster operation information
      - **ClientRequestId** *(string) --*

        The ID of the API request that triggered this operation.
    """


_ClientDescribeClusterOperationResponseTypeDef = TypedDict(
    "_ClientDescribeClusterOperationResponseTypeDef",
    {"ClusterOperationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef},
    total=False,
)


class ClientDescribeClusterOperationResponseTypeDef(_ClientDescribeClusterOperationResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **ClusterOperationInfo** *(dict) --*

        Cluster operation information
        - **ClientRequestId** *(string) --*

          The ID of the API request that triggered this operation.
    """


_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)


class ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef(
    _ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef",
    {"Tls": ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef(
    _ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef(
    _ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)


class ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef(
    _ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef
):
    pass


_ClientDescribeClusterResponseClusterInfoTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterInfoTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "NumberOfBrokerNodes": int,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterInfoTypeDef(
    _ClientDescribeClusterResponseClusterInfoTypeDef
):
    """
    - **ClusterInfo** *(dict) --*

      The cluster information.
      - **ActiveOperationArn** *(string) --*

        Arn of active cluster operation.
    """


_ClientDescribeClusterResponseTypeDef = TypedDict(
    "_ClientDescribeClusterResponseTypeDef",
    {"ClusterInfo": ClientDescribeClusterResponseClusterInfoTypeDef},
    total=False,
)


class ClientDescribeClusterResponseTypeDef(_ClientDescribeClusterResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **ClusterInfo** *(dict) --*

        The cluster information.
        - **ActiveOperationArn** *(string) --*

          Arn of active cluster operation.
    """


_ClientDescribeConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientDescribeConfigurationResponseLatestRevisionTypeDef(
    _ClientDescribeConfigurationResponseLatestRevisionTypeDef
):
    pass


_ClientDescribeConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ClientDescribeConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ClientDescribeConfigurationResponseTypeDef(_ClientDescribeConfigurationResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration.
    """


_ClientDescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
    },
    total=False,
)


class ClientDescribeConfigurationRevisionResponseTypeDef(
    _ClientDescribeConfigurationRevisionResponseTypeDef
):
    """
    - *(dict) --*

      200 response
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration.
    """


_ClientGetBootstrapBrokersResponseTypeDef = TypedDict(
    "_ClientGetBootstrapBrokersResponseTypeDef",
    {"BootstrapBrokerString": str, "BootstrapBrokerStringTls": str},
    total=False,
)


class ClientGetBootstrapBrokersResponseTypeDef(_ClientGetBootstrapBrokersResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **BootstrapBrokerString** *(string) --*

        A string containing one or more hostname:port pairs.
    """


_ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef
):
    pass


_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
):
    pass


_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef
):
    pass


_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef
):
    pass


_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
):
    pass


_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef
):
    pass


_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef
):
    pass


_ClientListClusterOperationsResponseClusterOperationInfoListTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseClusterOperationInfoListTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef,
        "TargetClusterInfo": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef,
    },
    total=False,
)


class ClientListClusterOperationsResponseClusterOperationInfoListTypeDef(
    _ClientListClusterOperationsResponseClusterOperationInfoListTypeDef
):
    """
    - *(dict) --*

      Returns information about a cluster operation.
      - **ClientRequestId** *(string) --*

        The ID of the API request that triggered this operation.
    """


_ClientListClusterOperationsResponseTypeDef = TypedDict(
    "_ClientListClusterOperationsResponseTypeDef",
    {
        "ClusterOperationInfoList": List[
            ClientListClusterOperationsResponseClusterOperationInfoListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListClusterOperationsResponseTypeDef(_ClientListClusterOperationsResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **ClusterOperationInfoList** *(list) --*

        An array of cluster operation information objects.
        - *(dict) --*

          Returns information about a cluster operation.
          - **ClientRequestId** *(string) --*

            The ID of the API request that triggered this operation.
    """


_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)


class ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef(
    _ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)


class ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef(
    _ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)


class ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef(
    _ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)


class ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef(
    _ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef",
    {"Tls": ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef},
    total=False,
)


class ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef(
    _ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef(
    _ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)


class ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef(
    _ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)


class ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef(
    _ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)


class ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef(
    _ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef
):
    pass


_ClientListClustersResponseClusterInfoListTypeDef = TypedDict(
    "_ClientListClustersResponseClusterInfoListTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "NumberOfBrokerNodes": int,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)


class ClientListClustersResponseClusterInfoListTypeDef(
    _ClientListClustersResponseClusterInfoListTypeDef
):
    """
    - *(dict) --*

      Returns information about a cluster.
      - **ActiveOperationArn** *(string) --*

        Arn of active cluster operation.
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef",
    {"ClusterInfoList": List[ClientListClustersResponseClusterInfoListTypeDef], "NextToken": str},
    total=False,
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **ClusterInfoList** *(list) --*

        Information on each of the MSK clusters in the response.
        - *(dict) --*

          Returns information about a cluster.
          - **ActiveOperationArn** *(string) --*

            Arn of active cluster operation.
    """


_ClientListConfigurationRevisionsResponseRevisionsTypeDef = TypedDict(
    "_ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientListConfigurationRevisionsResponseRevisionsTypeDef(
    _ClientListConfigurationRevisionsResponseRevisionsTypeDef
):
    pass


_ClientListConfigurationRevisionsResponseTypeDef = TypedDict(
    "_ClientListConfigurationRevisionsResponseTypeDef",
    {"NextToken": str, "Revisions": List[ClientListConfigurationRevisionsResponseRevisionsTypeDef]},
    total=False,
)


class ClientListConfigurationRevisionsResponseTypeDef(
    _ClientListConfigurationRevisionsResponseTypeDef
):
    """
    - *(dict) --*

      200 response
      - **NextToken** *(string) --*

        Paginated results marker.
    """


_ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "_ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef(
    _ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef
):
    pass


_ClientListConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "_ClientListConfigurationsResponseConfigurationsTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ClientListConfigurationsResponseConfigurationsTypeDef(
    _ClientListConfigurationsResponseConfigurationsTypeDef
):
    """
    - *(dict) --*

      Represents an MSK Configuration.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration.
    """


_ClientListConfigurationsResponseTypeDef = TypedDict(
    "_ClientListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ClientListConfigurationsResponseConfigurationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListConfigurationsResponseTypeDef(_ClientListConfigurationsResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **Configurations** *(list) --*

        An array of MSK configurations.
        - *(dict) --*

          Represents an MSK Configuration.
          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the configuration.
    """


_ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef(
    _ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef
):
    pass


_ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef = TypedDict(
    "_ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef,
        "Endpoints": List[str],
    },
    total=False,
)


class ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef(
    _ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef
):
    pass


_ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef = TypedDict(
    "_ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)


class ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef(
    _ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef
):
    pass


_ClientListNodesResponseNodeInfoListTypeDef = TypedDict(
    "_ClientListNodesResponseNodeInfoListTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef,
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": str,
        "ZookeeperNodeInfo": ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef,
    },
    total=False,
)


class ClientListNodesResponseNodeInfoListTypeDef(_ClientListNodesResponseNodeInfoListTypeDef):
    pass


_ClientListNodesResponseTypeDef = TypedDict(
    "_ClientListNodesResponseTypeDef",
    {"NextToken": str, "NodeInfoList": List[ClientListNodesResponseNodeInfoListTypeDef]},
    total=False,
)


class ClientListNodesResponseTypeDef(_ClientListNodesResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **NextToken** *(string) --*

        The paginated results marker. When the result of a ListNodes operation is truncated, the
        call returns NextToken in the response. To get another batch of nodes, provide this token in
        your next request.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      Success response.
      - **Tags** *(dict) --*

        The key-value pair for the resource tag.
        - *(string) --*

          - *(string) --*
    """


_ClientUpdateBrokerCountResponseTypeDef = TypedDict(
    "_ClientUpdateBrokerCountResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)


class ClientUpdateBrokerCountResponseTypeDef(_ClientUpdateBrokerCountResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) of the cluster.
    """


_ClientUpdateBrokerStorageResponseTypeDef = TypedDict(
    "_ClientUpdateBrokerStorageResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)


class ClientUpdateBrokerStorageResponseTypeDef(_ClientUpdateBrokerStorageResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) of the cluster.
    """


_RequiredClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_RequiredClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef", {"KafkaBrokerNodeId": str}
)
_OptionalClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_OptionalClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef",
    {"VolumeSizeGB": int},
    total=False,
)


class ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef(
    _RequiredClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef,
    _OptionalClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef,
):
    """
    - *(dict) --*

      Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword
      ALL. This means the changes apply to all the brokers in the cluster.
      - **KafkaBrokerNodeId** *(string) --***[REQUIRED]**

        The ID of the broker to update.
    """


_RequiredClientUpdateClusterConfigurationConfigurationInfoTypeDef = TypedDict(
    "_RequiredClientUpdateClusterConfigurationConfigurationInfoTypeDef", {"Arn": str}
)
_OptionalClientUpdateClusterConfigurationConfigurationInfoTypeDef = TypedDict(
    "_OptionalClientUpdateClusterConfigurationConfigurationInfoTypeDef",
    {"Revision": int},
    total=False,
)


class ClientUpdateClusterConfigurationConfigurationInfoTypeDef(
    _RequiredClientUpdateClusterConfigurationConfigurationInfoTypeDef,
    _OptionalClientUpdateClusterConfigurationConfigurationInfoTypeDef,
):
    """
    Represents the configuration that you want MSK to use for the brokers in a cluster.
    - **Arn** *(string) --***[REQUIRED]**

      ARN of the configuration to use.
    """


_ClientUpdateClusterConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateClusterConfigurationResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)


class ClientUpdateClusterConfigurationResponseTypeDef(
    _ClientUpdateClusterConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      Successful response.
      - **ClusterArn** *(string) --*

        The Amazon Resource Name (ARN) of the cluster.
    """


_ListClusterOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClusterOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClusterOperationsPaginatePaginationConfigTypeDef(
    _ListClusterOperationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef
):
    pass


_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
):
    pass


_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef
):
    pass


_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef
):
    pass


_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
):
    pass


_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef
):
    pass


_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef
):
    pass


_ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef,
        "TargetClusterInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef,
    },
    total=False,
)


class ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef(
    _ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef
):
    """
    - *(dict) --*

      Returns information about a cluster operation.
      - **ClientRequestId** *(string) --*

        The ID of the API request that triggered this operation.
    """


_ListClusterOperationsPaginateResponseTypeDef = TypedDict(
    "_ListClusterOperationsPaginateResponseTypeDef",
    {
        "ClusterOperationInfoList": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef
        ]
    },
    total=False,
)


class ListClusterOperationsPaginateResponseTypeDef(_ListClusterOperationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **ClusterOperationInfoList** *(list) --*

        An array of cluster operation information objects.
        - *(dict) --*

          Returns information about a cluster operation.
          - **ClientRequestId** *(string) --*

            The ID of the API request that triggered this operation.
    """


_ListClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClustersPaginatePaginationConfigTypeDef(_ListClustersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)


class ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)


class ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef(
    _ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef",
    {"Tls": ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef(
    _ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef(
    _ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)


class ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef(
    _ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)


class ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef(
    _ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef
):
    pass


_ListClustersPaginateResponseClusterInfoListTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterInfoListTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "NumberOfBrokerNodes": int,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)


class ListClustersPaginateResponseClusterInfoListTypeDef(
    _ListClustersPaginateResponseClusterInfoListTypeDef
):
    """
    - *(dict) --*

      Returns information about a cluster.
      - **ActiveOperationArn** *(string) --*

        Arn of active cluster operation.
    """


_ListClustersPaginateResponseTypeDef = TypedDict(
    "_ListClustersPaginateResponseTypeDef",
    {"ClusterInfoList": List[ListClustersPaginateResponseClusterInfoListTypeDef]},
    total=False,
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **ClusterInfoList** *(list) --*

        Information on each of the MSK clusters in the response.
        - *(dict) --*

          Returns information about a cluster.
          - **ActiveOperationArn** *(string) --*

            Arn of active cluster operation.
    """


_ListConfigurationRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigurationRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigurationRevisionsPaginatePaginationConfigTypeDef(
    _ListConfigurationRevisionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConfigurationRevisionsPaginateResponseRevisionsTypeDef = TypedDict(
    "_ListConfigurationRevisionsPaginateResponseRevisionsTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ListConfigurationRevisionsPaginateResponseRevisionsTypeDef(
    _ListConfigurationRevisionsPaginateResponseRevisionsTypeDef
):
    """
    - *(dict) --*

      Describes a configuration revision.
      - **CreationTime** *(datetime) --*

        The time when the configuration revision was created.
    """


_ListConfigurationRevisionsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationRevisionsPaginateResponseTypeDef",
    {"Revisions": List[ListConfigurationRevisionsPaginateResponseRevisionsTypeDef]},
    total=False,
)


class ListConfigurationRevisionsPaginateResponseTypeDef(
    _ListConfigurationRevisionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      200 response
      - **Revisions** *(list) --*

        List of ConfigurationRevision objects.
        - *(dict) --*

          Describes a configuration revision.
          - **CreationTime** *(datetime) --*

            The time when the configuration revision was created.
    """


_ListConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigurationsPaginatePaginationConfigTypeDef(
    _ListConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "_ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)


class ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef(
    _ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef
):
    pass


_ListConfigurationsPaginateResponseConfigurationsTypeDef = TypedDict(
    "_ListConfigurationsPaginateResponseConfigurationsTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ListConfigurationsPaginateResponseConfigurationsTypeDef(
    _ListConfigurationsPaginateResponseConfigurationsTypeDef
):
    """
    - *(dict) --*

      Represents an MSK Configuration.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the configuration.
    """


_ListConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationsPaginateResponseTypeDef",
    {"Configurations": List[ListConfigurationsPaginateResponseConfigurationsTypeDef]},
    total=False,
)


class ListConfigurationsPaginateResponseTypeDef(_ListConfigurationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **Configurations** *(list) --*

        An array of MSK configurations.
        - *(dict) --*

          Represents an MSK Configuration.
          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the configuration.
    """


_ListNodesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNodesPaginatePaginationConfigTypeDef(_ListNodesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "_ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)


class ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef(
    _ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef
):
    pass


_ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef = TypedDict(
    "_ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef,
        "Endpoints": List[str],
    },
    total=False,
)


class ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef(
    _ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef
):
    pass


_ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef = TypedDict(
    "_ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)


class ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef(
    _ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef
):
    pass


_ListNodesPaginateResponseNodeInfoListTypeDef = TypedDict(
    "_ListNodesPaginateResponseNodeInfoListTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef,
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": str,
        "ZookeeperNodeInfo": ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef,
    },
    total=False,
)


class ListNodesPaginateResponseNodeInfoListTypeDef(_ListNodesPaginateResponseNodeInfoListTypeDef):
    """
    - *(dict) --*

      The node information object.
      - **AddedToClusterTime** *(string) --*

        The start time.
    """


_ListNodesPaginateResponseTypeDef = TypedDict(
    "_ListNodesPaginateResponseTypeDef",
    {"NodeInfoList": List[ListNodesPaginateResponseNodeInfoListTypeDef]},
    total=False,
)


class ListNodesPaginateResponseTypeDef(_ListNodesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Successful response.
      - **NodeInfoList** *(list) --*

        List containing a NodeInfo object.
        - *(dict) --*

          The node information object.
          - **AddedToClusterTime** *(string) --*

            The start time.
    """
