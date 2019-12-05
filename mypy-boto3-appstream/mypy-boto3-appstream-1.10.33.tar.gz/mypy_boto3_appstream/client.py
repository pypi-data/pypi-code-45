"Main interface for appstream service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_appstream.client as client_scope

# pylint: disable=import-self
import mypy_boto3_appstream.paginator as paginator_scope
from mypy_boto3_appstream.type_defs import (
    ClientBatchAssociateUserStackResponseTypeDef,
    ClientBatchAssociateUserStackUserStackAssociationsTypeDef,
    ClientBatchDisassociateUserStackResponseTypeDef,
    ClientBatchDisassociateUserStackUserStackAssociationsTypeDef,
    ClientCopyImageResponseTypeDef,
    ClientCreateDirectoryConfigResponseTypeDef,
    ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef,
    ClientCreateFleetComputeCapacityTypeDef,
    ClientCreateFleetDomainJoinInfoTypeDef,
    ClientCreateFleetResponseTypeDef,
    ClientCreateFleetVpcConfigTypeDef,
    ClientCreateImageBuilderAccessEndpointsTypeDef,
    ClientCreateImageBuilderDomainJoinInfoTypeDef,
    ClientCreateImageBuilderResponseTypeDef,
    ClientCreateImageBuilderStreamingUrlResponseTypeDef,
    ClientCreateImageBuilderVpcConfigTypeDef,
    ClientCreateStackAccessEndpointsTypeDef,
    ClientCreateStackApplicationSettingsTypeDef,
    ClientCreateStackResponseTypeDef,
    ClientCreateStackStorageConnectorsTypeDef,
    ClientCreateStackUserSettingsTypeDef,
    ClientCreateStreamingUrlResponseTypeDef,
    ClientCreateUsageReportSubscriptionResponseTypeDef,
    ClientDeleteImageBuilderResponseTypeDef,
    ClientDeleteImageResponseTypeDef,
    ClientDescribeDirectoryConfigsResponseTypeDef,
    ClientDescribeFleetsResponseTypeDef,
    ClientDescribeImageBuildersResponseTypeDef,
    ClientDescribeImagePermissionsResponseTypeDef,
    ClientDescribeImagesResponseTypeDef,
    ClientDescribeSessionsResponseTypeDef,
    ClientDescribeStacksResponseTypeDef,
    ClientDescribeUsageReportSubscriptionsResponseTypeDef,
    ClientDescribeUserStackAssociationsResponseTypeDef,
    ClientDescribeUsersResponseTypeDef,
    ClientListAssociatedFleetsResponseTypeDef,
    ClientListAssociatedStacksResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientStartImageBuilderResponseTypeDef,
    ClientStopImageBuilderResponseTypeDef,
    ClientUpdateDirectoryConfigResponseTypeDef,
    ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef,
    ClientUpdateFleetComputeCapacityTypeDef,
    ClientUpdateFleetDomainJoinInfoTypeDef,
    ClientUpdateFleetResponseTypeDef,
    ClientUpdateFleetVpcConfigTypeDef,
    ClientUpdateImagePermissionsImagePermissionsTypeDef,
    ClientUpdateStackAccessEndpointsTypeDef,
    ClientUpdateStackApplicationSettingsTypeDef,
    ClientUpdateStackResponseTypeDef,
    ClientUpdateStackStorageConnectorsTypeDef,
    ClientUpdateStackUserSettingsTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_appstream.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [AppStream.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_fleet(self, FleetName: str, StackName: str) -> Dict[str, Any]:
        """
        [Client.associate_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.associate_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_associate_user_stack(
        self, UserStackAssociations: List[ClientBatchAssociateUserStackUserStackAssociationsTypeDef]
    ) -> ClientBatchAssociateUserStackResponseTypeDef:
        """
        [Client.batch_associate_user_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.batch_associate_user_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_disassociate_user_stack(
        self,
        UserStackAssociations: List[ClientBatchDisassociateUserStackUserStackAssociationsTypeDef],
    ) -> ClientBatchDisassociateUserStackResponseTypeDef:
        """
        [Client.batch_disassociate_user_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.batch_disassociate_user_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_image(
        self,
        SourceImageName: str,
        DestinationImageName: str,
        DestinationRegion: str,
        DestinationImageDescription: str = None,
    ) -> ClientCopyImageResponseTypeDef:
        """
        [Client.copy_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.copy_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_directory_config(
        self,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str],
        ServiceAccountCredentials: ClientCreateDirectoryConfigServiceAccountCredentialsTypeDef,
    ) -> ClientCreateDirectoryConfigResponseTypeDef:
        """
        [Client.create_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.create_directory_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_fleet(
        self,
        Name: str,
        InstanceType: str,
        ComputeCapacity: ClientCreateFleetComputeCapacityTypeDef,
        ImageName: str = None,
        ImageArn: str = None,
        FleetType: Literal["ALWAYS_ON", "ON_DEMAND"] = None,
        VpcConfig: ClientCreateFleetVpcConfigTypeDef = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: ClientCreateFleetDomainJoinInfoTypeDef = None,
        Tags: Dict[str, str] = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        IamRoleArn: str = None,
    ) -> ClientCreateFleetResponseTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.create_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_image_builder(
        self,
        Name: str,
        InstanceType: str,
        ImageName: str = None,
        ImageArn: str = None,
        Description: str = None,
        DisplayName: str = None,
        VpcConfig: ClientCreateImageBuilderVpcConfigTypeDef = None,
        IamRoleArn: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: ClientCreateImageBuilderDomainJoinInfoTypeDef = None,
        AppstreamAgentVersion: str = None,
        Tags: Dict[str, str] = None,
        AccessEndpoints: List[ClientCreateImageBuilderAccessEndpointsTypeDef] = None,
    ) -> ClientCreateImageBuilderResponseTypeDef:
        """
        [Client.create_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.create_image_builder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_image_builder_streaming_url(
        self, Name: str, Validity: int = None
    ) -> ClientCreateImageBuilderStreamingUrlResponseTypeDef:
        """
        [Client.create_image_builder_streaming_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.create_image_builder_streaming_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stack(
        self,
        Name: str,
        Description: str = None,
        DisplayName: str = None,
        StorageConnectors: List[ClientCreateStackStorageConnectorsTypeDef] = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        UserSettings: List[ClientCreateStackUserSettingsTypeDef] = None,
        ApplicationSettings: ClientCreateStackApplicationSettingsTypeDef = None,
        Tags: Dict[str, str] = None,
        AccessEndpoints: List[ClientCreateStackAccessEndpointsTypeDef] = None,
        EmbedHostDomains: List[str] = None,
    ) -> ClientCreateStackResponseTypeDef:
        """
        [Client.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.create_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_streaming_url(
        self,
        StackName: str,
        FleetName: str,
        UserId: str,
        ApplicationId: str = None,
        Validity: int = None,
        SessionContext: str = None,
    ) -> ClientCreateStreamingUrlResponseTypeDef:
        """
        [Client.create_streaming_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.create_streaming_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_usage_report_subscription(
        self, *args: Any, **kwargs: Any
    ) -> ClientCreateUsageReportSubscriptionResponseTypeDef:
        """
        [Client.create_usage_report_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.create_usage_report_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self,
        UserName: str,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"],
        MessageAction: Literal["SUPPRESS", "RESEND"] = None,
        FirstName: str = None,
        LastName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.create_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_directory_config(self, DirectoryName: str) -> Dict[str, Any]:
        """
        [Client.delete_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.delete_directory_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_fleet(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.delete_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_image(self, Name: str) -> ClientDeleteImageResponseTypeDef:
        """
        [Client.delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.delete_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_image_builder(self, Name: str) -> ClientDeleteImageBuilderResponseTypeDef:
        """
        [Client.delete_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.delete_image_builder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_image_permissions(self, Name: str, SharedAccountId: str) -> Dict[str, Any]:
        """
        [Client.delete_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.delete_image_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stack(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.delete_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_usage_report_subscription(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.delete_usage_report_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.delete_usage_report_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(
        self, UserName: str, AuthenticationType: Literal["API", "SAML", "USERPOOL"]
    ) -> Dict[str, Any]:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.delete_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_directory_configs(
        self, DirectoryNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeDirectoryConfigsResponseTypeDef:
        """
        [Client.describe_directory_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_directory_configs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleets(
        self, Names: List[str] = None, NextToken: str = None
    ) -> ClientDescribeFleetsResponseTypeDef:
        """
        [Client.describe_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_fleets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_image_builders(
        self, Names: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeImageBuildersResponseTypeDef:
        """
        [Client.describe_image_builders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_image_builders)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_image_permissions(
        self,
        Name: str,
        MaxResults: int = None,
        SharedAwsAccountIds: List[str] = None,
        NextToken: str = None,
    ) -> ClientDescribeImagePermissionsResponseTypeDef:
        """
        [Client.describe_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_image_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_images(
        self,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: Literal["PUBLIC", "PRIVATE", "SHARED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeImagesResponseTypeDef:
        """
        [Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_sessions(
        self,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        NextToken: str = None,
        Limit: int = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
    ) -> ClientDescribeSessionsResponseTypeDef:
        """
        [Client.describe_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_sessions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stacks(
        self, Names: List[str] = None, NextToken: str = None
    ) -> ClientDescribeStacksResponseTypeDef:
        """
        [Client.describe_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_stacks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_usage_report_subscriptions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeUsageReportSubscriptionsResponseTypeDef:
        """
        [Client.describe_usage_report_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_usage_report_subscriptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user_stack_associations(
        self,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeUserStackAssociationsResponseTypeDef:
        """
        [Client.describe_user_stack_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_user_stack_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_users(
        self,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"],
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeUsersResponseTypeDef:
        """
        [Client.describe_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.describe_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_user(
        self, UserName: str, AuthenticationType: Literal["API", "SAML", "USERPOOL"]
    ) -> Dict[str, Any]:
        """
        [Client.disable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.disable_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_fleet(self, FleetName: str, StackName: str) -> Dict[str, Any]:
        """
        [Client.disassociate_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.disassociate_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_user(
        self, UserName: str, AuthenticationType: Literal["API", "SAML", "USERPOOL"]
    ) -> Dict[str, Any]:
        """
        [Client.enable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.enable_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def expire_session(self, SessionId: str) -> Dict[str, Any]:
        """
        [Client.expire_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.expire_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_associated_fleets(
        self, StackName: str, NextToken: str = None
    ) -> ClientListAssociatedFleetsResponseTypeDef:
        """
        [Client.list_associated_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.list_associated_fleets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_associated_stacks(
        self, FleetName: str, NextToken: str = None
    ) -> ClientListAssociatedStacksResponseTypeDef:
        """
        [Client.list_associated_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.list_associated_stacks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_fleet(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.start_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_image_builder(
        self, Name: str, AppstreamAgentVersion: str = None
    ) -> ClientStartImageBuilderResponseTypeDef:
        """
        [Client.start_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.start_image_builder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_fleet(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.stop_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_image_builder(self, Name: str) -> ClientStopImageBuilderResponseTypeDef:
        """
        [Client.stop_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.stop_image_builder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_directory_config(
        self,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str] = None,
        ServiceAccountCredentials: ClientUpdateDirectoryConfigServiceAccountCredentialsTypeDef = None,
    ) -> ClientUpdateDirectoryConfigResponseTypeDef:
        """
        [Client.update_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.update_directory_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_fleet(
        self,
        ImageName: str = None,
        ImageArn: str = None,
        Name: str = None,
        InstanceType: str = None,
        ComputeCapacity: ClientUpdateFleetComputeCapacityTypeDef = None,
        VpcConfig: ClientUpdateFleetVpcConfigTypeDef = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        DeleteVpcConfig: bool = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: ClientUpdateFleetDomainJoinInfoTypeDef = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        AttributesToDelete: List[
            Literal[
                "VPC_CONFIGURATION",
                "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
                "DOMAIN_JOIN_INFO",
                "IAM_ROLE_ARN",
            ]
        ] = None,
        IamRoleArn: str = None,
    ) -> ClientUpdateFleetResponseTypeDef:
        """
        [Client.update_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.update_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_image_permissions(
        self,
        Name: str,
        SharedAccountId: str,
        ImagePermissions: ClientUpdateImagePermissionsImagePermissionsTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.update_image_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_stack(
        self,
        Name: str,
        DisplayName: str = None,
        Description: str = None,
        StorageConnectors: List[ClientUpdateStackStorageConnectorsTypeDef] = None,
        DeleteStorageConnectors: bool = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        AttributesToDelete: List[
            Literal[
                "STORAGE_CONNECTORS",
                "STORAGE_CONNECTOR_HOMEFOLDERS",
                "STORAGE_CONNECTOR_GOOGLE_DRIVE",
                "STORAGE_CONNECTOR_ONE_DRIVE",
                "REDIRECT_URL",
                "FEEDBACK_URL",
                "THEME_NAME",
                "USER_SETTINGS",
                "EMBED_HOST_DOMAINS",
                "IAM_ROLE_ARN",
                "ACCESS_ENDPOINTS",
            ]
        ] = None,
        UserSettings: List[ClientUpdateStackUserSettingsTypeDef] = None,
        ApplicationSettings: ClientUpdateStackApplicationSettingsTypeDef = None,
        AccessEndpoints: List[ClientUpdateStackAccessEndpointsTypeDef] = None,
        EmbedHostDomains: List[str] = None,
    ) -> ClientUpdateStackResponseTypeDef:
        """
        [Client.update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Client.update_stack)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_directory_configs"]
    ) -> paginator_scope.DescribeDirectoryConfigsPaginator:
        """
        [Paginator.DescribeDirectoryConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_fleets"]
    ) -> paginator_scope.DescribeFleetsPaginator:
        """
        [Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_image_builders"]
    ) -> paginator_scope.DescribeImageBuildersPaginator:
        """
        [Paginator.DescribeImageBuilders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_images"]
    ) -> paginator_scope.DescribeImagesPaginator:
        """
        [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.DescribeImages)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> paginator_scope.DescribeSessionsPaginator:
        """
        [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_stacks"]
    ) -> paginator_scope.DescribeStacksPaginator:
        """
        [Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_user_stack_associations"]
    ) -> paginator_scope.DescribeUserStackAssociationsPaginator:
        """
        [Paginator.DescribeUserStackAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_users"]
    ) -> paginator_scope.DescribeUsersPaginator:
        """
        [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_associated_fleets"]
    ) -> paginator_scope.ListAssociatedFleetsPaginator:
        """
        [Paginator.ListAssociatedFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_associated_stacks"]
    ) -> paginator_scope.ListAssociatedStacksPaginator:
        """
        [Paginator.ListAssociatedStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["fleet_started"]) -> waiter_scope.FleetStartedWaiter:
        """
        [Waiter.FleetStarted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Waiter.FleetStarted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["fleet_stopped"]) -> waiter_scope.FleetStoppedWaiter:
        """
        [Waiter.FleetStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/appstream.html#AppStream.Waiter.FleetStopped)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    IncompatibleImageException: Boto3ClientError
    InvalidAccountStatusException: Boto3ClientError
    InvalidParameterCombinationException: Boto3ClientError
    InvalidRoleException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotAvailableException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
