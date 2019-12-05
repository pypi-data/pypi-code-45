"Main interface for s3 service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from botocore.eventstream import EventStream
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


BucketAclPutAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "BucketAclPutAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

BucketAclPutAccessControlPolicyGrantsTypeDef = TypedDict(
    "BucketAclPutAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": BucketAclPutAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

BucketAclPutAccessControlPolicyOwnerTypeDef = TypedDict(
    "BucketAclPutAccessControlPolicyOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

BucketAclPutAccessControlPolicyTypeDef = TypedDict(
    "BucketAclPutAccessControlPolicyTypeDef",
    {
        "Grants": List[BucketAclPutAccessControlPolicyGrantsTypeDef],
        "Owner": BucketAclPutAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)

BucketCorsPutCORSConfigurationCORSRulesTypeDef = TypedDict(
    "BucketCorsPutCORSConfigurationCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)

BucketCorsPutCORSConfigurationTypeDef = TypedDict(
    "BucketCorsPutCORSConfigurationTypeDef",
    {"CORSRules": List[BucketCorsPutCORSConfigurationCORSRulesTypeDef]},
)

BucketCreateCreateBucketConfigurationTypeDef = TypedDict(
    "BucketCreateCreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": Literal[
            "EU",
            "eu-west-1",
            "us-west-1",
            "us-west-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "cn-north-1",
            "eu-central-1",
        ]
    },
    total=False,
)

BucketCreateResponseTypeDef = TypedDict(
    "BucketCreateResponseTypeDef", {"Location": str}, total=False
)

_RequiredBucketDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_RequiredBucketDeleteObjectsDeleteObjectsTypeDef", {"Key": str}
)
_OptionalBucketDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_OptionalBucketDeleteObjectsDeleteObjectsTypeDef", {"VersionId": str}, total=False
)


class BucketDeleteObjectsDeleteObjectsTypeDef(
    _RequiredBucketDeleteObjectsDeleteObjectsTypeDef,
    _OptionalBucketDeleteObjectsDeleteObjectsTypeDef,
):
    pass


_RequiredBucketDeleteObjectsDeleteTypeDef = TypedDict(
    "_RequiredBucketDeleteObjectsDeleteTypeDef",
    {"Objects": List[BucketDeleteObjectsDeleteObjectsTypeDef]},
)
_OptionalBucketDeleteObjectsDeleteTypeDef = TypedDict(
    "_OptionalBucketDeleteObjectsDeleteTypeDef", {"Quiet": bool}, total=False
)


class BucketDeleteObjectsDeleteTypeDef(
    _RequiredBucketDeleteObjectsDeleteTypeDef, _OptionalBucketDeleteObjectsDeleteTypeDef
):
    pass


BucketDeleteObjectsResponseDeletedTypeDef = TypedDict(
    "BucketDeleteObjectsResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)

BucketDeleteObjectsResponseErrorsTypeDef = TypedDict(
    "BucketDeleteObjectsResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)

BucketDeleteObjectsResponseTypeDef = TypedDict(
    "BucketDeleteObjectsResponseTypeDef",
    {
        "Deleted": List[BucketDeleteObjectsResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[BucketDeleteObjectsResponseErrorsTypeDef],
    },
    total=False,
)

BucketExistsWaitWaiterConfigTypeDef = TypedDict(
    "BucketExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef,
        "And": BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesTransitionsTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesTransitionsTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef",
    {
        "Expiration": BucketLifecycleConfigurationPutLifecycleConfigurationRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Filter": BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "Transitions": List[
            BucketLifecycleConfigurationPutLifecycleConfigurationRulesTransitionsTypeDef
        ],
        "NoncurrentVersionTransitions": List[
            BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef
        ],
        "NoncurrentVersionExpiration": BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": BucketLifecycleConfigurationPutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

BucketLifecycleConfigurationPutLifecycleConfigurationTypeDef = TypedDict(
    "BucketLifecycleConfigurationPutLifecycleConfigurationTypeDef",
    {"Rules": List[BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef]},
)

BucketLifecyclePutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "BucketLifecyclePutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

BucketLifecyclePutLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "BucketLifecyclePutLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

BucketLifecyclePutLifecycleConfigurationRulesTransitionTypeDef = TypedDict(
    "BucketLifecyclePutLifecycleConfigurationRulesTransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

BucketLifecyclePutLifecycleConfigurationRulesTypeDef = TypedDict(
    "BucketLifecyclePutLifecycleConfigurationRulesTypeDef",
    {
        "Expiration": BucketLifecyclePutLifecycleConfigurationRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Status": Literal["Enabled", "Disabled"],
        "Transition": BucketLifecyclePutLifecycleConfigurationRulesTransitionTypeDef,
        "NoncurrentVersionTransition": BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef,
        "NoncurrentVersionExpiration": BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": BucketLifecyclePutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

BucketLifecyclePutLifecycleConfigurationTypeDef = TypedDict(
    "BucketLifecyclePutLifecycleConfigurationTypeDef",
    {"Rules": List[BucketLifecyclePutLifecycleConfigurationRulesTypeDef]},
)

BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE"],
    },
    total=False,
)

_RequiredBucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef = TypedDict(
    "_RequiredBucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef", {"TargetBucket": str}
)
_OptionalBucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef = TypedDict(
    "_OptionalBucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef",
    {
        "TargetGrants": List[BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef],
        "TargetPrefix": str,
    },
    total=False,
)


class BucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef(
    _RequiredBucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef,
    _OptionalBucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef,
):
    pass


BucketLoggingPutBucketLoggingStatusTypeDef = TypedDict(
    "BucketLoggingPutBucketLoggingStatusTypeDef",
    {"LoggingEnabled": BucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef},
    total=False,
)

BucketNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "BucketNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)

BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsTypeDef",
    {
        "Id": str,
        "LambdaFunctionArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef,
    },
    total=False,
)

BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterTypeDef",
    {"Key": BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef},
    total=False,
)

BucketNotificationPutNotificationConfigurationQueueConfigurationsTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationQueueConfigurationsTypeDef",
    {
        "Id": str,
        "QueueArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterTypeDef,
    },
    total=False,
)

BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterTypeDef",
    {"Key": BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef},
    total=False,
)

BucketNotificationPutNotificationConfigurationTopicConfigurationsTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationTopicConfigurationsTypeDef",
    {
        "Id": str,
        "TopicArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterTypeDef,
    },
    total=False,
)

BucketNotificationPutNotificationConfigurationTypeDef = TypedDict(
    "BucketNotificationPutNotificationConfigurationTypeDef",
    {
        "TopicConfigurations": List[
            BucketNotificationPutNotificationConfigurationTopicConfigurationsTypeDef
        ],
        "QueueConfigurations": List[
            BucketNotificationPutNotificationConfigurationQueueConfigurationsTypeDef
        ],
        "LambdaFunctionConfigurations": List[
            BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsTypeDef
        ],
    },
    total=False,
)

BucketRequestPaymentPutRequestPaymentConfigurationTypeDef = TypedDict(
    "BucketRequestPaymentPutRequestPaymentConfigurationTypeDef",
    {"Payer": Literal["Requester", "BucketOwner"]},
)

_RequiredBucketTaggingPutTaggingTagSetTypeDef = TypedDict(
    "_RequiredBucketTaggingPutTaggingTagSetTypeDef", {"Key": str}
)
_OptionalBucketTaggingPutTaggingTagSetTypeDef = TypedDict(
    "_OptionalBucketTaggingPutTaggingTagSetTypeDef", {"Value": str}, total=False
)


class BucketTaggingPutTaggingTagSetTypeDef(
    _RequiredBucketTaggingPutTaggingTagSetTypeDef, _OptionalBucketTaggingPutTaggingTagSetTypeDef
):
    pass


BucketTaggingPutTaggingTypeDef = TypedDict(
    "BucketTaggingPutTaggingTypeDef", {"TagSet": List[BucketTaggingPutTaggingTagSetTypeDef]}
)

BucketVersioningPutVersioningConfigurationTypeDef = TypedDict(
    "BucketVersioningPutVersioningConfigurationTypeDef",
    {"MFADelete": Literal["Enabled", "Disabled"], "Status": Literal["Enabled", "Suspended"]},
    total=False,
)

BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef = TypedDict(
    "BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef", {"Key": str}
)

BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef = TypedDict(
    "BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef", {"Suffix": str}, total=False
)

BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef = TypedDict(
    "BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": Literal["http", "https"]},
    total=False,
)

BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef = TypedDict(
    "BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)

BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef = TypedDict(
    "BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef = TypedDict(
    "BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef",
    {
        "Condition": BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef,
        "Redirect": BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef,
    },
    total=False,
)

BucketWebsitePutWebsiteConfigurationTypeDef = TypedDict(
    "BucketWebsitePutWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef,
        "IndexDocument": BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef,
        "RedirectAllRequestsTo": BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef,
        "RoutingRules": List[BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef],
    },
    total=False,
)

ClientAbortMultipartUploadResponseTypeDef = TypedDict(
    "ClientAbortMultipartUploadResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientCompleteMultipartUploadMultipartUploadPartsTypeDef = TypedDict(
    "ClientCompleteMultipartUploadMultipartUploadPartsTypeDef",
    {"ETag": str, "PartNumber": int},
    total=False,
)

ClientCompleteMultipartUploadMultipartUploadTypeDef = TypedDict(
    "ClientCompleteMultipartUploadMultipartUploadTypeDef",
    {"Parts": List[ClientCompleteMultipartUploadMultipartUploadPartsTypeDef]},
    total=False,
)

ClientCompleteMultipartUploadResponseTypeDef = TypedDict(
    "ClientCompleteMultipartUploadResponseTypeDef",
    {
        "Location": str,
        "Bucket": str,
        "Key": str,
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "VersionId": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientCopyObjectCopySource1TypeDef = TypedDict(
    "ClientCopyObjectCopySource1TypeDef", {"Bucket": str, "Key": str, "VersionId": str}, total=False
)

ClientCopyObjectResponseCopyObjectResultTypeDef = TypedDict(
    "ClientCopyObjectResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)

ClientCopyObjectResponseTypeDef = TypedDict(
    "ClientCopyObjectResponseTypeDef",
    {
        "CopyObjectResult": ClientCopyObjectResponseCopyObjectResultTypeDef,
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientCreateBucketCreateBucketConfigurationTypeDef = TypedDict(
    "ClientCreateBucketCreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": Literal[
            "EU",
            "eu-west-1",
            "us-west-1",
            "us-west-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "cn-north-1",
            "eu-central-1",
        ]
    },
    total=False,
)

ClientCreateBucketResponseTypeDef = TypedDict(
    "ClientCreateBucketResponseTypeDef", {"Location": str}, total=False
)

ClientCreateMultipartUploadResponseTypeDef = TypedDict(
    "ClientCreateMultipartUploadResponseTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientDeleteObjectResponseTypeDef = TypedDict(
    "ClientDeleteObjectResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)

ClientDeleteObjectTaggingResponseTypeDef = TypedDict(
    "ClientDeleteObjectTaggingResponseTypeDef", {"VersionId": str}, total=False
)

_RequiredClientDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_RequiredClientDeleteObjectsDeleteObjectsTypeDef", {"Key": str}
)
_OptionalClientDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_OptionalClientDeleteObjectsDeleteObjectsTypeDef", {"VersionId": str}, total=False
)


class ClientDeleteObjectsDeleteObjectsTypeDef(
    _RequiredClientDeleteObjectsDeleteObjectsTypeDef,
    _OptionalClientDeleteObjectsDeleteObjectsTypeDef,
):
    pass


_RequiredClientDeleteObjectsDeleteTypeDef = TypedDict(
    "_RequiredClientDeleteObjectsDeleteTypeDef",
    {"Objects": List[ClientDeleteObjectsDeleteObjectsTypeDef]},
)
_OptionalClientDeleteObjectsDeleteTypeDef = TypedDict(
    "_OptionalClientDeleteObjectsDeleteTypeDef", {"Quiet": bool}, total=False
)


class ClientDeleteObjectsDeleteTypeDef(
    _RequiredClientDeleteObjectsDeleteTypeDef, _OptionalClientDeleteObjectsDeleteTypeDef
):
    pass


ClientDeleteObjectsResponseDeletedTypeDef = TypedDict(
    "ClientDeleteObjectsResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)

ClientDeleteObjectsResponseErrorsTypeDef = TypedDict(
    "ClientDeleteObjectsResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)

ClientDeleteObjectsResponseTypeDef = TypedDict(
    "ClientDeleteObjectsResponseTypeDef",
    {
        "Deleted": List[ClientDeleteObjectsResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ClientDeleteObjectsResponseErrorsTypeDef],
    },
    total=False,
)

ClientGetBucketAccelerateConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketAccelerateConfigurationResponseTypeDef",
    {"Status": Literal["Enabled", "Suspended"]},
    total=False,
)

ClientGetBucketAclResponseGrantsGranteeTypeDef = TypedDict(
    "ClientGetBucketAclResponseGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientGetBucketAclResponseGrantsTypeDef = TypedDict(
    "ClientGetBucketAclResponseGrantsTypeDef",
    {
        "Grantee": ClientGetBucketAclResponseGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientGetBucketAclResponseOwnerTypeDef = TypedDict(
    "ClientGetBucketAclResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientGetBucketAclResponseTypeDef = TypedDict(
    "ClientGetBucketAclResponseTypeDef",
    {
        "Owner": ClientGetBucketAclResponseOwnerTypeDef,
        "Grants": List[ClientGetBucketAclResponseGrantsTypeDef],
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef,
        "And": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef,
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef,
        "StorageClassAnalysis": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef,
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseTypeDef",
    {
        "AnalyticsConfiguration": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef
    },
    total=False,
)

ClientGetBucketCorsResponseCORSRulesTypeDef = TypedDict(
    "ClientGetBucketCorsResponseCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)

ClientGetBucketCorsResponseTypeDef = TypedDict(
    "ClientGetBucketCorsResponseTypeDef",
    {"CORSRules": List[ClientGetBucketCorsResponseCORSRulesTypeDef]},
    total=False,
)

ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef = TypedDict(
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    {"SSEAlgorithm": Literal["AES256", "aws:kms"], "KMSMasterKeyID": str},
    total=False,
)

ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef = TypedDict(
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
    },
    total=False,
)

ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef",
    {"Rules": List[ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef]},
    total=False,
)

ClientGetBucketEncryptionResponseTypeDef = TypedDict(
    "ClientGetBucketEncryptionResponseTypeDef",
    {
        "ServerSideEncryptionConfiguration": ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef",
    {
        "S3BucketDestination": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef",
    {"Prefix": str},
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef",
    {
        "Destination": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef,
        "IsEnabled": bool,
        "Filter": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef,
        "Id": str,
        "IncludedObjectVersions": Literal["All", "Current"],
        "OptionalFields": List[
            Literal[
                "Size",
                "LastModifiedDate",
                "StorageClass",
                "ETag",
                "IsMultipartUploaded",
                "ReplicationStatus",
                "EncryptionStatus",
                "ObjectLockRetainUntilDate",
                "ObjectLockMode",
                "ObjectLockLegalHoldStatus",
                "IntelligentTieringAccessTier",
            ]
        ],
        "Schedule": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef,
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseTypeDef",
    {
        "InventoryConfiguration": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef],
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef,
        "And": ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef,
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesTypeDef",
    {
        "Expiration": ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Filter": ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "Transitions": List[ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef],
        "NoncurrentVersionTransitions": List[
            ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef
        ],
        "NoncurrentVersionExpiration": ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseTypeDef",
    {"Rules": List[ClientGetBucketLifecycleConfigurationResponseRulesTypeDef]},
    total=False,
)

ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

ClientGetBucketLifecycleResponseRulesExpirationTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientGetBucketLifecycleResponseRulesTransitionTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesTransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientGetBucketLifecycleResponseRulesTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesTypeDef",
    {
        "Expiration": ClientGetBucketLifecycleResponseRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Status": Literal["Enabled", "Disabled"],
        "Transition": ClientGetBucketLifecycleResponseRulesTransitionTypeDef,
        "NoncurrentVersionTransition": ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef,
        "NoncurrentVersionExpiration": ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

ClientGetBucketLifecycleResponseTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseTypeDef",
    {"Rules": List[ClientGetBucketLifecycleResponseRulesTypeDef]},
    total=False,
)

ClientGetBucketLocationResponseTypeDef = TypedDict(
    "ClientGetBucketLocationResponseTypeDef",
    {
        "LocationConstraint": Literal[
            "EU",
            "eu-west-1",
            "us-west-1",
            "us-west-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "cn-north-1",
            "eu-central-1",
        ]
    },
    total=False,
)

ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE"],
    },
    total=False,
)

ClientGetBucketLoggingResponseLoggingEnabledTypeDef = TypedDict(
    "ClientGetBucketLoggingResponseLoggingEnabledTypeDef",
    {
        "TargetBucket": str,
        "TargetGrants": List[ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef],
        "TargetPrefix": str,
    },
    total=False,
)

ClientGetBucketLoggingResponseTypeDef = TypedDict(
    "ClientGetBucketLoggingResponseTypeDef",
    {"LoggingEnabled": ClientGetBucketLoggingResponseLoggingEnabledTypeDef},
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef,
        "And": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef,
    },
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef,
    },
    total=False,
)

ClientGetBucketMetricsConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseTypeDef",
    {
        "MetricsConfiguration": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef",
    {
        "Id": str,
        "LambdaFunctionArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef",
    {"Key": ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef",
    {
        "Id": str,
        "QueueArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef",
    {"Key": ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef",
    {
        "Id": str,
        "TopicArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTypeDef",
    {
        "TopicConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef
        ],
        "QueueConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef
        ],
        "LambdaFunctionConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef = TypedDict(
    "ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "CloudFunction": str,
        "InvocationRole": str,
    },
    total=False,
)

ClientGetBucketNotificationResponseQueueConfigurationTypeDef = TypedDict(
    "ClientGetBucketNotificationResponseQueueConfigurationTypeDef",
    {
        "Id": str,
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Queue": str,
    },
    total=False,
)

ClientGetBucketNotificationResponseTopicConfigurationTypeDef = TypedDict(
    "ClientGetBucketNotificationResponseTopicConfigurationTypeDef",
    {
        "Id": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Topic": str,
    },
    total=False,
)

ClientGetBucketNotificationResponseTypeDef = TypedDict(
    "ClientGetBucketNotificationResponseTypeDef",
    {
        "TopicConfiguration": ClientGetBucketNotificationResponseTopicConfigurationTypeDef,
        "QueueConfiguration": ClientGetBucketNotificationResponseQueueConfigurationTypeDef,
        "CloudFunctionConfiguration": ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef,
    },
    total=False,
)

ClientGetBucketPolicyResponseTypeDef = TypedDict(
    "ClientGetBucketPolicyResponseTypeDef", {"Policy": str}, total=False
)

ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef = TypedDict(
    "ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef", {"IsPublic": bool}, total=False
)

ClientGetBucketPolicyStatusResponseTypeDef = TypedDict(
    "ClientGetBucketPolicyStatusResponseTypeDef",
    {"PolicyStatus": ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    {"Owner": str},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    {"ReplicaKmsKeyID": str},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    {"Minutes": int},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "EventThreshold": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    {"Minutes": int},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "Time": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef",
    {
        "Bucket": str,
        "Account": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "AccessControlTranslation": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef,
        "EncryptionConfiguration": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef,
        "ReplicationTime": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef,
        "Metrics": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef,
        "And": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "SourceSelectionCriteria": ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef,
        "ExistingObjectReplication": ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef,
        "Destination": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef,
        "DeleteMarkerReplication": ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": List[ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef],
    },
    total=False,
)

ClientGetBucketReplicationResponseTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseTypeDef",
    {"ReplicationConfiguration": ClientGetBucketReplicationResponseReplicationConfigurationTypeDef},
    total=False,
)

ClientGetBucketRequestPaymentResponseTypeDef = TypedDict(
    "ClientGetBucketRequestPaymentResponseTypeDef",
    {"Payer": Literal["Requester", "BucketOwner"]},
    total=False,
)

ClientGetBucketTaggingResponseTagSetTypeDef = TypedDict(
    "ClientGetBucketTaggingResponseTagSetTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetBucketTaggingResponseTypeDef = TypedDict(
    "ClientGetBucketTaggingResponseTypeDef",
    {"TagSet": List[ClientGetBucketTaggingResponseTagSetTypeDef]},
    total=False,
)

ClientGetBucketVersioningResponseTypeDef = TypedDict(
    "ClientGetBucketVersioningResponseTypeDef",
    {"Status": Literal["Enabled", "Suspended"], "MFADelete": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientGetBucketWebsiteResponseErrorDocumentTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseErrorDocumentTypeDef", {"Key": str}, total=False
)

ClientGetBucketWebsiteResponseIndexDocumentTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseIndexDocumentTypeDef", {"Suffix": str}, total=False
)

ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": Literal["http", "https"]},
    total=False,
)

ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)

ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

ClientGetBucketWebsiteResponseRoutingRulesTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseRoutingRulesTypeDef",
    {
        "Condition": ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef,
        "Redirect": ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef,
    },
    total=False,
)

ClientGetBucketWebsiteResponseTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseTypeDef",
    {
        "RedirectAllRequestsTo": ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef,
        "IndexDocument": ClientGetBucketWebsiteResponseIndexDocumentTypeDef,
        "ErrorDocument": ClientGetBucketWebsiteResponseErrorDocumentTypeDef,
        "RoutingRules": List[ClientGetBucketWebsiteResponseRoutingRulesTypeDef],
    },
    total=False,
)

ClientGetObjectAclResponseGrantsGranteeTypeDef = TypedDict(
    "ClientGetObjectAclResponseGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientGetObjectAclResponseGrantsTypeDef = TypedDict(
    "ClientGetObjectAclResponseGrantsTypeDef",
    {
        "Grantee": ClientGetObjectAclResponseGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientGetObjectAclResponseOwnerTypeDef = TypedDict(
    "ClientGetObjectAclResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientGetObjectAclResponseTypeDef = TypedDict(
    "ClientGetObjectAclResponseTypeDef",
    {
        "Owner": ClientGetObjectAclResponseOwnerTypeDef,
        "Grants": List[ClientGetObjectAclResponseGrantsTypeDef],
        "RequestCharged": str,
    },
    total=False,
)

ClientGetObjectLegalHoldResponseLegalHoldTypeDef = TypedDict(
    "ClientGetObjectLegalHoldResponseLegalHoldTypeDef",
    {"Status": Literal["ON", "OFF"]},
    total=False,
)

ClientGetObjectLegalHoldResponseTypeDef = TypedDict(
    "ClientGetObjectLegalHoldResponseTypeDef",
    {"LegalHold": ClientGetObjectLegalHoldResponseLegalHoldTypeDef},
    total=False,
)

ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef = TypedDict(
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "Days": int, "Years": int},
    total=False,
)

ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef = TypedDict(
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef",
    {
        "DefaultRetention": ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef
    },
    total=False,
)

ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef = TypedDict(
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef,
    },
    total=False,
)

ClientGetObjectLockConfigurationResponseTypeDef = TypedDict(
    "ClientGetObjectLockConfigurationResponseTypeDef",
    {
        "ObjectLockConfiguration": ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef
    },
    total=False,
)

ClientGetObjectResponseTypeDef = TypedDict(
    "ClientGetObjectResponseTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

ClientGetObjectRetentionResponseRetentionTypeDef = TypedDict(
    "ClientGetObjectRetentionResponseRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "RetainUntilDate": datetime},
    total=False,
)

ClientGetObjectRetentionResponseTypeDef = TypedDict(
    "ClientGetObjectRetentionResponseTypeDef",
    {"Retention": ClientGetObjectRetentionResponseRetentionTypeDef},
    total=False,
)

ClientGetObjectTaggingResponseTagSetTypeDef = TypedDict(
    "ClientGetObjectTaggingResponseTagSetTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetObjectTaggingResponseTypeDef = TypedDict(
    "ClientGetObjectTaggingResponseTypeDef",
    {"VersionId": str, "TagSet": List[ClientGetObjectTaggingResponseTagSetTypeDef]},
    total=False,
)

ClientGetObjectTorrentResponseTypeDef = TypedDict(
    "ClientGetObjectTorrentResponseTypeDef",
    {"Body": StreamingBody, "RequestCharged": str},
    total=False,
)

ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef = TypedDict(
    "ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

ClientGetPublicAccessBlockResponseTypeDef = TypedDict(
    "ClientGetPublicAccessBlockResponseTypeDef",
    {
        "PublicAccessBlockConfiguration": ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
    },
    total=False,
)

ClientHeadObjectResponseTypeDef = TypedDict(
    "ClientHeadObjectResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef,
        "And": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef,
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef",
    {
        "Id": str,
        "Filter": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef,
        "StorageClassAnalysis": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef,
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "AnalyticsConfigurationList": List[
            ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef
        ],
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef",
    {
        "S3BucketDestination": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef",
    {"Prefix": str},
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef",
    {
        "Destination": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef,
        "IsEnabled": bool,
        "Filter": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef,
        "Id": str,
        "IncludedObjectVersions": Literal["All", "Current"],
        "OptionalFields": List[
            Literal[
                "Size",
                "LastModifiedDate",
                "StorageClass",
                "ETag",
                "IsMultipartUploaded",
                "ReplicationStatus",
                "EncryptionStatus",
                "ObjectLockRetainUntilDate",
                "ObjectLockMode",
                "ObjectLockLegalHoldStatus",
                "IntelligentTieringAccessTier",
            ]
        ],
        "Schedule": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef,
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseTypeDef",
    {
        "ContinuationToken": str,
        "InventoryConfigurationList": List[
            ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef
        ],
        "IsTruncated": bool,
        "NextContinuationToken": str,
    },
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef,
        "And": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef,
    },
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef",
    {
        "Id": str,
        "Filter": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef,
    },
    total=False,
)

ClientListBucketMetricsConfigurationsResponseTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "MetricsConfigurationList": List[
            ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef
        ],
    },
    total=False,
)

ClientListBucketsResponseBucketsTypeDef = TypedDict(
    "ClientListBucketsResponseBucketsTypeDef", {"Name": str, "CreationDate": datetime}, total=False
)

ClientListBucketsResponseOwnerTypeDef = TypedDict(
    "ClientListBucketsResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientListBucketsResponseTypeDef = TypedDict(
    "ClientListBucketsResponseTypeDef",
    {
        "Buckets": List[ClientListBucketsResponseBucketsTypeDef],
        "Owner": ClientListBucketsResponseOwnerTypeDef,
    },
    total=False,
)

ClientListMultipartUploadsResponseCommonPrefixesTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ClientListMultipartUploadsResponseUploadsInitiatorTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseUploadsInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)

ClientListMultipartUploadsResponseUploadsOwnerTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseUploadsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientListMultipartUploadsResponseUploadsTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseUploadsTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "Owner": ClientListMultipartUploadsResponseUploadsOwnerTypeDef,
        "Initiator": ClientListMultipartUploadsResponseUploadsInitiatorTypeDef,
    },
    total=False,
)

ClientListMultipartUploadsResponseTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "NextKeyMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "NextUploadIdMarker": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List[ClientListMultipartUploadsResponseUploadsTypeDef],
        "CommonPrefixes": List[ClientListMultipartUploadsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)

ClientListObjectVersionsResponseCommonPrefixesTypeDef = TypedDict(
    "ClientListObjectVersionsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef = TypedDict(
    "ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientListObjectVersionsResponseDeleteMarkersTypeDef = TypedDict(
    "ClientListObjectVersionsResponseDeleteMarkersTypeDef",
    {
        "Owner": ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)

ClientListObjectVersionsResponseVersionsOwnerTypeDef = TypedDict(
    "ClientListObjectVersionsResponseVersionsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientListObjectVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListObjectVersionsResponseVersionsTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": ClientListObjectVersionsResponseVersionsOwnerTypeDef,
    },
    total=False,
)

ClientListObjectVersionsResponseTypeDef = TypedDict(
    "ClientListObjectVersionsResponseTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "NextKeyMarker": str,
        "NextVersionIdMarker": str,
        "Versions": List[ClientListObjectVersionsResponseVersionsTypeDef],
        "DeleteMarkers": List[ClientListObjectVersionsResponseDeleteMarkersTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectVersionsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)

ClientListObjectsResponseCommonPrefixesTypeDef = TypedDict(
    "ClientListObjectsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ClientListObjectsResponseContentsOwnerTypeDef = TypedDict(
    "ClientListObjectsResponseContentsOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientListObjectsResponseContentsTypeDef = TypedDict(
    "ClientListObjectsResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "Owner": ClientListObjectsResponseContentsOwnerTypeDef,
    },
    total=False,
)

ClientListObjectsResponseTypeDef = TypedDict(
    "ClientListObjectsResponseTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List[ClientListObjectsResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)

ClientListObjectsV2ResponseCommonPrefixesTypeDef = TypedDict(
    "ClientListObjectsV2ResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ClientListObjectsV2ResponseContentsOwnerTypeDef = TypedDict(
    "ClientListObjectsV2ResponseContentsOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientListObjectsV2ResponseContentsTypeDef = TypedDict(
    "ClientListObjectsV2ResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "Owner": ClientListObjectsV2ResponseContentsOwnerTypeDef,
    },
    total=False,
)

ClientListObjectsV2ResponseTypeDef = TypedDict(
    "ClientListObjectsV2ResponseTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List[ClientListObjectsV2ResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectsV2ResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "KeyCount": int,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "StartAfter": str,
    },
    total=False,
)

ClientListPartsResponseInitiatorTypeDef = TypedDict(
    "ClientListPartsResponseInitiatorTypeDef", {"ID": str, "DisplayName": str}, total=False
)

ClientListPartsResponseOwnerTypeDef = TypedDict(
    "ClientListPartsResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientListPartsResponsePartsTypeDef = TypedDict(
    "ClientListPartsResponsePartsTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)

ClientListPartsResponseTypeDef = TypedDict(
    "ClientListPartsResponseTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "NextPartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List[ClientListPartsResponsePartsTypeDef],
        "Initiator": ClientListPartsResponseInitiatorTypeDef,
        "Owner": ClientListPartsResponseOwnerTypeDef,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
    },
    total=False,
)

ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef = TypedDict(
    "ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef",
    {"Status": Literal["Enabled", "Suspended"]},
    total=False,
)

ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientPutBucketAclAccessControlPolicyGrantsTypeDef = TypedDict(
    "ClientPutBucketAclAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientPutBucketAclAccessControlPolicyOwnerTypeDef = TypedDict(
    "ClientPutBucketAclAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientPutBucketAclAccessControlPolicyTypeDef = TypedDict(
    "ClientPutBucketAclAccessControlPolicyTypeDef",
    {
        "Grants": List[ClientPutBucketAclAccessControlPolicyGrantsTypeDef],
        "Owner": ClientPutBucketAclAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef,
        "And": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef,
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)

_RequiredClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef", {"Id": str}
)
_OptionalClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef",
    {
        "Filter": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef,
        "StorageClassAnalysis": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef,
    },
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef(
    _RequiredClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef,
    _OptionalClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef,
):
    pass


ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef = TypedDict(
    "ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)

ClientPutBucketCorsCORSConfigurationTypeDef = TypedDict(
    "ClientPutBucketCorsCORSConfigurationTypeDef",
    {"CORSRules": List[ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef]},
)

_RequiredClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_RequiredClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    {"SSEAlgorithm": Literal["AES256", "aws:kms"]},
)
_OptionalClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_OptionalClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    {"KMSMasterKeyID": str},
    total=False,
)


class ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef(
    _RequiredClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef,
    _OptionalClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef,
):
    pass


ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef = TypedDict(
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
    },
    total=False,
)

ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef",
    {"Rules": List[ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef]},
)

ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)

ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)

ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)

ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef",
    {
        "S3BucketDestination": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef
    },
)

ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef",
    {"Prefix": str},
    total=False,
)

ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)

_RequiredClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef",
    {"Destination": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef},
)
_OptionalClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef",
    {
        "IsEnabled": bool,
        "Filter": ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef,
        "Id": str,
        "IncludedObjectVersions": Literal["All", "Current"],
        "OptionalFields": List[
            Literal[
                "Size",
                "LastModifiedDate",
                "StorageClass",
                "ETag",
                "IsMultipartUploaded",
                "ReplicationStatus",
                "EncryptionStatus",
                "ObjectLockRetainUntilDate",
                "ObjectLockMode",
                "ObjectLockLegalHoldStatus",
                "IntelligentTieringAccessTier",
            ]
        ],
        "Schedule": ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef,
    },
    total=False,
)


class ClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef(
    _RequiredClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef,
    _OptionalClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef,
):
    pass


ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef,
        "And": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef",
    {
        "Expiration": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Filter": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "Transitions": List[
            ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef
        ],
        "NoncurrentVersionTransitions": List[
            ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef
        ],
        "NoncurrentVersionExpiration": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef",
    {"Rules": List[ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef]},
)

ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef",
    {
        "Expiration": ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Status": Literal["Enabled", "Disabled"],
        "Transition": ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef,
        "NoncurrentVersionTransition": ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef,
        "NoncurrentVersionExpiration": ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationTypeDef",
    {"Rules": List[ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef]},
)

ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE"],
    },
    total=False,
)

_RequiredClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef = TypedDict(
    "_RequiredClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef", {"TargetBucket": str}
)
_OptionalClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef = TypedDict(
    "_OptionalClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef",
    {
        "TargetGrants": List[
            ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef
        ],
        "TargetPrefix": str,
    },
    total=False,
)


class ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef(
    _RequiredClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef,
    _OptionalClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef,
):
    pass


ClientPutBucketLoggingBucketLoggingStatusTypeDef = TypedDict(
    "ClientPutBucketLoggingBucketLoggingStatusTypeDef",
    {"LoggingEnabled": ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef},
    total=False,
)

ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef = TypedDict(
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef = TypedDict(
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef],
    },
    total=False,
)

ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef = TypedDict(
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef = TypedDict(
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef,
        "And": ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef,
    },
    total=False,
)

_RequiredClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef", {"Id": str}
)
_OptionalClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef",
    {"Filter": ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef},
    total=False,
)


class ClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef(
    _RequiredClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef,
    _OptionalClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef,
):
    pass


ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef",
    {
        "Id": str,
        "LambdaFunctionArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef",
    {
        "Id": str,
        "QueueArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef",
    {
        "Id": str,
        "TopicArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef",
    {
        "TopicConfigurations": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef
        ],
        "QueueConfigurations": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef
        ],
        "LambdaFunctionConfigurations": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "CloudFunction": str,
        "InvocationRole": str,
    },
    total=False,
)

ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef",
    {
        "Id": str,
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Queue": str,
    },
    total=False,
)

ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef",
    {
        "Id": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Topic": str,
    },
    total=False,
)

ClientPutBucketNotificationNotificationConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationNotificationConfigurationTypeDef",
    {
        "TopicConfiguration": ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef,
        "QueueConfiguration": ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef,
        "CloudFunctionConfiguration": ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    {"Owner": str},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    {"ReplicaKmsKeyID": str},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    {"Minutes": int},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "EventThreshold": ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    {"Minutes": int},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "Time": ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef",
    {
        "Bucket": str,
        "Account": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "AccessControlTranslation": ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef,
        "EncryptionConfiguration": ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef,
        "ReplicationTime": ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef,
        "Metrics": ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef],
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef,
        "And": ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "SourceSelectionCriteria": ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef,
        "ExistingObjectReplication": ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef,
        "Destination": ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef,
        "DeleteMarkerReplication": ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef,
    },
    total=False,
)

_RequiredClientPutBucketReplicationReplicationConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBucketReplicationReplicationConfigurationTypeDef", {"Role": str}
)
_OptionalClientPutBucketReplicationReplicationConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBucketReplicationReplicationConfigurationTypeDef",
    {"Rules": List[ClientPutBucketReplicationReplicationConfigurationRulesTypeDef]},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationTypeDef(
    _RequiredClientPutBucketReplicationReplicationConfigurationTypeDef,
    _OptionalClientPutBucketReplicationReplicationConfigurationTypeDef,
):
    pass


ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef = TypedDict(
    "ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef",
    {"Payer": Literal["Requester", "BucketOwner"]},
)

_RequiredClientPutBucketTaggingTaggingTagSetTypeDef = TypedDict(
    "_RequiredClientPutBucketTaggingTaggingTagSetTypeDef", {"Key": str}
)
_OptionalClientPutBucketTaggingTaggingTagSetTypeDef = TypedDict(
    "_OptionalClientPutBucketTaggingTaggingTagSetTypeDef", {"Value": str}, total=False
)


class ClientPutBucketTaggingTaggingTagSetTypeDef(
    _RequiredClientPutBucketTaggingTaggingTagSetTypeDef,
    _OptionalClientPutBucketTaggingTaggingTagSetTypeDef,
):
    pass


ClientPutBucketTaggingTaggingTypeDef = TypedDict(
    "ClientPutBucketTaggingTaggingTypeDef",
    {"TagSet": List[ClientPutBucketTaggingTaggingTagSetTypeDef]},
)

ClientPutBucketVersioningVersioningConfigurationTypeDef = TypedDict(
    "ClientPutBucketVersioningVersioningConfigurationTypeDef",
    {"MFADelete": Literal["Enabled", "Disabled"], "Status": Literal["Enabled", "Suspended"]},
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef", {"Key": str}
)

ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef", {"Suffix": str}, total=False
)

ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": Literal["http", "https"]},
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef",
    {
        "Condition": ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef,
        "Redirect": ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef,
    },
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef,
        "IndexDocument": ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef,
        "RedirectAllRequestsTo": ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef,
        "RoutingRules": List[ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef],
    },
    total=False,
)

ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientPutObjectAclAccessControlPolicyGrantsTypeDef = TypedDict(
    "ClientPutObjectAclAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientPutObjectAclAccessControlPolicyOwnerTypeDef = TypedDict(
    "ClientPutObjectAclAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientPutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "ClientPutObjectAclAccessControlPolicyTypeDef",
    {
        "Grants": List[ClientPutObjectAclAccessControlPolicyGrantsTypeDef],
        "Owner": ClientPutObjectAclAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)

ClientPutObjectAclResponseTypeDef = TypedDict(
    "ClientPutObjectAclResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientPutObjectLegalHoldLegalHoldTypeDef = TypedDict(
    "ClientPutObjectLegalHoldLegalHoldTypeDef", {"Status": Literal["ON", "OFF"]}, total=False
)

ClientPutObjectLegalHoldResponseTypeDef = TypedDict(
    "ClientPutObjectLegalHoldResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef = TypedDict(
    "ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "Days": int, "Years": int},
    total=False,
)

ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef = TypedDict(
    "ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef",
    {
        "DefaultRetention": ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef
    },
    total=False,
)

ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef = TypedDict(
    "ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef,
    },
    total=False,
)

ClientPutObjectLockConfigurationResponseTypeDef = TypedDict(
    "ClientPutObjectLockConfigurationResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientPutObjectResponseTypeDef = TypedDict(
    "ClientPutObjectResponseTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientPutObjectRetentionResponseTypeDef = TypedDict(
    "ClientPutObjectRetentionResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientPutObjectRetentionRetentionTypeDef = TypedDict(
    "ClientPutObjectRetentionRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "RetainUntilDate": datetime},
    total=False,
)

ClientPutObjectTaggingResponseTypeDef = TypedDict(
    "ClientPutObjectTaggingResponseTypeDef", {"VersionId": str}, total=False
)

_RequiredClientPutObjectTaggingTaggingTagSetTypeDef = TypedDict(
    "_RequiredClientPutObjectTaggingTaggingTagSetTypeDef", {"Key": str}
)
_OptionalClientPutObjectTaggingTaggingTagSetTypeDef = TypedDict(
    "_OptionalClientPutObjectTaggingTaggingTagSetTypeDef", {"Value": str}, total=False
)


class ClientPutObjectTaggingTaggingTagSetTypeDef(
    _RequiredClientPutObjectTaggingTaggingTagSetTypeDef,
    _OptionalClientPutObjectTaggingTaggingTagSetTypeDef,
):
    pass


ClientPutObjectTaggingTaggingTypeDef = TypedDict(
    "ClientPutObjectTaggingTaggingTypeDef",
    {"TagSet": List[ClientPutObjectTaggingTaggingTagSetTypeDef]},
)

ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef = TypedDict(
    "ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

ClientRestoreObjectResponseTypeDef = TypedDict(
    "ClientRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)

ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    {"Tier": Literal["Standard", "Bulk", "Expedited"]},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["AES256", "aws:kms"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {"TagSet": List[ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef]},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef,
        "UserMetadata": List[ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef],
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
    },
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef,
        "Type": str,
        "Tier": Literal["Standard", "Bulk", "Expedited"],
        "Description": str,
        "SelectParameters": ClientRestoreObjectRestoreRequestSelectParametersTypeDef,
        "OutputLocation": ClientRestoreObjectRestoreRequestOutputLocationTypeDef,
    },
    total=False,
)

ClientSelectObjectContentInputSerializationCSVTypeDef = TypedDict(
    "ClientSelectObjectContentInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

ClientSelectObjectContentInputSerializationJSONTypeDef = TypedDict(
    "ClientSelectObjectContentInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)

ClientSelectObjectContentInputSerializationTypeDef = TypedDict(
    "ClientSelectObjectContentInputSerializationTypeDef",
    {
        "CSV": ClientSelectObjectContentInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ClientSelectObjectContentInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)

ClientSelectObjectContentOutputSerializationCSVTypeDef = TypedDict(
    "ClientSelectObjectContentOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientSelectObjectContentOutputSerializationJSONTypeDef = TypedDict(
    "ClientSelectObjectContentOutputSerializationJSONTypeDef", {"RecordDelimiter": str}, total=False
)

ClientSelectObjectContentOutputSerializationTypeDef = TypedDict(
    "ClientSelectObjectContentOutputSerializationTypeDef",
    {
        "CSV": ClientSelectObjectContentOutputSerializationCSVTypeDef,
        "JSON": ClientSelectObjectContentOutputSerializationJSONTypeDef,
    },
    total=False,
)

ClientSelectObjectContentRequestProgressTypeDef = TypedDict(
    "ClientSelectObjectContentRequestProgressTypeDef", {"Enabled": bool}, total=False
)

ClientSelectObjectContentResponseTypeDef = TypedDict(
    "ClientSelectObjectContentResponseTypeDef", {"Payload": EventStream}, total=False
)

ClientSelectObjectContentScanRangeTypeDef = TypedDict(
    "ClientSelectObjectContentScanRangeTypeDef", {"Start": int, "End": int}, total=False
)

ClientUploadPartCopyCopySource1TypeDef = TypedDict(
    "ClientUploadPartCopyCopySource1TypeDef",
    {"Bucket": str, "Key": str, "VersionId": str},
    total=False,
)

ClientUploadPartCopyResponseCopyPartResultTypeDef = TypedDict(
    "ClientUploadPartCopyResponseCopyPartResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)

ClientUploadPartCopyResponseTypeDef = TypedDict(
    "ClientUploadPartCopyResponseTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": ClientUploadPartCopyResponseCopyPartResultTypeDef,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientUploadPartResponseTypeDef = TypedDict(
    "ClientUploadPartResponseTypeDef",
    {
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)

_RequiredCopySourceTypeDef = TypedDict("_RequiredCopySourceTypeDef", {"Bucket": str, "Key": str})
_OptionalCopySourceTypeDef = TypedDict(
    "_OptionalCopySourceTypeDef", {"VersionId": str}, total=False
)


class CopySourceTypeDef(_RequiredCopySourceTypeDef, _OptionalCopySourceTypeDef):
    pass


ListMultipartUploadsPaginatePaginationConfigTypeDef = TypedDict(
    "ListMultipartUploadsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef = TypedDict(
    "ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)

ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef = TypedDict(
    "ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ListMultipartUploadsPaginateResponseUploadsTypeDef = TypedDict(
    "ListMultipartUploadsPaginateResponseUploadsTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "Owner": ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef,
        "Initiator": ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef,
    },
    total=False,
)

ListMultipartUploadsPaginateResponseTypeDef = TypedDict(
    "ListMultipartUploadsPaginateResponseTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List[ListMultipartUploadsPaginateResponseUploadsTypeDef],
        "CommonPrefixes": List[ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "NextToken": str,
    },
    total=False,
)

ListObjectVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListObjectVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListObjectVersionsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "ListObjectVersionsPaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef = TypedDict(
    "ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ListObjectVersionsPaginateResponseDeleteMarkersTypeDef = TypedDict(
    "ListObjectVersionsPaginateResponseDeleteMarkersTypeDef",
    {
        "Owner": ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)

ListObjectVersionsPaginateResponseVersionsOwnerTypeDef = TypedDict(
    "ListObjectVersionsPaginateResponseVersionsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ListObjectVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListObjectVersionsPaginateResponseVersionsTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": ListObjectVersionsPaginateResponseVersionsOwnerTypeDef,
    },
    total=False,
)

ListObjectVersionsPaginateResponseTypeDef = TypedDict(
    "ListObjectVersionsPaginateResponseTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "Versions": List[ListObjectVersionsPaginateResponseVersionsTypeDef],
        "DeleteMarkers": List[ListObjectVersionsPaginateResponseDeleteMarkersTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ListObjectVersionsPaginateResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "NextToken": str,
    },
    total=False,
)

ListObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "ListObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListObjectsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "ListObjectsPaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ListObjectsPaginateResponseContentsOwnerTypeDef = TypedDict(
    "ListObjectsPaginateResponseContentsOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ListObjectsPaginateResponseContentsTypeDef = TypedDict(
    "ListObjectsPaginateResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "Owner": ListObjectsPaginateResponseContentsOwnerTypeDef,
    },
    total=False,
)

ListObjectsPaginateResponseTypeDef = TypedDict(
    "ListObjectsPaginateResponseTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List[ListObjectsPaginateResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ListObjectsPaginateResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "NextToken": str,
    },
    total=False,
)

ListObjectsV2PaginatePaginationConfigTypeDef = TypedDict(
    "ListObjectsV2PaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListObjectsV2PaginateResponseCommonPrefixesTypeDef = TypedDict(
    "ListObjectsV2PaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ListObjectsV2PaginateResponseContentsOwnerTypeDef = TypedDict(
    "ListObjectsV2PaginateResponseContentsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ListObjectsV2PaginateResponseContentsTypeDef = TypedDict(
    "ListObjectsV2PaginateResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "Owner": ListObjectsV2PaginateResponseContentsOwnerTypeDef,
    },
    total=False,
)

ListObjectsV2PaginateResponseTypeDef = TypedDict(
    "ListObjectsV2PaginateResponseTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List[ListObjectsV2PaginateResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ListObjectsV2PaginateResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "KeyCount": int,
        "ContinuationToken": str,
        "StartAfter": str,
        "NextToken": str,
    },
    total=False,
)

ListPartsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPartsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPartsPaginateResponseInitiatorTypeDef = TypedDict(
    "ListPartsPaginateResponseInitiatorTypeDef", {"ID": str, "DisplayName": str}, total=False
)

ListPartsPaginateResponseOwnerTypeDef = TypedDict(
    "ListPartsPaginateResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ListPartsPaginateResponsePartsTypeDef = TypedDict(
    "ListPartsPaginateResponsePartsTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)

ListPartsPaginateResponseTypeDef = TypedDict(
    "ListPartsPaginateResponseTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List[ListPartsPaginateResponsePartsTypeDef],
        "Initiator": ListPartsPaginateResponseInitiatorTypeDef,
        "Owner": ListPartsPaginateResponseOwnerTypeDef,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "NextToken": str,
    },
    total=False,
)

MultipartUploadAbortResponseTypeDef = TypedDict(
    "MultipartUploadAbortResponseTypeDef", {"RequestCharged": str}, total=False
)

MultipartUploadCompleteMultipartUploadPartsTypeDef = TypedDict(
    "MultipartUploadCompleteMultipartUploadPartsTypeDef",
    {"ETag": str, "PartNumber": int},
    total=False,
)

MultipartUploadCompleteMultipartUploadTypeDef = TypedDict(
    "MultipartUploadCompleteMultipartUploadTypeDef",
    {"Parts": List[MultipartUploadCompleteMultipartUploadPartsTypeDef]},
    total=False,
)

MultipartUploadPartCopyFromCopySource1TypeDef = TypedDict(
    "MultipartUploadPartCopyFromCopySource1TypeDef",
    {"Bucket": str, "Key": str, "VersionId": str},
    total=False,
)

MultipartUploadPartCopyFromResponseCopyPartResultTypeDef = TypedDict(
    "MultipartUploadPartCopyFromResponseCopyPartResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)

MultipartUploadPartCopyFromResponseTypeDef = TypedDict(
    "MultipartUploadPartCopyFromResponseTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": MultipartUploadPartCopyFromResponseCopyPartResultTypeDef,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)

MultipartUploadPartUploadResponseTypeDef = TypedDict(
    "MultipartUploadPartUploadResponseTypeDef",
    {
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)

ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ObjectAclPutAccessControlPolicyGrantsTypeDef = TypedDict(
    "ObjectAclPutAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ObjectAclPutAccessControlPolicyOwnerTypeDef = TypedDict(
    "ObjectAclPutAccessControlPolicyOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ObjectAclPutAccessControlPolicyTypeDef = TypedDict(
    "ObjectAclPutAccessControlPolicyTypeDef",
    {
        "Grants": List[ObjectAclPutAccessControlPolicyGrantsTypeDef],
        "Owner": ObjectAclPutAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)

ObjectAclPutResponseTypeDef = TypedDict(
    "ObjectAclPutResponseTypeDef", {"RequestCharged": str}, total=False
)

ObjectCopyFromCopySource1TypeDef = TypedDict(
    "ObjectCopyFromCopySource1TypeDef", {"Bucket": str, "Key": str, "VersionId": str}, total=False
)

ObjectCopyFromResponseCopyObjectResultTypeDef = TypedDict(
    "ObjectCopyFromResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)

ObjectCopyFromResponseTypeDef = TypedDict(
    "ObjectCopyFromResponseTypeDef",
    {
        "CopyObjectResult": ObjectCopyFromResponseCopyObjectResultTypeDef,
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ObjectDeleteResponseTypeDef = TypedDict(
    "ObjectDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)

ObjectExistsWaitWaiterConfigTypeDef = TypedDict(
    "ObjectExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ObjectGetResponseTypeDef = TypedDict(
    "ObjectGetResponseTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

ObjectNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "ObjectNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ObjectPutResponseTypeDef = TypedDict(
    "ObjectPutResponseTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ObjectRestoreObjectResponseTypeDef = TypedDict(
    "ObjectRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)

ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    {"Tier": Literal["Standard", "Bulk", "Expedited"]},
    total=False,
)

ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["AES256", "aws:kms"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {"TagSet": List[ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef]},
    total=False,
)

ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef,
        "UserMetadata": List[ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef],
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
    },
    total=False,
)

ObjectRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)

ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)

ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)

ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)

ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)

ObjectRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ObjectRestoreObjectRestoreRequestTypeDef = TypedDict(
    "ObjectRestoreObjectRestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef,
        "Type": str,
        "Tier": Literal["Standard", "Bulk", "Expedited"],
        "Description": str,
        "SelectParameters": ObjectRestoreObjectRestoreRequestSelectParametersTypeDef,
        "OutputLocation": ObjectRestoreObjectRestoreRequestOutputLocationTypeDef,
    },
    total=False,
)

ObjectSummaryCopyFromCopySource1TypeDef = TypedDict(
    "ObjectSummaryCopyFromCopySource1TypeDef",
    {"Bucket": str, "Key": str, "VersionId": str},
    total=False,
)

ObjectSummaryCopyFromResponseCopyObjectResultTypeDef = TypedDict(
    "ObjectSummaryCopyFromResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)

ObjectSummaryCopyFromResponseTypeDef = TypedDict(
    "ObjectSummaryCopyFromResponseTypeDef",
    {
        "CopyObjectResult": ObjectSummaryCopyFromResponseCopyObjectResultTypeDef,
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ObjectSummaryDeleteResponseTypeDef = TypedDict(
    "ObjectSummaryDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)

ObjectSummaryGetResponseTypeDef = TypedDict(
    "ObjectSummaryGetResponseTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

ObjectSummaryPutResponseTypeDef = TypedDict(
    "ObjectSummaryPutResponseTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ObjectSummaryRestoreObjectResponseTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    {"Tier": Literal["Standard", "Bulk", "Expedited"]},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["AES256", "aws:kms"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {"TagSet": List[ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef]},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef,
        "UserMetadata": List[
            ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
        ],
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
    },
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ObjectSummaryRestoreObjectRestoreRequestTypeDef = TypedDict(
    "ObjectSummaryRestoreObjectRestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef,
        "Type": str,
        "Tier": Literal["Standard", "Bulk", "Expedited"],
        "Description": str,
        "SelectParameters": ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef,
        "OutputLocation": ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef,
    },
    total=False,
)

ObjectVersionDeleteResponseTypeDef = TypedDict(
    "ObjectVersionDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)

ObjectVersionGetResponseTypeDef = TypedDict(
    "ObjectVersionGetResponseTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

ObjectVersionHeadResponseTypeDef = TypedDict(
    "ObjectVersionHeadResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

ObjectVersionsDeleteResponseDeletedTypeDef = TypedDict(
    "ObjectVersionsDeleteResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)

ObjectVersionsDeleteResponseErrorsTypeDef = TypedDict(
    "ObjectVersionsDeleteResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)

ObjectVersionsDeleteResponseTypeDef = TypedDict(
    "ObjectVersionsDeleteResponseTypeDef",
    {
        "Deleted": List[ObjectVersionsDeleteResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ObjectVersionsDeleteResponseErrorsTypeDef],
    },
    total=False,
)

ObjectsDeleteResponseDeletedTypeDef = TypedDict(
    "ObjectsDeleteResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)

ObjectsDeleteResponseErrorsTypeDef = TypedDict(
    "ObjectsDeleteResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)

ObjectsDeleteResponseTypeDef = TypedDict(
    "ObjectsDeleteResponseTypeDef",
    {
        "Deleted": List[ObjectsDeleteResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ObjectsDeleteResponseErrorsTypeDef],
    },
    total=False,
)

ServiceResourceCreateBucketCreateBucketConfigurationTypeDef = TypedDict(
    "ServiceResourceCreateBucketCreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": Literal[
            "EU",
            "eu-west-1",
            "us-west-1",
            "us-west-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "cn-north-1",
            "eu-central-1",
        ]
    },
    total=False,
)
