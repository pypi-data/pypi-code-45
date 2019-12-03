"Main interface for chime service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    "ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "ClientBatchCreateAttendeeAttendeesTypeDef",
    "ClientBatchCreateAttendeeResponseAttendeesTypeDef",
    "ClientBatchCreateAttendeeResponseErrorsTypeDef",
    "ClientBatchCreateAttendeeResponseTypeDef",
    "ClientBatchCreateRoomMembershipMembershipItemListTypeDef",
    "ClientBatchCreateRoomMembershipResponseErrorsTypeDef",
    "ClientBatchCreateRoomMembershipResponseTypeDef",
    "ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef",
    "ClientBatchDeletePhoneNumberResponseTypeDef",
    "ClientBatchSuspendUserResponseUserErrorsTypeDef",
    "ClientBatchSuspendUserResponseTypeDef",
    "ClientBatchUnsuspendUserResponseUserErrorsTypeDef",
    "ClientBatchUnsuspendUserResponseTypeDef",
    "ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef",
    "ClientBatchUpdatePhoneNumberResponseTypeDef",
    "ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    "ClientBatchUpdateUserResponseUserErrorsTypeDef",
    "ClientBatchUpdateUserResponseTypeDef",
    "ClientBatchUpdateUserUpdateUserRequestItemsTypeDef",
    "ClientCreateAccountResponseAccountTypeDef",
    "ClientCreateAccountResponseTypeDef",
    "ClientCreateAttendeeResponseAttendeeTypeDef",
    "ClientCreateAttendeeResponseTypeDef",
    "ClientCreateBotResponseBotTypeDef",
    "ClientCreateBotResponseTypeDef",
    "ClientCreateMeetingNotificationsConfigurationTypeDef",
    "ClientCreateMeetingResponseMeetingMediaPlacementTypeDef",
    "ClientCreateMeetingResponseMeetingTypeDef",
    "ClientCreateMeetingResponseTypeDef",
    "ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    "ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    "ClientCreatePhoneNumberOrderResponseTypeDef",
    "ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef",
    "ClientCreateRoomMembershipResponseRoomMembershipTypeDef",
    "ClientCreateRoomMembershipResponseTypeDef",
    "ClientCreateRoomResponseRoomTypeDef",
    "ClientCreateRoomResponseTypeDef",
    "ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientCreateVoiceConnectorGroupResponseTypeDef",
    "ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientCreateVoiceConnectorResponseTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    "ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "ClientGetAccountResponseAccountTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetAccountSettingsResponseAccountSettingsTypeDef",
    "ClientGetAccountSettingsResponseTypeDef",
    "ClientGetAttendeeResponseAttendeeTypeDef",
    "ClientGetAttendeeResponseTypeDef",
    "ClientGetBotResponseBotTypeDef",
    "ClientGetBotResponseTypeDef",
    "ClientGetEventsConfigurationResponseEventsConfigurationTypeDef",
    "ClientGetEventsConfigurationResponseTypeDef",
    "ClientGetGlobalSettingsResponseBusinessCallingTypeDef",
    "ClientGetGlobalSettingsResponseVoiceConnectorTypeDef",
    "ClientGetGlobalSettingsResponseTypeDef",
    "ClientGetMeetingResponseMeetingMediaPlacementTypeDef",
    "ClientGetMeetingResponseMeetingTypeDef",
    "ClientGetMeetingResponseTypeDef",
    "ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    "ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    "ClientGetPhoneNumberOrderResponseTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientGetPhoneNumberResponsePhoneNumberTypeDef",
    "ClientGetPhoneNumberResponseTypeDef",
    "ClientGetPhoneNumberSettingsResponseTypeDef",
    "ClientGetRoomResponseRoomTypeDef",
    "ClientGetRoomResponseTypeDef",
    "ClientGetUserResponseUserTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef",
    "ClientGetUserSettingsResponseUserSettingsTypeDef",
    "ClientGetUserSettingsResponseTypeDef",
    "ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientGetVoiceConnectorGroupResponseTypeDef",
    "ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    "ClientGetVoiceConnectorOriginationResponseOriginationTypeDef",
    "ClientGetVoiceConnectorOriginationResponseTypeDef",
    "ClientGetVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientGetVoiceConnectorResponseTypeDef",
    "ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    "ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef",
    "ClientGetVoiceConnectorTerminationHealthResponseTypeDef",
    "ClientGetVoiceConnectorTerminationResponseTerminationTypeDef",
    "ClientGetVoiceConnectorTerminationResponseTypeDef",
    "ClientInviteUsersResponseInvitesTypeDef",
    "ClientInviteUsersResponseTypeDef",
    "ClientListAccountsResponseAccountsTypeDef",
    "ClientListAccountsResponseTypeDef",
    "ClientListAttendeesResponseAttendeesTypeDef",
    "ClientListAttendeesResponseTypeDef",
    "ClientListBotsResponseBotsTypeDef",
    "ClientListBotsResponseTypeDef",
    "ClientListMeetingsResponseMeetingsMediaPlacementTypeDef",
    "ClientListMeetingsResponseMeetingsTypeDef",
    "ClientListMeetingsResponseTypeDef",
    "ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef",
    "ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef",
    "ClientListPhoneNumberOrdersResponseTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumbersTypeDef",
    "ClientListPhoneNumbersResponseTypeDef",
    "ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef",
    "ClientListRoomMembershipsResponseRoomMembershipsTypeDef",
    "ClientListRoomMembershipsResponseTypeDef",
    "ClientListRoomsResponseRoomsTypeDef",
    "ClientListRoomsResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef",
    "ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef",
    "ClientListVoiceConnectorGroupsResponseTypeDef",
    "ClientListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef",
    "ClientListVoiceConnectorsResponseTypeDef",
    "ClientPutEventsConfigurationResponseEventsConfigurationTypeDef",
    "ClientPutEventsConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef",
    "ClientPutVoiceConnectorOriginationOriginationTypeDef",
    "ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    "ClientPutVoiceConnectorOriginationResponseOriginationTypeDef",
    "ClientPutVoiceConnectorOriginationResponseTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    "ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef",
    "ClientPutVoiceConnectorTerminationResponseTerminationTypeDef",
    "ClientPutVoiceConnectorTerminationResponseTypeDef",
    "ClientPutVoiceConnectorTerminationTerminationTypeDef",
    "ClientRegenerateSecurityTokenResponseBotTypeDef",
    "ClientRegenerateSecurityTokenResponseTypeDef",
    "ClientResetPersonalPinResponseUserTypeDef",
    "ClientResetPersonalPinResponseTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientRestorePhoneNumberResponsePhoneNumberTypeDef",
    "ClientRestorePhoneNumberResponseTypeDef",
    "ClientSearchAvailablePhoneNumbersResponseTypeDef",
    "ClientUpdateAccountResponseAccountTypeDef",
    "ClientUpdateAccountResponseTypeDef",
    "ClientUpdateAccountSettingsAccountSettingsTypeDef",
    "ClientUpdateBotResponseBotTypeDef",
    "ClientUpdateBotResponseTypeDef",
    "ClientUpdateGlobalSettingsBusinessCallingTypeDef",
    "ClientUpdateGlobalSettingsVoiceConnectorTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    "ClientUpdatePhoneNumberResponsePhoneNumberTypeDef",
    "ClientUpdatePhoneNumberResponseTypeDef",
    "ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef",
    "ClientUpdateRoomMembershipResponseRoomMembershipTypeDef",
    "ClientUpdateRoomMembershipResponseTypeDef",
    "ClientUpdateRoomResponseRoomTypeDef",
    "ClientUpdateRoomResponseTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ClientUpdateUserSettingsUserSettingsTelephonyTypeDef",
    "ClientUpdateUserSettingsUserSettingsTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    "ClientUpdateVoiceConnectorGroupResponseTypeDef",
    "ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    "ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef",
    "ClientUpdateVoiceConnectorResponseTypeDef",
    "ListAccountsPaginatePaginationConfigTypeDef",
    "ListAccountsPaginateResponseAccountsTypeDef",
    "ListAccountsPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUsersTypeDef",
    "ListUsersPaginateResponseTypeDef",
)


_ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef(
    _ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
):
    """
    - *(dict) --*

      If the phone number action fails for one or more of the phone numbers in the request, a list
      of the phone numbers is returned, along with error codes and error messages.
      - **PhoneNumberId** *(string) --*

        The phone number ID for which the action failed.
    """


_ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef(
    _ClientAssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **PhoneNumberErrors** *(list) --*

        If the action fails for one or more of the phone numbers in the request, a list of the phone
        numbers is returned, along with error codes and error messages.
        - *(dict) --*

          If the phone number action fails for one or more of the phone numbers in the request, a
          list of the phone numbers is returned, along with error codes and error messages.
          - **PhoneNumberId** *(string) --*

            The phone number ID for which the action failed.
    """


_ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef(
    _ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef
):
    """
    - *(dict) --*

      If the phone number action fails for one or more of the phone numbers in the request, a list
      of the phone numbers is returned, along with error codes and error messages.
      - **PhoneNumberId** *(string) --*

        The phone number ID for which the action failed.
    """


_ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientAssociatePhoneNumbersWithVoiceConnectorResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef(
    _ClientAssociatePhoneNumbersWithVoiceConnectorResponseTypeDef
):
    """
    - *(dict) --*

      - **PhoneNumberErrors** *(list) --*

        If the action fails for one or more of the phone numbers in the request, a list of the phone
        numbers is returned, along with error codes and error messages.
        - *(dict) --*

          If the phone number action fails for one or more of the phone numbers in the request, a
          list of the phone numbers is returned, along with error codes and error messages.
          - **PhoneNumberId** *(string) --*

            The phone number ID for which the action failed.
    """


_ClientBatchCreateAttendeeAttendeesTypeDef = TypedDict(
    "_ClientBatchCreateAttendeeAttendeesTypeDef", {"ExternalUserId": str}
)


class ClientBatchCreateAttendeeAttendeesTypeDef(_ClientBatchCreateAttendeeAttendeesTypeDef):
    """
    - *(dict) --*

      The Amazon Chime SDK attendee fields to create, used with the BatchCreateAttendee action.
      - **ExternalUserId** *(string) --***[REQUIRED]**

        The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
        builder application.
    """


_ClientBatchCreateAttendeeResponseAttendeesTypeDef = TypedDict(
    "_ClientBatchCreateAttendeeResponseAttendeesTypeDef",
    {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str},
    total=False,
)


class ClientBatchCreateAttendeeResponseAttendeesTypeDef(
    _ClientBatchCreateAttendeeResponseAttendeesTypeDef
):
    """
    - *(dict) --*

      An Amazon Chime SDK meeting attendee. Includes a unique ``AttendeeId`` and ``JoinToken`` . The
      ``JoinToken`` allows a client to authenticate and join as the specified attendee. The
      ``JoinToken`` expires when the meeting ends or when  DeleteAttendee is called. After that, the
      attendee is unable to join the meeting.
      We recommend securely transferring each ``JoinToken`` from your server application to the
      client so that no other client has access to the token except for the one authorized to
      represent the attendee.
      - **ExternalUserId** *(string) --*

        The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
        builder application.
    """


_ClientBatchCreateAttendeeResponseErrorsTypeDef = TypedDict(
    "_ClientBatchCreateAttendeeResponseErrorsTypeDef",
    {"ExternalUserId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchCreateAttendeeResponseErrorsTypeDef(
    _ClientBatchCreateAttendeeResponseErrorsTypeDef
):
    pass


_ClientBatchCreateAttendeeResponseTypeDef = TypedDict(
    "_ClientBatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List[ClientBatchCreateAttendeeResponseAttendeesTypeDef],
        "Errors": List[ClientBatchCreateAttendeeResponseErrorsTypeDef],
    },
    total=False,
)


class ClientBatchCreateAttendeeResponseTypeDef(_ClientBatchCreateAttendeeResponseTypeDef):
    """
    - *(dict) --*

      - **Attendees** *(list) --*

        The attendee information, including attendees IDs and join tokens.
        - *(dict) --*

          An Amazon Chime SDK meeting attendee. Includes a unique ``AttendeeId`` and ``JoinToken`` .
          The ``JoinToken`` allows a client to authenticate and join as the specified attendee. The
          ``JoinToken`` expires when the meeting ends or when  DeleteAttendee is called. After that,
          the attendee is unable to join the meeting.
          We recommend securely transferring each ``JoinToken`` from your server application to the
          client so that no other client has access to the token except for the one authorized to
          represent the attendee.
          - **ExternalUserId** *(string) --*

            The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
            builder application.
    """


_ClientBatchCreateRoomMembershipMembershipItemListTypeDef = TypedDict(
    "_ClientBatchCreateRoomMembershipMembershipItemListTypeDef",
    {"MemberId": str, "Role": Literal["Administrator", "Member"]},
    total=False,
)


class ClientBatchCreateRoomMembershipMembershipItemListTypeDef(
    _ClientBatchCreateRoomMembershipMembershipItemListTypeDef
):
    """
    - *(dict) --*

      Membership details, such as member ID and member role.
      - **MemberId** *(string) --*

        The member ID.
    """


_ClientBatchCreateRoomMembershipResponseErrorsTypeDef = TypedDict(
    "_ClientBatchCreateRoomMembershipResponseErrorsTypeDef",
    {
        "MemberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchCreateRoomMembershipResponseErrorsTypeDef(
    _ClientBatchCreateRoomMembershipResponseErrorsTypeDef
):
    """
    - *(dict) --*

      The list of errors returned when a member action results in an error.
      - **MemberId** *(string) --*

        The member ID.
    """


_ClientBatchCreateRoomMembershipResponseTypeDef = TypedDict(
    "_ClientBatchCreateRoomMembershipResponseTypeDef",
    {"Errors": List[ClientBatchCreateRoomMembershipResponseErrorsTypeDef]},
    total=False,
)


class ClientBatchCreateRoomMembershipResponseTypeDef(
    _ClientBatchCreateRoomMembershipResponseTypeDef
):
    """
    - *(dict) --*

      - **Errors** *(list) --*

        If the action fails for one or more of the member IDs in the request, a list of the member
        IDs is returned, along with error codes and error messages.
        - *(dict) --*

          The list of errors returned when a member action results in an error.
          - **MemberId** *(string) --*

            The member ID.
    """


_ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef(
    _ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef
):
    """
    - *(dict) --*

      If the phone number action fails for one or more of the phone numbers in the request, a list
      of the phone numbers is returned, along with error codes and error messages.
      - **PhoneNumberId** *(string) --*

        The phone number ID for which the action failed.
    """


_ClientBatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "_ClientBatchDeletePhoneNumberResponseTypeDef",
    {"PhoneNumberErrors": List[ClientBatchDeletePhoneNumberResponsePhoneNumberErrorsTypeDef]},
    total=False,
)


class ClientBatchDeletePhoneNumberResponseTypeDef(_ClientBatchDeletePhoneNumberResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumberErrors** *(list) --*

        If the action fails for one or more of the phone numbers in the request, a list of the phone
        numbers is returned, along with error codes and error messages.
        - *(dict) --*

          If the phone number action fails for one or more of the phone numbers in the request, a
          list of the phone numbers is returned, along with error codes and error messages.
          - **PhoneNumberId** *(string) --*

            The phone number ID for which the action failed.
    """


_ClientBatchSuspendUserResponseUserErrorsTypeDef = TypedDict(
    "_ClientBatchSuspendUserResponseUserErrorsTypeDef",
    {
        "UserId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchSuspendUserResponseUserErrorsTypeDef(
    _ClientBatchSuspendUserResponseUserErrorsTypeDef
):
    """
    - *(dict) --*

      The list of errors returned when errors are encountered during the  BatchSuspendUser ,
      BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
      error messages.
      - **UserId** *(string) --*

        The user ID for which the action failed.
    """


_ClientBatchSuspendUserResponseTypeDef = TypedDict(
    "_ClientBatchSuspendUserResponseTypeDef",
    {"UserErrors": List[ClientBatchSuspendUserResponseUserErrorsTypeDef]},
    total=False,
)


class ClientBatchSuspendUserResponseTypeDef(_ClientBatchSuspendUserResponseTypeDef):
    """
    - *(dict) --*

      - **UserErrors** *(list) --*

        If the  BatchSuspendUser action fails for one or more of the user IDs in the request, a list
        of the user IDs is returned, along with error codes and error messages.
        - *(dict) --*

          The list of errors returned when errors are encountered during the  BatchSuspendUser ,
          BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
          error messages.
          - **UserId** *(string) --*

            The user ID for which the action failed.
    """


_ClientBatchUnsuspendUserResponseUserErrorsTypeDef = TypedDict(
    "_ClientBatchUnsuspendUserResponseUserErrorsTypeDef",
    {
        "UserId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchUnsuspendUserResponseUserErrorsTypeDef(
    _ClientBatchUnsuspendUserResponseUserErrorsTypeDef
):
    """
    - *(dict) --*

      The list of errors returned when errors are encountered during the  BatchSuspendUser ,
      BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
      error messages.
      - **UserId** *(string) --*

        The user ID for which the action failed.
    """


_ClientBatchUnsuspendUserResponseTypeDef = TypedDict(
    "_ClientBatchUnsuspendUserResponseTypeDef",
    {"UserErrors": List[ClientBatchUnsuspendUserResponseUserErrorsTypeDef]},
    total=False,
)


class ClientBatchUnsuspendUserResponseTypeDef(_ClientBatchUnsuspendUserResponseTypeDef):
    """
    - *(dict) --*

      - **UserErrors** *(list) --*

        If the  BatchUnsuspendUser action fails for one or more of the user IDs in the request, a
        list of the user IDs is returned, along with error codes and error messages.
        - *(dict) --*

          The list of errors returned when errors are encountered during the  BatchSuspendUser ,
          BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
          error messages.
          - **UserId** *(string) --*

            The user ID for which the action failed.
    """


_ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef(
    _ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef
):
    """
    - *(dict) --*

      If the phone number action fails for one or more of the phone numbers in the request, a list
      of the phone numbers is returned, along with error codes and error messages.
      - **PhoneNumberId** *(string) --*

        The phone number ID for which the action failed.
    """


_ClientBatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "_ClientBatchUpdatePhoneNumberResponseTypeDef",
    {"PhoneNumberErrors": List[ClientBatchUpdatePhoneNumberResponsePhoneNumberErrorsTypeDef]},
    total=False,
)


class ClientBatchUpdatePhoneNumberResponseTypeDef(_ClientBatchUpdatePhoneNumberResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumberErrors** *(list) --*

        If the action fails for one or more of the phone numbers in the request, a list of the phone
        numbers is returned, along with error codes and error messages.
        - *(dict) --*

          If the phone number action fails for one or more of the phone numbers in the request, a
          list of the phone numbers is returned, along with error codes and error messages.
          - **PhoneNumberId** *(string) --*

            The phone number ID for which the action failed.
    """


_RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef = TypedDict(
    "_RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    {"PhoneNumberId": str},
)
_OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef = TypedDict(
    "_OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef",
    {"ProductType": Literal["BusinessCalling", "VoiceConnector"], "CallingName": str},
    total=False,
)


class ClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef(
    _RequiredClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef,
    _OptionalClientBatchUpdatePhoneNumberUpdatePhoneNumberRequestItemsTypeDef,
):
    """
    - *(dict) --*

      The phone number ID, product type, or calling name fields to update, used with the
      BatchUpdatePhoneNumber and  UpdatePhoneNumber actions.
      - **PhoneNumberId** *(string) --***[REQUIRED]**

        The phone number ID to update.
    """


_ClientBatchUpdateUserResponseUserErrorsTypeDef = TypedDict(
    "_ClientBatchUpdateUserResponseUserErrorsTypeDef",
    {
        "UserId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchUpdateUserResponseUserErrorsTypeDef(
    _ClientBatchUpdateUserResponseUserErrorsTypeDef
):
    """
    - *(dict) --*

      The list of errors returned when errors are encountered during the  BatchSuspendUser ,
      BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
      error messages.
      - **UserId** *(string) --*

        The user ID for which the action failed.
    """


_ClientBatchUpdateUserResponseTypeDef = TypedDict(
    "_ClientBatchUpdateUserResponseTypeDef",
    {"UserErrors": List[ClientBatchUpdateUserResponseUserErrorsTypeDef]},
    total=False,
)


class ClientBatchUpdateUserResponseTypeDef(_ClientBatchUpdateUserResponseTypeDef):
    """
    - *(dict) --*

      - **UserErrors** *(list) --*

        If the  BatchUpdateUser action fails for one or more of the user IDs in the request, a list
        of the user IDs is returned, along with error codes and error messages.
        - *(dict) --*

          The list of errors returned when errors are encountered during the  BatchSuspendUser ,
          BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and
          error messages.
          - **UserId** *(string) --*

            The user ID for which the action failed.
    """


_RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef = TypedDict(
    "_RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef", {"UserId": str}
)
_OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef = TypedDict(
    "_OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef",
    {"LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"]},
    total=False,
)


class ClientBatchUpdateUserUpdateUserRequestItemsTypeDef(
    _RequiredClientBatchUpdateUserUpdateUserRequestItemsTypeDef,
    _OptionalClientBatchUpdateUserUpdateUserRequestItemsTypeDef,
):
    """
    - *(dict) --*

      The user ID and user fields to update, used with the  BatchUpdateUser action.
      - **UserId** *(string) --***[REQUIRED]**

        The user ID.
    """


_ClientCreateAccountResponseAccountTypeDef = TypedDict(
    "_ClientCreateAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
    },
    total=False,
)


class ClientCreateAccountResponseAccountTypeDef(_ClientCreateAccountResponseAccountTypeDef):
    """
    - **Account** *(dict) --*

      The Amazon Chime account details.
      - **AwsAccountId** *(string) --*

        The AWS account ID.
    """


_ClientCreateAccountResponseTypeDef = TypedDict(
    "_ClientCreateAccountResponseTypeDef",
    {"Account": ClientCreateAccountResponseAccountTypeDef},
    total=False,
)


class ClientCreateAccountResponseTypeDef(_ClientCreateAccountResponseTypeDef):
    """
    - *(dict) --*

      - **Account** *(dict) --*

        The Amazon Chime account details.
        - **AwsAccountId** *(string) --*

          The AWS account ID.
    """


_ClientCreateAttendeeResponseAttendeeTypeDef = TypedDict(
    "_ClientCreateAttendeeResponseAttendeeTypeDef",
    {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str},
    total=False,
)


class ClientCreateAttendeeResponseAttendeeTypeDef(_ClientCreateAttendeeResponseAttendeeTypeDef):
    """
    - **Attendee** *(dict) --*

      The attendee information, including attendee ID and join token.
      - **ExternalUserId** *(string) --*

        The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
        builder application.
    """


_ClientCreateAttendeeResponseTypeDef = TypedDict(
    "_ClientCreateAttendeeResponseTypeDef",
    {"Attendee": ClientCreateAttendeeResponseAttendeeTypeDef},
    total=False,
)


class ClientCreateAttendeeResponseTypeDef(_ClientCreateAttendeeResponseTypeDef):
    """
    - *(dict) --*

      - **Attendee** *(dict) --*

        The attendee information, including attendee ID and join token.
        - **ExternalUserId** *(string) --*

          The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
          builder application.
    """


_ClientCreateBotResponseBotTypeDef = TypedDict(
    "_ClientCreateBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientCreateBotResponseBotTypeDef(_ClientCreateBotResponseBotTypeDef):
    """
    - **Bot** *(dict) --*

      The bot details.
      - **BotId** *(string) --*

        The bot ID.
    """


_ClientCreateBotResponseTypeDef = TypedDict(
    "_ClientCreateBotResponseTypeDef", {"Bot": ClientCreateBotResponseBotTypeDef}, total=False
)


class ClientCreateBotResponseTypeDef(_ClientCreateBotResponseTypeDef):
    """
    - *(dict) --*

      - **Bot** *(dict) --*

        The bot details.
        - **BotId** *(string) --*

          The bot ID.
    """


_ClientCreateMeetingNotificationsConfigurationTypeDef = TypedDict(
    "_ClientCreateMeetingNotificationsConfigurationTypeDef",
    {"SnsTopicArn": str, "SqsQueueArn": str},
    total=False,
)


class ClientCreateMeetingNotificationsConfigurationTypeDef(
    _ClientCreateMeetingNotificationsConfigurationTypeDef
):
    """
    The configuration for resource targets to receive notifications when meeting and attendee events
    occur.
    - **SnsTopicArn** *(string) --*

      The SNS topic ARN.
    """


_ClientCreateMeetingResponseMeetingMediaPlacementTypeDef = TypedDict(
    "_ClientCreateMeetingResponseMeetingMediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "ScreenDataUrl": str,
        "ScreenSharingUrl": str,
        "ScreenViewingUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
    },
    total=False,
)


class ClientCreateMeetingResponseMeetingMediaPlacementTypeDef(
    _ClientCreateMeetingResponseMeetingMediaPlacementTypeDef
):
    pass


_ClientCreateMeetingResponseMeetingTypeDef = TypedDict(
    "_ClientCreateMeetingResponseMeetingTypeDef",
    {
        "MeetingId": str,
        "MediaPlacement": ClientCreateMeetingResponseMeetingMediaPlacementTypeDef,
        "MediaRegion": str,
    },
    total=False,
)


class ClientCreateMeetingResponseMeetingTypeDef(_ClientCreateMeetingResponseMeetingTypeDef):
    """
    - **Meeting** *(dict) --*

      The meeting information, including the meeting ID and ``MediaPlacement`` .
      - **MeetingId** *(string) --*

        The Amazon Chime SDK meeting ID.
    """


_ClientCreateMeetingResponseTypeDef = TypedDict(
    "_ClientCreateMeetingResponseTypeDef",
    {"Meeting": ClientCreateMeetingResponseMeetingTypeDef},
    total=False,
)


class ClientCreateMeetingResponseTypeDef(_ClientCreateMeetingResponseTypeDef):
    """
    - *(dict) --*

      - **Meeting** *(dict) --*

        The meeting information, including the meeting ID and ``MediaPlacement`` .
        - **MeetingId** *(string) --*

          The Amazon Chime SDK meeting ID.
    """


_ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef = TypedDict(
    "_ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": Literal["Processing", "Acquired", "Failed"]},
    total=False,
)


class ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef(
    _ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
):
    pass


_ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef = TypedDict(
    "_ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal["Processing", "Successful", "Failed", "Partial"],
        "OrderedPhoneNumbers": List[
            ClientCreatePhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef(
    _ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef
):
    """
    - **PhoneNumberOrder** *(dict) --*

      The phone number order details.
      - **PhoneNumberOrderId** *(string) --*

        The phone number order ID.
    """


_ClientCreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "_ClientCreatePhoneNumberOrderResponseTypeDef",
    {"PhoneNumberOrder": ClientCreatePhoneNumberOrderResponsePhoneNumberOrderTypeDef},
    total=False,
)


class ClientCreatePhoneNumberOrderResponseTypeDef(_ClientCreatePhoneNumberOrderResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumberOrder** *(dict) --*

        The phone number order details.
        - **PhoneNumberOrderId** *(string) --*

          The phone number order ID.
    """


_ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef = TypedDict(
    "_ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": Literal["User", "Bot", "Webhook"],
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)


class ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef(
    _ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef
):
    pass


_ClientCreateRoomMembershipResponseRoomMembershipTypeDef = TypedDict(
    "_ClientCreateRoomMembershipResponseRoomMembershipTypeDef",
    {
        "RoomId": str,
        "Member": ClientCreateRoomMembershipResponseRoomMembershipMemberTypeDef,
        "Role": Literal["Administrator", "Member"],
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateRoomMembershipResponseRoomMembershipTypeDef(
    _ClientCreateRoomMembershipResponseRoomMembershipTypeDef
):
    """
    - **RoomMembership** *(dict) --*

      The room membership details.
      - **RoomId** *(string) --*

        The room ID.
    """


_ClientCreateRoomMembershipResponseTypeDef = TypedDict(
    "_ClientCreateRoomMembershipResponseTypeDef",
    {"RoomMembership": ClientCreateRoomMembershipResponseRoomMembershipTypeDef},
    total=False,
)


class ClientCreateRoomMembershipResponseTypeDef(_ClientCreateRoomMembershipResponseTypeDef):
    """
    - *(dict) --*

      - **RoomMembership** *(dict) --*

        The room membership details.
        - **RoomId** *(string) --*

          The room ID.
    """


_ClientCreateRoomResponseRoomTypeDef = TypedDict(
    "_ClientCreateRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateRoomResponseRoomTypeDef(_ClientCreateRoomResponseRoomTypeDef):
    """
    - **Room** *(dict) --*

      The room details.
      - **RoomId** *(string) --*

        The room ID.
    """


_ClientCreateRoomResponseTypeDef = TypedDict(
    "_ClientCreateRoomResponseTypeDef", {"Room": ClientCreateRoomResponseRoomTypeDef}, total=False
)


class ClientCreateRoomResponseTypeDef(_ClientCreateRoomResponseTypeDef):
    """
    - *(dict) --*

      - **Room** *(dict) --*

        The room details.
        - **RoomId** *(string) --*

          The room ID.
    """


_ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)


class ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
):
    pass


_ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef(
    _ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
):
    """
    - **VoiceConnectorGroup** *(dict) --*

      The Amazon Chime Voice Connector group details.
      - **VoiceConnectorGroupId** *(string) --*

        The Amazon Chime Voice Connector group ID.
    """


_ClientCreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": ClientCreateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef},
    total=False,
)


class ClientCreateVoiceConnectorGroupResponseTypeDef(
    _ClientCreateVoiceConnectorGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **VoiceConnectorGroup** *(dict) --*

        The Amazon Chime Voice Connector group details.
        - **VoiceConnectorGroupId** *(string) --*

          The Amazon Chime Voice Connector group ID.
    """


_RequiredClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_RequiredClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef", {"VoiceConnectorId": str}
)
_OptionalClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_OptionalClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"Priority": int},
    total=False,
)


class ClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _RequiredClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
    _OptionalClientCreateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
):
    """
    - *(dict) --*

      For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route
      inbound calls. Includes priority configuration settings. Limit: 3 ``VoiceConnectorItems`` per
      Amazon Chime Voice Connector group.
      - **VoiceConnectorId** *(string) --***[REQUIRED]**

        The Amazon Chime Voice Connector ID.
    """


_ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef(
    _ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef
):
    """
    - **VoiceConnector** *(dict) --*

      The Amazon Chime Voice Connector details.
      - **VoiceConnectorId** *(string) --*

        The Amazon Chime Voice Connector ID.
    """


_ClientCreateVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientCreateVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientCreateVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)


class ClientCreateVoiceConnectorResponseTypeDef(_ClientCreateVoiceConnectorResponseTypeDef):
    """
    - *(dict) --*

      - **VoiceConnector** *(dict) --*

        The Amazon Chime Voice Connector details.
        - **VoiceConnectorId** *(string) --*

          The Amazon Chime Voice Connector ID.
    """


_ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef(
    _ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
):
    """
    - *(dict) --*

      If the phone number action fails for one or more of the phone numbers in the request, a list
      of the phone numbers is returned, along with error codes and error messages.
      - **PhoneNumberId** *(string) --*

        The phone number ID for which the action failed.
    """


_ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef(
    _ClientDisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **PhoneNumberErrors** *(list) --*

        If the action fails for one or more of the phone numbers in the request, a list of the phone
        numbers is returned, along with error codes and error messages.
        - *(dict) --*

          If the phone number action fails for one or more of the phone numbers in the request, a
          list of the phone numbers is returned, along with error codes and error messages.
          - **PhoneNumberId** *(string) --*

            The phone number ID for which the action failed.
    """


_ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef = TypedDict(
    "_ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": Literal[
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "AccessDenied",
            "ServiceUnavailable",
            "Throttled",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
            "PhoneNumberAssociationsExist",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef(
    _ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef
):
    """
    - *(dict) --*

      If the phone number action fails for one or more of the phone numbers in the request, a list
      of the phone numbers is returned, along with error codes and error messages.
      - **PhoneNumberId** *(string) --*

        The phone number ID for which the action failed.
    """


_ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[
            ClientDisassociatePhoneNumbersFromVoiceConnectorResponsePhoneNumberErrorsTypeDef
        ]
    },
    total=False,
)


class ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef(
    _ClientDisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef
):
    """
    - *(dict) --*

      - **PhoneNumberErrors** *(list) --*

        If the action fails for one or more of the phone numbers in the request, a list of the phone
        numbers is returned, along with error codes and error messages.
        - *(dict) --*

          If the phone number action fails for one or more of the phone numbers in the request, a
          list of the phone numbers is returned, along with error codes and error messages.
          - **PhoneNumberId** *(string) --*

            The phone number ID for which the action failed.
    """


_ClientGetAccountResponseAccountTypeDef = TypedDict(
    "_ClientGetAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
    },
    total=False,
)


class ClientGetAccountResponseAccountTypeDef(_ClientGetAccountResponseAccountTypeDef):
    """
    - **Account** *(dict) --*

      The Amazon Chime account details.
      - **AwsAccountId** *(string) --*

        The AWS account ID.
    """


_ClientGetAccountResponseTypeDef = TypedDict(
    "_ClientGetAccountResponseTypeDef",
    {"Account": ClientGetAccountResponseAccountTypeDef},
    total=False,
)


class ClientGetAccountResponseTypeDef(_ClientGetAccountResponseTypeDef):
    """
    - *(dict) --*

      - **Account** *(dict) --*

        The Amazon Chime account details.
        - **AwsAccountId** *(string) --*

          The AWS account ID.
    """


_ClientGetAccountSettingsResponseAccountSettingsTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseAccountSettingsTypeDef",
    {"DisableRemoteControl": bool, "EnableDialOut": bool},
    total=False,
)


class ClientGetAccountSettingsResponseAccountSettingsTypeDef(
    _ClientGetAccountSettingsResponseAccountSettingsTypeDef
):
    """
    - **AccountSettings** *(dict) --*

      The Amazon Chime account settings.
      - **DisableRemoteControl** *(boolean) --*

        Setting that stops or starts remote control of shared screens during meetings.
    """


_ClientGetAccountSettingsResponseTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseTypeDef",
    {"AccountSettings": ClientGetAccountSettingsResponseAccountSettingsTypeDef},
    total=False,
)


class ClientGetAccountSettingsResponseTypeDef(_ClientGetAccountSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **AccountSettings** *(dict) --*

        The Amazon Chime account settings.
        - **DisableRemoteControl** *(boolean) --*

          Setting that stops or starts remote control of shared screens during meetings.
    """


_ClientGetAttendeeResponseAttendeeTypeDef = TypedDict(
    "_ClientGetAttendeeResponseAttendeeTypeDef",
    {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str},
    total=False,
)


class ClientGetAttendeeResponseAttendeeTypeDef(_ClientGetAttendeeResponseAttendeeTypeDef):
    """
    - **Attendee** *(dict) --*

      The Amazon Chime SDK attendee information.
      - **ExternalUserId** *(string) --*

        The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
        builder application.
    """


_ClientGetAttendeeResponseTypeDef = TypedDict(
    "_ClientGetAttendeeResponseTypeDef",
    {"Attendee": ClientGetAttendeeResponseAttendeeTypeDef},
    total=False,
)


class ClientGetAttendeeResponseTypeDef(_ClientGetAttendeeResponseTypeDef):
    """
    - *(dict) --*

      - **Attendee** *(dict) --*

        The Amazon Chime SDK attendee information.
        - **ExternalUserId** *(string) --*

          The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
          builder application.
    """


_ClientGetBotResponseBotTypeDef = TypedDict(
    "_ClientGetBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientGetBotResponseBotTypeDef(_ClientGetBotResponseBotTypeDef):
    """
    - **Bot** *(dict) --*

      The chat bot details.
      - **BotId** *(string) --*

        The bot ID.
    """


_ClientGetBotResponseTypeDef = TypedDict(
    "_ClientGetBotResponseTypeDef", {"Bot": ClientGetBotResponseBotTypeDef}, total=False
)


class ClientGetBotResponseTypeDef(_ClientGetBotResponseTypeDef):
    """
    - *(dict) --*

      - **Bot** *(dict) --*

        The chat bot details.
        - **BotId** *(string) --*

          The bot ID.
    """


_ClientGetEventsConfigurationResponseEventsConfigurationTypeDef = TypedDict(
    "_ClientGetEventsConfigurationResponseEventsConfigurationTypeDef",
    {"BotId": str, "OutboundEventsHTTPSEndpoint": str, "LambdaFunctionArn": str},
    total=False,
)


class ClientGetEventsConfigurationResponseEventsConfigurationTypeDef(
    _ClientGetEventsConfigurationResponseEventsConfigurationTypeDef
):
    """
    - **EventsConfiguration** *(dict) --*

      The events configuration details.
      - **BotId** *(string) --*

        The bot ID.
    """


_ClientGetEventsConfigurationResponseTypeDef = TypedDict(
    "_ClientGetEventsConfigurationResponseTypeDef",
    {"EventsConfiguration": ClientGetEventsConfigurationResponseEventsConfigurationTypeDef},
    total=False,
)


class ClientGetEventsConfigurationResponseTypeDef(_ClientGetEventsConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **EventsConfiguration** *(dict) --*

        The events configuration details.
        - **BotId** *(string) --*

          The bot ID.
    """


_ClientGetGlobalSettingsResponseBusinessCallingTypeDef = TypedDict(
    "_ClientGetGlobalSettingsResponseBusinessCallingTypeDef", {"CdrBucket": str}, total=False
)


class ClientGetGlobalSettingsResponseBusinessCallingTypeDef(
    _ClientGetGlobalSettingsResponseBusinessCallingTypeDef
):
    """
    - **BusinessCalling** *(dict) --*

      The Amazon Chime Business Calling settings.
      - **CdrBucket** *(string) --*

        The Amazon S3 bucket designated for call detail record storage.
    """


_ClientGetGlobalSettingsResponseVoiceConnectorTypeDef = TypedDict(
    "_ClientGetGlobalSettingsResponseVoiceConnectorTypeDef", {"CdrBucket": str}, total=False
)


class ClientGetGlobalSettingsResponseVoiceConnectorTypeDef(
    _ClientGetGlobalSettingsResponseVoiceConnectorTypeDef
):
    pass


_ClientGetGlobalSettingsResponseTypeDef = TypedDict(
    "_ClientGetGlobalSettingsResponseTypeDef",
    {
        "BusinessCalling": ClientGetGlobalSettingsResponseBusinessCallingTypeDef,
        "VoiceConnector": ClientGetGlobalSettingsResponseVoiceConnectorTypeDef,
    },
    total=False,
)


class ClientGetGlobalSettingsResponseTypeDef(_ClientGetGlobalSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **BusinessCalling** *(dict) --*

        The Amazon Chime Business Calling settings.
        - **CdrBucket** *(string) --*

          The Amazon S3 bucket designated for call detail record storage.
    """


_ClientGetMeetingResponseMeetingMediaPlacementTypeDef = TypedDict(
    "_ClientGetMeetingResponseMeetingMediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "ScreenDataUrl": str,
        "ScreenSharingUrl": str,
        "ScreenViewingUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
    },
    total=False,
)


class ClientGetMeetingResponseMeetingMediaPlacementTypeDef(
    _ClientGetMeetingResponseMeetingMediaPlacementTypeDef
):
    pass


_ClientGetMeetingResponseMeetingTypeDef = TypedDict(
    "_ClientGetMeetingResponseMeetingTypeDef",
    {
        "MeetingId": str,
        "MediaPlacement": ClientGetMeetingResponseMeetingMediaPlacementTypeDef,
        "MediaRegion": str,
    },
    total=False,
)


class ClientGetMeetingResponseMeetingTypeDef(_ClientGetMeetingResponseMeetingTypeDef):
    """
    - **Meeting** *(dict) --*

      The Amazon Chime SDK meeting information.
      - **MeetingId** *(string) --*

        The Amazon Chime SDK meeting ID.
    """


_ClientGetMeetingResponseTypeDef = TypedDict(
    "_ClientGetMeetingResponseTypeDef",
    {"Meeting": ClientGetMeetingResponseMeetingTypeDef},
    total=False,
)


class ClientGetMeetingResponseTypeDef(_ClientGetMeetingResponseTypeDef):
    """
    - *(dict) --*

      - **Meeting** *(dict) --*

        The Amazon Chime SDK meeting information.
        - **MeetingId** *(string) --*

          The Amazon Chime SDK meeting ID.
    """


_ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef = TypedDict(
    "_ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": Literal["Processing", "Acquired", "Failed"]},
    total=False,
)


class ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef(
    _ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
):
    pass


_ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef = TypedDict(
    "_ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal["Processing", "Successful", "Failed", "Partial"],
        "OrderedPhoneNumbers": List[
            ClientGetPhoneNumberOrderResponsePhoneNumberOrderOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef(
    _ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef
):
    """
    - **PhoneNumberOrder** *(dict) --*

      The phone number order details.
      - **PhoneNumberOrderId** *(string) --*

        The phone number order ID.
    """


_ClientGetPhoneNumberOrderResponseTypeDef = TypedDict(
    "_ClientGetPhoneNumberOrderResponseTypeDef",
    {"PhoneNumberOrder": ClientGetPhoneNumberOrderResponsePhoneNumberOrderTypeDef},
    total=False,
)


class ClientGetPhoneNumberOrderResponseTypeDef(_ClientGetPhoneNumberOrderResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumberOrder** *(dict) --*

        The phone number order details.
        - **PhoneNumberOrderId** *(string) --*

          The phone number order ID.
    """


_ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "_ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {
        "Value": str,
        "Name": Literal["AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef(
    _ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef
):
    pass


_ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "_ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)


class ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef(
    _ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef
):
    pass


_ClientGetPhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "_ClientGetPhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": ClientGetPhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[ClientGetPhoneNumberResponsePhoneNumberAssociationsTypeDef],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ClientGetPhoneNumberResponsePhoneNumberTypeDef(
    _ClientGetPhoneNumberResponsePhoneNumberTypeDef
):
    """
    - **PhoneNumber** *(dict) --*

      The phone number details.
      - **PhoneNumberId** *(string) --*

        The phone number ID.
    """


_ClientGetPhoneNumberResponseTypeDef = TypedDict(
    "_ClientGetPhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientGetPhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)


class ClientGetPhoneNumberResponseTypeDef(_ClientGetPhoneNumberResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumber** *(dict) --*

        The phone number details.
        - **PhoneNumberId** *(string) --*

          The phone number ID.
    """


_ClientGetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "_ClientGetPhoneNumberSettingsResponseTypeDef",
    {"CallingName": str, "CallingNameUpdatedTimestamp": datetime},
    total=False,
)


class ClientGetPhoneNumberSettingsResponseTypeDef(_ClientGetPhoneNumberSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **CallingName** *(string) --*

        The default outbound calling name for the account.
    """


_ClientGetRoomResponseRoomTypeDef = TypedDict(
    "_ClientGetRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetRoomResponseRoomTypeDef(_ClientGetRoomResponseRoomTypeDef):
    """
    - **Room** *(dict) --*

      The room details.
      - **RoomId** *(string) --*

        The room ID.
    """


_ClientGetRoomResponseTypeDef = TypedDict(
    "_ClientGetRoomResponseTypeDef", {"Room": ClientGetRoomResponseRoomTypeDef}, total=False
)


class ClientGetRoomResponseTypeDef(_ClientGetRoomResponseTypeDef):
    """
    - *(dict) --*

      - **Room** *(dict) --*

        The room details.
        - **RoomId** *(string) --*

          The room ID.
    """


_ClientGetUserResponseUserTypeDef = TypedDict(
    "_ClientGetUserResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ClientGetUserResponseUserTypeDef(_ClientGetUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The user details.
      - **UserId** *(string) --*

        The user ID.
    """


_ClientGetUserResponseTypeDef = TypedDict(
    "_ClientGetUserResponseTypeDef", {"User": ClientGetUserResponseUserTypeDef}, total=False
)


class ClientGetUserResponseTypeDef(_ClientGetUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The user details.
        - **UserId** *(string) --*

          The user ID.
    """


_ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef = TypedDict(
    "_ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef",
    {"InboundCalling": bool, "OutboundCalling": bool, "SMS": bool},
    total=False,
)


class ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef(
    _ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef
):
    """
    - **Telephony** *(dict) --*

      The telephony settings associated with the user.
      - **InboundCalling** *(boolean) --*

        Allows or denies inbound calling.
    """


_ClientGetUserSettingsResponseUserSettingsTypeDef = TypedDict(
    "_ClientGetUserSettingsResponseUserSettingsTypeDef",
    {"Telephony": ClientGetUserSettingsResponseUserSettingsTelephonyTypeDef},
    total=False,
)


class ClientGetUserSettingsResponseUserSettingsTypeDef(
    _ClientGetUserSettingsResponseUserSettingsTypeDef
):
    """
    - **UserSettings** *(dict) --*

      The user settings.
      - **Telephony** *(dict) --*

        The telephony settings associated with the user.
        - **InboundCalling** *(boolean) --*

          Allows or denies inbound calling.
    """


_ClientGetUserSettingsResponseTypeDef = TypedDict(
    "_ClientGetUserSettingsResponseTypeDef",
    {"UserSettings": ClientGetUserSettingsResponseUserSettingsTypeDef},
    total=False,
)


class ClientGetUserSettingsResponseTypeDef(_ClientGetUserSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **UserSettings** *(dict) --*

        The user settings.
        - **Telephony** *(dict) --*

          The telephony settings associated with the user.
          - **InboundCalling** *(boolean) --*

            Allows or denies inbound calling.
    """


_ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)


class ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
):
    pass


_ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "_ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef(
    _ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
):
    """
    - **VoiceConnectorGroup** *(dict) --*

      The Amazon Chime Voice Connector group details.
      - **VoiceConnectorGroupId** *(string) --*

        The Amazon Chime Voice Connector group ID.
    """


_ClientGetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": ClientGetVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef},
    total=False,
)


class ClientGetVoiceConnectorGroupResponseTypeDef(_ClientGetVoiceConnectorGroupResponseTypeDef):
    """
    - *(dict) --*

      - **VoiceConnectorGroup** *(dict) --*

        The Amazon Chime Voice Connector group details.
        - **VoiceConnectorGroupId** *(string) --*

          The Amazon Chime Voice Connector group ID.
    """


_ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "_ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)


class ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef(
    _ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
):
    """
    - **LoggingConfiguration** *(dict) --*

      The logging configuration details.
      - **EnableSIPLogs** *(boolean) --*

        When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": ClientGetVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
    },
    total=False,
)


class ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef(
    _ClientGetVoiceConnectorLoggingConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **LoggingConfiguration** *(dict) --*

        The logging configuration details.
        - **EnableSIPLogs** *(boolean) --*

          When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef = TypedDict(
    "_ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": Literal["TCP", "UDP"], "Priority": int, "Weight": int},
    total=False,
)


class ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef(
    _ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef
):
    """
    - *(dict) --*

      Origination routes define call distribution properties for your SIP hosts to receive inbound
      calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon
      Chime Voice Connector.
      - **Host** *(string) --*

        The FQDN or IP address to contact for origination traffic.
    """


_ClientGetVoiceConnectorOriginationResponseOriginationTypeDef = TypedDict(
    "_ClientGetVoiceConnectorOriginationResponseOriginationTypeDef",
    {
        "Routes": List[ClientGetVoiceConnectorOriginationResponseOriginationRoutesTypeDef],
        "Disabled": bool,
    },
    total=False,
)


class ClientGetVoiceConnectorOriginationResponseOriginationTypeDef(
    _ClientGetVoiceConnectorOriginationResponseOriginationTypeDef
):
    """
    - **Origination** *(dict) --*

      The origination setting details.
      - **Routes** *(list) --*

        The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
        1. Maximum value of 20.
        - *(dict) --*

          Origination routes define call distribution properties for your SIP hosts to receive
          inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
          each Amazon Chime Voice Connector.
          - **Host** *(string) --*

            The FQDN or IP address to contact for origination traffic.
    """


_ClientGetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorOriginationResponseTypeDef",
    {"Origination": ClientGetVoiceConnectorOriginationResponseOriginationTypeDef},
    total=False,
)


class ClientGetVoiceConnectorOriginationResponseTypeDef(
    _ClientGetVoiceConnectorOriginationResponseTypeDef
):
    """
    - *(dict) --*

      - **Origination** *(dict) --*

        The origination setting details.
        - **Routes** *(list) --*

          The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
          1. Maximum value of 20.
          - *(dict) --*

            Origination routes define call distribution properties for your SIP hosts to receive
            inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
            each Amazon Chime Voice Connector.
            - **Host** *(string) --*

              The FQDN or IP address to contact for origination traffic.
    """


_ClientGetVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "_ClientGetVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientGetVoiceConnectorResponseVoiceConnectorTypeDef(
    _ClientGetVoiceConnectorResponseVoiceConnectorTypeDef
):
    """
    - **VoiceConnector** *(dict) --*

      The Amazon Chime Voice Connector details.
      - **VoiceConnectorId** *(string) --*

        The Amazon Chime Voice Connector ID.
    """


_ClientGetVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientGetVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)


class ClientGetVoiceConnectorResponseTypeDef(_ClientGetVoiceConnectorResponseTypeDef):
    """
    - *(dict) --*

      - **VoiceConnector** *(dict) --*

        The Amazon Chime Voice Connector details.
        - **VoiceConnectorId** *(string) --*

          The Amazon Chime Voice Connector ID.
    """


_ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef = TypedDict(
    "_ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int, "Disabled": bool},
    total=False,
)


class ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef(
    _ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
):
    """
    - **StreamingConfiguration** *(dict) --*

      The streaming configuration details.
      - **DataRetentionInHours** *(integer) --*

        The retention period, in hours, for the Amazon Kinesis data.
    """


_ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": ClientGetVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
    },
    total=False,
)


class ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef(
    _ClientGetVoiceConnectorStreamingConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **StreamingConfiguration** *(dict) --*

        The streaming configuration details.
        - **DataRetentionInHours** *(integer) --*

          The retention period, in hours, for the Amazon Kinesis data.
    """


_ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef = TypedDict(
    "_ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef",
    {"Timestamp": datetime, "Source": str},
    total=False,
)


class ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef(
    _ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef
):
    """
    - **TerminationHealth** *(dict) --*

      The termination health details.
      - **Timestamp** *(datetime) --*

        The timestamp, in ISO 8601 format.
    """


_ClientGetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorTerminationHealthResponseTypeDef",
    {"TerminationHealth": ClientGetVoiceConnectorTerminationHealthResponseTerminationHealthTypeDef},
    total=False,
)


class ClientGetVoiceConnectorTerminationHealthResponseTypeDef(
    _ClientGetVoiceConnectorTerminationHealthResponseTypeDef
):
    """
    - *(dict) --*

      - **TerminationHealth** *(dict) --*

        The termination health details.
        - **Timestamp** *(datetime) --*

          The timestamp, in ISO 8601 format.
    """


_ClientGetVoiceConnectorTerminationResponseTerminationTypeDef = TypedDict(
    "_ClientGetVoiceConnectorTerminationResponseTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)


class ClientGetVoiceConnectorTerminationResponseTerminationTypeDef(
    _ClientGetVoiceConnectorTerminationResponseTerminationTypeDef
):
    """
    - **Termination** *(dict) --*

      The termination setting details.
      - **CpsLimit** *(integer) --*

        The limit on calls per second. Max value based on account service limit. Default value of 1.
    """


_ClientGetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "_ClientGetVoiceConnectorTerminationResponseTypeDef",
    {"Termination": ClientGetVoiceConnectorTerminationResponseTerminationTypeDef},
    total=False,
)


class ClientGetVoiceConnectorTerminationResponseTypeDef(
    _ClientGetVoiceConnectorTerminationResponseTypeDef
):
    """
    - *(dict) --*

      - **Termination** *(dict) --*

        The termination setting details.
        - **CpsLimit** *(integer) --*

          The limit on calls per second. Max value based on account service limit. Default value of
          1.
    """


_ClientInviteUsersResponseInvitesTypeDef = TypedDict(
    "_ClientInviteUsersResponseInvitesTypeDef",
    {
        "InviteId": str,
        "Status": Literal["Pending", "Accepted", "Failed"],
        "EmailAddress": str,
        "EmailStatus": Literal["NotSent", "Sent", "Failed"],
    },
    total=False,
)


class ClientInviteUsersResponseInvitesTypeDef(_ClientInviteUsersResponseInvitesTypeDef):
    """
    - *(dict) --*

      Invitation object returned after emailing users to invite them to join the Amazon Chime
      ``Team`` account.
      - **InviteId** *(string) --*

        The invite ID.
    """


_ClientInviteUsersResponseTypeDef = TypedDict(
    "_ClientInviteUsersResponseTypeDef",
    {"Invites": List[ClientInviteUsersResponseInvitesTypeDef]},
    total=False,
)


class ClientInviteUsersResponseTypeDef(_ClientInviteUsersResponseTypeDef):
    """
    - *(dict) --*

      - **Invites** *(list) --*

        The email invitation details.
        - *(dict) --*

          Invitation object returned after emailing users to invite them to join the Amazon Chime
          ``Team`` account.
          - **InviteId** *(string) --*

            The invite ID.
    """


_ClientListAccountsResponseAccountsTypeDef = TypedDict(
    "_ClientListAccountsResponseAccountsTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
    },
    total=False,
)


class ClientListAccountsResponseAccountsTypeDef(_ClientListAccountsResponseAccountsTypeDef):
    """
    - *(dict) --*

      The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.
      - **AwsAccountId** *(string) --*

        The AWS account ID.
    """


_ClientListAccountsResponseTypeDef = TypedDict(
    "_ClientListAccountsResponseTypeDef",
    {"Accounts": List[ClientListAccountsResponseAccountsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAccountsResponseTypeDef(_ClientListAccountsResponseTypeDef):
    """
    - *(dict) --*

      - **Accounts** *(list) --*

        List of Amazon Chime accounts and account details.
        - *(dict) --*

          The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.
          - **AwsAccountId** *(string) --*

            The AWS account ID.
    """


_ClientListAttendeesResponseAttendeesTypeDef = TypedDict(
    "_ClientListAttendeesResponseAttendeesTypeDef",
    {"ExternalUserId": str, "AttendeeId": str, "JoinToken": str},
    total=False,
)


class ClientListAttendeesResponseAttendeesTypeDef(_ClientListAttendeesResponseAttendeesTypeDef):
    """
    - *(dict) --*

      An Amazon Chime SDK meeting attendee. Includes a unique ``AttendeeId`` and ``JoinToken`` . The
      ``JoinToken`` allows a client to authenticate and join as the specified attendee. The
      ``JoinToken`` expires when the meeting ends or when  DeleteAttendee is called. After that, the
      attendee is unable to join the meeting.
      We recommend securely transferring each ``JoinToken`` from your server application to the
      client so that no other client has access to the token except for the one authorized to
      represent the attendee.
      - **ExternalUserId** *(string) --*

        The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
        builder application.
    """


_ClientListAttendeesResponseTypeDef = TypedDict(
    "_ClientListAttendeesResponseTypeDef",
    {"Attendees": List[ClientListAttendeesResponseAttendeesTypeDef], "NextToken": str},
    total=False,
)


class ClientListAttendeesResponseTypeDef(_ClientListAttendeesResponseTypeDef):
    """
    - *(dict) --*

      - **Attendees** *(list) --*

        The Amazon Chime SDK attendee information.
        - *(dict) --*

          An Amazon Chime SDK meeting attendee. Includes a unique ``AttendeeId`` and ``JoinToken`` .
          The ``JoinToken`` allows a client to authenticate and join as the specified attendee. The
          ``JoinToken`` expires when the meeting ends or when  DeleteAttendee is called. After that,
          the attendee is unable to join the meeting.
          We recommend securely transferring each ``JoinToken`` from your server application to the
          client so that no other client has access to the token except for the one authorized to
          represent the attendee.
          - **ExternalUserId** *(string) --*

            The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a
            builder application.
    """


_ClientListBotsResponseBotsTypeDef = TypedDict(
    "_ClientListBotsResponseBotsTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientListBotsResponseBotsTypeDef(_ClientListBotsResponseBotsTypeDef):
    """
    - *(dict) --*

      A resource that allows Enterprise account administrators to configure an interface to receive
      events from Amazon Chime.
      - **BotId** *(string) --*

        The bot ID.
    """


_ClientListBotsResponseTypeDef = TypedDict(
    "_ClientListBotsResponseTypeDef",
    {"Bots": List[ClientListBotsResponseBotsTypeDef], "NextToken": str},
    total=False,
)


class ClientListBotsResponseTypeDef(_ClientListBotsResponseTypeDef):
    """
    - *(dict) --*

      - **Bots** *(list) --*

        List of bots and bot details.
        - *(dict) --*

          A resource that allows Enterprise account administrators to configure an interface to
          receive events from Amazon Chime.
          - **BotId** *(string) --*

            The bot ID.
    """


_ClientListMeetingsResponseMeetingsMediaPlacementTypeDef = TypedDict(
    "_ClientListMeetingsResponseMeetingsMediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "ScreenDataUrl": str,
        "ScreenSharingUrl": str,
        "ScreenViewingUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
    },
    total=False,
)


class ClientListMeetingsResponseMeetingsMediaPlacementTypeDef(
    _ClientListMeetingsResponseMeetingsMediaPlacementTypeDef
):
    pass


_ClientListMeetingsResponseMeetingsTypeDef = TypedDict(
    "_ClientListMeetingsResponseMeetingsTypeDef",
    {
        "MeetingId": str,
        "MediaPlacement": ClientListMeetingsResponseMeetingsMediaPlacementTypeDef,
        "MediaRegion": str,
    },
    total=False,
)


class ClientListMeetingsResponseMeetingsTypeDef(_ClientListMeetingsResponseMeetingsTypeDef):
    """
    - *(dict) --*

      A meeting created using the Amazon Chime SDK.
      - **MeetingId** *(string) --*

        The Amazon Chime SDK meeting ID.
    """


_ClientListMeetingsResponseTypeDef = TypedDict(
    "_ClientListMeetingsResponseTypeDef",
    {"Meetings": List[ClientListMeetingsResponseMeetingsTypeDef], "NextToken": str},
    total=False,
)


class ClientListMeetingsResponseTypeDef(_ClientListMeetingsResponseTypeDef):
    """
    - *(dict) --*

      - **Meetings** *(list) --*

        The Amazon Chime SDK meeting information.
        - *(dict) --*

          A meeting created using the Amazon Chime SDK.
          - **MeetingId** *(string) --*

            The Amazon Chime SDK meeting ID.
    """


_ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef = TypedDict(
    "_ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef",
    {"E164PhoneNumber": str, "Status": Literal["Processing", "Acquired", "Failed"]},
    total=False,
)


class ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef(
    _ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef
):
    pass


_ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef = TypedDict(
    "_ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal["Processing", "Successful", "Failed", "Partial"],
        "OrderedPhoneNumbers": List[
            ClientListPhoneNumberOrdersResponsePhoneNumberOrdersOrderedPhoneNumbersTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef(
    _ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef
):
    """
    - *(dict) --*

      The details of a phone number order created for Amazon Chime.
      - **PhoneNumberOrderId** *(string) --*

        The phone number order ID.
    """


_ClientListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "_ClientListPhoneNumberOrdersResponseTypeDef",
    {
        "PhoneNumberOrders": List[ClientListPhoneNumberOrdersResponsePhoneNumberOrdersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListPhoneNumberOrdersResponseTypeDef(_ClientListPhoneNumberOrdersResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumberOrders** *(list) --*

        The phone number order details.
        - *(dict) --*

          The details of a phone number order created for Amazon Chime.
          - **PhoneNumberOrderId** *(string) --*

            The phone number order ID.
    """


_ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef",
    {
        "Value": str,
        "Name": Literal["AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)


class ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef(
    _ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef
):
    pass


_ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)


class ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef(
    _ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef
):
    pass


_ClientListPhoneNumbersResponsePhoneNumbersTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponsePhoneNumbersTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": ClientListPhoneNumbersResponsePhoneNumbersCapabilitiesTypeDef,
        "Associations": List[ClientListPhoneNumbersResponsePhoneNumbersAssociationsTypeDef],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ClientListPhoneNumbersResponsePhoneNumbersTypeDef(
    _ClientListPhoneNumbersResponsePhoneNumbersTypeDef
):
    """
    - *(dict) --*

      A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.
      - **PhoneNumberId** *(string) --*

        The phone number ID.
    """


_ClientListPhoneNumbersResponseTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponseTypeDef",
    {"PhoneNumbers": List[ClientListPhoneNumbersResponsePhoneNumbersTypeDef], "NextToken": str},
    total=False,
)


class ClientListPhoneNumbersResponseTypeDef(_ClientListPhoneNumbersResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumbers** *(list) --*

        The phone number details.
        - *(dict) --*

          A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.
          - **PhoneNumberId** *(string) --*

            The phone number ID.
    """


_ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef = TypedDict(
    "_ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": Literal["User", "Bot", "Webhook"],
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)


class ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef(
    _ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef
):
    pass


_ClientListRoomMembershipsResponseRoomMembershipsTypeDef = TypedDict(
    "_ClientListRoomMembershipsResponseRoomMembershipsTypeDef",
    {
        "RoomId": str,
        "Member": ClientListRoomMembershipsResponseRoomMembershipsMemberTypeDef,
        "Role": Literal["Administrator", "Member"],
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListRoomMembershipsResponseRoomMembershipsTypeDef(
    _ClientListRoomMembershipsResponseRoomMembershipsTypeDef
):
    """
    - *(dict) --*

      The room membership details.
      - **RoomId** *(string) --*

        The room ID.
    """


_ClientListRoomMembershipsResponseTypeDef = TypedDict(
    "_ClientListRoomMembershipsResponseTypeDef",
    {
        "RoomMemberships": List[ClientListRoomMembershipsResponseRoomMembershipsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListRoomMembershipsResponseTypeDef(_ClientListRoomMembershipsResponseTypeDef):
    """
    - *(dict) --*

      - **RoomMemberships** *(list) --*

        The room membership details.
        - *(dict) --*

          The room membership details.
          - **RoomId** *(string) --*

            The room ID.
    """


_ClientListRoomsResponseRoomsTypeDef = TypedDict(
    "_ClientListRoomsResponseRoomsTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListRoomsResponseRoomsTypeDef(_ClientListRoomsResponseRoomsTypeDef):
    """
    - *(dict) --*

      The Amazon Chime chat room details.
      - **RoomId** *(string) --*

        The room ID.
    """


_ClientListRoomsResponseTypeDef = TypedDict(
    "_ClientListRoomsResponseTypeDef",
    {"Rooms": List[ClientListRoomsResponseRoomsTypeDef], "NextToken": str},
    total=False,
)


class ClientListRoomsResponseTypeDef(_ClientListRoomsResponseTypeDef):
    """
    - *(dict) --*

      - **Rooms** *(list) --*

        The room details.
        - *(dict) --*

          The Amazon Chime chat room details.
          - **RoomId** *(string) --*

            The room ID.
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    - *(dict) --*

      The user on the Amazon Chime account.
      - **UserId** *(string) --*

        The user ID.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        List of users and user details.
        - *(dict) --*

          The user on the Amazon Chime account.
          - **UserId** *(string) --*

            The user ID.
    """


_ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)


class ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef(
    _ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef
):
    pass


_ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef = TypedDict(
    "_ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef(
    _ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef
):
    """
    - *(dict) --*

      The Amazon Chime Voice Connector group configuration, including associated Amazon Chime Voice
      Connectors. You can include Amazon Chime Voice Connectors from different AWS Regions in your
      group. This creates a fault tolerant mechanism for fallback in case of availability events.
      - **VoiceConnectorGroupId** *(string) --*

        The Amazon Chime Voice Connector group ID.
    """


_ClientListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "_ClientListVoiceConnectorGroupsResponseTypeDef",
    {
        "VoiceConnectorGroups": List[
            ClientListVoiceConnectorGroupsResponseVoiceConnectorGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListVoiceConnectorGroupsResponseTypeDef(_ClientListVoiceConnectorGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **VoiceConnectorGroups** *(list) --*

        The details of the Amazon Chime Voice Connector groups.
        - *(dict) --*

          The Amazon Chime Voice Connector group configuration, including associated Amazon Chime
          Voice Connectors. You can include Amazon Chime Voice Connectors from different AWS Regions
          in your group. This creates a fault tolerant mechanism for fallback in case of
          availability events.
          - **VoiceConnectorGroupId** *(string) --*

            The Amazon Chime Voice Connector group ID.
    """


_ClientListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "_ClientListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {"Usernames": List[str]},
    total=False,
)


class ClientListVoiceConnectorTerminationCredentialsResponseTypeDef(
    _ClientListVoiceConnectorTerminationCredentialsResponseTypeDef
):
    """
    - *(dict) --*

      - **Usernames** *(list) --*

        A list of user names.
        - *(string) --*
    """


_ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef = TypedDict(
    "_ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef(
    _ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef
):
    """
    - *(dict) --*

      The Amazon Chime Voice Connector configuration, including outbound host name and encryption
      settings.
      - **VoiceConnectorId** *(string) --*

        The Amazon Chime Voice Connector ID.
    """


_ClientListVoiceConnectorsResponseTypeDef = TypedDict(
    "_ClientListVoiceConnectorsResponseTypeDef",
    {
        "VoiceConnectors": List[ClientListVoiceConnectorsResponseVoiceConnectorsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListVoiceConnectorsResponseTypeDef(_ClientListVoiceConnectorsResponseTypeDef):
    """
    - *(dict) --*

      - **VoiceConnectors** *(list) --*

        The details of the Amazon Chime Voice Connectors.
        - *(dict) --*

          The Amazon Chime Voice Connector configuration, including outbound host name and
          encryption settings.
          - **VoiceConnectorId** *(string) --*

            The Amazon Chime Voice Connector ID.
    """


_ClientPutEventsConfigurationResponseEventsConfigurationTypeDef = TypedDict(
    "_ClientPutEventsConfigurationResponseEventsConfigurationTypeDef",
    {"BotId": str, "OutboundEventsHTTPSEndpoint": str, "LambdaFunctionArn": str},
    total=False,
)


class ClientPutEventsConfigurationResponseEventsConfigurationTypeDef(
    _ClientPutEventsConfigurationResponseEventsConfigurationTypeDef
):
    """
    - **EventsConfiguration** *(dict) --*

      The configuration that allows a bot to receive outgoing events. Can be either an HTTPS
      endpoint or a Lambda function ARN.
      - **BotId** *(string) --*

        The bot ID.
    """


_ClientPutEventsConfigurationResponseTypeDef = TypedDict(
    "_ClientPutEventsConfigurationResponseTypeDef",
    {"EventsConfiguration": ClientPutEventsConfigurationResponseEventsConfigurationTypeDef},
    total=False,
)


class ClientPutEventsConfigurationResponseTypeDef(_ClientPutEventsConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **EventsConfiguration** *(dict) --*

        The configuration that allows a bot to receive outgoing events. Can be either an HTTPS
        endpoint or a Lambda function ARN.
        - **BotId** *(string) --*

          The bot ID.
    """


_ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)


class ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef(
    _ClientPutVoiceConnectorLoggingConfigurationLoggingConfigurationTypeDef
):
    """
    The logging configuration details to add.
    - **EnableSIPLogs** *(boolean) --*

      When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {"EnableSIPLogs": bool},
    total=False,
)


class ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef(
    _ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
):
    """
    - **LoggingConfiguration** *(dict) --*

      The updated logging configuration details.
      - **EnableSIPLogs** *(boolean) --*

        When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "_ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": ClientPutVoiceConnectorLoggingConfigurationResponseLoggingConfigurationTypeDef
    },
    total=False,
)


class ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef(
    _ClientPutVoiceConnectorLoggingConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **LoggingConfiguration** *(dict) --*

        The updated logging configuration details.
        - **EnableSIPLogs** *(boolean) --*

          When true, enables SIP message logs for sending to Amazon CloudWatch Logs.
    """


_ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": Literal["TCP", "UDP"], "Priority": int, "Weight": int},
    total=False,
)


class ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef(
    _ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef
):
    """
    - *(dict) --*

      Origination routes define call distribution properties for your SIP hosts to receive inbound
      calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon
      Chime Voice Connector.
      - **Host** *(string) --*

        The FQDN or IP address to contact for origination traffic.
    """


_ClientPutVoiceConnectorOriginationOriginationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationOriginationTypeDef",
    {"Routes": List[ClientPutVoiceConnectorOriginationOriginationRoutesTypeDef], "Disabled": bool},
    total=False,
)


class ClientPutVoiceConnectorOriginationOriginationTypeDef(
    _ClientPutVoiceConnectorOriginationOriginationTypeDef
):
    """
    The origination setting details to add.
    - **Routes** *(list) --*

      The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1.
      Maximum value of 20.
      - *(dict) --*

        Origination routes define call distribution properties for your SIP hosts to receive inbound
        calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon
        Chime Voice Connector.
        - **Host** *(string) --*

          The FQDN or IP address to contact for origination traffic.
    """


_ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef",
    {"Host": str, "Port": int, "Protocol": Literal["TCP", "UDP"], "Priority": int, "Weight": int},
    total=False,
)


class ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef(
    _ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef
):
    """
    - *(dict) --*

      Origination routes define call distribution properties for your SIP hosts to receive inbound
      calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon
      Chime Voice Connector.
      - **Host** *(string) --*

        The FQDN or IP address to contact for origination traffic.
    """


_ClientPutVoiceConnectorOriginationResponseOriginationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationResponseOriginationTypeDef",
    {
        "Routes": List[ClientPutVoiceConnectorOriginationResponseOriginationRoutesTypeDef],
        "Disabled": bool,
    },
    total=False,
)


class ClientPutVoiceConnectorOriginationResponseOriginationTypeDef(
    _ClientPutVoiceConnectorOriginationResponseOriginationTypeDef
):
    """
    - **Origination** *(dict) --*

      The updated origination setting details.
      - **Routes** *(list) --*

        The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
        1. Maximum value of 20.
        - *(dict) --*

          Origination routes define call distribution properties for your SIP hosts to receive
          inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
          each Amazon Chime Voice Connector.
          - **Host** *(string) --*

            The FQDN or IP address to contact for origination traffic.
    """


_ClientPutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "_ClientPutVoiceConnectorOriginationResponseTypeDef",
    {"Origination": ClientPutVoiceConnectorOriginationResponseOriginationTypeDef},
    total=False,
)


class ClientPutVoiceConnectorOriginationResponseTypeDef(
    _ClientPutVoiceConnectorOriginationResponseTypeDef
):
    """
    - *(dict) --*

      - **Origination** *(dict) --*

        The updated origination setting details.
        - **Routes** *(list) --*

          The call distribution properties defined for your SIP hosts. Valid range: Minimum value of
          1. Maximum value of 20.
          - *(dict) --*

            Origination routes define call distribution properties for your SIP hosts to receive
            inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for
            each Amazon Chime Voice Connector.
            - **Host** *(string) --*

              The FQDN or IP address to contact for origination traffic.
    """


_ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int, "Disabled": bool},
    total=False,
)


class ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef(
    _ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
):
    """
    - **StreamingConfiguration** *(dict) --*

      The updated streaming configuration details.
      - **DataRetentionInHours** *(integer) --*

        The retention period, in hours, for the Amazon Kinesis data.
    """


_ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "_ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": ClientPutVoiceConnectorStreamingConfigurationResponseStreamingConfigurationTypeDef
    },
    total=False,
)


class ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef(
    _ClientPutVoiceConnectorStreamingConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **StreamingConfiguration** *(dict) --*

        The updated streaming configuration details.
        - **DataRetentionInHours** *(integer) --*

          The retention period, in hours, for the Amazon Kinesis data.
    """


_RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef = TypedDict(
    "_RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    {"DataRetentionInHours": int},
)
_OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef = TypedDict(
    "_OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef",
    {"Disabled": bool},
    total=False,
)


class ClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef(
    _RequiredClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
    _OptionalClientPutVoiceConnectorStreamingConfigurationStreamingConfigurationTypeDef,
):
    """
    The streaming configuration details to add.
    - **DataRetentionInHours** *(integer) --***[REQUIRED]**

      The retention period, in hours, for the Amazon Kinesis data.
    """


_ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef = TypedDict(
    "_ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef",
    {"Username": str, "Password": str},
    total=False,
)


class ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef(
    _ClientPutVoiceConnectorTerminationCredentialsCredentialsTypeDef
):
    """
    - *(dict) --*

      The SIP credentials used to authenticate requests to your Amazon Chime Voice Connector.
      - **Username** *(string) --*

        The RFC2617 compliant user name associated with the SIP credentials, in US-ASCII format.
    """


_ClientPutVoiceConnectorTerminationResponseTerminationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorTerminationResponseTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)


class ClientPutVoiceConnectorTerminationResponseTerminationTypeDef(
    _ClientPutVoiceConnectorTerminationResponseTerminationTypeDef
):
    """
    - **Termination** *(dict) --*

      The updated termination setting details.
      - **CpsLimit** *(integer) --*

        The limit on calls per second. Max value based on account service limit. Default value of 1.
    """


_ClientPutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "_ClientPutVoiceConnectorTerminationResponseTypeDef",
    {"Termination": ClientPutVoiceConnectorTerminationResponseTerminationTypeDef},
    total=False,
)


class ClientPutVoiceConnectorTerminationResponseTypeDef(
    _ClientPutVoiceConnectorTerminationResponseTypeDef
):
    """
    - *(dict) --*

      - **Termination** *(dict) --*

        The updated termination setting details.
        - **CpsLimit** *(integer) --*

          The limit on calls per second. Max value based on account service limit. Default value of
          1.
    """


_ClientPutVoiceConnectorTerminationTerminationTypeDef = TypedDict(
    "_ClientPutVoiceConnectorTerminationTerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)


class ClientPutVoiceConnectorTerminationTerminationTypeDef(
    _ClientPutVoiceConnectorTerminationTerminationTypeDef
):
    """
    The termination setting details to add.
    - **CpsLimit** *(integer) --*

      The limit on calls per second. Max value based on account service limit. Default value of 1.
    """


_ClientRegenerateSecurityTokenResponseBotTypeDef = TypedDict(
    "_ClientRegenerateSecurityTokenResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientRegenerateSecurityTokenResponseBotTypeDef(
    _ClientRegenerateSecurityTokenResponseBotTypeDef
):
    """
    - **Bot** *(dict) --*

      A resource that allows Enterprise account administrators to configure an interface to receive
      events from Amazon Chime.
      - **BotId** *(string) --*

        The bot ID.
    """


_ClientRegenerateSecurityTokenResponseTypeDef = TypedDict(
    "_ClientRegenerateSecurityTokenResponseTypeDef",
    {"Bot": ClientRegenerateSecurityTokenResponseBotTypeDef},
    total=False,
)


class ClientRegenerateSecurityTokenResponseTypeDef(_ClientRegenerateSecurityTokenResponseTypeDef):
    """
    - *(dict) --*

      - **Bot** *(dict) --*

        A resource that allows Enterprise account administrators to configure an interface to
        receive events from Amazon Chime.
        - **BotId** *(string) --*

          The bot ID.
    """


_ClientResetPersonalPinResponseUserTypeDef = TypedDict(
    "_ClientResetPersonalPinResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ClientResetPersonalPinResponseUserTypeDef(_ClientResetPersonalPinResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The user details and new personal meeting PIN.
      - **UserId** *(string) --*

        The user ID.
    """


_ClientResetPersonalPinResponseTypeDef = TypedDict(
    "_ClientResetPersonalPinResponseTypeDef",
    {"User": ClientResetPersonalPinResponseUserTypeDef},
    total=False,
)


class ClientResetPersonalPinResponseTypeDef(_ClientResetPersonalPinResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The user details and new personal meeting PIN.
        - **UserId** *(string) --*

          The user ID.
    """


_ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "_ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {
        "Value": str,
        "Name": Literal["AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)


class ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef(
    _ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef
):
    pass


_ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "_ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)


class ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef(
    _ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef
):
    pass


_ClientRestorePhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "_ClientRestorePhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": ClientRestorePhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[ClientRestorePhoneNumberResponsePhoneNumberAssociationsTypeDef],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ClientRestorePhoneNumberResponsePhoneNumberTypeDef(
    _ClientRestorePhoneNumberResponsePhoneNumberTypeDef
):
    """
    - **PhoneNumber** *(dict) --*

      The phone number details.
      - **PhoneNumberId** *(string) --*

        The phone number ID.
    """


_ClientRestorePhoneNumberResponseTypeDef = TypedDict(
    "_ClientRestorePhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientRestorePhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)


class ClientRestorePhoneNumberResponseTypeDef(_ClientRestorePhoneNumberResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumber** *(dict) --*

        The phone number details.
        - **PhoneNumberId** *(string) --*

          The phone number ID.
    """


_ClientSearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "_ClientSearchAvailablePhoneNumbersResponseTypeDef",
    {"E164PhoneNumbers": List[str]},
    total=False,
)


class ClientSearchAvailablePhoneNumbersResponseTypeDef(
    _ClientSearchAvailablePhoneNumbersResponseTypeDef
):
    """
    - *(dict) --*

      - **E164PhoneNumbers** *(list) --*

        List of phone numbers, in E.164 format.
        - *(string) --*
    """


_ClientUpdateAccountResponseAccountTypeDef = TypedDict(
    "_ClientUpdateAccountResponseAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
    },
    total=False,
)


class ClientUpdateAccountResponseAccountTypeDef(_ClientUpdateAccountResponseAccountTypeDef):
    """
    - **Account** *(dict) --*

      The updated Amazon Chime account details.
      - **AwsAccountId** *(string) --*

        The AWS account ID.
    """


_ClientUpdateAccountResponseTypeDef = TypedDict(
    "_ClientUpdateAccountResponseTypeDef",
    {"Account": ClientUpdateAccountResponseAccountTypeDef},
    total=False,
)


class ClientUpdateAccountResponseTypeDef(_ClientUpdateAccountResponseTypeDef):
    """
    - *(dict) --*

      - **Account** *(dict) --*

        The updated Amazon Chime account details.
        - **AwsAccountId** *(string) --*

          The AWS account ID.
    """


_ClientUpdateAccountSettingsAccountSettingsTypeDef = TypedDict(
    "_ClientUpdateAccountSettingsAccountSettingsTypeDef",
    {"DisableRemoteControl": bool, "EnableDialOut": bool},
    total=False,
)


class ClientUpdateAccountSettingsAccountSettingsTypeDef(
    _ClientUpdateAccountSettingsAccountSettingsTypeDef
):
    """
    The Amazon Chime account settings to update.
    - **DisableRemoteControl** *(boolean) --*

      Setting that stops or starts remote control of shared screens during meetings.
    """


_ClientUpdateBotResponseBotTypeDef = TypedDict(
    "_ClientUpdateBotResponseBotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": str,
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)


class ClientUpdateBotResponseBotTypeDef(_ClientUpdateBotResponseBotTypeDef):
    """
    - **Bot** *(dict) --*

      The updated bot details.
      - **BotId** *(string) --*

        The bot ID.
    """


_ClientUpdateBotResponseTypeDef = TypedDict(
    "_ClientUpdateBotResponseTypeDef", {"Bot": ClientUpdateBotResponseBotTypeDef}, total=False
)


class ClientUpdateBotResponseTypeDef(_ClientUpdateBotResponseTypeDef):
    """
    - *(dict) --*

      - **Bot** *(dict) --*

        The updated bot details.
        - **BotId** *(string) --*

          The bot ID.
    """


_ClientUpdateGlobalSettingsBusinessCallingTypeDef = TypedDict(
    "_ClientUpdateGlobalSettingsBusinessCallingTypeDef", {"CdrBucket": str}, total=False
)


class ClientUpdateGlobalSettingsBusinessCallingTypeDef(
    _ClientUpdateGlobalSettingsBusinessCallingTypeDef
):
    """
    The Amazon Chime Business Calling settings.
    - **CdrBucket** *(string) --*

      The Amazon S3 bucket designated for call detail record storage.
    """


_ClientUpdateGlobalSettingsVoiceConnectorTypeDef = TypedDict(
    "_ClientUpdateGlobalSettingsVoiceConnectorTypeDef", {"CdrBucket": str}, total=False
)


class ClientUpdateGlobalSettingsVoiceConnectorTypeDef(
    _ClientUpdateGlobalSettingsVoiceConnectorTypeDef
):
    """
    The Amazon Chime Voice Connector settings.
    - **CdrBucket** *(string) --*

      The Amazon S3 bucket designated for call detail record storage.
    """


_ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef = TypedDict(
    "_ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef",
    {
        "Value": str,
        "Name": Literal["AccountId", "UserId", "VoiceConnectorId", "VoiceConnectorGroupId"],
        "AssociatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef(
    _ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef
):
    pass


_ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef = TypedDict(
    "_ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)


class ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef(
    _ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef
):
    pass


_ClientUpdatePhoneNumberResponsePhoneNumberTypeDef = TypedDict(
    "_ClientUpdatePhoneNumberResponsePhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Type": Literal["Local", "TollFree"],
        "ProductType": Literal["BusinessCalling", "VoiceConnector"],
        "Status": Literal[
            "AcquireInProgress",
            "AcquireFailed",
            "Unassigned",
            "Assigned",
            "ReleaseInProgress",
            "DeleteInProgress",
            "ReleaseFailed",
            "DeleteFailed",
        ],
        "Capabilities": ClientUpdatePhoneNumberResponsePhoneNumberCapabilitiesTypeDef,
        "Associations": List[ClientUpdatePhoneNumberResponsePhoneNumberAssociationsTypeDef],
        "CallingName": str,
        "CallingNameStatus": Literal[
            "Unassigned", "UpdateInProgress", "UpdateSucceeded", "UpdateFailed"
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ClientUpdatePhoneNumberResponsePhoneNumberTypeDef(
    _ClientUpdatePhoneNumberResponsePhoneNumberTypeDef
):
    """
    - **PhoneNumber** *(dict) --*

      The updated phone number details.
      - **PhoneNumberId** *(string) --*

        The phone number ID.
    """


_ClientUpdatePhoneNumberResponseTypeDef = TypedDict(
    "_ClientUpdatePhoneNumberResponseTypeDef",
    {"PhoneNumber": ClientUpdatePhoneNumberResponsePhoneNumberTypeDef},
    total=False,
)


class ClientUpdatePhoneNumberResponseTypeDef(_ClientUpdatePhoneNumberResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumber** *(dict) --*

        The updated phone number details.
        - **PhoneNumberId** *(string) --*

          The phone number ID.
    """


_ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef = TypedDict(
    "_ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": Literal["User", "Bot", "Webhook"],
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)


class ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef(
    _ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef
):
    pass


_ClientUpdateRoomMembershipResponseRoomMembershipTypeDef = TypedDict(
    "_ClientUpdateRoomMembershipResponseRoomMembershipTypeDef",
    {
        "RoomId": str,
        "Member": ClientUpdateRoomMembershipResponseRoomMembershipMemberTypeDef,
        "Role": Literal["Administrator", "Member"],
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateRoomMembershipResponseRoomMembershipTypeDef(
    _ClientUpdateRoomMembershipResponseRoomMembershipTypeDef
):
    """
    - **RoomMembership** *(dict) --*

      The room membership details.
      - **RoomId** *(string) --*

        The room ID.
    """


_ClientUpdateRoomMembershipResponseTypeDef = TypedDict(
    "_ClientUpdateRoomMembershipResponseTypeDef",
    {"RoomMembership": ClientUpdateRoomMembershipResponseRoomMembershipTypeDef},
    total=False,
)


class ClientUpdateRoomMembershipResponseTypeDef(_ClientUpdateRoomMembershipResponseTypeDef):
    """
    - *(dict) --*

      - **RoomMembership** *(dict) --*

        The room membership details.
        - **RoomId** *(string) --*

          The room ID.
    """


_ClientUpdateRoomResponseRoomTypeDef = TypedDict(
    "_ClientUpdateRoomResponseRoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateRoomResponseRoomTypeDef(_ClientUpdateRoomResponseRoomTypeDef):
    """
    - **Room** *(dict) --*

      The room details.
      - **RoomId** *(string) --*

        The room ID.
    """


_ClientUpdateRoomResponseTypeDef = TypedDict(
    "_ClientUpdateRoomResponseTypeDef", {"Room": ClientUpdateRoomResponseRoomTypeDef}, total=False
)


class ClientUpdateRoomResponseTypeDef(_ClientUpdateRoomResponseTypeDef):
    """
    - *(dict) --*

      - **Room** *(dict) --*

        The room details.
        - **RoomId** *(string) --*

          The room ID.
    """


_ClientUpdateUserResponseUserTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ClientUpdateUserResponseUserTypeDef(_ClientUpdateUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The updated user details.
      - **UserId** *(string) --*

        The user ID.
    """


_ClientUpdateUserResponseTypeDef = TypedDict(
    "_ClientUpdateUserResponseTypeDef", {"User": ClientUpdateUserResponseUserTypeDef}, total=False
)


class ClientUpdateUserResponseTypeDef(_ClientUpdateUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The updated user details.
        - **UserId** *(string) --*

          The user ID.
    """


_RequiredClientUpdateUserSettingsUserSettingsTelephonyTypeDef = TypedDict(
    "_RequiredClientUpdateUserSettingsUserSettingsTelephonyTypeDef", {"InboundCalling": bool}
)
_OptionalClientUpdateUserSettingsUserSettingsTelephonyTypeDef = TypedDict(
    "_OptionalClientUpdateUserSettingsUserSettingsTelephonyTypeDef",
    {"OutboundCalling": bool, "SMS": bool},
    total=False,
)


class ClientUpdateUserSettingsUserSettingsTelephonyTypeDef(
    _RequiredClientUpdateUserSettingsUserSettingsTelephonyTypeDef,
    _OptionalClientUpdateUserSettingsUserSettingsTelephonyTypeDef,
):
    """
    - **Telephony** *(dict) --***[REQUIRED]**

      The telephony settings associated with the user.
      - **InboundCalling** *(boolean) --***[REQUIRED]**

        Allows or denies inbound calling.
    """


_ClientUpdateUserSettingsUserSettingsTypeDef = TypedDict(
    "_ClientUpdateUserSettingsUserSettingsTypeDef",
    {"Telephony": ClientUpdateUserSettingsUserSettingsTelephonyTypeDef},
)


class ClientUpdateUserSettingsUserSettingsTypeDef(_ClientUpdateUserSettingsUserSettingsTypeDef):
    """
    The user settings to update.
    - **Telephony** *(dict) --***[REQUIRED]**

      The telephony settings associated with the user.
      - **InboundCalling** *(boolean) --***[REQUIRED]**

        Allows or denies inbound calling.
    """


_ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"VoiceConnectorId": str, "Priority": int},
    total=False,
)


class ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
):
    pass


_ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[
            ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupVoiceConnectorItemsTypeDef
        ],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef(
    _ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef
):
    """
    - **VoiceConnectorGroup** *(dict) --*

      The updated Amazon Chime Voice Connector group details.
      - **VoiceConnectorGroupId** *(string) --*

        The Amazon Chime Voice Connector group ID.
    """


_ClientUpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorGroupResponseTypeDef",
    {"VoiceConnectorGroup": ClientUpdateVoiceConnectorGroupResponseVoiceConnectorGroupTypeDef},
    total=False,
)


class ClientUpdateVoiceConnectorGroupResponseTypeDef(
    _ClientUpdateVoiceConnectorGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **VoiceConnectorGroup** *(dict) --*

        The updated Amazon Chime Voice Connector group details.
        - **VoiceConnectorGroupId** *(string) --*

          The Amazon Chime Voice Connector group ID.
    """


_RequiredClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_RequiredClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef", {"VoiceConnectorId": str}
)
_OptionalClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef = TypedDict(
    "_OptionalClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef",
    {"Priority": int},
    total=False,
)


class ClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef(
    _RequiredClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
    _OptionalClientUpdateVoiceConnectorGroupVoiceConnectorItemsTypeDef,
):
    """
    - *(dict) --*

      For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route
      inbound calls. Includes priority configuration settings. Limit: 3 ``VoiceConnectorItems`` per
      Amazon Chime Voice Connector group.
      - **VoiceConnectorId** *(string) --***[REQUIRED]**

        The Amazon Chime Voice Connector ID.
    """


_ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": Literal["us-east-1", "us-west-2"],
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef(
    _ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef
):
    """
    - **VoiceConnector** *(dict) --*

      The updated Amazon Chime Voice Connector details.
      - **VoiceConnectorId** *(string) --*

        The Amazon Chime Voice Connector ID.
    """


_ClientUpdateVoiceConnectorResponseTypeDef = TypedDict(
    "_ClientUpdateVoiceConnectorResponseTypeDef",
    {"VoiceConnector": ClientUpdateVoiceConnectorResponseVoiceConnectorTypeDef},
    total=False,
)


class ClientUpdateVoiceConnectorResponseTypeDef(_ClientUpdateVoiceConnectorResponseTypeDef):
    """
    - *(dict) --*

      - **VoiceConnector** *(dict) --*

        The updated Amazon Chime Voice Connector details.
        - **VoiceConnectorId** *(string) --*

          The Amazon Chime Voice Connector ID.
    """


_ListAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountsPaginatePaginationConfigTypeDef(_ListAccountsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAccountsPaginateResponseAccountsTypeDef = TypedDict(
    "_ListAccountsPaginateResponseAccountsTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": Literal["Team", "EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC"],
        "CreatedTimestamp": datetime,
        "DefaultLicense": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "SupportedLicenses": List[Literal["Basic", "Plus", "Pro", "ProTrial"]],
    },
    total=False,
)


class ListAccountsPaginateResponseAccountsTypeDef(_ListAccountsPaginateResponseAccountsTypeDef):
    """
    - *(dict) --*

      The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.
      - **AwsAccountId** *(string) --*

        The AWS account ID.
    """


_ListAccountsPaginateResponseTypeDef = TypedDict(
    "_ListAccountsPaginateResponseTypeDef",
    {"Accounts": List[ListAccountsPaginateResponseAccountsTypeDef]},
    total=False,
)


class ListAccountsPaginateResponseTypeDef(_ListAccountsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Accounts** *(list) --*

        List of Amazon Chime accounts and account details.
        - *(dict) --*

          The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.
          - **AwsAccountId** *(string) --*

            The AWS account ID.
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


_ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTypeDef",
    {
        "UserId": str,
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": Literal["Basic", "Plus", "Pro", "ProTrial"],
        "UserRegistrationStatus": Literal["Unregistered", "Registered", "Suspended"],
        "UserInvitationStatus": Literal["Pending", "Accepted", "Failed"],
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "PersonalPIN": str,
    },
    total=False,
)


class ListUsersPaginateResponseUsersTypeDef(_ListUsersPaginateResponseUsersTypeDef):
    """
    - *(dict) --*

      The user on the Amazon Chime account.
      - **UserId** *(string) --*

        The user ID.
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef]},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        List of users and user details.
        - *(dict) --*

          The user on the Amazon Chime account.
          - **UserId** *(string) --*

            The user ID.
    """
