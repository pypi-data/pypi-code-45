"Main interface for appstream service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef",
    "ClientBatchAssociateUserStackResponseerrorsTypeDef",
    "ClientBatchAssociateUserStackResponseTypeDef",
    "ClientBatchAssociateUserStackUserStackAssociationsTypeDef",
    "ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef",
    "ClientBatchDisassociateUserStackResponseerrorsTypeDef",
    "ClientBatchDisassociateUserStackResponseTypeDef",
    "ClientBatchDisassociateUserStackUserStackAssociationsTypeDef",
    "ClientCopyImageResponseTypeDef",
    "ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    "ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef",
    "ClientCreateDirectoryConfigResponseTypeDef",
    "ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef",
    "ClientCreateFleetComputeCapacityTypeDef",
    "ClientCreateFleetDomainJoinInfoTypeDef",
    "ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef",
    "ClientCreateFleetResponseFleetDomainJoinInfoTypeDef",
    "ClientCreateFleetResponseFleetFleetErrorsTypeDef",
    "ClientCreateFleetResponseFleetVpcConfigTypeDef",
    "ClientCreateFleetResponseFleetTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientCreateFleetVpcConfigTypeDef",
    "ClientCreateImageBuilderAccessEndpointsTypeDef",
    "ClientCreateImageBuilderDomainJoinInfoTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef",
    "ClientCreateImageBuilderResponseImageBuilderTypeDef",
    "ClientCreateImageBuilderResponseTypeDef",
    "ClientCreateImageBuilderStreamingUrlResponseTypeDef",
    "ClientCreateImageBuilderVpcConfigTypeDef",
    "ClientCreateStackAccessEndpointsTypeDef",
    "ClientCreateStackApplicationSettingsTypeDef",
    "ClientCreateStackResponseStackAccessEndpointsTypeDef",
    "ClientCreateStackResponseStackApplicationSettingsTypeDef",
    "ClientCreateStackResponseStackStackErrorsTypeDef",
    "ClientCreateStackResponseStackStorageConnectorsTypeDef",
    "ClientCreateStackResponseStackUserSettingsTypeDef",
    "ClientCreateStackResponseStackTypeDef",
    "ClientCreateStackResponseTypeDef",
    "ClientCreateStackStorageConnectorsTypeDef",
    "ClientCreateStackUserSettingsTypeDef",
    "ClientCreateStreamingUrlResponseTypeDef",
    "ClientCreateUsageReportSubscriptionResponseTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef",
    "ClientDeleteImageBuilderResponseImageBuilderTypeDef",
    "ClientDeleteImageBuilderResponseTypeDef",
    "ClientDeleteImageResponseImageApplicationsTypeDef",
    "ClientDeleteImageResponseImageImagePermissionsTypeDef",
    "ClientDeleteImageResponseImageStateChangeReasonTypeDef",
    "ClientDeleteImageResponseImageTypeDef",
    "ClientDeleteImageResponseTypeDef",
    "ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    "ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef",
    "ClientDescribeDirectoryConfigsResponseTypeDef",
    "ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef",
    "ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef",
    "ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef",
    "ClientDescribeFleetsResponseFleetsVpcConfigTypeDef",
    "ClientDescribeFleetsResponseFleetsTypeDef",
    "ClientDescribeFleetsResponseTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef",
    "ClientDescribeImageBuildersResponseImageBuildersTypeDef",
    "ClientDescribeImageBuildersResponseTypeDef",
    "ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef",
    "ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef",
    "ClientDescribeImagePermissionsResponseTypeDef",
    "ClientDescribeImagesResponseImagesApplicationsTypeDef",
    "ClientDescribeImagesResponseImagesImagePermissionsTypeDef",
    "ClientDescribeImagesResponseImagesStateChangeReasonTypeDef",
    "ClientDescribeImagesResponseImagesTypeDef",
    "ClientDescribeImagesResponseTypeDef",
    "ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef",
    "ClientDescribeSessionsResponseSessionsTypeDef",
    "ClientDescribeSessionsResponseTypeDef",
    "ClientDescribeStacksResponseStacksAccessEndpointsTypeDef",
    "ClientDescribeStacksResponseStacksApplicationSettingsTypeDef",
    "ClientDescribeStacksResponseStacksStackErrorsTypeDef",
    "ClientDescribeStacksResponseStacksStorageConnectorsTypeDef",
    "ClientDescribeStacksResponseStacksUserSettingsTypeDef",
    "ClientDescribeStacksResponseStacksTypeDef",
    "ClientDescribeStacksResponseTypeDef",
    "ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef",
    "ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef",
    "ClientDescribeUsageReportSubscriptionsResponseTypeDef",
    "ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef",
    "ClientDescribeUserStackAssociationsResponseTypeDef",
    "ClientDescribeUsersResponseUsersTypeDef",
    "ClientDescribeUsersResponseTypeDef",
    "ClientListAssociatedFleetsResponseTypeDef",
    "ClientListAssociatedStacksResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    "ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    "ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    "ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    "ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    "ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef",
    "ClientStartImageBuilderResponseImageBuilderTypeDef",
    "ClientStartImageBuilderResponseTypeDef",
    "ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    "ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    "ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
    "ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    "ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    "ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef",
    "ClientStopImageBuilderResponseImageBuilderTypeDef",
    "ClientStopImageBuilderResponseTypeDef",
    "ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    "ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef",
    "ClientUpdateDirectoryConfigResponseTypeDef",
    "ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef",
    "ClientUpdateFleetComputeCapacityTypeDef",
    "ClientUpdateFleetDomainJoinInfoTypeDef",
    "ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef",
    "ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef",
    "ClientUpdateFleetResponseFleetFleetErrorsTypeDef",
    "ClientUpdateFleetResponseFleetVpcConfigTypeDef",
    "ClientUpdateFleetResponseFleetTypeDef",
    "ClientUpdateFleetResponseTypeDef",
    "ClientUpdateFleetVpcConfigTypeDef",
    "ClientUpdateImagePermissionsImagePermissionsTypeDef",
    "ClientUpdateStackAccessEndpointsTypeDef",
    "ClientUpdateStackApplicationSettingsTypeDef",
    "ClientUpdateStackResponseStackAccessEndpointsTypeDef",
    "ClientUpdateStackResponseStackApplicationSettingsTypeDef",
    "ClientUpdateStackResponseStackStackErrorsTypeDef",
    "ClientUpdateStackResponseStackStorageConnectorsTypeDef",
    "ClientUpdateStackResponseStackUserSettingsTypeDef",
    "ClientUpdateStackResponseStackTypeDef",
    "ClientUpdateStackResponseTypeDef",
    "ClientUpdateStackStorageConnectorsTypeDef",
    "ClientUpdateStackUserSettingsTypeDef",
    "DescribeDirectoryConfigsPaginatePaginationConfigTypeDef",
    "DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    "DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef",
    "DescribeDirectoryConfigsPaginateResponseTypeDef",
    "DescribeFleetsPaginatePaginationConfigTypeDef",
    "DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef",
    "DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef",
    "DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef",
    "DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef",
    "DescribeFleetsPaginateResponseFleetsTypeDef",
    "DescribeFleetsPaginateResponseTypeDef",
    "DescribeImageBuildersPaginatePaginationConfigTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef",
    "DescribeImageBuildersPaginateResponseImageBuildersTypeDef",
    "DescribeImageBuildersPaginateResponseTypeDef",
    "DescribeImagesPaginatePaginationConfigTypeDef",
    "DescribeImagesPaginateResponseImagesApplicationsTypeDef",
    "DescribeImagesPaginateResponseImagesImagePermissionsTypeDef",
    "DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef",
    "DescribeImagesPaginateResponseImagesTypeDef",
    "DescribeImagesPaginateResponseTypeDef",
    "DescribeSessionsPaginatePaginationConfigTypeDef",
    "DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef",
    "DescribeSessionsPaginateResponseSessionsTypeDef",
    "DescribeSessionsPaginateResponseTypeDef",
    "DescribeStacksPaginatePaginationConfigTypeDef",
    "DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef",
    "DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef",
    "DescribeStacksPaginateResponseStacksStackErrorsTypeDef",
    "DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef",
    "DescribeStacksPaginateResponseStacksUserSettingsTypeDef",
    "DescribeStacksPaginateResponseStacksTypeDef",
    "DescribeStacksPaginateResponseTypeDef",
    "DescribeUserStackAssociationsPaginatePaginationConfigTypeDef",
    "DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef",
    "DescribeUserStackAssociationsPaginateResponseTypeDef",
    "DescribeUsersPaginatePaginationConfigTypeDef",
    "DescribeUsersPaginateResponseUsersTypeDef",
    "DescribeUsersPaginateResponseTypeDef",
    "FleetStartedWaitWaiterConfigTypeDef",
    "FleetStoppedWaitWaiterConfigTypeDef",
    "ListAssociatedFleetsPaginatePaginationConfigTypeDef",
    "ListAssociatedFleetsPaginateResponseTypeDef",
    "ListAssociatedStacksPaginatePaginationConfigTypeDef",
    "ListAssociatedStacksPaginateResponseTypeDef",
)


_ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef = TypedDict(
    "_ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)


class ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef(
    _ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef
):
    """
    - **UserStackAssociation** *(dict) --*

      Information about the user and associated stack.
      - **StackName** *(string) --*

        The name of the stack that is associated with the user.
    """


_ClientBatchAssociateUserStackResponseerrorsTypeDef = TypedDict(
    "_ClientBatchAssociateUserStackResponseerrorsTypeDef",
    {
        "UserStackAssociation": ClientBatchAssociateUserStackResponseerrorsUserStackAssociationTypeDef,
        "ErrorCode": Literal["STACK_NOT_FOUND", "USER_NAME_NOT_FOUND", "INTERNAL_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchAssociateUserStackResponseerrorsTypeDef(
    _ClientBatchAssociateUserStackResponseerrorsTypeDef
):
    """
    - *(dict) --*

      Describes the error that is returned when a user can’t be associated with or disassociated
      from a stack.
      - **UserStackAssociation** *(dict) --*

        Information about the user and associated stack.
        - **StackName** *(string) --*

          The name of the stack that is associated with the user.
    """


_ClientBatchAssociateUserStackResponseTypeDef = TypedDict(
    "_ClientBatchAssociateUserStackResponseTypeDef",
    {"errors": List[ClientBatchAssociateUserStackResponseerrorsTypeDef]},
    total=False,
)


class ClientBatchAssociateUserStackResponseTypeDef(_ClientBatchAssociateUserStackResponseTypeDef):
    """
    - *(dict) --*

      - **errors** *(list) --*

        The list of UserStackAssociationError objects.
        - *(dict) --*

          Describes the error that is returned when a user can’t be associated with or disassociated
          from a stack.
          - **UserStackAssociation** *(dict) --*

            Information about the user and associated stack.
            - **StackName** *(string) --*

              The name of the stack that is associated with the user.
    """


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
    """
    - *(dict) --*

      Describes a user in the user pool and the associated stack.
      - **StackName** *(string) --***[REQUIRED]**

        The name of the stack that is associated with the user.
    """


_ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef = TypedDict(
    "_ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)


class ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef(
    _ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef
):
    """
    - **UserStackAssociation** *(dict) --*

      Information about the user and associated stack.
      - **StackName** *(string) --*

        The name of the stack that is associated with the user.
    """


_ClientBatchDisassociateUserStackResponseerrorsTypeDef = TypedDict(
    "_ClientBatchDisassociateUserStackResponseerrorsTypeDef",
    {
        "UserStackAssociation": ClientBatchDisassociateUserStackResponseerrorsUserStackAssociationTypeDef,
        "ErrorCode": Literal["STACK_NOT_FOUND", "USER_NAME_NOT_FOUND", "INTERNAL_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchDisassociateUserStackResponseerrorsTypeDef(
    _ClientBatchDisassociateUserStackResponseerrorsTypeDef
):
    """
    - *(dict) --*

      Describes the error that is returned when a user can’t be associated with or disassociated
      from a stack.
      - **UserStackAssociation** *(dict) --*

        Information about the user and associated stack.
        - **StackName** *(string) --*

          The name of the stack that is associated with the user.
    """


_ClientBatchDisassociateUserStackResponseTypeDef = TypedDict(
    "_ClientBatchDisassociateUserStackResponseTypeDef",
    {"errors": List[ClientBatchDisassociateUserStackResponseerrorsTypeDef]},
    total=False,
)


class ClientBatchDisassociateUserStackResponseTypeDef(
    _ClientBatchDisassociateUserStackResponseTypeDef
):
    """
    - *(dict) --*

      - **errors** *(list) --*

        The list of UserStackAssociationError objects.
        - *(dict) --*

          Describes the error that is returned when a user can’t be associated with or disassociated
          from a stack.
          - **UserStackAssociation** *(dict) --*

            Information about the user and associated stack.
            - **StackName** *(string) --*

              The name of the stack that is associated with the user.
    """


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
    """
    - *(dict) --*

      Describes a user in the user pool and the associated stack.
      - **StackName** *(string) --***[REQUIRED]**

        The name of the stack that is associated with the user.
    """


_ClientCopyImageResponseTypeDef = TypedDict(
    "_ClientCopyImageResponseTypeDef", {"DestinationImageName": str}, total=False
)


class ClientCopyImageResponseTypeDef(_ClientCopyImageResponseTypeDef):
    """
    - *(dict) --*

      - **DestinationImageName** *(string) --*

        The name of the destination image.
    """


_ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)


class ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef(
    _ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef
):
    pass


_ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef = TypedDict(
    "_ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientCreateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef(
    _ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef
):
    """
    - **DirectoryConfig** *(dict) --*

      Information about the directory configuration.
      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).
    """


_ClientCreateDirectoryConfigResponseTypeDef = TypedDict(
    "_ClientCreateDirectoryConfigResponseTypeDef",
    {"DirectoryConfig": ClientCreateDirectoryConfigResponseDirectoryConfigTypeDef},
    total=False,
)


class ClientCreateDirectoryConfigResponseTypeDef(_ClientCreateDirectoryConfigResponseTypeDef):
    """
    - *(dict) --*

      - **DirectoryConfig** *(dict) --*

        Information about the directory configuration.
        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).
    """


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
    """
    The credentials for the service account used by the fleet or image builder to connect to the
    directory.
    - **AccountName** *(string) --***[REQUIRED]**

      The user name of the account. This account must have the following privileges: create computer
      objects, join computers to the domain, and change/reset the password on descendant computer
      objects for the organizational units specified.
    """


_ClientCreateFleetComputeCapacityTypeDef = TypedDict(
    "_ClientCreateFleetComputeCapacityTypeDef", {"DesiredInstances": int}
)


class ClientCreateFleetComputeCapacityTypeDef(_ClientCreateFleetComputeCapacityTypeDef):
    """
    The desired capacity for the fleet.
    - **DesiredInstances** *(integer) --***[REQUIRED]**

      The desired number of streaming instances.
    """


_ClientCreateFleetDomainJoinInfoTypeDef = TypedDict(
    "_ClientCreateFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientCreateFleetDomainJoinInfoTypeDef(_ClientCreateFleetDomainJoinInfoTypeDef):
    """
    The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft
    Active Directory domain.
    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).
    """


_ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)


class ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef(
    _ClientCreateFleetResponseFleetComputeCapacityStatusTypeDef
):
    pass


_ClientCreateFleetResponseFleetDomainJoinInfoTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientCreateFleetResponseFleetDomainJoinInfoTypeDef(
    _ClientCreateFleetResponseFleetDomainJoinInfoTypeDef
):
    pass


_ClientCreateFleetResponseFleetFleetErrorsTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetFleetErrorsTypeDef",
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


class ClientCreateFleetResponseFleetFleetErrorsTypeDef(
    _ClientCreateFleetResponseFleetFleetErrorsTypeDef
):
    pass


_ClientCreateFleetResponseFleetVpcConfigTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateFleetResponseFleetVpcConfigTypeDef(
    _ClientCreateFleetResponseFleetVpcConfigTypeDef
):
    pass


_ClientCreateFleetResponseFleetTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetTypeDef",
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


class ClientCreateFleetResponseFleetTypeDef(_ClientCreateFleetResponseFleetTypeDef):
    """
    - **Fleet** *(dict) --*

      Information about the fleet.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the fleet.
    """


_ClientCreateFleetResponseTypeDef = TypedDict(
    "_ClientCreateFleetResponseTypeDef",
    {"Fleet": ClientCreateFleetResponseFleetTypeDef},
    total=False,
)


class ClientCreateFleetResponseTypeDef(_ClientCreateFleetResponseTypeDef):
    """
    - *(dict) --*

      - **Fleet** *(dict) --*

        Information about the fleet.
        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) for the fleet.
    """


_ClientCreateFleetVpcConfigTypeDef = TypedDict(
    "_ClientCreateFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateFleetVpcConfigTypeDef(_ClientCreateFleetVpcConfigTypeDef):
    """
    The VPC configuration for the fleet.
    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image builder
      instances use one subnet.
      - *(string) --*
    """


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
    """
    - *(dict) --*

      Describes an interface VPC endpoint (interface endpoint) that lets you create a private
      connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When
      you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0
      only through that endpoint. When you specify an interface endpoint for an image builder,
      administrators can connect to the image builder only through that endpoint.
      - **EndpointType** *(string) --***[REQUIRED]**

        The type of interface endpoint.
    """


_ClientCreateImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientCreateImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientCreateImageBuilderDomainJoinInfoTypeDef(_ClientCreateImageBuilderDomainJoinInfoTypeDef):
    """
    The name of the directory and organizational unit (OU) to use to join the image builder to a
    Microsoft Active Directory domain.
    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).
    """


_ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderAccessEndpointsTypeDef
):
    pass


_ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderDomainJoinInfoTypeDef
):
    pass


_ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
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


class ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
):
    pass


_ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef
):
    pass


_ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderStateChangeReasonTypeDef
):
    pass


_ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderVpcConfigTypeDef
):
    pass


_ClientCreateImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseImageBuilderTypeDef",
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


class ClientCreateImageBuilderResponseImageBuilderTypeDef(
    _ClientCreateImageBuilderResponseImageBuilderTypeDef
):
    """
    - **ImageBuilder** *(dict) --*

      Information about the image builder.
      - **Name** *(string) --*

        The name of the image builder.
    """


_ClientCreateImageBuilderResponseTypeDef = TypedDict(
    "_ClientCreateImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientCreateImageBuilderResponseImageBuilderTypeDef},
    total=False,
)


class ClientCreateImageBuilderResponseTypeDef(_ClientCreateImageBuilderResponseTypeDef):
    """
    - *(dict) --*

      - **ImageBuilder** *(dict) --*

        Information about the image builder.
        - **Name** *(string) --*

          The name of the image builder.
    """


_ClientCreateImageBuilderStreamingUrlResponseTypeDef = TypedDict(
    "_ClientCreateImageBuilderStreamingUrlResponseTypeDef",
    {"StreamingURL": str, "Expires": datetime},
    total=False,
)


class ClientCreateImageBuilderStreamingUrlResponseTypeDef(
    _ClientCreateImageBuilderStreamingUrlResponseTypeDef
):
    """
    - *(dict) --*

      - **StreamingURL** *(string) --*

        The URL to start the AppStream 2.0 streaming session.
    """


_ClientCreateImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientCreateImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateImageBuilderVpcConfigTypeDef(_ClientCreateImageBuilderVpcConfigTypeDef):
    """
    The VPC configuration for the image builder. You can specify only one subnet.
    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image builder
      instances use one subnet.
      - *(string) --*
    """


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
    """
    - *(dict) --*

      Describes an interface VPC endpoint (interface endpoint) that lets you create a private
      connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When
      you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0
      only through that endpoint. When you specify an interface endpoint for an image builder,
      administrators can connect to the image builder only through that endpoint.
      - **EndpointType** *(string) --***[REQUIRED]**

        The type of interface endpoint.
    """


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
    """
    The persistent application settings for users of a stack. When these settings are enabled,
    changes that users make to applications and Windows settings are automatically saved after each
    session and applied to the next session.
    - **Enabled** *(boolean) --***[REQUIRED]**

      Enables or disables persistent application settings for users during their streaming sessions.
    """


_ClientCreateStackResponseStackAccessEndpointsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientCreateStackResponseStackAccessEndpointsTypeDef(
    _ClientCreateStackResponseStackAccessEndpointsTypeDef
):
    pass


_ClientCreateStackResponseStackApplicationSettingsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)


class ClientCreateStackResponseStackApplicationSettingsTypeDef(
    _ClientCreateStackResponseStackApplicationSettingsTypeDef
):
    pass


_ClientCreateStackResponseStackStackErrorsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackStackErrorsTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientCreateStackResponseStackStackErrorsTypeDef(
    _ClientCreateStackResponseStackStackErrorsTypeDef
):
    pass


_ClientCreateStackResponseStackStorageConnectorsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackStorageConnectorsTypeDef",
    {
        "ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"],
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)


class ClientCreateStackResponseStackStorageConnectorsTypeDef(
    _ClientCreateStackResponseStackStorageConnectorsTypeDef
):
    pass


_ClientCreateStackResponseStackUserSettingsTypeDef = TypedDict(
    "_ClientCreateStackResponseStackUserSettingsTypeDef",
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


class ClientCreateStackResponseStackUserSettingsTypeDef(
    _ClientCreateStackResponseStackUserSettingsTypeDef
):
    pass


_ClientCreateStackResponseStackTypeDef = TypedDict(
    "_ClientCreateStackResponseStackTypeDef",
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


class ClientCreateStackResponseStackTypeDef(_ClientCreateStackResponseStackTypeDef):
    """
    - **Stack** *(dict) --*

      Information about the stack.
      - **Arn** *(string) --*

        The ARN of the stack.
    """


_ClientCreateStackResponseTypeDef = TypedDict(
    "_ClientCreateStackResponseTypeDef",
    {"Stack": ClientCreateStackResponseStackTypeDef},
    total=False,
)


class ClientCreateStackResponseTypeDef(_ClientCreateStackResponseTypeDef):
    """
    - *(dict) --*

      - **Stack** *(dict) --*

        Information about the stack.
        - **Arn** *(string) --*

          The ARN of the stack.
    """


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
    """
    - *(dict) --*

      Describes a connector that enables persistent storage for users.
      - **ConnectorType** *(string) --***[REQUIRED]**

        The type of storage connector.
    """


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
    """
    - *(dict) --*

      Describes an action and whether the action is enabled or disabled for users during their
      streaming sessions.
      - **Action** *(string) --***[REQUIRED]**

        The action that is enabled or disabled.
    """


_ClientCreateStreamingUrlResponseTypeDef = TypedDict(
    "_ClientCreateStreamingUrlResponseTypeDef",
    {"StreamingURL": str, "Expires": datetime},
    total=False,
)


class ClientCreateStreamingUrlResponseTypeDef(_ClientCreateStreamingUrlResponseTypeDef):
    """
    - *(dict) --*

      - **StreamingURL** *(string) --*

        The URL to start the AppStream 2.0 streaming session.
    """


_ClientCreateUsageReportSubscriptionResponseTypeDef = TypedDict(
    "_ClientCreateUsageReportSubscriptionResponseTypeDef",
    {"S3BucketName": str, "Schedule": str},
    total=False,
)


class ClientCreateUsageReportSubscriptionResponseTypeDef(
    _ClientCreateUsageReportSubscriptionResponseTypeDef
):
    """
    - *(dict) --*

      - **S3BucketName** *(string) --*

        The Amazon S3 bucket where generated reports are stored.
        If you enabled on-instance session scripts and Amazon S3 logging for your session script
        configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket is
        unique to your account and Region. When you enable usage reporting in this case, AppStream
        2.0 uses the same bucket to store your usage reports. If you haven't already enabled
        on-instance session scripts, when you enable usage reports, AppStream 2.0 creates a new S3
        bucket.
    """


_ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderAccessEndpointsTypeDef
):
    pass


_ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderDomainJoinInfoTypeDef
):
    pass


_ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
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


class ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
):
    pass


_ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef
):
    pass


_ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderStateChangeReasonTypeDef
):
    pass


_ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderVpcConfigTypeDef
):
    pass


_ClientDeleteImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseImageBuilderTypeDef",
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


class ClientDeleteImageBuilderResponseImageBuilderTypeDef(
    _ClientDeleteImageBuilderResponseImageBuilderTypeDef
):
    """
    - **ImageBuilder** *(dict) --*

      Information about the image builder.
      - **Name** *(string) --*

        The name of the image builder.
    """


_ClientDeleteImageBuilderResponseTypeDef = TypedDict(
    "_ClientDeleteImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientDeleteImageBuilderResponseImageBuilderTypeDef},
    total=False,
)


class ClientDeleteImageBuilderResponseTypeDef(_ClientDeleteImageBuilderResponseTypeDef):
    """
    - *(dict) --*

      - **ImageBuilder** *(dict) --*

        Information about the image builder.
        - **Name** *(string) --*

          The name of the image builder.
    """


_ClientDeleteImageResponseImageApplicationsTypeDef = TypedDict(
    "_ClientDeleteImageResponseImageApplicationsTypeDef",
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


class ClientDeleteImageResponseImageApplicationsTypeDef(
    _ClientDeleteImageResponseImageApplicationsTypeDef
):
    pass


_ClientDeleteImageResponseImageImagePermissionsTypeDef = TypedDict(
    "_ClientDeleteImageResponseImageImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class ClientDeleteImageResponseImageImagePermissionsTypeDef(
    _ClientDeleteImageResponseImageImagePermissionsTypeDef
):
    pass


_ClientDeleteImageResponseImageStateChangeReasonTypeDef = TypedDict(
    "_ClientDeleteImageResponseImageStateChangeReasonTypeDef",
    {
        "Code": Literal["INTERNAL_ERROR", "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE"],
        "Message": str,
    },
    total=False,
)


class ClientDeleteImageResponseImageStateChangeReasonTypeDef(
    _ClientDeleteImageResponseImageStateChangeReasonTypeDef
):
    pass


_ClientDeleteImageResponseImageTypeDef = TypedDict(
    "_ClientDeleteImageResponseImageTypeDef",
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


class ClientDeleteImageResponseImageTypeDef(_ClientDeleteImageResponseImageTypeDef):
    """
    - **Image** *(dict) --*

      Information about the image.
      - **Name** *(string) --*

        The name of the image.
    """


_ClientDeleteImageResponseTypeDef = TypedDict(
    "_ClientDeleteImageResponseTypeDef",
    {"Image": ClientDeleteImageResponseImageTypeDef},
    total=False,
)


class ClientDeleteImageResponseTypeDef(_ClientDeleteImageResponseTypeDef):
    """
    - *(dict) --*

      - **Image** *(dict) --*

        Information about the image.
        - **Name** *(string) --*

          The name of the image.
    """


_ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef = TypedDict(
    "_ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)


class ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef(
    _ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef
):
    pass


_ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef = TypedDict(
    "_ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientDescribeDirectoryConfigsResponseDirectoryConfigsServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef(
    _ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef
):
    """
    - *(dict) --*

      Describes the configuration information required to join fleets and image builders to
      Microsoft Active Directory domains.
      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).
    """


_ClientDescribeDirectoryConfigsResponseTypeDef = TypedDict(
    "_ClientDescribeDirectoryConfigsResponseTypeDef",
    {
        "DirectoryConfigs": List[ClientDescribeDirectoryConfigsResponseDirectoryConfigsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDirectoryConfigsResponseTypeDef(_ClientDescribeDirectoryConfigsResponseTypeDef):
    """
    - *(dict) --*

      - **DirectoryConfigs** *(list) --*

        Information about the directory configurations. Note that although the response syntax in
        this topic includes the account password, this password is not returned in the actual
        response.
        - *(dict) --*

          Describes the configuration information required to join fleets and image builders to
          Microsoft Active Directory domains.
          - **DirectoryName** *(string) --*

            The fully qualified name of the directory (for example, corp.example.com).
    """


_ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)


class ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef(
    _ClientDescribeFleetsResponseFleetsComputeCapacityStatusTypeDef
):
    pass


_ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef(
    _ClientDescribeFleetsResponseFleetsDomainJoinInfoTypeDef
):
    pass


_ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef",
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


class ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef(
    _ClientDescribeFleetsResponseFleetsFleetErrorsTypeDef
):
    pass


_ClientDescribeFleetsResponseFleetsVpcConfigTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientDescribeFleetsResponseFleetsVpcConfigTypeDef(
    _ClientDescribeFleetsResponseFleetsVpcConfigTypeDef
):
    pass


_ClientDescribeFleetsResponseFleetsTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseFleetsTypeDef",
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


class ClientDescribeFleetsResponseFleetsTypeDef(_ClientDescribeFleetsResponseFleetsTypeDef):
    """
    - *(dict) --*

      Describes a fleet.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the fleet.
    """


_ClientDescribeFleetsResponseTypeDef = TypedDict(
    "_ClientDescribeFleetsResponseTypeDef",
    {"Fleets": List[ClientDescribeFleetsResponseFleetsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeFleetsResponseTypeDef(_ClientDescribeFleetsResponseTypeDef):
    """
    - *(dict) --*

      - **Fleets** *(list) --*

        Information about the fleets.
        - *(dict) --*

          Describes a fleet.
          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) for the fleet.
    """


_ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersAccessEndpointsTypeDef
):
    pass


_ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersDomainJoinInfoTypeDef
):
    pass


_ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef",
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


class ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersImageBuilderErrorsTypeDef
):
    pass


_ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersNetworkAccessConfigurationTypeDef
):
    pass


_ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersStateChangeReasonTypeDef
):
    pass


_ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersVpcConfigTypeDef
):
    pass


_ClientDescribeImageBuildersResponseImageBuildersTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseImageBuildersTypeDef",
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


class ClientDescribeImageBuildersResponseImageBuildersTypeDef(
    _ClientDescribeImageBuildersResponseImageBuildersTypeDef
):
    """
    - *(dict) --*

      Describes a virtual machine that is used to create an image.
      - **Name** *(string) --*

        The name of the image builder.
    """


_ClientDescribeImageBuildersResponseTypeDef = TypedDict(
    "_ClientDescribeImageBuildersResponseTypeDef",
    {
        "ImageBuilders": List[ClientDescribeImageBuildersResponseImageBuildersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeImageBuildersResponseTypeDef(_ClientDescribeImageBuildersResponseTypeDef):
    """
    - *(dict) --*

      - **ImageBuilders** *(list) --*

        Information about the image builders.
        - *(dict) --*

          Describes a virtual machine that is used to create an image.
          - **Name** *(string) --*

            The name of the image builder.
    """


_ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef = TypedDict(
    "_ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef(
    _ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef
):
    pass


_ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef = TypedDict(
    "_ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef",
    {
        "sharedAccountId": str,
        "imagePermissions": ClientDescribeImagePermissionsResponseSharedImagePermissionsListimagePermissionsTypeDef,
    },
    total=False,
)


class ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef(
    _ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef
):
    pass


_ClientDescribeImagePermissionsResponseTypeDef = TypedDict(
    "_ClientDescribeImagePermissionsResponseTypeDef",
    {
        "Name": str,
        "SharedImagePermissionsList": List[
            ClientDescribeImagePermissionsResponseSharedImagePermissionsListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeImagePermissionsResponseTypeDef(_ClientDescribeImagePermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the private image.
    """


_ClientDescribeImagesResponseImagesApplicationsTypeDef = TypedDict(
    "_ClientDescribeImagesResponseImagesApplicationsTypeDef",
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


class ClientDescribeImagesResponseImagesApplicationsTypeDef(
    _ClientDescribeImagesResponseImagesApplicationsTypeDef
):
    pass


_ClientDescribeImagesResponseImagesImagePermissionsTypeDef = TypedDict(
    "_ClientDescribeImagesResponseImagesImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class ClientDescribeImagesResponseImagesImagePermissionsTypeDef(
    _ClientDescribeImagesResponseImagesImagePermissionsTypeDef
):
    pass


_ClientDescribeImagesResponseImagesStateChangeReasonTypeDef = TypedDict(
    "_ClientDescribeImagesResponseImagesStateChangeReasonTypeDef",
    {
        "Code": Literal["INTERNAL_ERROR", "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE"],
        "Message": str,
    },
    total=False,
)


class ClientDescribeImagesResponseImagesStateChangeReasonTypeDef(
    _ClientDescribeImagesResponseImagesStateChangeReasonTypeDef
):
    pass


_ClientDescribeImagesResponseImagesTypeDef = TypedDict(
    "_ClientDescribeImagesResponseImagesTypeDef",
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


class ClientDescribeImagesResponseImagesTypeDef(_ClientDescribeImagesResponseImagesTypeDef):
    """
    - *(dict) --*

      Describes an image.
      - **Name** *(string) --*

        The name of the image.
    """


_ClientDescribeImagesResponseTypeDef = TypedDict(
    "_ClientDescribeImagesResponseTypeDef",
    {"Images": List[ClientDescribeImagesResponseImagesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeImagesResponseTypeDef(_ClientDescribeImagesResponseTypeDef):
    """
    - *(dict) --*

      - **Images** *(list) --*

        Information about the images.
        - *(dict) --*

          Describes an image.
          - **Name** *(string) --*

            The name of the image.
    """


_ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef(
    _ClientDescribeSessionsResponseSessionsNetworkAccessConfigurationTypeDef
):
    pass


_ClientDescribeSessionsResponseSessionsTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseSessionsTypeDef",
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


class ClientDescribeSessionsResponseSessionsTypeDef(_ClientDescribeSessionsResponseSessionsTypeDef):
    """
    - *(dict) --*

      Describes a streaming session.
      - **Id** *(string) --*

        The identifier of the streaming session.
    """


_ClientDescribeSessionsResponseTypeDef = TypedDict(
    "_ClientDescribeSessionsResponseTypeDef",
    {"Sessions": List[ClientDescribeSessionsResponseSessionsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeSessionsResponseTypeDef(_ClientDescribeSessionsResponseTypeDef):
    """
    - *(dict) --*

      - **Sessions** *(list) --*

        Information about the streaming sessions.
        - *(dict) --*

          Describes a streaming session.
          - **Id** *(string) --*

            The identifier of the streaming session.
    """


_ClientDescribeStacksResponseStacksAccessEndpointsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientDescribeStacksResponseStacksAccessEndpointsTypeDef(
    _ClientDescribeStacksResponseStacksAccessEndpointsTypeDef
):
    pass


_ClientDescribeStacksResponseStacksApplicationSettingsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)


class ClientDescribeStacksResponseStacksApplicationSettingsTypeDef(
    _ClientDescribeStacksResponseStacksApplicationSettingsTypeDef
):
    pass


_ClientDescribeStacksResponseStacksStackErrorsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksStackErrorsTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksStackErrorsTypeDef(
    _ClientDescribeStacksResponseStacksStackErrorsTypeDef
):
    pass


_ClientDescribeStacksResponseStacksStorageConnectorsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksStorageConnectorsTypeDef",
    {
        "ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"],
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)


class ClientDescribeStacksResponseStacksStorageConnectorsTypeDef(
    _ClientDescribeStacksResponseStacksStorageConnectorsTypeDef
):
    pass


_ClientDescribeStacksResponseStacksUserSettingsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksUserSettingsTypeDef",
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


class ClientDescribeStacksResponseStacksUserSettingsTypeDef(
    _ClientDescribeStacksResponseStacksUserSettingsTypeDef
):
    pass


_ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksTypeDef",
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


class ClientDescribeStacksResponseStacksTypeDef(_ClientDescribeStacksResponseStacksTypeDef):
    """
    - *(dict) --*

      Describes a stack.
      - **Arn** *(string) --*

        The ARN of the stack.
    """


_ClientDescribeStacksResponseTypeDef = TypedDict(
    "_ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeStacksResponseTypeDef(_ClientDescribeStacksResponseTypeDef):
    """
    - *(dict) --*

      - **Stacks** *(list) --*

        Information about the stacks.
        - *(dict) --*

          Describes a stack.
          - **Arn** *(string) --*

            The ARN of the stack.
    """


_ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef = TypedDict(
    "_ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef",
    {
        "ErrorCode": Literal["RESOURCE_NOT_FOUND", "ACCESS_DENIED", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef(
    _ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsSubscriptionErrorsTypeDef
):
    pass


_ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef = TypedDict(
    "_ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef",
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


class ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef(
    _ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef
):
    """
    - *(dict) --*

      Describes information about the usage report subscription.
      - **S3BucketName** *(string) --*

        The Amazon S3 bucket where generated reports are stored.
        If you enabled on-instance session scripts and Amazon S3 logging for your session script
        configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket is
        unique to your account and Region. When you enable usage reporting in this case, AppStream
        2.0 uses the same bucket to store your usage reports. If you haven't already enabled
        on-instance session scripts, when you enable usage reports, AppStream 2.0 creates a new S3
        bucket.
    """


_ClientDescribeUsageReportSubscriptionsResponseTypeDef = TypedDict(
    "_ClientDescribeUsageReportSubscriptionsResponseTypeDef",
    {
        "UsageReportSubscriptions": List[
            ClientDescribeUsageReportSubscriptionsResponseUsageReportSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeUsageReportSubscriptionsResponseTypeDef(
    _ClientDescribeUsageReportSubscriptionsResponseTypeDef
):
    """
    - *(dict) --*

      - **UsageReportSubscriptions** *(list) --*

        Information about the usage report subscription.
        - *(dict) --*

          Describes information about the usage report subscription.
          - **S3BucketName** *(string) --*

            The Amazon S3 bucket where generated reports are stored.
            If you enabled on-instance session scripts and Amazon S3 logging for your session script
            configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket
            is unique to your account and Region. When you enable usage reporting in this case,
            AppStream 2.0 uses the same bucket to store your usage reports. If you haven't already
            enabled on-instance session scripts, when you enable usage reports, AppStream 2.0
            creates a new S3 bucket.
    """


_ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef = TypedDict(
    "_ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)


class ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef(
    _ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes a user in the user pool and the associated stack.
      - **StackName** *(string) --*

        The name of the stack that is associated with the user.
    """


_ClientDescribeUserStackAssociationsResponseTypeDef = TypedDict(
    "_ClientDescribeUserStackAssociationsResponseTypeDef",
    {
        "UserStackAssociations": List[
            ClientDescribeUserStackAssociationsResponseUserStackAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeUserStackAssociationsResponseTypeDef(
    _ClientDescribeUserStackAssociationsResponseTypeDef
):
    """
    - *(dict) --*

      - **UserStackAssociations** *(list) --*

        The UserStackAssociation objects.
        - *(dict) --*

          Describes a user in the user pool and the associated stack.
          - **StackName** *(string) --*

            The name of the stack that is associated with the user.
    """


_ClientDescribeUsersResponseUsersTypeDef = TypedDict(
    "_ClientDescribeUsersResponseUsersTypeDef",
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


class ClientDescribeUsersResponseUsersTypeDef(_ClientDescribeUsersResponseUsersTypeDef):
    """
    - *(dict) --*

      Describes a user in the user pool.
      - **Arn** *(string) --*

        The ARN of the user.
    """


_ClientDescribeUsersResponseTypeDef = TypedDict(
    "_ClientDescribeUsersResponseTypeDef",
    {"Users": List[ClientDescribeUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeUsersResponseTypeDef(_ClientDescribeUsersResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        Information about users in the user pool.
        - *(dict) --*

          Describes a user in the user pool.
          - **Arn** *(string) --*

            The ARN of the user.
    """


_ClientListAssociatedFleetsResponseTypeDef = TypedDict(
    "_ClientListAssociatedFleetsResponseTypeDef",
    {"Names": List[str], "NextToken": str},
    total=False,
)


class ClientListAssociatedFleetsResponseTypeDef(_ClientListAssociatedFleetsResponseTypeDef):
    """
    - *(dict) --*

      - **Names** *(list) --*

        The name of the fleet.
        - *(string) --*
    """


_ClientListAssociatedStacksResponseTypeDef = TypedDict(
    "_ClientListAssociatedStacksResponseTypeDef",
    {"Names": List[str], "NextToken": str},
    total=False,
)


class ClientListAssociatedStacksResponseTypeDef(_ClientListAssociatedStacksResponseTypeDef):
    """
    - *(dict) --*

      - **Names** *(list) --*

        The name of the stack.
        - *(string) --*
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The information about the tags.
        - *(string) --*

          - *(string) --*
    """


_ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef(
    _ClientStartImageBuilderResponseImageBuilderAccessEndpointsTypeDef
):
    pass


_ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef(
    _ClientStartImageBuilderResponseImageBuilderDomainJoinInfoTypeDef
):
    pass


_ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
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


class ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef(
    _ClientStartImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
):
    pass


_ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef(
    _ClientStartImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef
):
    pass


_ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef(
    _ClientStartImageBuilderResponseImageBuilderStateChangeReasonTypeDef
):
    pass


_ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef(
    _ClientStartImageBuilderResponseImageBuilderVpcConfigTypeDef
):
    pass


_ClientStartImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseImageBuilderTypeDef",
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


class ClientStartImageBuilderResponseImageBuilderTypeDef(
    _ClientStartImageBuilderResponseImageBuilderTypeDef
):
    """
    - **ImageBuilder** *(dict) --*

      Information about the image builder.
      - **Name** *(string) --*

        The name of the image builder.
    """


_ClientStartImageBuilderResponseTypeDef = TypedDict(
    "_ClientStartImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientStartImageBuilderResponseImageBuilderTypeDef},
    total=False,
)


class ClientStartImageBuilderResponseTypeDef(_ClientStartImageBuilderResponseTypeDef):
    """
    - *(dict) --*

      - **ImageBuilder** *(dict) --*

        Information about the image builder.
        - **Name** *(string) --*

          The name of the image builder.
    """


_ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef(
    _ClientStopImageBuilderResponseImageBuilderAccessEndpointsTypeDef
):
    pass


_ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef(
    _ClientStopImageBuilderResponseImageBuilderDomainJoinInfoTypeDef
):
    pass


_ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef",
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


class ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef(
    _ClientStopImageBuilderResponseImageBuilderImageBuilderErrorsTypeDef
):
    pass


_ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef(
    _ClientStopImageBuilderResponseImageBuilderNetworkAccessConfigurationTypeDef
):
    pass


_ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef(
    _ClientStopImageBuilderResponseImageBuilderStateChangeReasonTypeDef
):
    pass


_ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef(
    _ClientStopImageBuilderResponseImageBuilderVpcConfigTypeDef
):
    pass


_ClientStopImageBuilderResponseImageBuilderTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseImageBuilderTypeDef",
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


class ClientStopImageBuilderResponseImageBuilderTypeDef(
    _ClientStopImageBuilderResponseImageBuilderTypeDef
):
    """
    - **ImageBuilder** *(dict) --*

      Information about the image builder.
      - **Name** *(string) --*

        The name of the image builder.
    """


_ClientStopImageBuilderResponseTypeDef = TypedDict(
    "_ClientStopImageBuilderResponseTypeDef",
    {"ImageBuilder": ClientStopImageBuilderResponseImageBuilderTypeDef},
    total=False,
)


class ClientStopImageBuilderResponseTypeDef(_ClientStopImageBuilderResponseTypeDef):
    """
    - *(dict) --*

      - **ImageBuilder** *(dict) --*

        Information about the image builder.
        - **Name** *(string) --*

          The name of the image builder.
    """


_ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef = TypedDict(
    "_ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)


class ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef(
    _ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef
):
    pass


_ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef = TypedDict(
    "_ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": ClientUpdateDirectoryConfigResponseDirectoryConfigServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef(
    _ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef
):
    """
    - **DirectoryConfig** *(dict) --*

      Information about the Directory Config object.
      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).
    """


_ClientUpdateDirectoryConfigResponseTypeDef = TypedDict(
    "_ClientUpdateDirectoryConfigResponseTypeDef",
    {"DirectoryConfig": ClientUpdateDirectoryConfigResponseDirectoryConfigTypeDef},
    total=False,
)


class ClientUpdateDirectoryConfigResponseTypeDef(_ClientUpdateDirectoryConfigResponseTypeDef):
    """
    - *(dict) --*

      - **DirectoryConfig** *(dict) --*

        Information about the Directory Config object.
        - **DirectoryName** *(string) --*

          The fully qualified name of the directory (for example, corp.example.com).
    """


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
    """
    The credentials for the service account used by the fleet or image builder to connect to the
    directory.
    - **AccountName** *(string) --***[REQUIRED]**

      The user name of the account. This account must have the following privileges: create computer
      objects, join computers to the domain, and change/reset the password on descendant computer
      objects for the organizational units specified.
    """


_ClientUpdateFleetComputeCapacityTypeDef = TypedDict(
    "_ClientUpdateFleetComputeCapacityTypeDef", {"DesiredInstances": int}
)


class ClientUpdateFleetComputeCapacityTypeDef(_ClientUpdateFleetComputeCapacityTypeDef):
    """
    The desired capacity for the fleet.
    - **DesiredInstances** *(integer) --***[REQUIRED]**

      The desired number of streaming instances.
    """


_ClientUpdateFleetDomainJoinInfoTypeDef = TypedDict(
    "_ClientUpdateFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientUpdateFleetDomainJoinInfoTypeDef(_ClientUpdateFleetDomainJoinInfoTypeDef):
    """
    The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft
    Active Directory domain.
    - **DirectoryName** *(string) --*

      The fully qualified name of the directory (for example, corp.example.com).
    """


_ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)


class ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef(
    _ClientUpdateFleetResponseFleetComputeCapacityStatusTypeDef
):
    pass


_ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef(
    _ClientUpdateFleetResponseFleetDomainJoinInfoTypeDef
):
    pass


_ClientUpdateFleetResponseFleetFleetErrorsTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetFleetErrorsTypeDef",
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


class ClientUpdateFleetResponseFleetFleetErrorsTypeDef(
    _ClientUpdateFleetResponseFleetFleetErrorsTypeDef
):
    pass


_ClientUpdateFleetResponseFleetVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientUpdateFleetResponseFleetVpcConfigTypeDef(
    _ClientUpdateFleetResponseFleetVpcConfigTypeDef
):
    pass


_ClientUpdateFleetResponseFleetTypeDef = TypedDict(
    "_ClientUpdateFleetResponseFleetTypeDef",
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


class ClientUpdateFleetResponseFleetTypeDef(_ClientUpdateFleetResponseFleetTypeDef):
    """
    - **Fleet** *(dict) --*

      Information about the fleet.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the fleet.
    """


_ClientUpdateFleetResponseTypeDef = TypedDict(
    "_ClientUpdateFleetResponseTypeDef",
    {"Fleet": ClientUpdateFleetResponseFleetTypeDef},
    total=False,
)


class ClientUpdateFleetResponseTypeDef(_ClientUpdateFleetResponseTypeDef):
    """
    - *(dict) --*

      - **Fleet** *(dict) --*

        Information about the fleet.
        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) for the fleet.
    """


_ClientUpdateFleetVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFleetVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientUpdateFleetVpcConfigTypeDef(_ClientUpdateFleetVpcConfigTypeDef):
    """
    The VPC configuration for the fleet.
    - **SubnetIds** *(list) --*

      The identifiers of the subnets to which a network interface is attached from the fleet
      instance or image builder instance. Fleet instances use one or more subnets. Image builder
      instances use one subnet.
      - *(string) --*
    """


_ClientUpdateImagePermissionsImagePermissionsTypeDef = TypedDict(
    "_ClientUpdateImagePermissionsImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class ClientUpdateImagePermissionsImagePermissionsTypeDef(
    _ClientUpdateImagePermissionsImagePermissionsTypeDef
):
    """
    The permissions for the image.
    - **allowFleet** *(boolean) --*

      Indicates whether the image can be used for a fleet.
    """


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
    """
    - *(dict) --*

      Describes an interface VPC endpoint (interface endpoint) that lets you create a private
      connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When
      you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0
      only through that endpoint. When you specify an interface endpoint for an image builder,
      administrators can connect to the image builder only through that endpoint.
      - **EndpointType** *(string) --***[REQUIRED]**

        The type of interface endpoint.
    """


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
    """
    The persistent application settings for users of a stack. When these settings are enabled,
    changes that users make to applications and Windows settings are automatically saved after each
    session and applied to the next session.
    - **Enabled** *(boolean) --***[REQUIRED]**

      Enables or disables persistent application settings for users during their streaming sessions.
    """


_ClientUpdateStackResponseStackAccessEndpointsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class ClientUpdateStackResponseStackAccessEndpointsTypeDef(
    _ClientUpdateStackResponseStackAccessEndpointsTypeDef
):
    pass


_ClientUpdateStackResponseStackApplicationSettingsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)


class ClientUpdateStackResponseStackApplicationSettingsTypeDef(
    _ClientUpdateStackResponseStackApplicationSettingsTypeDef
):
    pass


_ClientUpdateStackResponseStackStackErrorsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackStackErrorsTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientUpdateStackResponseStackStackErrorsTypeDef(
    _ClientUpdateStackResponseStackStackErrorsTypeDef
):
    pass


_ClientUpdateStackResponseStackStorageConnectorsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackStorageConnectorsTypeDef",
    {
        "ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"],
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)


class ClientUpdateStackResponseStackStorageConnectorsTypeDef(
    _ClientUpdateStackResponseStackStorageConnectorsTypeDef
):
    pass


_ClientUpdateStackResponseStackUserSettingsTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackUserSettingsTypeDef",
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


class ClientUpdateStackResponseStackUserSettingsTypeDef(
    _ClientUpdateStackResponseStackUserSettingsTypeDef
):
    pass


_ClientUpdateStackResponseStackTypeDef = TypedDict(
    "_ClientUpdateStackResponseStackTypeDef",
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


class ClientUpdateStackResponseStackTypeDef(_ClientUpdateStackResponseStackTypeDef):
    """
    - **Stack** *(dict) --*

      Information about the stack.
      - **Arn** *(string) --*

        The ARN of the stack.
    """


_ClientUpdateStackResponseTypeDef = TypedDict(
    "_ClientUpdateStackResponseTypeDef",
    {"Stack": ClientUpdateStackResponseStackTypeDef},
    total=False,
)


class ClientUpdateStackResponseTypeDef(_ClientUpdateStackResponseTypeDef):
    """
    - *(dict) --*

      - **Stack** *(dict) --*

        Information about the stack.
        - **Arn** *(string) --*

          The ARN of the stack.
    """


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
    """
    - *(dict) --*

      Describes a connector that enables persistent storage for users.
      - **ConnectorType** *(string) --***[REQUIRED]**

        The type of storage connector.
    """


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
    """
    - *(dict) --*

      Describes an action and whether the action is enabled or disabled for users during their
      streaming sessions.
      - **Action** *(string) --***[REQUIRED]**

        The action that is enabled or disabled.
    """


_DescribeDirectoryConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectoryConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectoryConfigsPaginatePaginationConfigTypeDef(
    _DescribeDirectoryConfigsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef = TypedDict(
    "_DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef",
    {"AccountName": str, "AccountPassword": str},
    total=False,
)


class DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef(
    _DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef
):
    pass


_DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef = TypedDict(
    "_DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": DescribeDirectoryConfigsPaginateResponseDirectoryConfigsServiceAccountCredentialsTypeDef,
        "CreatedTime": datetime,
    },
    total=False,
)


class DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef(
    _DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef
):
    """
    - *(dict) --*

      Describes the configuration information required to join fleets and image builders to
      Microsoft Active Directory domains.
      - **DirectoryName** *(string) --*

        The fully qualified name of the directory (for example, corp.example.com).
    """


_DescribeDirectoryConfigsPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectoryConfigsPaginateResponseTypeDef",
    {"DirectoryConfigs": List[DescribeDirectoryConfigsPaginateResponseDirectoryConfigsTypeDef]},
    total=False,
)


class DescribeDirectoryConfigsPaginateResponseTypeDef(
    _DescribeDirectoryConfigsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DirectoryConfigs** *(list) --*

        Information about the directory configurations. Note that although the response syntax in
        this topic includes the account password, this password is not returned in the actual
        response.
        - *(dict) --*

          Describes the configuration information required to join fleets and image builders to
          Microsoft Active Directory domains.
          - **DirectoryName** *(string) --*

            The fully qualified name of the directory (for example, corp.example.com).
    """


_DescribeFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeFleetsPaginatePaginationConfigTypeDef(_DescribeFleetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef",
    {"Desired": int, "Running": int, "InUse": int, "Available": int},
    total=False,
)


class DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef(
    _DescribeFleetsPaginateResponseFleetsComputeCapacityStatusTypeDef
):
    pass


_DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef(
    _DescribeFleetsPaginateResponseFleetsDomainJoinInfoTypeDef
):
    pass


_DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef",
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


class DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef(
    _DescribeFleetsPaginateResponseFleetsFleetErrorsTypeDef
):
    pass


_DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef(
    _DescribeFleetsPaginateResponseFleetsVpcConfigTypeDef
):
    pass


_DescribeFleetsPaginateResponseFleetsTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseFleetsTypeDef",
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


class DescribeFleetsPaginateResponseFleetsTypeDef(_DescribeFleetsPaginateResponseFleetsTypeDef):
    """
    - *(dict) --*

      Describes a fleet.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the fleet.
    """


_DescribeFleetsPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetsPaginateResponseTypeDef",
    {"Fleets": List[DescribeFleetsPaginateResponseFleetsTypeDef]},
    total=False,
)


class DescribeFleetsPaginateResponseTypeDef(_DescribeFleetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Fleets** *(list) --*

        Information about the fleets.
        - *(dict) --*

          Describes a fleet.
          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) for the fleet.
    """


_DescribeImageBuildersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeImageBuildersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeImageBuildersPaginatePaginationConfigTypeDef(
    _DescribeImageBuildersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersAccessEndpointsTypeDef
):
    pass


_DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersDomainJoinInfoTypeDef
):
    pass


_DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef",
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


class DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersImageBuilderErrorsTypeDef
):
    pass


_DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersNetworkAccessConfigurationTypeDef
):
    pass


_DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersStateChangeReasonTypeDef
):
    pass


_DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersVpcConfigTypeDef
):
    pass


_DescribeImageBuildersPaginateResponseImageBuildersTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseImageBuildersTypeDef",
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


class DescribeImageBuildersPaginateResponseImageBuildersTypeDef(
    _DescribeImageBuildersPaginateResponseImageBuildersTypeDef
):
    """
    - *(dict) --*

      Describes a virtual machine that is used to create an image.
      - **Name** *(string) --*

        The name of the image builder.
    """


_DescribeImageBuildersPaginateResponseTypeDef = TypedDict(
    "_DescribeImageBuildersPaginateResponseTypeDef",
    {"ImageBuilders": List[DescribeImageBuildersPaginateResponseImageBuildersTypeDef]},
    total=False,
)


class DescribeImageBuildersPaginateResponseTypeDef(_DescribeImageBuildersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ImageBuilders** *(list) --*

        Information about the image builders.
        - *(dict) --*

          Describes a virtual machine that is used to create an image.
          - **Name** *(string) --*

            The name of the image builder.
    """


_DescribeImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeImagesPaginatePaginationConfigTypeDef(_DescribeImagesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeImagesPaginateResponseImagesApplicationsTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseImagesApplicationsTypeDef",
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


class DescribeImagesPaginateResponseImagesApplicationsTypeDef(
    _DescribeImagesPaginateResponseImagesApplicationsTypeDef
):
    pass


_DescribeImagesPaginateResponseImagesImagePermissionsTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseImagesImagePermissionsTypeDef",
    {"allowFleet": bool, "allowImageBuilder": bool},
    total=False,
)


class DescribeImagesPaginateResponseImagesImagePermissionsTypeDef(
    _DescribeImagesPaginateResponseImagesImagePermissionsTypeDef
):
    pass


_DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef",
    {
        "Code": Literal["INTERNAL_ERROR", "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE"],
        "Message": str,
    },
    total=False,
)


class DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef(
    _DescribeImagesPaginateResponseImagesStateChangeReasonTypeDef
):
    pass


_DescribeImagesPaginateResponseImagesTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseImagesTypeDef",
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


class DescribeImagesPaginateResponseImagesTypeDef(_DescribeImagesPaginateResponseImagesTypeDef):
    """
    - *(dict) --*

      Describes an image.
      - **Name** *(string) --*

        The name of the image.
    """


_DescribeImagesPaginateResponseTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseTypeDef",
    {"Images": List[DescribeImagesPaginateResponseImagesTypeDef]},
    total=False,
)


class DescribeImagesPaginateResponseTypeDef(_DescribeImagesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Images** *(list) --*

        Information about the images.
        - *(dict) --*

          Describes an image.
          - **Name** *(string) --*

            The name of the image.
    """


_DescribeSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSessionsPaginatePaginationConfigTypeDef(
    _DescribeSessionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef",
    {"EniPrivateIpAddress": str, "EniId": str},
    total=False,
)


class DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef(
    _DescribeSessionsPaginateResponseSessionsNetworkAccessConfigurationTypeDef
):
    pass


_DescribeSessionsPaginateResponseSessionsTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseSessionsTypeDef",
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


class DescribeSessionsPaginateResponseSessionsTypeDef(
    _DescribeSessionsPaginateResponseSessionsTypeDef
):
    """
    - *(dict) --*

      Describes a streaming session.
      - **Id** *(string) --*

        The identifier of the streaming session.
    """


_DescribeSessionsPaginateResponseTypeDef = TypedDict(
    "_DescribeSessionsPaginateResponseTypeDef",
    {"Sessions": List[DescribeSessionsPaginateResponseSessionsTypeDef]},
    total=False,
)


class DescribeSessionsPaginateResponseTypeDef(_DescribeSessionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Sessions** *(list) --*

        Information about the streaming sessions.
        - *(dict) --*

          Describes a streaming session.
          - **Id** *(string) --*

            The identifier of the streaming session.
    """


_DescribeStacksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeStacksPaginatePaginationConfigTypeDef(_DescribeStacksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef",
    {"EndpointType": str, "VpceId": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef(
    _DescribeStacksPaginateResponseStacksAccessEndpointsTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef(
    _DescribeStacksPaginateResponseStacksApplicationSettingsTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksStackErrorsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksStackErrorsTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksStackErrorsTypeDef(
    _DescribeStacksPaginateResponseStacksStackErrorsTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef",
    {
        "ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"],
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef(
    _DescribeStacksPaginateResponseStacksStorageConnectorsTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksUserSettingsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksUserSettingsTypeDef",
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


class DescribeStacksPaginateResponseStacksUserSettingsTypeDef(
    _DescribeStacksPaginateResponseStacksUserSettingsTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksTypeDef",
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


class DescribeStacksPaginateResponseStacksTypeDef(_DescribeStacksPaginateResponseStacksTypeDef):
    """
    - *(dict) --*

      Describes a stack.
      - **Arn** *(string) --*

        The ARN of the stack.
    """


_DescribeStacksPaginateResponseTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseTypeDef",
    {"Stacks": List[DescribeStacksPaginateResponseStacksTypeDef]},
    total=False,
)


class DescribeStacksPaginateResponseTypeDef(_DescribeStacksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Stacks** *(list) --*

        Information about the stacks.
        - *(dict) --*

          Describes a stack.
          - **Arn** *(string) --*

            The ARN of the stack.
    """


_DescribeUserStackAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeUserStackAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeUserStackAssociationsPaginatePaginationConfigTypeDef(
    _DescribeUserStackAssociationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef = TypedDict(
    "_DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "SendEmailNotification": bool,
    },
    total=False,
)


class DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef(
    _DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes a user in the user pool and the associated stack.
      - **StackName** *(string) --*

        The name of the stack that is associated with the user.
    """


_DescribeUserStackAssociationsPaginateResponseTypeDef = TypedDict(
    "_DescribeUserStackAssociationsPaginateResponseTypeDef",
    {
        "UserStackAssociations": List[
            DescribeUserStackAssociationsPaginateResponseUserStackAssociationsTypeDef
        ]
    },
    total=False,
)


class DescribeUserStackAssociationsPaginateResponseTypeDef(
    _DescribeUserStackAssociationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **UserStackAssociations** *(list) --*

        The UserStackAssociation objects.
        - *(dict) --*

          Describes a user in the user pool and the associated stack.
          - **StackName** *(string) --*

            The name of the stack that is associated with the user.
    """


_DescribeUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeUsersPaginatePaginationConfigTypeDef(_DescribeUsersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeUsersPaginateResponseUsersTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseUsersTypeDef",
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


class DescribeUsersPaginateResponseUsersTypeDef(_DescribeUsersPaginateResponseUsersTypeDef):
    """
    - *(dict) --*

      Describes a user in the user pool.
      - **Arn** *(string) --*

        The ARN of the user.
    """


_DescribeUsersPaginateResponseTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseTypeDef",
    {"Users": List[DescribeUsersPaginateResponseUsersTypeDef]},
    total=False,
)


class DescribeUsersPaginateResponseTypeDef(_DescribeUsersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        Information about users in the user pool.
        - *(dict) --*

          Describes a user in the user pool.
          - **Arn** *(string) --*

            The ARN of the user.
    """


_FleetStartedWaitWaiterConfigTypeDef = TypedDict(
    "_FleetStartedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class FleetStartedWaitWaiterConfigTypeDef(_FleetStartedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_FleetStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_FleetStoppedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class FleetStoppedWaitWaiterConfigTypeDef(_FleetStoppedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ListAssociatedFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssociatedFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListAssociatedFleetsPaginatePaginationConfigTypeDef(
    _ListAssociatedFleetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssociatedFleetsPaginateResponseTypeDef = TypedDict(
    "_ListAssociatedFleetsPaginateResponseTypeDef", {"Names": List[str]}, total=False
)


class ListAssociatedFleetsPaginateResponseTypeDef(_ListAssociatedFleetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Names** *(list) --*

        The name of the fleet.
        - *(string) --*
    """


_ListAssociatedStacksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssociatedStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListAssociatedStacksPaginatePaginationConfigTypeDef(
    _ListAssociatedStacksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssociatedStacksPaginateResponseTypeDef = TypedDict(
    "_ListAssociatedStacksPaginateResponseTypeDef", {"Names": List[str]}, total=False
)


class ListAssociatedStacksPaginateResponseTypeDef(_ListAssociatedStacksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Names** *(list) --*

        The name of the stack.
        - *(string) --*
    """
