"Main interface for cloudtrail service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddTagsTagsListTypeDef",
    "ClientCreateTrailResponseTypeDef",
    "ClientCreateTrailTagsListTypeDef",
    "ClientDescribeTrailsResponsetrailListTypeDef",
    "ClientDescribeTrailsResponseTypeDef",
    "ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    "ClientGetEventSelectorsResponseEventSelectorsTypeDef",
    "ClientGetEventSelectorsResponseTypeDef",
    "ClientGetInsightSelectorsResponseInsightSelectorsTypeDef",
    "ClientGetInsightSelectorsResponseTypeDef",
    "ClientGetTrailResponseTrailTypeDef",
    "ClientGetTrailResponseTypeDef",
    "ClientGetTrailStatusResponseTypeDef",
    "ClientListPublicKeysResponsePublicKeyListTypeDef",
    "ClientListPublicKeysResponseTypeDef",
    "ClientListTagsResponseResourceTagListTagsListTypeDef",
    "ClientListTagsResponseResourceTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListTrailsResponseTrailsTypeDef",
    "ClientListTrailsResponseTypeDef",
    "ClientLookupEventsLookupAttributesTypeDef",
    "ClientLookupEventsResponseEventsResourcesTypeDef",
    "ClientLookupEventsResponseEventsTypeDef",
    "ClientLookupEventsResponseTypeDef",
    "ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef",
    "ClientPutEventSelectorsEventSelectorsTypeDef",
    "ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    "ClientPutEventSelectorsResponseEventSelectorsTypeDef",
    "ClientPutEventSelectorsResponseTypeDef",
    "ClientPutInsightSelectorsInsightSelectorsTypeDef",
    "ClientPutInsightSelectorsResponseInsightSelectorsTypeDef",
    "ClientPutInsightSelectorsResponseTypeDef",
    "ClientRemoveTagsTagsListTypeDef",
    "ClientUpdateTrailResponseTypeDef",
    "ListPublicKeysPaginatePaginationConfigTypeDef",
    "ListPublicKeysPaginateResponsePublicKeyListTypeDef",
    "ListPublicKeysPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseResourceTagListTagsListTypeDef",
    "ListTagsPaginateResponseResourceTagListTypeDef",
    "ListTagsPaginateResponseTypeDef",
    "ListTrailsPaginatePaginationConfigTypeDef",
    "ListTrailsPaginateResponseTrailsTypeDef",
    "ListTrailsPaginateResponseTypeDef",
    "LookupEventsPaginateLookupAttributesTypeDef",
    "LookupEventsPaginatePaginationConfigTypeDef",
    "LookupEventsPaginateResponseEventsResourcesTypeDef",
    "LookupEventsPaginateResponseEventsTypeDef",
    "LookupEventsPaginateResponseTypeDef",
)


_RequiredClientAddTagsTagsListTypeDef = TypedDict(
    "_RequiredClientAddTagsTagsListTypeDef", {"Key": str}
)
_OptionalClientAddTagsTagsListTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsListTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsListTypeDef(
    _RequiredClientAddTagsTagsListTypeDef, _OptionalClientAddTagsTagsListTypeDef
):
    """
    - *(dict) --*

      A custom key-value pair associated with a resource such as a CloudTrail trail.
      - **Key** *(string) --***[REQUIRED]**

        The key in a key-value pair. The key must be must be no longer than 128 Unicode characters.
        The key must be unique for the resource to which it applies.
    """


_ClientCreateTrailResponseTypeDef = TypedDict(
    "_ClientCreateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class ClientCreateTrailResponseTypeDef(_ClientCreateTrailResponseTypeDef):
    """
    - *(dict) --*

      Returns the objects or data listed below if successful. Otherwise, returns an error.
      - **Name** *(string) --*

        Specifies the name of the trail.
    """


_RequiredClientCreateTrailTagsListTypeDef = TypedDict(
    "_RequiredClientCreateTrailTagsListTypeDef", {"Key": str}
)
_OptionalClientCreateTrailTagsListTypeDef = TypedDict(
    "_OptionalClientCreateTrailTagsListTypeDef", {"Value": str}, total=False
)


class ClientCreateTrailTagsListTypeDef(
    _RequiredClientCreateTrailTagsListTypeDef, _OptionalClientCreateTrailTagsListTypeDef
):
    """
    - *(dict) --*

      A custom key-value pair associated with a resource such as a CloudTrail trail.
      - **Key** *(string) --***[REQUIRED]**

        The key in a key-value pair. The key must be must be no longer than 128 Unicode characters.
        The key must be unique for the resource to which it applies.
    """


_ClientDescribeTrailsResponsetrailListTypeDef = TypedDict(
    "_ClientDescribeTrailsResponsetrailListTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "HasInsightSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class ClientDescribeTrailsResponsetrailListTypeDef(_ClientDescribeTrailsResponsetrailListTypeDef):
    """
    - *(dict) --*

      The settings for a trail.
      - **Name** *(string) --*

        Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.
    """


_ClientDescribeTrailsResponseTypeDef = TypedDict(
    "_ClientDescribeTrailsResponseTypeDef",
    {"trailList": List[ClientDescribeTrailsResponsetrailListTypeDef]},
    total=False,
)


class ClientDescribeTrailsResponseTypeDef(_ClientDescribeTrailsResponseTypeDef):
    """
    - *(dict) --*

      Returns the objects or data listed below if successful. Otherwise, returns an error.
      - **trailList** *(list) --*

        The list of trail objects. Trail objects with string values are only returned if values for
        the objects exist in a trail's configuration. For example, ``SNSTopicName`` and
        ``SNSTopicARN`` are only returned in results if a trail is configured to send SNS
        notifications. Similarly, ``KMSKeyId`` only appears in results if a trail's log files are
        encrypted with AWS KMS-managed keys.
        - *(dict) --*

          The settings for a trail.
          - **Name** *(string) --*

            Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.
    """


_ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef = TypedDict(
    "_ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)


class ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef(
    _ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef
):
    pass


_ClientGetEventSelectorsResponseEventSelectorsTypeDef = TypedDict(
    "_ClientGetEventSelectorsResponseEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)


class ClientGetEventSelectorsResponseEventSelectorsTypeDef(
    _ClientGetEventSelectorsResponseEventSelectorsTypeDef
):
    pass


_ClientGetEventSelectorsResponseTypeDef = TypedDict(
    "_ClientGetEventSelectorsResponseTypeDef",
    {"TrailARN": str, "EventSelectors": List[ClientGetEventSelectorsResponseEventSelectorsTypeDef]},
    total=False,
)


class ClientGetEventSelectorsResponseTypeDef(_ClientGetEventSelectorsResponseTypeDef):
    """
    - *(dict) --*

      - **TrailARN** *(string) --*

        The specified trail ARN that has the event selectors.
    """


_ClientGetInsightSelectorsResponseInsightSelectorsTypeDef = TypedDict(
    "_ClientGetInsightSelectorsResponseInsightSelectorsTypeDef", {"InsightType": str}, total=False
)


class ClientGetInsightSelectorsResponseInsightSelectorsTypeDef(
    _ClientGetInsightSelectorsResponseInsightSelectorsTypeDef
):
    pass


_ClientGetInsightSelectorsResponseTypeDef = TypedDict(
    "_ClientGetInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[ClientGetInsightSelectorsResponseInsightSelectorsTypeDef],
    },
    total=False,
)


class ClientGetInsightSelectorsResponseTypeDef(_ClientGetInsightSelectorsResponseTypeDef):
    """
    - *(dict) --*

      - **TrailARN** *(string) --*

        The Amazon Resource Name (ARN) of a trail for which you want to get Insights selectors.
    """


_ClientGetTrailResponseTrailTypeDef = TypedDict(
    "_ClientGetTrailResponseTrailTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "HasInsightSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class ClientGetTrailResponseTrailTypeDef(_ClientGetTrailResponseTrailTypeDef):
    """
    - **Trail** *(dict) --*

      The settings for a trail.
      - **Name** *(string) --*

        Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.
    """


_ClientGetTrailResponseTypeDef = TypedDict(
    "_ClientGetTrailResponseTypeDef", {"Trail": ClientGetTrailResponseTrailTypeDef}, total=False
)


class ClientGetTrailResponseTypeDef(_ClientGetTrailResponseTypeDef):
    """
    - *(dict) --*

      - **Trail** *(dict) --*

        The settings for a trail.
        - **Name** *(string) --*

          Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.
    """


_ClientGetTrailStatusResponseTypeDef = TypedDict(
    "_ClientGetTrailStatusResponseTypeDef",
    {
        "IsLogging": bool,
        "LatestDeliveryError": str,
        "LatestNotificationError": str,
        "LatestDeliveryTime": datetime,
        "LatestNotificationTime": datetime,
        "StartLoggingTime": datetime,
        "StopLoggingTime": datetime,
        "LatestCloudWatchLogsDeliveryError": str,
        "LatestCloudWatchLogsDeliveryTime": datetime,
        "LatestDigestDeliveryTime": datetime,
        "LatestDigestDeliveryError": str,
        "LatestDeliveryAttemptTime": str,
        "LatestNotificationAttemptTime": str,
        "LatestNotificationAttemptSucceeded": str,
        "LatestDeliveryAttemptSucceeded": str,
        "TimeLoggingStarted": str,
        "TimeLoggingStopped": str,
    },
    total=False,
)


class ClientGetTrailStatusResponseTypeDef(_ClientGetTrailStatusResponseTypeDef):
    """
    - *(dict) --*

      Returns the objects or data listed below if successful. Otherwise, returns an error.
      - **IsLogging** *(boolean) --*

        Whether the CloudTrail is currently logging AWS API calls.
    """


_ClientListPublicKeysResponsePublicKeyListTypeDef = TypedDict(
    "_ClientListPublicKeysResponsePublicKeyListTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)


class ClientListPublicKeysResponsePublicKeyListTypeDef(
    _ClientListPublicKeysResponsePublicKeyListTypeDef
):
    pass


_ClientListPublicKeysResponseTypeDef = TypedDict(
    "_ClientListPublicKeysResponseTypeDef",
    {"PublicKeyList": List[ClientListPublicKeysResponsePublicKeyListTypeDef], "NextToken": str},
    total=False,
)


class ClientListPublicKeysResponseTypeDef(_ClientListPublicKeysResponseTypeDef):
    """
    - *(dict) --*

      Returns the objects or data listed below if successful. Otherwise, returns an error.
      - **PublicKeyList** *(list) --*

        Contains an array of PublicKey objects.
        .. note::

          The returned public keys may have validity time ranges that overlap.
    """


_ClientListTagsResponseResourceTagListTagsListTypeDef = TypedDict(
    "_ClientListTagsResponseResourceTagListTagsListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseResourceTagListTagsListTypeDef(
    _ClientListTagsResponseResourceTagListTagsListTypeDef
):
    pass


_ClientListTagsResponseResourceTagListTypeDef = TypedDict(
    "_ClientListTagsResponseResourceTagListTypeDef",
    {"ResourceId": str, "TagsList": List[ClientListTagsResponseResourceTagListTagsListTypeDef]},
    total=False,
)


class ClientListTagsResponseResourceTagListTypeDef(_ClientListTagsResponseResourceTagListTypeDef):
    """
    - *(dict) --*

      A resource tag.
      - **ResourceId** *(string) --*

        Specifies the ARN of the resource.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"ResourceTagList": List[ClientListTagsResponseResourceTagListTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      Returns the objects or data listed below if successful. Otherwise, returns an error.
      - **ResourceTagList** *(list) --*

        A list of resource tags.
        - *(dict) --*

          A resource tag.
          - **ResourceId** *(string) --*

            Specifies the ARN of the resource.
    """


_ClientListTrailsResponseTrailsTypeDef = TypedDict(
    "_ClientListTrailsResponseTrailsTypeDef",
    {"TrailARN": str, "Name": str, "HomeRegion": str},
    total=False,
)


class ClientListTrailsResponseTrailsTypeDef(_ClientListTrailsResponseTrailsTypeDef):
    """
    - *(dict) --*

      Information about a CloudTrail trail, including the trail's name, home region, and Amazon
      Resource Name (ARN).
      - **TrailARN** *(string) --*

        The ARN of a trail.
    """


_ClientListTrailsResponseTypeDef = TypedDict(
    "_ClientListTrailsResponseTypeDef",
    {"Trails": List[ClientListTrailsResponseTrailsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTrailsResponseTypeDef(_ClientListTrailsResponseTypeDef):
    """
    - *(dict) --*

      - **Trails** *(list) --*

        Returns the name, ARN, and home region of trails in the current account.
        - *(dict) --*

          Information about a CloudTrail trail, including the trail's name, home region, and Amazon
          Resource Name (ARN).
          - **TrailARN** *(string) --*

            The ARN of a trail.
    """


_RequiredClientLookupEventsLookupAttributesTypeDef = TypedDict(
    "_RequiredClientLookupEventsLookupAttributesTypeDef",
    {
        "AttributeKey": Literal[
            "EventId",
            "EventName",
            "ReadOnly",
            "Username",
            "ResourceType",
            "ResourceName",
            "EventSource",
            "AccessKeyId",
        ]
    },
)
_OptionalClientLookupEventsLookupAttributesTypeDef = TypedDict(
    "_OptionalClientLookupEventsLookupAttributesTypeDef", {"AttributeValue": str}, total=False
)


class ClientLookupEventsLookupAttributesTypeDef(
    _RequiredClientLookupEventsLookupAttributesTypeDef,
    _OptionalClientLookupEventsLookupAttributesTypeDef,
):
    """
    - *(dict) --*

      Specifies an attribute and value that filter the events returned.
      - **AttributeKey** *(string) --***[REQUIRED]**

        Specifies an attribute on which to filter the events returned.
    """


_ClientLookupEventsResponseEventsResourcesTypeDef = TypedDict(
    "_ClientLookupEventsResponseEventsResourcesTypeDef",
    {"ResourceType": str, "ResourceName": str},
    total=False,
)


class ClientLookupEventsResponseEventsResourcesTypeDef(
    _ClientLookupEventsResponseEventsResourcesTypeDef
):
    pass


_ClientLookupEventsResponseEventsTypeDef = TypedDict(
    "_ClientLookupEventsResponseEventsTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List[ClientLookupEventsResponseEventsResourcesTypeDef],
        "CloudTrailEvent": str,
    },
    total=False,
)


class ClientLookupEventsResponseEventsTypeDef(_ClientLookupEventsResponseEventsTypeDef):
    """
    - *(dict) --*

      Contains information about an event that was returned by a lookup request. The result includes
      a representation of a CloudTrail event.
      - **EventId** *(string) --*

        The CloudTrail ID of the event returned.
    """


_ClientLookupEventsResponseTypeDef = TypedDict(
    "_ClientLookupEventsResponseTypeDef",
    {"Events": List[ClientLookupEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientLookupEventsResponseTypeDef(_ClientLookupEventsResponseTypeDef):
    """
    - *(dict) --*

      Contains a response to a LookupEvents action.
      - **Events** *(list) --*

        A list of events returned based on the lookup attributes specified and the CloudTrail event.
        The events list is sorted by time. The most recent event is listed first.
        - *(dict) --*

          Contains information about an event that was returned by a lookup request. The result
          includes a representation of a CloudTrail event.
          - **EventId** *(string) --*

            The CloudTrail ID of the event returned.
    """


_ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef = TypedDict(
    "_ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)


class ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef(
    _ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef
):
    pass


_ClientPutEventSelectorsEventSelectorsTypeDef = TypedDict(
    "_ClientPutEventSelectorsEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)


class ClientPutEventSelectorsEventSelectorsTypeDef(_ClientPutEventSelectorsEventSelectorsTypeDef):
    """
    - *(dict) --*

      Use event selectors to further specify the management and data event settings for your trail.
      By default, trails created without specific event selectors will be configured to log all read
      and write management events, and no data events. When an event occurs in your account,
      CloudTrail evaluates the event selector for all trails. For each trail, if the event matches
      any event selector, the trail processes and logs the event. If the event doesn't match any
      event selector, the trail doesn't log the event.
      You can configure up to five event selectors for a trail.
      - **ReadWriteType** *(string) --*

        Specify if you want your trail to log read-only events, write-only events, or all. For
        example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a
        write-only API operation.
        By default, the value is ``All`` .
    """


_ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef = TypedDict(
    "_ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)


class ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef(
    _ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef
):
    pass


_ClientPutEventSelectorsResponseEventSelectorsTypeDef = TypedDict(
    "_ClientPutEventSelectorsResponseEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)


class ClientPutEventSelectorsResponseEventSelectorsTypeDef(
    _ClientPutEventSelectorsResponseEventSelectorsTypeDef
):
    pass


_ClientPutEventSelectorsResponseTypeDef = TypedDict(
    "_ClientPutEventSelectorsResponseTypeDef",
    {"TrailARN": str, "EventSelectors": List[ClientPutEventSelectorsResponseEventSelectorsTypeDef]},
    total=False,
)


class ClientPutEventSelectorsResponseTypeDef(_ClientPutEventSelectorsResponseTypeDef):
    """
    - *(dict) --*

      - **TrailARN** *(string) --*

        Specifies the ARN of the trail that was updated with event selectors. The format of a trail
        ARN is:

          ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``
    """


_ClientPutInsightSelectorsInsightSelectorsTypeDef = TypedDict(
    "_ClientPutInsightSelectorsInsightSelectorsTypeDef", {"InsightType": str}, total=False
)


class ClientPutInsightSelectorsInsightSelectorsTypeDef(
    _ClientPutInsightSelectorsInsightSelectorsTypeDef
):
    """
    - *(dict) --*

      A JSON string that contains a list of insight types that are logged on a trail.
      - **InsightType** *(string) --*

        The type of insights to log on a trail. In this release, only ``ApiCallRateInsight`` is
        supported as an insight type.
    """


_ClientPutInsightSelectorsResponseInsightSelectorsTypeDef = TypedDict(
    "_ClientPutInsightSelectorsResponseInsightSelectorsTypeDef", {"InsightType": str}, total=False
)


class ClientPutInsightSelectorsResponseInsightSelectorsTypeDef(
    _ClientPutInsightSelectorsResponseInsightSelectorsTypeDef
):
    pass


_ClientPutInsightSelectorsResponseTypeDef = TypedDict(
    "_ClientPutInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[ClientPutInsightSelectorsResponseInsightSelectorsTypeDef],
    },
    total=False,
)


class ClientPutInsightSelectorsResponseTypeDef(_ClientPutInsightSelectorsResponseTypeDef):
    """
    - *(dict) --*

      - **TrailARN** *(string) --*

        The Amazon Resource Name (ARN) of a trail for which you want to change or add Insights
        selectors.
    """


_RequiredClientRemoveTagsTagsListTypeDef = TypedDict(
    "_RequiredClientRemoveTagsTagsListTypeDef", {"Key": str}
)
_OptionalClientRemoveTagsTagsListTypeDef = TypedDict(
    "_OptionalClientRemoveTagsTagsListTypeDef", {"Value": str}, total=False
)


class ClientRemoveTagsTagsListTypeDef(
    _RequiredClientRemoveTagsTagsListTypeDef, _OptionalClientRemoveTagsTagsListTypeDef
):
    """
    - *(dict) --*

      A custom key-value pair associated with a resource such as a CloudTrail trail.
      - **Key** *(string) --***[REQUIRED]**

        The key in a key-value pair. The key must be must be no longer than 128 Unicode characters.
        The key must be unique for the resource to which it applies.
    """


_ClientUpdateTrailResponseTypeDef = TypedDict(
    "_ClientUpdateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class ClientUpdateTrailResponseTypeDef(_ClientUpdateTrailResponseTypeDef):
    """
    - *(dict) --*

      Returns the objects or data listed below if successful. Otherwise, returns an error.
      - **Name** *(string) --*

        Specifies the name of the trail.
    """


_ListPublicKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPublicKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPublicKeysPaginatePaginationConfigTypeDef(_ListPublicKeysPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPublicKeysPaginateResponsePublicKeyListTypeDef = TypedDict(
    "_ListPublicKeysPaginateResponsePublicKeyListTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)


class ListPublicKeysPaginateResponsePublicKeyListTypeDef(
    _ListPublicKeysPaginateResponsePublicKeyListTypeDef
):
    pass


_ListPublicKeysPaginateResponseTypeDef = TypedDict(
    "_ListPublicKeysPaginateResponseTypeDef",
    {"PublicKeyList": List[ListPublicKeysPaginateResponsePublicKeyListTypeDef]},
    total=False,
)


class ListPublicKeysPaginateResponseTypeDef(_ListPublicKeysPaginateResponseTypeDef):
    """
    - *(dict) --*

      Returns the objects or data listed below if successful. Otherwise, returns an error.
      - **PublicKeyList** *(list) --*

        Contains an array of PublicKey objects.
        .. note::

          The returned public keys may have validity time ranges that overlap.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsPaginateResponseResourceTagListTagsListTypeDef = TypedDict(
    "_ListTagsPaginateResponseResourceTagListTagsListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsPaginateResponseResourceTagListTagsListTypeDef(
    _ListTagsPaginateResponseResourceTagListTagsListTypeDef
):
    pass


_ListTagsPaginateResponseResourceTagListTypeDef = TypedDict(
    "_ListTagsPaginateResponseResourceTagListTypeDef",
    {"ResourceId": str, "TagsList": List[ListTagsPaginateResponseResourceTagListTagsListTypeDef]},
    total=False,
)


class ListTagsPaginateResponseResourceTagListTypeDef(
    _ListTagsPaginateResponseResourceTagListTypeDef
):
    """
    - *(dict) --*

      A resource tag.
      - **ResourceId** *(string) --*

        Specifies the ARN of the resource.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"ResourceTagList": List[ListTagsPaginateResponseResourceTagListTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Returns the objects or data listed below if successful. Otherwise, returns an error.
      - **ResourceTagList** *(list) --*

        A list of resource tags.
        - *(dict) --*

          A resource tag.
          - **ResourceId** *(string) --*

            Specifies the ARN of the resource.
    """


_ListTrailsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTrailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTrailsPaginatePaginationConfigTypeDef(_ListTrailsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTrailsPaginateResponseTrailsTypeDef = TypedDict(
    "_ListTrailsPaginateResponseTrailsTypeDef",
    {"TrailARN": str, "Name": str, "HomeRegion": str},
    total=False,
)


class ListTrailsPaginateResponseTrailsTypeDef(_ListTrailsPaginateResponseTrailsTypeDef):
    """
    - *(dict) --*

      Information about a CloudTrail trail, including the trail's name, home region, and Amazon
      Resource Name (ARN).
      - **TrailARN** *(string) --*

        The ARN of a trail.
    """


_ListTrailsPaginateResponseTypeDef = TypedDict(
    "_ListTrailsPaginateResponseTypeDef",
    {"Trails": List[ListTrailsPaginateResponseTrailsTypeDef]},
    total=False,
)


class ListTrailsPaginateResponseTypeDef(_ListTrailsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Trails** *(list) --*

        Returns the name, ARN, and home region of trails in the current account.
        - *(dict) --*

          Information about a CloudTrail trail, including the trail's name, home region, and Amazon
          Resource Name (ARN).
          - **TrailARN** *(string) --*

            The ARN of a trail.
    """


_RequiredLookupEventsPaginateLookupAttributesTypeDef = TypedDict(
    "_RequiredLookupEventsPaginateLookupAttributesTypeDef",
    {
        "AttributeKey": Literal[
            "EventId",
            "EventName",
            "ReadOnly",
            "Username",
            "ResourceType",
            "ResourceName",
            "EventSource",
            "AccessKeyId",
        ]
    },
)
_OptionalLookupEventsPaginateLookupAttributesTypeDef = TypedDict(
    "_OptionalLookupEventsPaginateLookupAttributesTypeDef", {"AttributeValue": str}, total=False
)


class LookupEventsPaginateLookupAttributesTypeDef(
    _RequiredLookupEventsPaginateLookupAttributesTypeDef,
    _OptionalLookupEventsPaginateLookupAttributesTypeDef,
):
    """
    - *(dict) --*

      Specifies an attribute and value that filter the events returned.
      - **AttributeKey** *(string) --***[REQUIRED]**

        Specifies an attribute on which to filter the events returned.
    """


_LookupEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_LookupEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class LookupEventsPaginatePaginationConfigTypeDef(_LookupEventsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_LookupEventsPaginateResponseEventsResourcesTypeDef = TypedDict(
    "_LookupEventsPaginateResponseEventsResourcesTypeDef",
    {"ResourceType": str, "ResourceName": str},
    total=False,
)


class LookupEventsPaginateResponseEventsResourcesTypeDef(
    _LookupEventsPaginateResponseEventsResourcesTypeDef
):
    pass


_LookupEventsPaginateResponseEventsTypeDef = TypedDict(
    "_LookupEventsPaginateResponseEventsTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List[LookupEventsPaginateResponseEventsResourcesTypeDef],
        "CloudTrailEvent": str,
    },
    total=False,
)


class LookupEventsPaginateResponseEventsTypeDef(_LookupEventsPaginateResponseEventsTypeDef):
    """
    - *(dict) --*

      Contains information about an event that was returned by a lookup request. The result includes
      a representation of a CloudTrail event.
      - **EventId** *(string) --*

        The CloudTrail ID of the event returned.
    """


_LookupEventsPaginateResponseTypeDef = TypedDict(
    "_LookupEventsPaginateResponseTypeDef",
    {"Events": List[LookupEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class LookupEventsPaginateResponseTypeDef(_LookupEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains a response to a LookupEvents action.
      - **Events** *(list) --*

        A list of events returned based on the lookup attributes specified and the CloudTrail event.
        The events list is sorted by time. The most recent event is listed first.
        - *(dict) --*

          Contains information about an event that was returned by a lookup request. The result
          includes a representation of a CloudTrail event.
          - **EventId** *(string) --*

            The CloudTrail ID of the event returned.
    """
