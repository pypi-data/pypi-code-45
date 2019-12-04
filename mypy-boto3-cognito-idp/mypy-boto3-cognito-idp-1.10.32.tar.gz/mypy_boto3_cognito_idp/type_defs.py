"Main interface for cognito-idp service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "AdminListGroupsForUserPaginatePaginationConfigTypeDef",
    "AdminListGroupsForUserPaginateResponseGroupsTypeDef",
    "AdminListGroupsForUserPaginateResponseTypeDef",
    "AdminListUserAuthEventsPaginatePaginationConfigTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef",
    "AdminListUserAuthEventsPaginateResponseTypeDef",
    "ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef",
    "ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef",
    "ClientAddCustomAttributesCustomAttributesTypeDef",
    "ClientAdminCreateUserResponseUserAttributesTypeDef",
    "ClientAdminCreateUserResponseUserMFAOptionsTypeDef",
    "ClientAdminCreateUserResponseUserTypeDef",
    "ClientAdminCreateUserResponseTypeDef",
    "ClientAdminCreateUserUserAttributesTypeDef",
    "ClientAdminCreateUserValidationDataTypeDef",
    "ClientAdminDisableProviderForUserUserTypeDef",
    "ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef",
    "ClientAdminGetDeviceResponseDeviceTypeDef",
    "ClientAdminGetDeviceResponseTypeDef",
    "ClientAdminGetUserResponseMFAOptionsTypeDef",
    "ClientAdminGetUserResponseUserAttributesTypeDef",
    "ClientAdminGetUserResponseTypeDef",
    "ClientAdminInitiateAuthAnalyticsMetadataTypeDef",
    "ClientAdminInitiateAuthContextDataHttpHeadersTypeDef",
    "ClientAdminInitiateAuthContextDataTypeDef",
    "ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientAdminInitiateAuthResponseAuthenticationResultTypeDef",
    "ClientAdminInitiateAuthResponseTypeDef",
    "ClientAdminLinkProviderForUserDestinationUserTypeDef",
    "ClientAdminLinkProviderForUserSourceUserTypeDef",
    "ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef",
    "ClientAdminListDevicesResponseDevicesTypeDef",
    "ClientAdminListDevicesResponseTypeDef",
    "ClientAdminListGroupsForUserResponseGroupsTypeDef",
    "ClientAdminListGroupsForUserResponseTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsTypeDef",
    "ClientAdminListUserAuthEventsResponseTypeDef",
    "ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef",
    "ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef",
    "ClientAdminRespondToAuthChallengeContextDataTypeDef",
    "ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    "ClientAdminRespondToAuthChallengeResponseTypeDef",
    "ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    "ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    "ClientAdminSetUserSettingsMFAOptionsTypeDef",
    "ClientAdminUpdateUserAttributesUserAttributesTypeDef",
    "ClientAssociateSoftwareTokenResponseTypeDef",
    "ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef",
    "ClientConfirmDeviceResponseTypeDef",
    "ClientConfirmForgotPasswordAnalyticsMetadataTypeDef",
    "ClientConfirmForgotPasswordUserContextDataTypeDef",
    "ClientConfirmSignUpAnalyticsMetadataTypeDef",
    "ClientConfirmSignUpUserContextDataTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateIdentityProviderResponseIdentityProviderTypeDef",
    "ClientCreateIdentityProviderResponseTypeDef",
    "ClientCreateResourceServerResponseResourceServerScopesTypeDef",
    "ClientCreateResourceServerResponseResourceServerTypeDef",
    "ClientCreateResourceServerResponseTypeDef",
    "ClientCreateResourceServerScopesTypeDef",
    "ClientCreateUserImportJobResponseUserImportJobTypeDef",
    "ClientCreateUserImportJobResponseTypeDef",
    "ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    "ClientCreateUserPoolAccountRecoverySettingTypeDef",
    "ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientCreateUserPoolAdminCreateUserConfigTypeDef",
    "ClientCreateUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientCreateUserPoolClientResponseUserPoolClientTypeDef",
    "ClientCreateUserPoolClientResponseTypeDef",
    "ClientCreateUserPoolDeviceConfigurationTypeDef",
    "ClientCreateUserPoolDomainCustomDomainConfigTypeDef",
    "ClientCreateUserPoolDomainResponseTypeDef",
    "ClientCreateUserPoolEmailConfigurationTypeDef",
    "ClientCreateUserPoolLambdaConfigTypeDef",
    "ClientCreateUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientCreateUserPoolPoliciesTypeDef",
    "ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    "ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef",
    "ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    "ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef",
    "ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientCreateUserPoolResponseUserPoolPoliciesTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef",
    "ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    "ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    "ClientCreateUserPoolResponseUserPoolTypeDef",
    "ClientCreateUserPoolResponseTypeDef",
    "ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef",
    "ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef",
    "ClientCreateUserPoolSchemaTypeDef",
    "ClientCreateUserPoolSmsConfigurationTypeDef",
    "ClientCreateUserPoolUserPoolAddOnsTypeDef",
    "ClientCreateUserPoolVerificationMessageTemplateTypeDef",
    "ClientDescribeIdentityProviderResponseIdentityProviderTypeDef",
    "ClientDescribeIdentityProviderResponseTypeDef",
    "ClientDescribeResourceServerResponseResourceServerScopesTypeDef",
    "ClientDescribeResourceServerResponseResourceServerTypeDef",
    "ClientDescribeResourceServerResponseTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseTypeDef",
    "ClientDescribeUserImportJobResponseUserImportJobTypeDef",
    "ClientDescribeUserImportJobResponseTypeDef",
    "ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientDescribeUserPoolClientResponseUserPoolClientTypeDef",
    "ClientDescribeUserPoolClientResponseTypeDef",
    "ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef",
    "ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef",
    "ClientDescribeUserPoolDomainResponseTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    "ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef",
    "ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    "ClientDescribeUserPoolResponseUserPoolTypeDef",
    "ClientDescribeUserPoolResponseTypeDef",
    "ClientForgotPasswordAnalyticsMetadataTypeDef",
    "ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef",
    "ClientForgotPasswordResponseTypeDef",
    "ClientForgotPasswordUserContextDataTypeDef",
    "ClientGetCsvHeaderResponseTypeDef",
    "ClientGetDeviceResponseDeviceDeviceAttributesTypeDef",
    "ClientGetDeviceResponseDeviceTypeDef",
    "ClientGetDeviceResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef",
    "ClientGetIdentityProviderByIdentifierResponseTypeDef",
    "ClientGetSigningCertificateResponseTypeDef",
    "ClientGetUiCustomizationResponseUICustomizationTypeDef",
    "ClientGetUiCustomizationResponseTypeDef",
    "ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef",
    "ClientGetUserAttributeVerificationCodeResponseTypeDef",
    "ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseTypeDef",
    "ClientGetUserResponseMFAOptionsTypeDef",
    "ClientGetUserResponseUserAttributesTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientInitiateAuthAnalyticsMetadataTypeDef",
    "ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientInitiateAuthResponseAuthenticationResultTypeDef",
    "ClientInitiateAuthResponseTypeDef",
    "ClientInitiateAuthUserContextDataTypeDef",
    "ClientListDevicesResponseDevicesDeviceAttributesTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListIdentityProvidersResponseProvidersTypeDef",
    "ClientListIdentityProvidersResponseTypeDef",
    "ClientListResourceServersResponseResourceServersScopesTypeDef",
    "ClientListResourceServersResponseResourceServersTypeDef",
    "ClientListResourceServersResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUserImportJobsResponseUserImportJobsTypeDef",
    "ClientListUserImportJobsResponseTypeDef",
    "ClientListUserPoolClientsResponseUserPoolClientsTypeDef",
    "ClientListUserPoolClientsResponseTypeDef",
    "ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef",
    "ClientListUserPoolsResponseUserPoolsTypeDef",
    "ClientListUserPoolsResponseTypeDef",
    "ClientListUsersInGroupResponseUsersAttributesTypeDef",
    "ClientListUsersInGroupResponseUsersMFAOptionsTypeDef",
    "ClientListUsersInGroupResponseUsersTypeDef",
    "ClientListUsersInGroupResponseTypeDef",
    "ClientListUsersResponseUsersAttributesTypeDef",
    "ClientListUsersResponseUsersMFAOptionsTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientResendConfirmationCodeAnalyticsMetadataTypeDef",
    "ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef",
    "ClientResendConfirmationCodeResponseTypeDef",
    "ClientResendConfirmationCodeUserContextDataTypeDef",
    "ClientRespondToAuthChallengeAnalyticsMetadataTypeDef",
    "ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    "ClientRespondToAuthChallengeResponseTypeDef",
    "ClientRespondToAuthChallengeUserContextDataTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseTypeDef",
    "ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientSetUiCustomizationResponseUICustomizationTypeDef",
    "ClientSetUiCustomizationResponseTypeDef",
    "ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    "ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    "ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseTypeDef",
    "ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef",
    "ClientSetUserSettingsMFAOptionsTypeDef",
    "ClientSignUpAnalyticsMetadataTypeDef",
    "ClientSignUpResponseCodeDeliveryDetailsTypeDef",
    "ClientSignUpResponseTypeDef",
    "ClientSignUpUserAttributesTypeDef",
    "ClientSignUpUserContextDataTypeDef",
    "ClientSignUpValidationDataTypeDef",
    "ClientStartUserImportJobResponseUserImportJobTypeDef",
    "ClientStartUserImportJobResponseTypeDef",
    "ClientStopUserImportJobResponseUserImportJobTypeDef",
    "ClientStopUserImportJobResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateIdentityProviderResponseIdentityProviderTypeDef",
    "ClientUpdateIdentityProviderResponseTypeDef",
    "ClientUpdateResourceServerResponseResourceServerScopesTypeDef",
    "ClientUpdateResourceServerResponseResourceServerTypeDef",
    "ClientUpdateResourceServerResponseTypeDef",
    "ClientUpdateResourceServerScopesTypeDef",
    "ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef",
    "ClientUpdateUserAttributesResponseTypeDef",
    "ClientUpdateUserAttributesUserAttributesTypeDef",
    "ClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    "ClientUpdateUserPoolAccountRecoverySettingTypeDef",
    "ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientUpdateUserPoolAdminCreateUserConfigTypeDef",
    "ClientUpdateUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientUpdateUserPoolClientResponseUserPoolClientTypeDef",
    "ClientUpdateUserPoolClientResponseTypeDef",
    "ClientUpdateUserPoolDeviceConfigurationTypeDef",
    "ClientUpdateUserPoolDomainCustomDomainConfigTypeDef",
    "ClientUpdateUserPoolDomainResponseTypeDef",
    "ClientUpdateUserPoolEmailConfigurationTypeDef",
    "ClientUpdateUserPoolLambdaConfigTypeDef",
    "ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientUpdateUserPoolPoliciesTypeDef",
    "ClientUpdateUserPoolSmsConfigurationTypeDef",
    "ClientUpdateUserPoolUserPoolAddOnsTypeDef",
    "ClientUpdateUserPoolVerificationMessageTemplateTypeDef",
    "ClientVerifySoftwareTokenResponseTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "ListIdentityProvidersPaginatePaginationConfigTypeDef",
    "ListIdentityProvidersPaginateResponseProvidersTypeDef",
    "ListIdentityProvidersPaginateResponseTypeDef",
    "ListResourceServersPaginatePaginationConfigTypeDef",
    "ListResourceServersPaginateResponseResourceServersScopesTypeDef",
    "ListResourceServersPaginateResponseResourceServersTypeDef",
    "ListResourceServersPaginateResponseTypeDef",
    "ListUserPoolClientsPaginatePaginationConfigTypeDef",
    "ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef",
    "ListUserPoolClientsPaginateResponseTypeDef",
    "ListUserPoolsPaginatePaginationConfigTypeDef",
    "ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef",
    "ListUserPoolsPaginateResponseUserPoolsTypeDef",
    "ListUserPoolsPaginateResponseTypeDef",
    "ListUsersInGroupPaginatePaginationConfigTypeDef",
    "ListUsersInGroupPaginateResponseUsersAttributesTypeDef",
    "ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef",
    "ListUsersInGroupPaginateResponseUsersTypeDef",
    "ListUsersInGroupPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUsersAttributesTypeDef",
    "ListUsersPaginateResponseUsersMFAOptionsTypeDef",
    "ListUsersPaginateResponseUsersTypeDef",
    "ListUsersPaginateResponseTypeDef",
)


_AdminListGroupsForUserPaginatePaginationConfigTypeDef = TypedDict(
    "_AdminListGroupsForUserPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class AdminListGroupsForUserPaginatePaginationConfigTypeDef(
    _AdminListGroupsForUserPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_AdminListGroupsForUserPaginateResponseGroupsTypeDef = TypedDict(
    "_AdminListGroupsForUserPaginateResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class AdminListGroupsForUserPaginateResponseGroupsTypeDef(
    _AdminListGroupsForUserPaginateResponseGroupsTypeDef
):
    """
    - *(dict) --*

      The group type.
      - **GroupName** *(string) --*

        The name of the group.
    """


_AdminListGroupsForUserPaginateResponseTypeDef = TypedDict(
    "_AdminListGroupsForUserPaginateResponseTypeDef",
    {"Groups": List[AdminListGroupsForUserPaginateResponseGroupsTypeDef]},
    total=False,
)


class AdminListGroupsForUserPaginateResponseTypeDef(_AdminListGroupsForUserPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The groups that the user belongs to.
        - *(dict) --*

          The group type.
          - **GroupName** *(string) --*

            The name of the group.
    """


_AdminListUserAuthEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class AdminListUserAuthEventsPaginatePaginationConfigTypeDef(
    _AdminListUserAuthEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef",
    {
        "ChallengeName": Literal["Password", "Mfa"],
        "ChallengeResponse": Literal["Success", "Failure"],
    },
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef
):
    pass


_AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef",
    {"IpAddress": str, "DeviceName": str, "Timezone": str, "City": str, "Country": str},
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef
):
    pass


_AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef",
    {"FeedbackValue": Literal["Valid", "Invalid"], "Provider": str, "FeedbackDate": datetime},
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef
):
    pass


_AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef",
    {
        "RiskDecision": Literal["NoRisk", "AccountTakeover", "Block"],
        "RiskLevel": Literal["Low", "Medium", "High"],
    },
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef
):
    pass


_AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef",
    {
        "EventId": str,
        "EventType": Literal["SignIn", "SignUp", "ForgotPassword"],
        "CreationDate": datetime,
        "EventResponse": Literal["Success", "Failure"],
        "EventRisk": AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef,
        "ChallengeResponses": List[
            AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef
        ],
        "EventContextData": AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef,
        "EventFeedback": AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef,
    },
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef
):
    """
    - *(dict) --*

      The authentication event type.
      - **EventId** *(string) --*

        The event ID.
    """


_AdminListUserAuthEventsPaginateResponseTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseTypeDef",
    {"AuthEvents": List[AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef]},
    total=False,
)


class AdminListUserAuthEventsPaginateResponseTypeDef(
    _AdminListUserAuthEventsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AuthEvents** *(list) --*

        The response object. It includes the ``EventID`` , ``EventType`` , ``CreationDate`` ,
        ``EventRisk`` , and ``EventResponse`` .
        - *(dict) --*

          The authentication event type.
          - **EventId** *(string) --*

            The event ID.
    """


_ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "_ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef(
    _ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef
):
    pass


_ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "_ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)


class ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef(
    _ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef
):
    pass


_ClientAddCustomAttributesCustomAttributesTypeDef = TypedDict(
    "_ClientAddCustomAttributesCustomAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": Literal["String", "Number", "DateTime", "Boolean"],
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)


class ClientAddCustomAttributesCustomAttributesTypeDef(
    _ClientAddCustomAttributesCustomAttributesTypeDef
):
    """
    - *(dict) --*

      Contains information about the schema attribute.
      - **Name** *(string) --*

        A schema attribute of the name type.
    """


_ClientAdminCreateUserResponseUserAttributesTypeDef = TypedDict(
    "_ClientAdminCreateUserResponseUserAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientAdminCreateUserResponseUserAttributesTypeDef(
    _ClientAdminCreateUserResponseUserAttributesTypeDef
):
    pass


_ClientAdminCreateUserResponseUserMFAOptionsTypeDef = TypedDict(
    "_ClientAdminCreateUserResponseUserMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientAdminCreateUserResponseUserMFAOptionsTypeDef(
    _ClientAdminCreateUserResponseUserMFAOptionsTypeDef
):
    pass


_ClientAdminCreateUserResponseUserTypeDef = TypedDict(
    "_ClientAdminCreateUserResponseUserTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientAdminCreateUserResponseUserAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ClientAdminCreateUserResponseUserMFAOptionsTypeDef],
    },
    total=False,
)


class ClientAdminCreateUserResponseUserTypeDef(_ClientAdminCreateUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The newly created user.
      - **Username** *(string) --*

        The user name of the user you wish to describe.
    """


_ClientAdminCreateUserResponseTypeDef = TypedDict(
    "_ClientAdminCreateUserResponseTypeDef",
    {"User": ClientAdminCreateUserResponseUserTypeDef},
    total=False,
)


class ClientAdminCreateUserResponseTypeDef(_ClientAdminCreateUserResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to the request to create the user.
      - **User** *(dict) --*

        The newly created user.
        - **Username** *(string) --*

          The user name of the user you wish to describe.
    """


_RequiredClientAdminCreateUserUserAttributesTypeDef = TypedDict(
    "_RequiredClientAdminCreateUserUserAttributesTypeDef", {"Name": str}
)
_OptionalClientAdminCreateUserUserAttributesTypeDef = TypedDict(
    "_OptionalClientAdminCreateUserUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientAdminCreateUserUserAttributesTypeDef(
    _RequiredClientAdminCreateUserUserAttributesTypeDef,
    _OptionalClientAdminCreateUserUserAttributesTypeDef,
):
    """
    - *(dict) --*

      Specifies whether the attribute is standard or custom.
      - **Name** *(string) --***[REQUIRED]**

        The name of the attribute.
    """


_RequiredClientAdminCreateUserValidationDataTypeDef = TypedDict(
    "_RequiredClientAdminCreateUserValidationDataTypeDef", {"Name": str}
)
_OptionalClientAdminCreateUserValidationDataTypeDef = TypedDict(
    "_OptionalClientAdminCreateUserValidationDataTypeDef", {"Value": str}, total=False
)


class ClientAdminCreateUserValidationDataTypeDef(
    _RequiredClientAdminCreateUserValidationDataTypeDef,
    _OptionalClientAdminCreateUserValidationDataTypeDef,
):
    """
    - *(dict) --*

      Specifies whether the attribute is standard or custom.
      - **Name** *(string) --***[REQUIRED]**

        The name of the attribute.
    """


_ClientAdminDisableProviderForUserUserTypeDef = TypedDict(
    "_ClientAdminDisableProviderForUserUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)


class ClientAdminDisableProviderForUserUserTypeDef(_ClientAdminDisableProviderForUserUserTypeDef):
    """
    The user to be disabled.
    - **ProviderName** *(string) --*

      The name of the provider, for example, Facebook, Google, or Login with Amazon.
    """


_ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef = TypedDict(
    "_ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef(
    _ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef
):
    pass


_ClientAdminGetDeviceResponseDeviceTypeDef = TypedDict(
    "_ClientAdminGetDeviceResponseDeviceTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)


class ClientAdminGetDeviceResponseDeviceTypeDef(_ClientAdminGetDeviceResponseDeviceTypeDef):
    """
    - **Device** *(dict) --*

      The device.
      - **DeviceKey** *(string) --*

        The device key.
    """


_ClientAdminGetDeviceResponseTypeDef = TypedDict(
    "_ClientAdminGetDeviceResponseTypeDef",
    {"Device": ClientAdminGetDeviceResponseDeviceTypeDef},
    total=False,
)


class ClientAdminGetDeviceResponseTypeDef(_ClientAdminGetDeviceResponseTypeDef):
    """
    - *(dict) --*

      Gets the device response, as an administrator.
      - **Device** *(dict) --*

        The device.
        - **DeviceKey** *(string) --*

          The device key.
    """


_ClientAdminGetUserResponseMFAOptionsTypeDef = TypedDict(
    "_ClientAdminGetUserResponseMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientAdminGetUserResponseMFAOptionsTypeDef(_ClientAdminGetUserResponseMFAOptionsTypeDef):
    pass


_ClientAdminGetUserResponseUserAttributesTypeDef = TypedDict(
    "_ClientAdminGetUserResponseUserAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientAdminGetUserResponseUserAttributesTypeDef(
    _ClientAdminGetUserResponseUserAttributesTypeDef
):
    pass


_ClientAdminGetUserResponseTypeDef = TypedDict(
    "_ClientAdminGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[ClientAdminGetUserResponseUserAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ClientAdminGetUserResponseMFAOptionsTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)


class ClientAdminGetUserResponseTypeDef(_ClientAdminGetUserResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server from the request to get the specified user as an
      administrator.
      - **Username** *(string) --*

        The user name of the user about whom you are receiving information.
    """


_ClientAdminInitiateAuthAnalyticsMetadataTypeDef = TypedDict(
    "_ClientAdminInitiateAuthAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)


class ClientAdminInitiateAuthAnalyticsMetadataTypeDef(
    _ClientAdminInitiateAuthAnalyticsMetadataTypeDef
):
    """
    The analytics metadata for collecting Amazon Pinpoint metrics for ``AdminInitiateAuth`` calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientAdminInitiateAuthContextDataHttpHeadersTypeDef = TypedDict(
    "_ClientAdminInitiateAuthContextDataHttpHeadersTypeDef",
    {"headerName": str, "headerValue": str},
    total=False,
)


class ClientAdminInitiateAuthContextDataHttpHeadersTypeDef(
    _ClientAdminInitiateAuthContextDataHttpHeadersTypeDef
):
    pass


_RequiredClientAdminInitiateAuthContextDataTypeDef = TypedDict(
    "_RequiredClientAdminInitiateAuthContextDataTypeDef", {"IpAddress": str}
)
_OptionalClientAdminInitiateAuthContextDataTypeDef = TypedDict(
    "_OptionalClientAdminInitiateAuthContextDataTypeDef",
    {
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List[ClientAdminInitiateAuthContextDataHttpHeadersTypeDef],
        "EncodedData": str,
    },
    total=False,
)


class ClientAdminInitiateAuthContextDataTypeDef(
    _RequiredClientAdminInitiateAuthContextDataTypeDef,
    _OptionalClientAdminInitiateAuthContextDataTypeDef,
):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **IpAddress** *(string) --***[REQUIRED]**

      Source IP address of your user.
    """


_ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "_ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)


class ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef(
    _ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef
):
    pass


_ClientAdminInitiateAuthResponseAuthenticationResultTypeDef = TypedDict(
    "_ClientAdminInitiateAuthResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)


class ClientAdminInitiateAuthResponseAuthenticationResultTypeDef(
    _ClientAdminInitiateAuthResponseAuthenticationResultTypeDef
):
    pass


_ClientAdminInitiateAuthResponseTypeDef = TypedDict(
    "_ClientAdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": Literal[
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
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientAdminInitiateAuthResponseAuthenticationResultTypeDef,
    },
    total=False,
)


class ClientAdminInitiateAuthResponseTypeDef(_ClientAdminInitiateAuthResponseTypeDef):
    """
    - *(dict) --*

      Initiates the authentication response, as an administrator.
      - **ChallengeName** *(string) --*

        The name of the challenge which you are responding to with this call. This is returned to
        you in the ``AdminInitiateAuth`` response if you need to pass another challenge.
        * ``MFA_SETUP`` : If MFA is required, users who do not have at least one of the MFA methods
        set up are presented with an ``MFA_SETUP`` challenge. The user must set up at least one MFA
        type to continue to authenticate.
        * ``SELECT_MFA_TYPE`` : Selects the MFA type. Valid MFA options are ``SMS_MFA`` for text SMS
        MFA, and ``SOFTWARE_TOKEN_MFA`` for TOTP software token MFA.
        * ``SMS_MFA`` : Next challenge is to supply an ``SMS_MFA_CODE`` , delivered via SMS.
        * ``PASSWORD_VERIFIER`` : Next challenge is to supply ``PASSWORD_CLAIM_SIGNATURE`` ,
        ``PASSWORD_CLAIM_SECRET_BLOCK`` , and ``TIMESTAMP`` after the client-side SRP calculations.
        * ``CUSTOM_CHALLENGE`` : This is returned if your custom authentication flow determines that
        the user should pass another challenge before tokens are issued.
        * ``DEVICE_SRP_AUTH`` : If device tracking was enabled on your user pool and the previous
        challenges were passed, this challenge is returned so that Amazon Cognito can start tracking
        this device.
        * ``DEVICE_PASSWORD_VERIFIER`` : Similar to ``PASSWORD_VERIFIER`` , but for devices only.
        * ``ADMIN_NO_SRP_AUTH`` : This is returned if you need to authenticate with ``USERNAME`` and
        ``PASSWORD`` directly. An app client must be enabled to use this flow.
        * ``NEW_PASSWORD_REQUIRED`` : For users which are required to change their passwords after
        successful first login. This challenge should be passed with ``NEW_PASSWORD`` and any other
        required attributes.
    """


_ClientAdminLinkProviderForUserDestinationUserTypeDef = TypedDict(
    "_ClientAdminLinkProviderForUserDestinationUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)


class ClientAdminLinkProviderForUserDestinationUserTypeDef(
    _ClientAdminLinkProviderForUserDestinationUserTypeDef
):
    """
    The existing user in the user pool to be linked to the external identity provider user account.
    Can be a native (Username + Password) Cognito User Pools user or a federated user (for example,
    a SAML or Facebook user). If the user doesn't exist, an exception is thrown. This is the user
    that is returned when the new user (with the linked identity provider attribute) signs in.
    For a native username + password user, the ``ProviderAttributeValue`` for the
    ``DestinationUser`` should be the username in the user pool. For a federated user, it should be
    the provider-specific ``user_id`` .
    The ``ProviderAttributeName`` of the ``DestinationUser`` is ignored.
    The ``ProviderName`` should be set to ``Cognito`` for users in Cognito user pools.
    - **ProviderName** *(string) --*

      The name of the provider, for example, Facebook, Google, or Login with Amazon.
    """


_ClientAdminLinkProviderForUserSourceUserTypeDef = TypedDict(
    "_ClientAdminLinkProviderForUserSourceUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)


class ClientAdminLinkProviderForUserSourceUserTypeDef(
    _ClientAdminLinkProviderForUserSourceUserTypeDef
):
    """
    An external identity provider account for a user who does not currently exist yet in the user
    pool. This user must be a federated user (for example, a SAML or Facebook user), not another
    native user.
    If the ``SourceUser`` is a federated social identity provider user (Facebook, Google, or Login
    with Amazon), you must set the ``ProviderAttributeName`` to ``Cognito_Subject`` . For social
    identity providers, the ``ProviderName`` will be ``Facebook`` , ``Google`` , or
    ``LoginWithAmazon`` , and Cognito will automatically parse the Facebook, Google, and Login with
    Amazon tokens for ``id`` , ``sub`` , and ``user_id`` , respectively. The
    ``ProviderAttributeValue`` for the user must be the same value as the ``id`` , ``sub`` , or
    ``user_id`` value found in the social identity provider token.
    For SAML, the ``ProviderAttributeName`` can be any value that matches a claim in the SAML
    assertion. If you wish to link SAML users based on the subject of the SAML assertion, you should
    map the subject to a claim through the SAML identity provider and submit that claim name as the
    ``ProviderAttributeName`` . If you set ``ProviderAttributeName`` to ``Cognito_Subject`` ,
    Cognito will automatically parse the default unique identifier found in the subject from the
    SAML token.
    - **ProviderName** *(string) --*

      The name of the provider, for example, Facebook, Google, or Login with Amazon.
    """


_ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef = TypedDict(
    "_ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef(
    _ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef
):
    pass


_ClientAdminListDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientAdminListDevicesResponseDevicesTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)


class ClientAdminListDevicesResponseDevicesTypeDef(_ClientAdminListDevicesResponseDevicesTypeDef):
    """
    - *(dict) --*

      The device type.
      - **DeviceKey** *(string) --*

        The device key.
    """


_ClientAdminListDevicesResponseTypeDef = TypedDict(
    "_ClientAdminListDevicesResponseTypeDef",
    {"Devices": List[ClientAdminListDevicesResponseDevicesTypeDef], "PaginationToken": str},
    total=False,
)


class ClientAdminListDevicesResponseTypeDef(_ClientAdminListDevicesResponseTypeDef):
    """
    - *(dict) --*

      Lists the device's response, as an administrator.
      - **Devices** *(list) --*

        The devices in the list of devices response.
        - *(dict) --*

          The device type.
          - **DeviceKey** *(string) --*

            The device key.
    """


_ClientAdminListGroupsForUserResponseGroupsTypeDef = TypedDict(
    "_ClientAdminListGroupsForUserResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientAdminListGroupsForUserResponseGroupsTypeDef(
    _ClientAdminListGroupsForUserResponseGroupsTypeDef
):
    """
    - *(dict) --*

      The group type.
      - **GroupName** *(string) --*

        The name of the group.
    """


_ClientAdminListGroupsForUserResponseTypeDef = TypedDict(
    "_ClientAdminListGroupsForUserResponseTypeDef",
    {"Groups": List[ClientAdminListGroupsForUserResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientAdminListGroupsForUserResponseTypeDef(_ClientAdminListGroupsForUserResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The groups that the user belongs to.
        - *(dict) --*

          The group type.
          - **GroupName** *(string) --*

            The name of the group.
    """


_ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef",
    {
        "ChallengeName": Literal["Password", "Mfa"],
        "ChallengeResponse": Literal["Success", "Failure"],
    },
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef
):
    pass


_ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef",
    {"IpAddress": str, "DeviceName": str, "Timezone": str, "City": str, "Country": str},
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef
):
    pass


_ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef",
    {"FeedbackValue": Literal["Valid", "Invalid"], "Provider": str, "FeedbackDate": datetime},
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef
):
    pass


_ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef",
    {
        "RiskDecision": Literal["NoRisk", "AccountTakeover", "Block"],
        "RiskLevel": Literal["Low", "Medium", "High"],
    },
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef
):
    pass


_ClientAdminListUserAuthEventsResponseAuthEventsTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsTypeDef",
    {
        "EventId": str,
        "EventType": Literal["SignIn", "SignUp", "ForgotPassword"],
        "CreationDate": datetime,
        "EventResponse": Literal["Success", "Failure"],
        "EventRisk": ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef,
        "ChallengeResponses": List[
            ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef
        ],
        "EventContextData": ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef,
        "EventFeedback": ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef,
    },
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsTypeDef
):
    """
    - *(dict) --*

      The authentication event type.
      - **EventId** *(string) --*

        The event ID.
    """


_ClientAdminListUserAuthEventsResponseTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseTypeDef",
    {"AuthEvents": List[ClientAdminListUserAuthEventsResponseAuthEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientAdminListUserAuthEventsResponseTypeDef(_ClientAdminListUserAuthEventsResponseTypeDef):
    """
    - *(dict) --*

      - **AuthEvents** *(list) --*

        The response object. It includes the ``EventID`` , ``EventType`` , ``CreationDate`` ,
        ``EventRisk`` , and ``EventResponse`` .
        - *(dict) --*

          The authentication event type.
          - **EventId** *(string) --*

            The event ID.
    """


_ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef(
    _ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef
):
    """
    The analytics metadata for collecting Amazon Pinpoint metrics for
    ``AdminRespondToAuthChallenge`` calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef",
    {"headerName": str, "headerValue": str},
    total=False,
)


class ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef(
    _ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef
):
    pass


_RequiredClientAdminRespondToAuthChallengeContextDataTypeDef = TypedDict(
    "_RequiredClientAdminRespondToAuthChallengeContextDataTypeDef", {"IpAddress": str}
)
_OptionalClientAdminRespondToAuthChallengeContextDataTypeDef = TypedDict(
    "_OptionalClientAdminRespondToAuthChallengeContextDataTypeDef",
    {
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List[ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef],
        "EncodedData": str,
    },
    total=False,
)


class ClientAdminRespondToAuthChallengeContextDataTypeDef(
    _RequiredClientAdminRespondToAuthChallengeContextDataTypeDef,
    _OptionalClientAdminRespondToAuthChallengeContextDataTypeDef,
):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **IpAddress** *(string) --***[REQUIRED]**

      Source IP address of your user.
    """


_ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)


class ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef(
    _ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef
):
    pass


_ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)


class ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef(
    _ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef
):
    pass


_ClientAdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": Literal[
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
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef,
    },
    total=False,
)


class ClientAdminRespondToAuthChallengeResponseTypeDef(
    _ClientAdminRespondToAuthChallengeResponseTypeDef
):
    """
    - *(dict) --*

      Responds to the authentication challenge, as an administrator.
      - **ChallengeName** *(string) --*

        The name of the challenge. For more information, see .
    """


_ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef = TypedDict(
    "_ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)


class ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef(
    _ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef
):
    """
    The SMS text message MFA settings.
    - **Enabled** *(boolean) --*

      Specifies whether SMS text message MFA is enabled.
    """


_ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef = TypedDict(
    "_ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)


class ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef(
    _ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef
):
    """
    The time-based one-time password software token MFA settings.
    - **Enabled** *(boolean) --*

      Specifies whether software token MFA is enabled.
    """


_ClientAdminSetUserSettingsMFAOptionsTypeDef = TypedDict(
    "_ClientAdminSetUserSettingsMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientAdminSetUserSettingsMFAOptionsTypeDef(_ClientAdminSetUserSettingsMFAOptionsTypeDef):
    """
    - *(dict) --*

      *This data type is no longer supported.* You can use it only for SMS MFA configurations. You
      can't use it for TOTP software token MFA configurations.
      To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
      SetUserMFAPreference actions.
      To look up information about either type of MFA configuration, use the
      AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.
      - **DeliveryMedium** *(string) --*

        The delivery medium to send the MFA code. You can use this parameter to set only the ``SMS``
        delivery medium value.
    """


_RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef", {"Name": str}
)
_OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientAdminUpdateUserAttributesUserAttributesTypeDef(
    _RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef,
    _OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef,
):
    """
    - *(dict) --*

      Specifies whether the attribute is standard or custom.
      - **Name** *(string) --***[REQUIRED]**

        The name of the attribute.
    """


_ClientAssociateSoftwareTokenResponseTypeDef = TypedDict(
    "_ClientAssociateSoftwareTokenResponseTypeDef", {"SecretCode": str, "Session": str}, total=False
)


class ClientAssociateSoftwareTokenResponseTypeDef(_ClientAssociateSoftwareTokenResponseTypeDef):
    """
    - *(dict) --*

      - **SecretCode** *(string) --*

        A unique generated shared secret code that is used in the TOTP algorithm to generate a one
        time code.
    """


_ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef = TypedDict(
    "_ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef",
    {"PasswordVerifier": str, "Salt": str},
    total=False,
)


class ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef(
    _ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef
):
    """
    The configuration of the device secret verifier.
    - **PasswordVerifier** *(string) --*

      The password verifier.
    """


_ClientConfirmDeviceResponseTypeDef = TypedDict(
    "_ClientConfirmDeviceResponseTypeDef", {"UserConfirmationNecessary": bool}, total=False
)


class ClientConfirmDeviceResponseTypeDef(_ClientConfirmDeviceResponseTypeDef):
    """
    - *(dict) --*

      Confirms the device response.
      - **UserConfirmationNecessary** *(boolean) --*

        Indicates whether the user confirmation is necessary to confirm the device response.
    """


_ClientConfirmForgotPasswordAnalyticsMetadataTypeDef = TypedDict(
    "_ClientConfirmForgotPasswordAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientConfirmForgotPasswordAnalyticsMetadataTypeDef(
    _ClientConfirmForgotPasswordAnalyticsMetadataTypeDef
):
    """
    The Amazon Pinpoint analytics metadata for collecting metrics for ``ConfirmForgotPassword``
    calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientConfirmForgotPasswordUserContextDataTypeDef = TypedDict(
    "_ClientConfirmForgotPasswordUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientConfirmForgotPasswordUserContextDataTypeDef(
    _ClientConfirmForgotPasswordUserContextDataTypeDef
):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientConfirmSignUpAnalyticsMetadataTypeDef = TypedDict(
    "_ClientConfirmSignUpAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)


class ClientConfirmSignUpAnalyticsMetadataTypeDef(_ClientConfirmSignUpAnalyticsMetadataTypeDef):
    """
    The Amazon Pinpoint analytics metadata for collecting metrics for ``ConfirmSignUp`` calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientConfirmSignUpUserContextDataTypeDef = TypedDict(
    "_ClientConfirmSignUpUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientConfirmSignUpUserContextDataTypeDef(_ClientConfirmSignUpUserContextDataTypeDef):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The group object for the group.
      - **GroupName** *(string) --*

        The name of the group.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The group object for the group.
        - **GroupName** *(string) --*

          The name of the group.
    """


_ClientCreateIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "_ClientCreateIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientCreateIdentityProviderResponseIdentityProviderTypeDef(
    _ClientCreateIdentityProviderResponseIdentityProviderTypeDef
):
    """
    - **IdentityProvider** *(dict) --*

      The newly created identity provider object.
      - **UserPoolId** *(string) --*

        The user pool ID.
    """


_ClientCreateIdentityProviderResponseTypeDef = TypedDict(
    "_ClientCreateIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientCreateIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)


class ClientCreateIdentityProviderResponseTypeDef(_ClientCreateIdentityProviderResponseTypeDef):
    """
    - *(dict) --*

      - **IdentityProvider** *(dict) --*

        The newly created identity provider object.
        - **UserPoolId** *(string) --*

          The user pool ID.
    """


_ClientCreateResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "_ClientCreateResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ClientCreateResourceServerResponseResourceServerScopesTypeDef(
    _ClientCreateResourceServerResponseResourceServerScopesTypeDef
):
    pass


_ClientCreateResourceServerResponseResourceServerTypeDef = TypedDict(
    "_ClientCreateResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientCreateResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)


class ClientCreateResourceServerResponseResourceServerTypeDef(
    _ClientCreateResourceServerResponseResourceServerTypeDef
):
    """
    - **ResourceServer** *(dict) --*

      The newly created resource server.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that hosts the resource server.
    """


_ClientCreateResourceServerResponseTypeDef = TypedDict(
    "_ClientCreateResourceServerResponseTypeDef",
    {"ResourceServer": ClientCreateResourceServerResponseResourceServerTypeDef},
    total=False,
)


class ClientCreateResourceServerResponseTypeDef(_ClientCreateResourceServerResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceServer** *(dict) --*

        The newly created resource server.
        - **UserPoolId** *(string) --*

          The user pool ID for the user pool that hosts the resource server.
    """


_RequiredClientCreateResourceServerScopesTypeDef = TypedDict(
    "_RequiredClientCreateResourceServerScopesTypeDef", {"ScopeName": str}
)
_OptionalClientCreateResourceServerScopesTypeDef = TypedDict(
    "_OptionalClientCreateResourceServerScopesTypeDef", {"ScopeDescription": str}, total=False
)


class ClientCreateResourceServerScopesTypeDef(
    _RequiredClientCreateResourceServerScopesTypeDef,
    _OptionalClientCreateResourceServerScopesTypeDef,
):
    """
    - *(dict) --*

      A resource server scope.
      - **ScopeName** *(string) --***[REQUIRED]**

        The name of the scope.
    """


_ClientCreateUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "_ClientCreateUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientCreateUserImportJobResponseUserImportJobTypeDef(
    _ClientCreateUserImportJobResponseUserImportJobTypeDef
):
    """
    - **UserImportJob** *(dict) --*

      The job object that represents the user import job.
      - **JobName** *(string) --*

        The job name for the user import job.
    """


_ClientCreateUserImportJobResponseTypeDef = TypedDict(
    "_ClientCreateUserImportJobResponseTypeDef",
    {"UserImportJob": ClientCreateUserImportJobResponseUserImportJobTypeDef},
    total=False,
)


class ClientCreateUserImportJobResponseTypeDef(_ClientCreateUserImportJobResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to the request to create the user import job.
      - **UserImportJob** *(dict) --*

        The job object that represents the user import job.
        - **JobName** *(string) --*

          The job name for the user import job.
    """


_ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "_ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Priority": int, "Name": Literal["verified_email", "verified_phone_number", "admin_only"]},
    total=False,
)


class ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef(
    _ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
):
    pass


_ClientCreateUserPoolAccountRecoverySettingTypeDef = TypedDict(
    "_ClientCreateUserPoolAccountRecoverySettingTypeDef",
    {
        "RecoveryMechanisms": List[
            ClientCreateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
        ]
    },
    total=False,
)


class ClientCreateUserPoolAccountRecoverySettingTypeDef(
    _ClientCreateUserPoolAccountRecoverySettingTypeDef
):
    """
    Use this setting to define which verified available method a user can use to recover their
    password when they call ``ForgotPassword`` . It allows you to define a preferred method when a
    user has more than one method available. With this setting, SMS does not qualify for a valid
    password recovery mechanism if the user also has SMS MFA enabled. In the absence of this
    setting, Cognito uses the legacy behavior to determine the recovery method where SMS is
    preferred over email.
    .. note::

      Starting February 1, 2020, the value of ``AccountRecoverySetting`` will default to
      ``verified_email`` first and ``verified_phone_number`` as the second option for newly created
      user pools if no value is provided.
    """


_ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "_ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)


class ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef(
    _ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef
):
    pass


_ClientCreateUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolAdminCreateUserConfigTypeDef(
    _ClientCreateUserPoolAdminCreateUserConfigTypeDef
):
    """
    The configuration for ``AdminCreateUser`` requests.
    - **AllowAdminCreateUserOnly** *(boolean) --*

      Set to ``True`` if only the administrator is allowed to create user profiles. Set to ``False``
      if users can sign themselves up via an app.
    """


_RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef", {"ApplicationId": str}
)
_OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef",
    {"RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientCreateUserPoolClientAnalyticsConfigurationTypeDef(
    _RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef,
    _OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef,
):
    """
    The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.
    - **ApplicationId** *(string) --***[REQUIRED]**

      The application ID for an Amazon Pinpoint application.
    """


_ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef(
    _ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef
):
    pass


_ClientCreateUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "_ClientCreateUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[
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
        ],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[Literal["code", "implicit", "client_credentials"]],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": Literal["LEGACY", "ENABLED"],
    },
    total=False,
)


class ClientCreateUserPoolClientResponseUserPoolClientTypeDef(
    _ClientCreateUserPoolClientResponseUserPoolClientTypeDef
):
    """
    - **UserPoolClient** *(dict) --*

      The user pool client that was just created.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool client.
    """


_ClientCreateUserPoolClientResponseTypeDef = TypedDict(
    "_ClientCreateUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientCreateUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)


class ClientCreateUserPoolClientResponseTypeDef(_ClientCreateUserPoolClientResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to create a user pool client.
      - **UserPoolClient** *(dict) --*

        The user pool client that was just created.
        - **UserPoolId** *(string) --*

          The user pool ID for the user pool client.
    """


_ClientCreateUserPoolDeviceConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)


class ClientCreateUserPoolDeviceConfigurationTypeDef(
    _ClientCreateUserPoolDeviceConfigurationTypeDef
):
    """
    The device configuration.
    - **ChallengeRequiredOnNewDevice** *(boolean) --*

      Indicates whether a challenge is required on a new device. Only applicable to a new device.
    """


_ClientCreateUserPoolDomainCustomDomainConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolDomainCustomDomainConfigTypeDef", {"CertificateArn": str}
)


class ClientCreateUserPoolDomainCustomDomainConfigTypeDef(
    _ClientCreateUserPoolDomainCustomDomainConfigTypeDef
):
    """
    The configuration for a custom domain that hosts the sign-up and sign-in webpages for your
    application.
    Provide this parameter only if you want to use a custom domain for your user pool. Otherwise,
    you can exclude this parameter and use the Amazon Cognito hosted domain instead.
    For more information about the hosted domain and custom domains, see `Configuring a User Pool
    Domain
    <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html>`__
    .
    - **CertificateArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this
      certificate for the subdomain of your custom domain.
    """


_ClientCreateUserPoolDomainResponseTypeDef = TypedDict(
    "_ClientCreateUserPoolDomainResponseTypeDef", {"CloudFrontDomain": str}, total=False
)


class ClientCreateUserPoolDomainResponseTypeDef(_ClientCreateUserPoolDomainResponseTypeDef):
    """
    - *(dict) --*

      - **CloudFrontDomain** *(string) --*

        The Amazon CloudFront endpoint that you use as the target of the alias that you set up with
        your Domain Name Service (DNS) provider.
    """


_ClientCreateUserPoolEmailConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": Literal["COGNITO_DEFAULT", "DEVELOPER"],
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)


class ClientCreateUserPoolEmailConfigurationTypeDef(_ClientCreateUserPoolEmailConfigurationTypeDef):
    """
    The email configuration.
    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email address
      is used in one of the following ways, depending on the value that you specify for the
      ``EmailSendingAccount`` parameter:
      * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom FROM
      address when it emails your users by using its built-in email account.
      * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by calling
      Amazon SES on your behalf.
    """


_ClientCreateUserPoolLambdaConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientCreateUserPoolLambdaConfigTypeDef(_ClientCreateUserPoolLambdaConfigTypeDef):
    """
    The Lambda trigger configuration information for the new user pool.
    .. note::

      In a push model, event sources (such as Amazon S3 and custom applications) need permission to
      invoke a function. So you will need to make an extra call to add permission for these event
      sources to invoke your Lambda function.
      For more information on using the Lambda API to add permission, see `AddPermission
      <https://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html>`__ .
      For adding permission using the AWS CLI, see `add-permission
      <https://docs.aws.amazon.com/cli/latest/reference/lambda/add-permission.html>`__ .
    """


_ClientCreateUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "_ClientCreateUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)


class ClientCreateUserPoolPoliciesPasswordPolicyTypeDef(
    _ClientCreateUserPoolPoliciesPasswordPolicyTypeDef
):
    """
    - **PasswordPolicy** *(dict) --*

      The password policy.
      - **MinimumLength** *(integer) --*

        The minimum length of the password policy that you have set. Cannot be less than 6.
    """


_ClientCreateUserPoolPoliciesTypeDef = TypedDict(
    "_ClientCreateUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientCreateUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)


class ClientCreateUserPoolPoliciesTypeDef(_ClientCreateUserPoolPoliciesTypeDef):
    """
    The policies associated with the new user pool.
    - **PasswordPolicy** *(dict) --*

      The password policy.
      - **MinimumLength** *(integer) --*

        The minimum length of the password policy that you have set. Cannot be less than 6.
    """


_ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Priority": int, "Name": Literal["verified_email", "verified_phone_number", "admin_only"]},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef(
    _ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef",
    {
        "RecoveryMechanisms": List[
            ClientCreateUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
        ]
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef(
    _ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef(
    _ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef(
    _ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef(
    _ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": Literal["COGNITO_DEFAULT", "DEVELOPER"],
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef(
    _ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef(
    _ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef(
    _ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolPoliciesTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolPoliciesTypeDef(
    _ClientCreateUserPoolResponseUserPoolPoliciesTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef(
    _ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef(
    _ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": Literal["String", "Number", "DateTime", "Boolean"],
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef(
    _ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef(
    _ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": Literal["OFF", "AUDIT", "ENFORCED"]},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef(
    _ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": Literal["CONFIRM_WITH_LINK", "CONFIRM_WITH_CODE"],
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef(
    _ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef
):
    pass


_ClientCreateUserPoolResponseUserPoolTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": ClientCreateUserPoolResponseUserPoolPoliciesTypeDef,
        "LambdaConfig": ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List[ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef],
        "AutoVerifiedAttributes": List[Literal["phone_number", "email"]],
        "AliasAttributes": List[Literal["phone_number", "email", "preferred_username"]],
        "UsernameAttributes": List[Literal["phone_number", "email"]],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef,
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": Literal["OFF", "ON", "OPTIONAL"],
        "DeviceConfiguration": ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef,
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef,
        "SmsConfiguration": ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef,
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef,
        "UserPoolAddOns": ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef,
        "Arn": str,
        "AccountRecoverySetting": ClientCreateUserPoolResponseUserPoolAccountRecoverySettingTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolTypeDef(_ClientCreateUserPoolResponseUserPoolTypeDef):
    """
    - **UserPool** *(dict) --*

      A container for the user pool details.
      - **Id** *(string) --*

        The ID of the user pool.
    """


_ClientCreateUserPoolResponseTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseTypeDef",
    {"UserPool": ClientCreateUserPoolResponseUserPoolTypeDef},
    total=False,
)


class ClientCreateUserPoolResponseTypeDef(_ClientCreateUserPoolResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server for the request to create a user pool.
      - **UserPool** *(dict) --*

        A container for the user pool details.
        - **Id** *(string) --*

          The ID of the user pool.
    """


_ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef = TypedDict(
    "_ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef(
    _ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef
):
    pass


_ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef = TypedDict(
    "_ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)


class ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef(
    _ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef
):
    pass


_ClientCreateUserPoolSchemaTypeDef = TypedDict(
    "_ClientCreateUserPoolSchemaTypeDef",
    {
        "Name": str,
        "AttributeDataType": Literal["String", "Number", "DateTime", "Boolean"],
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolSchemaTypeDef(_ClientCreateUserPoolSchemaTypeDef):
    """
    - *(dict) --*

      Contains information about the schema attribute.
      - **Name** *(string) --*

        A schema attribute of the name type.
    """


_RequiredClientCreateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateUserPoolSmsConfigurationTypeDef", {"SnsCallerArn": str}
)
_OptionalClientCreateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateUserPoolSmsConfigurationTypeDef", {"ExternalId": str}, total=False
)


class ClientCreateUserPoolSmsConfigurationTypeDef(
    _RequiredClientCreateUserPoolSmsConfigurationTypeDef,
    _OptionalClientCreateUserPoolSmsConfigurationTypeDef,
):
    """
    The SMS configuration.
    - **SnsCallerArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is
      the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.
    """


_ClientCreateUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "_ClientCreateUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": Literal["OFF", "AUDIT", "ENFORCED"]},
)


class ClientCreateUserPoolUserPoolAddOnsTypeDef(_ClientCreateUserPoolUserPoolAddOnsTypeDef):
    """
    Used to enable advanced security risk detection. Set the key ``AdvancedSecurityMode`` to the
    value "AUDIT".
    - **AdvancedSecurityMode** *(string) --***[REQUIRED]**

      The advanced security mode.
    """


_ClientCreateUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "_ClientCreateUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": Literal["CONFIRM_WITH_LINK", "CONFIRM_WITH_CODE"],
    },
    total=False,
)


class ClientCreateUserPoolVerificationMessageTemplateTypeDef(
    _ClientCreateUserPoolVerificationMessageTemplateTypeDef
):
    """
    The template for the verification message that the user sees when the app requests permission to
    access the user's information.
    - **SmsMessage** *(string) --*

      The SMS message template.
    """


_ClientDescribeIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "_ClientDescribeIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientDescribeIdentityProviderResponseIdentityProviderTypeDef(
    _ClientDescribeIdentityProviderResponseIdentityProviderTypeDef
):
    """
    - **IdentityProvider** *(dict) --*

      The identity provider that was deleted.
      - **UserPoolId** *(string) --*

        The user pool ID.
    """


_ClientDescribeIdentityProviderResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientDescribeIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)


class ClientDescribeIdentityProviderResponseTypeDef(_ClientDescribeIdentityProviderResponseTypeDef):
    """
    - *(dict) --*

      - **IdentityProvider** *(dict) --*

        The identity provider that was deleted.
        - **UserPoolId** *(string) --*

          The user pool ID.
    """


_ClientDescribeResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "_ClientDescribeResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ClientDescribeResourceServerResponseResourceServerScopesTypeDef(
    _ClientDescribeResourceServerResponseResourceServerScopesTypeDef
):
    pass


_ClientDescribeResourceServerResponseResourceServerTypeDef = TypedDict(
    "_ClientDescribeResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientDescribeResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)


class ClientDescribeResourceServerResponseResourceServerTypeDef(
    _ClientDescribeResourceServerResponseResourceServerTypeDef
):
    """
    - **ResourceServer** *(dict) --*

      The resource server.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that hosts the resource server.
    """


_ClientDescribeResourceServerResponseTypeDef = TypedDict(
    "_ClientDescribeResourceServerResponseTypeDef",
    {"ResourceServer": ClientDescribeResourceServerResponseResourceServerTypeDef},
    total=False,
)


class ClientDescribeResourceServerResponseTypeDef(_ClientDescribeResourceServerResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceServer** *(dict) --*

        The resource server.
        - **UserPoolId** *(string) --*

          The user pool ID for the user pool that hosts the resource server.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "SourceArn": str,
        "BlockEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
        "Actions": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": Literal["BLOCK", "NO_ACTION"]},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "EventFilter": List[Literal["SIGN_IN", "PASSWORD_CHANGE", "SIGN_UP"]],
        "Actions": ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef
):
    pass


_ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
        "AccountTakeoverRiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
        "RiskExceptionConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef
):
    """
    - **RiskConfiguration** *(dict) --*

      The risk configuration.
      - **UserPoolId** *(string) --*

        The user pool ID.
    """


_ClientDescribeRiskConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseTypeDef",
    {"RiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef},
    total=False,
)


class ClientDescribeRiskConfigurationResponseTypeDef(
    _ClientDescribeRiskConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **RiskConfiguration** *(dict) --*

        The risk configuration.
        - **UserPoolId** *(string) --*

          The user pool ID.
    """


_ClientDescribeUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "_ClientDescribeUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientDescribeUserImportJobResponseUserImportJobTypeDef(
    _ClientDescribeUserImportJobResponseUserImportJobTypeDef
):
    """
    - **UserImportJob** *(dict) --*

      The job object that represents the user import job.
      - **JobName** *(string) --*

        The job name for the user import job.
    """


_ClientDescribeUserImportJobResponseTypeDef = TypedDict(
    "_ClientDescribeUserImportJobResponseTypeDef",
    {"UserImportJob": ClientDescribeUserImportJobResponseUserImportJobTypeDef},
    total=False,
)


class ClientDescribeUserImportJobResponseTypeDef(_ClientDescribeUserImportJobResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to the request to describe the user import job.
      - **UserImportJob** *(dict) --*

        The job object that represents the user import job.
        - **JobName** *(string) --*

          The job name for the user import job.
    """


_ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef(
    _ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef
):
    pass


_ClientDescribeUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "_ClientDescribeUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[
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
        ],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[Literal["code", "implicit", "client_credentials"]],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": Literal["LEGACY", "ENABLED"],
    },
    total=False,
)


class ClientDescribeUserPoolClientResponseUserPoolClientTypeDef(
    _ClientDescribeUserPoolClientResponseUserPoolClientTypeDef
):
    """
    - **UserPoolClient** *(dict) --*

      The user pool client from a server response to describe the user pool client.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool client.
    """


_ClientDescribeUserPoolClientResponseTypeDef = TypedDict(
    "_ClientDescribeUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientDescribeUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)


class ClientDescribeUserPoolClientResponseTypeDef(_ClientDescribeUserPoolClientResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server from a request to describe the user pool client.
      - **UserPoolClient** *(dict) --*

        The user pool client from a server response to describe the user pool client.
        - **UserPoolId** *(string) --*

          The user pool ID for the user pool client.
    """


_ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef = TypedDict(
    "_ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef",
    {"CertificateArn": str},
    total=False,
)


class ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef(
    _ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef
):
    pass


_ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef = TypedDict(
    "_ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef",
    {
        "UserPoolId": str,
        "AWSAccountId": str,
        "Domain": str,
        "S3Bucket": str,
        "CloudFrontDistribution": str,
        "Version": str,
        "Status": Literal["CREATING", "DELETING", "UPDATING", "ACTIVE", "FAILED"],
        "CustomDomainConfig": ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef,
    },
    total=False,
)


class ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef(
    _ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef
):
    """
    - **DomainDescription** *(dict) --*

      A domain description object containing information about the domain.
      - **UserPoolId** *(string) --*

        The user pool ID.
    """


_ClientDescribeUserPoolDomainResponseTypeDef = TypedDict(
    "_ClientDescribeUserPoolDomainResponseTypeDef",
    {"DomainDescription": ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef},
    total=False,
)


class ClientDescribeUserPoolDomainResponseTypeDef(_ClientDescribeUserPoolDomainResponseTypeDef):
    """
    - *(dict) --*

      - **DomainDescription** *(dict) --*

        A domain description object containing information about the domain.
        - **UserPoolId** *(string) --*

          The user pool ID.
    """


_ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Priority": int, "Name": Literal["verified_email", "verified_phone_number", "admin_only"]},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef(
    _ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef",
    {
        "RecoveryMechanisms": List[
            ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef(
    _ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef(
    _ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef(
    _ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef(
    _ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": Literal["COGNITO_DEFAULT", "DEVELOPER"],
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef(
    _ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef(
    _ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef(
    _ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef(
    _ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef(
    _ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef(
    _ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": Literal["String", "Number", "DateTime", "Boolean"],
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef(
    _ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef(
    _ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": Literal["OFF", "AUDIT", "ENFORCED"]},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef(
    _ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": Literal["CONFIRM_WITH_LINK", "CONFIRM_WITH_CODE"],
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef(
    _ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef
):
    pass


_ClientDescribeUserPoolResponseUserPoolTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef,
        "LambdaConfig": ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List[ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef],
        "AutoVerifiedAttributes": List[Literal["phone_number", "email"]],
        "AliasAttributes": List[Literal["phone_number", "email", "preferred_username"]],
        "UsernameAttributes": List[Literal["phone_number", "email"]],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef,
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": Literal["OFF", "ON", "OPTIONAL"],
        "DeviceConfiguration": ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef,
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef,
        "SmsConfiguration": ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef,
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef,
        "UserPoolAddOns": ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef,
        "Arn": str,
        "AccountRecoverySetting": ClientDescribeUserPoolResponseUserPoolAccountRecoverySettingTypeDef,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolTypeDef(_ClientDescribeUserPoolResponseUserPoolTypeDef):
    """
    - **UserPool** *(dict) --*

      The container of metadata returned by the server to describe the pool.
      - **Id** *(string) --*

        The ID of the user pool.
    """


_ClientDescribeUserPoolResponseTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseTypeDef",
    {"UserPool": ClientDescribeUserPoolResponseUserPoolTypeDef},
    total=False,
)


class ClientDescribeUserPoolResponseTypeDef(_ClientDescribeUserPoolResponseTypeDef):
    """
    - *(dict) --*

      Represents the response to describe the user pool.
      - **UserPool** *(dict) --*

        The container of metadata returned by the server to describe the pool.
        - **Id** *(string) --*

          The ID of the user pool.
    """


_ClientForgotPasswordAnalyticsMetadataTypeDef = TypedDict(
    "_ClientForgotPasswordAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)


class ClientForgotPasswordAnalyticsMetadataTypeDef(_ClientForgotPasswordAnalyticsMetadataTypeDef):
    """
    The Amazon Pinpoint analytics metadata for collecting metrics for ``ForgotPassword`` calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "_ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef(
    _ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef
):
    """
    - **CodeDeliveryDetails** *(dict) --*

      The code delivery details returned by the server in response to the request to reset a
      password.
      - **Destination** *(string) --*

        The destination for the code delivery details.
    """


_ClientForgotPasswordResponseTypeDef = TypedDict(
    "_ClientForgotPasswordResponseTypeDef",
    {"CodeDeliveryDetails": ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef},
    total=False,
)


class ClientForgotPasswordResponseTypeDef(_ClientForgotPasswordResponseTypeDef):
    """
    - *(dict) --*

      Respresents the response from the server regarding the request to reset a password.
      - **CodeDeliveryDetails** *(dict) --*

        The code delivery details returned by the server in response to the request to reset a
        password.
        - **Destination** *(string) --*

          The destination for the code delivery details.
    """


_ClientForgotPasswordUserContextDataTypeDef = TypedDict(
    "_ClientForgotPasswordUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientForgotPasswordUserContextDataTypeDef(_ClientForgotPasswordUserContextDataTypeDef):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientGetCsvHeaderResponseTypeDef = TypedDict(
    "_ClientGetCsvHeaderResponseTypeDef", {"UserPoolId": str, "CSVHeader": List[str]}, total=False
)


class ClientGetCsvHeaderResponseTypeDef(_ClientGetCsvHeaderResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to the request to get the header information for the
      .csv file for the user import job.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that the users are to be imported into.
    """


_ClientGetDeviceResponseDeviceDeviceAttributesTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetDeviceResponseDeviceDeviceAttributesTypeDef(
    _ClientGetDeviceResponseDeviceDeviceAttributesTypeDef
):
    pass


_ClientGetDeviceResponseDeviceTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientGetDeviceResponseDeviceDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)


class ClientGetDeviceResponseDeviceTypeDef(_ClientGetDeviceResponseDeviceTypeDef):
    """
    - **Device** *(dict) --*

      The device.
      - **DeviceKey** *(string) --*

        The device key.
    """


_ClientGetDeviceResponseTypeDef = TypedDict(
    "_ClientGetDeviceResponseTypeDef", {"Device": ClientGetDeviceResponseDeviceTypeDef}, total=False
)


class ClientGetDeviceResponseTypeDef(_ClientGetDeviceResponseTypeDef):
    """
    - *(dict) --*

      Gets the device response.
      - **Device** *(dict) --*

        The device.
        - **DeviceKey** *(string) --*

          The device key.
    """


_ClientGetGroupResponseGroupTypeDef = TypedDict(
    "_ClientGetGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetGroupResponseGroupTypeDef(_ClientGetGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The group object for the group.
      - **GroupName** *(string) --*

        The name of the group.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef", {"Group": ClientGetGroupResponseGroupTypeDef}, total=False
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The group object for the group.
        - **GroupName** *(string) --*

          The name of the group.
    """


_ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef = TypedDict(
    "_ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef(
    _ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef
):
    """
    - **IdentityProvider** *(dict) --*

      The identity provider object.
      - **UserPoolId** *(string) --*

        The user pool ID.
    """


_ClientGetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "_ClientGetIdentityProviderByIdentifierResponseTypeDef",
    {"IdentityProvider": ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef},
    total=False,
)


class ClientGetIdentityProviderByIdentifierResponseTypeDef(
    _ClientGetIdentityProviderByIdentifierResponseTypeDef
):
    """
    - *(dict) --*

      - **IdentityProvider** *(dict) --*

        The identity provider object.
        - **UserPoolId** *(string) --*

          The user pool ID.
    """


_ClientGetSigningCertificateResponseTypeDef = TypedDict(
    "_ClientGetSigningCertificateResponseTypeDef", {"Certificate": str}, total=False
)


class ClientGetSigningCertificateResponseTypeDef(_ClientGetSigningCertificateResponseTypeDef):
    """
    - *(dict) --*

      Response from Cognito for a signing certificate request.
      - **Certificate** *(string) --*

        The signing certificate.
    """


_ClientGetUiCustomizationResponseUICustomizationTypeDef = TypedDict(
    "_ClientGetUiCustomizationResponseUICustomizationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetUiCustomizationResponseUICustomizationTypeDef(
    _ClientGetUiCustomizationResponseUICustomizationTypeDef
):
    """
    - **UICustomization** *(dict) --*

      The UI customization information.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool.
    """


_ClientGetUiCustomizationResponseTypeDef = TypedDict(
    "_ClientGetUiCustomizationResponseTypeDef",
    {"UICustomization": ClientGetUiCustomizationResponseUICustomizationTypeDef},
    total=False,
)


class ClientGetUiCustomizationResponseTypeDef(_ClientGetUiCustomizationResponseTypeDef):
    """
    - *(dict) --*

      - **UICustomization** *(dict) --*

        The UI customization information.
        - **UserPoolId** *(string) --*

          The user pool ID for the user pool.
    """


_ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "_ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef(
    _ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef
):
    """
    - **CodeDeliveryDetails** *(dict) --*

      The code delivery details returned by the server in response to the request to get the user
      attribute verification code.
      - **Destination** *(string) --*

        The destination for the code delivery details.
    """


_ClientGetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "_ClientGetUserAttributeVerificationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef
    },
    total=False,
)


class ClientGetUserAttributeVerificationCodeResponseTypeDef(
    _ClientGetUserAttributeVerificationCodeResponseTypeDef
):
    """
    - *(dict) --*

      The verification code response returned by the server response to get the user attribute
      verification code.
      - **CodeDeliveryDetails** *(dict) --*

        The code delivery details returned by the server in response to the request to get the user
        attribute verification code.
        - **Destination** *(string) --*

          The destination for the code delivery details.
    """


_ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "_ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef(
    _ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef
):
    pass


_ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef = TypedDict(
    "_ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)


class ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef(
    _ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef
):
    """
    - **SmsMfaConfiguration** *(dict) --*

      The SMS text message multi-factor (MFA) configuration.
      - **SmsAuthenticationMessage** *(string) --*

        The SMS authentication message that will be sent to users with the code they need to sign
        in. The message must contain the ‘{####}’ placeholder, which will be replaced with the code.
        If the message is not included, and default message will be used.
    """


_ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "_ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef(
    _ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef
):
    pass


_ClientGetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "_ClientGetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef,
        "SoftwareTokenMfaConfiguration": ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef,
        "MfaConfiguration": Literal["OFF", "ON", "OPTIONAL"],
    },
    total=False,
)


class ClientGetUserPoolMfaConfigResponseTypeDef(_ClientGetUserPoolMfaConfigResponseTypeDef):
    """
    - *(dict) --*

      - **SmsMfaConfiguration** *(dict) --*

        The SMS text message multi-factor (MFA) configuration.
        - **SmsAuthenticationMessage** *(string) --*

          The SMS authentication message that will be sent to users with the code they need to sign
          in. The message must contain the ‘{####}’ placeholder, which will be replaced with the
          code. If the message is not included, and default message will be used.
    """


_ClientGetUserResponseMFAOptionsTypeDef = TypedDict(
    "_ClientGetUserResponseMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientGetUserResponseMFAOptionsTypeDef(_ClientGetUserResponseMFAOptionsTypeDef):
    pass


_ClientGetUserResponseUserAttributesTypeDef = TypedDict(
    "_ClientGetUserResponseUserAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientGetUserResponseUserAttributesTypeDef(_ClientGetUserResponseUserAttributesTypeDef):
    pass


_ClientGetUserResponseTypeDef = TypedDict(
    "_ClientGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[ClientGetUserResponseUserAttributesTypeDef],
        "MFAOptions": List[ClientGetUserResponseMFAOptionsTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)


class ClientGetUserResponseTypeDef(_ClientGetUserResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server from the request to get information about the user.
      - **Username** *(string) --*

        The user name of the user you wish to retrieve from the get user request.
    """


_ClientInitiateAuthAnalyticsMetadataTypeDef = TypedDict(
    "_ClientInitiateAuthAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)


class ClientInitiateAuthAnalyticsMetadataTypeDef(_ClientInitiateAuthAnalyticsMetadataTypeDef):
    """
    The Amazon Pinpoint analytics metadata for collecting metrics for ``InitiateAuth`` calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "_ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)


class ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef(
    _ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef
):
    pass


_ClientInitiateAuthResponseAuthenticationResultTypeDef = TypedDict(
    "_ClientInitiateAuthResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)


class ClientInitiateAuthResponseAuthenticationResultTypeDef(
    _ClientInitiateAuthResponseAuthenticationResultTypeDef
):
    pass


_ClientInitiateAuthResponseTypeDef = TypedDict(
    "_ClientInitiateAuthResponseTypeDef",
    {
        "ChallengeName": Literal[
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
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientInitiateAuthResponseAuthenticationResultTypeDef,
    },
    total=False,
)


class ClientInitiateAuthResponseTypeDef(_ClientInitiateAuthResponseTypeDef):
    """
    - *(dict) --*

      Initiates the authentication response.
      - **ChallengeName** *(string) --*

        The name of the challenge which you are responding to with this call. This is returned to
        you in the ``AdminInitiateAuth`` response if you need to pass another challenge.
        Valid values include the following. Note that all of these challenges require ``USERNAME``
        and ``SECRET_HASH`` (if applicable) in the parameters.
        * ``SMS_MFA`` : Next challenge is to supply an ``SMS_MFA_CODE`` , delivered via SMS.
        * ``PASSWORD_VERIFIER`` : Next challenge is to supply ``PASSWORD_CLAIM_SIGNATURE`` ,
        ``PASSWORD_CLAIM_SECRET_BLOCK`` , and ``TIMESTAMP`` after the client-side SRP calculations.
        * ``CUSTOM_CHALLENGE`` : This is returned if your custom authentication flow determines that
        the user should pass another challenge before tokens are issued.
        * ``DEVICE_SRP_AUTH`` : If device tracking was enabled on your user pool and the previous
        challenges were passed, this challenge is returned so that Amazon Cognito can start tracking
        this device.
        * ``DEVICE_PASSWORD_VERIFIER`` : Similar to ``PASSWORD_VERIFIER`` , but for devices only.
        * ``NEW_PASSWORD_REQUIRED`` : For users which are required to change their passwords after
        successful first login. This challenge should be passed with ``NEW_PASSWORD`` and any other
        required attributes.
    """


_ClientInitiateAuthUserContextDataTypeDef = TypedDict(
    "_ClientInitiateAuthUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientInitiateAuthUserContextDataTypeDef(_ClientInitiateAuthUserContextDataTypeDef):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientListDevicesResponseDevicesDeviceAttributesTypeDef = TypedDict(
    "_ClientListDevicesResponseDevicesDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListDevicesResponseDevicesDeviceAttributesTypeDef(
    _ClientListDevicesResponseDevicesDeviceAttributesTypeDef
):
    pass


_ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientListDevicesResponseDevicesTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientListDevicesResponseDevicesDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)


class ClientListDevicesResponseDevicesTypeDef(_ClientListDevicesResponseDevicesTypeDef):
    """
    - *(dict) --*

      The device type.
      - **DeviceKey** *(string) --*

        The device key.
    """


_ClientListDevicesResponseTypeDef = TypedDict(
    "_ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "PaginationToken": str},
    total=False,
)


class ClientListDevicesResponseTypeDef(_ClientListDevicesResponseTypeDef):
    """
    - *(dict) --*

      Represents the response to list devices.
      - **Devices** *(list) --*

        The devices returned in the list devices response.
        - *(dict) --*

          The device type.
          - **DeviceKey** *(string) --*

            The device key.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    - *(dict) --*

      The group type.
      - **GroupName** *(string) --*

        The name of the group.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The group objects for the groups.
        - *(dict) --*

          The group type.
          - **GroupName** *(string) --*

            The name of the group.
    """


_ClientListIdentityProvidersResponseProvidersTypeDef = TypedDict(
    "_ClientListIdentityProvidersResponseProvidersTypeDef",
    {
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListIdentityProvidersResponseProvidersTypeDef(
    _ClientListIdentityProvidersResponseProvidersTypeDef
):
    """
    - *(dict) --*

      A container for identity provider details.
      - **ProviderName** *(string) --*

        The identity provider name.
    """


_ClientListIdentityProvidersResponseTypeDef = TypedDict(
    "_ClientListIdentityProvidersResponseTypeDef",
    {"Providers": List[ClientListIdentityProvidersResponseProvidersTypeDef], "NextToken": str},
    total=False,
)


class ClientListIdentityProvidersResponseTypeDef(_ClientListIdentityProvidersResponseTypeDef):
    """
    - *(dict) --*

      - **Providers** *(list) --*

        A list of identity provider objects.
        - *(dict) --*

          A container for identity provider details.
          - **ProviderName** *(string) --*

            The identity provider name.
    """


_ClientListResourceServersResponseResourceServersScopesTypeDef = TypedDict(
    "_ClientListResourceServersResponseResourceServersScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ClientListResourceServersResponseResourceServersScopesTypeDef(
    _ClientListResourceServersResponseResourceServersScopesTypeDef
):
    pass


_ClientListResourceServersResponseResourceServersTypeDef = TypedDict(
    "_ClientListResourceServersResponseResourceServersTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientListResourceServersResponseResourceServersScopesTypeDef],
    },
    total=False,
)


class ClientListResourceServersResponseResourceServersTypeDef(
    _ClientListResourceServersResponseResourceServersTypeDef
):
    """
    - *(dict) --*

      A container for information about a resource server for a user pool.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that hosts the resource server.
    """


_ClientListResourceServersResponseTypeDef = TypedDict(
    "_ClientListResourceServersResponseTypeDef",
    {
        "ResourceServers": List[ClientListResourceServersResponseResourceServersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceServersResponseTypeDef(_ClientListResourceServersResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceServers** *(list) --*

        The resource servers.
        - *(dict) --*

          A container for information about a resource server for a user pool.
          - **UserPoolId** *(string) --*

            The user pool ID for the user pool that hosts the resource server.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The tags that are assigned to the user pool.
        - *(string) --*

          - *(string) --*
    """


_ClientListUserImportJobsResponseUserImportJobsTypeDef = TypedDict(
    "_ClientListUserImportJobsResponseUserImportJobsTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientListUserImportJobsResponseUserImportJobsTypeDef(
    _ClientListUserImportJobsResponseUserImportJobsTypeDef
):
    """
    - *(dict) --*

      The user import job type.
      - **JobName** *(string) --*

        The job name for the user import job.
    """


_ClientListUserImportJobsResponseTypeDef = TypedDict(
    "_ClientListUserImportJobsResponseTypeDef",
    {
        "UserImportJobs": List[ClientListUserImportJobsResponseUserImportJobsTypeDef],
        "PaginationToken": str,
    },
    total=False,
)


class ClientListUserImportJobsResponseTypeDef(_ClientListUserImportJobsResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to the request to list the user import jobs.
      - **UserImportJobs** *(list) --*

        The user import jobs.
        - *(dict) --*

          The user import job type.
          - **JobName** *(string) --*

            The job name for the user import job.
    """


_ClientListUserPoolClientsResponseUserPoolClientsTypeDef = TypedDict(
    "_ClientListUserPoolClientsResponseUserPoolClientsTypeDef",
    {"ClientId": str, "UserPoolId": str, "ClientName": str},
    total=False,
)


class ClientListUserPoolClientsResponseUserPoolClientsTypeDef(
    _ClientListUserPoolClientsResponseUserPoolClientsTypeDef
):
    """
    - *(dict) --*

      The description of the user pool client.
      - **ClientId** *(string) --*

        The ID of the client associated with the user pool.
    """


_ClientListUserPoolClientsResponseTypeDef = TypedDict(
    "_ClientListUserPoolClientsResponseTypeDef",
    {
        "UserPoolClients": List[ClientListUserPoolClientsResponseUserPoolClientsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListUserPoolClientsResponseTypeDef(_ClientListUserPoolClientsResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server that lists user pool clients.
      - **UserPoolClients** *(list) --*

        The user pool clients in the response that lists user pool clients.
        - *(dict) --*

          The description of the user pool client.
          - **ClientId** *(string) --*

            The ID of the client associated with the user pool.
    """


_ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef = TypedDict(
    "_ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef(
    _ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef
):
    pass


_ClientListUserPoolsResponseUserPoolsTypeDef = TypedDict(
    "_ClientListUserPoolsResponseUserPoolsTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListUserPoolsResponseUserPoolsTypeDef(_ClientListUserPoolsResponseUserPoolsTypeDef):
    """
    - *(dict) --*

      A user pool description.
      - **Id** *(string) --*

        The ID in a user pool description.
    """


_ClientListUserPoolsResponseTypeDef = TypedDict(
    "_ClientListUserPoolsResponseTypeDef",
    {"UserPools": List[ClientListUserPoolsResponseUserPoolsTypeDef], "NextToken": str},
    total=False,
)


class ClientListUserPoolsResponseTypeDef(_ClientListUserPoolsResponseTypeDef):
    """
    - *(dict) --*

      Represents the response to list user pools.
      - **UserPools** *(list) --*

        The user pools from the response to list users.
        - *(dict) --*

          A user pool description.
          - **Id** *(string) --*

            The ID in a user pool description.
    """


_ClientListUsersInGroupResponseUsersAttributesTypeDef = TypedDict(
    "_ClientListUsersInGroupResponseUsersAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListUsersInGroupResponseUsersAttributesTypeDef(
    _ClientListUsersInGroupResponseUsersAttributesTypeDef
):
    pass


_ClientListUsersInGroupResponseUsersMFAOptionsTypeDef = TypedDict(
    "_ClientListUsersInGroupResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientListUsersInGroupResponseUsersMFAOptionsTypeDef(
    _ClientListUsersInGroupResponseUsersMFAOptionsTypeDef
):
    pass


_ClientListUsersInGroupResponseUsersTypeDef = TypedDict(
    "_ClientListUsersInGroupResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientListUsersInGroupResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ClientListUsersInGroupResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)


class ClientListUsersInGroupResponseUsersTypeDef(_ClientListUsersInGroupResponseUsersTypeDef):
    """
    - *(dict) --*

      The user type.
      - **Username** *(string) --*

        The user name of the user you wish to describe.
    """


_ClientListUsersInGroupResponseTypeDef = TypedDict(
    "_ClientListUsersInGroupResponseTypeDef",
    {"Users": List[ClientListUsersInGroupResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ClientListUsersInGroupResponseTypeDef(_ClientListUsersInGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        The users returned in the request to list users.
        - *(dict) --*

          The user type.
          - **Username** *(string) --*

            The user name of the user you wish to describe.
    """


_ClientListUsersResponseUsersAttributesTypeDef = TypedDict(
    "_ClientListUsersResponseUsersAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientListUsersResponseUsersAttributesTypeDef(_ClientListUsersResponseUsersAttributesTypeDef):
    pass


_ClientListUsersResponseUsersMFAOptionsTypeDef = TypedDict(
    "_ClientListUsersResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientListUsersResponseUsersMFAOptionsTypeDef(_ClientListUsersResponseUsersMFAOptionsTypeDef):
    pass


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientListUsersResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ClientListUsersResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    - *(dict) --*

      The user type.
      - **Username** *(string) --*

        The user name of the user you wish to describe.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "PaginationToken": str},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    - *(dict) --*

      The response from the request to list users.
      - **Users** *(list) --*

        The users returned in the request to list users.
        - *(dict) --*

          The user type.
          - **Username** *(string) --*

            The user name of the user you wish to describe.
    """


_ClientResendConfirmationCodeAnalyticsMetadataTypeDef = TypedDict(
    "_ClientResendConfirmationCodeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientResendConfirmationCodeAnalyticsMetadataTypeDef(
    _ClientResendConfirmationCodeAnalyticsMetadataTypeDef
):
    """
    The Amazon Pinpoint analytics metadata for collecting metrics for ``ResendConfirmationCode``
    calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "_ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef(
    _ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef
):
    """
    - **CodeDeliveryDetails** *(dict) --*

      The code delivery details returned by the server in response to the request to resend the
      confirmation code.
      - **Destination** *(string) --*

        The destination for the code delivery details.
    """


_ClientResendConfirmationCodeResponseTypeDef = TypedDict(
    "_ClientResendConfirmationCodeResponseTypeDef",
    {"CodeDeliveryDetails": ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef},
    total=False,
)


class ClientResendConfirmationCodeResponseTypeDef(_ClientResendConfirmationCodeResponseTypeDef):
    """
    - *(dict) --*

      The response from the server when the Amazon Cognito Your User Pools service makes the request
      to resend a confirmation code.
      - **CodeDeliveryDetails** *(dict) --*

        The code delivery details returned by the server in response to the request to resend the
        confirmation code.
        - **Destination** *(string) --*

          The destination for the code delivery details.
    """


_ClientResendConfirmationCodeUserContextDataTypeDef = TypedDict(
    "_ClientResendConfirmationCodeUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientResendConfirmationCodeUserContextDataTypeDef(
    _ClientResendConfirmationCodeUserContextDataTypeDef
):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientRespondToAuthChallengeAnalyticsMetadataTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientRespondToAuthChallengeAnalyticsMetadataTypeDef(
    _ClientRespondToAuthChallengeAnalyticsMetadataTypeDef
):
    """
    The Amazon Pinpoint analytics metadata for collecting metrics for ``RespondToAuthChallenge``
    calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)


class ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef(
    _ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef
):
    pass


_ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)


class ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef(
    _ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef
):
    pass


_ClientRespondToAuthChallengeResponseTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": Literal[
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
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef,
    },
    total=False,
)


class ClientRespondToAuthChallengeResponseTypeDef(_ClientRespondToAuthChallengeResponseTypeDef):
    """
    - *(dict) --*

      The response to respond to the authentication challenge.
      - **ChallengeName** *(string) --*

        The challenge name. For more information, see .
    """


_ClientRespondToAuthChallengeUserContextDataTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientRespondToAuthChallengeUserContextDataTypeDef(
    _ClientRespondToAuthChallengeUserContextDataTypeDef
):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef
):
    pass


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef
):
    pass


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef
):
    pass


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef
):
    pass


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef
):
    pass


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef
):
    pass


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef
):
    pass


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "SourceArn": str,
        "BlockEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef
):
    """
    - **NotifyConfiguration** *(dict) --*

      The notify configuration used to construct email notifications.
      - **From** *(string) --*

        The email address that is sending the email. It must be either individually verified with
        Amazon SES, or from a domain that has been verified with Amazon SES.
    """


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
        "Actions": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef
):
    """
    The account takeover risk configuration.
    - **NotifyConfiguration** *(dict) --*

      The notify configuration used to construct email notifications.
      - **From** *(string) --*

        The email address that is sending the email. It must be either individually verified with
        Amazon SES, or from a domain that has been verified with Amazon SES.
    """


_ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": Literal["BLOCK", "NO_ACTION"]},
    total=False,
)


class ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef(
    _ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef
):
    pass


_ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "EventFilter": List[Literal["SIGN_IN", "PASSWORD_CHANGE", "SIGN_UP"]],
        "Actions": ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef(
    _ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef
):
    """
    The compromised credentials risk configuration.
    - **EventFilter** *(list) --*

      Perform the action for these events. The default is to perform all events if no event filter
      is specified.
      - *(string) --*
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {
        "Notify": bool,
        "EventAction": Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"],
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "SourceArn": str,
        "BlockEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
        "Actions": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": Literal["BLOCK", "NO_ACTION"]},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "EventFilter": List[Literal["SIGN_IN", "PASSWORD_CHANGE", "SIGN_UP"]],
        "Actions": ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef
):
    pass


_ClientSetRiskConfigurationResponseRiskConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
        "AccountTakeoverRiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
        "RiskExceptionConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationTypeDef
):
    """
    - **RiskConfiguration** *(dict) --*

      The risk configuration.
      - **UserPoolId** *(string) --*

        The user pool ID.
    """


_ClientSetRiskConfigurationResponseTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseTypeDef",
    {"RiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationTypeDef},
    total=False,
)


class ClientSetRiskConfigurationResponseTypeDef(_ClientSetRiskConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **RiskConfiguration** *(dict) --*

        The risk configuration.
        - **UserPoolId** *(string) --*

          The user pool ID.
    """


_ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)


class ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef(
    _ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef
):
    """
    The configuration to override the risk decision.
    - **BlockedIPRangeList** *(list) --*

      Overrides the risk decision to always block the pre-authentication requests. The IP range is
      in CIDR notation: a compact representation of an IP address and its associated routing prefix.
      - *(string) --*
    """


_ClientSetUiCustomizationResponseUICustomizationTypeDef = TypedDict(
    "_ClientSetUiCustomizationResponseUICustomizationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientSetUiCustomizationResponseUICustomizationTypeDef(
    _ClientSetUiCustomizationResponseUICustomizationTypeDef
):
    """
    - **UICustomization** *(dict) --*

      The UI customization information.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool.
    """


_ClientSetUiCustomizationResponseTypeDef = TypedDict(
    "_ClientSetUiCustomizationResponseTypeDef",
    {"UICustomization": ClientSetUiCustomizationResponseUICustomizationTypeDef},
    total=False,
)


class ClientSetUiCustomizationResponseTypeDef(_ClientSetUiCustomizationResponseTypeDef):
    """
    - *(dict) --*

      - **UICustomization** *(dict) --*

        The UI customization information.
        - **UserPoolId** *(string) --*

          The user pool ID for the user pool.
    """


_ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef = TypedDict(
    "_ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)


class ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef(
    _ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef
):
    """
    The SMS text message multi-factor authentication (MFA) settings.
    - **Enabled** *(boolean) --*

      Specifies whether SMS text message MFA is enabled.
    """


_ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef = TypedDict(
    "_ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)


class ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef(
    _ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef
):
    """
    The time-based one-time password software token MFA settings.
    - **Enabled** *(boolean) --*

      Specifies whether software token MFA is enabled.
    """


_ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef
):
    pass


_ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)


class ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef
):
    """
    - **SmsMfaConfiguration** *(dict) --*

      The SMS text message MFA configuration.
      - **SmsAuthenticationMessage** *(string) --*

        The SMS authentication message that will be sent to users with the code they need to sign
        in. The message must contain the ‘{####}’ placeholder, which will be replaced with the code.
        If the message is not included, and default message will be used.
    """


_ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef
):
    pass


_ClientSetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef,
        "SoftwareTokenMfaConfiguration": ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef,
        "MfaConfiguration": Literal["OFF", "ON", "OPTIONAL"],
    },
    total=False,
)


class ClientSetUserPoolMfaConfigResponseTypeDef(_ClientSetUserPoolMfaConfigResponseTypeDef):
    """
    - *(dict) --*

      - **SmsMfaConfiguration** *(dict) --*

        The SMS text message MFA configuration.
        - **SmsAuthenticationMessage** *(string) --*

          The SMS authentication message that will be sent to users with the code they need to sign
          in. The message must contain the ‘{####}’ placeholder, which will be replaced with the
          code. If the message is not included, and default message will be used.
    """


_ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef
):
    pass


_ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)


class ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef
):
    """
    The SMS text message MFA configuration.
    - **SmsAuthenticationMessage** *(string) --*

      The SMS authentication message that will be sent to users with the code they need to sign in.
      The message must contain the ‘{####}’ placeholder, which will be replaced with the code. If
      the message is not included, and default message will be used.
    """


_ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef
):
    """
    The software token MFA configuration.
    - **Enabled** *(boolean) --*

      Specifies whether software token MFA is enabled.
    """


_ClientSetUserSettingsMFAOptionsTypeDef = TypedDict(
    "_ClientSetUserSettingsMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientSetUserSettingsMFAOptionsTypeDef(_ClientSetUserSettingsMFAOptionsTypeDef):
    """
    - *(dict) --*

      *This data type is no longer supported.* You can use it only for SMS MFA configurations. You
      can't use it for TOTP software token MFA configurations.
      To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
      SetUserMFAPreference actions.
      To look up information about either type of MFA configuration, use the
      AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.
      - **DeliveryMedium** *(string) --*

        The delivery medium to send the MFA code. You can use this parameter to set only the ``SMS``
        delivery medium value.
    """


_ClientSignUpAnalyticsMetadataTypeDef = TypedDict(
    "_ClientSignUpAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)


class ClientSignUpAnalyticsMetadataTypeDef(_ClientSignUpAnalyticsMetadataTypeDef):
    """
    The Amazon Pinpoint analytics metadata for collecting metrics for ``SignUp`` calls.
    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientSignUpResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "_ClientSignUpResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientSignUpResponseCodeDeliveryDetailsTypeDef(
    _ClientSignUpResponseCodeDeliveryDetailsTypeDef
):
    pass


_ClientSignUpResponseTypeDef = TypedDict(
    "_ClientSignUpResponseTypeDef",
    {
        "UserConfirmed": bool,
        "CodeDeliveryDetails": ClientSignUpResponseCodeDeliveryDetailsTypeDef,
        "UserSub": str,
    },
    total=False,
)


class ClientSignUpResponseTypeDef(_ClientSignUpResponseTypeDef):
    """
    - *(dict) --*

      The response from the server for a registration request.
      - **UserConfirmed** *(boolean) --*

        A response from the server indicating that a user registration has been confirmed.
    """


_RequiredClientSignUpUserAttributesTypeDef = TypedDict(
    "_RequiredClientSignUpUserAttributesTypeDef", {"Name": str}
)
_OptionalClientSignUpUserAttributesTypeDef = TypedDict(
    "_OptionalClientSignUpUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientSignUpUserAttributesTypeDef(
    _RequiredClientSignUpUserAttributesTypeDef, _OptionalClientSignUpUserAttributesTypeDef
):
    """
    - *(dict) --*

      Specifies whether the attribute is standard or custom.
      - **Name** *(string) --***[REQUIRED]**

        The name of the attribute.
    """


_ClientSignUpUserContextDataTypeDef = TypedDict(
    "_ClientSignUpUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientSignUpUserContextDataTypeDef(_ClientSignUpUserContextDataTypeDef):
    """
    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_RequiredClientSignUpValidationDataTypeDef = TypedDict(
    "_RequiredClientSignUpValidationDataTypeDef", {"Name": str}
)
_OptionalClientSignUpValidationDataTypeDef = TypedDict(
    "_OptionalClientSignUpValidationDataTypeDef", {"Value": str}, total=False
)


class ClientSignUpValidationDataTypeDef(
    _RequiredClientSignUpValidationDataTypeDef, _OptionalClientSignUpValidationDataTypeDef
):
    """
    - *(dict) --*

      Specifies whether the attribute is standard or custom.
      - **Name** *(string) --***[REQUIRED]**

        The name of the attribute.
    """


_ClientStartUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "_ClientStartUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientStartUserImportJobResponseUserImportJobTypeDef(
    _ClientStartUserImportJobResponseUserImportJobTypeDef
):
    """
    - **UserImportJob** *(dict) --*

      The job object that represents the user import job.
      - **JobName** *(string) --*

        The job name for the user import job.
    """


_ClientStartUserImportJobResponseTypeDef = TypedDict(
    "_ClientStartUserImportJobResponseTypeDef",
    {"UserImportJob": ClientStartUserImportJobResponseUserImportJobTypeDef},
    total=False,
)


class ClientStartUserImportJobResponseTypeDef(_ClientStartUserImportJobResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to the request to start the user import job.
      - **UserImportJob** *(dict) --*

        The job object that represents the user import job.
        - **JobName** *(string) --*

          The job name for the user import job.
    """


_ClientStopUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "_ClientStopUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal[
            "Created",
            "Pending",
            "InProgress",
            "Stopping",
            "Expired",
            "Stopped",
            "Failed",
            "Succeeded",
        ],
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientStopUserImportJobResponseUserImportJobTypeDef(
    _ClientStopUserImportJobResponseUserImportJobTypeDef
):
    """
    - **UserImportJob** *(dict) --*

      The job object that represents the user import job.
      - **JobName** *(string) --*

        The job name for the user import job.
    """


_ClientStopUserImportJobResponseTypeDef = TypedDict(
    "_ClientStopUserImportJobResponseTypeDef",
    {"UserImportJob": ClientStopUserImportJobResponseUserImportJobTypeDef},
    total=False,
)


class ClientStopUserImportJobResponseTypeDef(_ClientStopUserImportJobResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to the request to stop the user import job.
      - **UserImportJob** *(dict) --*

        The job object that represents the user import job.
        - **JobName** *(string) --*

          The job name for the user import job.
    """


_ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "_ClientUpdateGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientUpdateGroupResponseGroupTypeDef(_ClientUpdateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The group object for the group.
      - **GroupName** *(string) --*

        The name of the group.
    """


_ClientUpdateGroupResponseTypeDef = TypedDict(
    "_ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)


class ClientUpdateGroupResponseTypeDef(_ClientUpdateGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The group object for the group.
        - **GroupName** *(string) --*

          The name of the group.
    """


_ClientUpdateIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "_ClientUpdateIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientUpdateIdentityProviderResponseIdentityProviderTypeDef(
    _ClientUpdateIdentityProviderResponseIdentityProviderTypeDef
):
    """
    - **IdentityProvider** *(dict) --*

      The identity provider object.
      - **UserPoolId** *(string) --*

        The user pool ID.
    """


_ClientUpdateIdentityProviderResponseTypeDef = TypedDict(
    "_ClientUpdateIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientUpdateIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)


class ClientUpdateIdentityProviderResponseTypeDef(_ClientUpdateIdentityProviderResponseTypeDef):
    """
    - *(dict) --*

      - **IdentityProvider** *(dict) --*

        The identity provider object.
        - **UserPoolId** *(string) --*

          The user pool ID.
    """


_ClientUpdateResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "_ClientUpdateResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ClientUpdateResourceServerResponseResourceServerScopesTypeDef(
    _ClientUpdateResourceServerResponseResourceServerScopesTypeDef
):
    pass


_ClientUpdateResourceServerResponseResourceServerTypeDef = TypedDict(
    "_ClientUpdateResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientUpdateResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)


class ClientUpdateResourceServerResponseResourceServerTypeDef(
    _ClientUpdateResourceServerResponseResourceServerTypeDef
):
    """
    - **ResourceServer** *(dict) --*

      The resource server.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that hosts the resource server.
    """


_ClientUpdateResourceServerResponseTypeDef = TypedDict(
    "_ClientUpdateResourceServerResponseTypeDef",
    {"ResourceServer": ClientUpdateResourceServerResponseResourceServerTypeDef},
    total=False,
)


class ClientUpdateResourceServerResponseTypeDef(_ClientUpdateResourceServerResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceServer** *(dict) --*

        The resource server.
        - **UserPoolId** *(string) --*

          The user pool ID for the user pool that hosts the resource server.
    """


_RequiredClientUpdateResourceServerScopesTypeDef = TypedDict(
    "_RequiredClientUpdateResourceServerScopesTypeDef", {"ScopeName": str}
)
_OptionalClientUpdateResourceServerScopesTypeDef = TypedDict(
    "_OptionalClientUpdateResourceServerScopesTypeDef", {"ScopeDescription": str}, total=False
)


class ClientUpdateResourceServerScopesTypeDef(
    _RequiredClientUpdateResourceServerScopesTypeDef,
    _OptionalClientUpdateResourceServerScopesTypeDef,
):
    """
    - *(dict) --*

      A resource server scope.
      - **ScopeName** *(string) --***[REQUIRED]**

        The name of the scope.
    """


_ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef = TypedDict(
    "_ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef",
    {"Destination": str, "DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef(
    _ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef
):
    """
    - *(dict) --*

      The code delivery details being returned from the server.
      - **Destination** *(string) --*

        The destination for the code delivery details.
    """


_ClientUpdateUserAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateUserAttributesResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List[
            ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef
        ]
    },
    total=False,
)


class ClientUpdateUserAttributesResponseTypeDef(_ClientUpdateUserAttributesResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server for the request to update user attributes.
      - **CodeDeliveryDetailsList** *(list) --*

        The code delivery details list from the server for the request to update user attributes.
        - *(dict) --*

          The code delivery details being returned from the server.
          - **Destination** *(string) --*

            The destination for the code delivery details.
    """


_RequiredClientUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_RequiredClientUpdateUserAttributesUserAttributesTypeDef", {"Name": str}
)
_OptionalClientUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_OptionalClientUpdateUserAttributesUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientUpdateUserAttributesUserAttributesTypeDef(
    _RequiredClientUpdateUserAttributesUserAttributesTypeDef,
    _OptionalClientUpdateUserAttributesUserAttributesTypeDef,
):
    """
    - *(dict) --*

      Specifies whether the attribute is standard or custom.
      - **Name** *(string) --***[REQUIRED]**

        The name of the attribute.
    """


_RequiredClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "_RequiredClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Priority": int},
)
_OptionalClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef = TypedDict(
    "_OptionalClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef",
    {"Name": Literal["verified_email", "verified_phone_number", "admin_only"]},
    total=False,
)


class ClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef(
    _RequiredClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef,
    _OptionalClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef,
):
    """
    - *(dict) --*

      A map containing a priority as a key, and recovery method name as a value.
      - **Priority** *(integer) --***[REQUIRED]**

        A positive integer specifying priority of a method with 1 being the highest priority.
    """


_ClientUpdateUserPoolAccountRecoverySettingTypeDef = TypedDict(
    "_ClientUpdateUserPoolAccountRecoverySettingTypeDef",
    {
        "RecoveryMechanisms": List[
            ClientUpdateUserPoolAccountRecoverySettingRecoveryMechanismsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateUserPoolAccountRecoverySettingTypeDef(
    _ClientUpdateUserPoolAccountRecoverySettingTypeDef
):
    """
    Use this setting to define which verified available method a user can use to recover their
    password when they call ``ForgotPassword`` . It allows you to define a preferred method when a
    user has more than one method available. With this setting, SMS does not qualify for a valid
    password recovery mechanism if the user also has SMS MFA enabled. In the absence of this
    setting, Cognito uses the legacy behavior to determine the recovery method where SMS is
    preferred over email.
    - **RecoveryMechanisms** *(list) --*

      The list of ``RecoveryOptionTypes`` .
      - *(dict) --*

        A map containing a priority as a key, and recovery method name as a value.
        - **Priority** *(integer) --***[REQUIRED]**

          A positive integer specifying priority of a method with 1 being the highest priority.
    """


_ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "_ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)


class ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef(
    _ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef
):
    pass


_ClientUpdateUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "_ClientUpdateUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)


class ClientUpdateUserPoolAdminCreateUserConfigTypeDef(
    _ClientUpdateUserPoolAdminCreateUserConfigTypeDef
):
    """
    The configuration for ``AdminCreateUser`` requests.
    - **AllowAdminCreateUserOnly** *(boolean) --*

      Set to ``True`` if only the administrator is allowed to create user profiles. Set to ``False``
      if users can sign themselves up via an app.
    """


_RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef", {"ApplicationId": str}
)
_OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef",
    {"RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientUpdateUserPoolClientAnalyticsConfigurationTypeDef(
    _RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef,
    _OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef,
):
    """
    The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.
    - **ApplicationId** *(string) --***[REQUIRED]**

      The application ID for an Amazon Pinpoint application.
    """


_ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef(
    _ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef
):
    pass


_ClientUpdateUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "_ClientUpdateUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[
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
        ],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[Literal["code", "implicit", "client_credentials"]],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": Literal["LEGACY", "ENABLED"],
    },
    total=False,
)


class ClientUpdateUserPoolClientResponseUserPoolClientTypeDef(
    _ClientUpdateUserPoolClientResponseUserPoolClientTypeDef
):
    """
    - **UserPoolClient** *(dict) --*

      The user pool client value from the response from the server when an update user pool client
      request is made.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool client.
    """


_ClientUpdateUserPoolClientResponseTypeDef = TypedDict(
    "_ClientUpdateUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientUpdateUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)


class ClientUpdateUserPoolClientResponseTypeDef(_ClientUpdateUserPoolClientResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server to the request to update the user pool client.
      - **UserPoolClient** *(dict) --*

        The user pool client value from the response from the server when an update user pool client
        request is made.
        - **UserPoolId** *(string) --*

          The user pool ID for the user pool client.
    """


_ClientUpdateUserPoolDeviceConfigurationTypeDef = TypedDict(
    "_ClientUpdateUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)


class ClientUpdateUserPoolDeviceConfigurationTypeDef(
    _ClientUpdateUserPoolDeviceConfigurationTypeDef
):
    """
    Device configuration.
    - **ChallengeRequiredOnNewDevice** *(boolean) --*

      Indicates whether a challenge is required on a new device. Only applicable to a new device.
    """


_ClientUpdateUserPoolDomainCustomDomainConfigTypeDef = TypedDict(
    "_ClientUpdateUserPoolDomainCustomDomainConfigTypeDef", {"CertificateArn": str}
)


class ClientUpdateUserPoolDomainCustomDomainConfigTypeDef(
    _ClientUpdateUserPoolDomainCustomDomainConfigTypeDef
):
    """
    The configuration for a custom domain that hosts the sign-up and sign-in pages for your
    application. Use this object to specify an SSL certificate that is managed by ACM.
    - **CertificateArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this
      certificate for the subdomain of your custom domain.
    """


_ClientUpdateUserPoolDomainResponseTypeDef = TypedDict(
    "_ClientUpdateUserPoolDomainResponseTypeDef", {"CloudFrontDomain": str}, total=False
)


class ClientUpdateUserPoolDomainResponseTypeDef(_ClientUpdateUserPoolDomainResponseTypeDef):
    """
    - *(dict) --*

      The UpdateUserPoolDomain response output.
      - **CloudFrontDomain** *(string) --*

        The Amazon CloudFront endpoint that Amazon Cognito set up when you added the custom domain
        to your user pool.
    """


_ClientUpdateUserPoolEmailConfigurationTypeDef = TypedDict(
    "_ClientUpdateUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": Literal["COGNITO_DEFAULT", "DEVELOPER"],
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)


class ClientUpdateUserPoolEmailConfigurationTypeDef(_ClientUpdateUserPoolEmailConfigurationTypeDef):
    """
    Email configuration.
    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email address
      is used in one of the following ways, depending on the value that you specify for the
      ``EmailSendingAccount`` parameter:
      * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom FROM
      address when it emails your users by using its built-in email account.
      * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by calling
      Amazon SES on your behalf.
    """


_ClientUpdateUserPoolLambdaConfigTypeDef = TypedDict(
    "_ClientUpdateUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientUpdateUserPoolLambdaConfigTypeDef(_ClientUpdateUserPoolLambdaConfigTypeDef):
    """
    The AWS Lambda configuration information from the request to update the user pool.
    - **PreSignUp** *(string) --*

      A pre-registration AWS Lambda trigger.
    """


_ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "_ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)


class ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef(
    _ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef
):
    """
    - **PasswordPolicy** *(dict) --*

      The password policy.
      - **MinimumLength** *(integer) --*

        The minimum length of the password policy that you have set. Cannot be less than 6.
    """


_ClientUpdateUserPoolPoliciesTypeDef = TypedDict(
    "_ClientUpdateUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)


class ClientUpdateUserPoolPoliciesTypeDef(_ClientUpdateUserPoolPoliciesTypeDef):
    """
    A container with the policies you wish to update in a user pool.
    - **PasswordPolicy** *(dict) --*

      The password policy.
      - **MinimumLength** *(integer) --*

        The minimum length of the password policy that you have set. Cannot be less than 6.
    """


_RequiredClientUpdateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateUserPoolSmsConfigurationTypeDef", {"SnsCallerArn": str}
)
_OptionalClientUpdateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateUserPoolSmsConfigurationTypeDef", {"ExternalId": str}, total=False
)


class ClientUpdateUserPoolSmsConfigurationTypeDef(
    _RequiredClientUpdateUserPoolSmsConfigurationTypeDef,
    _OptionalClientUpdateUserPoolSmsConfigurationTypeDef,
):
    """
    SMS configuration.
    - **SnsCallerArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is
      the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.
    """


_ClientUpdateUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "_ClientUpdateUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": Literal["OFF", "AUDIT", "ENFORCED"]},
)


class ClientUpdateUserPoolUserPoolAddOnsTypeDef(_ClientUpdateUserPoolUserPoolAddOnsTypeDef):
    """
    Used to enable advanced security risk detection. Set the key ``AdvancedSecurityMode`` to the
    value "AUDIT".
    - **AdvancedSecurityMode** *(string) --***[REQUIRED]**

      The advanced security mode.
    """


_ClientUpdateUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "_ClientUpdateUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": Literal["CONFIRM_WITH_LINK", "CONFIRM_WITH_CODE"],
    },
    total=False,
)


class ClientUpdateUserPoolVerificationMessageTemplateTypeDef(
    _ClientUpdateUserPoolVerificationMessageTemplateTypeDef
):
    """
    The template for verification messages.
    - **SmsMessage** *(string) --*

      The SMS message template.
    """


_ClientVerifySoftwareTokenResponseTypeDef = TypedDict(
    "_ClientVerifySoftwareTokenResponseTypeDef",
    {"Status": Literal["SUCCESS", "ERROR"], "Session": str},
    total=False,
)


class ClientVerifySoftwareTokenResponseTypeDef(_ClientVerifySoftwareTokenResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The status of the verify software token.
    """


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(_ListGroupsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    - *(dict) --*

      The group type.
      - **GroupName** *(string) --*

        The name of the group.
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {"Groups": List[ListGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The group objects for the groups.
        - *(dict) --*

          The group type.
          - **GroupName** *(string) --*

            The name of the group.
    """


_ListIdentityProvidersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIdentityProvidersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIdentityProvidersPaginatePaginationConfigTypeDef(
    _ListIdentityProvidersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListIdentityProvidersPaginateResponseProvidersTypeDef = TypedDict(
    "_ListIdentityProvidersPaginateResponseProvidersTypeDef",
    {
        "ProviderName": str,
        "ProviderType": Literal[
            "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC"
        ],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ListIdentityProvidersPaginateResponseProvidersTypeDef(
    _ListIdentityProvidersPaginateResponseProvidersTypeDef
):
    """
    - *(dict) --*

      A container for identity provider details.
      - **ProviderName** *(string) --*

        The identity provider name.
    """


_ListIdentityProvidersPaginateResponseTypeDef = TypedDict(
    "_ListIdentityProvidersPaginateResponseTypeDef",
    {"Providers": List[ListIdentityProvidersPaginateResponseProvidersTypeDef]},
    total=False,
)


class ListIdentityProvidersPaginateResponseTypeDef(_ListIdentityProvidersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Providers** *(list) --*

        A list of identity provider objects.
        - *(dict) --*

          A container for identity provider details.
          - **ProviderName** *(string) --*

            The identity provider name.
    """


_ListResourceServersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceServersPaginatePaginationConfigTypeDef(
    _ListResourceServersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourceServersPaginateResponseResourceServersScopesTypeDef = TypedDict(
    "_ListResourceServersPaginateResponseResourceServersScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ListResourceServersPaginateResponseResourceServersScopesTypeDef(
    _ListResourceServersPaginateResponseResourceServersScopesTypeDef
):
    pass


_ListResourceServersPaginateResponseResourceServersTypeDef = TypedDict(
    "_ListResourceServersPaginateResponseResourceServersTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ListResourceServersPaginateResponseResourceServersScopesTypeDef],
    },
    total=False,
)


class ListResourceServersPaginateResponseResourceServersTypeDef(
    _ListResourceServersPaginateResponseResourceServersTypeDef
):
    """
    - *(dict) --*

      A container for information about a resource server for a user pool.
      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that hosts the resource server.
    """


_ListResourceServersPaginateResponseTypeDef = TypedDict(
    "_ListResourceServersPaginateResponseTypeDef",
    {"ResourceServers": List[ListResourceServersPaginateResponseResourceServersTypeDef]},
    total=False,
)


class ListResourceServersPaginateResponseTypeDef(_ListResourceServersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceServers** *(list) --*

        The resource servers.
        - *(dict) --*

          A container for information about a resource server for a user pool.
          - **UserPoolId** *(string) --*

            The user pool ID for the user pool that hosts the resource server.
    """


_ListUserPoolClientsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserPoolClientsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserPoolClientsPaginatePaginationConfigTypeDef(
    _ListUserPoolClientsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef = TypedDict(
    "_ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef",
    {"ClientId": str, "UserPoolId": str, "ClientName": str},
    total=False,
)


class ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef(
    _ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef
):
    """
    - *(dict) --*

      The description of the user pool client.
      - **ClientId** *(string) --*

        The ID of the client associated with the user pool.
    """


_ListUserPoolClientsPaginateResponseTypeDef = TypedDict(
    "_ListUserPoolClientsPaginateResponseTypeDef",
    {"UserPoolClients": List[ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef]},
    total=False,
)


class ListUserPoolClientsPaginateResponseTypeDef(_ListUserPoolClientsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server that lists user pool clients.
      - **UserPoolClients** *(list) --*

        The user pool clients in the response that lists user pool clients.
        - *(dict) --*

          The description of the user pool client.
          - **ClientId** *(string) --*

            The ID of the client associated with the user pool.
    """


_ListUserPoolsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserPoolsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserPoolsPaginatePaginationConfigTypeDef(_ListUserPoolsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef = TypedDict(
    "_ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef(
    _ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef
):
    pass


_ListUserPoolsPaginateResponseUserPoolsTypeDef = TypedDict(
    "_ListUserPoolsPaginateResponseUserPoolsTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ListUserPoolsPaginateResponseUserPoolsTypeDef(_ListUserPoolsPaginateResponseUserPoolsTypeDef):
    """
    - *(dict) --*

      A user pool description.
      - **Id** *(string) --*

        The ID in a user pool description.
    """


_ListUserPoolsPaginateResponseTypeDef = TypedDict(
    "_ListUserPoolsPaginateResponseTypeDef",
    {"UserPools": List[ListUserPoolsPaginateResponseUserPoolsTypeDef]},
    total=False,
)


class ListUserPoolsPaginateResponseTypeDef(_ListUserPoolsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the response to list user pools.
      - **UserPools** *(list) --*

        The user pools from the response to list users.
        - *(dict) --*

          A user pool description.
          - **Id** *(string) --*

            The ID in a user pool description.
    """


_ListUsersInGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersInGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersInGroupPaginatePaginationConfigTypeDef(
    _ListUsersInGroupPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUsersInGroupPaginateResponseUsersAttributesTypeDef = TypedDict(
    "_ListUsersInGroupPaginateResponseUsersAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ListUsersInGroupPaginateResponseUsersAttributesTypeDef(
    _ListUsersInGroupPaginateResponseUsersAttributesTypeDef
):
    pass


_ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef = TypedDict(
    "_ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef(
    _ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef
):
    pass


_ListUsersInGroupPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersInGroupPaginateResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ListUsersInGroupPaginateResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)


class ListUsersInGroupPaginateResponseUsersTypeDef(_ListUsersInGroupPaginateResponseUsersTypeDef):
    """
    - *(dict) --*

      The user type.
      - **Username** *(string) --*

        The user name of the user you wish to describe.
    """


_ListUsersInGroupPaginateResponseTypeDef = TypedDict(
    "_ListUsersInGroupPaginateResponseTypeDef",
    {"Users": List[ListUsersInGroupPaginateResponseUsersTypeDef]},
    total=False,
)


class ListUsersInGroupPaginateResponseTypeDef(_ListUsersInGroupPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        The users returned in the request to list users.
        - *(dict) --*

          The user type.
          - **Username** *(string) --*

            The user name of the user you wish to describe.
    """


_ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersPaginatePaginationConfigTypeDef(_ListUsersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUsersPaginateResponseUsersAttributesTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ListUsersPaginateResponseUsersAttributesTypeDef(
    _ListUsersPaginateResponseUsersAttributesTypeDef
):
    pass


_ListUsersPaginateResponseUsersMFAOptionsTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": Literal["SMS", "EMAIL"], "AttributeName": str},
    total=False,
)


class ListUsersPaginateResponseUsersMFAOptionsTypeDef(
    _ListUsersPaginateResponseUsersMFAOptionsTypeDef
):
    pass


_ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ListUsersPaginateResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": Literal[
            "UNCONFIRMED",
            "CONFIRMED",
            "ARCHIVED",
            "COMPROMISED",
            "UNKNOWN",
            "RESET_REQUIRED",
            "FORCE_CHANGE_PASSWORD",
        ],
        "MFAOptions": List[ListUsersPaginateResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)


class ListUsersPaginateResponseUsersTypeDef(_ListUsersPaginateResponseUsersTypeDef):
    """
    - *(dict) --*

      The user type.
      - **Username** *(string) --*

        The user name of the user you wish to describe.
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    - *(dict) --*

      The response from the request to list users.
      - **Users** *(list) --*

        The users returned in the request to list users.
        - *(dict) --*

          The user type.
          - **Username** *(string) --*

            The user name of the user you wish to describe.
    """
