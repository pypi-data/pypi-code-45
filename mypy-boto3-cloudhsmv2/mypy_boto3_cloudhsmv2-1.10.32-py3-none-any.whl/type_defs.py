"Main interface for cloudhsmv2 service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCopyBackupToRegionResponseDestinationBackupTypeDef",
    "ClientCopyBackupToRegionResponseTypeDef",
    "ClientCreateClusterResponseClusterCertificatesTypeDef",
    "ClientCreateClusterResponseClusterHsmsTypeDef",
    "ClientCreateClusterResponseClusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateHsmResponseHsmTypeDef",
    "ClientCreateHsmResponseTypeDef",
    "ClientDeleteBackupResponseBackupTypeDef",
    "ClientDeleteBackupResponseTypeDef",
    "ClientDeleteClusterResponseClusterCertificatesTypeDef",
    "ClientDeleteClusterResponseClusterHsmsTypeDef",
    "ClientDeleteClusterResponseClusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteHsmResponseTypeDef",
    "ClientDescribeBackupsResponseBackupsTypeDef",
    "ClientDescribeBackupsResponseTypeDef",
    "ClientDescribeClustersResponseClustersCertificatesTypeDef",
    "ClientDescribeClustersResponseClustersHsmsTypeDef",
    "ClientDescribeClustersResponseClustersTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientInitializeClusterResponseTypeDef",
    "ClientListTagsResponseTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRestoreBackupResponseBackupTypeDef",
    "ClientRestoreBackupResponseTypeDef",
    "ClientTagResourceTagListTypeDef",
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    "DescribeBackupsPaginateResponseBackupsTypeDef",
    "DescribeBackupsPaginateResponseTypeDef",
    "DescribeClustersPaginatePaginationConfigTypeDef",
    "DescribeClustersPaginateResponseClustersCertificatesTypeDef",
    "DescribeClustersPaginateResponseClustersHsmsTypeDef",
    "DescribeClustersPaginateResponseClustersTypeDef",
    "DescribeClustersPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagListTypeDef",
    "ListTagsPaginateResponseTypeDef",
)


_ClientCopyBackupToRegionResponseDestinationBackupTypeDef = TypedDict(
    "_ClientCopyBackupToRegionResponseDestinationBackupTypeDef",
    {"CreateTimestamp": datetime, "SourceRegion": str, "SourceBackup": str, "SourceCluster": str},
    total=False,
)


class ClientCopyBackupToRegionResponseDestinationBackupTypeDef(
    _ClientCopyBackupToRegionResponseDestinationBackupTypeDef
):
    """
    - **DestinationBackup** *(dict) --*

      Information on the backup that will be copied to the destination region, including
      CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the
      destination backup will be the same as that of the source backup.
      You will need to use the ``sourceBackupID`` returned in this operation to use the
      DescribeBackups operation on the backup that will be copied to the destination region.
      - **CreateTimestamp** *(datetime) --*
      - **SourceRegion** *(string) --*
      - **SourceBackup** *(string) --*
      - **SourceCluster** *(string) --*
    """


_ClientCopyBackupToRegionResponseTypeDef = TypedDict(
    "_ClientCopyBackupToRegionResponseTypeDef",
    {"DestinationBackup": ClientCopyBackupToRegionResponseDestinationBackupTypeDef},
    total=False,
)


class ClientCopyBackupToRegionResponseTypeDef(_ClientCopyBackupToRegionResponseTypeDef):
    """
    - *(dict) --*

      - **DestinationBackup** *(dict) --*

        Information on the backup that will be copied to the destination region, including
        CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the
        destination backup will be the same as that of the source backup.
        You will need to use the ``sourceBackupID`` returned in this operation to use the
        DescribeBackups operation on the backup that will be copied to the destination region.
        - **CreateTimestamp** *(datetime) --*
        - **SourceRegion** *(string) --*
        - **SourceBackup** *(string) --*
        - **SourceCluster** *(string) --*
    """


_ClientCreateClusterResponseClusterCertificatesTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)


class ClientCreateClusterResponseClusterCertificatesTypeDef(
    _ClientCreateClusterResponseClusterCertificatesTypeDef
):
    pass


_ClientCreateClusterResponseClusterHsmsTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterHsmsTypeDef",
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


class ClientCreateClusterResponseClusterHsmsTypeDef(_ClientCreateClusterResponseClusterHsmsTypeDef):
    pass


_ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "_ClientCreateClusterResponseClusterTypeDef",
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


class ClientCreateClusterResponseClusterTypeDef(_ClientCreateClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      Information about the cluster that was created.
      - **BackupPolicy** *(string) --*

        The cluster's backup policy.
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

        Information about the cluster that was created.
        - **BackupPolicy** *(string) --*

          The cluster's backup policy.
    """


_ClientCreateHsmResponseHsmTypeDef = TypedDict(
    "_ClientCreateHsmResponseHsmTypeDef",
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


class ClientCreateHsmResponseHsmTypeDef(_ClientCreateHsmResponseHsmTypeDef):
    """
    - **Hsm** *(dict) --*

      Information about the HSM that was created.
      - **AvailabilityZone** *(string) --*

        The Availability Zone that contains the HSM.
    """


_ClientCreateHsmResponseTypeDef = TypedDict(
    "_ClientCreateHsmResponseTypeDef", {"Hsm": ClientCreateHsmResponseHsmTypeDef}, total=False
)


class ClientCreateHsmResponseTypeDef(_ClientCreateHsmResponseTypeDef):
    """
    - *(dict) --*

      - **Hsm** *(dict) --*

        Information about the HSM that was created.
        - **AvailabilityZone** *(string) --*

          The Availability Zone that contains the HSM.
    """


_ClientDeleteBackupResponseBackupTypeDef = TypedDict(
    "_ClientDeleteBackupResponseBackupTypeDef",
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


class ClientDeleteBackupResponseBackupTypeDef(_ClientDeleteBackupResponseBackupTypeDef):
    """
    - **Backup** *(dict) --*

      Information on the ``Backup`` object deleted.
      - **BackupId** *(string) --*

        The identifier (ID) of the backup.
    """


_ClientDeleteBackupResponseTypeDef = TypedDict(
    "_ClientDeleteBackupResponseTypeDef",
    {"Backup": ClientDeleteBackupResponseBackupTypeDef},
    total=False,
)


class ClientDeleteBackupResponseTypeDef(_ClientDeleteBackupResponseTypeDef):
    """
    - *(dict) --*

      - **Backup** *(dict) --*

        Information on the ``Backup`` object deleted.
        - **BackupId** *(string) --*

          The identifier (ID) of the backup.
    """


_ClientDeleteClusterResponseClusterCertificatesTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)


class ClientDeleteClusterResponseClusterCertificatesTypeDef(
    _ClientDeleteClusterResponseClusterCertificatesTypeDef
):
    pass


_ClientDeleteClusterResponseClusterHsmsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterHsmsTypeDef",
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


class ClientDeleteClusterResponseClusterHsmsTypeDef(_ClientDeleteClusterResponseClusterHsmsTypeDef):
    pass


_ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "_ClientDeleteClusterResponseClusterTypeDef",
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


class ClientDeleteClusterResponseClusterTypeDef(_ClientDeleteClusterResponseClusterTypeDef):
    """
    - **Cluster** *(dict) --*

      Information about the cluster that was deleted.
      - **BackupPolicy** *(string) --*

        The cluster's backup policy.
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

        Information about the cluster that was deleted.
        - **BackupPolicy** *(string) --*

          The cluster's backup policy.
    """


_ClientDeleteHsmResponseTypeDef = TypedDict(
    "_ClientDeleteHsmResponseTypeDef", {"HsmId": str}, total=False
)


class ClientDeleteHsmResponseTypeDef(_ClientDeleteHsmResponseTypeDef):
    """
    - *(dict) --*

      - **HsmId** *(string) --*

        The identifier (ID) of the HSM that was deleted.
    """


_ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsTypeDef",
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


class ClientDescribeBackupsResponseBackupsTypeDef(_ClientDescribeBackupsResponseBackupsTypeDef):
    """
    - *(dict) --*

      Contains information about a backup of an AWS CloudHSM cluster.
      - **BackupId** *(string) --*

        The identifier (ID) of the backup.
    """


_ClientDescribeBackupsResponseTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeBackupsResponseTypeDef(_ClientDescribeBackupsResponseTypeDef):
    """
    - *(dict) --*

      - **Backups** *(list) --*

        A list of backups.
        - *(dict) --*

          Contains information about a backup of an AWS CloudHSM cluster.
          - **BackupId** *(string) --*

            The identifier (ID) of the backup.
    """


_ClientDescribeClustersResponseClustersCertificatesTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)


class ClientDescribeClustersResponseClustersCertificatesTypeDef(
    _ClientDescribeClustersResponseClustersCertificatesTypeDef
):
    pass


_ClientDescribeClustersResponseClustersHsmsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersHsmsTypeDef",
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


class ClientDescribeClustersResponseClustersHsmsTypeDef(
    _ClientDescribeClustersResponseClustersHsmsTypeDef
):
    pass


_ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "_ClientDescribeClustersResponseClustersTypeDef",
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


class ClientDescribeClustersResponseClustersTypeDef(_ClientDescribeClustersResponseClustersTypeDef):
    """
    - *(dict) --*

      Contains information about an AWS CloudHSM cluster.
      - **BackupPolicy** *(string) --*

        The cluster's backup policy.
    """


_ClientDescribeClustersResponseTypeDef = TypedDict(
    "_ClientDescribeClustersResponseTypeDef",
    {"Clusters": List[ClientDescribeClustersResponseClustersTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeClustersResponseTypeDef(_ClientDescribeClustersResponseTypeDef):
    """
    - *(dict) --*

      - **Clusters** *(list) --*

        A list of clusters.
        - *(dict) --*

          Contains information about an AWS CloudHSM cluster.
          - **BackupPolicy** *(string) --*

            The cluster's backup policy.
    """


_ClientInitializeClusterResponseTypeDef = TypedDict(
    "_ClientInitializeClusterResponseTypeDef",
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


class ClientInitializeClusterResponseTypeDef(_ClientInitializeClusterResponseTypeDef):
    """
    - *(dict) --*

      - **State** *(string) --*

        The cluster's state.
    """


_ClientListTagsResponseTagListTypeDef = TypedDict(
    "_ClientListTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagListTypeDef(_ClientListTagsResponseTagListTypeDef):
    """
    - *(dict) --*

      Contains a tag. A tag is a key-value pair.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"TagList": List[ClientListTagsResponseTagListTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      - **TagList** *(list) --*

        A list of tags.
        - *(dict) --*

          Contains a tag. A tag is a key-value pair.
          - **Key** *(string) --*

            The key of the tag.
    """


_ClientRestoreBackupResponseBackupTypeDef = TypedDict(
    "_ClientRestoreBackupResponseBackupTypeDef",
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


class ClientRestoreBackupResponseBackupTypeDef(_ClientRestoreBackupResponseBackupTypeDef):
    """
    - **Backup** *(dict) --*

      Information on the ``Backup`` object created.
      - **BackupId** *(string) --*

        The identifier (ID) of the backup.
    """


_ClientRestoreBackupResponseTypeDef = TypedDict(
    "_ClientRestoreBackupResponseTypeDef",
    {"Backup": ClientRestoreBackupResponseBackupTypeDef},
    total=False,
)


class ClientRestoreBackupResponseTypeDef(_ClientRestoreBackupResponseTypeDef):
    """
    - *(dict) --*

      - **Backup** *(dict) --*

        Information on the ``Backup`` object created.
        - **BackupId** *(string) --*

          The identifier (ID) of the backup.
    """


_RequiredClientTagResourceTagListTypeDef = TypedDict(
    "_RequiredClientTagResourceTagListTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagListTypeDef = TypedDict(
    "_OptionalClientTagResourceTagListTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagListTypeDef(
    _RequiredClientTagResourceTagListTypeDef, _OptionalClientTagResourceTagListTypeDef
):
    """
    - *(dict) --*

      Contains a tag. A tag is a key-value pair.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_DescribeBackupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeBackupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeBackupsPaginatePaginationConfigTypeDef(
    _DescribeBackupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeBackupsPaginateResponseBackupsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsTypeDef",
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


class DescribeBackupsPaginateResponseBackupsTypeDef(_DescribeBackupsPaginateResponseBackupsTypeDef):
    """
    - *(dict) --*

      Contains information about a backup of an AWS CloudHSM cluster.
      - **BackupId** *(string) --*

        The identifier (ID) of the backup.
    """


_DescribeBackupsPaginateResponseTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseTypeDef",
    {"Backups": List[DescribeBackupsPaginateResponseBackupsTypeDef]},
    total=False,
)


class DescribeBackupsPaginateResponseTypeDef(_DescribeBackupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Backups** *(list) --*

        A list of backups.
        - *(dict) --*

          Contains information about a backup of an AWS CloudHSM cluster.
          - **BackupId** *(string) --*

            The identifier (ID) of the backup.
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


_DescribeClustersPaginateResponseClustersCertificatesTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)


class DescribeClustersPaginateResponseClustersCertificatesTypeDef(
    _DescribeClustersPaginateResponseClustersCertificatesTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersHsmsTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersHsmsTypeDef",
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


class DescribeClustersPaginateResponseClustersHsmsTypeDef(
    _DescribeClustersPaginateResponseClustersHsmsTypeDef
):
    pass


_DescribeClustersPaginateResponseClustersTypeDef = TypedDict(
    "_DescribeClustersPaginateResponseClustersTypeDef",
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


class DescribeClustersPaginateResponseClustersTypeDef(
    _DescribeClustersPaginateResponseClustersTypeDef
):
    """
    - *(dict) --*

      Contains information about an AWS CloudHSM cluster.
      - **BackupPolicy** *(string) --*

        The cluster's backup policy.
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

        A list of clusters.
        - *(dict) --*

          Contains information about an AWS CloudHSM cluster.
          - **BackupPolicy** *(string) --*

            The cluster's backup policy.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsPaginateResponseTagListTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagListTypeDef(_ListTagsPaginateResponseTagListTypeDef):
    """
    - *(dict) --*

      Contains a tag. A tag is a key-value pair.
      - **Key** *(string) --*

        The key of the tag.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"TagList": List[ListTagsPaginateResponseTagListTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TagList** *(list) --*

        A list of tags.
        - *(dict) --*

          Contains a tag. A tag is a key-value pair.
          - **Key** *(string) --*

            The key of the tag.
    """
