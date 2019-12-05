"Main interface for opsworkscm service type defs"
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


ClientAssociateNodeEngineAttributesTypeDef = TypedDict(
    "ClientAssociateNodeEngineAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientAssociateNodeResponseTypeDef = TypedDict(
    "ClientAssociateNodeResponseTypeDef", {"NodeAssociationStatusToken": str}, total=False
)

ClientCreateBackupResponseBackupTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": Literal["AUTOMATED", "MANUAL"],
        "CreatedAt": datetime,
        "Description": str,
        "Engine": str,
        "EngineModel": str,
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "S3DataSize": int,
        "S3DataUrl": str,
        "S3LogUrl": str,
        "SecurityGroupIds": List[str],
        "ServerName": str,
        "ServiceRoleArn": str,
        "Status": Literal["IN_PROGRESS", "OK", "FAILED", "DELETING"],
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
    },
    total=False,
)

ClientCreateBackupResponseTypeDef = TypedDict(
    "ClientCreateBackupResponseTypeDef",
    {"Backup": ClientCreateBackupResponseBackupTypeDef},
    total=False,
)

ClientCreateServerEngineAttributesTypeDef = TypedDict(
    "ClientCreateServerEngineAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientCreateServerResponseServerEngineAttributesTypeDef = TypedDict(
    "ClientCreateServerResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateServerResponseServerTypeDef = TypedDict(
    "ClientCreateServerResponseServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[ClientCreateServerResponseServerEngineAttributesTypeDef],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": Literal["SUCCESS", "FAILED"],
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": Literal[
            "BACKING_UP",
            "CONNECTION_LOST",
            "CREATING",
            "DELETING",
            "MODIFYING",
            "FAILED",
            "HEALTHY",
            "RUNNING",
            "RESTORING",
            "SETUP",
            "UNDER_MAINTENANCE",
            "UNHEALTHY",
            "TERMINATED",
        ],
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

ClientCreateServerResponseTypeDef = TypedDict(
    "ClientCreateServerResponseTypeDef",
    {"Server": ClientCreateServerResponseServerTypeDef},
    total=False,
)

ClientDescribeAccountAttributesResponseAttributesTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseAttributesTypeDef",
    {"Name": str, "Maximum": int, "Used": int},
    total=False,
)

ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeAccountAttributesResponseAttributesTypeDef]},
    total=False,
)

ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": Literal["AUTOMATED", "MANUAL"],
        "CreatedAt": datetime,
        "Description": str,
        "Engine": str,
        "EngineModel": str,
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "S3DataSize": int,
        "S3DataUrl": str,
        "S3LogUrl": str,
        "SecurityGroupIds": List[str],
        "ServerName": str,
        "ServiceRoleArn": str,
        "Status": Literal["IN_PROGRESS", "OK", "FAILED", "DELETING"],
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
    },
    total=False,
)

ClientDescribeBackupsResponseTypeDef = TypedDict(
    "ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeEventsResponseServerEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseServerEventsTypeDef",
    {"CreatedAt": datetime, "ServerName": str, "Message": str, "LogUrl": str},
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"ServerEvents": List[ClientDescribeEventsResponseServerEventsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef = TypedDict(
    "ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeNodeAssociationStatusResponseTypeDef = TypedDict(
    "ClientDescribeNodeAssociationStatusResponseTypeDef",
    {
        "NodeAssociationStatus": Literal["SUCCESS", "FAILED", "IN_PROGRESS"],
        "EngineAttributes": List[
            ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef
        ],
    },
    total=False,
)

ClientDescribeServersResponseServersEngineAttributesTypeDef = TypedDict(
    "ClientDescribeServersResponseServersEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeServersResponseServersTypeDef = TypedDict(
    "ClientDescribeServersResponseServersTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[ClientDescribeServersResponseServersEngineAttributesTypeDef],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": Literal["SUCCESS", "FAILED"],
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": Literal[
            "BACKING_UP",
            "CONNECTION_LOST",
            "CREATING",
            "DELETING",
            "MODIFYING",
            "FAILED",
            "HEALTHY",
            "RUNNING",
            "RESTORING",
            "SETUP",
            "UNDER_MAINTENANCE",
            "UNHEALTHY",
            "TERMINATED",
        ],
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

ClientDescribeServersResponseTypeDef = TypedDict(
    "ClientDescribeServersResponseTypeDef",
    {"Servers": List[ClientDescribeServersResponseServersTypeDef], "NextToken": str},
    total=False,
)

ClientDisassociateNodeEngineAttributesTypeDef = TypedDict(
    "ClientDisassociateNodeEngineAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientDisassociateNodeResponseTypeDef = TypedDict(
    "ClientDisassociateNodeResponseTypeDef", {"NodeAssociationStatusToken": str}, total=False
)

ClientExportServerEngineAttributeInputAttributesTypeDef = TypedDict(
    "ClientExportServerEngineAttributeInputAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientExportServerEngineAttributeResponseEngineAttributeTypeDef = TypedDict(
    "ClientExportServerEngineAttributeResponseEngineAttributeTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientExportServerEngineAttributeResponseTypeDef = TypedDict(
    "ClientExportServerEngineAttributeResponseTypeDef",
    {
        "EngineAttribute": ClientExportServerEngineAttributeResponseEngineAttributeTypeDef,
        "ServerName": str,
    },
    total=False,
)

ClientStartMaintenanceEngineAttributesTypeDef = TypedDict(
    "ClientStartMaintenanceEngineAttributesTypeDef", {"Name": str, "Value": str}, total=False
)

ClientStartMaintenanceResponseServerEngineAttributesTypeDef = TypedDict(
    "ClientStartMaintenanceResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientStartMaintenanceResponseServerTypeDef = TypedDict(
    "ClientStartMaintenanceResponseServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[ClientStartMaintenanceResponseServerEngineAttributesTypeDef],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": Literal["SUCCESS", "FAILED"],
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": Literal[
            "BACKING_UP",
            "CONNECTION_LOST",
            "CREATING",
            "DELETING",
            "MODIFYING",
            "FAILED",
            "HEALTHY",
            "RUNNING",
            "RESTORING",
            "SETUP",
            "UNDER_MAINTENANCE",
            "UNHEALTHY",
            "TERMINATED",
        ],
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

ClientStartMaintenanceResponseTypeDef = TypedDict(
    "ClientStartMaintenanceResponseTypeDef",
    {"Server": ClientStartMaintenanceResponseServerTypeDef},
    total=False,
)

ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef = TypedDict(
    "ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientUpdateServerEngineAttributesResponseServerTypeDef = TypedDict(
    "ClientUpdateServerEngineAttributesResponseServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[
            ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef
        ],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": Literal["SUCCESS", "FAILED"],
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": Literal[
            "BACKING_UP",
            "CONNECTION_LOST",
            "CREATING",
            "DELETING",
            "MODIFYING",
            "FAILED",
            "HEALTHY",
            "RUNNING",
            "RESTORING",
            "SETUP",
            "UNDER_MAINTENANCE",
            "UNHEALTHY",
            "TERMINATED",
        ],
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

ClientUpdateServerEngineAttributesResponseTypeDef = TypedDict(
    "ClientUpdateServerEngineAttributesResponseTypeDef",
    {"Server": ClientUpdateServerEngineAttributesResponseServerTypeDef},
    total=False,
)

ClientUpdateServerResponseServerEngineAttributesTypeDef = TypedDict(
    "ClientUpdateServerResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientUpdateServerResponseServerTypeDef = TypedDict(
    "ClientUpdateServerResponseServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[ClientUpdateServerResponseServerEngineAttributesTypeDef],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": Literal["SUCCESS", "FAILED"],
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": Literal[
            "BACKING_UP",
            "CONNECTION_LOST",
            "CREATING",
            "DELETING",
            "MODIFYING",
            "FAILED",
            "HEALTHY",
            "RUNNING",
            "RESTORING",
            "SETUP",
            "UNDER_MAINTENANCE",
            "UNHEALTHY",
            "TERMINATED",
        ],
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

ClientUpdateServerResponseTypeDef = TypedDict(
    "ClientUpdateServerResponseTypeDef",
    {"Server": ClientUpdateServerResponseServerTypeDef},
    total=False,
)

DescribeBackupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeBackupsPaginateResponseBackupsTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseBackupsTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": Literal["AUTOMATED", "MANUAL"],
        "CreatedAt": datetime,
        "Description": str,
        "Engine": str,
        "EngineModel": str,
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "S3DataSize": int,
        "S3DataUrl": str,
        "S3LogUrl": str,
        "SecurityGroupIds": List[str],
        "ServerName": str,
        "ServiceRoleArn": str,
        "Status": Literal["IN_PROGRESS", "OK", "FAILED", "DELETING"],
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
    },
    total=False,
)

DescribeBackupsPaginateResponseTypeDef = TypedDict(
    "DescribeBackupsPaginateResponseTypeDef",
    {"Backups": List[DescribeBackupsPaginateResponseBackupsTypeDef]},
    total=False,
)

DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEventsPaginateResponseServerEventsTypeDef = TypedDict(
    "DescribeEventsPaginateResponseServerEventsTypeDef",
    {"CreatedAt": datetime, "ServerName": str, "Message": str, "LogUrl": str},
    total=False,
)

DescribeEventsPaginateResponseTypeDef = TypedDict(
    "DescribeEventsPaginateResponseTypeDef",
    {"ServerEvents": List[DescribeEventsPaginateResponseServerEventsTypeDef]},
    total=False,
)

DescribeServersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeServersPaginateResponseServersEngineAttributesTypeDef = TypedDict(
    "DescribeServersPaginateResponseServersEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

DescribeServersPaginateResponseServersTypeDef = TypedDict(
    "DescribeServersPaginateResponseServersTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[DescribeServersPaginateResponseServersEngineAttributesTypeDef],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": Literal["SUCCESS", "FAILED"],
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": Literal[
            "BACKING_UP",
            "CONNECTION_LOST",
            "CREATING",
            "DELETING",
            "MODIFYING",
            "FAILED",
            "HEALTHY",
            "RUNNING",
            "RESTORING",
            "SETUP",
            "UNDER_MAINTENANCE",
            "UNHEALTHY",
            "TERMINATED",
        ],
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

DescribeServersPaginateResponseTypeDef = TypedDict(
    "DescribeServersPaginateResponseTypeDef",
    {"Servers": List[DescribeServersPaginateResponseServersTypeDef]},
    total=False,
)

NodeAssociatedWaitWaiterConfigTypeDef = TypedDict(
    "NodeAssociatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
