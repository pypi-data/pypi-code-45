"Main interface for codestar-notifications service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateNotificationRuleResponseTypeDef",
    "ClientCreateNotificationRuleTargetsTypeDef",
    "ClientDeleteNotificationRuleResponseTypeDef",
    "ClientDescribeNotificationRuleResponseEventTypesTypeDef",
    "ClientDescribeNotificationRuleResponseTargetsTypeDef",
    "ClientDescribeNotificationRuleResponseTypeDef",
    "ClientListEventTypesFiltersTypeDef",
    "ClientListEventTypesResponseEventTypesTypeDef",
    "ClientListEventTypesResponseTypeDef",
    "ClientListNotificationRulesFiltersTypeDef",
    "ClientListNotificationRulesResponseNotificationRulesTypeDef",
    "ClientListNotificationRulesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsFiltersTypeDef",
    "ClientListTargetsResponseTargetsTypeDef",
    "ClientListTargetsResponseTypeDef",
    "ClientSubscribeResponseTypeDef",
    "ClientSubscribeTargetTypeDef",
    "ClientTagResourceResponseTypeDef",
    "ClientUnsubscribeResponseTypeDef",
    "ClientUpdateNotificationRuleTargetsTypeDef",
    "ListEventTypesPaginateFiltersTypeDef",
    "ListEventTypesPaginatePaginationConfigTypeDef",
    "ListEventTypesPaginateResponseEventTypesTypeDef",
    "ListEventTypesPaginateResponseTypeDef",
    "ListNotificationRulesPaginateFiltersTypeDef",
    "ListNotificationRulesPaginatePaginationConfigTypeDef",
    "ListNotificationRulesPaginateResponseNotificationRulesTypeDef",
    "ListNotificationRulesPaginateResponseTypeDef",
    "ListTargetsPaginateFiltersTypeDef",
    "ListTargetsPaginatePaginationConfigTypeDef",
    "ListTargetsPaginateResponseTargetsTypeDef",
    "ListTargetsPaginateResponseTypeDef",
)


_ClientCreateNotificationRuleResponseTypeDef = TypedDict(
    "_ClientCreateNotificationRuleResponseTypeDef", {"Arn": str}, total=False
)


class ClientCreateNotificationRuleResponseTypeDef(_ClientCreateNotificationRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the notification rule.
    """


_ClientCreateNotificationRuleTargetsTypeDef = TypedDict(
    "_ClientCreateNotificationRuleTargetsTypeDef",
    {"TargetType": str, "TargetAddress": str},
    total=False,
)


class ClientCreateNotificationRuleTargetsTypeDef(_ClientCreateNotificationRuleTargetsTypeDef):
    """
    - *(dict) --*

      Information about the SNS topics associated with a notification rule.
      - **TargetType** *(string) --*

        The target type. Can be an Amazon SNS topic.
    """


_ClientDeleteNotificationRuleResponseTypeDef = TypedDict(
    "_ClientDeleteNotificationRuleResponseTypeDef", {"Arn": str}, total=False
)


class ClientDeleteNotificationRuleResponseTypeDef(_ClientDeleteNotificationRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the deleted notification rule.
    """


_ClientDescribeNotificationRuleResponseEventTypesTypeDef = TypedDict(
    "_ClientDescribeNotificationRuleResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)


class ClientDescribeNotificationRuleResponseEventTypesTypeDef(
    _ClientDescribeNotificationRuleResponseEventTypesTypeDef
):
    pass


_ClientDescribeNotificationRuleResponseTargetsTypeDef = TypedDict(
    "_ClientDescribeNotificationRuleResponseTargetsTypeDef",
    {
        "TargetAddress": str,
        "TargetType": str,
        "TargetStatus": Literal["PENDING", "ACTIVE", "UNREACHABLE", "INACTIVE", "DEACTIVATED"],
    },
    total=False,
)


class ClientDescribeNotificationRuleResponseTargetsTypeDef(
    _ClientDescribeNotificationRuleResponseTargetsTypeDef
):
    pass


_ClientDescribeNotificationRuleResponseTypeDef = TypedDict(
    "_ClientDescribeNotificationRuleResponseTypeDef",
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


class ClientDescribeNotificationRuleResponseTypeDef(_ClientDescribeNotificationRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the notification rule.
    """


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
    """
    - *(dict) --*

      Information about a filter to apply to the list of returned event types. You can filter by
      resource type or service name.
      - **Name** *(string) --***[REQUIRED]**

        The system-generated name of the filter type you want to filter by.
    """


_ClientListEventTypesResponseEventTypesTypeDef = TypedDict(
    "_ClientListEventTypesResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)


class ClientListEventTypesResponseEventTypesTypeDef(_ClientListEventTypesResponseEventTypesTypeDef):
    """
    - *(dict) --*

      Returns information about an event that has triggered a notification rule.
      - **EventTypeId** *(string) --*

        The system-generated ID of the event.
    """


_ClientListEventTypesResponseTypeDef = TypedDict(
    "_ClientListEventTypesResponseTypeDef",
    {"EventTypes": List[ClientListEventTypesResponseEventTypesTypeDef], "NextToken": str},
    total=False,
)


class ClientListEventTypesResponseTypeDef(_ClientListEventTypesResponseTypeDef):
    """
    - *(dict) --*

      - **EventTypes** *(list) --*

        Information about each event, including service name, resource type, event ID, and event
        name.
        - *(dict) --*

          Returns information about an event that has triggered a notification rule.
          - **EventTypeId** *(string) --*

            The system-generated ID of the event.
    """


_ClientListNotificationRulesFiltersTypeDef = TypedDict(
    "_ClientListNotificationRulesFiltersTypeDef",
    {"Name": Literal["EVENT_TYPE_ID", "CREATED_BY", "RESOURCE", "TARGET_ADDRESS"], "Value": str},
    total=False,
)


class ClientListNotificationRulesFiltersTypeDef(_ClientListNotificationRulesFiltersTypeDef):
    pass


_ClientListNotificationRulesResponseNotificationRulesTypeDef = TypedDict(
    "_ClientListNotificationRulesResponseNotificationRulesTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class ClientListNotificationRulesResponseNotificationRulesTypeDef(
    _ClientListNotificationRulesResponseNotificationRulesTypeDef
):
    pass


_ClientListNotificationRulesResponseTypeDef = TypedDict(
    "_ClientListNotificationRulesResponseTypeDef",
    {
        "NextToken": str,
        "NotificationRules": List[ClientListNotificationRulesResponseNotificationRulesTypeDef],
    },
    total=False,
)


class ClientListNotificationRulesResponseTypeDef(_ClientListNotificationRulesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        An enumeration token that can be used in a request to return the next batch of the results.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The tags associated with the notification rule.
        - *(string) --*

          - *(string) --*
    """


_ClientListTargetsFiltersTypeDef = TypedDict(
    "_ClientListTargetsFiltersTypeDef",
    {"Name": Literal["TARGET_TYPE", "TARGET_ADDRESS", "TARGET_STATUS"], "Value": str},
    total=False,
)


class ClientListTargetsFiltersTypeDef(_ClientListTargetsFiltersTypeDef):
    pass


_ClientListTargetsResponseTargetsTypeDef = TypedDict(
    "_ClientListTargetsResponseTargetsTypeDef",
    {
        "TargetAddress": str,
        "TargetType": str,
        "TargetStatus": Literal["PENDING", "ACTIVE", "UNREACHABLE", "INACTIVE", "DEACTIVATED"],
    },
    total=False,
)


class ClientListTargetsResponseTargetsTypeDef(_ClientListTargetsResponseTargetsTypeDef):
    """
    - *(dict) --*

      Information about the targets specified for a notification rule.
      - **TargetAddress** *(string) --*

        The Amazon Resource Name (ARN) of the SNS topic.
    """


_ClientListTargetsResponseTypeDef = TypedDict(
    "_ClientListTargetsResponseTypeDef",
    {"Targets": List[ClientListTargetsResponseTargetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTargetsResponseTypeDef(_ClientListTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        The list of notification rule targets.
        - *(dict) --*

          Information about the targets specified for a notification rule.
          - **TargetAddress** *(string) --*

            The Amazon Resource Name (ARN) of the SNS topic.
    """


_ClientSubscribeResponseTypeDef = TypedDict(
    "_ClientSubscribeResponseTypeDef", {"Arn": str}, total=False
)


class ClientSubscribeResponseTypeDef(_ClientSubscribeResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the notification rule for which you have created
        assocations.
    """


_ClientSubscribeTargetTypeDef = TypedDict(
    "_ClientSubscribeTargetTypeDef", {"TargetType": str, "TargetAddress": str}, total=False
)


class ClientSubscribeTargetTypeDef(_ClientSubscribeTargetTypeDef):
    """
    Information about the SNS topics associated with a notification rule.
    - **TargetType** *(string) --*

      The target type. Can be an Amazon SNS topic.
    """


_ClientTagResourceResponseTypeDef = TypedDict(
    "_ClientTagResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientTagResourceResponseTypeDef(_ClientTagResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The list of tags associated with the resource.
        - *(string) --*

          - *(string) --*
    """


_ClientUnsubscribeResponseTypeDef = TypedDict(
    "_ClientUnsubscribeResponseTypeDef", {"Arn": str}, total=False
)


class ClientUnsubscribeResponseTypeDef(_ClientUnsubscribeResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the the notification rule from which you have removed a
        subscription.
    """


_ClientUpdateNotificationRuleTargetsTypeDef = TypedDict(
    "_ClientUpdateNotificationRuleTargetsTypeDef",
    {"TargetType": str, "TargetAddress": str},
    total=False,
)


class ClientUpdateNotificationRuleTargetsTypeDef(_ClientUpdateNotificationRuleTargetsTypeDef):
    """
    - *(dict) --*

      Information about the SNS topics associated with a notification rule.
      - **TargetType** *(string) --*

        The target type. Can be an Amazon SNS topic.
    """


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
    """
    - *(dict) --*

      Information about a filter to apply to the list of returned event types. You can filter by
      resource type or service name.
      - **Name** *(string) --***[REQUIRED]**

        The system-generated name of the filter type you want to filter by.
    """


_ListEventTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEventTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEventTypesPaginatePaginationConfigTypeDef(_ListEventTypesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEventTypesPaginateResponseEventTypesTypeDef = TypedDict(
    "_ListEventTypesPaginateResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)


class ListEventTypesPaginateResponseEventTypesTypeDef(
    _ListEventTypesPaginateResponseEventTypesTypeDef
):
    """
    - *(dict) --*

      Returns information about an event that has triggered a notification rule.
      - **EventTypeId** *(string) --*

        The system-generated ID of the event.
    """


_ListEventTypesPaginateResponseTypeDef = TypedDict(
    "_ListEventTypesPaginateResponseTypeDef",
    {"EventTypes": List[ListEventTypesPaginateResponseEventTypesTypeDef]},
    total=False,
)


class ListEventTypesPaginateResponseTypeDef(_ListEventTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **EventTypes** *(list) --*

        Information about each event, including service name, resource type, event ID, and event
        name.
        - *(dict) --*

          Returns information about an event that has triggered a notification rule.
          - **EventTypeId** *(string) --*

            The system-generated ID of the event.
    """


_ListNotificationRulesPaginateFiltersTypeDef = TypedDict(
    "_ListNotificationRulesPaginateFiltersTypeDef",
    {"Name": Literal["EVENT_TYPE_ID", "CREATED_BY", "RESOURCE", "TARGET_ADDRESS"], "Value": str},
    total=False,
)


class ListNotificationRulesPaginateFiltersTypeDef(_ListNotificationRulesPaginateFiltersTypeDef):
    pass


_ListNotificationRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNotificationRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNotificationRulesPaginatePaginationConfigTypeDef(
    _ListNotificationRulesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListNotificationRulesPaginateResponseNotificationRulesTypeDef = TypedDict(
    "_ListNotificationRulesPaginateResponseNotificationRulesTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class ListNotificationRulesPaginateResponseNotificationRulesTypeDef(
    _ListNotificationRulesPaginateResponseNotificationRulesTypeDef
):
    """
    - *(dict) --*

      Information about a specified notification rule.
      - **Id** *(string) --*

        The unique ID of the notification rule.
    """


_ListNotificationRulesPaginateResponseTypeDef = TypedDict(
    "_ListNotificationRulesPaginateResponseTypeDef",
    {"NotificationRules": List[ListNotificationRulesPaginateResponseNotificationRulesTypeDef]},
    total=False,
)


class ListNotificationRulesPaginateResponseTypeDef(_ListNotificationRulesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NotificationRules** *(list) --*

        The list of notification rules for the AWS account, by Amazon Resource Name (ARN) and ID.
        - *(dict) --*

          Information about a specified notification rule.
          - **Id** *(string) --*

            The unique ID of the notification rule.
    """


_ListTargetsPaginateFiltersTypeDef = TypedDict(
    "_ListTargetsPaginateFiltersTypeDef",
    {"Name": Literal["TARGET_TYPE", "TARGET_ADDRESS", "TARGET_STATUS"], "Value": str},
    total=False,
)


class ListTargetsPaginateFiltersTypeDef(_ListTargetsPaginateFiltersTypeDef):
    pass


_ListTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsPaginatePaginationConfigTypeDef(_ListTargetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTargetsPaginateResponseTargetsTypeDef = TypedDict(
    "_ListTargetsPaginateResponseTargetsTypeDef",
    {
        "TargetAddress": str,
        "TargetType": str,
        "TargetStatus": Literal["PENDING", "ACTIVE", "UNREACHABLE", "INACTIVE", "DEACTIVATED"],
    },
    total=False,
)


class ListTargetsPaginateResponseTargetsTypeDef(_ListTargetsPaginateResponseTargetsTypeDef):
    """
    - *(dict) --*

      Information about the targets specified for a notification rule.
      - **TargetAddress** *(string) --*

        The Amazon Resource Name (ARN) of the SNS topic.
    """


_ListTargetsPaginateResponseTypeDef = TypedDict(
    "_ListTargetsPaginateResponseTypeDef",
    {"Targets": List[ListTargetsPaginateResponseTargetsTypeDef]},
    total=False,
)


class ListTargetsPaginateResponseTypeDef(_ListTargetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        The list of notification rule targets.
        - *(dict) --*

          Information about the targets specified for a notification rule.
          - **TargetAddress** *(string) --*

            The Amazon Resource Name (ARN) of the SNS topic.
    """
