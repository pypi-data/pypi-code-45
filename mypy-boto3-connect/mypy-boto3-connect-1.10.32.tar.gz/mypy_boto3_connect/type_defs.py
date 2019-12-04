"Main interface for connect service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateUserIdentityInfoTypeDef",
    "ClientCreateUserPhoneConfigTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef",
    "ClientDescribeUserHierarchyGroupResponseTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef",
    "ClientDescribeUserHierarchyStructureResponseTypeDef",
    "ClientDescribeUserResponseUserIdentityInfoTypeDef",
    "ClientDescribeUserResponseUserPhoneConfigTypeDef",
    "ClientDescribeUserResponseUserTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientGetContactAttributesResponseTypeDef",
    "ClientGetCurrentMetricDataCurrentMetricsTypeDef",
    "ClientGetCurrentMetricDataFiltersTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsTypeDef",
    "ClientGetCurrentMetricDataResponseTypeDef",
    "ClientGetFederationTokenResponseCredentialsTypeDef",
    "ClientGetFederationTokenResponseTypeDef",
    "ClientGetMetricDataFiltersTypeDef",
    "ClientGetMetricDataHistoricalMetricsThresholdTypeDef",
    "ClientGetMetricDataHistoricalMetricsTypeDef",
    "ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef",
    "ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef",
    "ClientGetMetricDataResponseMetricResultsCollectionsTypeDef",
    "ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    "ClientGetMetricDataResponseMetricResultsDimensionsTypeDef",
    "ClientGetMetricDataResponseMetricResultsTypeDef",
    "ClientGetMetricDataResponseTypeDef",
    "ClientListContactFlowsResponseContactFlowSummaryListTypeDef",
    "ClientListContactFlowsResponseTypeDef",
    "ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef",
    "ClientListHoursOfOperationsResponseTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef",
    "ClientListPhoneNumbersResponseTypeDef",
    "ClientListQueuesResponseQueueSummaryListTypeDef",
    "ClientListQueuesResponseTypeDef",
    "ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef",
    "ClientListRoutingProfilesResponseTypeDef",
    "ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef",
    "ClientListSecurityProfilesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef",
    "ClientListUserHierarchyGroupsResponseTypeDef",
    "ClientListUsersResponseUserSummaryListTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientStartChatContactInitialMessageTypeDef",
    "ClientStartChatContactParticipantDetailsTypeDef",
    "ClientStartChatContactResponseTypeDef",
    "ClientStartOutboundVoiceContactResponseTypeDef",
    "ClientUpdateUserIdentityInfoIdentityInfoTypeDef",
    "ClientUpdateUserPhoneConfigPhoneConfigTypeDef",
    "GetMetricDataPaginateFiltersTypeDef",
    "GetMetricDataPaginateHistoricalMetricsThresholdTypeDef",
    "GetMetricDataPaginateHistoricalMetricsTypeDef",
    "GetMetricDataPaginatePaginationConfigTypeDef",
    "GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef",
    "GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef",
    "GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef",
    "GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef",
    "GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef",
    "GetMetricDataPaginateResponseMetricResultsTypeDef",
    "GetMetricDataPaginateResponseTypeDef",
    "ListContactFlowsPaginatePaginationConfigTypeDef",
    "ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef",
    "ListContactFlowsPaginateResponseTypeDef",
    "ListHoursOfOperationsPaginatePaginationConfigTypeDef",
    "ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef",
    "ListHoursOfOperationsPaginateResponseTypeDef",
    "ListPhoneNumbersPaginatePaginationConfigTypeDef",
    "ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef",
    "ListPhoneNumbersPaginateResponseTypeDef",
    "ListQueuesPaginatePaginationConfigTypeDef",
    "ListQueuesPaginateResponseQueueSummaryListTypeDef",
    "ListQueuesPaginateResponseTypeDef",
    "ListRoutingProfilesPaginatePaginationConfigTypeDef",
    "ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef",
    "ListRoutingProfilesPaginateResponseTypeDef",
    "ListSecurityProfilesPaginatePaginationConfigTypeDef",
    "ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef",
    "ListSecurityProfilesPaginateResponseTypeDef",
    "ListUserHierarchyGroupsPaginatePaginationConfigTypeDef",
    "ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef",
    "ListUserHierarchyGroupsPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUserSummaryListTypeDef",
    "ListUsersPaginateResponseTypeDef",
)


_ClientCreateUserIdentityInfoTypeDef = TypedDict(
    "_ClientCreateUserIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)


class ClientCreateUserIdentityInfoTypeDef(_ClientCreateUserIdentityInfoTypeDef):
    """
    The information about the identity of the user.
    - **FirstName** *(string) --*

      The first name. This is required if you are using Amazon Connect or SAML for identity
      management.
    """


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
    """
    The phone settings for the user.
    - **PhoneType** *(string) --***[REQUIRED]**

      The phone type.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"UserId": str, "UserArn": str}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    - *(dict) --*

      - **UserId** *(string) --*

        The identifier of the user account.
    """


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef
):
    pass


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef
):
    pass


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef
):
    pass


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef
):
    pass


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef
):
    pass


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef",
    {
        "LevelOne": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef,
        "LevelTwo": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef,
        "LevelThree": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef,
        "LevelFour": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef,
        "LevelFive": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef,
    },
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef
):
    pass


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "LevelId": str,
        "HierarchyPath": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef,
    },
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef
):
    """
    - **HierarchyGroup** *(dict) --*

      Information about the hierarchy group.
      - **Id** *(string) --*

        The identifier of the hierarchy group.
    """


_ClientDescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseTypeDef",
    {"HierarchyGroup": ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseTypeDef(
    _ClientDescribeUserHierarchyGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **HierarchyGroup** *(dict) --*

        Information about the hierarchy group.
        - **Id** *(string) --*

          The identifier of the hierarchy group.
    """


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef
):
    pass


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef
):
    pass


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef
):
    """
    - **LevelOne** *(dict) --*

      Information about level one.
      - **Id** *(string) --*

        The identifier of the hierarchy level.
    """


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef
):
    pass


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef
):
    pass


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef",
    {
        "LevelOne": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef,
        "LevelTwo": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef,
        "LevelThree": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef,
        "LevelFour": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef,
        "LevelFive": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef,
    },
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef
):
    """
    - **HierarchyStructure** *(dict) --*

      Information about the hierarchy structure.
      - **LevelOne** *(dict) --*

        Information about level one.
        - **Id** *(string) --*

          The identifier of the hierarchy level.
    """


_ClientDescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseTypeDef",
    {"HierarchyStructure": ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseTypeDef(
    _ClientDescribeUserHierarchyStructureResponseTypeDef
):
    """
    - *(dict) --*

      - **HierarchyStructure** *(dict) --*

        Information about the hierarchy structure.
        - **LevelOne** *(dict) --*

          Information about level one.
          - **Id** *(string) --*

            The identifier of the hierarchy level.
    """


_ClientDescribeUserResponseUserIdentityInfoTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)


class ClientDescribeUserResponseUserIdentityInfoTypeDef(
    _ClientDescribeUserResponseUserIdentityInfoTypeDef
):
    pass


_ClientDescribeUserResponseUserPhoneConfigTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserPhoneConfigTypeDef",
    {
        "PhoneType": Literal["SOFT_PHONE", "DESK_PHONE"],
        "AutoAccept": bool,
        "AfterContactWorkTimeLimit": int,
        "DeskPhoneNumber": str,
    },
    total=False,
)


class ClientDescribeUserResponseUserPhoneConfigTypeDef(
    _ClientDescribeUserResponseUserPhoneConfigTypeDef
):
    pass


_ClientDescribeUserResponseUserTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserTypeDef",
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


class ClientDescribeUserResponseUserTypeDef(_ClientDescribeUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      Information about the user account and configuration settings.
      - **Id** *(string) --*

        The identifier of the user account.
    """


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {"User": ClientDescribeUserResponseUserTypeDef},
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        Information about the user account and configuration settings.
        - **Id** *(string) --*

          The identifier of the user account.
    """


_ClientGetContactAttributesResponseTypeDef = TypedDict(
    "_ClientGetContactAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)


class ClientGetContactAttributesResponseTypeDef(_ClientGetContactAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **Attributes** *(dict) --*

        Information about the attributes.
        - *(string) --*

          - *(string) --*
    """


_ClientGetCurrentMetricDataCurrentMetricsTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataCurrentMetricsTypeDef",
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


class ClientGetCurrentMetricDataCurrentMetricsTypeDef(
    _ClientGetCurrentMetricDataCurrentMetricsTypeDef
):
    pass


_ClientGetCurrentMetricDataFiltersTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataFiltersTypeDef",
    {"Queues": List[str], "Channels": List[Literal["VOICE", "CHAT"]]},
    total=False,
)


class ClientGetCurrentMetricDataFiltersTypeDef(_ClientGetCurrentMetricDataFiltersTypeDef):
    """
    The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
    retrieved only for the resources associated with the queues or channels included in the filter.
    You can include both queue IDs and queue ARNs in the same request. The only supported channel is
    ``VOICE`` .
    - **Queues** *(list) --*

      The queues to use to filter the metrics. You can specify up to 100 queues per request.
      - *(string) --*
    """


_ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef",
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


class ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef
):
    pass


_ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef",
    {
        "Metric": ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef,
        "Value": float,
    },
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef
):
    pass


_ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef
):
    pass


_ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": Literal["VOICE", "CHAT"],
    },
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef
):
    pass


_ClientGetCurrentMetricDataResponseMetricResultsTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsTypeDef",
    {
        "Dimensions": ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef,
        "Collections": List[ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef],
    },
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsTypeDef
):
    pass


_ClientGetCurrentMetricDataResponseTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List[ClientGetCurrentMetricDataResponseMetricResultsTypeDef],
        "DataSnapshotTime": datetime,
    },
    total=False,
)


class ClientGetCurrentMetricDataResponseTypeDef(_ClientGetCurrentMetricDataResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If there are additional results, this is the token for the next set of results.
        The token expires after 5 minutes from the time it is created. Subsequent requests that use
        the token must use the same request parameters as the request that generated the token.
    """


_ClientGetFederationTokenResponseCredentialsTypeDef = TypedDict(
    "_ClientGetFederationTokenResponseCredentialsTypeDef",
    {
        "AccessToken": str,
        "AccessTokenExpiration": datetime,
        "RefreshToken": str,
        "RefreshTokenExpiration": datetime,
    },
    total=False,
)


class ClientGetFederationTokenResponseCredentialsTypeDef(
    _ClientGetFederationTokenResponseCredentialsTypeDef
):
    """
    - **Credentials** *(dict) --*

      The credentials to use for federation.
      - **AccessToken** *(string) --*

        An access token generated for a federated user to access Amazon Connect.
    """


_ClientGetFederationTokenResponseTypeDef = TypedDict(
    "_ClientGetFederationTokenResponseTypeDef",
    {"Credentials": ClientGetFederationTokenResponseCredentialsTypeDef},
    total=False,
)


class ClientGetFederationTokenResponseTypeDef(_ClientGetFederationTokenResponseTypeDef):
    """
    - *(dict) --*

      - **Credentials** *(dict) --*

        The credentials to use for federation.
        - **AccessToken** *(string) --*

          An access token generated for a federated user to access Amazon Connect.
    """


_ClientGetMetricDataFiltersTypeDef = TypedDict(
    "_ClientGetMetricDataFiltersTypeDef",
    {"Queues": List[str], "Channels": List[Literal["VOICE", "CHAT"]]},
    total=False,
)


class ClientGetMetricDataFiltersTypeDef(_ClientGetMetricDataFiltersTypeDef):
    """
    The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
    retrieved only for the resources associated with the queues or channels included in the filter.
    You can include both queue IDs and queue ARNs in the same request. The only supported channel is
    ``VOICE`` .
    - **Queues** *(list) --*

      The queues to use to filter the metrics. You can specify up to 100 queues per request.
      - *(string) --*
    """


_ClientGetMetricDataHistoricalMetricsThresholdTypeDef = TypedDict(
    "_ClientGetMetricDataHistoricalMetricsThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)


class ClientGetMetricDataHistoricalMetricsThresholdTypeDef(
    _ClientGetMetricDataHistoricalMetricsThresholdTypeDef
):
    pass


_ClientGetMetricDataHistoricalMetricsTypeDef = TypedDict(
    "_ClientGetMetricDataHistoricalMetricsTypeDef",
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


class ClientGetMetricDataHistoricalMetricsTypeDef(_ClientGetMetricDataHistoricalMetricsTypeDef):
    pass


_ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)


class ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef(
    _ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef
):
    pass


_ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef",
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


class ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef(
    _ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef
):
    pass


_ClientGetMetricDataResponseMetricResultsCollectionsTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsCollectionsTypeDef",
    {"Metric": ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef, "Value": float},
    total=False,
)


class ClientGetMetricDataResponseMetricResultsCollectionsTypeDef(
    _ClientGetMetricDataResponseMetricResultsCollectionsTypeDef
):
    pass


_ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef(
    _ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef
):
    pass


_ClientGetMetricDataResponseMetricResultsDimensionsTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": Literal["VOICE", "CHAT"],
    },
    total=False,
)


class ClientGetMetricDataResponseMetricResultsDimensionsTypeDef(
    _ClientGetMetricDataResponseMetricResultsDimensionsTypeDef
):
    pass


_ClientGetMetricDataResponseMetricResultsTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsTypeDef",
    {
        "Dimensions": ClientGetMetricDataResponseMetricResultsDimensionsTypeDef,
        "Collections": List[ClientGetMetricDataResponseMetricResultsCollectionsTypeDef],
    },
    total=False,
)


class ClientGetMetricDataResponseMetricResultsTypeDef(
    _ClientGetMetricDataResponseMetricResultsTypeDef
):
    pass


_ClientGetMetricDataResponseTypeDef = TypedDict(
    "_ClientGetMetricDataResponseTypeDef",
    {"NextToken": str, "MetricResults": List[ClientGetMetricDataResponseMetricResultsTypeDef]},
    total=False,
)


class ClientGetMetricDataResponseTypeDef(_ClientGetMetricDataResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If there are additional results, this is the token for the next set of results.
        The token expires after 5 minutes from the time it is created. Subsequent requests that use
        the token must use the same request parameters as the request that generated the token.
    """


_ClientListContactFlowsResponseContactFlowSummaryListTypeDef = TypedDict(
    "_ClientListContactFlowsResponseContactFlowSummaryListTypeDef",
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


class ClientListContactFlowsResponseContactFlowSummaryListTypeDef(
    _ClientListContactFlowsResponseContactFlowSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a contact flow.
      - **Id** *(string) --*

        The identifier of the contact flow.
    """


_ClientListContactFlowsResponseTypeDef = TypedDict(
    "_ClientListContactFlowsResponseTypeDef",
    {
        "ContactFlowSummaryList": List[ClientListContactFlowsResponseContactFlowSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListContactFlowsResponseTypeDef(_ClientListContactFlowsResponseTypeDef):
    """
    - *(dict) --*

      - **ContactFlowSummaryList** *(list) --*

        Information about the contact flows.
        - *(dict) --*

          Contains summary information about a contact flow.
          - **Id** *(string) --*

            The identifier of the contact flow.
    """


_ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef = TypedDict(
    "_ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef(
    _ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about hours of operation for a contact center.
      - **Id** *(string) --*

        The identifier of the hours of operation.
    """


_ClientListHoursOfOperationsResponseTypeDef = TypedDict(
    "_ClientListHoursOfOperationsResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List[
            ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListHoursOfOperationsResponseTypeDef(_ClientListHoursOfOperationsResponseTypeDef):
    """
    - *(dict) --*

      - **HoursOfOperationSummaryList** *(list) --*

        Information about the hours of operation.
        - *(dict) --*

          Contains summary information about hours of operation for a contact center.
          - **Id** *(string) --*

            The identifier of the hours of operation.
    """


_ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef",
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


class ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef(
    _ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a phone number for a contact center.
      - **Id** *(string) --*

        The identifier of the phone number.
    """


_ClientListPhoneNumbersResponseTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumberSummaryList": List[ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListPhoneNumbersResponseTypeDef(_ClientListPhoneNumbersResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumberSummaryList** *(list) --*

        Information about the phone numbers.
        - *(dict) --*

          Contains summary information about a phone number for a contact center.
          - **Id** *(string) --*

            The identifier of the phone number.
    """


_ClientListQueuesResponseQueueSummaryListTypeDef = TypedDict(
    "_ClientListQueuesResponseQueueSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str, "QueueType": Literal["STANDARD", "AGENT"]},
    total=False,
)


class ClientListQueuesResponseQueueSummaryListTypeDef(
    _ClientListQueuesResponseQueueSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a queue.
      - **Id** *(string) --*

        The identifier of the queue.
    """


_ClientListQueuesResponseTypeDef = TypedDict(
    "_ClientListQueuesResponseTypeDef",
    {"QueueSummaryList": List[ClientListQueuesResponseQueueSummaryListTypeDef], "NextToken": str},
    total=False,
)


class ClientListQueuesResponseTypeDef(_ClientListQueuesResponseTypeDef):
    """
    - *(dict) --*

      - **QueueSummaryList** *(list) --*

        Information about the queues.
        - *(dict) --*

          Contains summary information about a queue.
          - **Id** *(string) --*

            The identifier of the queue.
    """


_ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef = TypedDict(
    "_ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef(
    _ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a routing profile.
      - **Id** *(string) --*

        The identifier of the routing profile.
    """


_ClientListRoutingProfilesResponseTypeDef = TypedDict(
    "_ClientListRoutingProfilesResponseTypeDef",
    {
        "RoutingProfileSummaryList": List[
            ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListRoutingProfilesResponseTypeDef(_ClientListRoutingProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **RoutingProfileSummaryList** *(list) --*

        Information about the routing profiles.
        - *(dict) --*

          Contains summary information about a routing profile.
          - **Id** *(string) --*

            The identifier of the routing profile.
    """


_ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef = TypedDict(
    "_ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef(
    _ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains information about a security profile.
      - **Id** *(string) --*

        The identifier of the security profile.
    """


_ClientListSecurityProfilesResponseTypeDef = TypedDict(
    "_ClientListSecurityProfilesResponseTypeDef",
    {
        "SecurityProfileSummaryList": List[
            ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSecurityProfilesResponseTypeDef(_ClientListSecurityProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **SecurityProfileSummaryList** *(list) --*

        Information about the security profiles.
        - *(dict) --*

          Contains information about a security profile.
          - **Id** *(string) --*

            The identifier of the security profile.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        Information about the tags.
        - *(string) --*

          - *(string) --*
    """


_ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef = TypedDict(
    "_ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef(
    _ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a hierarchy group.
      - **Id** *(string) --*

        The identifier of the hierarchy group.
    """


_ClientListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "_ClientListUserHierarchyGroupsResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List[
            ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListUserHierarchyGroupsResponseTypeDef(_ClientListUserHierarchyGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **UserHierarchyGroupSummaryList** *(list) --*

        Information about the hierarchy groups.
        - *(dict) --*

          Contains summary information about a hierarchy group.
          - **Id** *(string) --*

            The identifier of the hierarchy group.
    """


_ClientListUsersResponseUserSummaryListTypeDef = TypedDict(
    "_ClientListUsersResponseUserSummaryListTypeDef",
    {"Id": str, "Arn": str, "Username": str},
    total=False,
)


class ClientListUsersResponseUserSummaryListTypeDef(_ClientListUsersResponseUserSummaryListTypeDef):
    """
    - *(dict) --*

      Contains summary information about a user.
      - **Id** *(string) --*

        The identifier of the user account.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"UserSummaryList": List[ClientListUsersResponseUserSummaryListTypeDef], "NextToken": str},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    - *(dict) --*

      - **UserSummaryList** *(list) --*

        Information about the users.
        - *(dict) --*

          Contains summary information about a user.
          - **Id** *(string) --*

            The identifier of the user account.
    """


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
    """
    The initial message to be sent to the newly created chat.
    - **ContentType** *(string) --***[REQUIRED]**

      The type of the content. Supported types are text/plain.
    """


_ClientStartChatContactParticipantDetailsTypeDef = TypedDict(
    "_ClientStartChatContactParticipantDetailsTypeDef", {"DisplayName": str}
)


class ClientStartChatContactParticipantDetailsTypeDef(
    _ClientStartChatContactParticipantDetailsTypeDef
):
    """
    Information identifying the participant.
    - **DisplayName** *(string) --***[REQUIRED]**

      Display name of the participant.
    """


_ClientStartChatContactResponseTypeDef = TypedDict(
    "_ClientStartChatContactResponseTypeDef",
    {"ContactId": str, "ParticipantId": str, "ParticipantToken": str},
    total=False,
)


class ClientStartChatContactResponseTypeDef(_ClientStartChatContactResponseTypeDef):
    """
    - *(dict) --*

      - **ContactId** *(string) --*

        The identifier of this contact within the Amazon Connect instance.
    """


_ClientStartOutboundVoiceContactResponseTypeDef = TypedDict(
    "_ClientStartOutboundVoiceContactResponseTypeDef", {"ContactId": str}, total=False
)


class ClientStartOutboundVoiceContactResponseTypeDef(
    _ClientStartOutboundVoiceContactResponseTypeDef
):
    """
    - *(dict) --*

      - **ContactId** *(string) --*

        The identifier of this contact within the Amazon Connect instance.
    """


_ClientUpdateUserIdentityInfoIdentityInfoTypeDef = TypedDict(
    "_ClientUpdateUserIdentityInfoIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)


class ClientUpdateUserIdentityInfoIdentityInfoTypeDef(
    _ClientUpdateUserIdentityInfoIdentityInfoTypeDef
):
    """
    The identity information for the user.
    - **FirstName** *(string) --*

      The first name. This is required if you are using Amazon Connect or SAML for identity
      management.
    """


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
    """
    Information about phone configuration settings for the user.
    - **PhoneType** *(string) --***[REQUIRED]**

      The phone type.
    """


_GetMetricDataPaginateFiltersTypeDef = TypedDict(
    "_GetMetricDataPaginateFiltersTypeDef",
    {"Queues": List[str], "Channels": List[Literal["VOICE", "CHAT"]]},
    total=False,
)


class GetMetricDataPaginateFiltersTypeDef(_GetMetricDataPaginateFiltersTypeDef):
    """
    The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
    retrieved only for the resources associated with the queues or channels included in the filter.
    You can include both queue IDs and queue ARNs in the same request. The only supported channel is
    ``VOICE`` .
    - **Queues** *(list) --*

      The queues to use to filter the metrics. You can specify up to 100 queues per request.
      - *(string) --*
    """


_GetMetricDataPaginateHistoricalMetricsThresholdTypeDef = TypedDict(
    "_GetMetricDataPaginateHistoricalMetricsThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)


class GetMetricDataPaginateHistoricalMetricsThresholdTypeDef(
    _GetMetricDataPaginateHistoricalMetricsThresholdTypeDef
):
    pass


_GetMetricDataPaginateHistoricalMetricsTypeDef = TypedDict(
    "_GetMetricDataPaginateHistoricalMetricsTypeDef",
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


class GetMetricDataPaginateHistoricalMetricsTypeDef(_GetMetricDataPaginateHistoricalMetricsTypeDef):
    pass


_GetMetricDataPaginatePaginationConfigTypeDef = TypedDict(
    "_GetMetricDataPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetMetricDataPaginatePaginationConfigTypeDef(_GetMetricDataPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef(
    _GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef
):
    pass


_GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef",
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


class GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef(
    _GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef
):
    pass


_GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef",
    {"Metric": GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef, "Value": float},
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef(
    _GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef
):
    pass


_GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef(
    _GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef
):
    """
    - **Queue** *(dict) --*

      Information about the queue for which metrics are returned.
      - **Id** *(string) --*

        The identifier of the queue.
    """


_GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": Literal["VOICE", "CHAT"],
    },
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef(
    _GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef
):
    """
    - **Dimensions** *(dict) --*

      The dimension for the metrics.
      - **Queue** *(dict) --*

        Information about the queue for which metrics are returned.
        - **Id** *(string) --*

          The identifier of the queue.
    """


_GetMetricDataPaginateResponseMetricResultsTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsTypeDef",
    {
        "Dimensions": GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef,
        "Collections": List[GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef],
    },
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsTypeDef(
    _GetMetricDataPaginateResponseMetricResultsTypeDef
):
    """
    - *(dict) --*

      Contains information about the historical metrics retrieved.
      - **Dimensions** *(dict) --*

        The dimension for the metrics.
        - **Queue** *(dict) --*

          Information about the queue for which metrics are returned.
          - **Id** *(string) --*

            The identifier of the queue.
    """


_GetMetricDataPaginateResponseTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseTypeDef",
    {"MetricResults": List[GetMetricDataPaginateResponseMetricResultsTypeDef]},
    total=False,
)


class GetMetricDataPaginateResponseTypeDef(_GetMetricDataPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **MetricResults** *(list) --*

        Information about the historical metrics.
        If no grouping is specified, a summary of metric data is returned.
        - *(dict) --*

          Contains information about the historical metrics retrieved.
          - **Dimensions** *(dict) --*

            The dimension for the metrics.
            - **Queue** *(dict) --*

              Information about the queue for which metrics are returned.
              - **Id** *(string) --*

                The identifier of the queue.
    """


_ListContactFlowsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListContactFlowsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListContactFlowsPaginatePaginationConfigTypeDef(
    _ListContactFlowsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef = TypedDict(
    "_ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef",
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


class ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef(
    _ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a contact flow.
      - **Id** *(string) --*

        The identifier of the contact flow.
    """


_ListContactFlowsPaginateResponseTypeDef = TypedDict(
    "_ListContactFlowsPaginateResponseTypeDef",
    {"ContactFlowSummaryList": List[ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef]},
    total=False,
)


class ListContactFlowsPaginateResponseTypeDef(_ListContactFlowsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ContactFlowSummaryList** *(list) --*

        Information about the contact flows.
        - *(dict) --*

          Contains summary information about a contact flow.
          - **Id** *(string) --*

            The identifier of the contact flow.
    """


_ListHoursOfOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHoursOfOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHoursOfOperationsPaginatePaginationConfigTypeDef(
    _ListHoursOfOperationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef = TypedDict(
    "_ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef(
    _ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about hours of operation for a contact center.
      - **Id** *(string) --*

        The identifier of the hours of operation.
    """


_ListHoursOfOperationsPaginateResponseTypeDef = TypedDict(
    "_ListHoursOfOperationsPaginateResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List[
            ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef
        ]
    },
    total=False,
)


class ListHoursOfOperationsPaginateResponseTypeDef(_ListHoursOfOperationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **HoursOfOperationSummaryList** *(list) --*

        Information about the hours of operation.
        - *(dict) --*

          Contains summary information about hours of operation for a contact center.
          - **Id** *(string) --*

            The identifier of the hours of operation.
    """


_ListPhoneNumbersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPhoneNumbersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPhoneNumbersPaginatePaginationConfigTypeDef(
    _ListPhoneNumbersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef = TypedDict(
    "_ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef",
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


class ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef(
    _ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a phone number for a contact center.
      - **Id** *(string) --*

        The identifier of the phone number.
    """


_ListPhoneNumbersPaginateResponseTypeDef = TypedDict(
    "_ListPhoneNumbersPaginateResponseTypeDef",
    {"PhoneNumberSummaryList": List[ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef]},
    total=False,
)


class ListPhoneNumbersPaginateResponseTypeDef(_ListPhoneNumbersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **PhoneNumberSummaryList** *(list) --*

        Information about the phone numbers.
        - *(dict) --*

          Contains summary information about a phone number for a contact center.
          - **Id** *(string) --*

            The identifier of the phone number.
    """


_ListQueuesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQueuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQueuesPaginatePaginationConfigTypeDef(_ListQueuesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListQueuesPaginateResponseQueueSummaryListTypeDef = TypedDict(
    "_ListQueuesPaginateResponseQueueSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str, "QueueType": Literal["STANDARD", "AGENT"]},
    total=False,
)


class ListQueuesPaginateResponseQueueSummaryListTypeDef(
    _ListQueuesPaginateResponseQueueSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a queue.
      - **Id** *(string) --*

        The identifier of the queue.
    """


_ListQueuesPaginateResponseTypeDef = TypedDict(
    "_ListQueuesPaginateResponseTypeDef",
    {"QueueSummaryList": List[ListQueuesPaginateResponseQueueSummaryListTypeDef]},
    total=False,
)


class ListQueuesPaginateResponseTypeDef(_ListQueuesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **QueueSummaryList** *(list) --*

        Information about the queues.
        - *(dict) --*

          Contains summary information about a queue.
          - **Id** *(string) --*

            The identifier of the queue.
    """


_ListRoutingProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRoutingProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRoutingProfilesPaginatePaginationConfigTypeDef(
    _ListRoutingProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef = TypedDict(
    "_ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef(
    _ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a routing profile.
      - **Id** *(string) --*

        The identifier of the routing profile.
    """


_ListRoutingProfilesPaginateResponseTypeDef = TypedDict(
    "_ListRoutingProfilesPaginateResponseTypeDef",
    {
        "RoutingProfileSummaryList": List[
            ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef
        ]
    },
    total=False,
)


class ListRoutingProfilesPaginateResponseTypeDef(_ListRoutingProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **RoutingProfileSummaryList** *(list) --*

        Information about the routing profiles.
        - *(dict) --*

          Contains summary information about a routing profile.
          - **Id** *(string) --*

            The identifier of the routing profile.
    """


_ListSecurityProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecurityProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSecurityProfilesPaginatePaginationConfigTypeDef(
    _ListSecurityProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef = TypedDict(
    "_ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef(
    _ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains information about a security profile.
      - **Id** *(string) --*

        The identifier of the security profile.
    """


_ListSecurityProfilesPaginateResponseTypeDef = TypedDict(
    "_ListSecurityProfilesPaginateResponseTypeDef",
    {
        "SecurityProfileSummaryList": List[
            ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef
        ]
    },
    total=False,
)


class ListSecurityProfilesPaginateResponseTypeDef(_ListSecurityProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SecurityProfileSummaryList** *(list) --*

        Information about the security profiles.
        - *(dict) --*

          Contains information about a security profile.
          - **Id** *(string) --*

            The identifier of the security profile.
    """


_ListUserHierarchyGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserHierarchyGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserHierarchyGroupsPaginatePaginationConfigTypeDef(
    _ListUserHierarchyGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef = TypedDict(
    "_ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef(
    _ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a hierarchy group.
      - **Id** *(string) --*

        The identifier of the hierarchy group.
    """


_ListUserHierarchyGroupsPaginateResponseTypeDef = TypedDict(
    "_ListUserHierarchyGroupsPaginateResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List[
            ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef
        ]
    },
    total=False,
)


class ListUserHierarchyGroupsPaginateResponseTypeDef(
    _ListUserHierarchyGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **UserHierarchyGroupSummaryList** *(list) --*

        Information about the hierarchy groups.
        - *(dict) --*

          Contains summary information about a hierarchy group.
          - **Id** *(string) --*

            The identifier of the hierarchy group.
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


_ListUsersPaginateResponseUserSummaryListTypeDef = TypedDict(
    "_ListUsersPaginateResponseUserSummaryListTypeDef",
    {"Id": str, "Arn": str, "Username": str},
    total=False,
)


class ListUsersPaginateResponseUserSummaryListTypeDef(
    _ListUsersPaginateResponseUserSummaryListTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a user.
      - **Id** *(string) --*

        The identifier of the user account.
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"UserSummaryList": List[ListUsersPaginateResponseUserSummaryListTypeDef]},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **UserSummaryList** *(list) --*

        Information about the users.
        - *(dict) --*

          Contains summary information about a user.
          - **Id** *(string) --*

            The identifier of the user account.
    """
