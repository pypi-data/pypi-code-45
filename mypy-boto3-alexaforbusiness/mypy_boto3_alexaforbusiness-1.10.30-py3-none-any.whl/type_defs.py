"Main interface for alexaforbusiness service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAddressBookResponseTypeDef",
    "ClientCreateBusinessReportScheduleContentRangeTypeDef",
    "ClientCreateBusinessReportScheduleRecurrenceTypeDef",
    "ClientCreateBusinessReportScheduleResponseTypeDef",
    "ClientCreateConferenceProviderIPDialInTypeDef",
    "ClientCreateConferenceProviderMeetingSettingTypeDef",
    "ClientCreateConferenceProviderPSTNDialInTypeDef",
    "ClientCreateConferenceProviderResponseTypeDef",
    "ClientCreateContactPhoneNumbersTypeDef",
    "ClientCreateContactResponseTypeDef",
    "ClientCreateContactSipAddressesTypeDef",
    "ClientCreateGatewayGroupResponseTypeDef",
    "ClientCreateNetworkProfileResponseTypeDef",
    "ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    "ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef",
    "ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    "ClientCreateProfileMeetingRoomConfigurationTypeDef",
    "ClientCreateProfileResponseTypeDef",
    "ClientCreateRoomResponseTypeDef",
    "ClientCreateRoomTagsTypeDef",
    "ClientCreateSkillGroupResponseTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientGetAddressBookResponseAddressBookTypeDef",
    "ClientGetAddressBookResponseTypeDef",
    "ClientGetConferencePreferenceResponsePreferenceTypeDef",
    "ClientGetConferencePreferenceResponseTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef",
    "ClientGetConferenceProviderResponseConferenceProviderTypeDef",
    "ClientGetConferenceProviderResponseTypeDef",
    "ClientGetContactResponseContactPhoneNumbersTypeDef",
    "ClientGetContactResponseContactSipAddressesTypeDef",
    "ClientGetContactResponseContactTypeDef",
    "ClientGetContactResponseTypeDef",
    "ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef",
    "ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef",
    "ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef",
    "ClientGetDeviceResponseDeviceTypeDef",
    "ClientGetDeviceResponseTypeDef",
    "ClientGetGatewayGroupResponseGatewayGroupTypeDef",
    "ClientGetGatewayGroupResponseTypeDef",
    "ClientGetGatewayResponseGatewayTypeDef",
    "ClientGetGatewayResponseTypeDef",
    "ClientGetInvitationConfigurationResponseTypeDef",
    "ClientGetNetworkProfileResponseNetworkProfileTypeDef",
    "ClientGetNetworkProfileResponseTypeDef",
    "ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    "ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef",
    "ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    "ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef",
    "ClientGetProfileResponseProfileTypeDef",
    "ClientGetProfileResponseTypeDef",
    "ClientGetRoomResponseRoomTypeDef",
    "ClientGetRoomResponseTypeDef",
    "ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef",
    "ClientGetRoomSkillParameterResponseTypeDef",
    "ClientGetSkillGroupResponseSkillGroupTypeDef",
    "ClientGetSkillGroupResponseTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef",
    "ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef",
    "ClientListBusinessReportSchedulesResponseTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef",
    "ClientListConferenceProvidersResponseConferenceProvidersTypeDef",
    "ClientListConferenceProvidersResponseTypeDef",
    "ClientListDeviceEventsResponseDeviceEventsTypeDef",
    "ClientListDeviceEventsResponseTypeDef",
    "ClientListGatewayGroupsResponseGatewayGroupsTypeDef",
    "ClientListGatewayGroupsResponseTypeDef",
    "ClientListGatewaysResponseGatewaysTypeDef",
    "ClientListGatewaysResponseTypeDef",
    "ClientListSkillsResponseSkillSummariesTypeDef",
    "ClientListSkillsResponseTypeDef",
    "ClientListSkillsStoreCategoriesResponseCategoryListTypeDef",
    "ClientListSkillsStoreCategoriesResponseTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef",
    "ClientListSkillsStoreSkillsByCategoryResponseTypeDef",
    "ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef",
    "ClientListSmartHomeAppliancesResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientPutConferencePreferenceConferencePreferenceTypeDef",
    "ClientPutRoomSkillParameterRoomSkillParameterTypeDef",
    "ClientRegisterAvsDeviceResponseTypeDef",
    "ClientResolveRoomResponseRoomSkillParametersTypeDef",
    "ClientResolveRoomResponseTypeDef",
    "ClientSearchAddressBooksFiltersTypeDef",
    "ClientSearchAddressBooksResponseAddressBooksTypeDef",
    "ClientSearchAddressBooksResponseTypeDef",
    "ClientSearchAddressBooksSortCriteriaTypeDef",
    "ClientSearchContactsFiltersTypeDef",
    "ClientSearchContactsResponseContactsPhoneNumbersTypeDef",
    "ClientSearchContactsResponseContactsSipAddressesTypeDef",
    "ClientSearchContactsResponseContactsTypeDef",
    "ClientSearchContactsResponseTypeDef",
    "ClientSearchContactsSortCriteriaTypeDef",
    "ClientSearchDevicesFiltersTypeDef",
    "ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    "ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef",
    "ClientSearchDevicesResponseDevicesTypeDef",
    "ClientSearchDevicesResponseTypeDef",
    "ClientSearchDevicesSortCriteriaTypeDef",
    "ClientSearchNetworkProfilesFiltersTypeDef",
    "ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef",
    "ClientSearchNetworkProfilesResponseTypeDef",
    "ClientSearchNetworkProfilesSortCriteriaTypeDef",
    "ClientSearchProfilesFiltersTypeDef",
    "ClientSearchProfilesResponseProfilesTypeDef",
    "ClientSearchProfilesResponseTypeDef",
    "ClientSearchProfilesSortCriteriaTypeDef",
    "ClientSearchRoomsFiltersTypeDef",
    "ClientSearchRoomsResponseRoomsTypeDef",
    "ClientSearchRoomsResponseTypeDef",
    "ClientSearchRoomsSortCriteriaTypeDef",
    "ClientSearchSkillGroupsFiltersTypeDef",
    "ClientSearchSkillGroupsResponseSkillGroupsTypeDef",
    "ClientSearchSkillGroupsResponseTypeDef",
    "ClientSearchSkillGroupsSortCriteriaTypeDef",
    "ClientSearchUsersFiltersTypeDef",
    "ClientSearchUsersResponseUsersTypeDef",
    "ClientSearchUsersResponseTypeDef",
    "ClientSearchUsersSortCriteriaTypeDef",
    "ClientSendAnnouncementContentAudioListTypeDef",
    "ClientSendAnnouncementContentSsmlListTypeDef",
    "ClientSendAnnouncementContentTextListTypeDef",
    "ClientSendAnnouncementContentTypeDef",
    "ClientSendAnnouncementResponseTypeDef",
    "ClientSendAnnouncementRoomFiltersTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateBusinessReportScheduleRecurrenceTypeDef",
    "ClientUpdateConferenceProviderIPDialInTypeDef",
    "ClientUpdateConferenceProviderMeetingSettingTypeDef",
    "ClientUpdateConferenceProviderPSTNDialInTypeDef",
    "ClientUpdateContactPhoneNumbersTypeDef",
    "ClientUpdateContactSipAddressesTypeDef",
    "ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    "ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef",
    "ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    "ClientUpdateProfileMeetingRoomConfigurationTypeDef",
    "ListBusinessReportSchedulesPaginatePaginationConfigTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef",
    "ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef",
    "ListBusinessReportSchedulesPaginateResponseTypeDef",
    "ListConferenceProvidersPaginatePaginationConfigTypeDef",
    "ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef",
    "ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef",
    "ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef",
    "ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef",
    "ListConferenceProvidersPaginateResponseTypeDef",
    "ListDeviceEventsPaginatePaginationConfigTypeDef",
    "ListDeviceEventsPaginateResponseDeviceEventsTypeDef",
    "ListDeviceEventsPaginateResponseTypeDef",
    "ListSkillsPaginatePaginationConfigTypeDef",
    "ListSkillsPaginateResponseSkillSummariesTypeDef",
    "ListSkillsPaginateResponseTypeDef",
    "ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef",
    "ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef",
    "ListSkillsStoreCategoriesPaginateResponseTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef",
    "ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef",
    "ListSmartHomeAppliancesPaginatePaginationConfigTypeDef",
    "ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef",
    "ListSmartHomeAppliancesPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagsTypeDef",
    "ListTagsPaginateResponseTypeDef",
    "SearchDevicesPaginateFiltersTypeDef",
    "SearchDevicesPaginatePaginationConfigTypeDef",
    "SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    "SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef",
    "SearchDevicesPaginateResponseDevicesTypeDef",
    "SearchDevicesPaginateResponseTypeDef",
    "SearchDevicesPaginateSortCriteriaTypeDef",
    "SearchProfilesPaginateFiltersTypeDef",
    "SearchProfilesPaginatePaginationConfigTypeDef",
    "SearchProfilesPaginateResponseProfilesTypeDef",
    "SearchProfilesPaginateResponseTypeDef",
    "SearchProfilesPaginateSortCriteriaTypeDef",
    "SearchRoomsPaginateFiltersTypeDef",
    "SearchRoomsPaginatePaginationConfigTypeDef",
    "SearchRoomsPaginateResponseRoomsTypeDef",
    "SearchRoomsPaginateResponseTypeDef",
    "SearchRoomsPaginateSortCriteriaTypeDef",
    "SearchSkillGroupsPaginateFiltersTypeDef",
    "SearchSkillGroupsPaginatePaginationConfigTypeDef",
    "SearchSkillGroupsPaginateResponseSkillGroupsTypeDef",
    "SearchSkillGroupsPaginateResponseTypeDef",
    "SearchSkillGroupsPaginateSortCriteriaTypeDef",
    "SearchUsersPaginateFiltersTypeDef",
    "SearchUsersPaginatePaginationConfigTypeDef",
    "SearchUsersPaginateResponseUsersTypeDef",
    "SearchUsersPaginateResponseTypeDef",
    "SearchUsersPaginateSortCriteriaTypeDef",
)


_ClientCreateAddressBookResponseTypeDef = TypedDict(
    "_ClientCreateAddressBookResponseTypeDef", {"AddressBookArn": str}, total=False
)


class ClientCreateAddressBookResponseTypeDef(_ClientCreateAddressBookResponseTypeDef):
    """
    - *(dict) --*

      - **AddressBookArn** *(string) --*

        The ARN of the newly created address book.
    """


_ClientCreateBusinessReportScheduleContentRangeTypeDef = TypedDict(
    "_ClientCreateBusinessReportScheduleContentRangeTypeDef",
    {"Interval": Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"]},
    total=False,
)


class ClientCreateBusinessReportScheduleContentRangeTypeDef(
    _ClientCreateBusinessReportScheduleContentRangeTypeDef
):
    """
    The content range of the reports.
    - **Interval** *(string) --*

      The interval of the content range.
    """


_ClientCreateBusinessReportScheduleRecurrenceTypeDef = TypedDict(
    "_ClientCreateBusinessReportScheduleRecurrenceTypeDef", {"StartDate": str}, total=False
)


class ClientCreateBusinessReportScheduleRecurrenceTypeDef(
    _ClientCreateBusinessReportScheduleRecurrenceTypeDef
):
    """
    The recurrence of the reports. If this isn't specified, the report will only be delivered one
    time when the API is called.
    - **StartDate** *(string) --*

      The start date.
    """


_ClientCreateBusinessReportScheduleResponseTypeDef = TypedDict(
    "_ClientCreateBusinessReportScheduleResponseTypeDef", {"ScheduleArn": str}, total=False
)


class ClientCreateBusinessReportScheduleResponseTypeDef(
    _ClientCreateBusinessReportScheduleResponseTypeDef
):
    """
    - *(dict) --*

      - **ScheduleArn** *(string) --*

        The ARN of the business report schedule.
    """


_RequiredClientCreateConferenceProviderIPDialInTypeDef = TypedDict(
    "_RequiredClientCreateConferenceProviderIPDialInTypeDef", {"Endpoint": str}
)
_OptionalClientCreateConferenceProviderIPDialInTypeDef = TypedDict(
    "_OptionalClientCreateConferenceProviderIPDialInTypeDef",
    {"CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)


class ClientCreateConferenceProviderIPDialInTypeDef(
    _RequiredClientCreateConferenceProviderIPDialInTypeDef,
    _OptionalClientCreateConferenceProviderIPDialInTypeDef,
):
    """
    The IP endpoint and protocol for calling.
    - **Endpoint** *(string) --***[REQUIRED]**

      The IP address.
    """


_ClientCreateConferenceProviderMeetingSettingTypeDef = TypedDict(
    "_ClientCreateConferenceProviderMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
)


class ClientCreateConferenceProviderMeetingSettingTypeDef(
    _ClientCreateConferenceProviderMeetingSettingTypeDef
):
    """
    The meeting settings for the conference provider.
    - **RequirePin** *(string) --***[REQUIRED]**

      The values that indicate whether the pin is always required.
    """


_RequiredClientCreateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_RequiredClientCreateConferenceProviderPSTNDialInTypeDef", {"CountryCode": str}
)
_OptionalClientCreateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_OptionalClientCreateConferenceProviderPSTNDialInTypeDef",
    {"PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)


class ClientCreateConferenceProviderPSTNDialInTypeDef(
    _RequiredClientCreateConferenceProviderPSTNDialInTypeDef,
    _OptionalClientCreateConferenceProviderPSTNDialInTypeDef,
):
    """
    The information for PSTN conferencing.
    - **CountryCode** *(string) --***[REQUIRED]**

      The zip code.
    """


_ClientCreateConferenceProviderResponseTypeDef = TypedDict(
    "_ClientCreateConferenceProviderResponseTypeDef", {"ConferenceProviderArn": str}, total=False
)


class ClientCreateConferenceProviderResponseTypeDef(_ClientCreateConferenceProviderResponseTypeDef):
    """
    - *(dict) --*

      - **ConferenceProviderArn** *(string) --*

        The ARN of the newly-created conference provider.
    """


_RequiredClientCreateContactPhoneNumbersTypeDef = TypedDict(
    "_RequiredClientCreateContactPhoneNumbersTypeDef", {"Number": str}
)
_OptionalClientCreateContactPhoneNumbersTypeDef = TypedDict(
    "_OptionalClientCreateContactPhoneNumbersTypeDef",
    {"Type": Literal["MOBILE", "WORK", "HOME"]},
    total=False,
)


class ClientCreateContactPhoneNumbersTypeDef(
    _RequiredClientCreateContactPhoneNumbersTypeDef, _OptionalClientCreateContactPhoneNumbersTypeDef
):
    """
    - *(dict) --*

      The phone number for the contact containing the raw number and phone number type.
      - **Number** *(string) --***[REQUIRED]**

        The raw value of the phone number.
    """


_ClientCreateContactResponseTypeDef = TypedDict(
    "_ClientCreateContactResponseTypeDef", {"ContactArn": str}, total=False
)


class ClientCreateContactResponseTypeDef(_ClientCreateContactResponseTypeDef):
    """
    - *(dict) --*

      - **ContactArn** *(string) --*

        The ARN of the newly created address book.
    """


_RequiredClientCreateContactSipAddressesTypeDef = TypedDict(
    "_RequiredClientCreateContactSipAddressesTypeDef", {"Uri": str}
)
_OptionalClientCreateContactSipAddressesTypeDef = TypedDict(
    "_OptionalClientCreateContactSipAddressesTypeDef", {"Type": str}, total=False
)


class ClientCreateContactSipAddressesTypeDef(
    _RequiredClientCreateContactSipAddressesTypeDef, _OptionalClientCreateContactSipAddressesTypeDef
):
    """
    - *(dict) --*

      The SIP address for the contact containing the URI and SIP address type.
      - **Uri** *(string) --***[REQUIRED]**

        The URI for the SIP address.
    """


_ClientCreateGatewayGroupResponseTypeDef = TypedDict(
    "_ClientCreateGatewayGroupResponseTypeDef", {"GatewayGroupArn": str}, total=False
)


class ClientCreateGatewayGroupResponseTypeDef(_ClientCreateGatewayGroupResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayGroupArn** *(string) --*

        The ARN of the created gateway group.
    """


_ClientCreateNetworkProfileResponseTypeDef = TypedDict(
    "_ClientCreateNetworkProfileResponseTypeDef", {"NetworkProfileArn": str}, total=False
)


class ClientCreateNetworkProfileResponseTypeDef(_ClientCreateNetworkProfileResponseTypeDef):
    """
    - *(dict) --*

      - **NetworkProfileArn** *(string) --*

        The ARN of the network profile associated with a device.
    """


_ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef = TypedDict(
    "_ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": Literal[
            "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
        ],
        "Enabled": bool,
    },
    total=False,
)


class ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef(
    _ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef
):
    pass


_ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef = TypedDict(
    "_ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef",
    {"DurationInMinutes": int, "Enabled": bool},
    total=False,
)


class ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef(
    _ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef
):
    pass


_ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef = TypedDict(
    "_ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    {"ReleaseAfterMinutes": int, "Enabled": bool},
    total=False,
)


class ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef(
    _ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef
):
    pass


_ClientCreateProfileMeetingRoomConfigurationTypeDef = TypedDict(
    "_ClientCreateProfileMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": ClientCreateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef,
        "InstantBooking": ClientCreateProfileMeetingRoomConfigurationInstantBookingTypeDef,
        "RequireCheckIn": ClientCreateProfileMeetingRoomConfigurationRequireCheckInTypeDef,
    },
    total=False,
)


class ClientCreateProfileMeetingRoomConfigurationTypeDef(
    _ClientCreateProfileMeetingRoomConfigurationTypeDef
):
    """
    The meeting room settings of a room profile.
    - **RoomUtilizationMetricsEnabled** *(boolean) --*

      Whether room utilization metrics are enabled or not.
    """


_ClientCreateProfileResponseTypeDef = TypedDict(
    "_ClientCreateProfileResponseTypeDef", {"ProfileArn": str}, total=False
)


class ClientCreateProfileResponseTypeDef(_ClientCreateProfileResponseTypeDef):
    """
    - *(dict) --*

      - **ProfileArn** *(string) --*

        The ARN of the newly created room profile in the response.
    """


_ClientCreateRoomResponseTypeDef = TypedDict(
    "_ClientCreateRoomResponseTypeDef", {"RoomArn": str}, total=False
)


class ClientCreateRoomResponseTypeDef(_ClientCreateRoomResponseTypeDef):
    """
    - *(dict) --*

      - **RoomArn** *(string) --*

        The ARN of the newly created room in the response.
    """


_RequiredClientCreateRoomTagsTypeDef = TypedDict(
    "_RequiredClientCreateRoomTagsTypeDef", {"Key": str}
)
_OptionalClientCreateRoomTagsTypeDef = TypedDict(
    "_OptionalClientCreateRoomTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateRoomTagsTypeDef(
    _RequiredClientCreateRoomTagsTypeDef, _OptionalClientCreateRoomTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that can be associated with a resource.
      - **Key** *(string) --***[REQUIRED]**

        The key of a tag. Tag keys are case-sensitive.
    """


_ClientCreateSkillGroupResponseTypeDef = TypedDict(
    "_ClientCreateSkillGroupResponseTypeDef", {"SkillGroupArn": str}, total=False
)


class ClientCreateSkillGroupResponseTypeDef(_ClientCreateSkillGroupResponseTypeDef):
    """
    - *(dict) --*

      - **SkillGroupArn** *(string) --*

        The ARN of the newly created skill group in the response.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"UserArn": str}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    - *(dict) --*

      - **UserArn** *(string) --*

        The ARN of the newly created user in the response.
    """


_RequiredClientCreateUserTagsTypeDef = TypedDict(
    "_RequiredClientCreateUserTagsTypeDef", {"Key": str}
)
_OptionalClientCreateUserTagsTypeDef = TypedDict(
    "_OptionalClientCreateUserTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateUserTagsTypeDef(
    _RequiredClientCreateUserTagsTypeDef, _OptionalClientCreateUserTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that can be associated with a resource.
      - **Key** *(string) --***[REQUIRED]**

        The key of a tag. Tag keys are case-sensitive.
    """


_ClientGetAddressBookResponseAddressBookTypeDef = TypedDict(
    "_ClientGetAddressBookResponseAddressBookTypeDef",
    {"AddressBookArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientGetAddressBookResponseAddressBookTypeDef(
    _ClientGetAddressBookResponseAddressBookTypeDef
):
    """
    - **AddressBook** *(dict) --*

      The details of the requested address book.
      - **AddressBookArn** *(string) --*

        The ARN of the address book.
    """


_ClientGetAddressBookResponseTypeDef = TypedDict(
    "_ClientGetAddressBookResponseTypeDef",
    {"AddressBook": ClientGetAddressBookResponseAddressBookTypeDef},
    total=False,
)


class ClientGetAddressBookResponseTypeDef(_ClientGetAddressBookResponseTypeDef):
    """
    - *(dict) --*

      - **AddressBook** *(dict) --*

        The details of the requested address book.
        - **AddressBookArn** *(string) --*

          The ARN of the address book.
    """


_ClientGetConferencePreferenceResponsePreferenceTypeDef = TypedDict(
    "_ClientGetConferencePreferenceResponsePreferenceTypeDef",
    {"DefaultConferenceProviderArn": str},
    total=False,
)


class ClientGetConferencePreferenceResponsePreferenceTypeDef(
    _ClientGetConferencePreferenceResponsePreferenceTypeDef
):
    """
    - **Preference** *(dict) --*

      The conference preference.
      - **DefaultConferenceProviderArn** *(string) --*

        The ARN of the default conference provider.
    """


_ClientGetConferencePreferenceResponseTypeDef = TypedDict(
    "_ClientGetConferencePreferenceResponseTypeDef",
    {"Preference": ClientGetConferencePreferenceResponsePreferenceTypeDef},
    total=False,
)


class ClientGetConferencePreferenceResponseTypeDef(_ClientGetConferencePreferenceResponseTypeDef):
    """
    - *(dict) --*

      - **Preference** *(dict) --*

        The conference preference.
        - **DefaultConferenceProviderArn** *(string) --*

          The ARN of the default conference provider.
    """


_ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)


class ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef(
    _ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef
):
    pass


_ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
    total=False,
)


class ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef(
    _ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef
):
    pass


_ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef",
    {"CountryCode": str, "PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)


class ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef(
    _ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef
):
    pass


_ClientGetConferenceProviderResponseConferenceProviderTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseConferenceProviderTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": Literal[
            "CHIME",
            "BLUEJEANS",
            "FUZE",
            "GOOGLE_HANGOUTS",
            "POLYCOM",
            "RINGCENTRAL",
            "SKYPE_FOR_BUSINESS",
            "WEBEX",
            "ZOOM",
            "CUSTOM",
        ],
        "IPDialIn": ClientGetConferenceProviderResponseConferenceProviderIPDialInTypeDef,
        "PSTNDialIn": ClientGetConferenceProviderResponseConferenceProviderPSTNDialInTypeDef,
        "MeetingSetting": ClientGetConferenceProviderResponseConferenceProviderMeetingSettingTypeDef,
    },
    total=False,
)


class ClientGetConferenceProviderResponseConferenceProviderTypeDef(
    _ClientGetConferenceProviderResponseConferenceProviderTypeDef
):
    """
    - **ConferenceProvider** *(dict) --*

      The conference provider.
      - **Arn** *(string) --*

        The ARN of the newly created conference provider.
    """


_ClientGetConferenceProviderResponseTypeDef = TypedDict(
    "_ClientGetConferenceProviderResponseTypeDef",
    {"ConferenceProvider": ClientGetConferenceProviderResponseConferenceProviderTypeDef},
    total=False,
)


class ClientGetConferenceProviderResponseTypeDef(_ClientGetConferenceProviderResponseTypeDef):
    """
    - *(dict) --*

      - **ConferenceProvider** *(dict) --*

        The conference provider.
        - **Arn** *(string) --*

          The ARN of the newly created conference provider.
    """


_ClientGetContactResponseContactPhoneNumbersTypeDef = TypedDict(
    "_ClientGetContactResponseContactPhoneNumbersTypeDef",
    {"Number": str, "Type": Literal["MOBILE", "WORK", "HOME"]},
    total=False,
)


class ClientGetContactResponseContactPhoneNumbersTypeDef(
    _ClientGetContactResponseContactPhoneNumbersTypeDef
):
    pass


_ClientGetContactResponseContactSipAddressesTypeDef = TypedDict(
    "_ClientGetContactResponseContactSipAddressesTypeDef", {"Uri": str, "Type": str}, total=False
)


class ClientGetContactResponseContactSipAddressesTypeDef(
    _ClientGetContactResponseContactSipAddressesTypeDef
):
    pass


_ClientGetContactResponseContactTypeDef = TypedDict(
    "_ClientGetContactResponseContactTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List[ClientGetContactResponseContactPhoneNumbersTypeDef],
        "SipAddresses": List[ClientGetContactResponseContactSipAddressesTypeDef],
    },
    total=False,
)


class ClientGetContactResponseContactTypeDef(_ClientGetContactResponseContactTypeDef):
    """
    - **Contact** *(dict) --*

      The details of the requested contact.
      - **ContactArn** *(string) --*

        The ARN of the contact.
    """


_ClientGetContactResponseTypeDef = TypedDict(
    "_ClientGetContactResponseTypeDef",
    {"Contact": ClientGetContactResponseContactTypeDef},
    total=False,
)


class ClientGetContactResponseTypeDef(_ClientGetContactResponseTypeDef):
    """
    - *(dict) --*

      - **Contact** *(dict) --*

        The details of the requested contact.
        - **ContactArn** *(string) --*

          The ARN of the contact.
    """


_ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef",
    {
        "Feature": Literal[
            "BLUETOOTH",
            "VOLUME",
            "NOTIFICATIONS",
            "LISTS",
            "SKILLS",
            "NETWORK_PROFILE",
            "SETTINGS",
            "ALL",
        ],
        "Code": Literal[
            "DEVICE_SOFTWARE_UPDATE_NEEDED",
            "DEVICE_WAS_OFFLINE",
            "CREDENTIALS_ACCESS_FAILURE",
            "TLS_VERSION_MISMATCH",
            "ASSOCIATION_REJECTION",
            "AUTHENTICATION_FAILURE",
            "DHCP_FAILURE",
            "INTERNET_UNAVAILABLE",
            "DNS_FAILURE",
            "UNKNOWN_FAILURE",
            "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
            "INVALID_CERTIFICATE_AUTHORITY",
            "NETWORK_PROFILE_NOT_FOUND",
            "INVALID_PASSWORD_STATE",
            "PASSWORD_NOT_FOUND",
        ],
    },
    total=False,
)


class ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef(
    _ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef
):
    pass


_ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[
            ClientGetDeviceResponseDeviceDeviceStatusInfoDeviceStatusDetailsTypeDef
        ],
        "ConnectionStatus": Literal["ONLINE", "OFFLINE"],
    },
    total=False,
)


class ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef(
    _ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef
):
    pass


_ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef",
    {"NetworkProfileArn": str, "CertificateArn": str, "CertificateExpirationTime": datetime},
    total=False,
)


class ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef(
    _ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef
):
    pass


_ClientGetDeviceResponseDeviceTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "RoomArn": str,
        "DeviceStatus": Literal["READY", "PENDING", "WAS_OFFLINE", "DEREGISTERED", "FAILED"],
        "DeviceStatusInfo": ClientGetDeviceResponseDeviceDeviceStatusInfoTypeDef,
        "NetworkProfileInfo": ClientGetDeviceResponseDeviceNetworkProfileInfoTypeDef,
    },
    total=False,
)


class ClientGetDeviceResponseDeviceTypeDef(_ClientGetDeviceResponseDeviceTypeDef):
    """
    - **Device** *(dict) --*

      The details of the device requested. Required.
      - **DeviceArn** *(string) --*

        The ARN of a device.
    """


_ClientGetDeviceResponseTypeDef = TypedDict(
    "_ClientGetDeviceResponseTypeDef", {"Device": ClientGetDeviceResponseDeviceTypeDef}, total=False
)


class ClientGetDeviceResponseTypeDef(_ClientGetDeviceResponseTypeDef):
    """
    - *(dict) --*

      - **Device** *(dict) --*

        The details of the device requested. Required.
        - **DeviceArn** *(string) --*

          The ARN of a device.
    """


_ClientGetGatewayGroupResponseGatewayGroupTypeDef = TypedDict(
    "_ClientGetGatewayGroupResponseGatewayGroupTypeDef",
    {"Arn": str, "Name": str, "Description": str},
    total=False,
)


class ClientGetGatewayGroupResponseGatewayGroupTypeDef(
    _ClientGetGatewayGroupResponseGatewayGroupTypeDef
):
    """
    - **GatewayGroup** *(dict) --*

      The details of the gateway group.
      - **Arn** *(string) --*

        The ARN of the gateway group.
    """


_ClientGetGatewayGroupResponseTypeDef = TypedDict(
    "_ClientGetGatewayGroupResponseTypeDef",
    {"GatewayGroup": ClientGetGatewayGroupResponseGatewayGroupTypeDef},
    total=False,
)


class ClientGetGatewayGroupResponseTypeDef(_ClientGetGatewayGroupResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayGroup** *(dict) --*

        The details of the gateway group.
        - **Arn** *(string) --*

          The ARN of the gateway group.
    """


_ClientGetGatewayResponseGatewayTypeDef = TypedDict(
    "_ClientGetGatewayResponseGatewayTypeDef",
    {"Arn": str, "Name": str, "Description": str, "GatewayGroupArn": str, "SoftwareVersion": str},
    total=False,
)


class ClientGetGatewayResponseGatewayTypeDef(_ClientGetGatewayResponseGatewayTypeDef):
    """
    - **Gateway** *(dict) --*

      The details of the gateway.
      - **Arn** *(string) --*

        The ARN of the gateway.
    """


_ClientGetGatewayResponseTypeDef = TypedDict(
    "_ClientGetGatewayResponseTypeDef",
    {"Gateway": ClientGetGatewayResponseGatewayTypeDef},
    total=False,
)


class ClientGetGatewayResponseTypeDef(_ClientGetGatewayResponseTypeDef):
    """
    - *(dict) --*

      - **Gateway** *(dict) --*

        The details of the gateway.
        - **Arn** *(string) --*

          The ARN of the gateway.
    """


_ClientGetInvitationConfigurationResponseTypeDef = TypedDict(
    "_ClientGetInvitationConfigurationResponseTypeDef",
    {"OrganizationName": str, "ContactEmail": str, "PrivateSkillIds": List[str]},
    total=False,
)


class ClientGetInvitationConfigurationResponseTypeDef(
    _ClientGetInvitationConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationName** *(string) --*

        The name of the organization sending the enrollment invite to a user.
    """


_ClientGetNetworkProfileResponseNetworkProfileTypeDef = TypedDict(
    "_ClientGetNetworkProfileResponseNetworkProfileTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": Literal["OPEN", "WEP", "WPA_PSK", "WPA2_PSK", "WPA2_ENTERPRISE"],
        "EapMethod": str,
        "CurrentPassword": str,
        "NextPassword": str,
        "CertificateAuthorityArn": str,
        "TrustAnchors": List[str],
    },
    total=False,
)


class ClientGetNetworkProfileResponseNetworkProfileTypeDef(
    _ClientGetNetworkProfileResponseNetworkProfileTypeDef
):
    """
    - **NetworkProfile** *(dict) --*

      The network profile associated with a device.
      - **NetworkProfileArn** *(string) --*

        The ARN of the network profile associated with a device.
    """


_ClientGetNetworkProfileResponseTypeDef = TypedDict(
    "_ClientGetNetworkProfileResponseTypeDef",
    {"NetworkProfile": ClientGetNetworkProfileResponseNetworkProfileTypeDef},
    total=False,
)


class ClientGetNetworkProfileResponseTypeDef(_ClientGetNetworkProfileResponseTypeDef):
    """
    - *(dict) --*

      - **NetworkProfile** *(dict) --*

        The network profile associated with a device.
        - **NetworkProfileArn** *(string) --*

          The ARN of the network profile associated with a device.
    """


_ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef = TypedDict(
    "_ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": Literal[
            "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
        ],
        "Enabled": bool,
    },
    total=False,
)


class ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef(
    _ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef
):
    pass


_ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef = TypedDict(
    "_ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef",
    {"DurationInMinutes": int, "Enabled": bool},
    total=False,
)


class ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef(
    _ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef
):
    pass


_ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef = TypedDict(
    "_ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    {"ReleaseAfterMinutes": int, "Enabled": bool},
    total=False,
)


class ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef(
    _ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef
):
    pass


_ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef = TypedDict(
    "_ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": ClientGetProfileResponseProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef,
        "InstantBooking": ClientGetProfileResponseProfileMeetingRoomConfigurationInstantBookingTypeDef,
        "RequireCheckIn": ClientGetProfileResponseProfileMeetingRoomConfigurationRequireCheckInTypeDef,
    },
    total=False,
)


class ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef(
    _ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef
):
    pass


_ClientGetProfileResponseProfileTypeDef = TypedDict(
    "_ClientGetProfileResponseProfileTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": Literal["METRIC", "IMPERIAL"],
        "TemperatureUnit": Literal["FAHRENHEIT", "CELSIUS"],
        "WakeWord": Literal["ALEXA", "AMAZON", "ECHO", "COMPUTER"],
        "Locale": str,
        "SetupModeDisabled": bool,
        "MaxVolumeLimit": int,
        "PSTNEnabled": bool,
        "AddressBookArn": str,
        "MeetingRoomConfiguration": ClientGetProfileResponseProfileMeetingRoomConfigurationTypeDef,
    },
    total=False,
)


class ClientGetProfileResponseProfileTypeDef(_ClientGetProfileResponseProfileTypeDef):
    """
    - **Profile** *(dict) --*

      The details of the room profile requested. Required.
      - **ProfileArn** *(string) --*

        The ARN of a room profile.
    """


_ClientGetProfileResponseTypeDef = TypedDict(
    "_ClientGetProfileResponseTypeDef",
    {"Profile": ClientGetProfileResponseProfileTypeDef},
    total=False,
)


class ClientGetProfileResponseTypeDef(_ClientGetProfileResponseTypeDef):
    """
    - *(dict) --*

      - **Profile** *(dict) --*

        The details of the room profile requested. Required.
        - **ProfileArn** *(string) --*

          The ARN of a room profile.
    """


_ClientGetRoomResponseRoomTypeDef = TypedDict(
    "_ClientGetRoomResponseRoomTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
    },
    total=False,
)


class ClientGetRoomResponseRoomTypeDef(_ClientGetRoomResponseRoomTypeDef):
    """
    - **Room** *(dict) --*

      The details of the room requested.
      - **RoomArn** *(string) --*

        The ARN of a room.
    """


_ClientGetRoomResponseTypeDef = TypedDict(
    "_ClientGetRoomResponseTypeDef", {"Room": ClientGetRoomResponseRoomTypeDef}, total=False
)


class ClientGetRoomResponseTypeDef(_ClientGetRoomResponseTypeDef):
    """
    - *(dict) --*

      - **Room** *(dict) --*

        The details of the room requested.
        - **RoomArn** *(string) --*

          The ARN of a room.
    """


_ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef = TypedDict(
    "_ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef",
    {"ParameterKey": str, "ParameterValue": str},
    total=False,
)


class ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef(
    _ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef
):
    """
    - **RoomSkillParameter** *(dict) --*

      The details of the room skill parameter requested. Required.
      - **ParameterKey** *(string) --*

        The parameter key of a room skill parameter. ParameterKey is an enumerated type that only
        takes “DEFAULT” or “SCOPE” as valid values.
    """


_ClientGetRoomSkillParameterResponseTypeDef = TypedDict(
    "_ClientGetRoomSkillParameterResponseTypeDef",
    {"RoomSkillParameter": ClientGetRoomSkillParameterResponseRoomSkillParameterTypeDef},
    total=False,
)


class ClientGetRoomSkillParameterResponseTypeDef(_ClientGetRoomSkillParameterResponseTypeDef):
    """
    - *(dict) --*

      - **RoomSkillParameter** *(dict) --*

        The details of the room skill parameter requested. Required.
        - **ParameterKey** *(string) --*

          The parameter key of a room skill parameter. ParameterKey is an enumerated type that only
          takes “DEFAULT” or “SCOPE” as valid values.
    """


_ClientGetSkillGroupResponseSkillGroupTypeDef = TypedDict(
    "_ClientGetSkillGroupResponseSkillGroupTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)


class ClientGetSkillGroupResponseSkillGroupTypeDef(_ClientGetSkillGroupResponseSkillGroupTypeDef):
    """
    - **SkillGroup** *(dict) --*

      The details of the skill group requested. Required.
      - **SkillGroupArn** *(string) --*

        The ARN of a skill group.
    """


_ClientGetSkillGroupResponseTypeDef = TypedDict(
    "_ClientGetSkillGroupResponseTypeDef",
    {"SkillGroup": ClientGetSkillGroupResponseSkillGroupTypeDef},
    total=False,
)


class ClientGetSkillGroupResponseTypeDef(_ClientGetSkillGroupResponseTypeDef):
    """
    - *(dict) --*

      - **SkillGroup** *(dict) --*

        The details of the skill group requested. Required.
        - **SkillGroupArn** *(string) --*

          The ARN of a skill group.
    """


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef",
    {"Interval": Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"]},
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef
):
    pass


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    {"Path": str, "BucketName": str},
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef
):
    pass


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    {
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED"],
        "FailureCode": Literal["ACCESS_DENIED", "NO_SUCH_BUCKET", "INTERNAL_FAILURE"],
        "S3Location": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef,
        "DeliveryTime": datetime,
        "DownloadUrl": str,
    },
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef
):
    pass


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef",
    {"StartDate": str},
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef
):
    pass


_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef",
    {
        "ScheduleArn": str,
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": Literal["CSV", "CSV_ZIP"],
        "ContentRange": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesContentRangeTypeDef,
        "Recurrence": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesRecurrenceTypeDef,
        "LastBusinessReport": ClientListBusinessReportSchedulesResponseBusinessReportSchedulesLastBusinessReportTypeDef,
    },
    total=False,
)


class ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef(
    _ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef
):
    """
    - *(dict) --*

      The schedule of the usage report.
      - **ScheduleArn** *(string) --*

        The ARN of the business report schedule.
    """


_ClientListBusinessReportSchedulesResponseTypeDef = TypedDict(
    "_ClientListBusinessReportSchedulesResponseTypeDef",
    {
        "BusinessReportSchedules": List[
            ClientListBusinessReportSchedulesResponseBusinessReportSchedulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListBusinessReportSchedulesResponseTypeDef(
    _ClientListBusinessReportSchedulesResponseTypeDef
):
    """
    - *(dict) --*

      - **BusinessReportSchedules** *(list) --*

        The schedule of the reports.
        - *(dict) --*

          The schedule of the usage report.
          - **ScheduleArn** *(string) --*

            The ARN of the business report schedule.
    """


_ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)


class ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef(
    _ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef
):
    pass


_ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
    total=False,
)


class ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef(
    _ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef
):
    pass


_ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef",
    {"CountryCode": str, "PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)


class ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef(
    _ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef
):
    pass


_ClientListConferenceProvidersResponseConferenceProvidersTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseConferenceProvidersTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": Literal[
            "CHIME",
            "BLUEJEANS",
            "FUZE",
            "GOOGLE_HANGOUTS",
            "POLYCOM",
            "RINGCENTRAL",
            "SKYPE_FOR_BUSINESS",
            "WEBEX",
            "ZOOM",
            "CUSTOM",
        ],
        "IPDialIn": ClientListConferenceProvidersResponseConferenceProvidersIPDialInTypeDef,
        "PSTNDialIn": ClientListConferenceProvidersResponseConferenceProvidersPSTNDialInTypeDef,
        "MeetingSetting": ClientListConferenceProvidersResponseConferenceProvidersMeetingSettingTypeDef,
    },
    total=False,
)


class ClientListConferenceProvidersResponseConferenceProvidersTypeDef(
    _ClientListConferenceProvidersResponseConferenceProvidersTypeDef
):
    """
    - *(dict) --*

      An entity that provides a conferencing solution. Alexa for Business acts as the voice
      interface and mediator that connects users to their preferred conference provider. Examples of
      conference providers include Amazon Chime, Zoom, Cisco, and Polycom.
      - **Arn** *(string) --*

        The ARN of the newly created conference provider.
    """


_ClientListConferenceProvidersResponseTypeDef = TypedDict(
    "_ClientListConferenceProvidersResponseTypeDef",
    {
        "ConferenceProviders": List[
            ClientListConferenceProvidersResponseConferenceProvidersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListConferenceProvidersResponseTypeDef(_ClientListConferenceProvidersResponseTypeDef):
    """
    - *(dict) --*

      - **ConferenceProviders** *(list) --*

        The conference providers.
        - *(dict) --*

          An entity that provides a conferencing solution. Alexa for Business acts as the voice
          interface and mediator that connects users to their preferred conference provider.
          Examples of conference providers include Amazon Chime, Zoom, Cisco, and Polycom.
          - **Arn** *(string) --*

            The ARN of the newly created conference provider.
    """


_ClientListDeviceEventsResponseDeviceEventsTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseDeviceEventsTypeDef",
    {"Type": Literal["CONNECTION_STATUS", "DEVICE_STATUS"], "Value": str, "Timestamp": datetime},
    total=False,
)


class ClientListDeviceEventsResponseDeviceEventsTypeDef(
    _ClientListDeviceEventsResponseDeviceEventsTypeDef
):
    """
    - *(dict) --*

      The list of device events.
      - **Type** *(string) --*

        The type of device event.
    """


_ClientListDeviceEventsResponseTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseTypeDef",
    {"DeviceEvents": List[ClientListDeviceEventsResponseDeviceEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDeviceEventsResponseTypeDef(_ClientListDeviceEventsResponseTypeDef):
    """
    - *(dict) --*

      - **DeviceEvents** *(list) --*

        The device events requested for the device ARN.
        - *(dict) --*

          The list of device events.
          - **Type** *(string) --*

            The type of device event.
    """


_ClientListGatewayGroupsResponseGatewayGroupsTypeDef = TypedDict(
    "_ClientListGatewayGroupsResponseGatewayGroupsTypeDef",
    {"Arn": str, "Name": str, "Description": str},
    total=False,
)


class ClientListGatewayGroupsResponseGatewayGroupsTypeDef(
    _ClientListGatewayGroupsResponseGatewayGroupsTypeDef
):
    """
    - *(dict) --*

      The summary of a gateway group.
      - **Arn** *(string) --*

        The ARN of the gateway group.
    """


_ClientListGatewayGroupsResponseTypeDef = TypedDict(
    "_ClientListGatewayGroupsResponseTypeDef",
    {"GatewayGroups": List[ClientListGatewayGroupsResponseGatewayGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListGatewayGroupsResponseTypeDef(_ClientListGatewayGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayGroups** *(list) --*

        The gateway groups in the list.
        - *(dict) --*

          The summary of a gateway group.
          - **Arn** *(string) --*

            The ARN of the gateway group.
    """


_ClientListGatewaysResponseGatewaysTypeDef = TypedDict(
    "_ClientListGatewaysResponseGatewaysTypeDef",
    {"Arn": str, "Name": str, "Description": str, "GatewayGroupArn": str, "SoftwareVersion": str},
    total=False,
)


class ClientListGatewaysResponseGatewaysTypeDef(_ClientListGatewaysResponseGatewaysTypeDef):
    """
    - *(dict) --*

      The summary of a gateway.
      - **Arn** *(string) --*

        The ARN of the gateway.
    """


_ClientListGatewaysResponseTypeDef = TypedDict(
    "_ClientListGatewaysResponseTypeDef",
    {"Gateways": List[ClientListGatewaysResponseGatewaysTypeDef], "NextToken": str},
    total=False,
)


class ClientListGatewaysResponseTypeDef(_ClientListGatewaysResponseTypeDef):
    """
    - *(dict) --*

      - **Gateways** *(list) --*

        The gateways in the list.
        - *(dict) --*

          The summary of a gateway.
          - **Arn** *(string) --*

            The ARN of the gateway.
    """


_ClientListSkillsResponseSkillSummariesTypeDef = TypedDict(
    "_ClientListSkillsResponseSkillSummariesTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "SupportsLinking": bool,
        "EnablementType": Literal["ENABLED", "PENDING"],
        "SkillType": Literal["PUBLIC", "PRIVATE"],
    },
    total=False,
)


class ClientListSkillsResponseSkillSummariesTypeDef(_ClientListSkillsResponseSkillSummariesTypeDef):
    """
    - *(dict) --*

      The summary of skills.
      - **SkillId** *(string) --*

        The ARN of the skill summary.
    """


_ClientListSkillsResponseTypeDef = TypedDict(
    "_ClientListSkillsResponseTypeDef",
    {"SkillSummaries": List[ClientListSkillsResponseSkillSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListSkillsResponseTypeDef(_ClientListSkillsResponseTypeDef):
    """
    - *(dict) --*

      - **SkillSummaries** *(list) --*

        The list of enabled skills requested. Required.
        - *(dict) --*

          The summary of skills.
          - **SkillId** *(string) --*

            The ARN of the skill summary.
    """


_ClientListSkillsStoreCategoriesResponseCategoryListTypeDef = TypedDict(
    "_ClientListSkillsStoreCategoriesResponseCategoryListTypeDef",
    {"CategoryId": int, "CategoryName": str},
    total=False,
)


class ClientListSkillsStoreCategoriesResponseCategoryListTypeDef(
    _ClientListSkillsStoreCategoriesResponseCategoryListTypeDef
):
    """
    - *(dict) --*

      The skill store category that is shown. Alexa skills are assigned a specific skill category
      during creation, such as News, Social, and Sports.
      - **CategoryId** *(integer) --*

        The ID of the skill store category.
    """


_ClientListSkillsStoreCategoriesResponseTypeDef = TypedDict(
    "_ClientListSkillsStoreCategoriesResponseTypeDef",
    {
        "CategoryList": List[ClientListSkillsStoreCategoriesResponseCategoryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListSkillsStoreCategoriesResponseTypeDef(
    _ClientListSkillsStoreCategoriesResponseTypeDef
):
    """
    - *(dict) --*

      - **CategoryList** *(list) --*

        The list of categories.
        - *(dict) --*

          The skill store category that is shown. Alexa skills are assigned a specific skill
          category during creation, such as News, Social, and Sports.
          - **CategoryId** *(integer) --*

            The ID of the skill store category.
    """


_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef = TypedDict(
    "_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    {"DeveloperName": str, "PrivacyPolicy": str, "Email": str, "Url": str},
    total=False,
)


class ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef(
    _ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef
):
    pass


_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef = TypedDict(
    "_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef",
    {
        "ProductDescription": str,
        "InvocationPhrase": str,
        "ReleaseDate": str,
        "EndUserLicenseAgreement": str,
        "GenericKeywords": List[str],
        "BulletPoints": List[str],
        "NewInThisVersionBulletPoints": List[str],
        "SkillTypes": List[str],
        "Reviews": Dict[str, str],
        "DeveloperInfo": ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef,
    },
    total=False,
)


class ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef(
    _ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef
):
    pass


_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef = TypedDict(
    "_ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "ShortDescription": str,
        "IconUrl": str,
        "SampleUtterances": List[str],
        "SkillDetails": ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsSkillDetailsTypeDef,
        "SupportsLinking": bool,
    },
    total=False,
)


class ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef(
    _ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef
):
    """
    - *(dict) --*

      The detailed information about an Alexa skill.
      - **SkillId** *(string) --*

        The ARN of the skill.
    """


_ClientListSkillsStoreSkillsByCategoryResponseTypeDef = TypedDict(
    "_ClientListSkillsStoreSkillsByCategoryResponseTypeDef",
    {
        "SkillsStoreSkills": List[
            ClientListSkillsStoreSkillsByCategoryResponseSkillsStoreSkillsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSkillsStoreSkillsByCategoryResponseTypeDef(
    _ClientListSkillsStoreSkillsByCategoryResponseTypeDef
):
    """
    - *(dict) --*

      - **SkillsStoreSkills** *(list) --*

        The skill store skills.
        - *(dict) --*

          The detailed information about an Alexa skill.
          - **SkillId** *(string) --*

            The ARN of the skill.
    """


_ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef = TypedDict(
    "_ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef",
    {"FriendlyName": str, "Description": str, "ManufacturerName": str},
    total=False,
)


class ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef(
    _ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef
):
    """
    - *(dict) --*

      A smart home appliance that can connect to a central system. Any domestic device can be a
      smart appliance.
      - **FriendlyName** *(string) --*

        The friendly name of the smart home appliance.
    """


_ClientListSmartHomeAppliancesResponseTypeDef = TypedDict(
    "_ClientListSmartHomeAppliancesResponseTypeDef",
    {
        "SmartHomeAppliances": List[
            ClientListSmartHomeAppliancesResponseSmartHomeAppliancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSmartHomeAppliancesResponseTypeDef(_ClientListSmartHomeAppliancesResponseTypeDef):
    """
    - *(dict) --*

      - **SmartHomeAppliances** *(list) --*

        The smart home appliances.
        - *(dict) --*

          A smart home appliance that can connect to a central system. Any domestic device can be a
          smart appliance.
          - **FriendlyName** *(string) --*

            The friendly name of the smart home appliance.
    """


_ClientListTagsResponseTagsTypeDef = TypedDict(
    "_ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagsTypeDef(_ClientListTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      A key-value pair that can be associated with a resource.
      - **Key** *(string) --*

        The key of a tag. Tag keys are case-sensitive.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags requested for the specified resource.
        - *(dict) --*

          A key-value pair that can be associated with a resource.
          - **Key** *(string) --*

            The key of a tag. Tag keys are case-sensitive.
    """


_ClientPutConferencePreferenceConferencePreferenceTypeDef = TypedDict(
    "_ClientPutConferencePreferenceConferencePreferenceTypeDef",
    {"DefaultConferenceProviderArn": str},
    total=False,
)


class ClientPutConferencePreferenceConferencePreferenceTypeDef(
    _ClientPutConferencePreferenceConferencePreferenceTypeDef
):
    """
    The conference preference of a specific conference provider.
    - **DefaultConferenceProviderArn** *(string) --*

      The ARN of the default conference provider.
    """


_RequiredClientPutRoomSkillParameterRoomSkillParameterTypeDef = TypedDict(
    "_RequiredClientPutRoomSkillParameterRoomSkillParameterTypeDef", {"ParameterKey": str}
)
_OptionalClientPutRoomSkillParameterRoomSkillParameterTypeDef = TypedDict(
    "_OptionalClientPutRoomSkillParameterRoomSkillParameterTypeDef",
    {"ParameterValue": str},
    total=False,
)


class ClientPutRoomSkillParameterRoomSkillParameterTypeDef(
    _RequiredClientPutRoomSkillParameterRoomSkillParameterTypeDef,
    _OptionalClientPutRoomSkillParameterRoomSkillParameterTypeDef,
):
    """
    The updated room skill parameter. Required.
    - **ParameterKey** *(string) --***[REQUIRED]**

      The parameter key of a room skill parameter. ParameterKey is an enumerated type that only
      takes “DEFAULT” or “SCOPE” as valid values.
    """


_ClientRegisterAvsDeviceResponseTypeDef = TypedDict(
    "_ClientRegisterAvsDeviceResponseTypeDef", {"DeviceArn": str}, total=False
)


class ClientRegisterAvsDeviceResponseTypeDef(_ClientRegisterAvsDeviceResponseTypeDef):
    """
    - *(dict) --*

      - **DeviceArn** *(string) --*

        The ARN of the device.
    """


_ClientResolveRoomResponseRoomSkillParametersTypeDef = TypedDict(
    "_ClientResolveRoomResponseRoomSkillParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str},
    total=False,
)


class ClientResolveRoomResponseRoomSkillParametersTypeDef(
    _ClientResolveRoomResponseRoomSkillParametersTypeDef
):
    pass


_ClientResolveRoomResponseTypeDef = TypedDict(
    "_ClientResolveRoomResponseTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "RoomSkillParameters": List[ClientResolveRoomResponseRoomSkillParametersTypeDef],
    },
    total=False,
)


class ClientResolveRoomResponseTypeDef(_ClientResolveRoomResponseTypeDef):
    """
    - *(dict) --*

      - **RoomArn** *(string) --*

        The ARN of the room from which the skill request was invoked.
    """


_RequiredClientSearchAddressBooksFiltersTypeDef = TypedDict(
    "_RequiredClientSearchAddressBooksFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchAddressBooksFiltersTypeDef = TypedDict(
    "_OptionalClientSearchAddressBooksFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchAddressBooksFiltersTypeDef(
    _RequiredClientSearchAddressBooksFiltersTypeDef, _OptionalClientSearchAddressBooksFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_ClientSearchAddressBooksResponseAddressBooksTypeDef = TypedDict(
    "_ClientSearchAddressBooksResponseAddressBooksTypeDef",
    {"AddressBookArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientSearchAddressBooksResponseAddressBooksTypeDef(
    _ClientSearchAddressBooksResponseAddressBooksTypeDef
):
    """
    - *(dict) --*

      Information related to an address book.
      - **AddressBookArn** *(string) --*

        The ARN of the address book.
    """


_ClientSearchAddressBooksResponseTypeDef = TypedDict(
    "_ClientSearchAddressBooksResponseTypeDef",
    {
        "AddressBooks": List[ClientSearchAddressBooksResponseAddressBooksTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchAddressBooksResponseTypeDef(_ClientSearchAddressBooksResponseTypeDef):
    """
    - *(dict) --*

      - **AddressBooks** *(list) --*

        The address books that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          Information related to an address book.
          - **AddressBookArn** *(string) --*

            The ARN of the address book.
    """


_RequiredClientSearchAddressBooksSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchAddressBooksSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchAddressBooksSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchAddressBooksSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchAddressBooksSortCriteriaTypeDef(
    _RequiredClientSearchAddressBooksSortCriteriaTypeDef,
    _OptionalClientSearchAddressBooksSortCriteriaTypeDef,
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredClientSearchContactsFiltersTypeDef = TypedDict(
    "_RequiredClientSearchContactsFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchContactsFiltersTypeDef = TypedDict(
    "_OptionalClientSearchContactsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchContactsFiltersTypeDef(
    _RequiredClientSearchContactsFiltersTypeDef, _OptionalClientSearchContactsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_ClientSearchContactsResponseContactsPhoneNumbersTypeDef = TypedDict(
    "_ClientSearchContactsResponseContactsPhoneNumbersTypeDef",
    {"Number": str, "Type": Literal["MOBILE", "WORK", "HOME"]},
    total=False,
)


class ClientSearchContactsResponseContactsPhoneNumbersTypeDef(
    _ClientSearchContactsResponseContactsPhoneNumbersTypeDef
):
    pass


_ClientSearchContactsResponseContactsSipAddressesTypeDef = TypedDict(
    "_ClientSearchContactsResponseContactsSipAddressesTypeDef",
    {"Uri": str, "Type": str},
    total=False,
)


class ClientSearchContactsResponseContactsSipAddressesTypeDef(
    _ClientSearchContactsResponseContactsSipAddressesTypeDef
):
    pass


_ClientSearchContactsResponseContactsTypeDef = TypedDict(
    "_ClientSearchContactsResponseContactsTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List[ClientSearchContactsResponseContactsPhoneNumbersTypeDef],
        "SipAddresses": List[ClientSearchContactsResponseContactsSipAddressesTypeDef],
    },
    total=False,
)


class ClientSearchContactsResponseContactsTypeDef(_ClientSearchContactsResponseContactsTypeDef):
    """
    - *(dict) --*

      Information related to a contact.
      - **ContactArn** *(string) --*

        The ARN of the contact.
    """


_ClientSearchContactsResponseTypeDef = TypedDict(
    "_ClientSearchContactsResponseTypeDef",
    {
        "Contacts": List[ClientSearchContactsResponseContactsTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchContactsResponseTypeDef(_ClientSearchContactsResponseTypeDef):
    """
    - *(dict) --*

      - **Contacts** *(list) --*

        The contacts that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          Information related to a contact.
          - **ContactArn** *(string) --*

            The ARN of the contact.
    """


_RequiredClientSearchContactsSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchContactsSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchContactsSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchContactsSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchContactsSortCriteriaTypeDef(
    _RequiredClientSearchContactsSortCriteriaTypeDef,
    _OptionalClientSearchContactsSortCriteriaTypeDef,
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredClientSearchDevicesFiltersTypeDef = TypedDict(
    "_RequiredClientSearchDevicesFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchDevicesFiltersTypeDef = TypedDict(
    "_OptionalClientSearchDevicesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchDevicesFiltersTypeDef(
    _RequiredClientSearchDevicesFiltersTypeDef, _OptionalClientSearchDevicesFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef = TypedDict(
    "_ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    {
        "Feature": Literal[
            "BLUETOOTH",
            "VOLUME",
            "NOTIFICATIONS",
            "LISTS",
            "SKILLS",
            "NETWORK_PROFILE",
            "SETTINGS",
            "ALL",
        ],
        "Code": Literal[
            "DEVICE_SOFTWARE_UPDATE_NEEDED",
            "DEVICE_WAS_OFFLINE",
            "CREDENTIALS_ACCESS_FAILURE",
            "TLS_VERSION_MISMATCH",
            "ASSOCIATION_REJECTION",
            "AUTHENTICATION_FAILURE",
            "DHCP_FAILURE",
            "INTERNET_UNAVAILABLE",
            "DNS_FAILURE",
            "UNKNOWN_FAILURE",
            "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
            "INVALID_CERTIFICATE_AUTHORITY",
            "NETWORK_PROFILE_NOT_FOUND",
            "INVALID_PASSWORD_STATE",
            "PASSWORD_NOT_FOUND",
        ],
    },
    total=False,
)


class ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef(
    _ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
):
    pass


_ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef = TypedDict(
    "_ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[
            ClientSearchDevicesResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
        ],
        "ConnectionStatus": Literal["ONLINE", "OFFLINE"],
    },
    total=False,
)


class ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef(
    _ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef
):
    pass


_ClientSearchDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientSearchDevicesResponseDevicesTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "DeviceStatus": Literal["READY", "PENDING", "WAS_OFFLINE", "DEREGISTERED", "FAILED"],
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "RoomArn": str,
        "RoomName": str,
        "DeviceStatusInfo": ClientSearchDevicesResponseDevicesDeviceStatusInfoTypeDef,
    },
    total=False,
)


class ClientSearchDevicesResponseDevicesTypeDef(_ClientSearchDevicesResponseDevicesTypeDef):
    """
    - *(dict) --*

      Device attributes.
      - **DeviceArn** *(string) --*

        The ARN of a device.
    """


_ClientSearchDevicesResponseTypeDef = TypedDict(
    "_ClientSearchDevicesResponseTypeDef",
    {
        "Devices": List[ClientSearchDevicesResponseDevicesTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchDevicesResponseTypeDef(_ClientSearchDevicesResponseTypeDef):
    """
    - *(dict) --*

      - **Devices** *(list) --*

        The devices that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          Device attributes.
          - **DeviceArn** *(string) --*

            The ARN of a device.
    """


_RequiredClientSearchDevicesSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchDevicesSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchDevicesSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchDevicesSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchDevicesSortCriteriaTypeDef(
    _RequiredClientSearchDevicesSortCriteriaTypeDef, _OptionalClientSearchDevicesSortCriteriaTypeDef
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredClientSearchNetworkProfilesFiltersTypeDef = TypedDict(
    "_RequiredClientSearchNetworkProfilesFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchNetworkProfilesFiltersTypeDef = TypedDict(
    "_OptionalClientSearchNetworkProfilesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchNetworkProfilesFiltersTypeDef(
    _RequiredClientSearchNetworkProfilesFiltersTypeDef,
    _OptionalClientSearchNetworkProfilesFiltersTypeDef,
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef = TypedDict(
    "_ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": Literal["OPEN", "WEP", "WPA_PSK", "WPA2_PSK", "WPA2_ENTERPRISE"],
        "EapMethod": str,
        "CertificateAuthorityArn": str,
    },
    total=False,
)


class ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef(
    _ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef
):
    """
    - *(dict) --*

      The data associated with a network profile.
      - **NetworkProfileArn** *(string) --*

        The ARN of the network profile associated with a device.
    """


_ClientSearchNetworkProfilesResponseTypeDef = TypedDict(
    "_ClientSearchNetworkProfilesResponseTypeDef",
    {
        "NetworkProfiles": List[ClientSearchNetworkProfilesResponseNetworkProfilesTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchNetworkProfilesResponseTypeDef(_ClientSearchNetworkProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **NetworkProfiles** *(list) --*

        The network profiles that meet the specified set of filter criteria, in sort order. It is a
        list of NetworkProfileData objects.
        - *(dict) --*

          The data associated with a network profile.
          - **NetworkProfileArn** *(string) --*

            The ARN of the network profile associated with a device.
    """


_RequiredClientSearchNetworkProfilesSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchNetworkProfilesSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchNetworkProfilesSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchNetworkProfilesSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchNetworkProfilesSortCriteriaTypeDef(
    _RequiredClientSearchNetworkProfilesSortCriteriaTypeDef,
    _OptionalClientSearchNetworkProfilesSortCriteriaTypeDef,
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredClientSearchProfilesFiltersTypeDef = TypedDict(
    "_RequiredClientSearchProfilesFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchProfilesFiltersTypeDef = TypedDict(
    "_OptionalClientSearchProfilesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchProfilesFiltersTypeDef(
    _RequiredClientSearchProfilesFiltersTypeDef, _OptionalClientSearchProfilesFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_ClientSearchProfilesResponseProfilesTypeDef = TypedDict(
    "_ClientSearchProfilesResponseProfilesTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": Literal["METRIC", "IMPERIAL"],
        "TemperatureUnit": Literal["FAHRENHEIT", "CELSIUS"],
        "WakeWord": Literal["ALEXA", "AMAZON", "ECHO", "COMPUTER"],
        "Locale": str,
    },
    total=False,
)


class ClientSearchProfilesResponseProfilesTypeDef(_ClientSearchProfilesResponseProfilesTypeDef):
    """
    - *(dict) --*

      The data of a room profile.
      - **ProfileArn** *(string) --*

        The ARN of a room profile.
    """


_ClientSearchProfilesResponseTypeDef = TypedDict(
    "_ClientSearchProfilesResponseTypeDef",
    {
        "Profiles": List[ClientSearchProfilesResponseProfilesTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchProfilesResponseTypeDef(_ClientSearchProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **Profiles** *(list) --*

        The profiles that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          The data of a room profile.
          - **ProfileArn** *(string) --*

            The ARN of a room profile.
    """


_RequiredClientSearchProfilesSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchProfilesSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchProfilesSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchProfilesSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchProfilesSortCriteriaTypeDef(
    _RequiredClientSearchProfilesSortCriteriaTypeDef,
    _OptionalClientSearchProfilesSortCriteriaTypeDef,
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredClientSearchRoomsFiltersTypeDef = TypedDict(
    "_RequiredClientSearchRoomsFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchRoomsFiltersTypeDef = TypedDict(
    "_OptionalClientSearchRoomsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchRoomsFiltersTypeDef(
    _RequiredClientSearchRoomsFiltersTypeDef, _OptionalClientSearchRoomsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_ClientSearchRoomsResponseRoomsTypeDef = TypedDict(
    "_ClientSearchRoomsResponseRoomsTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
        "ProfileName": str,
    },
    total=False,
)


class ClientSearchRoomsResponseRoomsTypeDef(_ClientSearchRoomsResponseRoomsTypeDef):
    """
    - *(dict) --*

      The data of a room.
      - **RoomArn** *(string) --*

        The ARN of a room.
    """


_ClientSearchRoomsResponseTypeDef = TypedDict(
    "_ClientSearchRoomsResponseTypeDef",
    {"Rooms": List[ClientSearchRoomsResponseRoomsTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)


class ClientSearchRoomsResponseTypeDef(_ClientSearchRoomsResponseTypeDef):
    """
    - *(dict) --*

      - **Rooms** *(list) --*

        The rooms that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          The data of a room.
          - **RoomArn** *(string) --*

            The ARN of a room.
    """


_RequiredClientSearchRoomsSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchRoomsSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchRoomsSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchRoomsSortCriteriaTypeDef", {"Value": Literal["ASC", "DESC"]}, total=False
)


class ClientSearchRoomsSortCriteriaTypeDef(
    _RequiredClientSearchRoomsSortCriteriaTypeDef, _OptionalClientSearchRoomsSortCriteriaTypeDef
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredClientSearchSkillGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientSearchSkillGroupsFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchSkillGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientSearchSkillGroupsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchSkillGroupsFiltersTypeDef(
    _RequiredClientSearchSkillGroupsFiltersTypeDef, _OptionalClientSearchSkillGroupsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_ClientSearchSkillGroupsResponseSkillGroupsTypeDef = TypedDict(
    "_ClientSearchSkillGroupsResponseSkillGroupsTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)


class ClientSearchSkillGroupsResponseSkillGroupsTypeDef(
    _ClientSearchSkillGroupsResponseSkillGroupsTypeDef
):
    """
    - *(dict) --*

      The attributes of a skill group.
      - **SkillGroupArn** *(string) --*

        The skill group ARN of a skill group.
    """


_ClientSearchSkillGroupsResponseTypeDef = TypedDict(
    "_ClientSearchSkillGroupsResponseTypeDef",
    {
        "SkillGroups": List[ClientSearchSkillGroupsResponseSkillGroupsTypeDef],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)


class ClientSearchSkillGroupsResponseTypeDef(_ClientSearchSkillGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **SkillGroups** *(list) --*

        The skill groups that meet the filter criteria, in sort order.
        - *(dict) --*

          The attributes of a skill group.
          - **SkillGroupArn** *(string) --*

            The skill group ARN of a skill group.
    """


_RequiredClientSearchSkillGroupsSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchSkillGroupsSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchSkillGroupsSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchSkillGroupsSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class ClientSearchSkillGroupsSortCriteriaTypeDef(
    _RequiredClientSearchSkillGroupsSortCriteriaTypeDef,
    _OptionalClientSearchSkillGroupsSortCriteriaTypeDef,
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredClientSearchUsersFiltersTypeDef = TypedDict(
    "_RequiredClientSearchUsersFiltersTypeDef", {"Key": str}
)
_OptionalClientSearchUsersFiltersTypeDef = TypedDict(
    "_OptionalClientSearchUsersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSearchUsersFiltersTypeDef(
    _RequiredClientSearchUsersFiltersTypeDef, _OptionalClientSearchUsersFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_ClientSearchUsersResponseUsersTypeDef = TypedDict(
    "_ClientSearchUsersResponseUsersTypeDef",
    {
        "UserArn": str,
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "EnrollmentStatus": Literal[
            "INITIALIZED", "PENDING", "REGISTERED", "DISASSOCIATING", "DEREGISTERING"
        ],
        "EnrollmentId": str,
    },
    total=False,
)


class ClientSearchUsersResponseUsersTypeDef(_ClientSearchUsersResponseUsersTypeDef):
    """
    - *(dict) --*

      Information related to a user.
      - **UserArn** *(string) --*

        The ARN of a user.
    """


_ClientSearchUsersResponseTypeDef = TypedDict(
    "_ClientSearchUsersResponseTypeDef",
    {"Users": List[ClientSearchUsersResponseUsersTypeDef], "NextToken": str, "TotalCount": int},
    total=False,
)


class ClientSearchUsersResponseTypeDef(_ClientSearchUsersResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        The users that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          Information related to a user.
          - **UserArn** *(string) --*

            The ARN of a user.
    """


_RequiredClientSearchUsersSortCriteriaTypeDef = TypedDict(
    "_RequiredClientSearchUsersSortCriteriaTypeDef", {"Key": str}
)
_OptionalClientSearchUsersSortCriteriaTypeDef = TypedDict(
    "_OptionalClientSearchUsersSortCriteriaTypeDef", {"Value": Literal["ASC", "DESC"]}, total=False
)


class ClientSearchUsersSortCriteriaTypeDef(
    _RequiredClientSearchUsersSortCriteriaTypeDef, _OptionalClientSearchUsersSortCriteriaTypeDef
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_ClientSendAnnouncementContentAudioListTypeDef = TypedDict(
    "_ClientSendAnnouncementContentAudioListTypeDef", {"Locale": str, "Location": str}, total=False
)


class ClientSendAnnouncementContentAudioListTypeDef(_ClientSendAnnouncementContentAudioListTypeDef):
    pass


_ClientSendAnnouncementContentSsmlListTypeDef = TypedDict(
    "_ClientSendAnnouncementContentSsmlListTypeDef", {"Locale": str, "Value": str}, total=False
)


class ClientSendAnnouncementContentSsmlListTypeDef(_ClientSendAnnouncementContentSsmlListTypeDef):
    pass


_RequiredClientSendAnnouncementContentTextListTypeDef = TypedDict(
    "_RequiredClientSendAnnouncementContentTextListTypeDef", {"Locale": str}
)
_OptionalClientSendAnnouncementContentTextListTypeDef = TypedDict(
    "_OptionalClientSendAnnouncementContentTextListTypeDef", {"Value": str}, total=False
)


class ClientSendAnnouncementContentTextListTypeDef(
    _RequiredClientSendAnnouncementContentTextListTypeDef,
    _OptionalClientSendAnnouncementContentTextListTypeDef,
):
    """
    - *(dict) --*

      The text message.
      - **Locale** *(string) --***[REQUIRED]**

        The locale of the text message. Currently, en-US is supported.
    """


_ClientSendAnnouncementContentTypeDef = TypedDict(
    "_ClientSendAnnouncementContentTypeDef",
    {
        "TextList": List[ClientSendAnnouncementContentTextListTypeDef],
        "SsmlList": List[ClientSendAnnouncementContentSsmlListTypeDef],
        "AudioList": List[ClientSendAnnouncementContentAudioListTypeDef],
    },
    total=False,
)


class ClientSendAnnouncementContentTypeDef(_ClientSendAnnouncementContentTypeDef):
    """
    The announcement content. This can contain only one of the three possible announcement types
    (text, SSML or audio).
    - **TextList** *(list) --*

      The list of text messages.
      - *(dict) --*

        The text message.
        - **Locale** *(string) --***[REQUIRED]**

          The locale of the text message. Currently, en-US is supported.
    """


_ClientSendAnnouncementResponseTypeDef = TypedDict(
    "_ClientSendAnnouncementResponseTypeDef", {"AnnouncementArn": str}, total=False
)


class ClientSendAnnouncementResponseTypeDef(_ClientSendAnnouncementResponseTypeDef):
    """
    - *(dict) --*

      - **AnnouncementArn** *(string) --*

        The identifier of the announcement.
    """


_RequiredClientSendAnnouncementRoomFiltersTypeDef = TypedDict(
    "_RequiredClientSendAnnouncementRoomFiltersTypeDef", {"Key": str}
)
_OptionalClientSendAnnouncementRoomFiltersTypeDef = TypedDict(
    "_OptionalClientSendAnnouncementRoomFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientSendAnnouncementRoomFiltersTypeDef(
    _RequiredClientSendAnnouncementRoomFiltersTypeDef,
    _OptionalClientSendAnnouncementRoomFiltersTypeDef,
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that can be associated with a resource.
      - **Key** *(string) --***[REQUIRED]**

        The key of a tag. Tag keys are case-sensitive.
    """


_ClientUpdateBusinessReportScheduleRecurrenceTypeDef = TypedDict(
    "_ClientUpdateBusinessReportScheduleRecurrenceTypeDef", {"StartDate": str}, total=False
)


class ClientUpdateBusinessReportScheduleRecurrenceTypeDef(
    _ClientUpdateBusinessReportScheduleRecurrenceTypeDef
):
    """
    The recurrence of the reports.
    - **StartDate** *(string) --*

      The start date.
    """


_RequiredClientUpdateConferenceProviderIPDialInTypeDef = TypedDict(
    "_RequiredClientUpdateConferenceProviderIPDialInTypeDef", {"Endpoint": str}
)
_OptionalClientUpdateConferenceProviderIPDialInTypeDef = TypedDict(
    "_OptionalClientUpdateConferenceProviderIPDialInTypeDef",
    {"CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)


class ClientUpdateConferenceProviderIPDialInTypeDef(
    _RequiredClientUpdateConferenceProviderIPDialInTypeDef,
    _OptionalClientUpdateConferenceProviderIPDialInTypeDef,
):
    """
    The IP endpoint and protocol for calling.
    - **Endpoint** *(string) --***[REQUIRED]**

      The IP address.
    """


_ClientUpdateConferenceProviderMeetingSettingTypeDef = TypedDict(
    "_ClientUpdateConferenceProviderMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
)


class ClientUpdateConferenceProviderMeetingSettingTypeDef(
    _ClientUpdateConferenceProviderMeetingSettingTypeDef
):
    """
    The meeting settings for the conference provider.
    - **RequirePin** *(string) --***[REQUIRED]**

      The values that indicate whether the pin is always required.
    """


_RequiredClientUpdateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_RequiredClientUpdateConferenceProviderPSTNDialInTypeDef", {"CountryCode": str}
)
_OptionalClientUpdateConferenceProviderPSTNDialInTypeDef = TypedDict(
    "_OptionalClientUpdateConferenceProviderPSTNDialInTypeDef",
    {"PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)


class ClientUpdateConferenceProviderPSTNDialInTypeDef(
    _RequiredClientUpdateConferenceProviderPSTNDialInTypeDef,
    _OptionalClientUpdateConferenceProviderPSTNDialInTypeDef,
):
    """
    The information for PSTN conferencing.
    - **CountryCode** *(string) --***[REQUIRED]**

      The zip code.
    """


_RequiredClientUpdateContactPhoneNumbersTypeDef = TypedDict(
    "_RequiredClientUpdateContactPhoneNumbersTypeDef", {"Number": str}
)
_OptionalClientUpdateContactPhoneNumbersTypeDef = TypedDict(
    "_OptionalClientUpdateContactPhoneNumbersTypeDef",
    {"Type": Literal["MOBILE", "WORK", "HOME"]},
    total=False,
)


class ClientUpdateContactPhoneNumbersTypeDef(
    _RequiredClientUpdateContactPhoneNumbersTypeDef, _OptionalClientUpdateContactPhoneNumbersTypeDef
):
    """
    - *(dict) --*

      The phone number for the contact containing the raw number and phone number type.
      - **Number** *(string) --***[REQUIRED]**

        The raw value of the phone number.
    """


_RequiredClientUpdateContactSipAddressesTypeDef = TypedDict(
    "_RequiredClientUpdateContactSipAddressesTypeDef", {"Uri": str}
)
_OptionalClientUpdateContactSipAddressesTypeDef = TypedDict(
    "_OptionalClientUpdateContactSipAddressesTypeDef", {"Type": str}, total=False
)


class ClientUpdateContactSipAddressesTypeDef(
    _RequiredClientUpdateContactSipAddressesTypeDef, _OptionalClientUpdateContactSipAddressesTypeDef
):
    """
    - *(dict) --*

      The SIP address for the contact containing the URI and SIP address type.
      - **Uri** *(string) --***[REQUIRED]**

        The URI for the SIP address.
    """


_ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef = TypedDict(
    "_ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": Literal[
            "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
        ],
        "Enabled": bool,
    },
    total=False,
)


class ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef(
    _ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef
):
    pass


_ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef = TypedDict(
    "_ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef",
    {"DurationInMinutes": int, "Enabled": bool},
    total=False,
)


class ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef(
    _ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef
):
    pass


_ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef = TypedDict(
    "_ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef",
    {"ReleaseAfterMinutes": int, "Enabled": bool},
    total=False,
)


class ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef(
    _ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef
):
    pass


_ClientUpdateProfileMeetingRoomConfigurationTypeDef = TypedDict(
    "_ClientUpdateProfileMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": ClientUpdateProfileMeetingRoomConfigurationEndOfMeetingReminderTypeDef,
        "InstantBooking": ClientUpdateProfileMeetingRoomConfigurationInstantBookingTypeDef,
        "RequireCheckIn": ClientUpdateProfileMeetingRoomConfigurationRequireCheckInTypeDef,
    },
    total=False,
)


class ClientUpdateProfileMeetingRoomConfigurationTypeDef(
    _ClientUpdateProfileMeetingRoomConfigurationTypeDef
):
    """
    The updated meeting room settings of a room profile.
    - **RoomUtilizationMetricsEnabled** *(boolean) --*

      Whether room utilization metrics are enabled or not.
    """


_ListBusinessReportSchedulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBusinessReportSchedulesPaginatePaginationConfigTypeDef(
    _ListBusinessReportSchedulesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef",
    {"Interval": Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"]},
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef
):
    pass


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef",
    {"Path": str, "BucketName": str},
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef
):
    pass


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef",
    {
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED"],
        "FailureCode": Literal["ACCESS_DENIED", "NO_SUCH_BUCKET", "INTERNAL_FAILURE"],
        "S3Location": ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportS3LocationTypeDef,
        "DeliveryTime": datetime,
        "DownloadUrl": str,
    },
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef
):
    pass


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef",
    {"StartDate": str},
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef
):
    pass


_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef",
    {
        "ScheduleArn": str,
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": Literal["CSV", "CSV_ZIP"],
        "ContentRange": ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesContentRangeTypeDef,
        "Recurrence": ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesRecurrenceTypeDef,
        "LastBusinessReport": ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesLastBusinessReportTypeDef,
    },
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef(
    _ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef
):
    """
    - *(dict) --*

      The schedule of the usage report.
      - **ScheduleArn** *(string) --*

        The ARN of the business report schedule.
    """


_ListBusinessReportSchedulesPaginateResponseTypeDef = TypedDict(
    "_ListBusinessReportSchedulesPaginateResponseTypeDef",
    {
        "BusinessReportSchedules": List[
            ListBusinessReportSchedulesPaginateResponseBusinessReportSchedulesTypeDef
        ]
    },
    total=False,
)


class ListBusinessReportSchedulesPaginateResponseTypeDef(
    _ListBusinessReportSchedulesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **BusinessReportSchedules** *(list) --*

        The schedule of the reports.
        - *(dict) --*

          The schedule of the usage report.
          - **ScheduleArn** *(string) --*

            The ARN of the business report schedule.
    """


_ListConferenceProvidersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConferenceProvidersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConferenceProvidersPaginatePaginationConfigTypeDef(
    _ListConferenceProvidersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef",
    {"Endpoint": str, "CommsProtocol": Literal["SIP", "SIPS", "H323"]},
    total=False,
)


class ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef(
    _ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef
):
    pass


_ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef",
    {"RequirePin": Literal["YES", "NO", "OPTIONAL"]},
    total=False,
)


class ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef(
    _ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef
):
    pass


_ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef",
    {"CountryCode": str, "PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
    total=False,
)


class ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef(
    _ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef
):
    pass


_ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": Literal[
            "CHIME",
            "BLUEJEANS",
            "FUZE",
            "GOOGLE_HANGOUTS",
            "POLYCOM",
            "RINGCENTRAL",
            "SKYPE_FOR_BUSINESS",
            "WEBEX",
            "ZOOM",
            "CUSTOM",
        ],
        "IPDialIn": ListConferenceProvidersPaginateResponseConferenceProvidersIPDialInTypeDef,
        "PSTNDialIn": ListConferenceProvidersPaginateResponseConferenceProvidersPSTNDialInTypeDef,
        "MeetingSetting": ListConferenceProvidersPaginateResponseConferenceProvidersMeetingSettingTypeDef,
    },
    total=False,
)


class ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef(
    _ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef
):
    """
    - *(dict) --*

      An entity that provides a conferencing solution. Alexa for Business acts as the voice
      interface and mediator that connects users to their preferred conference provider. Examples of
      conference providers include Amazon Chime, Zoom, Cisco, and Polycom.
      - **Arn** *(string) --*

        The ARN of the newly created conference provider.
    """


_ListConferenceProvidersPaginateResponseTypeDef = TypedDict(
    "_ListConferenceProvidersPaginateResponseTypeDef",
    {
        "ConferenceProviders": List[
            ListConferenceProvidersPaginateResponseConferenceProvidersTypeDef
        ]
    },
    total=False,
)


class ListConferenceProvidersPaginateResponseTypeDef(
    _ListConferenceProvidersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ConferenceProviders** *(list) --*

        The conference providers.
        - *(dict) --*

          An entity that provides a conferencing solution. Alexa for Business acts as the voice
          interface and mediator that connects users to their preferred conference provider.
          Examples of conference providers include Amazon Chime, Zoom, Cisco, and Polycom.
          - **Arn** *(string) --*

            The ARN of the newly created conference provider.
    """


_ListDeviceEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceEventsPaginatePaginationConfigTypeDef(
    _ListDeviceEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeviceEventsPaginateResponseDeviceEventsTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseDeviceEventsTypeDef",
    {"Type": Literal["CONNECTION_STATUS", "DEVICE_STATUS"], "Value": str, "Timestamp": datetime},
    total=False,
)


class ListDeviceEventsPaginateResponseDeviceEventsTypeDef(
    _ListDeviceEventsPaginateResponseDeviceEventsTypeDef
):
    """
    - *(dict) --*

      The list of device events.
      - **Type** *(string) --*

        The type of device event.
    """


_ListDeviceEventsPaginateResponseTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseTypeDef",
    {"DeviceEvents": List[ListDeviceEventsPaginateResponseDeviceEventsTypeDef]},
    total=False,
)


class ListDeviceEventsPaginateResponseTypeDef(_ListDeviceEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DeviceEvents** *(list) --*

        The device events requested for the device ARN.
        - *(dict) --*

          The list of device events.
          - **Type** *(string) --*

            The type of device event.
    """


_ListSkillsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSkillsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSkillsPaginatePaginationConfigTypeDef(_ListSkillsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSkillsPaginateResponseSkillSummariesTypeDef = TypedDict(
    "_ListSkillsPaginateResponseSkillSummariesTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "SupportsLinking": bool,
        "EnablementType": Literal["ENABLED", "PENDING"],
        "SkillType": Literal["PUBLIC", "PRIVATE"],
    },
    total=False,
)


class ListSkillsPaginateResponseSkillSummariesTypeDef(
    _ListSkillsPaginateResponseSkillSummariesTypeDef
):
    """
    - *(dict) --*

      The summary of skills.
      - **SkillId** *(string) --*

        The ARN of the skill summary.
    """


_ListSkillsPaginateResponseTypeDef = TypedDict(
    "_ListSkillsPaginateResponseTypeDef",
    {"SkillSummaries": List[ListSkillsPaginateResponseSkillSummariesTypeDef]},
    total=False,
)


class ListSkillsPaginateResponseTypeDef(_ListSkillsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SkillSummaries** *(list) --*

        The list of enabled skills requested. Required.
        - *(dict) --*

          The summary of skills.
          - **SkillId** *(string) --*

            The ARN of the skill summary.
    """


_ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef(
    _ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef = TypedDict(
    "_ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef",
    {"CategoryId": int, "CategoryName": str},
    total=False,
)


class ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef(
    _ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef
):
    """
    - *(dict) --*

      The skill store category that is shown. Alexa skills are assigned a specific skill category
      during creation, such as News, Social, and Sports.
      - **CategoryId** *(integer) --*

        The ID of the skill store category.
    """


_ListSkillsStoreCategoriesPaginateResponseTypeDef = TypedDict(
    "_ListSkillsStoreCategoriesPaginateResponseTypeDef",
    {"CategoryList": List[ListSkillsStoreCategoriesPaginateResponseCategoryListTypeDef]},
    total=False,
)


class ListSkillsStoreCategoriesPaginateResponseTypeDef(
    _ListSkillsStoreCategoriesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **CategoryList** *(list) --*

        The list of categories.
        - *(dict) --*

          The skill store category that is shown. Alexa skills are assigned a specific skill
          category during creation, such as News, Social, and Sports.
          - **CategoryId** *(integer) --*

            The ID of the skill store category.
    """


_ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef",
    {"DeveloperName": str, "PrivacyPolicy": str, "Email": str, "Url": str},
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef
):
    pass


_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef",
    {
        "ProductDescription": str,
        "InvocationPhrase": str,
        "ReleaseDate": str,
        "EndUserLicenseAgreement": str,
        "GenericKeywords": List[str],
        "BulletPoints": List[str],
        "NewInThisVersionBulletPoints": List[str],
        "SkillTypes": List[str],
        "Reviews": Dict[str, str],
        "DeveloperInfo": ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsDeveloperInfoTypeDef,
    },
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef
):
    pass


_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "ShortDescription": str,
        "IconUrl": str,
        "SampleUtterances": List[str],
        "SkillDetails": ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsSkillDetailsTypeDef,
        "SupportsLinking": bool,
    },
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef
):
    """
    - *(dict) --*

      The detailed information about an Alexa skill.
      - **SkillId** *(string) --*

        The ARN of the skill.
    """


_ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef = TypedDict(
    "_ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef",
    {
        "SkillsStoreSkills": List[
            ListSkillsStoreSkillsByCategoryPaginateResponseSkillsStoreSkillsTypeDef
        ]
    },
    total=False,
)


class ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef(
    _ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SkillsStoreSkills** *(list) --*

        The skill store skills.
        - *(dict) --*

          The detailed information about an Alexa skill.
          - **SkillId** *(string) --*

            The ARN of the skill.
    """


_ListSmartHomeAppliancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSmartHomeAppliancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSmartHomeAppliancesPaginatePaginationConfigTypeDef(
    _ListSmartHomeAppliancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef = TypedDict(
    "_ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef",
    {"FriendlyName": str, "Description": str, "ManufacturerName": str},
    total=False,
)


class ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef(
    _ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef
):
    """
    - *(dict) --*

      A smart home appliance that can connect to a central system. Any domestic device can be a
      smart appliance.
      - **FriendlyName** *(string) --*

        The friendly name of the smart home appliance.
    """


_ListSmartHomeAppliancesPaginateResponseTypeDef = TypedDict(
    "_ListSmartHomeAppliancesPaginateResponseTypeDef",
    {
        "SmartHomeAppliances": List[
            ListSmartHomeAppliancesPaginateResponseSmartHomeAppliancesTypeDef
        ]
    },
    total=False,
)


class ListSmartHomeAppliancesPaginateResponseTypeDef(
    _ListSmartHomeAppliancesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SmartHomeAppliances** *(list) --*

        The smart home appliances.
        - *(dict) --*

          A smart home appliance that can connect to a central system. Any domestic device can be a
          smart appliance.
          - **FriendlyName** *(string) --*

            The friendly name of the smart home appliance.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsPaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagsTypeDef(_ListTagsPaginateResponseTagsTypeDef):
    """
    - *(dict) --*

      A key-value pair that can be associated with a resource.
      - **Key** *(string) --*

        The key of a tag. Tag keys are case-sensitive.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"Tags": List[ListTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags requested for the specified resource.
        - *(dict) --*

          A key-value pair that can be associated with a resource.
          - **Key** *(string) --*

            The key of a tag. Tag keys are case-sensitive.
    """


_RequiredSearchDevicesPaginateFiltersTypeDef = TypedDict(
    "_RequiredSearchDevicesPaginateFiltersTypeDef", {"Key": str}
)
_OptionalSearchDevicesPaginateFiltersTypeDef = TypedDict(
    "_OptionalSearchDevicesPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class SearchDevicesPaginateFiltersTypeDef(
    _RequiredSearchDevicesPaginateFiltersTypeDef, _OptionalSearchDevicesPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_SearchDevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchDevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchDevicesPaginatePaginationConfigTypeDef(_SearchDevicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef = TypedDict(
    "_SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef",
    {
        "Feature": Literal[
            "BLUETOOTH",
            "VOLUME",
            "NOTIFICATIONS",
            "LISTS",
            "SKILLS",
            "NETWORK_PROFILE",
            "SETTINGS",
            "ALL",
        ],
        "Code": Literal[
            "DEVICE_SOFTWARE_UPDATE_NEEDED",
            "DEVICE_WAS_OFFLINE",
            "CREDENTIALS_ACCESS_FAILURE",
            "TLS_VERSION_MISMATCH",
            "ASSOCIATION_REJECTION",
            "AUTHENTICATION_FAILURE",
            "DHCP_FAILURE",
            "INTERNET_UNAVAILABLE",
            "DNS_FAILURE",
            "UNKNOWN_FAILURE",
            "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
            "INVALID_CERTIFICATE_AUTHORITY",
            "NETWORK_PROFILE_NOT_FOUND",
            "INVALID_PASSWORD_STATE",
            "PASSWORD_NOT_FOUND",
        ],
    },
    total=False,
)


class SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef(
    _SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
):
    pass


_SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef = TypedDict(
    "_SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List[
            SearchDevicesPaginateResponseDevicesDeviceStatusInfoDeviceStatusDetailsTypeDef
        ],
        "ConnectionStatus": Literal["ONLINE", "OFFLINE"],
    },
    total=False,
)


class SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef(
    _SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef
):
    pass


_SearchDevicesPaginateResponseDevicesTypeDef = TypedDict(
    "_SearchDevicesPaginateResponseDevicesTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "DeviceStatus": Literal["READY", "PENDING", "WAS_OFFLINE", "DEREGISTERED", "FAILED"],
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "RoomArn": str,
        "RoomName": str,
        "DeviceStatusInfo": SearchDevicesPaginateResponseDevicesDeviceStatusInfoTypeDef,
    },
    total=False,
)


class SearchDevicesPaginateResponseDevicesTypeDef(_SearchDevicesPaginateResponseDevicesTypeDef):
    """
    - *(dict) --*

      Device attributes.
      - **DeviceArn** *(string) --*

        The ARN of a device.
    """


_SearchDevicesPaginateResponseTypeDef = TypedDict(
    "_SearchDevicesPaginateResponseTypeDef",
    {"Devices": List[SearchDevicesPaginateResponseDevicesTypeDef], "TotalCount": int},
    total=False,
)


class SearchDevicesPaginateResponseTypeDef(_SearchDevicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Devices** *(list) --*

        The devices that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          Device attributes.
          - **DeviceArn** *(string) --*

            The ARN of a device.
    """


_RequiredSearchDevicesPaginateSortCriteriaTypeDef = TypedDict(
    "_RequiredSearchDevicesPaginateSortCriteriaTypeDef", {"Key": str}
)
_OptionalSearchDevicesPaginateSortCriteriaTypeDef = TypedDict(
    "_OptionalSearchDevicesPaginateSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class SearchDevicesPaginateSortCriteriaTypeDef(
    _RequiredSearchDevicesPaginateSortCriteriaTypeDef,
    _OptionalSearchDevicesPaginateSortCriteriaTypeDef,
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredSearchProfilesPaginateFiltersTypeDef = TypedDict(
    "_RequiredSearchProfilesPaginateFiltersTypeDef", {"Key": str}
)
_OptionalSearchProfilesPaginateFiltersTypeDef = TypedDict(
    "_OptionalSearchProfilesPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class SearchProfilesPaginateFiltersTypeDef(
    _RequiredSearchProfilesPaginateFiltersTypeDef, _OptionalSearchProfilesPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_SearchProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchProfilesPaginatePaginationConfigTypeDef(_SearchProfilesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchProfilesPaginateResponseProfilesTypeDef = TypedDict(
    "_SearchProfilesPaginateResponseProfilesTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": Literal["METRIC", "IMPERIAL"],
        "TemperatureUnit": Literal["FAHRENHEIT", "CELSIUS"],
        "WakeWord": Literal["ALEXA", "AMAZON", "ECHO", "COMPUTER"],
        "Locale": str,
    },
    total=False,
)


class SearchProfilesPaginateResponseProfilesTypeDef(_SearchProfilesPaginateResponseProfilesTypeDef):
    """
    - *(dict) --*

      The data of a room profile.
      - **ProfileArn** *(string) --*

        The ARN of a room profile.
    """


_SearchProfilesPaginateResponseTypeDef = TypedDict(
    "_SearchProfilesPaginateResponseTypeDef",
    {"Profiles": List[SearchProfilesPaginateResponseProfilesTypeDef], "TotalCount": int},
    total=False,
)


class SearchProfilesPaginateResponseTypeDef(_SearchProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Profiles** *(list) --*

        The profiles that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          The data of a room profile.
          - **ProfileArn** *(string) --*

            The ARN of a room profile.
    """


_RequiredSearchProfilesPaginateSortCriteriaTypeDef = TypedDict(
    "_RequiredSearchProfilesPaginateSortCriteriaTypeDef", {"Key": str}
)
_OptionalSearchProfilesPaginateSortCriteriaTypeDef = TypedDict(
    "_OptionalSearchProfilesPaginateSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class SearchProfilesPaginateSortCriteriaTypeDef(
    _RequiredSearchProfilesPaginateSortCriteriaTypeDef,
    _OptionalSearchProfilesPaginateSortCriteriaTypeDef,
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredSearchRoomsPaginateFiltersTypeDef = TypedDict(
    "_RequiredSearchRoomsPaginateFiltersTypeDef", {"Key": str}
)
_OptionalSearchRoomsPaginateFiltersTypeDef = TypedDict(
    "_OptionalSearchRoomsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class SearchRoomsPaginateFiltersTypeDef(
    _RequiredSearchRoomsPaginateFiltersTypeDef, _OptionalSearchRoomsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_SearchRoomsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchRoomsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchRoomsPaginatePaginationConfigTypeDef(_SearchRoomsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchRoomsPaginateResponseRoomsTypeDef = TypedDict(
    "_SearchRoomsPaginateResponseRoomsTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
        "ProfileName": str,
    },
    total=False,
)


class SearchRoomsPaginateResponseRoomsTypeDef(_SearchRoomsPaginateResponseRoomsTypeDef):
    """
    - *(dict) --*

      The data of a room.
      - **RoomArn** *(string) --*

        The ARN of a room.
    """


_SearchRoomsPaginateResponseTypeDef = TypedDict(
    "_SearchRoomsPaginateResponseTypeDef",
    {"Rooms": List[SearchRoomsPaginateResponseRoomsTypeDef], "TotalCount": int},
    total=False,
)


class SearchRoomsPaginateResponseTypeDef(_SearchRoomsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Rooms** *(list) --*

        The rooms that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          The data of a room.
          - **RoomArn** *(string) --*

            The ARN of a room.
    """


_RequiredSearchRoomsPaginateSortCriteriaTypeDef = TypedDict(
    "_RequiredSearchRoomsPaginateSortCriteriaTypeDef", {"Key": str}
)
_OptionalSearchRoomsPaginateSortCriteriaTypeDef = TypedDict(
    "_OptionalSearchRoomsPaginateSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class SearchRoomsPaginateSortCriteriaTypeDef(
    _RequiredSearchRoomsPaginateSortCriteriaTypeDef, _OptionalSearchRoomsPaginateSortCriteriaTypeDef
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredSearchSkillGroupsPaginateFiltersTypeDef = TypedDict(
    "_RequiredSearchSkillGroupsPaginateFiltersTypeDef", {"Key": str}
)
_OptionalSearchSkillGroupsPaginateFiltersTypeDef = TypedDict(
    "_OptionalSearchSkillGroupsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class SearchSkillGroupsPaginateFiltersTypeDef(
    _RequiredSearchSkillGroupsPaginateFiltersTypeDef,
    _OptionalSearchSkillGroupsPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_SearchSkillGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchSkillGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchSkillGroupsPaginatePaginationConfigTypeDef(
    _SearchSkillGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchSkillGroupsPaginateResponseSkillGroupsTypeDef = TypedDict(
    "_SearchSkillGroupsPaginateResponseSkillGroupsTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)


class SearchSkillGroupsPaginateResponseSkillGroupsTypeDef(
    _SearchSkillGroupsPaginateResponseSkillGroupsTypeDef
):
    """
    - *(dict) --*

      The attributes of a skill group.
      - **SkillGroupArn** *(string) --*

        The skill group ARN of a skill group.
    """


_SearchSkillGroupsPaginateResponseTypeDef = TypedDict(
    "_SearchSkillGroupsPaginateResponseTypeDef",
    {"SkillGroups": List[SearchSkillGroupsPaginateResponseSkillGroupsTypeDef], "TotalCount": int},
    total=False,
)


class SearchSkillGroupsPaginateResponseTypeDef(_SearchSkillGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SkillGroups** *(list) --*

        The skill groups that meet the filter criteria, in sort order.
        - *(dict) --*

          The attributes of a skill group.
          - **SkillGroupArn** *(string) --*

            The skill group ARN of a skill group.
    """


_RequiredSearchSkillGroupsPaginateSortCriteriaTypeDef = TypedDict(
    "_RequiredSearchSkillGroupsPaginateSortCriteriaTypeDef", {"Key": str}
)
_OptionalSearchSkillGroupsPaginateSortCriteriaTypeDef = TypedDict(
    "_OptionalSearchSkillGroupsPaginateSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class SearchSkillGroupsPaginateSortCriteriaTypeDef(
    _RequiredSearchSkillGroupsPaginateSortCriteriaTypeDef,
    _OptionalSearchSkillGroupsPaginateSortCriteriaTypeDef,
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """


_RequiredSearchUsersPaginateFiltersTypeDef = TypedDict(
    "_RequiredSearchUsersPaginateFiltersTypeDef", {"Key": str}
)
_OptionalSearchUsersPaginateFiltersTypeDef = TypedDict(
    "_OptionalSearchUsersPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class SearchUsersPaginateFiltersTypeDef(
    _RequiredSearchUsersPaginateFiltersTypeDef, _OptionalSearchUsersPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return a more specific list of results. Filters
      can be used to match a set of resources by various criteria.
      - **Key** *(string) --***[REQUIRED]**

        The key of a filter.
    """


_SearchUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchUsersPaginatePaginationConfigTypeDef(_SearchUsersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchUsersPaginateResponseUsersTypeDef = TypedDict(
    "_SearchUsersPaginateResponseUsersTypeDef",
    {
        "UserArn": str,
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "EnrollmentStatus": Literal[
            "INITIALIZED", "PENDING", "REGISTERED", "DISASSOCIATING", "DEREGISTERING"
        ],
        "EnrollmentId": str,
    },
    total=False,
)


class SearchUsersPaginateResponseUsersTypeDef(_SearchUsersPaginateResponseUsersTypeDef):
    """
    - *(dict) --*

      Information related to a user.
      - **UserArn** *(string) --*

        The ARN of a user.
    """


_SearchUsersPaginateResponseTypeDef = TypedDict(
    "_SearchUsersPaginateResponseTypeDef",
    {"Users": List[SearchUsersPaginateResponseUsersTypeDef], "TotalCount": int},
    total=False,
)


class SearchUsersPaginateResponseTypeDef(_SearchUsersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        The users that meet the specified set of filter criteria, in sort order.
        - *(dict) --*

          Information related to a user.
          - **UserArn** *(string) --*

            The ARN of a user.
    """


_RequiredSearchUsersPaginateSortCriteriaTypeDef = TypedDict(
    "_RequiredSearchUsersPaginateSortCriteriaTypeDef", {"Key": str}
)
_OptionalSearchUsersPaginateSortCriteriaTypeDef = TypedDict(
    "_OptionalSearchUsersPaginateSortCriteriaTypeDef",
    {"Value": Literal["ASC", "DESC"]},
    total=False,
)


class SearchUsersPaginateSortCriteriaTypeDef(
    _RequiredSearchUsersPaginateSortCriteriaTypeDef, _OptionalSearchUsersPaginateSortCriteriaTypeDef
):
    """
    - *(dict) --*

      An object representing a sort criteria.
      - **Key** *(string) --***[REQUIRED]**

        The sort key of a sort object.
    """
