"Main interface for health service type defs"
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


ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

_RequiredClientDescribeAffectedEntitiesFilterTypeDef = TypedDict(
    "_RequiredClientDescribeAffectedEntitiesFilterTypeDef", {"eventArns": List[str]}
)
_OptionalClientDescribeAffectedEntitiesFilterTypeDef = TypedDict(
    "_OptionalClientDescribeAffectedEntitiesFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef],
        "tags": List[Dict[str, str]],
        "statusCodes": List[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]],
    },
    total=False,
)


class ClientDescribeAffectedEntitiesFilterTypeDef(
    _RequiredClientDescribeAffectedEntitiesFilterTypeDef,
    _OptionalClientDescribeAffectedEntitiesFilterTypeDef,
):
    pass


ClientDescribeAffectedEntitiesResponseentitiesTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesResponseentitiesTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeAffectedEntitiesResponseTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesResponseTypeDef",
    {"entities": List[ClientDescribeAffectedEntitiesResponseentitiesTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef = TypedDict(
    "ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef",
    {"eventArn": str, "count": int},
    total=False,
)

ClientDescribeEntityAggregatesResponseTypeDef = TypedDict(
    "ClientDescribeEntityAggregatesResponseTypeDef",
    {"entityAggregates": List[ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef]},
    total=False,
)

ClientDescribeEventAggregatesFilterendTimesTypeDef = TypedDict(
    "ClientDescribeEventAggregatesFilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef = TypedDict(
    "ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventAggregatesFilterstartTimesTypeDef = TypedDict(
    "ClientDescribeEventAggregatesFilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventAggregatesFilterTypeDef = TypedDict(
    "ClientDescribeEventAggregatesFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[ClientDescribeEventAggregatesFilterstartTimesTypeDef],
        "endTimes": List[ClientDescribeEventAggregatesFilterendTimesTypeDef],
        "lastUpdatedTimes": List[ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

ClientDescribeEventAggregatesResponseeventAggregatesTypeDef = TypedDict(
    "ClientDescribeEventAggregatesResponseeventAggregatesTypeDef",
    {"aggregateValue": str, "count": int},
    total=False,
)

ClientDescribeEventAggregatesResponseTypeDef = TypedDict(
    "ClientDescribeEventAggregatesResponseTypeDef",
    {
        "eventAggregates": List[ClientDescribeEventAggregatesResponseeventAggregatesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeEventDetailsResponsefailedSetTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponsefailedSetTypeDef",
    {"eventArn": str, "errorName": str, "errorMessage": str},
    total=False,
)

ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef",
    {"latestDescription": str},
    total=False,
)

ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

ClientDescribeEventDetailsResponsesuccessfulSetTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponsesuccessfulSetTypeDef",
    {
        "event": ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef,
        "eventDescription": ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef,
        "eventMetadata": Dict[str, str],
    },
    total=False,
)

ClientDescribeEventDetailsResponseTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponseTypeDef",
    {
        "successfulSet": List[ClientDescribeEventDetailsResponsesuccessfulSetTypeDef],
        "failedSet": List[ClientDescribeEventDetailsResponsefailedSetTypeDef],
    },
    total=False,
)

ClientDescribeEventTypesFilterTypeDef = TypedDict(
    "ClientDescribeEventTypesFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
    },
    total=False,
)

ClientDescribeEventTypesResponseeventTypesTypeDef = TypedDict(
    "ClientDescribeEventTypesResponseeventTypesTypeDef",
    {
        "service": str,
        "code": str,
        "category": Literal["issue", "accountNotification", "scheduledChange", "investigation"],
    },
    total=False,
)

ClientDescribeEventTypesResponseTypeDef = TypedDict(
    "ClientDescribeEventTypesResponseTypeDef",
    {"eventTypes": List[ClientDescribeEventTypesResponseeventTypesTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeEventsFilterendTimesTypeDef = TypedDict(
    "ClientDescribeEventsFilterendTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)

ClientDescribeEventsFilterlastUpdatedTimesTypeDef = TypedDict(
    "ClientDescribeEventsFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventsFilterstartTimesTypeDef = TypedDict(
    "ClientDescribeEventsFilterstartTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)

ClientDescribeEventsFilterTypeDef = TypedDict(
    "ClientDescribeEventsFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[ClientDescribeEventsFilterstartTimesTypeDef],
        "endTimes": List[ClientDescribeEventsFilterendTimesTypeDef],
        "lastUpdatedTimes": List[ClientDescribeEventsFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

ClientDescribeEventsResponseeventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseeventsTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"events": List[ClientDescribeEventsResponseeventsTypeDef], "nextToken": str},
    total=False,
)

DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef = TypedDict(
    "DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

_RequiredDescribeAffectedEntitiesPaginateFilterTypeDef = TypedDict(
    "_RequiredDescribeAffectedEntitiesPaginateFilterTypeDef", {"eventArns": List[str]}
)
_OptionalDescribeAffectedEntitiesPaginateFilterTypeDef = TypedDict(
    "_OptionalDescribeAffectedEntitiesPaginateFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef],
        "tags": List[Dict[str, str]],
        "statusCodes": List[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]],
    },
    total=False,
)


class DescribeAffectedEntitiesPaginateFilterTypeDef(
    _RequiredDescribeAffectedEntitiesPaginateFilterTypeDef,
    _OptionalDescribeAffectedEntitiesPaginateFilterTypeDef,
):
    pass


DescribeAffectedEntitiesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAffectedEntitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAffectedEntitiesPaginateResponseentitiesTypeDef = TypedDict(
    "DescribeAffectedEntitiesPaginateResponseentitiesTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"],
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeAffectedEntitiesPaginateResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesPaginateResponseTypeDef",
    {"entities": List[DescribeAffectedEntitiesPaginateResponseentitiesTypeDef], "NextToken": str},
    total=False,
)

DescribeEventAggregatesPaginateFilterendTimesTypeDef = TypedDict(
    "DescribeEventAggregatesPaginateFilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef = TypedDict(
    "DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

DescribeEventAggregatesPaginateFilterstartTimesTypeDef = TypedDict(
    "DescribeEventAggregatesPaginateFilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

DescribeEventAggregatesPaginateFilterTypeDef = TypedDict(
    "DescribeEventAggregatesPaginateFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[DescribeEventAggregatesPaginateFilterstartTimesTypeDef],
        "endTimes": List[DescribeEventAggregatesPaginateFilterendTimesTypeDef],
        "lastUpdatedTimes": List[DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

DescribeEventAggregatesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEventAggregatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef = TypedDict(
    "DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef",
    {"aggregateValue": str, "count": int},
    total=False,
)

DescribeEventAggregatesPaginateResponseTypeDef = TypedDict(
    "DescribeEventAggregatesPaginateResponseTypeDef",
    {
        "eventAggregates": List[DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeEventTypesPaginateFilterTypeDef = TypedDict(
    "DescribeEventTypesPaginateFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
    },
    total=False,
)

DescribeEventTypesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEventTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEventTypesPaginateResponseeventTypesTypeDef = TypedDict(
    "DescribeEventTypesPaginateResponseeventTypesTypeDef",
    {
        "service": str,
        "code": str,
        "category": Literal["issue", "accountNotification", "scheduledChange", "investigation"],
    },
    total=False,
)

DescribeEventTypesPaginateResponseTypeDef = TypedDict(
    "DescribeEventTypesPaginateResponseTypeDef",
    {"eventTypes": List[DescribeEventTypesPaginateResponseeventTypesTypeDef], "NextToken": str},
    total=False,
)

DescribeEventsPaginateFilterendTimesTypeDef = TypedDict(
    "DescribeEventsPaginateFilterendTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)

DescribeEventsPaginateFilterlastUpdatedTimesTypeDef = TypedDict(
    "DescribeEventsPaginateFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

DescribeEventsPaginateFilterstartTimesTypeDef = TypedDict(
    "DescribeEventsPaginateFilterstartTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)

DescribeEventsPaginateFilterTypeDef = TypedDict(
    "DescribeEventsPaginateFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[DescribeEventsPaginateFilterstartTimesTypeDef],
        "endTimes": List[DescribeEventsPaginateFilterendTimesTypeDef],
        "lastUpdatedTimes": List[DescribeEventsPaginateFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEventsPaginateResponseeventsTypeDef = TypedDict(
    "DescribeEventsPaginateResponseeventsTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

DescribeEventsPaginateResponseTypeDef = TypedDict(
    "DescribeEventsPaginateResponseTypeDef",
    {"events": List[DescribeEventsPaginateResponseeventsTypeDef], "NextToken": str},
    total=False,
)
