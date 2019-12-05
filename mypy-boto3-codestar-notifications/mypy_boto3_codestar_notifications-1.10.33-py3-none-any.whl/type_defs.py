"Main interface for codestar-notifications service type defs"
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


ClientCreateNotificationRuleResponseTypeDef = TypedDict(
    "ClientCreateNotificationRuleResponseTypeDef", {"Arn": str}, total=False
)

ClientCreateNotificationRuleTargetsTypeDef = TypedDict(
    "ClientCreateNotificationRuleTargetsTypeDef",
    {"TargetType": str, "TargetAddress": str},
    total=False,
)

ClientDeleteNotificationRuleResponseTypeDef = TypedDict(
    "ClientDeleteNotificationRuleResponseTypeDef", {"Arn": str}, total=False
)

ClientDescribeNotificationRuleResponseEventTypesTypeDef = TypedDict(
    "ClientDescribeNotificationRuleResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)

ClientDescribeNotificationRuleResponseTargetsTypeDef = TypedDict(
    "ClientDescribeNotificationRuleResponseTargetsTypeDef",
    {
        "TargetAddress": str,
        "TargetType": str,
        "TargetStatus": Literal["PENDING", "ACTIVE", "UNREACHABLE", "INACTIVE", "DEACTIVATED"],
    },
    total=False,
)

ClientDescribeNotificationRuleResponseTypeDef = TypedDict(
    "ClientDescribeNotificationRuleResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "EventTypes": List[ClientDescribeNotificationRuleResponseEventTypesTypeDef],
        "Resource": str,
        "Targets": List[ClientDescribeNotificationRuleResponseTargetsTypeDef],
        "DetailType": Literal["BASIC", "FULL"],
        "CreatedBy": str,
        "Status": Literal["ENABLED", "DISABLED"],
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredClientListEventTypesFiltersTypeDef = TypedDict(
    "_RequiredClientListEventTypesFiltersTypeDef",
    {"Name": Literal["RESOURCE_TYPE", "SERVICE_NAME"]},
)
_OptionalClientListEventTypesFiltersTypeDef = TypedDict(
    "_OptionalClientListEventTypesFiltersTypeDef", {"Value": str}, total=False
)


class ClientListEventTypesFiltersTypeDef(
    _RequiredClientListEventTypesFiltersTypeDef, _OptionalClientListEventTypesFiltersTypeDef
):
    pass


ClientListEventTypesResponseEventTypesTypeDef = TypedDict(
    "ClientListEventTypesResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)

ClientListEventTypesResponseTypeDef = TypedDict(
    "ClientListEventTypesResponseTypeDef",
    {"EventTypes": List[ClientListEventTypesResponseEventTypesTypeDef], "NextToken": str},
    total=False,
)

ClientListNotificationRulesFiltersTypeDef = TypedDict(
    "ClientListNotificationRulesFiltersTypeDef",
    {"Name": Literal["EVENT_TYPE_ID", "CREATED_BY", "RESOURCE", "TARGET_ADDRESS"], "Value": str},
    total=False,
)

ClientListNotificationRulesResponseNotificationRulesTypeDef = TypedDict(
    "ClientListNotificationRulesResponseNotificationRulesTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)

ClientListNotificationRulesResponseTypeDef = TypedDict(
    "ClientListNotificationRulesResponseTypeDef",
    {
        "NextToken": str,
        "NotificationRules": List[ClientListNotificationRulesResponseNotificationRulesTypeDef],
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListTargetsFiltersTypeDef = TypedDict(
    "ClientListTargetsFiltersTypeDef",
    {"Name": Literal["TARGET_TYPE", "TARGET_ADDRESS", "TARGET_STATUS"], "Value": str},
    total=False,
)

ClientListTargetsResponseTargetsTypeDef = TypedDict(
    "ClientListTargetsResponseTargetsTypeDef",
    {
        "TargetAddress": str,
        "TargetType": str,
        "TargetStatus": Literal["PENDING", "ACTIVE", "UNREACHABLE", "INACTIVE", "DEACTIVATED"],
    },
    total=False,
)

ClientListTargetsResponseTypeDef = TypedDict(
    "ClientListTargetsResponseTypeDef",
    {"Targets": List[ClientListTargetsResponseTargetsTypeDef], "NextToken": str},
    total=False,
)

ClientSubscribeResponseTypeDef = TypedDict(
    "ClientSubscribeResponseTypeDef", {"Arn": str}, total=False
)

ClientSubscribeTargetTypeDef = TypedDict(
    "ClientSubscribeTargetTypeDef", {"TargetType": str, "TargetAddress": str}, total=False
)

ClientTagResourceResponseTypeDef = TypedDict(
    "ClientTagResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUnsubscribeResponseTypeDef = TypedDict(
    "ClientUnsubscribeResponseTypeDef", {"Arn": str}, total=False
)

ClientUpdateNotificationRuleTargetsTypeDef = TypedDict(
    "ClientUpdateNotificationRuleTargetsTypeDef",
    {"TargetType": str, "TargetAddress": str},
    total=False,
)

_RequiredListEventTypesPaginateFiltersTypeDef = TypedDict(
    "_RequiredListEventTypesPaginateFiltersTypeDef",
    {"Name": Literal["RESOURCE_TYPE", "SERVICE_NAME"]},
)
_OptionalListEventTypesPaginateFiltersTypeDef = TypedDict(
    "_OptionalListEventTypesPaginateFiltersTypeDef", {"Value": str}, total=False
)


class ListEventTypesPaginateFiltersTypeDef(
    _RequiredListEventTypesPaginateFiltersTypeDef, _OptionalListEventTypesPaginateFiltersTypeDef
):
    pass


ListEventTypesPaginatePaginationConfigTypeDef = TypedDict(
    "ListEventTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListEventTypesPaginateResponseEventTypesTypeDef = TypedDict(
    "ListEventTypesPaginateResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)

ListEventTypesPaginateResponseTypeDef = TypedDict(
    "ListEventTypesPaginateResponseTypeDef",
    {"EventTypes": List[ListEventTypesPaginateResponseEventTypesTypeDef]},
    total=False,
)

ListNotificationRulesPaginateFiltersTypeDef = TypedDict(
    "ListNotificationRulesPaginateFiltersTypeDef",
    {"Name": Literal["EVENT_TYPE_ID", "CREATED_BY", "RESOURCE", "TARGET_ADDRESS"], "Value": str},
    total=False,
)

ListNotificationRulesPaginatePaginationConfigTypeDef = TypedDict(
    "ListNotificationRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListNotificationRulesPaginateResponseNotificationRulesTypeDef = TypedDict(
    "ListNotificationRulesPaginateResponseNotificationRulesTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)

ListNotificationRulesPaginateResponseTypeDef = TypedDict(
    "ListNotificationRulesPaginateResponseTypeDef",
    {"NotificationRules": List[ListNotificationRulesPaginateResponseNotificationRulesTypeDef]},
    total=False,
)

ListTargetsPaginateFiltersTypeDef = TypedDict(
    "ListTargetsPaginateFiltersTypeDef",
    {"Name": Literal["TARGET_TYPE", "TARGET_ADDRESS", "TARGET_STATUS"], "Value": str},
    total=False,
)

ListTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTargetsPaginateResponseTargetsTypeDef = TypedDict(
    "ListTargetsPaginateResponseTargetsTypeDef",
    {
        "TargetAddress": str,
        "TargetType": str,
        "TargetStatus": Literal["PENDING", "ACTIVE", "UNREACHABLE", "INACTIVE", "DEACTIVATED"],
    },
    total=False,
)

ListTargetsPaginateResponseTypeDef = TypedDict(
    "ListTargetsPaginateResponseTypeDef",
    {"Targets": List[ListTargetsPaginateResponseTargetsTypeDef]},
    total=False,
)
