"Main interface for sns service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef",
    "ClientConfirmSubscriptionResponseTypeDef",
    "ClientCreatePlatformApplicationResponseTypeDef",
    "ClientCreatePlatformEndpointResponseTypeDef",
    "ClientCreateTopicResponseTypeDef",
    "ClientCreateTopicTagsTypeDef",
    "ClientGetEndpointAttributesResponseTypeDef",
    "ClientGetPlatformApplicationAttributesResponseTypeDef",
    "ClientGetSmsAttributesResponseTypeDef",
    "ClientGetSubscriptionAttributesResponseTypeDef",
    "ClientGetTopicAttributesResponseTypeDef",
    "ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef",
    "ClientListEndpointsByPlatformApplicationResponseTypeDef",
    "ClientListPhoneNumbersOptedOutResponseTypeDef",
    "ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef",
    "ClientListPlatformApplicationsResponseTypeDef",
    "ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef",
    "ClientListSubscriptionsByTopicResponseTypeDef",
    "ClientListSubscriptionsResponseSubscriptionsTypeDef",
    "ClientListSubscriptionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTopicsResponseTopicsTypeDef",
    "ClientListTopicsResponseTypeDef",
    "ClientPublishMessageAttributesTypeDef",
    "ClientPublishResponseTypeDef",
    "ClientSubscribeResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef",
    "ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef",
    "ListEndpointsByPlatformApplicationPaginateResponseTypeDef",
    "ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef",
    "ListPhoneNumbersOptedOutPaginateResponseTypeDef",
    "ListPlatformApplicationsPaginatePaginationConfigTypeDef",
    "ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef",
    "ListPlatformApplicationsPaginateResponseTypeDef",
    "ListSubscriptionsByTopicPaginatePaginationConfigTypeDef",
    "ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef",
    "ListSubscriptionsByTopicPaginateResponseTypeDef",
    "ListSubscriptionsPaginatePaginationConfigTypeDef",
    "ListSubscriptionsPaginateResponseSubscriptionsTypeDef",
    "ListSubscriptionsPaginateResponseTypeDef",
    "ListTopicsPaginatePaginationConfigTypeDef",
    "ListTopicsPaginateResponseTopicsTypeDef",
    "ListTopicsPaginateResponseTypeDef",
    "PlatformEndpointPublishMessageAttributesTypeDef",
    "PlatformEndpointPublishResponseTypeDef",
    "ServiceResourceCreateTopicTagsTypeDef",
    "TopicPublishMessageAttributesTypeDef",
    "TopicPublishResponseTypeDef",
)


_ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef = TypedDict(
    "_ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef", {"isOptedOut": bool}, total=False
)


class ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef(
    _ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef
):
    """
    - *(dict) --*

      The response from the ``CheckIfPhoneNumberIsOptedOut`` action.
      - **isOptedOut** *(boolean) --*

        Indicates whether the phone number is opted out:
        * ``true`` – The phone number is opted out, meaning you cannot publish SMS messages to it.
        * ``false`` – The phone number is opted in, meaning you can publish SMS messages to it.
    """


_ClientConfirmSubscriptionResponseTypeDef = TypedDict(
    "_ClientConfirmSubscriptionResponseTypeDef", {"SubscriptionArn": str}, total=False
)


class ClientConfirmSubscriptionResponseTypeDef(_ClientConfirmSubscriptionResponseTypeDef):
    """
    - *(dict) --*

      Response for ConfirmSubscriptions action.
      - **SubscriptionArn** *(string) --*

        The ARN of the created subscription.
    """


_ClientCreatePlatformApplicationResponseTypeDef = TypedDict(
    "_ClientCreatePlatformApplicationResponseTypeDef", {"PlatformApplicationArn": str}, total=False
)


class ClientCreatePlatformApplicationResponseTypeDef(
    _ClientCreatePlatformApplicationResponseTypeDef
):
    """
    - *(dict) --*

      Response from CreatePlatformApplication action.
      - **PlatformApplicationArn** *(string) --*

        PlatformApplicationArn is returned.
    """


_ClientCreatePlatformEndpointResponseTypeDef = TypedDict(
    "_ClientCreatePlatformEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)


class ClientCreatePlatformEndpointResponseTypeDef(_ClientCreatePlatformEndpointResponseTypeDef):
    """
    - *(dict) --*

      Response from CreateEndpoint action.
      - **EndpointArn** *(string) --*

        EndpointArn returned from CreateEndpoint action.
    """


_ClientCreateTopicResponseTypeDef = TypedDict(
    "_ClientCreateTopicResponseTypeDef", {"TopicArn": str}, total=False
)


class ClientCreateTopicResponseTypeDef(_ClientCreateTopicResponseTypeDef):
    """
    - *(dict) --*

      Response from CreateTopic action.
      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) assigned to the created topic.
    """


_ClientCreateTopicTagsTypeDef = TypedDict(
    "_ClientCreateTopicTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateTopicTagsTypeDef(_ClientCreateTopicTagsTypeDef):
    pass


_ClientGetEndpointAttributesResponseTypeDef = TypedDict(
    "_ClientGetEndpointAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)


class ClientGetEndpointAttributesResponseTypeDef(_ClientGetEndpointAttributesResponseTypeDef):
    """
    - *(dict) --*

      Response from GetEndpointAttributes of the EndpointArn.
      - **Attributes** *(dict) --*

        Attributes include the following:
        * ``CustomUserData`` – arbitrary user data to associate with the endpoint. Amazon SNS does
        not use this data. The data must be in UTF-8 format and less than 2KB.
        * ``Enabled`` – flag that enables/disables delivery to the endpoint. Amazon SNS will set
        this to false when a notification service indicates to Amazon SNS that the endpoint is
        invalid. Users can set it back to true, typically after updating Token.
        * ``Token`` – device token, also referred to as a registration id, for an app and mobile
        device. This is returned from the notification service when an app and mobile device are
        registered with the notification service.
        .. note::

          The device token for the iOS platform is returned in lowercase.
    """


_ClientGetPlatformApplicationAttributesResponseTypeDef = TypedDict(
    "_ClientGetPlatformApplicationAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)


class ClientGetPlatformApplicationAttributesResponseTypeDef(
    _ClientGetPlatformApplicationAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Response for GetPlatformApplicationAttributes action.
      - **Attributes** *(dict) --*

        Attributes include the following:
        * ``EventEndpointCreated`` – Topic ARN to which EndpointCreated event notifications should
        be sent.
        * ``EventEndpointDeleted`` – Topic ARN to which EndpointDeleted event notifications should
        be sent.
        * ``EventEndpointUpdated`` – Topic ARN to which EndpointUpdate event notifications should be
        sent.
        * ``EventDeliveryFailure`` – Topic ARN to which DeliveryFailure event notifications should
        be sent upon Direct Publish delivery failure (permanent) to one of the application's
        endpoints.
        - *(string) --*

          - *(string) --*
    """


_ClientGetSmsAttributesResponseTypeDef = TypedDict(
    "_ClientGetSmsAttributesResponseTypeDef", {"attributes": Dict[str, str]}, total=False
)


class ClientGetSmsAttributesResponseTypeDef(_ClientGetSmsAttributesResponseTypeDef):
    """
    - *(dict) --*

      The response from the ``GetSMSAttributes`` request.
      - **attributes** *(dict) --*

        The SMS attribute names and their values.
        - *(string) --*

          - *(string) --*
    """


_ClientGetSubscriptionAttributesResponseTypeDef = TypedDict(
    "_ClientGetSubscriptionAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)


class ClientGetSubscriptionAttributesResponseTypeDef(
    _ClientGetSubscriptionAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Response for GetSubscriptionAttributes action.
      - **Attributes** *(dict) --*

        A map of the subscription's attributes. Attributes in this map include the following:
        * ``ConfirmationWasAuthenticated`` – ``true`` if the subscription confirmation request was
        authenticated.
        * ``DeliveryPolicy`` – The JSON serialization of the subscription's delivery policy.
        * ``EffectiveDeliveryPolicy`` – The JSON serialization of the effective delivery policy that
        takes into account the topic delivery policy and account system defaults.
        * ``FilterPolicy`` – The filter policy JSON that is assigned to the subscription.
        * ``Owner`` – The AWS account ID of the subscription's owner.
        * ``PendingConfirmation`` – ``true`` if the subscription hasn't been confirmed. To confirm a
        pending subscription, call the ``ConfirmSubscription`` action with a confirmation token.
        * ``RawMessageDelivery`` – ``true`` if raw message delivery is enabled for the subscription.
        Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints.
        * ``RedrivePolicy`` – When specified, sends undeliverable messages to the specified Amazon
        SQS dead-letter queue. Messages that can't be delivered due to client errors (for example,
        when the subscribed endpoint is unreachable) or server errors (for example, when the service
        that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue
        for further analysis or reprocessing.
        * ``SubscriptionArn`` – The subscription's ARN.
        * ``TopicArn`` – The topic ARN that the subscription is associated with.
        - *(string) --*

          - *(string) --*
    """


_ClientGetTopicAttributesResponseTypeDef = TypedDict(
    "_ClientGetTopicAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)


class ClientGetTopicAttributesResponseTypeDef(_ClientGetTopicAttributesResponseTypeDef):
    """
    - *(dict) --*

      Response for GetTopicAttributes action.
      - **Attributes** *(dict) --*

        A map of the topic's attributes. Attributes in this map include the following:
        * ``DeliveryPolicy`` – The JSON serialization of the topic's delivery policy.
        * ``DisplayName`` – The human-readable name used in the ``From`` field for notifications to
        ``email`` and ``email-json`` endpoints.
        * ``Owner`` – The AWS account ID of the topic's owner.
        * ``Policy`` – The JSON serialization of the topic's access control policy.
        * ``SubscriptionsConfirmed`` – The number of confirmed subscriptions for the topic.
        * ``SubscriptionsDeleted`` – The number of deleted subscriptions for the topic.
        * ``SubscriptionsPending`` – The number of subscriptions pending confirmation for the topic.
        * ``TopicArn`` – The topic's ARN.
        * ``EffectiveDeliveryPolicy`` – Yhe JSON serialization of the effective delivery policy,
        taking system defaults into account.
        The following attribute applies only to `server-side-encryption
        <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html>`__ :
        * ``KmsMasterKeyId`` - The ID of an AWS-managed customer master key (CMK) for Amazon SNS or
        a custom CMK. For more information, see `Key Terms
        <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms>`__
        . For more examples, see `KeyId
        <https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters>`__
        in the *AWS Key Management Service API Reference* .
        - *(string) --*

          - *(string) --*
    """


_ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef = TypedDict(
    "_ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef",
    {"EndpointArn": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef(
    _ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef
):
    """
    - *(dict) --*

      Endpoint for mobile app and device.
      - **EndpointArn** *(string) --*

        EndpointArn for mobile app and device.
    """


_ClientListEndpointsByPlatformApplicationResponseTypeDef = TypedDict(
    "_ClientListEndpointsByPlatformApplicationResponseTypeDef",
    {
        "Endpoints": List[ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEndpointsByPlatformApplicationResponseTypeDef(
    _ClientListEndpointsByPlatformApplicationResponseTypeDef
):
    """
    - *(dict) --*

      Response for ListEndpointsByPlatformApplication action.
      - **Endpoints** *(list) --*

        Endpoints returned for ListEndpointsByPlatformApplication action.
        - *(dict) --*

          Endpoint for mobile app and device.
          - **EndpointArn** *(string) --*

            EndpointArn for mobile app and device.
    """


_ClientListPhoneNumbersOptedOutResponseTypeDef = TypedDict(
    "_ClientListPhoneNumbersOptedOutResponseTypeDef",
    {"phoneNumbers": List[str], "nextToken": str},
    total=False,
)


class ClientListPhoneNumbersOptedOutResponseTypeDef(_ClientListPhoneNumbersOptedOutResponseTypeDef):
    """
    - *(dict) --*

      The response from the ``ListPhoneNumbersOptedOut`` action.
      - **phoneNumbers** *(list) --*

        A list of phone numbers that are opted out of receiving SMS messages. The list is paginated,
        and each page can contain up to 100 phone numbers.
        - *(string) --*
    """


_ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef = TypedDict(
    "_ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef",
    {"PlatformApplicationArn": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef(
    _ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef
):
    """
    - *(dict) --*

      Platform application object.
      - **PlatformApplicationArn** *(string) --*

        PlatformApplicationArn for platform application object.
    """


_ClientListPlatformApplicationsResponseTypeDef = TypedDict(
    "_ClientListPlatformApplicationsResponseTypeDef",
    {
        "PlatformApplications": List[
            ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPlatformApplicationsResponseTypeDef(_ClientListPlatformApplicationsResponseTypeDef):
    """
    - *(dict) --*

      Response for ListPlatformApplications action.
      - **PlatformApplications** *(list) --*

        Platform applications returned when calling ListPlatformApplications action.
        - *(dict) --*

          Platform application object.
          - **PlatformApplicationArn** *(string) --*

            PlatformApplicationArn for platform application object.
    """


_ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef = TypedDict(
    "_ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)


class ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef(
    _ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef
):
    """
    - *(dict) --*

      A wrapper type for the attributes of an Amazon SNS subscription.
      - **SubscriptionArn** *(string) --*

        The subscription's ARN.
    """


_ClientListSubscriptionsByTopicResponseTypeDef = TypedDict(
    "_ClientListSubscriptionsByTopicResponseTypeDef",
    {
        "Subscriptions": List[ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListSubscriptionsByTopicResponseTypeDef(_ClientListSubscriptionsByTopicResponseTypeDef):
    """
    - *(dict) --*

      Response for ListSubscriptionsByTopic action.
      - **Subscriptions** *(list) --*

        A list of subscriptions.
        - *(dict) --*

          A wrapper type for the attributes of an Amazon SNS subscription.
          - **SubscriptionArn** *(string) --*

            The subscription's ARN.
    """


_ClientListSubscriptionsResponseSubscriptionsTypeDef = TypedDict(
    "_ClientListSubscriptionsResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)


class ClientListSubscriptionsResponseSubscriptionsTypeDef(
    _ClientListSubscriptionsResponseSubscriptionsTypeDef
):
    """
    - *(dict) --*

      A wrapper type for the attributes of an Amazon SNS subscription.
      - **SubscriptionArn** *(string) --*

        The subscription's ARN.
    """


_ClientListSubscriptionsResponseTypeDef = TypedDict(
    "_ClientListSubscriptionsResponseTypeDef",
    {"Subscriptions": List[ClientListSubscriptionsResponseSubscriptionsTypeDef], "NextToken": str},
    total=False,
)


class ClientListSubscriptionsResponseTypeDef(_ClientListSubscriptionsResponseTypeDef):
    """
    - *(dict) --*

      Response for ListSubscriptions action
      - **Subscriptions** *(list) --*

        A list of subscriptions.
        - *(dict) --*

          A wrapper type for the attributes of an Amazon SNS subscription.
          - **SubscriptionArn** *(string) --*

            The subscription's ARN.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      The list of tags to be added to the specified topic.
      - **Key** *(string) --*

        The required key portion of the tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags associated with the specified topic.
        - *(dict) --*

          The list of tags to be added to the specified topic.
          - **Key** *(string) --*

            The required key portion of the tag.
    """


_ClientListTopicsResponseTopicsTypeDef = TypedDict(
    "_ClientListTopicsResponseTopicsTypeDef", {"TopicArn": str}, total=False
)


class ClientListTopicsResponseTopicsTypeDef(_ClientListTopicsResponseTopicsTypeDef):
    """
    - *(dict) --*

      A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's attributes,
      use ``GetTopicAttributes`` .
      - **TopicArn** *(string) --*

        The topic's ARN.
    """


_ClientListTopicsResponseTypeDef = TypedDict(
    "_ClientListTopicsResponseTypeDef",
    {"Topics": List[ClientListTopicsResponseTopicsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTopicsResponseTypeDef(_ClientListTopicsResponseTypeDef):
    """
    - *(dict) --*

      Response for ListTopics action.
      - **Topics** *(list) --*

        A list of topic ARNs.
        - *(dict) --*

          A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
          attributes, use ``GetTopicAttributes`` .
          - **TopicArn** *(string) --*

            The topic's ARN.
    """


_ClientPublishMessageAttributesTypeDef = TypedDict(
    "_ClientPublishMessageAttributesTypeDef",
    {"DataType": str, "StringValue": str, "BinaryValue": bytes},
    total=False,
)


class ClientPublishMessageAttributesTypeDef(_ClientPublishMessageAttributesTypeDef):
    pass


_ClientPublishResponseTypeDef = TypedDict(
    "_ClientPublishResponseTypeDef", {"MessageId": str}, total=False
)


class ClientPublishResponseTypeDef(_ClientPublishResponseTypeDef):
    """
    - *(dict) --*

      Response for Publish action.
      - **MessageId** *(string) --*

        Unique identifier assigned to the published message.
        Length Constraint: Maximum 100 characters
    """


_ClientSubscribeResponseTypeDef = TypedDict(
    "_ClientSubscribeResponseTypeDef", {"SubscriptionArn": str}, total=False
)


class ClientSubscribeResponseTypeDef(_ClientSubscribeResponseTypeDef):
    """
    - *(dict) --*

      Response for Subscribe action.
      - **SubscriptionArn** *(string) --*

        The ARN of the subscription if it is confirmed, or the string "pending confirmation" if the
        subscription requires confirmation. However, if the API request parameter
        ``ReturnSubscriptionArn`` is true, then the value is always the subscription ARN, even if
        the subscription requires confirmation.
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

      The list of tags to be added to the specified topic.
      - **Key** *(string) --***[REQUIRED]**

        The required key portion of the tag.
    """


_ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef(
    _ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef = TypedDict(
    "_ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef",
    {"EndpointArn": str, "Attributes": Dict[str, str]},
    total=False,
)


class ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef(
    _ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef
):
    """
    - *(dict) --*

      Endpoint for mobile app and device.
      - **EndpointArn** *(string) --*

        EndpointArn for mobile app and device.
    """


_ListEndpointsByPlatformApplicationPaginateResponseTypeDef = TypedDict(
    "_ListEndpointsByPlatformApplicationPaginateResponseTypeDef",
    {"Endpoints": List[ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef]},
    total=False,
)


class ListEndpointsByPlatformApplicationPaginateResponseTypeDef(
    _ListEndpointsByPlatformApplicationPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Response for ListEndpointsByPlatformApplication action.
      - **Endpoints** *(list) --*

        Endpoints returned for ListEndpointsByPlatformApplication action.
        - *(dict) --*

          Endpoint for mobile app and device.
          - **EndpointArn** *(string) --*

            EndpointArn for mobile app and device.
    """


_ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef(
    _ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPhoneNumbersOptedOutPaginateResponseTypeDef = TypedDict(
    "_ListPhoneNumbersOptedOutPaginateResponseTypeDef",
    {"phoneNumbers": List[str], "NextToken": str},
    total=False,
)


class ListPhoneNumbersOptedOutPaginateResponseTypeDef(
    _ListPhoneNumbersOptedOutPaginateResponseTypeDef
):
    """
    - *(dict) --*

      The response from the ``ListPhoneNumbersOptedOut`` action.
      - **phoneNumbers** *(list) --*

        A list of phone numbers that are opted out of receiving SMS messages. The list is paginated,
        and each page can contain up to 100 phone numbers.
        - *(string) --*
    """


_ListPlatformApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPlatformApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPlatformApplicationsPaginatePaginationConfigTypeDef(
    _ListPlatformApplicationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef = TypedDict(
    "_ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef",
    {"PlatformApplicationArn": str, "Attributes": Dict[str, str]},
    total=False,
)


class ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef(
    _ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef
):
    """
    - *(dict) --*

      Platform application object.
      - **PlatformApplicationArn** *(string) --*

        PlatformApplicationArn for platform application object.
    """


_ListPlatformApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListPlatformApplicationsPaginateResponseTypeDef",
    {
        "PlatformApplications": List[
            ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef
        ]
    },
    total=False,
)


class ListPlatformApplicationsPaginateResponseTypeDef(
    _ListPlatformApplicationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Response for ListPlatformApplications action.
      - **PlatformApplications** *(list) --*

        Platform applications returned when calling ListPlatformApplications action.
        - *(dict) --*

          Platform application object.
          - **PlatformApplicationArn** *(string) --*

            PlatformApplicationArn for platform application object.
    """


_ListSubscriptionsByTopicPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscriptionsByTopicPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListSubscriptionsByTopicPaginatePaginationConfigTypeDef(
    _ListSubscriptionsByTopicPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef = TypedDict(
    "_ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)


class ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef(
    _ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef
):
    """
    - *(dict) --*

      A wrapper type for the attributes of an Amazon SNS subscription.
      - **SubscriptionArn** *(string) --*

        The subscription's ARN.
    """


_ListSubscriptionsByTopicPaginateResponseTypeDef = TypedDict(
    "_ListSubscriptionsByTopicPaginateResponseTypeDef",
    {"Subscriptions": List[ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef]},
    total=False,
)


class ListSubscriptionsByTopicPaginateResponseTypeDef(
    _ListSubscriptionsByTopicPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Response for ListSubscriptionsByTopic action.
      - **Subscriptions** *(list) --*

        A list of subscriptions.
        - *(dict) --*

          A wrapper type for the attributes of an Amazon SNS subscription.
          - **SubscriptionArn** *(string) --*

            The subscription's ARN.
    """


_ListSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListSubscriptionsPaginatePaginationConfigTypeDef(
    _ListSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSubscriptionsPaginateResponseSubscriptionsTypeDef = TypedDict(
    "_ListSubscriptionsPaginateResponseSubscriptionsTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)


class ListSubscriptionsPaginateResponseSubscriptionsTypeDef(
    _ListSubscriptionsPaginateResponseSubscriptionsTypeDef
):
    """
    - *(dict) --*

      A wrapper type for the attributes of an Amazon SNS subscription.
      - **SubscriptionArn** *(string) --*

        The subscription's ARN.
    """


_ListSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_ListSubscriptionsPaginateResponseTypeDef",
    {"Subscriptions": List[ListSubscriptionsPaginateResponseSubscriptionsTypeDef]},
    total=False,
)


class ListSubscriptionsPaginateResponseTypeDef(_ListSubscriptionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Response for ListSubscriptions action
      - **Subscriptions** *(list) --*

        A list of subscriptions.
        - *(dict) --*

          A wrapper type for the attributes of an Amazon SNS subscription.
          - **SubscriptionArn** *(string) --*

            The subscription's ARN.
    """


_ListTopicsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTopicsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTopicsPaginatePaginationConfigTypeDef(_ListTopicsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTopicsPaginateResponseTopicsTypeDef = TypedDict(
    "_ListTopicsPaginateResponseTopicsTypeDef", {"TopicArn": str}, total=False
)


class ListTopicsPaginateResponseTopicsTypeDef(_ListTopicsPaginateResponseTopicsTypeDef):
    """
    - *(dict) --*

      A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's attributes,
      use ``GetTopicAttributes`` .
      - **TopicArn** *(string) --*

        The topic's ARN.
    """


_ListTopicsPaginateResponseTypeDef = TypedDict(
    "_ListTopicsPaginateResponseTypeDef",
    {"Topics": List[ListTopicsPaginateResponseTopicsTypeDef]},
    total=False,
)


class ListTopicsPaginateResponseTypeDef(_ListTopicsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Response for ListTopics action.
      - **Topics** *(list) --*

        A list of topic ARNs.
        - *(dict) --*

          A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
          attributes, use ``GetTopicAttributes`` .
          - **TopicArn** *(string) --*

            The topic's ARN.
    """


_PlatformEndpointPublishMessageAttributesTypeDef = TypedDict(
    "_PlatformEndpointPublishMessageAttributesTypeDef",
    {"DataType": str, "StringValue": str, "BinaryValue": bytes},
    total=False,
)


class PlatformEndpointPublishMessageAttributesTypeDef(
    _PlatformEndpointPublishMessageAttributesTypeDef
):
    pass


_PlatformEndpointPublishResponseTypeDef = TypedDict(
    "_PlatformEndpointPublishResponseTypeDef", {"MessageId": str}, total=False
)


class PlatformEndpointPublishResponseTypeDef(_PlatformEndpointPublishResponseTypeDef):
    """
    - *(dict) --*

      Response for Publish action.
      - **MessageId** *(string) --*

        Unique identifier assigned to the published message.
        Length Constraint: Maximum 100 characters
    """


_ServiceResourceCreateTopicTagsTypeDef = TypedDict(
    "_ServiceResourceCreateTopicTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ServiceResourceCreateTopicTagsTypeDef(_ServiceResourceCreateTopicTagsTypeDef):
    pass


_TopicPublishMessageAttributesTypeDef = TypedDict(
    "_TopicPublishMessageAttributesTypeDef",
    {"DataType": str, "StringValue": str, "BinaryValue": bytes},
    total=False,
)


class TopicPublishMessageAttributesTypeDef(_TopicPublishMessageAttributesTypeDef):
    pass


_TopicPublishResponseTypeDef = TypedDict(
    "_TopicPublishResponseTypeDef", {"MessageId": str}, total=False
)


class TopicPublishResponseTypeDef(_TopicPublishResponseTypeDef):
    """
    - *(dict) --*

      Response for Publish action.
      - **MessageId** *(string) --*

        Unique identifier assigned to the published message.
        Length Constraint: Maximum 100 characters
    """
