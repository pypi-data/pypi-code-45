"Main interface for appstream service type defs"
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


ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef = TypedDict(
    "ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)

ClientBatchAssociateUserStackResponseerrorsTypeDef = TypedDict(
    "ClientBatchAssociateUserStackResponseerrorsTypeDef",
    {
        "UserStackAssociation": ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef,
        "ErrorCode": Literal["STACK_NOT_FOUND", "USER_NAME_NOT_FOUND", "INTERNAL_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchAssociateUserStackResponseTypeDef = TypedDict(
    "ClientBatchAssociateUserStackResponseTypeDef",
    {"errors": List[ClientBatchAssociateUserStackResponseerrorsTypeDef]},
    total=False,
)

_RequiredClientBatchAssociateUserStackUserStackAssociationsTypeDef = TypedDict(
    "_RequiredClientBatchAssociateUserStackUserStackAssociationsTypeDef", {"StackName": str}
)
_OptionalClientBatchAssociateUserStackUserStackAssociationsTypeDef = TypedDict(
    "_OptionalClientBatchAssociateUserStackUserStackAssociationsTypeDef",
    {
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)


class ClientBatchAssociateUserStackUserStackAssociationsTypeDef(
    _RequiredClientBatchAssociateUserStackUserStackAssociationsTypeDef,
    _OptionalClientBatchAssociateUserStackUserStackAssociationsTypeDef,
):
    pass


ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef = TypedDict(
    "ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)

ClientBatchDisassociateUserStackResponseerrorsTypeDef = TypedDict(
    "ClientBatchDisassociateUserStackResponseerrorsTypeDef",
    {
        "UserStackAssociation": ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef,
        "ErrorCode": Literal["STACK_NOT_FOUND", "USER_NAME_NOT_FOUND", "INTERNAL_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchDisassociateUserStackResponseTypeDef = TypedDict(
    "ClientBatchDisassociateUserStackResponseTypeDef",
    {"errors": List[ClientBatchDisassociateUserStackResponseerrorsTypeDef]},
    total=False,
)

_RequiredClientBatchDisassociateUserStackUserStackAssociationsTypeDef = TypedDict(
    "_RequiredClientBatchDisassociateUserStackUserStackAssociationsTypeDef", {"StackName": str}
)
_OptionalClientBatchDisassociateUserStackUserStackAssociationsTypeDef = TypedDict(
    "_OptionalClientBatchDisassociateUserStackUserStackAssociationsTypeDef",
    {
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)


class ClientBatchDisassociateUserStackUserStackAssociationsTypeDef(
    _RequiredClientBatchDisassociateUserStackUserStackAssociationsTypeDef,
    _OptionalClientBatchDisassociateUserStackUserStackAssociationsTypeDef,
):
    pass


ClientCopyImageResponseTypeDef = TypedDict(
    "ClientCopyImageResponseTypeDef", {"DestinationImageName": str}, total=False
)

ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)

ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef = TypedDict(
    "ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientCreateDirectoryConfigResponseTypeDef = TypedDict(
    "ClientCreateDirectoryConfigResponseTypeDef",
    {"DirectoryConfig": ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef},
    total=False,
)

_RequiredClientCreateDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_RequiredClientCreateDirectoryConfigServiceAccountCredentialsTypeDef", {"AccountName": str}
)
_OptionalClientCreateDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_OptionalClientCreateDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountPassword": str},
    total=False,
)


class ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef(
    _RequiredClientCreateDirectoryConfigServiceAccountCredentialsTypeDef,
    _OptionalClientCreateDirectoryConfigServiceAccountCredentialsTypeDef,
):
    pass


ClientCreateFleetComputeCapacityTypeDef = TypedDict(
    "ClientCreateFleetComputeCapacityTypeDef", {"DesiredInstances": int}
)

ClientCreateFleetDomainJoinInfoTypeDef = TypedDict(
    "ClientCreateFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef = TypedDict(
    "ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)

ClientCreateFleetResponseFleetDomainJoinInfoTypeDef = TypedDict(
    "ClientCreateFleetResponseFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientCreateFleetResponseFleetFleetErrorsTypeDef = TypedDict(
    "ClientCreateFleetResponseFleetFleetErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientCreateFleetResponseFleetVpcConfigTypeDef = TypedDict(
    "ClientCreateFleetResponseFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientCreateFleetResponseFleetTypeDef = TypedDict(
    "ClientCreateFleetResponseFleetTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "InstanceType": str,
        "FleetType": Literal["ALWAYS_ON", "ON_DEMAND"],
        "ComputeCapacityStatus": ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "State": Literal["STARTING", "RUNNING", "STOPPING", "STOPPED"],
        "VpcConfig": ClientCreateFleetResponseFleetVpcConfigTypeDef,
        "CreatedTime": datetime,
        "FleetErrors": List[ClientCreateFleetResponseFleetFleetErrorsTypeDef],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientCreateFleetResponseFleetDomainJoinInfoTypeDef,
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
    },
    total=False,
)

ClientCreateFleetResponseTypeDef = TypedDict(
    "ClientCreateFleetResponseTypeDef",
    {"Fleet": ClientCreateFleetResponseFleetTypeDef},
    total=False,
)

ClientCreateFleetVpcConfigTypeDef = TypedDict(
    "ClientCreateFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

_RequiredClientCreateImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_RequiredClientCreateImageBuilderAccessEndpointsTypeDef", {"EndpointType": str}
)
_OptionalClientCreateImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_OptionalClientCreateImageBuilderAccessEndpointsTypeDef", {"VpceId": str}, total=False
)


class ClientCreateImageBuilderAccessEndpointsTypeDef(
    _RequiredClientCreateImageBuilderAccessEndpointsTypeDef,
    _OptionalClientCreateImageBuilderAccessEndpointsTypeDef,
):
    pass


ClientCreateImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "ClientCreateImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)

ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)

ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientCreateImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "ClientCreateImageBuilderResponseImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "IamRoleArn": str,
        "State": Literal[
            "PENDING",
            "UPDATING_AGENT",
            "RUNNING",
            "STOPPING",
            "STOPPED",
            "REBOOTING",
            "SNAPSHOTTING",
            "DELETING",
            "FAILED",
        ],
        "StateChangeReason": ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef],
    },
    total=False,
)

ClientCreateImageBuilderResponseTypeDef = TypedDict(
    "ClientCreateImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientCreateImageBuilderResponseImageBuilderTypeDef},
    total=False,
)

ClientCreateImageBuilderStreamingUrlResponseTypeDef = TypedDict(
    "ClientCreateImageBuilderStreamingUrlResponseTypeDef",
    {"StreamingURL": str, "Expires": datetime},
    total=False,
)

ClientCreateImageBuilderVpcConfigTypeDef = TypedDict(
    "ClientCreateImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

_RequiredClientCreateStackAccessEndpointsTypeDef = TypedDict(
    "_RequiredClientCreateStackAccessEndpointsTypeDef", {"EndpointType": str}
)
_OptionalClientCreateStackAccessEndpointsTypeDef = TypedDict(
    "_OptionalClientCreateStackAccessEndpointsTypeDef", {"VpceId": str}, total=False
)


class ClientCreateStackAccessEndpointsTypeDef(
    _RequiredClientCreateStackAccessEndpointsTypeDef,
    _OptionalClientCreateStackAccessEndpointsTypeDef,
):
    pass


_RequiredClientCreateStackApplicationSettingsTypeDef = TypedDict(
    "_RequiredClientCreateStackApplicationSettingsTypeDef", {"Enabled": bool}
)
_OptionalClientCreateStackApplicationSettingsTypeDef = TypedDict(
    "_OptionalClientCreateStackApplicationSettingsTypeDef", {"SettingsGroup": str}, total=False
)


class ClientCreateStackApplicationSettingsTypeDef(
    _RequiredClientCreateStackApplicationSettingsTypeDef,
    _OptionalClientCreateStackApplicationSettingsTypeDef,
):
    pass


ClientCreateStackResponseStackAccessEndpointsTypeDef = TypedDict(
    "ClientCreateStackResponseStackAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

ClientCreateStackResponseStackApplicationSettingsTypeDef = TypedDict(
    "ClientCreateStackResponseStackApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)

ClientCreateStackResponseStackStackErrorsTypeDef = TypedDict(
    "ClientCreateStackResponseStackStackErrorsTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientCreateStackResponseStackStorageConnectorsTypeDef = TypedDict(
    "ClientCreateStackResponseStackStorageConnectorsTypeDef",
    {
        "ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"],
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)

ClientCreateStackResponseStackUserSettingsTypeDef = TypedDict(
    "ClientCreateStackResponseStackUserSettingsTypeDef",
    {
        "Action": Literal[
            "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
            "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
            "FILE_UPLOAD",
            "FILE_DOWNLOAD",
            "PRINTING_TO_LOCAL_DEVICE",
        ],
        "Permission": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientCreateStackResponseStackTypeDef = TypedDict(
    "ClientCreateStackResponseStackTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List[ClientCreateStackResponseStackStorageConnectorsTypeDef],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List[ClientCreateStackResponseStackStackErrorsTypeDef],
        "UserSettings": List[ClientCreateStackResponseStackUserSettingsTypeDef],
        "ApplicationSettings": ClientCreateStackResponseStackApplicationSettingsTypeDef,
        "AccessEndpoints": List[ClientCreateStackResponseStackAccessEndpointsTypeDef],
        "EmbedHostDomains": List[str],
    },
    total=False,
)

ClientCreateStackResponseTypeDef = TypedDict(
    "ClientCreateStackResponseTypeDef",
    {"Stack": ClientCreateStackResponseStackTypeDef},
    total=False,
)

_RequiredClientCreateStackStorageConnectorsTypeDef = TypedDict(
    "_RequiredClientCreateStackStorageConnectorsTypeDef",
    {"ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"]},
)
_OptionalClientCreateStackStorageConnectorsTypeDef = TypedDict(
    "_OptionalClientCreateStackStorageConnectorsTypeDef",
    {"ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class ClientCreateStackStorageConnectorsTypeDef(
    _RequiredClientCreateStackStorageConnectorsTypeDef,
    _OptionalClientCreateStackStorageConnectorsTypeDef,
):
    pass


_RequiredClientCreateStackUserSettingsTypeDef = TypedDict(
    "_RequiredClientCreateStackUserSettingsTypeDef",
    {
        "Action": Literal[
            "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
            "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
            "FILE_UPLOAD",
            "FILE_DOWNLOAD",
            "PRINTING_TO_LOCAL_DEVICE",
        ]
    },
)
_OptionalClientCreateStackUserSettingsTypeDef = TypedDict(
    "_OptionalClientCreateStackUserSettingsTypeDef",
    {"Permission": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientCreateStackUserSettingsTypeDef(
    _RequiredClientCreateStackUserSettingsTypeDef, _OptionalClientCreateStackUserSettingsTypeDef
):
    pass


ClientCreateStreamingUrlResponseTypeDef = TypedDict(
    "ClientCreateStreamingUrlResponseTypeDef",
    {"StreamingURL": str, "Expires": datetime},
    total=False,
)

ClientCreateUsageReportSubscriptionResponseTypeDef = TypedDict(
    "ClientCreateUsageReportSubscriptionResponseTypeDef",
    {"S3BucketName": str, "Schedule": str},
    total=False,
)

ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)

ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)

ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientDeleteImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "ClientDeleteImageBuilderResponseImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "IamRoleArn": str,
        "State": Literal[
            "PENDING",
            "UPDATING_AGENT",
            "RUNNING",
            "STOPPING",
            "STOPPED",
            "REBOOTING",
            "SNAPSHOTTING",
            "DELETING",
            "FAILED",
        ],
        "StateChangeReason": ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef],
    },
    total=False,
)

ClientDeleteImageBuilderResponseTypeDef = TypedDict(
    "ClientDeleteImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientDeleteImageBuilderResponseImageBuilderTypeDef},
    total=False,
)

ClientDeleteImageResponseImageApplicationsTypeDef = TypedDict(
    "ClientDeleteImageResponseImageApplicationsTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "IconURL": str,
        "LaunchPath": str,
        "LaunchParameters": str,
        "Enabled": bool,
        "Metadata": Dict[str, str],
    },
    total=False,
)

ClientDeleteImageResponseImageImagePermissionsTypeDef = TypedDict(
    "ClientDeleteImageResponseImageImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)

ClientDeleteImageResponseImageStateChangeReasonTypeDef = TypedDict(
    "ClientDeleteImageResponseImageStateChangeReasonTypeDef",
    {
        "Code": Literal["INTERNAL_ERROR", "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE"],
        "Message": str,
    },
    total=False,
)

ClientDeleteImageResponseImageTypeDef = TypedDict(
    "ClientDeleteImageResponseImageTypeDef",
    {
        "Name": str,
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": Literal["PENDING", "AVAILABLE", "FAILED", "COPYING", "DELETING"],
        "Visibility": Literal["PUBLIC", "PRIVATE", "SHARED"],
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "Description": str,
        "StateChangeReason": ClientDeleteImageResponseImageStateChangeReasonTypeDef,
        "Applications": List[ClientDeleteImageResponseImageApplicationsTypeDef],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": ClientDeleteImageResponseImageImagePermissionsTypeDef,
    },
    total=False,
)

ClientDeleteImageResponseTypeDef = TypedDict(
    "ClientDeleteImageResponseTypeDef",
    {"Image": ClientDeleteImageResponseImageTypeDef},
    total=False,
)

ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef = TypedDict(
    "ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)

ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef = TypedDict(
    "ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientDescribeDirectoryConfigsResponseTypeDef = TypedDict(
    "ClientDescribeDirectoryConfigsResponseTypeDef",
    {
        "DirectoryConfigs": List[ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef = TypedDict(
    "ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)

ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef = TypedDict(
    "ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef = TypedDict(
    "ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientDescribeFleetsResponseFleetsVpcConfigTypeDef = TypedDict(
    "ClientDescribeFleetsResponseFleetsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientDescribeFleetsResponseFleetsTypeDef = TypedDict(
    "ClientDescribeFleetsResponseFleetsTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "InstanceType": str,
        "FleetType": Literal["ALWAYS_ON", "ON_DEMAND"],
        "ComputeCapacityStatus": ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "State": Literal["STARTING", "RUNNING", "STOPPING", "STOPPED"],
        "VpcConfig": ClientDescribeFleetsResponseFleetsVpcConfigTypeDef,
        "CreatedTime": datetime,
        "FleetErrors": List[ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef,
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
    },
    total=False,
)

ClientDescribeFleetsResponseTypeDef = TypedDict(
    "ClientDescribeFleetsResponseTypeDef",
    {"Fleets": List[ClientDescribeFleetsResponseFleetsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef = TypedDict(
    "ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef = TypedDict(
    "ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef = TypedDict(
    "ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef = TypedDict(
    "ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)

ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef = TypedDict(
    "ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)

ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef = TypedDict(
    "ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientDescribeImageBuildersResponseImageBuildersTypeDef = TypedDict(
    "ClientDescribeImageBuildersResponseImageBuildersTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "IamRoleArn": str,
        "State": Literal[
            "PENDING",
            "UPDATING_AGENT",
            "RUNNING",
            "STOPPING",
            "STOPPED",
            "REBOOTING",
            "SNAPSHOTTING",
            "DELETING",
            "FAILED",
        ],
        "StateChangeReason": ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[
            ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef
        ],
    },
    total=False,
)

ClientDescribeImageBuildersResponseTypeDef = TypedDict(
    "ClientDescribeImageBuildersResponseTypeDef",
    {
        "ImageBuilders": List[ClientDescribeImageBuildersResponseImageBuildersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef = TypedDict(
    "ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)

ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef = TypedDict(
    "ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef",
    {
        "sharedAccountId": str,
        "imagePermissions": ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef,
    },
    total=False,
)

ClientDescribeImagePermissionsResponseTypeDef = TypedDict(
    "ClientDescribeImagePermissionsResponseTypeDef",
    {
        "Name": str,
        "SharedImagePermissionsList": List[
            ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeImagesResponseImagesApplicationsTypeDef = TypedDict(
    "ClientDescribeImagesResponseImagesApplicationsTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "IconURL": str,
        "LaunchPath": str,
        "LaunchParameters": str,
        "Enabled": bool,
        "Metadata": Dict[str, str],
    },
    total=False,
)

ClientDescribeImagesResponseImagesImagePermissionsTypeDef = TypedDict(
    "ClientDescribeImagesResponseImagesImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)

ClientDescribeImagesResponseImagesStateChangeReasonTypeDef = TypedDict(
    "ClientDescribeImagesResponseImagesStateChangeReasonTypeDef",
    {
        "Code": Literal["INTERNAL_ERROR", "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE"],
        "Message": str,
    },
    total=False,
)

ClientDescribeImagesResponseImagesTypeDef = TypedDict(
    "ClientDescribeImagesResponseImagesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": Literal["PENDING", "AVAILABLE", "FAILED", "COPYING", "DELETING"],
        "Visibility": Literal["PUBLIC", "PRIVATE", "SHARED"],
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "Description": str,
        "StateChangeReason": ClientDescribeImagesResponseImagesStateChangeReasonTypeDef,
        "Applications": List[ClientDescribeImagesResponseImagesApplicationsTypeDef],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": ClientDescribeImagesResponseImagesImagePermissionsTypeDef,
    },
    total=False,
)

ClientDescribeImagesResponseTypeDef = TypedDict(
    "ClientDescribeImagesResponseTypeDef",
    {"Images": List[ClientDescribeImagesResponseImagesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef = TypedDict(
    "ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)

ClientDescribeSessionsResponseSessionsTypeDef = TypedDict(
    "ClientDescribeSessionsResponseSessionsTypeDef",
    {
        "Id": str,
        "UserId": str,
        "StackName": str,
        "FleetName": str,
        "State": Literal["ACTIVE", "PENDING", "EXPIRED"],
        "ConnectionState": Literal["CONNECTED", "NOT_CONNECTED"],
        "StartTime": datetime,
        "MaxExpirationTime": datetime,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "NetworkAccessConfiguration": ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeSessionsResponseTypeDef = TypedDict(
    "ClientDescribeSessionsResponseTypeDef",
    {"Sessions": List[ClientDescribeSessionsResponseSessionsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeStacksResponseStacksAccessEndpointsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

ClientDescribeStacksResponseStacksApplicationSettingsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)

ClientDescribeStacksResponseStacksStackErrorsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksStackErrorsTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientDescribeStacksResponseStacksStorageConnectorsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksStorageConnectorsTypeDef",
    {
        "ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"],
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)

ClientDescribeStacksResponseStacksUserSettingsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksUserSettingsTypeDef",
    {
        "Action": Literal[
            "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
            "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
            "FILE_UPLOAD",
            "FILE_DOWNLOAD",
            "PRINTING_TO_LOCAL_DEVICE",
        ],
        "Permission": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List[ClientDescribeStacksResponseStacksStorageConnectorsTypeDef],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List[ClientDescribeStacksResponseStacksStackErrorsTypeDef],
        "UserSettings": List[ClientDescribeStacksResponseStacksUserSettingsTypeDef],
        "ApplicationSettings": ClientDescribeStacksResponseStacksApplicationSettingsTypeDef,
        "AccessEndpoints": List[ClientDescribeStacksResponseStacksAccessEndpointsTypeDef],
        "EmbedHostDomains": List[str],
    },
    total=False,
)

ClientDescribeStacksResponseTypeDef = TypedDict(
    "ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef = TypedDict(
    "ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef",
    {
        "ErrorCode": Literal["RESOURCE_NOT_FOUND", "ACCESS_DENIED", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef = TypedDict(
    "ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef",
    {
        "S3BucketName": str,
        "Schedule": str,
        "LastGeneratedReportDate": datetime,
        "SubscriptionErrors": List[
            ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef
        ],
    },
    total=False,
)

ClientDescribeUsageReportSubscriptionsResponseTypeDef = TypedDict(
    "ClientDescribeUsageReportSubscriptionsResponseTypeDef",
    {
        "UsageReportSubscriptions": List[
            ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef = TypedDict(
    "ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)

ClientDescribeUserStackAssociationsResponseTypeDef = TypedDict(
    "ClientDescribeUserStackAssociationsResponseTypeDef",
    {
        "UserStackAssociations": List[
            ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeUsersResponseUsersTypeDef = TypedDict(
    "ClientDescribeUsersResponseUsersTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Enabled": bool,
        "Status": str,
        "FirstName": str,
        "LastName": str,
        "CreatedTime": datetime,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
    },
    total=False,
)

ClientDescribeUsersResponseTypeDef = TypedDict(
    "ClientDescribeUsersResponseTypeDef",
    {"Users": List[ClientDescribeUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)

ClientListAssociatedFleetsResponseTypeDef = TypedDict(
    "ClientListAssociatedFleetsResponseTypeDef", {"Names": List[str], "NextToken": str}, total=False
)

ClientListAssociatedStacksResponseTypeDef = TypedDict(
    "ClientListAssociatedStacksResponseTypeDef", {"Names": List[str], "NextToken": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)

ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)

ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientStartImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "ClientStartImageBuilderResponseImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "IamRoleArn": str,
        "State": Literal[
            "PENDING",
            "UPDATING_AGENT",
            "RUNNING",
            "STOPPING",
            "STOPPED",
            "REBOOTING",
            "SNAPSHOTTING",
            "DELETING",
            "FAILED",
        ],
        "StateChangeReason": ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef],
    },
    total=False,
)

ClientStartImageBuilderResponseTypeDef = TypedDict(
    "ClientStartImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientStartImageBuilderResponseImageBuilderTypeDef},
    total=False,
)

ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)

ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)

ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientStopImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "ClientStopImageBuilderResponseImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "IamRoleArn": str,
        "State": Literal[
            "PENDING",
            "UPDATING_AGENT",
            "RUNNING",
            "STOPPING",
            "STOPPED",
            "REBOOTING",
            "SNAPSHOTTING",
            "DELETING",
            "FAILED",
        ],
        "StateChangeReason": ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef],
    },
    total=False,
)

ClientStopImageBuilderResponseTypeDef = TypedDict(
    "ClientStopImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientStopImageBuilderResponseImageBuilderTypeDef},
    total=False,
)

ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)

ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef = TypedDict(
    "ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientUpdateDirectoryConfigResponseTypeDef = TypedDict(
    "ClientUpdateDirectoryConfigResponseTypeDef",
    {"DirectoryConfig": ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef},
    total=False,
)

_RequiredClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_RequiredClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef", {"AccountName": str}
)
_OptionalClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_OptionalClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountPassword": str},
    total=False,
)


class ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef(
    _RequiredClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef,
    _OptionalClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef,
):
    pass


ClientUpdateFleetComputeCapacityTypeDef = TypedDict(
    "ClientUpdateFleetComputeCapacityTypeDef", {"DesiredInstances": int}
)

ClientUpdateFleetDomainJoinInfoTypeDef = TypedDict(
    "ClientUpdateFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef = TypedDict(
    "ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)

ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef = TypedDict(
    "ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

ClientUpdateFleetResponseFleetFleetErrorsTypeDef = TypedDict(
    "ClientUpdateFleetResponseFleetFleetErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientUpdateFleetResponseFleetVpcConfigTypeDef = TypedDict(
    "ClientUpdateFleetResponseFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientUpdateFleetResponseFleetTypeDef = TypedDict(
    "ClientUpdateFleetResponseFleetTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "InstanceType": str,
        "FleetType": Literal["ALWAYS_ON", "ON_DEMAND"],
        "ComputeCapacityStatus": ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "State": Literal["STARTING", "RUNNING", "STOPPING", "STOPPED"],
        "VpcConfig": ClientUpdateFleetResponseFleetVpcConfigTypeDef,
        "CreatedTime": datetime,
        "FleetErrors": List[ClientUpdateFleetResponseFleetFleetErrorsTypeDef],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef,
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
    },
    total=False,
)

ClientUpdateFleetResponseTypeDef = TypedDict(
    "ClientUpdateFleetResponseTypeDef",
    {"Fleet": ClientUpdateFleetResponseFleetTypeDef},
    total=False,
)

ClientUpdateFleetVpcConfigTypeDef = TypedDict(
    "ClientUpdateFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientUpdateImagePermissionsImagePermissionsTypeDef = TypedDict(
    "ClientUpdateImagePermissionsImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)

_RequiredClientUpdateStackAccessEndpointsTypeDef = TypedDict(
    "_RequiredClientUpdateStackAccessEndpointsTypeDef", {"EndpointType": str}
)
_OptionalClientUpdateStackAccessEndpointsTypeDef = TypedDict(
    "_OptionalClientUpdateStackAccessEndpointsTypeDef", {"VpceId": str}, total=False
)


class ClientUpdateStackAccessEndpointsTypeDef(
    _RequiredClientUpdateStackAccessEndpointsTypeDef,
    _OptionalClientUpdateStackAccessEndpointsTypeDef,
):
    pass


_RequiredClientUpdateStackApplicationSettingsTypeDef = TypedDict(
    "_RequiredClientUpdateStackApplicationSettingsTypeDef", {"Enabled": bool}
)
_OptionalClientUpdateStackApplicationSettingsTypeDef = TypedDict(
    "_OptionalClientUpdateStackApplicationSettingsTypeDef", {"SettingsGroup": str}, total=False
)


class ClientUpdateStackApplicationSettingsTypeDef(
    _RequiredClientUpdateStackApplicationSettingsTypeDef,
    _OptionalClientUpdateStackApplicationSettingsTypeDef,
):
    pass


ClientUpdateStackResponseStackAccessEndpointsTypeDef = TypedDict(
    "ClientUpdateStackResponseStackAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

ClientUpdateStackResponseStackApplicationSettingsTypeDef = TypedDict(
    "ClientUpdateStackResponseStackApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)

ClientUpdateStackResponseStackStackErrorsTypeDef = TypedDict(
    "ClientUpdateStackResponseStackStackErrorsTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientUpdateStackResponseStackStorageConnectorsTypeDef = TypedDict(
    "ClientUpdateStackResponseStackStorageConnectorsTypeDef",
    {
        "ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"],
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)

ClientUpdateStackResponseStackUserSettingsTypeDef = TypedDict(
    "ClientUpdateStackResponseStackUserSettingsTypeDef",
    {
        "Action": Literal[
            "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
            "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
            "FILE_UPLOAD",
            "FILE_DOWNLOAD",
            "PRINTING_TO_LOCAL_DEVICE",
        ],
        "Permission": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientUpdateStackResponseStackTypeDef = TypedDict(
    "ClientUpdateStackResponseStackTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List[ClientUpdateStackResponseStackStorageConnectorsTypeDef],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List[ClientUpdateStackResponseStackStackErrorsTypeDef],
        "UserSettings": List[ClientUpdateStackResponseStackUserSettingsTypeDef],
        "ApplicationSettings": ClientUpdateStackResponseStackApplicationSettingsTypeDef,
        "AccessEndpoints": List[ClientUpdateStackResponseStackAccessEndpointsTypeDef],
        "EmbedHostDomains": List[str],
    },
    total=False,
)

ClientUpdateStackResponseTypeDef = TypedDict(
    "ClientUpdateStackResponseTypeDef",
    {"Stack": ClientUpdateStackResponseStackTypeDef},
    total=False,
)

_RequiredClientUpdateStackStorageConnectorsTypeDef = TypedDict(
    "_RequiredClientUpdateStackStorageConnectorsTypeDef",
    {"ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"]},
)
_OptionalClientUpdateStackStorageConnectorsTypeDef = TypedDict(
    "_OptionalClientUpdateStackStorageConnectorsTypeDef",
    {"ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class ClientUpdateStackStorageConnectorsTypeDef(
    _RequiredClientUpdateStackStorageConnectorsTypeDef,
    _OptionalClientUpdateStackStorageConnectorsTypeDef,
):
    pass


_RequiredClientUpdateStackUserSettingsTypeDef = TypedDict(
    "_RequiredClientUpdateStackUserSettingsTypeDef",
    {
        "Action": Literal[
            "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
            "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
            "FILE_UPLOAD",
            "FILE_DOWNLOAD",
            "PRINTING_TO_LOCAL_DEVICE",
        ]
    },
)
_OptionalClientUpdateStackUserSettingsTypeDef = TypedDict(
    "_OptionalClientUpdateStackUserSettingsTypeDef",
    {"Permission": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientUpdateStackUserSettingsTypeDef(
    _RequiredClientUpdateStackUserSettingsTypeDef, _OptionalClientUpdateStackUserSettingsTypeDef
):
    pass


DescribeDirectoryConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeDirectoryConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef = TypedDict(
    "DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)

DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef = TypedDict(
    "DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)

DescribeDirectoryConfigsPaginateResponseTypeDef = TypedDict(
    "DescribeDirectoryConfigsPaginateResponseTypeDef",
    {"DirectoryConfigs": List[DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef]},
    total=False,
)

DescribeFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef = TypedDict(
    "DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)

DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef = TypedDict(
    "DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef = TypedDict(
    "DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef = TypedDict(
    "DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

DescribeFleetsPaginateResponseFleetsTypeDef = TypedDict(
    "DescribeFleetsPaginateResponseFleetsTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "InstanceType": str,
        "FleetType": Literal["ALWAYS_ON", "ON_DEMAND"],
        "ComputeCapacityStatus": DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "State": Literal["STARTING", "RUNNING", "STOPPING", "STOPPED"],
        "VpcConfig": DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef,
        "CreatedTime": datetime,
        "FleetErrors": List[DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef,
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
    },
    total=False,
)

DescribeFleetsPaginateResponseTypeDef = TypedDict(
    "DescribeFleetsPaginateResponseTypeDef",
    {"Fleets": List[DescribeFleetsPaginateResponseFleetsTypeDef]},
    total=False,
)

DescribeImageBuildersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeImageBuildersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef = TypedDict(
    "DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef = TypedDict(
    "DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef = TypedDict(
    "DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef = TypedDict(
    "DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)

DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef = TypedDict(
    "DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)

DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef = TypedDict(
    "DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

DescribeImageBuildersPaginateResponseImageBuildersTypeDef = TypedDict(
    "DescribeImageBuildersPaginateResponseImageBuildersTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef,
        "InstanceType": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "IamRoleArn": str,
        "State": Literal[
            "PENDING",
            "UPDATING_AGENT",
            "RUNNING",
            "STOPPING",
            "STOPPED",
            "REBOOTING",
            "SNAPSHOTTING",
            "DELETING",
            "FAILED",
        ],
        "StateChangeReason": DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef,
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef,
        "NetworkAccessConfiguration": DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef,
        "ImageBuilderErrors": List[
            DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef
        ],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List[
            DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef
        ],
    },
    total=False,
)

DescribeImageBuildersPaginateResponseTypeDef = TypedDict(
    "DescribeImageBuildersPaginateResponseTypeDef",
    {"ImageBuilders": List[DescribeImageBuildersPaginateResponseImageBuildersTypeDef]},
    total=False,
)

DescribeImagesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeImagesPaginateResponseImagesApplicationsTypeDef = TypedDict(
    "DescribeImagesPaginateResponseImagesApplicationsTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "IconURL": str,
        "LaunchPath": str,
        "LaunchParameters": str,
        "Enabled": bool,
        "Metadata": Dict[str, str],
    },
    total=False,
)

DescribeImagesPaginateResponseImagesImagePermissionsTypeDef = TypedDict(
    "DescribeImagesPaginateResponseImagesImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)

DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef = TypedDict(
    "DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef",
    {
        "Code": Literal["INTERNAL_ERROR", "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE"],
        "Message": str,
    },
    total=False,
)

DescribeImagesPaginateResponseImagesTypeDef = TypedDict(
    "DescribeImagesPaginateResponseImagesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": Literal["PENDING", "AVAILABLE", "FAILED", "COPYING", "DELETING"],
        "Visibility": Literal["PUBLIC", "PRIVATE", "SHARED"],
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "Description": str,
        "StateChangeReason": DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef,
        "Applications": List[DescribeImagesPaginateResponseImagesApplicationsTypeDef],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": DescribeImagesPaginateResponseImagesImagePermissionsTypeDef,
    },
    total=False,
)

DescribeImagesPaginateResponseTypeDef = TypedDict(
    "DescribeImagesPaginateResponseTypeDef",
    {"Images": List[DescribeImagesPaginateResponseImagesTypeDef]},
    total=False,
)

DescribeSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef = TypedDict(
    "DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)

DescribeSessionsPaginateResponseSessionsTypeDef = TypedDict(
    "DescribeSessionsPaginateResponseSessionsTypeDef",
    {
        "Id": str,
        "UserId": str,
        "StackName": str,
        "FleetName": str,
        "State": Literal["ACTIVE", "PENDING", "EXPIRED"],
        "ConnectionState": Literal["CONNECTED", "NOT_CONNECTED"],
        "StartTime": datetime,
        "MaxExpirationTime": datetime,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "NetworkAccessConfiguration": DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef,
    },
    total=False,
)

DescribeSessionsPaginateResponseTypeDef = TypedDict(
    "DescribeSessionsPaginateResponseTypeDef",
    {"Sessions": List[DescribeSessionsPaginateResponseSessionsTypeDef]},
    total=False,
)

DescribeStacksPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)

DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)

DescribeStacksPaginateResponseStacksStackErrorsTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksStackErrorsTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef",
    {
        "ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"],
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)

DescribeStacksPaginateResponseStacksUserSettingsTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksUserSettingsTypeDef",
    {
        "Action": Literal[
            "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
            "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
            "FILE_UPLOAD",
            "FILE_DOWNLOAD",
            "PRINTING_TO_LOCAL_DEVICE",
        ],
        "Permission": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

DescribeStacksPaginateResponseStacksTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List[DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List[DescribeStacksPaginateResponseStacksStackErrorsTypeDef],
        "UserSettings": List[DescribeStacksPaginateResponseStacksUserSettingsTypeDef],
        "ApplicationSettings": DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef,
        "AccessEndpoints": List[DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef],
        "EmbedHostDomains": List[str],
    },
    total=False,
)

DescribeStacksPaginateResponseTypeDef = TypedDict(
    "DescribeStacksPaginateResponseTypeDef",
    {"Stacks": List[DescribeStacksPaginateResponseStacksTypeDef]},
    total=False,
)

DescribeUserStackAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeUserStackAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef = TypedDict(
    "DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)

DescribeUserStackAssociationsPaginateResponseTypeDef = TypedDict(
    "DescribeUserStackAssociationsPaginateResponseTypeDef",
    {
        "UserStackAssociations": List[
            DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef
        ]
    },
    total=False,
)

DescribeUsersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeUsersPaginateResponseUsersTypeDef = TypedDict(
    "DescribeUsersPaginateResponseUsersTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Enabled": bool,
        "Status": str,
        "FirstName": str,
        "LastName": str,
        "CreatedTime": datetime,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
    },
    total=False,
)

DescribeUsersPaginateResponseTypeDef = TypedDict(
    "DescribeUsersPaginateResponseTypeDef",
    {"Users": List[DescribeUsersPaginateResponseUsersTypeDef]},
    total=False,
)

FleetStartedWaitWaiterConfigTypeDef = TypedDict(
    "FleetStartedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

FleetStoppedWaitWaiterConfigTypeDef = TypedDict(
    "FleetStoppedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ListAssociatedFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssociatedFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListAssociatedFleetsPaginateResponseTypeDef = TypedDict(
    "ListAssociatedFleetsPaginateResponseTypeDef", {"Names": List[str]}, total=False
)

ListAssociatedStacksPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssociatedStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListAssociatedStacksPaginateResponseTypeDef = TypedDict(
    "ListAssociatedStacksPaginateResponseTypeDef", {"Names": List[str]}, total=False
)
