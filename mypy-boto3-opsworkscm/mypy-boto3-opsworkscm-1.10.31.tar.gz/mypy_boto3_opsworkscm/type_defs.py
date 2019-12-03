"Main interface for opsworkscm service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociateNodeEngineAttributesTypeDef",
    "ClientAssociateNodeResponseTypeDef",
    "ClientCreateBackupResponseBackupTypeDef",
    "ClientCreateBackupResponseTypeDef",
    "ClientCreateServerEngineAttributesTypeDef",
    "ClientCreateServerResponseServerEngineAttributesTypeDef",
    "ClientCreateServerResponseServerTypeDef",
    "ClientCreateServerResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAttributesTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeBackupsResponseBackupsTypeDef",
    "ClientDescribeBackupsResponseTypeDef",
    "ClientDescribeEventsResponseServerEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef",
    "ClientDescribeNodeAssociationStatusResponseTypeDef",
    "ClientDescribeServersResponseServersEngineAttributesTypeDef",
    "ClientDescribeServersResponseServersTypeDef",
    "ClientDescribeServersResponseTypeDef",
    "ClientDisassociateNodeEngineAttributesTypeDef",
    "ClientDisassociateNodeResponseTypeDef",
    "ClientExportServerEngineAttributeInputAttributesTypeDef",
    "ClientExportServerEngineAttributeResponseEngineAttributeTypeDef",
    "ClientExportServerEngineAttributeResponseTypeDef",
    "ClientStartMaintenanceEngineAttributesTypeDef",
    "ClientStartMaintenanceResponseServerEngineAttributesTypeDef",
    "ClientStartMaintenanceResponseServerTypeDef",
    "ClientStartMaintenanceResponseTypeDef",
    "ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef",
    "ClientUpdateServerEngineAttributesResponseServerTypeDef",
    "ClientUpdateServerEngineAttributesResponseTypeDef",
    "ClientUpdateServerResponseServerEngineAttributesTypeDef",
    "ClientUpdateServerResponseServerTypeDef",
    "ClientUpdateServerResponseTypeDef",
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    "DescribeBackupsPaginateResponseBackupsTypeDef",
    "DescribeBackupsPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseServerEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeServersPaginatePaginationConfigTypeDef",
    "DescribeServersPaginateResponseServersEngineAttributesTypeDef",
    "DescribeServersPaginateResponseServersTypeDef",
    "DescribeServersPaginateResponseTypeDef",
    "NodeAssociatedWaitWaiterConfigTypeDef",
)


_ClientAssociateNodeEngineAttributesTypeDef = TypedDict(
    "_ClientAssociateNodeEngineAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientAssociateNodeEngineAttributesTypeDef(_ClientAssociateNodeEngineAttributesTypeDef):
    pass


_ClientAssociateNodeResponseTypeDef = TypedDict(
    "_ClientAssociateNodeResponseTypeDef", {"NodeAssociationStatusToken": str}, total=False
)


class ClientAssociateNodeResponseTypeDef(_ClientAssociateNodeResponseTypeDef):
    """
    - *(dict) --*

      - **NodeAssociationStatusToken** *(string) --*

        Contains a token which can be passed to the ``DescribeNodeAssociationStatus`` API call to
        get the status of the association request.
    """


_ClientCreateBackupResponseBackupTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupTypeDef",
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


class ClientCreateBackupResponseBackupTypeDef(_ClientCreateBackupResponseBackupTypeDef):
    """
    - **Backup** *(dict) --*

      Backup created by request.
      - **BackupArn** *(string) --*

        The ARN of the backup.
    """


_ClientCreateBackupResponseTypeDef = TypedDict(
    "_ClientCreateBackupResponseTypeDef",
    {"Backup": ClientCreateBackupResponseBackupTypeDef},
    total=False,
)


class ClientCreateBackupResponseTypeDef(_ClientCreateBackupResponseTypeDef):
    """
    - *(dict) --*

      - **Backup** *(dict) --*

        Backup created by request.
        - **BackupArn** *(string) --*

          The ARN of the backup.
    """


_ClientCreateServerEngineAttributesTypeDef = TypedDict(
    "_ClientCreateServerEngineAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientCreateServerEngineAttributesTypeDef(_ClientCreateServerEngineAttributesTypeDef):
    pass


_ClientCreateServerResponseServerEngineAttributesTypeDef = TypedDict(
    "_ClientCreateServerResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateServerResponseServerEngineAttributesTypeDef(
    _ClientCreateServerResponseServerEngineAttributesTypeDef
):
    pass


_ClientCreateServerResponseServerTypeDef = TypedDict(
    "_ClientCreateServerResponseServerTypeDef",
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


class ClientCreateServerResponseServerTypeDef(_ClientCreateServerResponseServerTypeDef):
    """
    - **Server** *(dict) --*

      The server that is created by the request.
      - **AssociatePublicIpAddress** *(boolean) --*

        Associate a public IP address with a server that you are launching.
    """


_ClientCreateServerResponseTypeDef = TypedDict(
    "_ClientCreateServerResponseTypeDef",
    {"Server": ClientCreateServerResponseServerTypeDef},
    total=False,
)


class ClientCreateServerResponseTypeDef(_ClientCreateServerResponseTypeDef):
    """
    - *(dict) --*

      - **Server** *(dict) --*

        The server that is created by the request.
        - **AssociatePublicIpAddress** *(boolean) --*

          Associate a public IP address with a server that you are launching.
    """


_ClientDescribeAccountAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseAttributesTypeDef",
    {"Name": str, "Maximum": int, "Used": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseAttributesTypeDef(
    _ClientDescribeAccountAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      Stores account attributes.
      - **Name** *(string) --*

        The attribute name. The following are supported attribute names.
        * *ServerLimit:* The number of current servers/maximum number of servers allowed. By
        default, you can have a maximum of 10 servers.
        * *ManualBackupLimit:* The number of current manual backups/maximum number of backups
        allowed. By default, you can have a maximum of 50 manual backups saved.
    """


_ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeAccountAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientDescribeAccountAttributesResponseTypeDef(
    _ClientDescribeAccountAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        The attributes that are currently set for the account.
        - *(dict) --*

          Stores account attributes.
          - **Name** *(string) --*

            The attribute name. The following are supported attribute names.
            * *ServerLimit:* The number of current servers/maximum number of servers allowed. By
            default, you can have a maximum of 10 servers.
            * *ManualBackupLimit:* The number of current manual backups/maximum number of backups
            allowed. By default, you can have a maximum of 50 manual backups saved.
    """


_ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsTypeDef",
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


class ClientDescribeBackupsResponseBackupsTypeDef(_ClientDescribeBackupsResponseBackupsTypeDef):
    """
    - *(dict) --*

      Describes a single backup.
      - **BackupArn** *(string) --*

        The ARN of the backup.
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

        Contains the response to a ``DescribeBackups`` request.
        - *(dict) --*

          Describes a single backup.
          - **BackupArn** *(string) --*

            The ARN of the backup.
    """


_ClientDescribeEventsResponseServerEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseServerEventsTypeDef",
    {"CreatedAt": datetime, "ServerName": str, "Message": str, "LogUrl": str},
    total=False,
)


class ClientDescribeEventsResponseServerEventsTypeDef(
    _ClientDescribeEventsResponseServerEventsTypeDef
):
    """
    - *(dict) --*

      An event that is related to the server, such as the start of maintenance or backup.
      - **CreatedAt** *(datetime) --*

        The time when the event occurred.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"ServerEvents": List[ClientDescribeEventsResponseServerEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    - *(dict) --*

      - **ServerEvents** *(list) --*

        Contains the response to a ``DescribeEvents`` request.
        - *(dict) --*

          An event that is related to the server, such as the start of maintenance or backup.
          - **CreatedAt** *(datetime) --*

            The time when the event occurred.
    """


_ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef = TypedDict(
    "_ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef(
    _ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef
):
    pass


_ClientDescribeNodeAssociationStatusResponseTypeDef = TypedDict(
    "_ClientDescribeNodeAssociationStatusResponseTypeDef",
    {
        "NodeAssociationStatus": Literal["SUCCESS", "FAILED", "IN_PROGRESS"],
        "EngineAttributes": List[
            ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeNodeAssociationStatusResponseTypeDef(
    _ClientDescribeNodeAssociationStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **NodeAssociationStatus** *(string) --*

        The status of the association or disassociation request.

          **Possible values:**
    """


_ClientDescribeServersResponseServersEngineAttributesTypeDef = TypedDict(
    "_ClientDescribeServersResponseServersEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeServersResponseServersEngineAttributesTypeDef(
    _ClientDescribeServersResponseServersEngineAttributesTypeDef
):
    pass


_ClientDescribeServersResponseServersTypeDef = TypedDict(
    "_ClientDescribeServersResponseServersTypeDef",
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


class ClientDescribeServersResponseServersTypeDef(_ClientDescribeServersResponseServersTypeDef):
    pass


_ClientDescribeServersResponseTypeDef = TypedDict(
    "_ClientDescribeServersResponseTypeDef",
    {"Servers": List[ClientDescribeServersResponseServersTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeServersResponseTypeDef(_ClientDescribeServersResponseTypeDef):
    """
    - *(dict) --*

      - **Servers** *(list) --*

        Contains the response to a ``DescribeServers`` request.

          *For Puppet Server:*  ``DescribeServersResponse$Servers$EngineAttributes`` contains
          PUPPET_API_CA_CERT. This is the PEM-encoded CA certificate that is used by the Puppet API
          over TCP port number 8140. The CA certificate is also used to sign node certificates.
    """


_ClientDisassociateNodeEngineAttributesTypeDef = TypedDict(
    "_ClientDisassociateNodeEngineAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientDisassociateNodeEngineAttributesTypeDef(_ClientDisassociateNodeEngineAttributesTypeDef):
    pass


_ClientDisassociateNodeResponseTypeDef = TypedDict(
    "_ClientDisassociateNodeResponseTypeDef", {"NodeAssociationStatusToken": str}, total=False
)


class ClientDisassociateNodeResponseTypeDef(_ClientDisassociateNodeResponseTypeDef):
    """
    - *(dict) --*

      - **NodeAssociationStatusToken** *(string) --*

        Contains a token which can be passed to the ``DescribeNodeAssociationStatus`` API call to
        get the status of the disassociation request.
    """


_ClientExportServerEngineAttributeInputAttributesTypeDef = TypedDict(
    "_ClientExportServerEngineAttributeInputAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientExportServerEngineAttributeInputAttributesTypeDef(
    _ClientExportServerEngineAttributeInputAttributesTypeDef
):
    """
    - *(dict) --*

      A name and value pair that is specific to the engine of the server.
      - **Name** *(string) --*

        The name of the engine attribute.
    """


_ClientExportServerEngineAttributeResponseEngineAttributeTypeDef = TypedDict(
    "_ClientExportServerEngineAttributeResponseEngineAttributeTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientExportServerEngineAttributeResponseEngineAttributeTypeDef(
    _ClientExportServerEngineAttributeResponseEngineAttributeTypeDef
):
    """
    - **EngineAttribute** *(dict) --*

      The requested engine attribute pair with attribute name and value.
      - **Name** *(string) --*

        The name of the engine attribute.
    """


_ClientExportServerEngineAttributeResponseTypeDef = TypedDict(
    "_ClientExportServerEngineAttributeResponseTypeDef",
    {
        "EngineAttribute": ClientExportServerEngineAttributeResponseEngineAttributeTypeDef,
        "ServerName": str,
    },
    total=False,
)


class ClientExportServerEngineAttributeResponseTypeDef(
    _ClientExportServerEngineAttributeResponseTypeDef
):
    """
    - *(dict) --*

      - **EngineAttribute** *(dict) --*

        The requested engine attribute pair with attribute name and value.
        - **Name** *(string) --*

          The name of the engine attribute.
    """


_ClientStartMaintenanceEngineAttributesTypeDef = TypedDict(
    "_ClientStartMaintenanceEngineAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientStartMaintenanceEngineAttributesTypeDef(_ClientStartMaintenanceEngineAttributesTypeDef):
    """
    - *(dict) --*

      A name and value pair that is specific to the engine of the server.
      - **Name** *(string) --*

        The name of the engine attribute.
    """


_ClientStartMaintenanceResponseServerEngineAttributesTypeDef = TypedDict(
    "_ClientStartMaintenanceResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientStartMaintenanceResponseServerEngineAttributesTypeDef(
    _ClientStartMaintenanceResponseServerEngineAttributesTypeDef
):
    pass


_ClientStartMaintenanceResponseServerTypeDef = TypedDict(
    "_ClientStartMaintenanceResponseServerTypeDef",
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


class ClientStartMaintenanceResponseServerTypeDef(_ClientStartMaintenanceResponseServerTypeDef):
    """
    - **Server** *(dict) --*

      Contains the response to a ``StartMaintenance`` request.
      - **AssociatePublicIpAddress** *(boolean) --*

        Associate a public IP address with a server that you are launching.
    """


_ClientStartMaintenanceResponseTypeDef = TypedDict(
    "_ClientStartMaintenanceResponseTypeDef",
    {"Server": ClientStartMaintenanceResponseServerTypeDef},
    total=False,
)


class ClientStartMaintenanceResponseTypeDef(_ClientStartMaintenanceResponseTypeDef):
    """
    - *(dict) --*

      - **Server** *(dict) --*

        Contains the response to a ``StartMaintenance`` request.
        - **AssociatePublicIpAddress** *(boolean) --*

          Associate a public IP address with a server that you are launching.
    """


_ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef = TypedDict(
    "_ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef(
    _ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef
):
    pass


_ClientUpdateServerEngineAttributesResponseServerTypeDef = TypedDict(
    "_ClientUpdateServerEngineAttributesResponseServerTypeDef",
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


class ClientUpdateServerEngineAttributesResponseServerTypeDef(
    _ClientUpdateServerEngineAttributesResponseServerTypeDef
):
    """
    - **Server** *(dict) --*

      Contains the response to an ``UpdateServerEngineAttributes`` request.
      - **AssociatePublicIpAddress** *(boolean) --*

        Associate a public IP address with a server that you are launching.
    """


_ClientUpdateServerEngineAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateServerEngineAttributesResponseTypeDef",
    {"Server": ClientUpdateServerEngineAttributesResponseServerTypeDef},
    total=False,
)


class ClientUpdateServerEngineAttributesResponseTypeDef(
    _ClientUpdateServerEngineAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **Server** *(dict) --*

        Contains the response to an ``UpdateServerEngineAttributes`` request.
        - **AssociatePublicIpAddress** *(boolean) --*

          Associate a public IP address with a server that you are launching.
    """


_ClientUpdateServerResponseServerEngineAttributesTypeDef = TypedDict(
    "_ClientUpdateServerResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientUpdateServerResponseServerEngineAttributesTypeDef(
    _ClientUpdateServerResponseServerEngineAttributesTypeDef
):
    pass


_ClientUpdateServerResponseServerTypeDef = TypedDict(
    "_ClientUpdateServerResponseServerTypeDef",
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


class ClientUpdateServerResponseServerTypeDef(_ClientUpdateServerResponseServerTypeDef):
    """
    - **Server** *(dict) --*

      Contains the response to a ``UpdateServer`` request.
      - **AssociatePublicIpAddress** *(boolean) --*

        Associate a public IP address with a server that you are launching.
    """


_ClientUpdateServerResponseTypeDef = TypedDict(
    "_ClientUpdateServerResponseTypeDef",
    {"Server": ClientUpdateServerResponseServerTypeDef},
    total=False,
)


class ClientUpdateServerResponseTypeDef(_ClientUpdateServerResponseTypeDef):
    """
    - *(dict) --*

      - **Server** *(dict) --*

        Contains the response to a ``UpdateServer`` request.
        - **AssociatePublicIpAddress** *(boolean) --*

          Associate a public IP address with a server that you are launching.
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


class DescribeBackupsPaginateResponseBackupsTypeDef(_DescribeBackupsPaginateResponseBackupsTypeDef):
    """
    - *(dict) --*

      Describes a single backup.
      - **BackupArn** *(string) --*

        The ARN of the backup.
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

        Contains the response to a ``DescribeBackups`` request.
        - *(dict) --*

          Describes a single backup.
          - **BackupArn** *(string) --*

            The ARN of the backup.
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


_DescribeEventsPaginateResponseServerEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseServerEventsTypeDef",
    {"CreatedAt": datetime, "ServerName": str, "Message": str, "LogUrl": str},
    total=False,
)


class DescribeEventsPaginateResponseServerEventsTypeDef(
    _DescribeEventsPaginateResponseServerEventsTypeDef
):
    """
    - *(dict) --*

      An event that is related to the server, such as the start of maintenance or backup.
      - **CreatedAt** *(datetime) --*

        The time when the event occurred.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"ServerEvents": List[DescribeEventsPaginateResponseServerEventsTypeDef]},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ServerEvents** *(list) --*

        Contains the response to a ``DescribeEvents`` request.
        - *(dict) --*

          An event that is related to the server, such as the start of maintenance or backup.
          - **CreatedAt** *(datetime) --*

            The time when the event occurred.
    """


_DescribeServersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeServersPaginatePaginationConfigTypeDef(
    _DescribeServersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeServersPaginateResponseServersEngineAttributesTypeDef = TypedDict(
    "_DescribeServersPaginateResponseServersEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeServersPaginateResponseServersEngineAttributesTypeDef(
    _DescribeServersPaginateResponseServersEngineAttributesTypeDef
):
    pass


_DescribeServersPaginateResponseServersTypeDef = TypedDict(
    "_DescribeServersPaginateResponseServersTypeDef",
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


class DescribeServersPaginateResponseServersTypeDef(_DescribeServersPaginateResponseServersTypeDef):
    pass


_DescribeServersPaginateResponseTypeDef = TypedDict(
    "_DescribeServersPaginateResponseTypeDef",
    {"Servers": List[DescribeServersPaginateResponseServersTypeDef]},
    total=False,
)


class DescribeServersPaginateResponseTypeDef(_DescribeServersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Servers** *(list) --*

        Contains the response to a ``DescribeServers`` request.

          *For Puppet Server:*  ``DescribeServersResponse$Servers$EngineAttributes`` contains
          PUPPET_API_CA_CERT. This is the PEM-encoded CA certificate that is used by the Puppet API
          over TCP port number 8140. The CA certificate is also used to sign node certificates.
    """


_NodeAssociatedWaitWaiterConfigTypeDef = TypedDict(
    "_NodeAssociatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class NodeAssociatedWaitWaiterConfigTypeDef(_NodeAssociatedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """
