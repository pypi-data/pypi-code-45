"Main interface for cloudtrail service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


_RequiredClientAddTagsTagsListTypeDef = TypedDict(
    "_RequiredClientAddTagsTagsListTypeDef", {"Key": str}
)
_OptionalClientAddTagsTagsListTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsListTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsListTypeDef(
    _RequiredClientAddTagsTagsListTypeDef, _OptionalClientAddTagsTagsListTypeDef
):
    pass


ClientCreateTrailResponseTypeDef = TypedDict(
    "ClientCreateTrailResponseTypeDef",
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

_RequiredClientCreateTrailTagsListTypeDef = TypedDict(
    "_RequiredClientCreateTrailTagsListTypeDef", {"Key": str}
)
_OptionalClientCreateTrailTagsListTypeDef = TypedDict(
    "_OptionalClientCreateTrailTagsListTypeDef", {"Value": str}, total=False
)


class ClientCreateTrailTagsListTypeDef(
    _RequiredClientCreateTrailTagsListTypeDef, _OptionalClientCreateTrailTagsListTypeDef
):
    pass


ClientDescribeTrailsResponsetrailListTypeDef = TypedDict(
    "ClientDescribeTrailsResponsetrailListTypeDef",
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

ClientDescribeTrailsResponseTypeDef = TypedDict(
    "ClientDescribeTrailsResponseTypeDef",
    {"trailList": List[ClientDescribeTrailsResponsetrailListTypeDef]},
    total=False,
)

ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef = TypedDict(
    "ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)

ClientGetEventSelectorsResponseEventSelectorsTypeDef = TypedDict(
    "ClientGetEventSelectorsResponseEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientGetEventSelectorsResponseEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

ClientGetEventSelectorsResponseTypeDef = TypedDict(
    "ClientGetEventSelectorsResponseTypeDef",
    {"TrailARN": str, "EventSelectors": List[ClientGetEventSelectorsResponseEventSelectorsTypeDef]},
    total=False,
)

ClientGetInsightSelectorsResponseInsightSelectorsTypeDef = TypedDict(
    "ClientGetInsightSelectorsResponseInsightSelectorsTypeDef", {"InsightType": str}, total=False
)

ClientGetInsightSelectorsResponseTypeDef = TypedDict(
    "ClientGetInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[ClientGetInsightSelectorsResponseInsightSelectorsTypeDef],
    },
    total=False,
)

ClientGetTrailResponseTrailTypeDef = TypedDict(
    "ClientGetTrailResponseTrailTypeDef",
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

ClientGetTrailResponseTypeDef = TypedDict(
    "ClientGetTrailResponseTypeDef", {"Trail": ClientGetTrailResponseTrailTypeDef}, total=False
)

ClientGetTrailStatusResponseTypeDef = TypedDict(
    "ClientGetTrailStatusResponseTypeDef",
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

ClientListPublicKeysResponsePublicKeyListTypeDef = TypedDict(
    "ClientListPublicKeysResponsePublicKeyListTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)

ClientListPublicKeysResponseTypeDef = TypedDict(
    "ClientListPublicKeysResponseTypeDef",
    {"PublicKeyList": List[ClientListPublicKeysResponsePublicKeyListTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsResponseResourceTagListTagsListTypeDef = TypedDict(
    "ClientListTagsResponseResourceTagListTagsListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseResourceTagListTypeDef = TypedDict(
    "ClientListTagsResponseResourceTagListTypeDef",
    {"ResourceId": str, "TagsList": List[ClientListTagsResponseResourceTagListTagsListTypeDef]},
    total=False,
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"ResourceTagList": List[ClientListTagsResponseResourceTagListTypeDef], "NextToken": str},
    total=False,
)

ClientListTrailsResponseTrailsTypeDef = TypedDict(
    "ClientListTrailsResponseTrailsTypeDef",
    {"TrailARN": str, "Name": str, "HomeRegion": str},
    total=False,
)

ClientListTrailsResponseTypeDef = TypedDict(
    "ClientListTrailsResponseTypeDef",
    {"Trails": List[ClientListTrailsResponseTrailsTypeDef], "NextToken": str},
    total=False,
)

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
    pass


ClientLookupEventsResponseEventsResourcesTypeDef = TypedDict(
    "ClientLookupEventsResponseEventsResourcesTypeDef",
    {"ResourceType": str, "ResourceName": str},
    total=False,
)

ClientLookupEventsResponseEventsTypeDef = TypedDict(
    "ClientLookupEventsResponseEventsTypeDef",
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

ClientLookupEventsResponseTypeDef = TypedDict(
    "ClientLookupEventsResponseTypeDef",
    {"Events": List[ClientLookupEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)

ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef = TypedDict(
    "ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)

ClientPutEventSelectorsEventSelectorsTypeDef = TypedDict(
    "ClientPutEventSelectorsEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientPutEventSelectorsEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef = TypedDict(
    "ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef",
    {"Type": str, "Values": List[str]},
    total=False,
)

ClientPutEventSelectorsResponseEventSelectorsTypeDef = TypedDict(
    "ClientPutEventSelectorsResponseEventSelectorsTypeDef",
    {
        "ReadWriteType": Literal["ReadOnly", "WriteOnly", "All"],
        "IncludeManagementEvents": bool,
        "DataResources": List[ClientPutEventSelectorsResponseEventSelectorsDataResourcesTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

ClientPutEventSelectorsResponseTypeDef = TypedDict(
    "ClientPutEventSelectorsResponseTypeDef",
    {"TrailARN": str, "EventSelectors": List[ClientPutEventSelectorsResponseEventSelectorsTypeDef]},
    total=False,
)

ClientPutInsightSelectorsInsightSelectorsTypeDef = TypedDict(
    "ClientPutInsightSelectorsInsightSelectorsTypeDef", {"InsightType": str}, total=False
)

ClientPutInsightSelectorsResponseInsightSelectorsTypeDef = TypedDict(
    "ClientPutInsightSelectorsResponseInsightSelectorsTypeDef", {"InsightType": str}, total=False
)

ClientPutInsightSelectorsResponseTypeDef = TypedDict(
    "ClientPutInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[ClientPutInsightSelectorsResponseInsightSelectorsTypeDef],
    },
    total=False,
)

_RequiredClientRemoveTagsTagsListTypeDef = TypedDict(
    "_RequiredClientRemoveTagsTagsListTypeDef", {"Key": str}
)
_OptionalClientRemoveTagsTagsListTypeDef = TypedDict(
    "_OptionalClientRemoveTagsTagsListTypeDef", {"Value": str}, total=False
)


class ClientRemoveTagsTagsListTypeDef(
    _RequiredClientRemoveTagsTagsListTypeDef, _OptionalClientRemoveTagsTagsListTypeDef
):
    pass


ClientUpdateTrailResponseTypeDef = TypedDict(
    "ClientUpdateTrailResponseTypeDef",
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

ListPublicKeysPaginatePaginationConfigTypeDef = TypedDict(
    "ListPublicKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListPublicKeysPaginateResponsePublicKeyListTypeDef = TypedDict(
    "ListPublicKeysPaginateResponsePublicKeyListTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)

ListPublicKeysPaginateResponseTypeDef = TypedDict(
    "ListPublicKeysPaginateResponseTypeDef",
    {"PublicKeyList": List[ListPublicKeysPaginateResponsePublicKeyListTypeDef]},
    total=False,
)

ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "ListTagsPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)

ListTagsPaginateResponseResourceTagListTagsListTypeDef = TypedDict(
    "ListTagsPaginateResponseResourceTagListTagsListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ListTagsPaginateResponseResourceTagListTypeDef = TypedDict(
    "ListTagsPaginateResponseResourceTagListTypeDef",
    {"ResourceId": str, "TagsList": List[ListTagsPaginateResponseResourceTagListTagsListTypeDef]},
    total=False,
)

ListTagsPaginateResponseTypeDef = TypedDict(
    "ListTagsPaginateResponseTypeDef",
    {"ResourceTagList": List[ListTagsPaginateResponseResourceTagListTypeDef]},
    total=False,
)

ListTrailsPaginatePaginationConfigTypeDef = TypedDict(
    "ListTrailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListTrailsPaginateResponseTrailsTypeDef = TypedDict(
    "ListTrailsPaginateResponseTrailsTypeDef",
    {"TrailARN": str, "Name": str, "HomeRegion": str},
    total=False,
)

ListTrailsPaginateResponseTypeDef = TypedDict(
    "ListTrailsPaginateResponseTypeDef",
    {"Trails": List[ListTrailsPaginateResponseTrailsTypeDef]},
    total=False,
)

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
    pass


LookupEventsPaginatePaginationConfigTypeDef = TypedDict(
    "LookupEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

LookupEventsPaginateResponseEventsResourcesTypeDef = TypedDict(
    "LookupEventsPaginateResponseEventsResourcesTypeDef",
    {"ResourceType": str, "ResourceName": str},
    total=False,
)

LookupEventsPaginateResponseEventsTypeDef = TypedDict(
    "LookupEventsPaginateResponseEventsTypeDef",
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

LookupEventsPaginateResponseTypeDef = TypedDict(
    "LookupEventsPaginateResponseTypeDef",
    {"Events": List[LookupEventsPaginateResponseEventsTypeDef]},
    total=False,
)
