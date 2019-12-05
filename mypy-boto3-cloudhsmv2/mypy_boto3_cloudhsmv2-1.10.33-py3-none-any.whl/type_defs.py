"Main interface for cloudhsmv2 service type defs"
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


ClientCopyBackupToRegionResponseDestinationBackupTypeDef = TypedDict(
    "ClientCopyBackupToRegionResponseDestinationBackupTypeDef",
    {"CreateTimestamp": datetime, "SourceRegion": str, "SourceBackup": str, "SourceCluster": str},
    total=False,
)

ClientCopyBackupToRegionResponseTypeDef = TypedDict(
    "ClientCopyBackupToRegionResponseTypeDef",
    {"DestinationBackup": ClientCopyBackupToRegionResponseDestinationBackupTypeDef},
    total=False,
)

ClientCreateClusterResponseClusterCertificatesTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

ClientCreateClusterResponseClusterHsmsTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientCreateClusterResponseClusterHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientCreateClusterResponseClusterCertificatesTypeDef,
    },
    total=False,
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef",
    {"Cluster": ClientCreateClusterResponseClusterTypeDef},
    total=False,
)

ClientCreateHsmResponseHsmTypeDef = TypedDict(
    "ClientCreateHsmResponseHsmTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientCreateHsmResponseTypeDef = TypedDict(
    "ClientCreateHsmResponseTypeDef", {"Hsm": ClientCreateHsmResponseHsmTypeDef}, total=False
)

ClientDeleteBackupResponseBackupTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)

ClientDeleteBackupResponseTypeDef = TypedDict(
    "ClientDeleteBackupResponseTypeDef",
    {"Backup": ClientDeleteBackupResponseBackupTypeDef},
    total=False,
)

ClientDeleteClusterResponseClusterCertificatesTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

ClientDeleteClusterResponseClusterHsmsTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientDeleteClusterResponseClusterHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientDeleteClusterResponseClusterCertificatesTypeDef,
    },
    total=False,
)

ClientDeleteClusterResponseTypeDef = TypedDict(
    "ClientDeleteClusterResponseTypeDef",
    {"Cluster": ClientDeleteClusterResponseClusterTypeDef},
    total=False,
)

ClientDeleteHsmResponseTypeDef = TypedDict(
    "ClientDeleteHsmResponseTypeDef", {"HsmId": str}, total=False
)

ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsTypeDef",
    {
        "BackupId": str,
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)

ClientDescribeBackupsResponseTypeDef = TypedDict(
    "ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeClustersResponseClustersCertificatesTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

ClientDescribeClustersResponseClustersHsmsTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientDescribeClustersResponseClustersHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientDescribeClustersResponseClustersCertificatesTypeDef,
    },
    total=False,
)

ClientDescribeClustersResponseTypeDef = TypedDict(
    "ClientDescribeClustersResponseTypeDef",
    {"Clusters": List[ClientDescribeClustersResponseClustersTypeDef], "NextToken": str},
    total=False,
)

ClientInitializeClusterResponseTypeDef = TypedDict(
    "ClientInitializeClusterResponseTypeDef",
    {
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientListTagsResponseTagListTypeDef = TypedDict(
    "ClientListTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"TagList": List[ClientListTagsResponseTagListTypeDef], "NextToken": str},
    total=False,
)

ClientRestoreBackupResponseBackupTypeDef = TypedDict(
    "ClientRestoreBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)

ClientRestoreBackupResponseTypeDef = TypedDict(
    "ClientRestoreBackupResponseTypeDef",
    {"Backup": ClientRestoreBackupResponseBackupTypeDef},
    total=False,
)

_RequiredClientTagResourceTagListTypeDef = TypedDict(
    "_RequiredClientTagResourceTagListTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagListTypeDef = TypedDict(
    "_OptionalClientTagResourceTagListTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagListTypeDef(
    _RequiredClientTagResourceTagListTypeDef, _OptionalClientTagResourceTagListTypeDef
):
    pass


DescribeBackupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeBackupsPaginateResponseBackupsTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsTypeDef",
    {
        "BackupId": str,
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)

DescribeBackupsPaginateResponseTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseTypeDef",
    {"Backups": List[DescribeBackupsPaginateResponseBackupsTypeDef]},
    total=False,
)

DescribeClustersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeClustersPaginateResponseClustersCertificatesTypeDef = TypedDict(
    "DescribeClustersPaginateResponseClustersCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

DescribeClustersPaginateResponseClustersHsmsTypeDef = TypedDict(
    "DescribeClustersPaginateResponseClustersHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

DescribeClustersPaginateResponseClustersTypeDef = TypedDict(
    "DescribeClustersPaginateResponseClustersTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[DescribeClustersPaginateResponseClustersHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": DescribeClustersPaginateResponseClustersCertificatesTypeDef,
    },
    total=False,
)

DescribeClustersPaginateResponseTypeDef = TypedDict(
    "DescribeClustersPaginateResponseTypeDef",
    {"Clusters": List[DescribeClustersPaginateResponseClustersTypeDef]},
    total=False,
)

ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTagsPaginateResponseTagListTypeDef = TypedDict(
    "ListTagsPaginateResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ListTagsPaginateResponseTypeDef = TypedDict(
    "ListTagsPaginateResponseTypeDef",
    {"TagList": List[ListTagsPaginateResponseTagListTypeDef]},
    total=False,
)
