"Main interface for kafka service type defs"
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


ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)

ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef",
    {"EbsStorageInfo": ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef},
    total=False,
)

ClientCreateClusterBrokerNodeGroupInfoTypeDef = TypedDict(
    "ClientCreateClusterBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)

ClientCreateClusterClientAuthenticationTlsTypeDef = TypedDict(
    "ClientCreateClusterClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)

ClientCreateClusterClientAuthenticationTypeDef = TypedDict(
    "ClientCreateClusterClientAuthenticationTypeDef",
    {"Tls": ClientCreateClusterClientAuthenticationTlsTypeDef},
    total=False,
)

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
    pass


ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef", {"DataVolumeKMSKeyId": str}
)

ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

ClientCreateClusterEncryptionInfoTypeDef = TypedDict(
    "ClientCreateClusterEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
    },
    total=False,
)

ClientCreateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientCreateConfigurationResponseTypeDef = TypedDict(
    "ClientCreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": ClientCreateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)

ClientDeleteClusterResponseTypeDef = TypedDict(
    "ClientDeleteClusterResponseTypeDef",
    {"ClusterArn": str, "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"]},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef",
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

ClientDescribeClusterOperationResponseTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseTypeDef",
    {"ClusterOperationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef},
    total=False,
)

ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)

ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)

ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)

ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)

ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef",
    {"Tls": ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef},
    total=False,
)

ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)

ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)

ClientDescribeClusterResponseClusterInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoTypeDef",
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

ClientDescribeClusterResponseTypeDef = TypedDict(
    "ClientDescribeClusterResponseTypeDef",
    {"ClusterInfo": ClientDescribeClusterResponseClusterInfoTypeDef},
    total=False,
)

ClientDescribeConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientDescribeConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationResponseTypeDef",
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

ClientDescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
    },
    total=False,
)

ClientGetBootstrapBrokersResponseTypeDef = TypedDict(
    "ClientGetBootstrapBrokersResponseTypeDef",
    {"BootstrapBrokerString": str, "BootstrapBrokerStringTls": str},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTypeDef",
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

ClientListClusterOperationsResponseTypeDef = TypedDict(
    "ClientListClusterOperationsResponseTypeDef",
    {
        "ClusterOperationInfoList": List[
            ClientListClusterOperationsResponseClusterOperationInfoListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)

ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)

ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)

ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)

ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef",
    {"Tls": ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef},
    total=False,
)

ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)

ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)

ClientListClustersResponseClusterInfoListTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListTypeDef",
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

ClientListClustersResponseTypeDef = TypedDict(
    "ClientListClustersResponseTypeDef",
    {"ClusterInfoList": List[ClientListClustersResponseClusterInfoListTypeDef], "NextToken": str},
    total=False,
)

ClientListConfigurationRevisionsResponseRevisionsTypeDef = TypedDict(
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ClientListConfigurationRevisionsResponseTypeDef",
    {"NextToken": str, "Revisions": List[ClientListConfigurationRevisionsResponseRevisionsTypeDef]},
    total=False,
)

ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientListConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "ClientListConfigurationsResponseConfigurationsTypeDef",
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

ClientListConfigurationsResponseTypeDef = TypedDict(
    "ClientListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ClientListConfigurationsResponseConfigurationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef = TypedDict(
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef",
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

ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef = TypedDict(
    "ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)

ClientListNodesResponseNodeInfoListTypeDef = TypedDict(
    "ClientListNodesResponseNodeInfoListTypeDef",
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

ClientListNodesResponseTypeDef = TypedDict(
    "ClientListNodesResponseTypeDef",
    {"NextToken": str, "NodeInfoList": List[ClientListNodesResponseNodeInfoListTypeDef]},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUpdateBrokerCountResponseTypeDef = TypedDict(
    "ClientUpdateBrokerCountResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

ClientUpdateBrokerStorageResponseTypeDef = TypedDict(
    "ClientUpdateBrokerStorageResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

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
    pass


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
    pass


ClientUpdateClusterConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateClusterConfigurationResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

ListClusterOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListClusterOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseClusterOperationInfoListErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)

ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)

ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ListClusterOperationsPaginateResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
    },
    total=False,
)

ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef",
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

ListClusterOperationsPaginateResponseTypeDef = TypedDict(
    "ListClusterOperationsPaginateResponseTypeDef",
    {
        "ClusterOperationInfoList": List[
            ListClusterOperationsPaginateResponseClusterOperationInfoListTypeDef
        ]
    },
    total=False,
)

ListClustersPaginatePaginationConfigTypeDef = TypedDict(
    "ListClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)

ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)

ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ListClustersPaginateResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)

ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)

ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListClientAuthenticationTypeDef",
    {"Tls": ListClustersPaginateResponseClusterInfoListClientAuthenticationTlsTypeDef},
    total=False,
)

ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)

ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ListClustersPaginateResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)

ListClustersPaginateResponseClusterInfoListTypeDef = TypedDict(
    "ListClustersPaginateResponseClusterInfoListTypeDef",
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

ListClustersPaginateResponseTypeDef = TypedDict(
    "ListClustersPaginateResponseTypeDef",
    {"ClusterInfoList": List[ListClustersPaginateResponseClusterInfoListTypeDef]},
    total=False,
)

ListConfigurationRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListConfigurationRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListConfigurationRevisionsPaginateResponseRevisionsTypeDef = TypedDict(
    "ListConfigurationRevisionsPaginateResponseRevisionsTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ListConfigurationRevisionsPaginateResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsPaginateResponseTypeDef",
    {"Revisions": List[ListConfigurationRevisionsPaginateResponseRevisionsTypeDef]},
    total=False,
)

ListConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "ListConfigurationsPaginateResponseConfigurationsLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ListConfigurationsPaginateResponseConfigurationsTypeDef = TypedDict(
    "ListConfigurationsPaginateResponseConfigurationsTypeDef",
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

ListConfigurationsPaginateResponseTypeDef = TypedDict(
    "ListConfigurationsPaginateResponseTypeDef",
    {"Configurations": List[ListConfigurationsPaginateResponseConfigurationsTypeDef]},
    total=False,
)

ListNodesPaginatePaginationConfigTypeDef = TypedDict(
    "ListNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "ListNodesPaginateResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef = TypedDict(
    "ListNodesPaginateResponseNodeInfoListBrokerNodeInfoTypeDef",
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

ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef = TypedDict(
    "ListNodesPaginateResponseNodeInfoListZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)

ListNodesPaginateResponseNodeInfoListTypeDef = TypedDict(
    "ListNodesPaginateResponseNodeInfoListTypeDef",
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

ListNodesPaginateResponseTypeDef = TypedDict(
    "ListNodesPaginateResponseTypeDef",
    {"NodeInfoList": List[ListNodesPaginateResponseNodeInfoListTypeDef]},
    total=False,
)
