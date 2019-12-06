"Main interface for cognito-idp service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_cognito_idp.client as client_scope

# pylint: disable=import-self
import mypy_boto3_cognito_idp.paginator as paginator_scope
from mypy_boto3_cognito_idp.type_defs import (
    ClientAddCustomAttributesCustomAttributesTypeDef,
    ClientAdminCreateUserResponseTypeDef,
    ClientAdminCreateUserUserAttributesTypeDef,
    ClientAdminCreateUserValidationDataTypeDef,
    ClientAdminDisableProviderForUserUserTypeDef,
    ClientAdminGetDeviceResponseTypeDef,
    ClientAdminGetUserResponseTypeDef,
    ClientAdminInitiateAuthAnalyticsMetadataTypeDef,
    ClientAdminInitiateAuthContextDataTypeDef,
    ClientAdminInitiateAuthResponseTypeDef,
    ClientAdminLinkProviderForUserDestinationUserTypeDef,
    ClientAdminLinkProviderForUserSourceUserTypeDef,
    ClientAdminListDevicesResponseTypeDef,
    ClientAdminListGroupsForUserResponseTypeDef,
    ClientAdminListUserAuthEventsResponseTypeDef,
    ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef,
    ClientAdminRespondToAuthChallengeContextDataTypeDef,
    ClientAdminRespondToAuthChallengeResponseTypeDef,
    ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef,
    ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef,
    ClientAdminSetUserSettingsMFAOptionsTypeDef,
    ClientAdminUpdateUserAttributesUserAttributesTypeDef,
    ClientAssociateSoftwareTokenResponseTypeDef,
    ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef,
    ClientConfirmDeviceResponseTypeDef,
    ClientConfirmForgotPasswordAnalyticsMetadataTypeDef,
    ClientConfirmForgotPasswordUserContextDataTypeDef,
    ClientConfirmSignUpAnalyticsMetadataTypeDef,
    ClientConfirmSignUpUserContextDataTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientCreateIdentityProviderResponseTypeDef,
    ClientCreateResourceServerResponseTypeDef,
    ClientCreateResourceServerScopesTypeDef,
    ClientCreateUserImportJobResponseTypeDef,
    ClientCreateUserPoolAccountRecoverySettingTypeDef,
    ClientCreateUserPoolAdminCreateUserConfigTypeDef,
    ClientCreateUserPoolClientAnalyticsConfigurationTypeDef,
    ClientCreateUserPoolClientResponseTypeDef,
    ClientCreateUserPoolDeviceConfigurationTypeDef,
    ClientCreateUserPoolDomainCustomDomainConfigTypeDef,
    ClientCreateUserPoolDomainResponseTypeDef,
    ClientCreateUserPoolEmailConfigurationTypeDef,
    ClientCreateUserPoolLambdaConfigTypeDef,
    ClientCreateUserPoolPoliciesTypeDef,
    ClientCreateUserPoolResponseTypeDef,
    ClientCreateUserPoolSchemaTypeDef,
    ClientCreateUserPoolSmsConfigurationTypeDef,
    ClientCreateUserPoolUserPoolAddOnsTypeDef,
    ClientCreateUserPoolVerificationMessageTemplateTypeDef,
    ClientDescribeIdentityProviderResponseTypeDef,
    ClientDescribeResourceServerResponseTypeDef,
    ClientDescribeRiskConfigurationResponseTypeDef,
    ClientDescribeUserImportJobResponseTypeDef,
    ClientDescribeUserPoolClientResponseTypeDef,
    ClientDescribeUserPoolDomainResponseTypeDef,
    ClientDescribeUserPoolResponseTypeDef,
    ClientForgotPasswordAnalyticsMetadataTypeDef,
    ClientForgotPasswordResponseTypeDef,
    ClientForgotPasswordUserContextDataTypeDef,
    ClientGetCsvHeaderResponseTypeDef,
    ClientGetDeviceResponseTypeDef,
    ClientGetGroupResponseTypeDef,
    ClientGetIdentityProviderByIdentifierResponseTypeDef,
    ClientGetSigningCertificateResponseTypeDef,
    ClientGetUiCustomizationResponseTypeDef,
    ClientGetUserAttributeVerificationCodeResponseTypeDef,
    ClientGetUserPoolMfaConfigResponseTypeDef,
    ClientGetUserResponseTypeDef,
    ClientInitiateAuthAnalyticsMetadataTypeDef,
    ClientInitiateAuthResponseTypeDef,
    ClientInitiateAuthUserContextDataTypeDef,
    ClientListDevicesResponseTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientListIdentityProvidersResponseTypeDef,
    ClientListResourceServersResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUserImportJobsResponseTypeDef,
    ClientListUserPoolClientsResponseTypeDef,
    ClientListUserPoolsResponseTypeDef,
    ClientListUsersInGroupResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientResendConfirmationCodeAnalyticsMetadataTypeDef,
    ClientResendConfirmationCodeResponseTypeDef,
    ClientResendConfirmationCodeUserContextDataTypeDef,
    ClientRespondToAuthChallengeAnalyticsMetadataTypeDef,
    ClientRespondToAuthChallengeResponseTypeDef,
    ClientRespondToAuthChallengeUserContextDataTypeDef,
    ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
    ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
    ClientSetRiskConfigurationResponseTypeDef,
    ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef,
    ClientSetUiCustomizationResponseTypeDef,
    ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef,
    ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef,
    ClientSetUserPoolMfaConfigResponseTypeDef,
    ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef,
    ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef,
    ClientSetUserSettingsMFAOptionsTypeDef,
    ClientSignUpAnalyticsMetadataTypeDef,
    ClientSignUpResponseTypeDef,
    ClientSignUpUserAttributesTypeDef,
    ClientSignUpUserContextDataTypeDef,
    ClientSignUpValidationDataTypeDef,
    ClientStartUserImportJobResponseTypeDef,
    ClientStopUserImportJobResponseTypeDef,
    ClientUpdateGroupResponseTypeDef,
    ClientUpdateIdentityProviderResponseTypeDef,
    ClientUpdateResourceServerResponseTypeDef,
    ClientUpdateResourceServerScopesTypeDef,
    ClientUpdateUserAttributesResponseTypeDef,
    ClientUpdateUserAttributesUserAttributesTypeDef,
    ClientUpdateUserPoolAccountRecoverySettingTypeDef,
    ClientUpdateUserPoolAdminCreateUserConfigTypeDef,
    ClientUpdateUserPoolClientAnalyticsConfigurationTypeDef,
    ClientUpdateUserPoolClientResponseTypeDef,
    ClientUpdateUserPoolDeviceConfigurationTypeDef,
    ClientUpdateUserPoolDomainCustomDomainConfigTypeDef,
    ClientUpdateUserPoolDomainResponseTypeDef,
    ClientUpdateUserPoolEmailConfigurationTypeDef,
    ClientUpdateUserPoolLambdaConfigTypeDef,
    ClientUpdateUserPoolPoliciesTypeDef,
    ClientUpdateUserPoolSmsConfigurationTypeDef,
    ClientUpdateUserPoolUserPoolAddOnsTypeDef,
    ClientUpdateUserPoolVerificationMessageTemplateTypeDef,
    ClientVerifySoftwareTokenResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [CognitoIdentityProvider.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_custom_attributes(
        self,
        UserPoolId: str,
        CustomAttributes: List[ClientAddCustomAttributesCustomAttributesTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.add_custom_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.add_custom_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_add_user_to_group(self, UserPoolId: str, Username: str, GroupName: str) -> None:
        """
        [Client.admin_add_user_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_add_user_to_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_confirm_sign_up(
        self, UserPoolId: str, Username: str, ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Client.admin_confirm_sign_up documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_confirm_sign_up)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_create_user(
        self,
        UserPoolId: str,
        Username: str,
        UserAttributes: List[ClientAdminCreateUserUserAttributesTypeDef] = None,
        ValidationData: List[ClientAdminCreateUserValidationDataTypeDef] = None,
        TemporaryPassword: str = None,
        ForceAliasCreation: bool = None,
        MessageAction: Literal["RESEND", "SUPPRESS"] = None,
        DesiredDeliveryMediums: List[Literal["SMS", "EMAIL"]] = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> ClientAdminCreateUserResponseTypeDef:
        """
        [Client.admin_create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_create_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_delete_user(self, UserPoolId: str, Username: str) -> None:
        """
        [Client.admin_delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_delete_user_attributes(
        self, UserPoolId: str, Username: str, UserAttributeNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.admin_delete_user_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_disable_provider_for_user(
        self, UserPoolId: str, User: ClientAdminDisableProviderForUserUserTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.admin_disable_provider_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_provider_for_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_disable_user(self, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        [Client.admin_disable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_enable_user(self, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        [Client.admin_enable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_enable_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_forget_device(self, UserPoolId: str, Username: str, DeviceKey: str) -> None:
        """
        [Client.admin_forget_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_forget_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_get_device(
        self, DeviceKey: str, UserPoolId: str, Username: str
    ) -> ClientAdminGetDeviceResponseTypeDef:
        """
        [Client.admin_get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_get_user(self, UserPoolId: str, Username: str) -> ClientAdminGetUserResponseTypeDef:
        """
        [Client.admin_get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_initiate_auth(
        self,
        UserPoolId: str,
        ClientId: str,
        AuthFlow: Literal[
            "USER_SRP_AUTH",
            "REFRESH_TOKEN_AUTH",
            "REFRESH_TOKEN",
            "CUSTOM_AUTH",
            "ADMIN_NO_SRP_AUTH",
            "USER_PASSWORD_AUTH",
            "ADMIN_USER_PASSWORD_AUTH",
        ],
        AuthParameters: Dict[str, str] = None,
        ClientMetadata: Dict[str, str] = None,
        AnalyticsMetadata: ClientAdminInitiateAuthAnalyticsMetadataTypeDef = None,
        ContextData: ClientAdminInitiateAuthContextDataTypeDef = None,
    ) -> ClientAdminInitiateAuthResponseTypeDef:
        """
        [Client.admin_initiate_auth documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_initiate_auth)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_link_provider_for_user(
        self,
        UserPoolId: str,
        DestinationUser: ClientAdminLinkProviderForUserDestinationUserTypeDef,
        SourceUser: ClientAdminLinkProviderForUserSourceUserTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.admin_link_provider_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_link_provider_for_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_list_devices(
        self, UserPoolId: str, Username: str, Limit: int = None, PaginationToken: str = None
    ) -> ClientAdminListDevicesResponseTypeDef:
        """
        [Client.admin_list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_devices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_list_groups_for_user(
        self, Username: str, UserPoolId: str, Limit: int = None, NextToken: str = None
    ) -> ClientAdminListGroupsForUserResponseTypeDef:
        """
        [Client.admin_list_groups_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_groups_for_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_list_user_auth_events(
        self, UserPoolId: str, Username: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientAdminListUserAuthEventsResponseTypeDef:
        """
        [Client.admin_list_user_auth_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_user_auth_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_remove_user_from_group(self, UserPoolId: str, Username: str, GroupName: str) -> None:
        """
        [Client.admin_remove_user_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_remove_user_from_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_reset_user_password(
        self, UserPoolId: str, Username: str, ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Client.admin_reset_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_reset_user_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_respond_to_auth_challenge(
        self,
        UserPoolId: str,
        ClientId: str,
        ChallengeName: Literal[
            "SMS_MFA",
            "SOFTWARE_TOKEN_MFA",
            "SELECT_MFA_TYPE",
            "MFA_SETUP",
            "PASSWORD_VERIFIER",
            "CUSTOM_CHALLENGE",
            "DEVICE_SRP_AUTH",
            "DEVICE_PASSWORD_VERIFIER",
            "ADMIN_NO_SRP_AUTH",
            "NEW_PASSWORD_REQUIRED",
        ],
        ChallengeResponses: Dict[str, str] = None,
        Session: str = None,
        AnalyticsMetadata: ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef = None,
        ContextData: ClientAdminRespondToAuthChallengeContextDataTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> ClientAdminRespondToAuthChallengeResponseTypeDef:
        """
        [Client.admin_respond_to_auth_challenge documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_respond_to_auth_challenge)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_set_user_mfa_preference(
        self,
        Username: str,
        UserPoolId: str,
        SMSMfaSettings: ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef = None,
        SoftwareTokenMfaSettings: ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.admin_set_user_mfa_preference documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_mfa_preference)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_set_user_password(
        self, UserPoolId: str, Username: str, Password: str, Permanent: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.admin_set_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_set_user_settings(
        self,
        UserPoolId: str,
        Username: str,
        MFAOptions: List[ClientAdminSetUserSettingsMFAOptionsTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.admin_set_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_update_auth_event_feedback(
        self,
        UserPoolId: str,
        Username: str,
        EventId: str,
        FeedbackValue: Literal["Valid", "Invalid"],
    ) -> Dict[str, Any]:
        """
        [Client.admin_update_auth_event_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_auth_event_feedback)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_update_device_status(
        self,
        UserPoolId: str,
        Username: str,
        DeviceKey: str,
        DeviceRememberedStatus: Literal["remembered", "not_remembered"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.admin_update_device_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_device_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_update_user_attributes(
        self,
        UserPoolId: str,
        Username: str,
        UserAttributes: List[ClientAdminUpdateUserAttributesUserAttributesTypeDef],
        ClientMetadata: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.admin_update_user_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_user_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def admin_user_global_sign_out(self, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        [Client.admin_user_global_sign_out documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_user_global_sign_out)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_software_token(
        self, AccessToken: str = None, Session: str = None
    ) -> ClientAssociateSoftwareTokenResponseTypeDef:
        """
        [Client.associate_software_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.associate_software_token)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_password(
        self, PreviousPassword: str, ProposedPassword: str, AccessToken: str
    ) -> Dict[str, Any]:
        """
        [Client.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.change_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_device(
        self,
        AccessToken: str,
        DeviceKey: str,
        DeviceSecretVerifierConfig: ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef = None,
        DeviceName: str = None,
    ) -> ClientConfirmDeviceResponseTypeDef:
        """
        [Client.confirm_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_forgot_password(
        self,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        Password: str,
        SecretHash: str = None,
        AnalyticsMetadata: ClientConfirmForgotPasswordAnalyticsMetadataTypeDef = None,
        UserContextData: ClientConfirmForgotPasswordUserContextDataTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.confirm_forgot_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_forgot_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_sign_up(
        self,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        SecretHash: str = None,
        ForceAliasCreation: bool = None,
        AnalyticsMetadata: ClientConfirmSignUpAnalyticsMetadataTypeDef = None,
        UserContextData: ClientConfirmSignUpUserContextDataTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.confirm_sign_up documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_sign_up)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(
        self,
        GroupName: str,
        UserPoolId: str,
        Description: str = None,
        RoleArn: str = None,
        Precedence: int = None,
    ) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_identity_provider(
        self,
        UserPoolId: str,
        ProviderName: str,
        ProviderType: Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        ProviderDetails: Dict[str, str],
        AttributeMapping: Dict[str, str] = None,
        IdpIdentifiers: List[str] = None,
    ) -> ClientCreateIdentityProviderResponseTypeDef:
        """
        [Client.create_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_identity_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_server(
        self,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: List[ClientCreateResourceServerScopesTypeDef] = None,
    ) -> ClientCreateResourceServerResponseTypeDef:
        """
        [Client.create_resource_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_resource_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user_import_job(
        self, JobName: str, UserPoolId: str, CloudWatchLogsRoleArn: str
    ) -> ClientCreateUserImportJobResponseTypeDef:
        """
        [Client.create_user_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user_pool(
        self,
        PoolName: str,
        Policies: ClientCreateUserPoolPoliciesTypeDef = None,
        LambdaConfig: ClientCreateUserPoolLambdaConfigTypeDef = None,
        AutoVerifiedAttributes: List[Literal["phone_number", "email"]] = None,
        AliasAttributes: List[Literal["phone_number", "email", "preferred_username"]] = None,
        UsernameAttributes: List[Literal["phone_number", "email"]] = None,
        SmsVerificationMessage: str = None,
        EmailVerificationMessage: str = None,
        EmailVerificationSubject: str = None,
        VerificationMessageTemplate: ClientCreateUserPoolVerificationMessageTemplateTypeDef = None,
        SmsAuthenticationMessage: str = None,
        MfaConfiguration: Literal["OFF", "ON", "OPTIONAL"] = None,
        DeviceConfiguration: ClientCreateUserPoolDeviceConfigurationTypeDef = None,
        EmailConfiguration: ClientCreateUserPoolEmailConfigurationTypeDef = None,
        SmsConfiguration: ClientCreateUserPoolSmsConfigurationTypeDef = None,
        UserPoolTags: Dict[str, str] = None,
        AdminCreateUserConfig: ClientCreateUserPoolAdminCreateUserConfigTypeDef = None,
        Schema: List[ClientCreateUserPoolSchemaTypeDef] = None,
        UserPoolAddOns: ClientCreateUserPoolUserPoolAddOnsTypeDef = None,
        AccountRecoverySetting: ClientCreateUserPoolAccountRecoverySettingTypeDef = None,
    ) -> ClientCreateUserPoolResponseTypeDef:
        """
        [Client.create_user_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user_pool_client(
        self,
        UserPoolId: str,
        ClientName: str,
        GenerateSecret: bool = None,
        RefreshTokenValidity: int = None,
        ReadAttributes: List[str] = None,
        WriteAttributes: List[str] = None,
        ExplicitAuthFlows: List[
            Literal[
                "ADMIN_NO_SRP_AUTH",
                "CUSTOM_AUTH_FLOW_ONLY",
                "USER_PASSWORD_AUTH",
                "ALLOW_ADMIN_USER_PASSWORD_AUTH",
                "ALLOW_CUSTOM_AUTH",
                "ALLOW_USER_PASSWORD_AUTH",
                "ALLOW_USER_SRP_AUTH",
                "ALLOW_REFRESH_TOKEN_AUTH",
            ]
        ] = None,
        SupportedIdentityProviders: List[str] = None,
        CallbackURLs: List[str] = None,
        LogoutURLs: List[str] = None,
        DefaultRedirectURI: str = None,
        AllowedOAuthFlows: List[Literal["code", "implicit", "client_credentials"]] = None,
        AllowedOAuthScopes: List[str] = None,
        AllowedOAuthFlowsUserPoolClient: bool = None,
        AnalyticsConfiguration: ClientCreateUserPoolClientAnalyticsConfigurationTypeDef = None,
        PreventUserExistenceErrors: Literal["LEGACY", "ENABLED"] = None,
    ) -> ClientCreateUserPoolClientResponseTypeDef:
        """
        [Client.create_user_pool_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_client)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user_pool_domain(
        self,
        Domain: str,
        UserPoolId: str,
        CustomDomainConfig: ClientCreateUserPoolDomainCustomDomainConfigTypeDef = None,
    ) -> ClientCreateUserPoolDomainResponseTypeDef:
        """
        [Client.create_user_pool_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(self, GroupName: str, UserPoolId: str) -> None:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_identity_provider(self, UserPoolId: str, ProviderName: str) -> None:
        """
        [Client.delete_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_identity_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_server(self, UserPoolId: str, Identifier: str) -> None:
        """
        [Client.delete_resource_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_resource_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(self, AccessToken: str) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user_attributes(
        self, UserAttributeNames: List[str], AccessToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_user_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user_pool(self, UserPoolId: str) -> None:
        """
        [Client.delete_user_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user_pool_client(self, UserPoolId: str, ClientId: str) -> None:
        """
        [Client.delete_user_pool_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_client)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user_pool_domain(self, Domain: str, UserPoolId: str) -> Dict[str, Any]:
        """
        [Client.delete_user_pool_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_identity_provider(
        self, UserPoolId: str, ProviderName: str
    ) -> ClientDescribeIdentityProviderResponseTypeDef:
        """
        [Client.describe_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_identity_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_resource_server(
        self, UserPoolId: str, Identifier: str
    ) -> ClientDescribeResourceServerResponseTypeDef:
        """
        [Client.describe_resource_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_resource_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_risk_configuration(
        self, UserPoolId: str, ClientId: str = None
    ) -> ClientDescribeRiskConfigurationResponseTypeDef:
        """
        [Client.describe_risk_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_risk_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user_import_job(
        self, UserPoolId: str, JobId: str
    ) -> ClientDescribeUserImportJobResponseTypeDef:
        """
        [Client.describe_user_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user_pool(self, UserPoolId: str) -> ClientDescribeUserPoolResponseTypeDef:
        """
        [Client.describe_user_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user_pool_client(
        self, UserPoolId: str, ClientId: str
    ) -> ClientDescribeUserPoolClientResponseTypeDef:
        """
        [Client.describe_user_pool_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_client)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user_pool_domain(self, Domain: str) -> ClientDescribeUserPoolDomainResponseTypeDef:
        """
        [Client.describe_user_pool_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def forget_device(self, DeviceKey: str, AccessToken: str = None) -> None:
        """
        [Client.forget_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forget_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def forgot_password(
        self,
        ClientId: str,
        Username: str,
        SecretHash: str = None,
        UserContextData: ClientForgotPasswordUserContextDataTypeDef = None,
        AnalyticsMetadata: ClientForgotPasswordAnalyticsMetadataTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> ClientForgotPasswordResponseTypeDef:
        """
        [Client.forgot_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forgot_password)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_csv_header(self, UserPoolId: str) -> ClientGetCsvHeaderResponseTypeDef:
        """
        [Client.get_csv_header documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_csv_header)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device(self, DeviceKey: str, AccessToken: str = None) -> ClientGetDeviceResponseTypeDef:
        """
        [Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group(self, GroupName: str, UserPoolId: str) -> ClientGetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_identity_provider_by_identifier(
        self, UserPoolId: str, IdpIdentifier: str
    ) -> ClientGetIdentityProviderByIdentifierResponseTypeDef:
        """
        [Client.get_identity_provider_by_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_identity_provider_by_identifier)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_signing_certificate(
        self, UserPoolId: str
    ) -> ClientGetSigningCertificateResponseTypeDef:
        """
        [Client.get_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_signing_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ui_customization(
        self, UserPoolId: str, ClientId: str = None
    ) -> ClientGetUiCustomizationResponseTypeDef:
        """
        [Client.get_ui_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_ui_customization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user(self, AccessToken: str) -> ClientGetUserResponseTypeDef:
        """
        [Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_attribute_verification_code(
        self, AccessToken: str, AttributeName: str, ClientMetadata: Dict[str, str] = None
    ) -> ClientGetUserAttributeVerificationCodeResponseTypeDef:
        """
        [Client.get_user_attribute_verification_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_attribute_verification_code)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_user_pool_mfa_config(
        self, UserPoolId: str
    ) -> ClientGetUserPoolMfaConfigResponseTypeDef:
        """
        [Client.get_user_pool_mfa_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_pool_mfa_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def global_sign_out(self, AccessToken: str) -> Dict[str, Any]:
        """
        [Client.global_sign_out documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.global_sign_out)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_auth(
        self,
        AuthFlow: Literal[
            "USER_SRP_AUTH",
            "REFRESH_TOKEN_AUTH",
            "REFRESH_TOKEN",
            "CUSTOM_AUTH",
            "ADMIN_NO_SRP_AUTH",
            "USER_PASSWORD_AUTH",
            "ADMIN_USER_PASSWORD_AUTH",
        ],
        ClientId: str,
        AuthParameters: Dict[str, str] = None,
        ClientMetadata: Dict[str, str] = None,
        AnalyticsMetadata: ClientInitiateAuthAnalyticsMetadataTypeDef = None,
        UserContextData: ClientInitiateAuthUserContextDataTypeDef = None,
    ) -> ClientInitiateAuthResponseTypeDef:
        """
        [Client.initiate_auth documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.initiate_auth)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_devices(
        self, AccessToken: str, Limit: int = None, PaginationToken: str = None
    ) -> ClientListDevicesResponseTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_devices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_groups(
        self, UserPoolId: str, Limit: int = None, NextToken: str = None
    ) -> ClientListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_identity_providers(
        self, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListIdentityProvidersResponseTypeDef:
        """
        [Client.list_identity_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_identity_providers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_servers(
        self, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListResourceServersResponseTypeDef:
        """
        [Client.list_resource_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_resource_servers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_user_import_jobs(
        self, UserPoolId: str, MaxResults: int, PaginationToken: str = None
    ) -> ClientListUserImportJobsResponseTypeDef:
        """
        [Client.list_user_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_import_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_user_pool_clients(
        self, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListUserPoolClientsResponseTypeDef:
        """
        [Client.list_user_pool_clients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pool_clients)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_user_pools(
        self, MaxResults: int, NextToken: str = None
    ) -> ClientListUserPoolsResponseTypeDef:
        """
        [Client.list_user_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pools)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        PaginationToken: str = None,
        Filter: str = None,
    ) -> ClientListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users_in_group(
        self, UserPoolId: str, GroupName: str, Limit: int = None, NextToken: str = None
    ) -> ClientListUsersInGroupResponseTypeDef:
        """
        [Client.list_users_in_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users_in_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resend_confirmation_code(
        self,
        ClientId: str,
        Username: str,
        SecretHash: str = None,
        UserContextData: ClientResendConfirmationCodeUserContextDataTypeDef = None,
        AnalyticsMetadata: ClientResendConfirmationCodeAnalyticsMetadataTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> ClientResendConfirmationCodeResponseTypeDef:
        """
        [Client.resend_confirmation_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.resend_confirmation_code)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def respond_to_auth_challenge(
        self,
        ClientId: str,
        ChallengeName: Literal[
            "SMS_MFA",
            "SOFTWARE_TOKEN_MFA",
            "SELECT_MFA_TYPE",
            "MFA_SETUP",
            "PASSWORD_VERIFIER",
            "CUSTOM_CHALLENGE",
            "DEVICE_SRP_AUTH",
            "DEVICE_PASSWORD_VERIFIER",
            "ADMIN_NO_SRP_AUTH",
            "NEW_PASSWORD_REQUIRED",
        ],
        Session: str = None,
        ChallengeResponses: Dict[str, str] = None,
        AnalyticsMetadata: ClientRespondToAuthChallengeAnalyticsMetadataTypeDef = None,
        UserContextData: ClientRespondToAuthChallengeUserContextDataTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> ClientRespondToAuthChallengeResponseTypeDef:
        """
        [Client.respond_to_auth_challenge documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.respond_to_auth_challenge)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_risk_configuration(
        self,
        UserPoolId: str,
        ClientId: str = None,
        CompromisedCredentialsRiskConfiguration: ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = None,
        AccountTakeoverRiskConfiguration: ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = None,
        RiskExceptionConfiguration: ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef = None,
    ) -> ClientSetRiskConfigurationResponseTypeDef:
        """
        [Client.set_risk_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_risk_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_ui_customization(
        self, UserPoolId: str, ClientId: str = None, CSS: str = None, ImageFile: bytes = None
    ) -> ClientSetUiCustomizationResponseTypeDef:
        """
        [Client.set_ui_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_ui_customization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_user_mfa_preference(
        self,
        AccessToken: str,
        SMSMfaSettings: ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef = None,
        SoftwareTokenMfaSettings: ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.set_user_mfa_preference documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_mfa_preference)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_user_pool_mfa_config(
        self,
        UserPoolId: str,
        SmsMfaConfiguration: ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef = None,
        SoftwareTokenMfaConfiguration: ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef = None,
        MfaConfiguration: Literal["OFF", "ON", "OPTIONAL"] = None,
    ) -> ClientSetUserPoolMfaConfigResponseTypeDef:
        """
        [Client.set_user_pool_mfa_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_pool_mfa_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_user_settings(
        self, AccessToken: str, MFAOptions: List[ClientSetUserSettingsMFAOptionsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.set_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def sign_up(
        self,
        ClientId: str,
        Username: str,
        Password: str,
        SecretHash: str = None,
        UserAttributes: List[ClientSignUpUserAttributesTypeDef] = None,
        ValidationData: List[ClientSignUpValidationDataTypeDef] = None,
        AnalyticsMetadata: ClientSignUpAnalyticsMetadataTypeDef = None,
        UserContextData: ClientSignUpUserContextDataTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> ClientSignUpResponseTypeDef:
        """
        [Client.sign_up documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.sign_up)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_user_import_job(
        self, UserPoolId: str, JobId: str
    ) -> ClientStartUserImportJobResponseTypeDef:
        """
        [Client.start_user_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.start_user_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_user_import_job(
        self, UserPoolId: str, JobId: str
    ) -> ClientStopUserImportJobResponseTypeDef:
        """
        [Client.stop_user_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.stop_user_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_auth_event_feedback(
        self,
        UserPoolId: str,
        Username: str,
        EventId: str,
        FeedbackToken: str,
        FeedbackValue: Literal["Valid", "Invalid"],
    ) -> Dict[str, Any]:
        """
        [Client.update_auth_event_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_auth_event_feedback)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_status(
        self,
        AccessToken: str,
        DeviceKey: str,
        DeviceRememberedStatus: Literal["remembered", "not_remembered"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_device_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_device_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group(
        self,
        GroupName: str,
        UserPoolId: str,
        Description: str = None,
        RoleArn: str = None,
        Precedence: int = None,
    ) -> ClientUpdateGroupResponseTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_identity_provider(
        self,
        UserPoolId: str,
        ProviderName: str,
        ProviderDetails: Dict[str, str] = None,
        AttributeMapping: Dict[str, str] = None,
        IdpIdentifiers: List[str] = None,
    ) -> ClientUpdateIdentityProviderResponseTypeDef:
        """
        [Client.update_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_identity_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resource_server(
        self,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: List[ClientUpdateResourceServerScopesTypeDef] = None,
    ) -> ClientUpdateResourceServerResponseTypeDef:
        """
        [Client.update_resource_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_resource_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_attributes(
        self,
        UserAttributes: List[ClientUpdateUserAttributesUserAttributesTypeDef],
        AccessToken: str,
        ClientMetadata: Dict[str, str] = None,
    ) -> ClientUpdateUserAttributesResponseTypeDef:
        """
        [Client.update_user_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_pool(
        self,
        UserPoolId: str,
        Policies: ClientUpdateUserPoolPoliciesTypeDef = None,
        LambdaConfig: ClientUpdateUserPoolLambdaConfigTypeDef = None,
        AutoVerifiedAttributes: List[Literal["phone_number", "email"]] = None,
        SmsVerificationMessage: str = None,
        EmailVerificationMessage: str = None,
        EmailVerificationSubject: str = None,
        VerificationMessageTemplate: ClientUpdateUserPoolVerificationMessageTemplateTypeDef = None,
        SmsAuthenticationMessage: str = None,
        MfaConfiguration: Literal["OFF", "ON", "OPTIONAL"] = None,
        DeviceConfiguration: ClientUpdateUserPoolDeviceConfigurationTypeDef = None,
        EmailConfiguration: ClientUpdateUserPoolEmailConfigurationTypeDef = None,
        SmsConfiguration: ClientUpdateUserPoolSmsConfigurationTypeDef = None,
        UserPoolTags: Dict[str, str] = None,
        AdminCreateUserConfig: ClientUpdateUserPoolAdminCreateUserConfigTypeDef = None,
        UserPoolAddOns: ClientUpdateUserPoolUserPoolAddOnsTypeDef = None,
        AccountRecoverySetting: ClientUpdateUserPoolAccountRecoverySettingTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_user_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_pool_client(
        self,
        UserPoolId: str,
        ClientId: str,
        ClientName: str = None,
        RefreshTokenValidity: int = None,
        ReadAttributes: List[str] = None,
        WriteAttributes: List[str] = None,
        ExplicitAuthFlows: List[
            Literal[
                "ADMIN_NO_SRP_AUTH",
                "CUSTOM_AUTH_FLOW_ONLY",
                "USER_PASSWORD_AUTH",
                "ALLOW_ADMIN_USER_PASSWORD_AUTH",
                "ALLOW_CUSTOM_AUTH",
                "ALLOW_USER_PASSWORD_AUTH",
                "ALLOW_USER_SRP_AUTH",
                "ALLOW_REFRESH_TOKEN_AUTH",
            ]
        ] = None,
        SupportedIdentityProviders: List[str] = None,
        CallbackURLs: List[str] = None,
        LogoutURLs: List[str] = None,
        DefaultRedirectURI: str = None,
        AllowedOAuthFlows: List[Literal["code", "implicit", "client_credentials"]] = None,
        AllowedOAuthScopes: List[str] = None,
        AllowedOAuthFlowsUserPoolClient: bool = None,
        AnalyticsConfiguration: ClientUpdateUserPoolClientAnalyticsConfigurationTypeDef = None,
        PreventUserExistenceErrors: Literal["LEGACY", "ENABLED"] = None,
    ) -> ClientUpdateUserPoolClientResponseTypeDef:
        """
        [Client.update_user_pool_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_client)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_pool_domain(
        self,
        Domain: str,
        UserPoolId: str,
        CustomDomainConfig: ClientUpdateUserPoolDomainCustomDomainConfigTypeDef,
    ) -> ClientUpdateUserPoolDomainResponseTypeDef:
        """
        [Client.update_user_pool_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify_software_token(
        self,
        UserCode: str,
        AccessToken: str = None,
        Session: str = None,
        FriendlyDeviceName: str = None,
    ) -> ClientVerifySoftwareTokenResponseTypeDef:
        """
        [Client.verify_software_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_software_token)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify_user_attribute(
        self, AccessToken: str, AttributeName: str, Code: str
    ) -> Dict[str, Any]:
        """
        [Client.verify_user_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_user_attribute)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["admin_list_groups_for_user"]
    ) -> paginator_scope.AdminListGroupsForUserPaginator:
        """
        [Paginator.AdminListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["admin_list_user_auth_events"]
    ) -> paginator_scope.AdminListUserAuthEventsPaginator:
        """
        [Paginator.AdminListUserAuthEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> paginator_scope.ListGroupsPaginator:
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_identity_providers"]
    ) -> paginator_scope.ListIdentityProvidersPaginator:
        """
        [Paginator.ListIdentityProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_servers"]
    ) -> paginator_scope.ListResourceServersPaginator:
        """
        [Paginator.ListResourceServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_user_pool_clients"]
    ) -> paginator_scope.ListUserPoolClientsPaginator:
        """
        [Paginator.ListUserPoolClients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_user_pools"]
    ) -> paginator_scope.ListUserPoolsPaginator:
        """
        [Paginator.ListUserPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> paginator_scope.ListUsersPaginator:
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_users_in_group"]
    ) -> paginator_scope.ListUsersInGroupPaginator:
        """
        [Paginator.ListUsersInGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup)
        """


class Exceptions:
    AliasExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    CodeDeliveryFailureException: Boto3ClientError
    CodeMismatchException: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DuplicateProviderException: Boto3ClientError
    EnableSoftwareTokenMFAException: Boto3ClientError
    ExpiredCodeException: Boto3ClientError
    GroupExistsException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidEmailRoleAccessPolicyException: Boto3ClientError
    InvalidLambdaResponseException: Boto3ClientError
    InvalidOAuthFlowException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidPasswordException: Boto3ClientError
    InvalidSmsRoleAccessPolicyException: Boto3ClientError
    InvalidSmsRoleTrustRelationshipException: Boto3ClientError
    InvalidUserPoolConfigurationException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MFAMethodNotFoundException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    PasswordResetRequiredException: Boto3ClientError
    PreconditionNotMetException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ScopeDoesNotExistException: Boto3ClientError
    SoftwareTokenMFANotFoundException: Boto3ClientError
    TooManyFailedAttemptsException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnexpectedLambdaException: Boto3ClientError
    UnsupportedIdentityProviderException: Boto3ClientError
    UnsupportedUserStateException: Boto3ClientError
    UserImportInProgressException: Boto3ClientError
    UserLambdaValidationException: Boto3ClientError
    UserNotConfirmedException: Boto3ClientError
    UserNotFoundException: Boto3ClientError
    UserPoolAddOnNotEnabledException: Boto3ClientError
    UserPoolTaggingException: Boto3ClientError
    UsernameExistsException: Boto3ClientError
