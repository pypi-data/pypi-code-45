"Main interface for sns service type defs"
from __future__ import annotations

import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef = TypedDict(
    "ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef", {"isOptedOut": bool}, total=False
)

ClientConfirmSubscriptionResponseTypeDef = TypedDict(
    "ClientConfirmSubscriptionResponseTypeDef", {"SubscriptionArn": str}, total=False
)

ClientCreatePlatformApplicationResponseTypeDef = TypedDict(
    "ClientCreatePlatformApplicationResponseTypeDef", {"PlatformApplicationArn": str}, total=False
)

ClientCreatePlatformEndpointResponseTypeDef = TypedDict(
    "ClientCreatePlatformEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)

ClientCreateTopicResponseTypeDef = TypedDict(
    "ClientCreateTopicResponseTypeDef", {"TopicArn": str}, total=False
)

ClientCreateTopicTagsTypeDef = TypedDict(
    "ClientCreateTopicTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetEndpointAttributesResponseTypeDef = TypedDict(
    "ClientGetEndpointAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientGetPlatformApplicationAttributesResponseTypeDef = TypedDict(
    "ClientGetPlatformApplicationAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)

ClientGetSmsAttributesResponseTypeDef = TypedDict(
    "ClientGetSmsAttributesResponseTypeDef", {"attributes": Dict[str, str]}, total=False
)

ClientGetSubscriptionAttributesResponseTypeDef = TypedDict(
    "ClientGetSubscriptionAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientGetTopicAttributesResponseTypeDef = TypedDict(
    "ClientGetTopicAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef = TypedDict(
    "ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef",
    {"EndpointArn": str, "Attributes": Dict[str, str]},
    total=False,
)

ClientListEndpointsByPlatformApplicationResponseTypeDef = TypedDict(
    "ClientListEndpointsByPlatformApplicationResponseTypeDef",
    {
        "Endpoints": List[ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListPhoneNumbersOptedOutResponseTypeDef = TypedDict(
    "ClientListPhoneNumbersOptedOutResponseTypeDef",
    {"phoneNumbers": List[str], "nextToken": str},
    total=False,
)

ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef = TypedDict(
    "ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef",
    {"PlatformApplicationArn": str, "Attributes": Dict[str, str]},
    total=False,
)

ClientListPlatformApplicationsResponseTypeDef = TypedDict(
    "ClientListPlatformApplicationsResponseTypeDef",
    {
        "PlatformApplications": List[
            ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef = TypedDict(
    "ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)

ClientListSubscriptionsByTopicResponseTypeDef = TypedDict(
    "ClientListSubscriptionsByTopicResponseTypeDef",
    {
        "Subscriptions": List[ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListSubscriptionsResponseSubscriptionsTypeDef = TypedDict(
    "ClientListSubscriptionsResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)

ClientListSubscriptionsResponseTypeDef = TypedDict(
    "ClientListSubscriptionsResponseTypeDef",
    {"Subscriptions": List[ClientListSubscriptionsResponseSubscriptionsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListTopicsResponseTopicsTypeDef = TypedDict(
    "ClientListTopicsResponseTopicsTypeDef", {"TopicArn": str}, total=False
)

ClientListTopicsResponseTypeDef = TypedDict(
    "ClientListTopicsResponseTypeDef",
    {"Topics": List[ClientListTopicsResponseTopicsTypeDef], "NextToken": str},
    total=False,
)

ClientPublishMessageAttributesTypeDef = TypedDict(
    "ClientPublishMessageAttributesTypeDef",
    {"DataType": str, "StringValue": str, "BinaryValue": bytes},
    total=False,
)

ClientPublishResponseTypeDef = TypedDict(
    "ClientPublishResponseTypeDef", {"MessageId": str}, total=False
)

ClientSubscribeResponseTypeDef = TypedDict(
    "ClientSubscribeResponseTypeDef", {"SubscriptionArn": str}, total=False
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef",
    {"EndpointArn": str, "Attributes": Dict[str, str]},
    total=False,
)

ListEndpointsByPlatformApplicationPaginateResponseTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationPaginateResponseTypeDef",
    {"Endpoints": List[ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef]},
    total=False,
)

ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListPhoneNumbersOptedOutPaginateResponseTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutPaginateResponseTypeDef",
    {"phoneNumbers": List[str], "NextToken": str},
    total=False,
)

ListPlatformApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPlatformApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef = TypedDict(
    "ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef",
    {"PlatformApplicationArn": str, "Attributes": Dict[str, str]},
    total=False,
)

ListPlatformApplicationsPaginateResponseTypeDef = TypedDict(
    "ListPlatformApplicationsPaginateResponseTypeDef",
    {
        "PlatformApplications": List[
            ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef
        ]
    },
    total=False,
)

ListSubscriptionsByTopicPaginatePaginationConfigTypeDef = TypedDict(
    "ListSubscriptionsByTopicPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef = TypedDict(
    "ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)

ListSubscriptionsByTopicPaginateResponseTypeDef = TypedDict(
    "ListSubscriptionsByTopicPaginateResponseTypeDef",
    {"Subscriptions": List[ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef]},
    total=False,
)

ListSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListSubscriptionsPaginateResponseSubscriptionsTypeDef = TypedDict(
    "ListSubscriptionsPaginateResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)

ListSubscriptionsPaginateResponseTypeDef = TypedDict(
    "ListSubscriptionsPaginateResponseTypeDef",
    {"Subscriptions": List[ListSubscriptionsPaginateResponseSubscriptionsTypeDef]},
    total=False,
)

ListTopicsPaginatePaginationConfigTypeDef = TypedDict(
    "ListTopicsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListTopicsPaginateResponseTopicsTypeDef = TypedDict(
    "ListTopicsPaginateResponseTopicsTypeDef", {"TopicArn": str}, total=False
)

ListTopicsPaginateResponseTypeDef = TypedDict(
    "ListTopicsPaginateResponseTypeDef",
    {"Topics": List[ListTopicsPaginateResponseTopicsTypeDef]},
    total=False,
)

PlatformEndpointPublishMessageAttributesTypeDef = TypedDict(
    "PlatformEndpointPublishMessageAttributesTypeDef",
    {"DataType": str, "StringValue": str, "BinaryValue": bytes},
    total=False,
)

PlatformEndpointPublishResponseTypeDef = TypedDict(
    "PlatformEndpointPublishResponseTypeDef", {"MessageId": str}, total=False
)

ServiceResourceCreateTopicTagsTypeDef = TypedDict(
    "ServiceResourceCreateTopicTagsTypeDef", {"Key": str, "Value": str}, total=False
)

TopicPublishMessageAttributesTypeDef = TypedDict(
    "TopicPublishMessageAttributesTypeDef",
    {"DataType": str, "StringValue": str, "BinaryValue": bytes},
    total=False,
)

TopicPublishResponseTypeDef = TypedDict(
    "TopicPublishResponseTypeDef", {"MessageId": str}, total=False
)
