"Main interface for connect service type defs"
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


ClientCreateUserIdentityInfoTypeDef = TypedDict(
    "ClientCreateUserIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)

_RequiredClientCreateUserPhoneConfigTypeDef = TypedDict(
    "_RequiredClientCreateUserPhoneConfigTypeDef",
    {"PhoneType": Literal["SOFT_PHONE", "DESK_PHONE"]},
)
_OptionalClientCreateUserPhoneConfigTypeDef = TypedDict(
    "_OptionalClientCreateUserPhoneConfigTypeDef",
    {"AutoAccept": bool, "AfterContactWorkTimeLimit": int, "DeskPhoneNumber": str},
    total=False,
)


class ClientCreateUserPhoneConfigTypeDef(
    _RequiredClientCreateUserPhoneConfigTypeDef, _OptionalClientCreateUserPhoneConfigTypeDef
):
    pass


ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"UserId": str, "UserArn": str}, total=False
)

ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef = TypedDict(
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef = TypedDict(
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef = TypedDict(
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef = TypedDict(
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef = TypedDict(
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef = TypedDict(
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef",
    {
        "LevelOne": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef,
        "LevelTwo": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef,
        "LevelThree": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef,
        "LevelFour": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef,
        "LevelFive": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef,
    },
    total=False,
)

ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef = TypedDict(
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "LevelId": str,
        "HierarchyPath": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef,
    },
    total=False,
)

ClientDescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "ClientDescribeUserHierarchyGroupResponseTypeDef",
    {"HierarchyGroup": ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef},
    total=False,
)

ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef = TypedDict(
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef = TypedDict(
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef = TypedDict(
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef = TypedDict(
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef = TypedDict(
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef = TypedDict(
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef",
    {
        "LevelOne": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef,
        "LevelTwo": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef,
        "LevelThree": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef,
        "LevelFour": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef,
        "LevelFive": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef,
    },
    total=False,
)

ClientDescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "ClientDescribeUserHierarchyStructureResponseTypeDef",
    {"HierarchyStructure": ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef},
    total=False,
)

ClientDescribeUserResponseUserIdentityInfoTypeDef = TypedDict(
    "ClientDescribeUserResponseUserIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)

ClientDescribeUserResponseUserPhoneConfigTypeDef = TypedDict(
    "ClientDescribeUserResponseUserPhoneConfigTypeDef",
    {
        "PhoneType": Literal["SOFT_PHONE", "DESK_PHONE"],
        "AutoAccept": bool,
        "AfterContactWorkTimeLimit": int,
        "DeskPhoneNumber": str,
    },
    total=False,
)

ClientDescribeUserResponseUserTypeDef = TypedDict(
    "ClientDescribeUserResponseUserTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
        "IdentityInfo": ClientDescribeUserResponseUserIdentityInfoTypeDef,
        "PhoneConfig": ClientDescribeUserResponseUserPhoneConfigTypeDef,
        "DirectoryUserId": str,
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeUserResponseTypeDef = TypedDict(
    "ClientDescribeUserResponseTypeDef",
    {"User": ClientDescribeUserResponseUserTypeDef},
    total=False,
)

ClientGetContactAttributesResponseTypeDef = TypedDict(
    "ClientGetContactAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientGetCurrentMetricDataCurrentMetricsTypeDef = TypedDict(
    "ClientGetCurrentMetricDataCurrentMetricsTypeDef",
    {
        "Name": Literal[
            "AGENTS_ONLINE",
            "AGENTS_AVAILABLE",
            "AGENTS_ON_CALL",
            "AGENTS_NON_PRODUCTIVE",
            "AGENTS_AFTER_CONTACT_WORK",
            "AGENTS_ERROR",
            "AGENTS_STAFFED",
            "CONTACTS_IN_QUEUE",
            "OLDEST_CONTACT_AGE",
            "CONTACTS_SCHEDULED",
            "AGENTS_ON_CONTACT",
            "SLOTS_ACTIVE",
            "SLOTS_AVAILABLE",
        ],
        "Unit": Literal["SECONDS", "COUNT", "PERCENT"],
    },
    total=False,
)

ClientGetCurrentMetricDataFiltersTypeDef = TypedDict(
    "ClientGetCurrentMetricDataFiltersTypeDef",
    {"Queues": List[str], "Channels": List[Literal["VOICE", "CHAT"]]},
    total=False,
)

ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef",
    {
        "Name": Literal[
            "AGENTS_ONLINE",
            "AGENTS_AVAILABLE",
            "AGENTS_ON_CALL",
            "AGENTS_NON_PRODUCTIVE",
            "AGENTS_AFTER_CONTACT_WORK",
            "AGENTS_ERROR",
            "AGENTS_STAFFED",
            "CONTACTS_IN_QUEUE",
            "OLDEST_CONTACT_AGE",
            "CONTACTS_SCHEDULED",
            "AGENTS_ON_CONTACT",
            "SLOTS_ACTIVE",
            "SLOTS_AVAILABLE",
        ],
        "Unit": Literal["SECONDS", "COUNT", "PERCENT"],
    },
    total=False,
)

ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef = TypedDict(
    "ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef",
    {
        "Metric": ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef,
        "Value": float,
    },
    total=False,
)

ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)

ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef = TypedDict(
    "ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": Literal["VOICE", "CHAT"],
    },
    total=False,
)

ClientGetCurrentMetricDataResponseMetricResultsTypeDef = TypedDict(
    "ClientGetCurrentMetricDataResponseMetricResultsTypeDef",
    {
        "Dimensions": ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef,
        "Collections": List[ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef],
    },
    total=False,
)

ClientGetCurrentMetricDataResponseTypeDef = TypedDict(
    "ClientGetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List[ClientGetCurrentMetricDataResponseMetricResultsTypeDef],
        "DataSnapshotTime": datetime,
    },
    total=False,
)

ClientGetFederationTokenResponseCredentialsTypeDef = TypedDict(
    "ClientGetFederationTokenResponseCredentialsTypeDef",
    {
        "AccessToken": str,
        "AccessTokenExpiration": datetime,
        "RefreshToken": str,
        "RefreshTokenExpiration": datetime,
    },
    total=False,
)

ClientGetFederationTokenResponseTypeDef = TypedDict(
    "ClientGetFederationTokenResponseTypeDef",
    {"Credentials": ClientGetFederationTokenResponseCredentialsTypeDef},
    total=False,
)

ClientGetMetricDataFiltersTypeDef = TypedDict(
    "ClientGetMetricDataFiltersTypeDef",
    {"Queues": List[str], "Channels": List[Literal["VOICE", "CHAT"]]},
    total=False,
)

ClientGetMetricDataHistoricalMetricsThresholdTypeDef = TypedDict(
    "ClientGetMetricDataHistoricalMetricsThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)

ClientGetMetricDataHistoricalMetricsTypeDef = TypedDict(
    "ClientGetMetricDataHistoricalMetricsTypeDef",
    {
        "Name": Literal[
            "CONTACTS_QUEUED",
            "CONTACTS_HANDLED",
            "CONTACTS_ABANDONED",
            "CONTACTS_CONSULTED",
            "CONTACTS_AGENT_HUNG_UP_FIRST",
            "CONTACTS_HANDLED_INCOMING",
            "CONTACTS_HANDLED_OUTBOUND",
            "CONTACTS_HOLD_ABANDONS",
            "CONTACTS_TRANSFERRED_IN",
            "CONTACTS_TRANSFERRED_OUT",
            "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
            "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
            "CONTACTS_MISSED",
            "CALLBACK_CONTACTS_HANDLED",
            "API_CONTACTS_HANDLED",
            "OCCUPANCY",
            "HANDLE_TIME",
            "AFTER_CONTACT_WORK_TIME",
            "QUEUED_TIME",
            "ABANDON_TIME",
            "QUEUE_ANSWER_TIME",
            "HOLD_TIME",
            "INTERACTION_TIME",
            "INTERACTION_AND_HOLD_TIME",
            "SERVICE_LEVEL",
        ],
        "Threshold": ClientGetMetricDataHistoricalMetricsThresholdTypeDef,
        "Statistic": Literal["SUM", "MAX", "AVG"],
        "Unit": Literal["SECONDS", "COUNT", "PERCENT"],
    },
    total=False,
)

ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)

ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef",
    {
        "Name": Literal[
            "CONTACTS_QUEUED",
            "CONTACTS_HANDLED",
            "CONTACTS_ABANDONED",
            "CONTACTS_CONSULTED",
            "CONTACTS_AGENT_HUNG_UP_FIRST",
            "CONTACTS_HANDLED_INCOMING",
            "CONTACTS_HANDLED_OUTBOUND",
            "CONTACTS_HOLD_ABANDONS",
            "CONTACTS_TRANSFERRED_IN",
            "CONTACTS_TRANSFERRED_OUT",
            "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
            "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
            "CONTACTS_MISSED",
            "CALLBACK_CONTACTS_HANDLED",
            "API_CONTACTS_HANDLED",
            "OCCUPANCY",
            "HANDLE_TIME",
            "AFTER_CONTACT_WORK_TIME",
            "QUEUED_TIME",
            "ABANDON_TIME",
            "QUEUE_ANSWER_TIME",
            "HOLD_TIME",
            "INTERACTION_TIME",
            "INTERACTION_AND_HOLD_TIME",
            "SERVICE_LEVEL",
        ],
        "Threshold": ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef,
        "Statistic": Literal["SUM", "MAX", "AVG"],
        "Unit": Literal["SECONDS", "COUNT", "PERCENT"],
    },
    total=False,
)

ClientGetMetricDataResponseMetricResultsCollectionsTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricResultsCollectionsTypeDef",
    {"Metric": ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef, "Value": float},
    total=False,
)

ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)

ClientGetMetricDataResponseMetricResultsDimensionsTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": Literal["VOICE", "CHAT"],
    },
    total=False,
)

ClientGetMetricDataResponseMetricResultsTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricResultsTypeDef",
    {
        "Dimensions": ClientGetMetricDataResponseMetricResultsDimensionsTypeDef,
        "Collections": List[ClientGetMetricDataResponseMetricResultsCollectionsTypeDef],
    },
    total=False,
)

ClientGetMetricDataResponseTypeDef = TypedDict(
    "ClientGetMetricDataResponseTypeDef",
    {"NextToken": str, "MetricResults": List[ClientGetMetricDataResponseMetricResultsTypeDef]},
    total=False,
)

ClientListContactFlowsResponseContactFlowSummaryListTypeDef = TypedDict(
    "ClientListContactFlowsResponseContactFlowSummaryListTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "ContactFlowType": Literal[
            "CONTACT_FLOW",
            "CUSTOMER_QUEUE",
            "CUSTOMER_HOLD",
            "CUSTOMER_WHISPER",
            "AGENT_HOLD",
            "AGENT_WHISPER",
            "OUTBOUND_WHISPER",
            "AGENT_TRANSFER",
            "QUEUE_TRANSFER",
        ],
    },
    total=False,
)

ClientListContactFlowsResponseTypeDef = TypedDict(
    "ClientListContactFlowsResponseTypeDef",
    {
        "ContactFlowSummaryList": List[ClientListContactFlowsResponseContactFlowSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef = TypedDict(
    "ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientListHoursOfOperationsResponseTypeDef = TypedDict(
    "ClientListHoursOfOperationsResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List[
            ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef = TypedDict(
    "ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": Literal["TOLL_FREE", "DID"],
        "PhoneNumberCountryCode": Literal[
            "AF",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BA",
            "BW",
            "BR",
            "IO",
            "VG",
            "BN",
            "BG",
            "BF",
            "BI",
            "KH",
            "CM",
            "CA",
            "CV",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CK",
            "CR",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "CD",
            "DK",
            "DJ",
            "DM",
            "DO",
            "TL",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "PF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "CI",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MK",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "AN",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "KP",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "CG",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "KR",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SZ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "VI",
            "UG",
            "UA",
            "AE",
            "GB",
            "US",
            "UY",
            "UZ",
            "VU",
            "VA",
            "VE",
            "VN",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
        ],
    },
    total=False,
)

ClientListPhoneNumbersResponseTypeDef = TypedDict(
    "ClientListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumberSummaryList": List[ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListQueuesResponseQueueSummaryListTypeDef = TypedDict(
    "ClientListQueuesResponseQueueSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str, "QueueType": Literal["STANDARD", "AGENT"]},
    total=False,
)

ClientListQueuesResponseTypeDef = TypedDict(
    "ClientListQueuesResponseTypeDef",
    {"QueueSummaryList": List[ClientListQueuesResponseQueueSummaryListTypeDef], "NextToken": str},
    total=False,
)

ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef = TypedDict(
    "ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientListRoutingProfilesResponseTypeDef = TypedDict(
    "ClientListRoutingProfilesResponseTypeDef",
    {
        "RoutingProfileSummaryList": List[
            ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef = TypedDict(
    "ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientListSecurityProfilesResponseTypeDef = TypedDict(
    "ClientListSecurityProfilesResponseTypeDef",
    {
        "SecurityProfileSummaryList": List[
            ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef = TypedDict(
    "ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ClientListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "ClientListUserHierarchyGroupsResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List[
            ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListUsersResponseUserSummaryListTypeDef = TypedDict(
    "ClientListUsersResponseUserSummaryListTypeDef",
    {"Id": str, "Arn": str, "Username": str},
    total=False,
)

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {"UserSummaryList": List[ClientListUsersResponseUserSummaryListTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientStartChatContactInitialMessageTypeDef = TypedDict(
    "_RequiredClientStartChatContactInitialMessageTypeDef", {"ContentType": str}
)
_OptionalClientStartChatContactInitialMessageTypeDef = TypedDict(
    "_OptionalClientStartChatContactInitialMessageTypeDef", {"Content": str}, total=False
)


class ClientStartChatContactInitialMessageTypeDef(
    _RequiredClientStartChatContactInitialMessageTypeDef,
    _OptionalClientStartChatContactInitialMessageTypeDef,
):
    pass


ClientStartChatContactParticipantDetailsTypeDef = TypedDict(
    "ClientStartChatContactParticipantDetailsTypeDef", {"DisplayName": str}
)

ClientStartChatContactResponseTypeDef = TypedDict(
    "ClientStartChatContactResponseTypeDef",
    {"ContactId": str, "ParticipantId": str, "ParticipantToken": str},
    total=False,
)

ClientStartOutboundVoiceContactResponseTypeDef = TypedDict(
    "ClientStartOutboundVoiceContactResponseTypeDef", {"ContactId": str}, total=False
)

ClientUpdateUserIdentityInfoIdentityInfoTypeDef = TypedDict(
    "ClientUpdateUserIdentityInfoIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)

_RequiredClientUpdateUserPhoneConfigPhoneConfigTypeDef = TypedDict(
    "_RequiredClientUpdateUserPhoneConfigPhoneConfigTypeDef",
    {"PhoneType": Literal["SOFT_PHONE", "DESK_PHONE"]},
)
_OptionalClientUpdateUserPhoneConfigPhoneConfigTypeDef = TypedDict(
    "_OptionalClientUpdateUserPhoneConfigPhoneConfigTypeDef",
    {"AutoAccept": bool, "AfterContactWorkTimeLimit": int, "DeskPhoneNumber": str},
    total=False,
)


class ClientUpdateUserPhoneConfigPhoneConfigTypeDef(
    _RequiredClientUpdateUserPhoneConfigPhoneConfigTypeDef,
    _OptionalClientUpdateUserPhoneConfigPhoneConfigTypeDef,
):
    pass


GetMetricDataPaginateFiltersTypeDef = TypedDict(
    "GetMetricDataPaginateFiltersTypeDef",
    {"Queues": List[str], "Channels": List[Literal["VOICE", "CHAT"]]},
    total=False,
)

GetMetricDataPaginateHistoricalMetricsThresholdTypeDef = TypedDict(
    "GetMetricDataPaginateHistoricalMetricsThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)

GetMetricDataPaginateHistoricalMetricsTypeDef = TypedDict(
    "GetMetricDataPaginateHistoricalMetricsTypeDef",
    {
        "Name": Literal[
            "CONTACTS_QUEUED",
            "CONTACTS_HANDLED",
            "CONTACTS_ABANDONED",
            "CONTACTS_CONSULTED",
            "CONTACTS_AGENT_HUNG_UP_FIRST",
            "CONTACTS_HANDLED_INCOMING",
            "CONTACTS_HANDLED_OUTBOUND",
            "CONTACTS_HOLD_ABANDONS",
            "CONTACTS_TRANSFERRED_IN",
            "CONTACTS_TRANSFERRED_OUT",
            "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
            "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
            "CONTACTS_MISSED",
            "CALLBACK_CONTACTS_HANDLED",
            "API_CONTACTS_HANDLED",
            "OCCUPANCY",
            "HANDLE_TIME",
            "AFTER_CONTACT_WORK_TIME",
            "QUEUED_TIME",
            "ABANDON_TIME",
            "QUEUE_ANSWER_TIME",
            "HOLD_TIME",
            "INTERACTION_TIME",
            "INTERACTION_AND_HOLD_TIME",
            "SERVICE_LEVEL",
        ],
        "Threshold": GetMetricDataPaginateHistoricalMetricsThresholdTypeDef,
        "Statistic": Literal["SUM", "MAX", "AVG"],
        "Unit": Literal["SECONDS", "COUNT", "PERCENT"],
    },
    total=False,
)

GetMetricDataPaginatePaginationConfigTypeDef = TypedDict(
    "GetMetricDataPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)

GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef",
    {
        "Name": Literal[
            "CONTACTS_QUEUED",
            "CONTACTS_HANDLED",
            "CONTACTS_ABANDONED",
            "CONTACTS_CONSULTED",
            "CONTACTS_AGENT_HUNG_UP_FIRST",
            "CONTACTS_HANDLED_INCOMING",
            "CONTACTS_HANDLED_OUTBOUND",
            "CONTACTS_HOLD_ABANDONS",
            "CONTACTS_TRANSFERRED_IN",
            "CONTACTS_TRANSFERRED_OUT",
            "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
            "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
            "CONTACTS_MISSED",
            "CALLBACK_CONTACTS_HANDLED",
            "API_CONTACTS_HANDLED",
            "OCCUPANCY",
            "HANDLE_TIME",
            "AFTER_CONTACT_WORK_TIME",
            "QUEUED_TIME",
            "ABANDON_TIME",
            "QUEUE_ANSWER_TIME",
            "HOLD_TIME",
            "INTERACTION_TIME",
            "INTERACTION_AND_HOLD_TIME",
            "SERVICE_LEVEL",
        ],
        "Threshold": GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef,
        "Statistic": Literal["SUM", "MAX", "AVG"],
        "Unit": Literal["SECONDS", "COUNT", "PERCENT"],
    },
    total=False,
)

GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef",
    {"Metric": GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef, "Value": float},
    total=False,
)

GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)

GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": Literal["VOICE", "CHAT"],
    },
    total=False,
)

GetMetricDataPaginateResponseMetricResultsTypeDef = TypedDict(
    "GetMetricDataPaginateResponseMetricResultsTypeDef",
    {
        "Dimensions": GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef,
        "Collections": List[GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef],
    },
    total=False,
)

GetMetricDataPaginateResponseTypeDef = TypedDict(
    "GetMetricDataPaginateResponseTypeDef",
    {"MetricResults": List[GetMetricDataPaginateResponseMetricResultsTypeDef]},
    total=False,
)

ListContactFlowsPaginatePaginationConfigTypeDef = TypedDict(
    "ListContactFlowsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef = TypedDict(
    "ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "ContactFlowType": Literal[
            "CONTACT_FLOW",
            "CUSTOMER_QUEUE",
            "CUSTOMER_HOLD",
            "CUSTOMER_WHISPER",
            "AGENT_HOLD",
            "AGENT_WHISPER",
            "OUTBOUND_WHISPER",
            "AGENT_TRANSFER",
            "QUEUE_TRANSFER",
        ],
    },
    total=False,
)

ListContactFlowsPaginateResponseTypeDef = TypedDict(
    "ListContactFlowsPaginateResponseTypeDef",
    {"ContactFlowSummaryList": List[ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef]},
    total=False,
)

ListHoursOfOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListHoursOfOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef = TypedDict(
    "ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ListHoursOfOperationsPaginateResponseTypeDef = TypedDict(
    "ListHoursOfOperationsPaginateResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List[
            ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef
        ]
    },
    total=False,
)

ListPhoneNumbersPaginatePaginationConfigTypeDef = TypedDict(
    "ListPhoneNumbersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef = TypedDict(
    "ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": Literal["TOLL_FREE", "DID"],
        "PhoneNumberCountryCode": Literal[
            "AF",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BA",
            "BW",
            "BR",
            "IO",
            "VG",
            "BN",
            "BG",
            "BF",
            "BI",
            "KH",
            "CM",
            "CA",
            "CV",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CK",
            "CR",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "CD",
            "DK",
            "DJ",
            "DM",
            "DO",
            "TL",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "PF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "CI",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MK",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "AN",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "KP",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "CG",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "KR",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SZ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "VI",
            "UG",
            "UA",
            "AE",
            "GB",
            "US",
            "UY",
            "UZ",
            "VU",
            "VA",
            "VE",
            "VN",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
        ],
    },
    total=False,
)

ListPhoneNumbersPaginateResponseTypeDef = TypedDict(
    "ListPhoneNumbersPaginateResponseTypeDef",
    {"PhoneNumberSummaryList": List[ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef]},
    total=False,
)

ListQueuesPaginatePaginationConfigTypeDef = TypedDict(
    "ListQueuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListQueuesPaginateResponseQueueSummaryListTypeDef = TypedDict(
    "ListQueuesPaginateResponseQueueSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str, "QueueType": Literal["STANDARD", "AGENT"]},
    total=False,
)

ListQueuesPaginateResponseTypeDef = TypedDict(
    "ListQueuesPaginateResponseTypeDef",
    {"QueueSummaryList": List[ListQueuesPaginateResponseQueueSummaryListTypeDef]},
    total=False,
)

ListRoutingProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "ListRoutingProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef = TypedDict(
    "ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ListRoutingProfilesPaginateResponseTypeDef = TypedDict(
    "ListRoutingProfilesPaginateResponseTypeDef",
    {
        "RoutingProfileSummaryList": List[
            ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef
        ]
    },
    total=False,
)

ListSecurityProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "ListSecurityProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef = TypedDict(
    "ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ListSecurityProfilesPaginateResponseTypeDef = TypedDict(
    "ListSecurityProfilesPaginateResponseTypeDef",
    {
        "SecurityProfileSummaryList": List[
            ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef
        ]
    },
    total=False,
)

ListUserHierarchyGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListUserHierarchyGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef = TypedDict(
    "ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)

ListUserHierarchyGroupsPaginateResponseTypeDef = TypedDict(
    "ListUserHierarchyGroupsPaginateResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List[
            ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef
        ]
    },
    total=False,
)

ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListUsersPaginateResponseUserSummaryListTypeDef = TypedDict(
    "ListUsersPaginateResponseUserSummaryListTypeDef",
    {"Id": str, "Arn": str, "Username": str},
    total=False,
)

ListUsersPaginateResponseTypeDef = TypedDict(
    "ListUsersPaginateResponseTypeDef",
    {"UserSummaryList": List[ListUsersPaginateResponseUserSummaryListTypeDef]},
    total=False,
)
