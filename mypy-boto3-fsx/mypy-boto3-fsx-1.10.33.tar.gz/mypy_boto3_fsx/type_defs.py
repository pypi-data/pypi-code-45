"Main interface for fsx service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateBackupResponseBackupDirectoryInformationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)

ClientCreateBackupResponseBackupFailureDetailsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientCreateBackupResponseBackupFileSystemTagsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef",
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

ClientCreateBackupResponseBackupFileSystemTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemTypeDef",
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

ClientCreateBackupResponseBackupTagsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateBackupResponseBackupTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupTypeDef",
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

ClientCreateBackupResponseTypeDef = TypedDict(
    "ClientCreateBackupResponseTypeDef",
    {"Backup": ClientCreateBackupResponseBackupTypeDef},
    total=False,
)

ClientCreateBackupTagsTypeDef = TypedDict(
    "ClientCreateBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef",
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

ClientCreateFileSystemFromBackupResponseFileSystemTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemTypeDef",
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

ClientCreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseTypeDef",
    {"FileSystem": ClientCreateFileSystemFromBackupResponseFileSystemTypeDef},
    total=False,
)

ClientCreateFileSystemFromBackupTagsTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
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

ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef",
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

ClientCreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
    },
    total=False,
)

ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientCreateFileSystemResponseFileSystemTagsTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
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

ClientCreateFileSystemResponseFileSystemTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemTypeDef",
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

ClientCreateFileSystemResponseTypeDef = TypedDict(
    "ClientCreateFileSystemResponseTypeDef",
    {"FileSystem": ClientCreateFileSystemResponseFileSystemTypeDef},
    total=False,
)

ClientCreateFileSystemTagsTypeDef = TypedDict(
    "ClientCreateFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
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

ClientCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemWindowsConfigurationTypeDef",
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

ClientDeleteBackupResponseTypeDef = TypedDict(
    "ClientDeleteBackupResponseTypeDef",
    {"BackupId": str, "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"]},
    total=False,
)

ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef = TypedDict(
    "ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDeleteFileSystemResponseWindowsResponseTypeDef = TypedDict(
    "ClientDeleteFileSystemResponseWindowsResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List[
            ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef
        ],
    },
    total=False,
)

ClientDeleteFileSystemResponseTypeDef = TypedDict(
    "ClientDeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "WindowsResponse": ClientDeleteFileSystemResponseWindowsResponseTypeDef,
    },
    total=False,
)

ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef = TypedDict(
    "ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientDeleteFileSystemWindowsConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List[ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef],
    },
    total=False,
)

ClientDescribeBackupsFiltersTypeDef = TypedDict(
    "ClientDescribeBackupsFiltersTypeDef",
    {"Name": Literal["file-system-id", "backup-type"], "Values": List[str]},
    total=False,
)

ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)

ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef",
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

ClientDescribeBackupsResponseBackupsFileSystemTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemTypeDef",
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

ClientDescribeBackupsResponseBackupsTagsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsTypeDef",
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

ClientDescribeBackupsResponseTypeDef = TypedDict(
    "ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef",
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

ClientDescribeFileSystemsResponseFileSystemsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
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

ClientDescribeFileSystemsResponseTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseTypeDef",
    {"FileSystems": List[ClientDescribeFileSystemsResponseFileSystemsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemLustreConfigurationTypeDef",
    {"WeeklyMaintenanceStartTime": str},
    total=False,
)

ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateFileSystemResponseFileSystemTagsTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
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

ClientUpdateFileSystemResponseFileSystemTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemTypeDef",
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

ClientUpdateFileSystemResponseTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseTypeDef",
    {"FileSystem": ClientUpdateFileSystemResponseFileSystemTypeDef},
    total=False,
)

ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {"UserName": str, "Password": str, "DnsIps": List[str]},
    total=False,
)

ClientUpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "SelfManagedActiveDirectoryConfiguration": ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
    },
    total=False,
)

DescribeBackupsPaginateFiltersTypeDef = TypedDict(
    "DescribeBackupsPaginateFiltersTypeDef",
    {"Name": Literal["file-system-id", "backup-type"], "Values": List[str]},
    total=False,
)

DescribeBackupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)

DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef", {"Message": str}, total=False
)

DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef",
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

DescribeBackupsPaginateResponseBackupsFileSystemTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsFileSystemTypeDef",
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

DescribeBackupsPaginateResponseBackupsTagsTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

DescribeBackupsPaginateResponseBackupsTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsTypeDef",
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

DescribeBackupsPaginateResponseTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseTypeDef",
    {"Backups": List[DescribeBackupsPaginateResponseBackupsTypeDef]},
    total=False,
)

DescribeFileSystemsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeFileSystemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef",
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

DescribeFileSystemsPaginateResponseFileSystemsTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
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

DescribeFileSystemsPaginateResponseTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseTypeDef",
    {"FileSystems": List[DescribeFileSystemsPaginateResponseFileSystemsTypeDef]},
    total=False,
)

ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "ListTagsForResourcePaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)
