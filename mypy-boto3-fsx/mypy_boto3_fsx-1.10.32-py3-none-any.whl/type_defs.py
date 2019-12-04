"Main interface for fsx service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateBackupResponseBackupDirectoryInformationTypeDef",
    "ClientCreateBackupResponseBackupFailureDetailsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemTagsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemTypeDef",
    "ClientCreateBackupResponseBackupTagsTypeDef",
    "ClientCreateBackupResponseBackupTypeDef",
    "ClientCreateBackupResponseTypeDef",
    "ClientCreateBackupTagsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemTypeDef",
    "ClientCreateFileSystemFromBackupResponseTypeDef",
    "ClientCreateFileSystemFromBackupTagsTypeDef",
    "ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef",
    "ClientCreateFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef",
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemTagsTypeDef",
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemTypeDef",
    "ClientCreateFileSystemResponseTypeDef",
    "ClientCreateFileSystemTagsTypeDef",
    "ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemWindowsConfigurationTypeDef",
    "ClientDeleteBackupResponseTypeDef",
    "ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef",
    "ClientDeleteFileSystemResponseWindowsResponseTypeDef",
    "ClientDeleteFileSystemResponseTypeDef",
    "ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef",
    "ClientDeleteFileSystemWindowsConfigurationTypeDef",
    "ClientDescribeBackupsFiltersTypeDef",
    "ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef",
    "ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemTypeDef",
    "ClientDescribeBackupsResponseBackupsTagsTypeDef",
    "ClientDescribeBackupsResponseBackupsTypeDef",
    "ClientDescribeBackupsResponseTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    "ClientDescribeFileSystemsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateFileSystemLustreConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef",
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemTagsTypeDef",
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemTypeDef",
    "ClientUpdateFileSystemResponseTypeDef",
    "ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientUpdateFileSystemWindowsConfigurationTypeDef",
    "DescribeBackupsPaginateFiltersTypeDef",
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    "DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemTypeDef",
    "DescribeBackupsPaginateResponseBackupsTagsTypeDef",
    "DescribeBackupsPaginateResponseBackupsTypeDef",
    "DescribeBackupsPaginateResponseTypeDef",
    "DescribeFileSystemsPaginatePaginationConfigTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
    "DescribeFileSystemsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
)


_ClientCreateBackupResponseBackupDirectoryInformationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)


class ClientCreateBackupResponseBackupDirectoryInformationTypeDef(
    _ClientCreateBackupResponseBackupDirectoryInformationTypeDef
):
    pass


_ClientCreateBackupResponseBackupFailureDetailsTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFailureDetailsTypeDef", {"Message": str}, total=False
)


class ClientCreateBackupResponseBackupFailureDetailsTypeDef(
    _ClientCreateBackupResponseBackupFailureDetailsTypeDef
):
    pass


_ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef(
    _ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef
):
    pass


_ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    pass


_ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef(
    _ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef
):
    pass


_ClientCreateBackupResponseBackupFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemTagsTypeDef(
    _ClientCreateBackupResponseBackupFileSystemTagsTypeDef
):
    pass


_ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef(
    _ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef
):
    pass


_ClientCreateBackupResponseBackupFileSystemTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateBackupResponseBackupFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemTypeDef(
    _ClientCreateBackupResponseBackupFileSystemTypeDef
):
    pass


_ClientCreateBackupResponseBackupTagsTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateBackupResponseBackupTagsTypeDef(_ClientCreateBackupResponseBackupTagsTypeDef):
    pass


_ClientCreateBackupResponseBackupTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"],
        "FailureDetails": ClientCreateBackupResponseBackupFailureDetailsTypeDef,
        "Type": Literal["AUTOMATIC", "USER_INITIATED"],
        "ProgressPercent": int,
        "CreationTime": datetime,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateBackupResponseBackupTagsTypeDef],
        "FileSystem": ClientCreateBackupResponseBackupFileSystemTypeDef,
        "DirectoryInformation": ClientCreateBackupResponseBackupDirectoryInformationTypeDef,
    },
    total=False,
)


class ClientCreateBackupResponseBackupTypeDef(_ClientCreateBackupResponseBackupTypeDef):
    """
    - **Backup** *(dict) --*

      A description of the backup.
      - **BackupId** *(string) --*

        The ID of the backup.
    """


_ClientCreateBackupResponseTypeDef = TypedDict(
    "_ClientCreateBackupResponseTypeDef",
    {"Backup": ClientCreateBackupResponseBackupTypeDef},
    total=False,
)


class ClientCreateBackupResponseTypeDef(_ClientCreateBackupResponseTypeDef):
    """
    - *(dict) --*

      The response object for the ``CreateBackup`` operation.
      - **Backup** *(dict) --*

        A description of the backup.
        - **BackupId** *(string) --*

          The ID of the backup.
    """


_ClientCreateBackupTagsTypeDef = TypedDict(
    "_ClientCreateBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateBackupTagsTypeDef(_ClientCreateBackupTagsTypeDef):
    """
    - *(dict) --*

      Specifies a key-value pair for a resource tag.
      - **Key** *(string) --*

        A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
        resource to which they are attached.
    """


_ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef
):
    pass


_ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    pass


_ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef
):
    pass


_ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef
):
    pass


_ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef
):
    pass


_ClientCreateFileSystemFromBackupResponseFileSystemTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemTypeDef
):
    """
    - **FileSystem** *(dict) --*

      A description of the file system.
      - **OwnerId** *(string) --*

        The AWS account that created the file system. If the file system was created by an AWS
        Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is
        the owner.
    """


_ClientCreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseTypeDef",
    {"FileSystem": ClientCreateFileSystemFromBackupResponseFileSystemTypeDef},
    total=False,
)


class ClientCreateFileSystemFromBackupResponseTypeDef(
    _ClientCreateFileSystemFromBackupResponseTypeDef
):
    """
    - *(dict) --*

      The response object for the ``CreateFileSystemFromBackup`` operation.
      - **FileSystem** *(dict) --*

        A description of the file system.
        - **OwnerId** *(string) --*

          The AWS account that created the file system. If the file system was created by an AWS
          Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs
          is the owner.
    """


_ClientCreateFileSystemFromBackupTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateFileSystemFromBackupTagsTypeDef(_ClientCreateFileSystemFromBackupTagsTypeDef):
    """
    - *(dict) --*

      Specifies a key-value pair for a resource tag.
      - **Key** *(string) --*

        A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
        resource to which they are attached.
    """


_ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "Password": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "PreferredSubnetId": str,
        "ThroughputCapacity": int,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef
):
    """
    The configuration for this Microsoft Windows file system.
    - **ActiveDirectoryId** *(string) --*

      The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file
      system should join when it's created.
    """


_ClientCreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
    },
    total=False,
)


class ClientCreateFileSystemLustreConfigurationTypeDef(
    _ClientCreateFileSystemLustreConfigurationTypeDef
):
    """
    The Lustre configuration for the file system being created. This value is required if
    ``FileSystemType`` is set to ``LUSTRE`` .
    - **WeeklyMaintenanceStartTime** *(string) --*

      The preferred time to perform weekly maintenance, in the UTC time zone.
    """


_ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)


class ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef(
    _ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef
):
    pass


_ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    pass


_ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef(
    _ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef
):
    pass


_ClientCreateFileSystemResponseFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateFileSystemResponseFileSystemTagsTypeDef(
    _ClientCreateFileSystemResponseFileSystemTagsTypeDef
):
    pass


_ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef(
    _ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef
):
    pass


_ClientCreateFileSystemResponseFileSystemTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateFileSystemResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFileSystemResponseFileSystemTypeDef(
    _ClientCreateFileSystemResponseFileSystemTypeDef
):
    """
    - **FileSystem** *(dict) --*

      The configuration of the file system that was created.
      - **OwnerId** *(string) --*

        The AWS account that created the file system. If the file system was created by an AWS
        Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is
        the owner.
    """


_ClientCreateFileSystemResponseTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseTypeDef",
    {"FileSystem": ClientCreateFileSystemResponseFileSystemTypeDef},
    total=False,
)


class ClientCreateFileSystemResponseTypeDef(_ClientCreateFileSystemResponseTypeDef):
    """
    - *(dict) --*

      The response object returned after the file system is created.
      - **FileSystem** *(dict) --*

        The configuration of the file system that was created.
        - **OwnerId** *(string) --*

          The AWS account that created the file system. If the file system was created by an AWS
          Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs
          is the owner.
    """


_ClientCreateFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateFileSystemTagsTypeDef(_ClientCreateFileSystemTagsTypeDef):
    """
    - *(dict) --*

      Specifies a key-value pair for a resource tag.
      - **Key** *(string) --*

        A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
        resource to which they are attached.
    """


_ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "Password": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "PreferredSubnetId": str,
        "ThroughputCapacity": int,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateFileSystemWindowsConfigurationTypeDef(
    _ClientCreateFileSystemWindowsConfigurationTypeDef
):
    """
    The Microsoft Windows configuration for the file system being created. This value is required if
    ``FileSystemType`` is set to ``WINDOWS`` .
    - **ActiveDirectoryId** *(string) --*

      The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file
      system should join when it's created.
    """


_ClientDeleteBackupResponseTypeDef = TypedDict(
    "_ClientDeleteBackupResponseTypeDef",
    {"BackupId": str, "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"]},
    total=False,
)


class ClientDeleteBackupResponseTypeDef(_ClientDeleteBackupResponseTypeDef):
    """
    - *(dict) --*

      The response object for ``DeleteBackup`` operation.
      - **BackupId** *(string) --*

        The ID of the backup deleted.
    """


_ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef = TypedDict(
    "_ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef(
    _ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef
):
    pass


_ClientDeleteFileSystemResponseWindowsResponseTypeDef = TypedDict(
    "_ClientDeleteFileSystemResponseWindowsResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List[
            ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteFileSystemResponseWindowsResponseTypeDef(
    _ClientDeleteFileSystemResponseWindowsResponseTypeDef
):
    pass


_ClientDeleteFileSystemResponseTypeDef = TypedDict(
    "_ClientDeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "WindowsResponse": ClientDeleteFileSystemResponseWindowsResponseTypeDef,
    },
    total=False,
)


class ClientDeleteFileSystemResponseTypeDef(_ClientDeleteFileSystemResponseTypeDef):
    """
    - *(dict) --*

      The response object for the ``DeleteFileSystem`` operation.
      - **FileSystemId** *(string) --*

        The ID of the file system being deleted.
    """


_ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef = TypedDict(
    "_ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef(
    _ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef
):
    pass


_ClientDeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientDeleteFileSystemWindowsConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List[ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef],
    },
    total=False,
)


class ClientDeleteFileSystemWindowsConfigurationTypeDef(
    _ClientDeleteFileSystemWindowsConfigurationTypeDef
):
    """
    The configuration object for the Microsoft Windows file system used in the ``DeleteFileSystem``
    operation.
    - **SkipFinalBackup** *(boolean) --*

      By default, Amazon FSx for Windows takes a final backup on your behalf when the
      ``DeleteFileSystem`` operation is invoked. Doing this helps protect you from data loss, and we
      highly recommend taking the final backup. If you want to skip this backup, use this flag to do
      so.
    """


_ClientDescribeBackupsFiltersTypeDef = TypedDict(
    "_ClientDescribeBackupsFiltersTypeDef",
    {"Name": Literal["file-system-id", "backup-type"], "Values": List[str]},
    total=False,
)


class ClientDescribeBackupsFiltersTypeDef(_ClientDescribeBackupsFiltersTypeDef):
    """
    - *(dict) --*

      A filter used to restrict the results of describe calls. You can use multiple filters to
      return results that meet all applied filter requirements.
      - **Name** *(string) --*

        The name for this filter.
    """


_ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)


class ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef(
    _ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef", {"Message": str}, total=False
)


class ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef(
    _ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsFileSystemTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsTagsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeBackupsResponseBackupsTagsTypeDef(
    _ClientDescribeBackupsResponseBackupsTagsTypeDef
):
    pass


_ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsTypeDef",
    {
        "BackupId": str,
        "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"],
        "FailureDetails": ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef,
        "Type": Literal["AUTOMATIC", "USER_INITIATED"],
        "ProgressPercent": int,
        "CreationTime": datetime,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeBackupsResponseBackupsTagsTypeDef],
        "FileSystem": ClientDescribeBackupsResponseBackupsFileSystemTypeDef,
        "DirectoryInformation": ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsTypeDef(_ClientDescribeBackupsResponseBackupsTypeDef):
    """
    - *(dict) --*

      A backup of an Amazon FSx for Windows File Server file system. You can create a new file
      system from a backup to protect against data loss.
      - **BackupId** *(string) --*

        The ID of the backup.
    """


_ClientDescribeBackupsResponseTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeBackupsResponseTypeDef(_ClientDescribeBackupsResponseTypeDef):
    """
    - *(dict) --*

      Response object for ``DescribeBackups`` operation.
      - **Backups** *(list) --*

        Any array of backups.
        - *(dict) --*

          A backup of an Amazon FSx for Windows File Server file system. You can create a new file
          system from a backup to protect against data loss.
          - **BackupId** *(string) --*

            The ID of the backup.
    """


_ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef
):
    pass


_ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef
):
    pass


_ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef
):
    pass


_ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef
):
    pass


_ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef
):
    pass


_ClientDescribeFileSystemsResponseFileSystemsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef],
        "WindowsConfiguration": ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsTypeDef
):
    """
    - *(dict) --*

      A description of a specific Amazon FSx file system.
      - **OwnerId** *(string) --*

        The AWS account that created the file system. If the file system was created by an AWS
        Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is
        the owner.
    """


_ClientDescribeFileSystemsResponseTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseTypeDef",
    {"FileSystems": List[ClientDescribeFileSystemsResponseFileSystemsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeFileSystemsResponseTypeDef(_ClientDescribeFileSystemsResponseTypeDef):
    """
    - *(dict) --*

      The response object for ``DescribeFileSystems`` operation.
      - **FileSystems** *(list) --*

        An array of file system descriptions.
        - *(dict) --*

          A description of a specific Amazon FSx file system.
          - **OwnerId** *(string) --*

            The AWS account that created the file system. If the file system was created by an AWS
            Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs
            is the owner.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      Specifies a key-value pair for a resource tag.
      - **Key** *(string) --*

        A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
        resource to which they are attached.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      The response object for ``ListTagsForResource`` operation.
      - **Tags** *(list) --*

        A list of tags on the resource.
        - *(dict) --*

          Specifies a key-value pair for a resource tag.
          - **Key** *(string) --*

            A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for
            the resource to which they are attached.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      Specifies a key-value pair for a resource tag.
      - **Key** *(string) --*

        A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
        resource to which they are attached.
    """


_ClientUpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemLustreConfigurationTypeDef",
    {"WeeklyMaintenanceStartTime": str},
    total=False,
)


class ClientUpdateFileSystemLustreConfigurationTypeDef(
    _ClientUpdateFileSystemLustreConfigurationTypeDef
):
    """
    The configuration object for Amazon FSx for Lustre file systems used in the ``UpdateFileSystem``
    operation.
    - **WeeklyMaintenanceStartTime** *(string) --*

      The preferred time to perform weekly maintenance, in the UTC time zone.
    """


_ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)


class ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef(
    _ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef
):
    pass


_ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    pass


_ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef(
    _ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef
):
    pass


_ClientUpdateFileSystemResponseFileSystemTagsTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdateFileSystemResponseFileSystemTagsTypeDef(
    _ClientUpdateFileSystemResponseFileSystemTagsTypeDef
):
    pass


_ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef(
    _ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef
):
    pass


_ClientUpdateFileSystemResponseFileSystemTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientUpdateFileSystemResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemTypeDef(
    _ClientUpdateFileSystemResponseFileSystemTypeDef
):
    """
    - **FileSystem** *(dict) --*

      A description of the file system that was updated.
      - **OwnerId** *(string) --*

        The AWS account that created the file system. If the file system was created by an AWS
        Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is
        the owner.
    """


_ClientUpdateFileSystemResponseTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseTypeDef",
    {"FileSystem": ClientUpdateFileSystemResponseFileSystemTypeDef},
    total=False,
)


class ClientUpdateFileSystemResponseTypeDef(_ClientUpdateFileSystemResponseTypeDef):
    """
    - *(dict) --*

      The response object for the ``UpdateFileSystem`` operation.
      - **FileSystem** *(dict) --*

        A description of the file system that was updated.
        - **OwnerId** *(string) --*

          The AWS account that created the file system. If the file system was created by an AWS
          Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs
          is the owner.
    """


_ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {"UserName": str, "Password": str, "DnsIps": List[str]},
    total=False,
)


class ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_ClientUpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "SelfManagedActiveDirectoryConfiguration": ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateFileSystemWindowsConfigurationTypeDef(
    _ClientUpdateFileSystemWindowsConfigurationTypeDef
):
    """
    The configuration update for this Microsoft Windows file system. The only supported options are
    for backup and maintenance and for self-managed Active Directory configuration.
    - **WeeklyMaintenanceStartTime** *(string) --*

      The preferred time to perform weekly maintenance, in the UTC time zone.
    """


_DescribeBackupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeBackupsPaginateFiltersTypeDef",
    {"Name": Literal["file-system-id", "backup-type"], "Values": List[str]},
    total=False,
)


class DescribeBackupsPaginateFiltersTypeDef(_DescribeBackupsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      A filter used to restrict the results of describe calls. You can use multiple filters to
      return results that meet all applied filter requirements.
      - **Name** *(string) --*

        The name for this filter.
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


_DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef(
    _DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef", {"Message": str}, total=False
)


class DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef(
    _DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsFileSystemTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef],
        "WindowsConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsTagsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class DescribeBackupsPaginateResponseBackupsTagsTypeDef(
    _DescribeBackupsPaginateResponseBackupsTagsTypeDef
):
    pass


_DescribeBackupsPaginateResponseBackupsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsTypeDef",
    {
        "BackupId": str,
        "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"],
        "FailureDetails": DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef,
        "Type": Literal["AUTOMATIC", "USER_INITIATED"],
        "ProgressPercent": int,
        "CreationTime": datetime,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[DescribeBackupsPaginateResponseBackupsTagsTypeDef],
        "FileSystem": DescribeBackupsPaginateResponseBackupsFileSystemTypeDef,
        "DirectoryInformation": DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsTypeDef(_DescribeBackupsPaginateResponseBackupsTypeDef):
    """
    - *(dict) --*

      A backup of an Amazon FSx for Windows File Server file system. You can create a new file
      system from a backup to protect against data loss.
      - **BackupId** *(string) --*

        The ID of the backup.
    """


_DescribeBackupsPaginateResponseTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseTypeDef",
    {"Backups": List[DescribeBackupsPaginateResponseBackupsTypeDef]},
    total=False,
)


class DescribeBackupsPaginateResponseTypeDef(_DescribeBackupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Response object for ``DescribeBackups`` operation.
      - **Backups** *(list) --*

        Any array of backups.
        - *(dict) --*

          A backup of an Amazon FSx for Windows File Server file system. You can create a new file
          system from a backup to protect against data loss.
          - **BackupId** *(string) --*

            The ID of the backup.
    """


_DescribeFileSystemsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFileSystemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFileSystemsPaginatePaginationConfigTypeDef(
    _DescribeFileSystemsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseFileSystemsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef],
        "WindowsConfiguration": DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef,
        "LustreConfiguration": DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef,
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsTypeDef
):
    """
    - *(dict) --*

      A description of a specific Amazon FSx file system.
      - **OwnerId** *(string) --*

        The AWS account that created the file system. If the file system was created by an AWS
        Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is
        the owner.
    """


_DescribeFileSystemsPaginateResponseTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseTypeDef",
    {"FileSystems": List[DescribeFileSystemsPaginateResponseFileSystemsTypeDef]},
    total=False,
)


class DescribeFileSystemsPaginateResponseTypeDef(_DescribeFileSystemsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The response object for ``DescribeFileSystems`` operation.
      - **FileSystems** *(list) --*

        An array of file system descriptions.
        - *(dict) --*

          A description of a specific Amazon FSx file system.
          - **OwnerId** *(string) --*

            The AWS account that created the file system. If the file system was created by an AWS
            Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs
            is the owner.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    - *(dict) --*

      Specifies a key-value pair for a resource tag.
      - **Key** *(string) --*

        A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
        resource to which they are attached.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      The response object for ``ListTagsForResource`` operation.
      - **Tags** *(list) --*

        A list of tags on the resource.
        - *(dict) --*

          Specifies a key-value pair for a resource tag.
          - **Key** *(string) --*

            A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for
            the resource to which they are attached.
    """
