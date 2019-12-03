"Main interface for s3 service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from botocore.eventstream import EventStream
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "BucketAclPutAccessControlPolicyGrantsGranteeTypeDef",
    "BucketAclPutAccessControlPolicyGrantsTypeDef",
    "BucketAclPutAccessControlPolicyOwnerTypeDef",
    "BucketAclPutAccessControlPolicyTypeDef",
    "BucketCorsPutCORSConfigurationCORSRulesTypeDef",
    "BucketCorsPutCORSConfigurationTypeDef",
    "BucketCreateCreateBucketConfigurationTypeDef",
    "BucketCreateResponseTypeDef",
    "BucketDeleteObjectsDeleteObjectsTypeDef",
    "BucketDeleteObjectsDeleteTypeDef",
    "BucketDeleteObjectsResponseDeletedTypeDef",
    "BucketDeleteObjectsResponseErrorsTypeDef",
    "BucketDeleteObjectsResponseTypeDef",
    "BucketExistsWaitWaiterConfigTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesExpirationTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesTransitionsTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef",
    "BucketLifecycleConfigurationPutLifecycleConfigurationTypeDef",
    "BucketLifecyclePutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    "BucketLifecyclePutLifecycleConfigurationRulesExpirationTypeDef",
    "BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    "BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef",
    "BucketLifecyclePutLifecycleConfigurationRulesTransitionTypeDef",
    "BucketLifecyclePutLifecycleConfigurationRulesTypeDef",
    "BucketLifecyclePutLifecycleConfigurationTypeDef",
    "BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef",
    "BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef",
    "BucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef",
    "BucketLoggingPutBucketLoggingStatusTypeDef",
    "BucketNotExistsWaitWaiterConfigTypeDef",
    "BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    "BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef",
    "BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef",
    "BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsTypeDef",
    "BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef",
    "BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef",
    "BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterTypeDef",
    "BucketNotificationPutNotificationConfigurationQueueConfigurationsTypeDef",
    "BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef",
    "BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef",
    "BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterTypeDef",
    "BucketNotificationPutNotificationConfigurationTopicConfigurationsTypeDef",
    "BucketNotificationPutNotificationConfigurationTypeDef",
    "BucketRequestPaymentPutRequestPaymentConfigurationTypeDef",
    "BucketTaggingPutTaggingTagSetTypeDef",
    "BucketTaggingPutTaggingTypeDef",
    "BucketVersioningPutVersioningConfigurationTypeDef",
    "BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef",
    "BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef",
    "BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef",
    "BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef",
    "BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef",
    "BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef",
    "BucketWebsitePutWebsiteConfigurationTypeDef",
    "ClientAbortMultipartUploadResponseTypeDef",
    "ClientCompleteMultipartUploadMultipartUploadPartsTypeDef",
    "ClientCompleteMultipartUploadMultipartUploadTypeDef",
    "ClientCompleteMultipartUploadResponseTypeDef",
    "ClientCopyObjectCopySource1TypeDef",
    "ClientCopyObjectResponseCopyObjectResultTypeDef",
    "ClientCopyObjectResponseTypeDef",
    "ClientCreateBucketCreateBucketConfigurationTypeDef",
    "ClientCreateBucketResponseTypeDef",
    "ClientCreateMultipartUploadResponseTypeDef",
    "ClientDeleteObjectResponseTypeDef",
    "ClientDeleteObjectTaggingResponseTypeDef",
    "ClientDeleteObjectsDeleteObjectsTypeDef",
    "ClientDeleteObjectsDeleteTypeDef",
    "ClientDeleteObjectsResponseDeletedTypeDef",
    "ClientDeleteObjectsResponseErrorsTypeDef",
    "ClientDeleteObjectsResponseTypeDef",
    "ClientGetBucketAccelerateConfigurationResponseTypeDef",
    "ClientGetBucketAclResponseGrantsGranteeTypeDef",
    "ClientGetBucketAclResponseGrantsTypeDef",
    "ClientGetBucketAclResponseOwnerTypeDef",
    "ClientGetBucketAclResponseTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseTypeDef",
    "ClientGetBucketCorsResponseCORSRulesTypeDef",
    "ClientGetBucketCorsResponseTypeDef",
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef",
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef",
    "ClientGetBucketEncryptionResponseTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef",
    "ClientGetBucketInventoryConfigurationResponseTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseTypeDef",
    "ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef",
    "ClientGetBucketLifecycleResponseRulesExpirationTypeDef",
    "ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef",
    "ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef",
    "ClientGetBucketLifecycleResponseRulesTransitionTypeDef",
    "ClientGetBucketLifecycleResponseRulesTypeDef",
    "ClientGetBucketLifecycleResponseTypeDef",
    "ClientGetBucketLocationResponseTypeDef",
    "ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef",
    "ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef",
    "ClientGetBucketLoggingResponseLoggingEnabledTypeDef",
    "ClientGetBucketLoggingResponseTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef",
    "ClientGetBucketMetricsConfigurationResponseTypeDef",
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef",
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef",
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef",
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef",
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef",
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTypeDef",
    "ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef",
    "ClientGetBucketNotificationResponseQueueConfigurationTypeDef",
    "ClientGetBucketNotificationResponseTopicConfigurationTypeDef",
    "ClientGetBucketNotificationResponseTypeDef",
    "ClientGetBucketPolicyResponseTypeDef",
    "ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef",
    "ClientGetBucketPolicyStatusResponseTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationTypeDef",
    "ClientGetBucketReplicationResponseTypeDef",
    "ClientGetBucketRequestPaymentResponseTypeDef",
    "ClientGetBucketTaggingResponseTagSetTypeDef",
    "ClientGetBucketTaggingResponseTypeDef",
    "ClientGetBucketVersioningResponseTypeDef",
    "ClientGetBucketWebsiteResponseErrorDocumentTypeDef",
    "ClientGetBucketWebsiteResponseIndexDocumentTypeDef",
    "ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef",
    "ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef",
    "ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef",
    "ClientGetBucketWebsiteResponseRoutingRulesTypeDef",
    "ClientGetBucketWebsiteResponseTypeDef",
    "ClientGetObjectAclResponseGrantsGranteeTypeDef",
    "ClientGetObjectAclResponseGrantsTypeDef",
    "ClientGetObjectAclResponseOwnerTypeDef",
    "ClientGetObjectAclResponseTypeDef",
    "ClientGetObjectLegalHoldResponseLegalHoldTypeDef",
    "ClientGetObjectLegalHoldResponseTypeDef",
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef",
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef",
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef",
    "ClientGetObjectLockConfigurationResponseTypeDef",
    "ClientGetObjectResponseTypeDef",
    "ClientGetObjectRetentionResponseRetentionTypeDef",
    "ClientGetObjectRetentionResponseTypeDef",
    "ClientGetObjectTaggingResponseTagSetTypeDef",
    "ClientGetObjectTaggingResponseTypeDef",
    "ClientGetObjectTorrentResponseTypeDef",
    "ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    "ClientGetPublicAccessBlockResponseTypeDef",
    "ClientHeadObjectResponseTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef",
    "ClientListBucketInventoryConfigurationsResponseTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef",
    "ClientListBucketMetricsConfigurationsResponseTypeDef",
    "ClientListBucketsResponseBucketsTypeDef",
    "ClientListBucketsResponseOwnerTypeDef",
    "ClientListBucketsResponseTypeDef",
    "ClientListMultipartUploadsResponseCommonPrefixesTypeDef",
    "ClientListMultipartUploadsResponseUploadsInitiatorTypeDef",
    "ClientListMultipartUploadsResponseUploadsOwnerTypeDef",
    "ClientListMultipartUploadsResponseUploadsTypeDef",
    "ClientListMultipartUploadsResponseTypeDef",
    "ClientListObjectVersionsResponseCommonPrefixesTypeDef",
    "ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef",
    "ClientListObjectVersionsResponseDeleteMarkersTypeDef",
    "ClientListObjectVersionsResponseVersionsOwnerTypeDef",
    "ClientListObjectVersionsResponseVersionsTypeDef",
    "ClientListObjectVersionsResponseTypeDef",
    "ClientListObjectsResponseCommonPrefixesTypeDef",
    "ClientListObjectsResponseContentsOwnerTypeDef",
    "ClientListObjectsResponseContentsTypeDef",
    "ClientListObjectsResponseTypeDef",
    "ClientListObjectsV2ResponseCommonPrefixesTypeDef",
    "ClientListObjectsV2ResponseContentsOwnerTypeDef",
    "ClientListObjectsV2ResponseContentsTypeDef",
    "ClientListObjectsV2ResponseTypeDef",
    "ClientListPartsResponseInitiatorTypeDef",
    "ClientListPartsResponseOwnerTypeDef",
    "ClientListPartsResponsePartsTypeDef",
    "ClientListPartsResponseTypeDef",
    "ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef",
    "ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef",
    "ClientPutBucketAclAccessControlPolicyGrantsTypeDef",
    "ClientPutBucketAclAccessControlPolicyOwnerTypeDef",
    "ClientPutBucketAclAccessControlPolicyTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef",
    "ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef",
    "ClientPutBucketCorsCORSConfigurationTypeDef",
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef",
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationTypeDef",
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef",
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef",
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef",
    "ClientPutBucketLoggingBucketLoggingStatusTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef",
    "ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef",
    "ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef",
    "ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef",
    "ClientPutBucketNotificationNotificationConfigurationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationTypeDef",
    "ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef",
    "ClientPutBucketTaggingTaggingTagSetTypeDef",
    "ClientPutBucketTaggingTaggingTypeDef",
    "ClientPutBucketVersioningVersioningConfigurationTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationTypeDef",
    "ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef",
    "ClientPutObjectAclAccessControlPolicyGrantsTypeDef",
    "ClientPutObjectAclAccessControlPolicyOwnerTypeDef",
    "ClientPutObjectAclAccessControlPolicyTypeDef",
    "ClientPutObjectAclResponseTypeDef",
    "ClientPutObjectLegalHoldLegalHoldTypeDef",
    "ClientPutObjectLegalHoldResponseTypeDef",
    "ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef",
    "ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef",
    "ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef",
    "ClientPutObjectLockConfigurationResponseTypeDef",
    "ClientPutObjectResponseTypeDef",
    "ClientPutObjectRetentionResponseTypeDef",
    "ClientPutObjectRetentionRetentionTypeDef",
    "ClientPutObjectTaggingResponseTypeDef",
    "ClientPutObjectTaggingTaggingTagSetTypeDef",
    "ClientPutObjectTaggingTaggingTypeDef",
    "ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    "ClientRestoreObjectResponseTypeDef",
    "ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersTypeDef",
    "ClientRestoreObjectRestoreRequestTypeDef",
    "ClientSelectObjectContentInputSerializationCSVTypeDef",
    "ClientSelectObjectContentInputSerializationJSONTypeDef",
    "ClientSelectObjectContentInputSerializationTypeDef",
    "ClientSelectObjectContentOutputSerializationCSVTypeDef",
    "ClientSelectObjectContentOutputSerializationJSONTypeDef",
    "ClientSelectObjectContentOutputSerializationTypeDef",
    "ClientSelectObjectContentRequestProgressTypeDef",
    "ClientSelectObjectContentResponseTypeDef",
    "ClientSelectObjectContentScanRangeTypeDef",
    "ClientUploadPartCopyCopySource1TypeDef",
    "ClientUploadPartCopyResponseCopyPartResultTypeDef",
    "ClientUploadPartCopyResponseTypeDef",
    "ClientUploadPartResponseTypeDef",
    "ListMultipartUploadsPaginatePaginationConfigTypeDef",
    "ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef",
    "ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef",
    "ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef",
    "ListMultipartUploadsPaginateResponseUploadsTypeDef",
    "ListMultipartUploadsPaginateResponseTypeDef",
    "ListObjectVersionsPaginatePaginationConfigTypeDef",
    "ListObjectVersionsPaginateResponseCommonPrefixesTypeDef",
    "ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef",
    "ListObjectVersionsPaginateResponseDeleteMarkersTypeDef",
    "ListObjectVersionsPaginateResponseVersionsOwnerTypeDef",
    "ListObjectVersionsPaginateResponseVersionsTypeDef",
    "ListObjectVersionsPaginateResponseTypeDef",
    "ListObjectsPaginatePaginationConfigTypeDef",
    "ListObjectsPaginateResponseCommonPrefixesTypeDef",
    "ListObjectsPaginateResponseContentsOwnerTypeDef",
    "ListObjectsPaginateResponseContentsTypeDef",
    "ListObjectsPaginateResponseTypeDef",
    "ListObjectsV2PaginatePaginationConfigTypeDef",
    "ListObjectsV2PaginateResponseCommonPrefixesTypeDef",
    "ListObjectsV2PaginateResponseContentsOwnerTypeDef",
    "ListObjectsV2PaginateResponseContentsTypeDef",
    "ListObjectsV2PaginateResponseTypeDef",
    "ListPartsPaginatePaginationConfigTypeDef",
    "ListPartsPaginateResponseInitiatorTypeDef",
    "ListPartsPaginateResponseOwnerTypeDef",
    "ListPartsPaginateResponsePartsTypeDef",
    "ListPartsPaginateResponseTypeDef",
    "MultipartUploadAbortResponseTypeDef",
    "MultipartUploadCompleteMultipartUploadPartsTypeDef",
    "MultipartUploadCompleteMultipartUploadTypeDef",
    "MultipartUploadPartCopyFromCopySource1TypeDef",
    "MultipartUploadPartCopyFromResponseCopyPartResultTypeDef",
    "MultipartUploadPartCopyFromResponseTypeDef",
    "MultipartUploadPartUploadResponseTypeDef",
    "ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef",
    "ObjectAclPutAccessControlPolicyGrantsTypeDef",
    "ObjectAclPutAccessControlPolicyOwnerTypeDef",
    "ObjectAclPutAccessControlPolicyTypeDef",
    "ObjectAclPutResponseTypeDef",
    "ObjectCopyFromCopySource1TypeDef",
    "ObjectCopyFromResponseCopyObjectResultTypeDef",
    "ObjectCopyFromResponseTypeDef",
    "ObjectDeleteResponseTypeDef",
    "ObjectExistsWaitWaiterConfigTypeDef",
    "ObjectGetResponseTypeDef",
    "ObjectNotExistsWaitWaiterConfigTypeDef",
    "ObjectPutResponseTypeDef",
    "ObjectRestoreObjectResponseTypeDef",
    "ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    "ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    "ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    "ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    "ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    "ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    "ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    "ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    "ObjectRestoreObjectRestoreRequestOutputLocationTypeDef",
    "ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    "ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    "ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    "ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    "ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    "ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    "ObjectRestoreObjectRestoreRequestSelectParametersTypeDef",
    "ObjectRestoreObjectRestoreRequestTypeDef",
    "ObjectSummaryCopyFromCopySource1TypeDef",
    "ObjectSummaryCopyFromResponseCopyObjectResultTypeDef",
    "ObjectSummaryCopyFromResponseTypeDef",
    "ObjectSummaryDeleteResponseTypeDef",
    "ObjectSummaryGetResponseTypeDef",
    "ObjectSummaryPutResponseTypeDef",
    "ObjectSummaryRestoreObjectResponseTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef",
    "ObjectSummaryRestoreObjectRestoreRequestTypeDef",
    "ObjectVersionDeleteResponseTypeDef",
    "ObjectVersionGetResponseTypeDef",
    "ObjectVersionHeadResponseTypeDef",
    "ObjectVersionsDeleteResponseDeletedTypeDef",
    "ObjectVersionsDeleteResponseErrorsTypeDef",
    "ObjectVersionsDeleteResponseTypeDef",
    "ObjectsDeleteResponseDeletedTypeDef",
    "ObjectsDeleteResponseErrorsTypeDef",
    "ObjectsDeleteResponseTypeDef",
    "ServiceResourceCreateBucketCreateBucketConfigurationTypeDef",
)


_BucketAclPutAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_BucketAclPutAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class BucketAclPutAccessControlPolicyGrantsGranteeTypeDef(
    _BucketAclPutAccessControlPolicyGrantsGranteeTypeDef
):
    """
    - **Grantee** *(dict) --*

      The person being granted permissions.
      - **DisplayName** *(string) --*

        Screen name of the grantee.
    """


_BucketAclPutAccessControlPolicyGrantsTypeDef = TypedDict(
    "_BucketAclPutAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": BucketAclPutAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class BucketAclPutAccessControlPolicyGrantsTypeDef(_BucketAclPutAccessControlPolicyGrantsTypeDef):
    """
    - *(dict) --*

      Container for grant information.
      - **Grantee** *(dict) --*

        The person being granted permissions.
        - **DisplayName** *(string) --*

          Screen name of the grantee.
    """


_BucketAclPutAccessControlPolicyOwnerTypeDef = TypedDict(
    "_BucketAclPutAccessControlPolicyOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class BucketAclPutAccessControlPolicyOwnerTypeDef(_BucketAclPutAccessControlPolicyOwnerTypeDef):
    pass


_BucketAclPutAccessControlPolicyTypeDef = TypedDict(
    "_BucketAclPutAccessControlPolicyTypeDef",
    {
        "Grants": List[BucketAclPutAccessControlPolicyGrantsTypeDef],
        "Owner": BucketAclPutAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)


class BucketAclPutAccessControlPolicyTypeDef(_BucketAclPutAccessControlPolicyTypeDef):
    """
    Contains the elements that set the ACL permissions for an object per grantee.
    - **Grants** *(list) --*

      A list of grants.
      - *(dict) --*

        Container for grant information.
        - **Grantee** *(dict) --*

          The person being granted permissions.
          - **DisplayName** *(string) --*

            Screen name of the grantee.
    """


_BucketCorsPutCORSConfigurationCORSRulesTypeDef = TypedDict(
    "_BucketCorsPutCORSConfigurationCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)


class BucketCorsPutCORSConfigurationCORSRulesTypeDef(
    _BucketCorsPutCORSConfigurationCORSRulesTypeDef
):
    """
    - *(dict) --*

      Specifies a cross-origin access rule for an Amazon S3 bucket.
      - **AllowedHeaders** *(list) --*

        Headers that are specified in the ``Access-Control-Request-Headers`` header. These headers
        are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request,
        Amazon S3 returns any requested headers that are allowed.
        - *(string) --*
    """


_BucketCorsPutCORSConfigurationTypeDef = TypedDict(
    "_BucketCorsPutCORSConfigurationTypeDef",
    {"CORSRules": List[BucketCorsPutCORSConfigurationCORSRulesTypeDef]},
)


class BucketCorsPutCORSConfigurationTypeDef(_BucketCorsPutCORSConfigurationTypeDef):
    """
    Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more
    information, see `Enabling Cross-Origin Resource Sharing
    <https://docs.aws.amazon.com/AmazonS3/latest/dev//cors.html>`__ in the *Amazon Simple Storage
    Service Developer Guide* .
    - **CORSRules** *(list) --***[REQUIRED]**

      A set of origins and methods (cross-origin access that you want to allow). You can add up to
      100 rules to the configuration.
      - *(dict) --*

        Specifies a cross-origin access rule for an Amazon S3 bucket.
        - **AllowedHeaders** *(list) --*

          Headers that are specified in the ``Access-Control-Request-Headers`` header. These headers
          are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request,
          Amazon S3 returns any requested headers that are allowed.
          - *(string) --*
    """


_BucketCreateCreateBucketConfigurationTypeDef = TypedDict(
    "_BucketCreateCreateBucketConfigurationTypeDef",
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


class BucketCreateCreateBucketConfigurationTypeDef(_BucketCreateCreateBucketConfigurationTypeDef):
    """
    The configuration information for the bucket.
    - **LocationConstraint** *(string) --*

      Specifies the Region where the bucket will be created. If you don't specify a Region, the
      bucket is created in the US East (N. Virginia) Region (us-east-1).
    """


_BucketCreateResponseTypeDef = TypedDict(
    "_BucketCreateResponseTypeDef", {"Location": str}, total=False
)


class BucketCreateResponseTypeDef(_BucketCreateResponseTypeDef):
    """
    - *(dict) --*

      - **Location** *(string) --*

        Specifies the Region where the bucket will be created. If you are creating a bucket on the
        US East (N. Virginia) Region (us-east-1), you do not need to specify the location.
    """


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
    """
    - *(dict) --*

      Object Identifier is unique value to identify objects.
      - **Key** *(string) --***[REQUIRED]**

        Key name of the object to delete.
    """


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
    """
    Container for the request.
    - **Objects** *(list) --***[REQUIRED]**

      The objects to delete.
      - *(dict) --*

        Object Identifier is unique value to identify objects.
        - **Key** *(string) --***[REQUIRED]**

          Key name of the object to delete.
    """


_BucketDeleteObjectsResponseDeletedTypeDef = TypedDict(
    "_BucketDeleteObjectsResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)


class BucketDeleteObjectsResponseDeletedTypeDef(_BucketDeleteObjectsResponseDeletedTypeDef):
    """
    - *(dict) --*

      Information about the deleted object.
      - **Key** *(string) --*

        The name of the deleted object.
    """


_BucketDeleteObjectsResponseErrorsTypeDef = TypedDict(
    "_BucketDeleteObjectsResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)


class BucketDeleteObjectsResponseErrorsTypeDef(_BucketDeleteObjectsResponseErrorsTypeDef):
    pass


_BucketDeleteObjectsResponseTypeDef = TypedDict(
    "_BucketDeleteObjectsResponseTypeDef",
    {
        "Deleted": List[BucketDeleteObjectsResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[BucketDeleteObjectsResponseErrorsTypeDef],
    },
    total=False,
)


class BucketDeleteObjectsResponseTypeDef(_BucketDeleteObjectsResponseTypeDef):
    """
    - *(dict) --*

      - **Deleted** *(list) --*

        Container element for a successful delete. It identifies the object that was successfully
        deleted.
        - *(dict) --*

          Information about the deleted object.
          - **Key** *(string) --*

            The name of the deleted object.
    """


_BucketExistsWaitWaiterConfigTypeDef = TypedDict(
    "_BucketExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class BucketExistsWaitWaiterConfigTypeDef(_BucketExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef
):
    pass


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesExpirationTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesExpirationTypeDef
):
    """
    - **Expiration** *(dict) --*

      Specifies the expiration for the lifecycle of the object in the form of date, days and,
      whether the object has a delete marker.
      - **Date** *(datetime) --*

        Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
        Format.
    """


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef
):
    pass


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef
):
    pass


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef
):
    pass


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTagTypeDef,
        "And": BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesFilterTypeDef
):
    pass


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef
):
    pass


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef
):
    pass


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesTransitionsTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesTransitionsTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesTransitionsTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesTransitionsTypeDef
):
    pass


_BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef",
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


class BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef
):
    """
    - *(dict) --*

      A lifecycle rule for individual objects in an Amazon S3 bucket.
      - **Expiration** *(dict) --*

        Specifies the expiration for the lifecycle of the object in the form of date, days and,
        whether the object has a delete marker.
        - **Date** *(datetime) --*

          Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
          Format.
    """


_BucketLifecycleConfigurationPutLifecycleConfigurationTypeDef = TypedDict(
    "_BucketLifecycleConfigurationPutLifecycleConfigurationTypeDef",
    {"Rules": List[BucketLifecycleConfigurationPutLifecycleConfigurationRulesTypeDef]},
)


class BucketLifecycleConfigurationPutLifecycleConfigurationTypeDef(
    _BucketLifecycleConfigurationPutLifecycleConfigurationTypeDef
):
    """
    Container for lifecycle rules. You can add as many as 1,000 rules.
    - **Rules** *(list) --***[REQUIRED]**

      A lifecycle rule for individual objects in an Amazon S3 bucket.
      - *(dict) --*

        A lifecycle rule for individual objects in an Amazon S3 bucket.
        - **Expiration** *(dict) --*

          Specifies the expiration for the lifecycle of the object in the form of date, days and,
          whether the object has a delete marker.
          - **Date** *(datetime) --*

            Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
            Format.
    """


_BucketLifecyclePutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "_BucketLifecyclePutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)


class BucketLifecyclePutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef(
    _BucketLifecyclePutLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef
):
    pass


_BucketLifecyclePutLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "_BucketLifecyclePutLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)


class BucketLifecyclePutLifecycleConfigurationRulesExpirationTypeDef(
    _BucketLifecyclePutLifecycleConfigurationRulesExpirationTypeDef
):
    """
    - **Expiration** *(dict) --*

      Specifies the expiration for the lifecycle of the object.
      - **Date** *(datetime) --*

        Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
        Format.
    """


_BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "_BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)


class BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef(
    _BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef
):
    pass


_BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "_BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef(
    _BucketLifecyclePutLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef
):
    pass


_BucketLifecyclePutLifecycleConfigurationRulesTransitionTypeDef = TypedDict(
    "_BucketLifecyclePutLifecycleConfigurationRulesTransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class BucketLifecyclePutLifecycleConfigurationRulesTransitionTypeDef(
    _BucketLifecyclePutLifecycleConfigurationRulesTransitionTypeDef
):
    pass


_BucketLifecyclePutLifecycleConfigurationRulesTypeDef = TypedDict(
    "_BucketLifecyclePutLifecycleConfigurationRulesTypeDef",
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


class BucketLifecyclePutLifecycleConfigurationRulesTypeDef(
    _BucketLifecyclePutLifecycleConfigurationRulesTypeDef
):
    """
    - *(dict) --*

      Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
      lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__ in
      the *Amazon Simple Storage Service API Reference* .
      - **Expiration** *(dict) --*

        Specifies the expiration for the lifecycle of the object.
        - **Date** *(datetime) --*

          Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
          Format.
    """


_BucketLifecyclePutLifecycleConfigurationTypeDef = TypedDict(
    "_BucketLifecyclePutLifecycleConfigurationTypeDef",
    {"Rules": List[BucketLifecyclePutLifecycleConfigurationRulesTypeDef]},
)


class BucketLifecyclePutLifecycleConfigurationTypeDef(
    _BucketLifecyclePutLifecycleConfigurationTypeDef
):
    """
    - **Rules** *(list) --***[REQUIRED]**

      Specifies lifecycle configuration rules for an Amazon S3 bucket.
      - *(dict) --*

        Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
        lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__
        in the *Amazon Simple Storage Service API Reference* .
        - **Expiration** *(dict) --*

          Specifies the expiration for the lifecycle of the object.
          - **Date** *(datetime) --*

            Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
            Format.
    """


_BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "_BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef(
    _BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef
):
    pass


_BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "_BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE"],
    },
    total=False,
)


class BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef(
    _BucketLoggingPutBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef
):
    pass


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
    """
    - **LoggingEnabled** *(dict) --*

      Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys
      for a bucket. For more information, see `PUT Bucket logging
      <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html>`__ in the *Amazon
      Simple Storage Service API Reference* .
      - **TargetBucket** *(string) --***[REQUIRED]**

        Specifies the bucket where you want Amazon S3 to store server access logs. You can have your
        logs delivered to any bucket that you own, including the same bucket that is being logged.
        You can also configure multiple buckets to deliver their logs to the same target bucket. In
        this case, you should choose a different ``TargetPrefix`` for each source bucket so that the
        delivered log files can be distinguished by key.
    """


_BucketLoggingPutBucketLoggingStatusTypeDef = TypedDict(
    "_BucketLoggingPutBucketLoggingStatusTypeDef",
    {"LoggingEnabled": BucketLoggingPutBucketLoggingStatusLoggingEnabledTypeDef},
    total=False,
)


class BucketLoggingPutBucketLoggingStatusTypeDef(_BucketLoggingPutBucketLoggingStatusTypeDef):
    """
    Container for logging status information.
    - **LoggingEnabled** *(dict) --*

      Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys
      for a bucket. For more information, see `PUT Bucket logging
      <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html>`__ in the *Amazon
      Simple Storage Service API Reference* .
      - **TargetBucket** *(string) --***[REQUIRED]**

        Specifies the bucket where you want Amazon S3 to store server access logs. You can have your
        logs delivered to any bucket that you own, including the same bucket that is being logged.
        You can also configure multiple buckets to deliver their logs to the same target bucket. In
        this case, you should choose a different ``TargetPrefix`` for each source bucket so that the
        delivered log files can be distinguished by key.
    """


_BucketNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "_BucketNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class BucketNotExistsWaitWaiterConfigTypeDef(_BucketNotExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


_BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef(
    _BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef(
    _BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)


class BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef(
    _BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsTypeDef",
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


class BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsTypeDef(
    _BucketNotificationPutNotificationConfigurationLambdaFunctionConfigurationsTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef(
    _BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef(
    _BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterTypeDef",
    {"Key": BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterKeyTypeDef},
    total=False,
)


class BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterTypeDef(
    _BucketNotificationPutNotificationConfigurationQueueConfigurationsFilterTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationQueueConfigurationsTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationQueueConfigurationsTypeDef",
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


class BucketNotificationPutNotificationConfigurationQueueConfigurationsTypeDef(
    _BucketNotificationPutNotificationConfigurationQueueConfigurationsTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef(
    _BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef(
    _BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterTypeDef",
    {"Key": BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterKeyTypeDef},
    total=False,
)


class BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterTypeDef(
    _BucketNotificationPutNotificationConfigurationTopicConfigurationsFilterTypeDef
):
    pass


_BucketNotificationPutNotificationConfigurationTopicConfigurationsTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationTopicConfigurationsTypeDef",
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


class BucketNotificationPutNotificationConfigurationTopicConfigurationsTypeDef(
    _BucketNotificationPutNotificationConfigurationTopicConfigurationsTypeDef
):
    """
    - *(dict) --*

      A container for specifying the configuration for publication of messages to an Amazon Simple
      Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.
    """


_BucketNotificationPutNotificationConfigurationTypeDef = TypedDict(
    "_BucketNotificationPutNotificationConfigurationTypeDef",
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


class BucketNotificationPutNotificationConfigurationTypeDef(
    _BucketNotificationPutNotificationConfigurationTypeDef
):
    """
    A container for specifying the notification configuration of the bucket. If this element is
    empty, notifications are turned off for the bucket.
    - **TopicConfigurations** *(list) --*

      The topic to which notifications are sent and the events for which notifications are
      generated.
      - *(dict) --*

        A container for specifying the configuration for publication of messages to an Amazon Simple
        Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
        - **Id** *(string) --*

          An optional unique identifier for configurations in a notification configuration. If you
          don't provide one, Amazon S3 will assign an ID.
    """


_BucketRequestPaymentPutRequestPaymentConfigurationTypeDef = TypedDict(
    "_BucketRequestPaymentPutRequestPaymentConfigurationTypeDef",
    {"Payer": Literal["Requester", "BucketOwner"]},
)


class BucketRequestPaymentPutRequestPaymentConfigurationTypeDef(
    _BucketRequestPaymentPutRequestPaymentConfigurationTypeDef
):
    """
    Container for Payer.
    - **Payer** *(string) --***[REQUIRED]**

      Specifies who pays for the download and request fees.
    """


_RequiredBucketTaggingPutTaggingTagSetTypeDef = TypedDict(
    "_RequiredBucketTaggingPutTaggingTagSetTypeDef", {"Key": str}
)
_OptionalBucketTaggingPutTaggingTagSetTypeDef = TypedDict(
    "_OptionalBucketTaggingPutTaggingTagSetTypeDef", {"Value": str}, total=False
)


class BucketTaggingPutTaggingTagSetTypeDef(
    _RequiredBucketTaggingPutTaggingTagSetTypeDef, _OptionalBucketTaggingPutTaggingTagSetTypeDef
):
    """
    - *(dict) --*

      A container of a key value name pair.
      - **Key** *(string) --***[REQUIRED]**

        Name of the tag.
    """


_BucketTaggingPutTaggingTypeDef = TypedDict(
    "_BucketTaggingPutTaggingTypeDef", {"TagSet": List[BucketTaggingPutTaggingTagSetTypeDef]}
)


class BucketTaggingPutTaggingTypeDef(_BucketTaggingPutTaggingTypeDef):
    """
    Container for the ``TagSet`` and ``Tag`` elements.
    - **TagSet** *(list) --***[REQUIRED]**

      A collection for a set of tags
      - *(dict) --*

        A container of a key value name pair.
        - **Key** *(string) --***[REQUIRED]**

          Name of the tag.
    """


_BucketVersioningPutVersioningConfigurationTypeDef = TypedDict(
    "_BucketVersioningPutVersioningConfigurationTypeDef",
    {"MFADelete": Literal["Enabled", "Disabled"], "Status": Literal["Enabled", "Suspended"]},
    total=False,
)


class BucketVersioningPutVersioningConfigurationTypeDef(
    _BucketVersioningPutVersioningConfigurationTypeDef
):
    """
    Container for setting the versioning state.
    - **MFADelete** *(string) --*

      Specifies whether MFA delete is enabled in the bucket versioning configuration. This element
      is only returned if the bucket has been configured with MFA delete. If the bucket has never
      been so configured, this element is not returned.
    """


_BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef = TypedDict(
    "_BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef", {"Key": str}
)


class BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef(
    _BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef
):
    """
    - **ErrorDocument** *(dict) --*

      The name of the error document for the website.
      - **Key** *(string) --***[REQUIRED]**

        The object key name to use when a 4XX class error occurs.
    """


_BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef = TypedDict(
    "_BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef", {"Suffix": str}, total=False
)


class BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef(
    _BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef
):
    pass


_BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef = TypedDict(
    "_BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": Literal["http", "https"]},
    total=False,
)


class BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef(
    _BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef
):
    pass


_BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef = TypedDict(
    "_BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)


class BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef(
    _BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef
):
    pass


_BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef = TypedDict(
    "_BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)


class BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef(
    _BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef
):
    pass


_BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef = TypedDict(
    "_BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef",
    {
        "Condition": BucketWebsitePutWebsiteConfigurationRoutingRulesConditionTypeDef,
        "Redirect": BucketWebsitePutWebsiteConfigurationRoutingRulesRedirectTypeDef,
    },
    total=False,
)


class BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef(
    _BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef
):
    pass


_BucketWebsitePutWebsiteConfigurationTypeDef = TypedDict(
    "_BucketWebsitePutWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": BucketWebsitePutWebsiteConfigurationErrorDocumentTypeDef,
        "IndexDocument": BucketWebsitePutWebsiteConfigurationIndexDocumentTypeDef,
        "RedirectAllRequestsTo": BucketWebsitePutWebsiteConfigurationRedirectAllRequestsToTypeDef,
        "RoutingRules": List[BucketWebsitePutWebsiteConfigurationRoutingRulesTypeDef],
    },
    total=False,
)


class BucketWebsitePutWebsiteConfigurationTypeDef(_BucketWebsitePutWebsiteConfigurationTypeDef):
    """
    Container for the request.
    - **ErrorDocument** *(dict) --*

      The name of the error document for the website.
      - **Key** *(string) --***[REQUIRED]**

        The object key name to use when a 4XX class error occurs.
    """


_ClientAbortMultipartUploadResponseTypeDef = TypedDict(
    "_ClientAbortMultipartUploadResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientAbortMultipartUploadResponseTypeDef(_ClientAbortMultipartUploadResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ClientCompleteMultipartUploadMultipartUploadPartsTypeDef = TypedDict(
    "_ClientCompleteMultipartUploadMultipartUploadPartsTypeDef",
    {"ETag": str, "PartNumber": int},
    total=False,
)


class ClientCompleteMultipartUploadMultipartUploadPartsTypeDef(
    _ClientCompleteMultipartUploadMultipartUploadPartsTypeDef
):
    """
    - *(dict) --*

      Details of the parts that were uploaded.
      - **ETag** *(string) --*

        Entity tag returned when the part was uploaded.
    """


_ClientCompleteMultipartUploadMultipartUploadTypeDef = TypedDict(
    "_ClientCompleteMultipartUploadMultipartUploadTypeDef",
    {"Parts": List[ClientCompleteMultipartUploadMultipartUploadPartsTypeDef]},
    total=False,
)


class ClientCompleteMultipartUploadMultipartUploadTypeDef(
    _ClientCompleteMultipartUploadMultipartUploadTypeDef
):
    """
    The container for the multipart upload request information.
    - **Parts** *(list) --*

      Array of CompletedPart data types.
      - *(dict) --*

        Details of the parts that were uploaded.
        - **ETag** *(string) --*

          Entity tag returned when the part was uploaded.
    """


_ClientCompleteMultipartUploadResponseTypeDef = TypedDict(
    "_ClientCompleteMultipartUploadResponseTypeDef",
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


class ClientCompleteMultipartUploadResponseTypeDef(_ClientCompleteMultipartUploadResponseTypeDef):
    """
    - *(dict) --*

      - **Location** *(string) --*

        The URI that identifies the newly created object.
    """


_ClientCopyObjectCopySource1TypeDef = TypedDict(
    "_ClientCopyObjectCopySource1TypeDef",
    {"Bucket": str, "Key": str, "VersionId": str},
    total=False,
)


class ClientCopyObjectCopySource1TypeDef(_ClientCopyObjectCopySource1TypeDef):
    pass


_ClientCopyObjectResponseCopyObjectResultTypeDef = TypedDict(
    "_ClientCopyObjectResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class ClientCopyObjectResponseCopyObjectResultTypeDef(
    _ClientCopyObjectResponseCopyObjectResultTypeDef
):
    """
    - **CopyObjectResult** *(dict) --*

      Container for all response elements.
      - **ETag** *(string) --*

        Returns the ETag of the new object. The ETag reflects only changes to the contents of an
        object, not its metadata. The source and destination ETag is identical for a successfully
        copied object.
    """


_ClientCopyObjectResponseTypeDef = TypedDict(
    "_ClientCopyObjectResponseTypeDef",
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


class ClientCopyObjectResponseTypeDef(_ClientCopyObjectResponseTypeDef):
    """
    - *(dict) --*

      - **CopyObjectResult** *(dict) --*

        Container for all response elements.
        - **ETag** *(string) --*

          Returns the ETag of the new object. The ETag reflects only changes to the contents of an
          object, not its metadata. The source and destination ETag is identical for a successfully
          copied object.
    """


_ClientCreateBucketCreateBucketConfigurationTypeDef = TypedDict(
    "_ClientCreateBucketCreateBucketConfigurationTypeDef",
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


class ClientCreateBucketCreateBucketConfigurationTypeDef(
    _ClientCreateBucketCreateBucketConfigurationTypeDef
):
    """
    The configuration information for the bucket.
    - **LocationConstraint** *(string) --*

      Specifies the Region where the bucket will be created. If you don't specify a Region, the
      bucket is created in the US East (N. Virginia) Region (us-east-1).
    """


_ClientCreateBucketResponseTypeDef = TypedDict(
    "_ClientCreateBucketResponseTypeDef", {"Location": str}, total=False
)


class ClientCreateBucketResponseTypeDef(_ClientCreateBucketResponseTypeDef):
    """
    - *(dict) --*

      - **Location** *(string) --*

        Specifies the Region where the bucket will be created. If you are creating a bucket on the
        US East (N. Virginia) Region (us-east-1), you do not need to specify the location.
    """


_ClientCreateMultipartUploadResponseTypeDef = TypedDict(
    "_ClientCreateMultipartUploadResponseTypeDef",
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


class ClientCreateMultipartUploadResponseTypeDef(_ClientCreateMultipartUploadResponseTypeDef):
    """
    - *(dict) --*

      - **AbortDate** *(datetime) --*

        If the bucket has a lifecycle rule configured with an action to abort incomplete multipart
        uploads and the prefix in the lifecycle rule matches the object name in the request, the
        response includes this header. The header indicates when the initiated multipart upload
        becomes eligible for an abort operation. For more information, see `Aborting Incomplete
        Multipart Uploads Using a Bucket Lifecycle Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
        .
        The response also includes the ``x-amz-abort-rule-id`` header that provides the ID of the
        lifecycle configuration rule that defines this action.
    """


_ClientDeleteObjectResponseTypeDef = TypedDict(
    "_ClientDeleteObjectResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)


class ClientDeleteObjectResponseTypeDef(_ClientDeleteObjectResponseTypeDef):
    """
    - *(dict) --*

      - **DeleteMarker** *(boolean) --*

        Specifies whether the versioned object that was permanently deleted was (true) or was not
        (false) a delete marker.
    """


_ClientDeleteObjectTaggingResponseTypeDef = TypedDict(
    "_ClientDeleteObjectTaggingResponseTypeDef", {"VersionId": str}, total=False
)


class ClientDeleteObjectTaggingResponseTypeDef(_ClientDeleteObjectTaggingResponseTypeDef):
    """
    - *(dict) --*

      - **VersionId** *(string) --*

        The versionId of the object the tag-set was removed from.
    """


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
    """
    - *(dict) --*

      Object Identifier is unique value to identify objects.
      - **Key** *(string) --***[REQUIRED]**

        Key name of the object to delete.
    """


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
    """
    Container for the request.
    - **Objects** *(list) --***[REQUIRED]**

      The objects to delete.
      - *(dict) --*

        Object Identifier is unique value to identify objects.
        - **Key** *(string) --***[REQUIRED]**

          Key name of the object to delete.
    """


_ClientDeleteObjectsResponseDeletedTypeDef = TypedDict(
    "_ClientDeleteObjectsResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)


class ClientDeleteObjectsResponseDeletedTypeDef(_ClientDeleteObjectsResponseDeletedTypeDef):
    """
    - *(dict) --*

      Information about the deleted object.
      - **Key** *(string) --*

        The name of the deleted object.
    """


_ClientDeleteObjectsResponseErrorsTypeDef = TypedDict(
    "_ClientDeleteObjectsResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)


class ClientDeleteObjectsResponseErrorsTypeDef(_ClientDeleteObjectsResponseErrorsTypeDef):
    pass


_ClientDeleteObjectsResponseTypeDef = TypedDict(
    "_ClientDeleteObjectsResponseTypeDef",
    {
        "Deleted": List[ClientDeleteObjectsResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ClientDeleteObjectsResponseErrorsTypeDef],
    },
    total=False,
)


class ClientDeleteObjectsResponseTypeDef(_ClientDeleteObjectsResponseTypeDef):
    """
    - *(dict) --*

      - **Deleted** *(list) --*

        Container element for a successful delete. It identifies the object that was successfully
        deleted.
        - *(dict) --*

          Information about the deleted object.
          - **Key** *(string) --*

            The name of the deleted object.
    """


_ClientGetBucketAccelerateConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketAccelerateConfigurationResponseTypeDef",
    {"Status": Literal["Enabled", "Suspended"]},
    total=False,
)


class ClientGetBucketAccelerateConfigurationResponseTypeDef(
    _ClientGetBucketAccelerateConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The accelerate configuration of the bucket.
    """


_ClientGetBucketAclResponseGrantsGranteeTypeDef = TypedDict(
    "_ClientGetBucketAclResponseGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ClientGetBucketAclResponseGrantsGranteeTypeDef(
    _ClientGetBucketAclResponseGrantsGranteeTypeDef
):
    pass


_ClientGetBucketAclResponseGrantsTypeDef = TypedDict(
    "_ClientGetBucketAclResponseGrantsTypeDef",
    {
        "Grantee": ClientGetBucketAclResponseGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ClientGetBucketAclResponseGrantsTypeDef(_ClientGetBucketAclResponseGrantsTypeDef):
    pass


_ClientGetBucketAclResponseOwnerTypeDef = TypedDict(
    "_ClientGetBucketAclResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ClientGetBucketAclResponseOwnerTypeDef(_ClientGetBucketAclResponseOwnerTypeDef):
    """
    - **Owner** *(dict) --*

      Container for the bucket owner's display name and ID.
      - **DisplayName** *(string) --*

        Container for the display name of the owner.
    """


_ClientGetBucketAclResponseTypeDef = TypedDict(
    "_ClientGetBucketAclResponseTypeDef",
    {
        "Owner": ClientGetBucketAclResponseOwnerTypeDef,
        "Grants": List[ClientGetBucketAclResponseGrantsTypeDef],
    },
    total=False,
)


class ClientGetBucketAclResponseTypeDef(_ClientGetBucketAclResponseTypeDef):
    """
    - *(dict) --*

      - **Owner** *(dict) --*

        Container for the bucket owner's display name and ID.
        - **DisplayName** *(string) --*

          Container for the display name of the owner.
    """


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef
):
    pass


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef
):
    pass


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef
):
    pass


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef,
        "And": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef,
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef
):
    pass


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
):
    pass


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef
):
    pass


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
):
    pass


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef
):
    pass


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef,
        "StorageClassAnalysis": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef,
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef
):
    """
    - **AnalyticsConfiguration** *(dict) --*

      The configuration and any analyses for the analytics filter.
      - **Id** *(string) --*

        The ID that identifies the analytics configuration.
    """


_ClientGetBucketAnalyticsConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseTypeDef",
    {
        "AnalyticsConfiguration": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **AnalyticsConfiguration** *(dict) --*

        The configuration and any analyses for the analytics filter.
        - **Id** *(string) --*

          The ID that identifies the analytics configuration.
    """


_ClientGetBucketCorsResponseCORSRulesTypeDef = TypedDict(
    "_ClientGetBucketCorsResponseCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)


class ClientGetBucketCorsResponseCORSRulesTypeDef(_ClientGetBucketCorsResponseCORSRulesTypeDef):
    """
    - *(dict) --*

      Specifies a cross-origin access rule for an Amazon S3 bucket.
      - **AllowedHeaders** *(list) --*

        Headers that are specified in the ``Access-Control-Request-Headers`` header. These headers
        are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request,
        Amazon S3 returns any requested headers that are allowed.
        - *(string) --*
    """


_ClientGetBucketCorsResponseTypeDef = TypedDict(
    "_ClientGetBucketCorsResponseTypeDef",
    {"CORSRules": List[ClientGetBucketCorsResponseCORSRulesTypeDef]},
    total=False,
)


class ClientGetBucketCorsResponseTypeDef(_ClientGetBucketCorsResponseTypeDef):
    """
    - *(dict) --*

      - **CORSRules** *(list) --*

        A set of origins and methods (cross-origin access that you want to allow). You can add up to
        100 rules to the configuration.
        - *(dict) --*

          Specifies a cross-origin access rule for an Amazon S3 bucket.
          - **AllowedHeaders** *(list) --*

            Headers that are specified in the ``Access-Control-Request-Headers`` header. These
            headers are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS
            request, Amazon S3 returns any requested headers that are allowed.
            - *(string) --*
    """


_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    {"SSEAlgorithm": Literal["AES256", "aws:kms"], "KMSMasterKeyID": str},
    total=False,
)


class ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef(
    _ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
):
    """
    - **ApplyServerSideEncryptionByDefault** *(dict) --*

      Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT
      Object request doesn't specify any server-side encryption, this default encryption will be
      applied.
      - **SSEAlgorithm** *(string) --*

        Server-side encryption algorithm to use for the default encryption.
    """


_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef = TypedDict(
    "_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
    },
    total=False,
)


class ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef(
    _ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef
):
    """
    - *(dict) --*

      Specifies the default server-side encryption configuration.
      - **ApplyServerSideEncryptionByDefault** *(dict) --*

        Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT
        Object request doesn't specify any server-side encryption, this default encryption will be
        applied.
        - **SSEAlgorithm** *(string) --*

          Server-side encryption algorithm to use for the default encryption.
    """


_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef",
    {"Rules": List[ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef]},
    total=False,
)


class ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef(
    _ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef
):
    """
    - **ServerSideEncryptionConfiguration** *(dict) --*

      Specifies the default server-side-encryption configuration.
      - **Rules** *(list) --*

        Container for information about a particular server-side encryption configuration rule.
        - *(dict) --*

          Specifies the default server-side encryption configuration.
          - **ApplyServerSideEncryptionByDefault** *(dict) --*

            Specifies the default server-side encryption to apply to new objects in the bucket. If a
            PUT Object request doesn't specify any server-side encryption, this default encryption
            will be applied.
            - **SSEAlgorithm** *(string) --*

              Server-side encryption algorithm to use for the default encryption.
    """


_ClientGetBucketEncryptionResponseTypeDef = TypedDict(
    "_ClientGetBucketEncryptionResponseTypeDef",
    {
        "ServerSideEncryptionConfiguration": ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketEncryptionResponseTypeDef(_ClientGetBucketEncryptionResponseTypeDef):
    """
    - *(dict) --*

      - **ServerSideEncryptionConfiguration** *(dict) --*

        Specifies the default server-side-encryption configuration.
        - **Rules** *(list) --*

          Container for information about a particular server-side encryption configuration rule.
          - *(dict) --*

            Specifies the default server-side encryption configuration.
            - **ApplyServerSideEncryptionByDefault** *(dict) --*

              Specifies the default server-side encryption to apply to new objects in the bucket. If
              a PUT Object request doesn't specify any server-side encryption, this default
              encryption will be applied.
              - **SSEAlgorithm** *(string) --*

                Server-side encryption algorithm to use for the default encryption.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef
):
    pass


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef
):
    pass


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef
):
    """
    - **S3BucketDestination** *(dict) --*

      Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
      inventory results are published.
      - **AccountId** *(string) --*

        The ID of the account that owns the destination bucket.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef",
    {
        "S3BucketDestination": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef
):
    """
    - **Destination** *(dict) --*

      Contains information about where to publish the inventory results.
      - **S3BucketDestination** *(dict) --*

        Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
        inventory results are published.
        - **AccountId** *(string) --*

          The ID of the account that owns the destination bucket.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef",
    {"Prefix": str},
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef
):
    pass


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef
):
    pass


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef",
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


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef
):
    """
    - **InventoryConfiguration** *(dict) --*

      Specifies the inventory configuration.
      - **Destination** *(dict) --*

        Contains information about where to publish the inventory results.
        - **S3BucketDestination** *(dict) --*

          Contains the bucket name, file format, bucket owner (optional), and prefix (optional)
          where inventory results are published.
          - **AccountId** *(string) --*

            The ID of the account that owns the destination bucket.
    """


_ClientGetBucketInventoryConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseTypeDef",
    {
        "InventoryConfiguration": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseTypeDef(
    _ClientGetBucketInventoryConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **InventoryConfiguration** *(dict) --*

        Specifies the inventory configuration.
        - **Destination** *(dict) --*

          Contains information about where to publish the inventory results.
          - **S3BucketDestination** *(dict) --*

            Contains the bucket name, file format, bucket owner (optional), and prefix (optional)
            where inventory results are published.
            - **AccountId** *(string) --*

              The ID of the account that owns the destination bucket.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef
):
    pass


_ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef
):
    """
    - **Expiration** *(dict) --*

      Specifies the expiration for the lifecycle of the object in the form of date, days and,
      whether the object has a delete marker.
      - **Date** *(datetime) --*

        Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
        Format.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef
):
    pass


_ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef],
    },
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef
):
    pass


_ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef
):
    pass


_ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef,
        "And": ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef,
    },
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef
):
    pass


_ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef
):
    pass


_ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef
):
    pass


_ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef
):
    pass


_ClientGetBucketLifecycleConfigurationResponseRulesTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesTypeDef",
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


class ClientGetBucketLifecycleConfigurationResponseRulesTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesTypeDef
):
    """
    - *(dict) --*

      A lifecycle rule for individual objects in an Amazon S3 bucket.
      - **Expiration** *(dict) --*

        Specifies the expiration for the lifecycle of the object in the form of date, days and,
        whether the object has a delete marker.
        - **Date** *(datetime) --*

          Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
          Format.
    """


_ClientGetBucketLifecycleConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseTypeDef",
    {"Rules": List[ClientGetBucketLifecycleConfigurationResponseRulesTypeDef]},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        Container for a lifecycle rule.
        - *(dict) --*

          A lifecycle rule for individual objects in an Amazon S3 bucket.
          - **Expiration** *(dict) --*

            Specifies the expiration for the lifecycle of the object in the form of date, days and,
            whether the object has a delete marker.
            - **Date** *(datetime) --*

              Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
              Format.
    """


_ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)


class ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef(
    _ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef
):
    pass


_ClientGetBucketLifecycleResponseRulesExpirationTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)


class ClientGetBucketLifecycleResponseRulesExpirationTypeDef(
    _ClientGetBucketLifecycleResponseRulesExpirationTypeDef
):
    """
    - **Expiration** *(dict) --*

      Specifies the expiration for the lifecycle of the object.
      - **Date** *(datetime) --*

        Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
        Format.
    """


_ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)


class ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef(
    _ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef
):
    pass


_ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef(
    _ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef
):
    pass


_ClientGetBucketLifecycleResponseRulesTransitionTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesTransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class ClientGetBucketLifecycleResponseRulesTransitionTypeDef(
    _ClientGetBucketLifecycleResponseRulesTransitionTypeDef
):
    pass


_ClientGetBucketLifecycleResponseRulesTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesTypeDef",
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


class ClientGetBucketLifecycleResponseRulesTypeDef(_ClientGetBucketLifecycleResponseRulesTypeDef):
    """
    - *(dict) --*

      Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
      lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__ in
      the *Amazon Simple Storage Service API Reference* .
      - **Expiration** *(dict) --*

        Specifies the expiration for the lifecycle of the object.
        - **Date** *(datetime) --*

          Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
          Format.
    """


_ClientGetBucketLifecycleResponseTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseTypeDef",
    {"Rules": List[ClientGetBucketLifecycleResponseRulesTypeDef]},
    total=False,
)


class ClientGetBucketLifecycleResponseTypeDef(_ClientGetBucketLifecycleResponseTypeDef):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        Container for a lifecycle rule.
        - *(dict) --*

          Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
          lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__
          in the *Amazon Simple Storage Service API Reference* .
          - **Expiration** *(dict) --*

            Specifies the expiration for the lifecycle of the object.
            - **Date** *(datetime) --*

              Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
              Format.
    """


_ClientGetBucketLocationResponseTypeDef = TypedDict(
    "_ClientGetBucketLocationResponseTypeDef",
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


class ClientGetBucketLocationResponseTypeDef(_ClientGetBucketLocationResponseTypeDef):
    """
    - *(dict) --*

      - **LocationConstraint** *(string) --*

        Specifies the Region where the bucket resides. For a list of all the Amazon S3 supported
        location constraints by Region, see `Regions and Endpoints
        <https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ .
    """


_ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "_ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef(
    _ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef
):
    pass


_ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "_ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE"],
    },
    total=False,
)


class ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef(
    _ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef
):
    pass


_ClientGetBucketLoggingResponseLoggingEnabledTypeDef = TypedDict(
    "_ClientGetBucketLoggingResponseLoggingEnabledTypeDef",
    {
        "TargetBucket": str,
        "TargetGrants": List[ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef],
        "TargetPrefix": str,
    },
    total=False,
)


class ClientGetBucketLoggingResponseLoggingEnabledTypeDef(
    _ClientGetBucketLoggingResponseLoggingEnabledTypeDef
):
    """
    - **LoggingEnabled** *(dict) --*

      Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys
      for a bucket. For more information, see `PUT Bucket logging
      <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html>`__ in the *Amazon
      Simple Storage Service API Reference* .
      - **TargetBucket** *(string) --*

        Specifies the bucket where you want Amazon S3 to store server access logs. You can have your
        logs delivered to any bucket that you own, including the same bucket that is being logged.
        You can also configure multiple buckets to deliver their logs to the same target bucket. In
        this case, you should choose a different ``TargetPrefix`` for each source bucket so that the
        delivered log files can be distinguished by key.
    """


_ClientGetBucketLoggingResponseTypeDef = TypedDict(
    "_ClientGetBucketLoggingResponseTypeDef",
    {"LoggingEnabled": ClientGetBucketLoggingResponseLoggingEnabledTypeDef},
    total=False,
)


class ClientGetBucketLoggingResponseTypeDef(_ClientGetBucketLoggingResponseTypeDef):
    """
    - *(dict) --*

      - **LoggingEnabled** *(dict) --*

        Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys
        for a bucket. For more information, see `PUT Bucket logging
        <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html>`__ in the
        *Amazon Simple Storage Service API Reference* .
        - **TargetBucket** *(string) --*

          Specifies the bucket where you want Amazon S3 to store server access logs. You can have
          your logs delivered to any bucket that you own, including the same bucket that is being
          logged. You can also configure multiple buckets to deliver their logs to the same target
          bucket. In this case, you should choose a different ``TargetPrefix`` for each source
          bucket so that the delivered log files can be distinguished by key.
    """


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef
):
    pass


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef
):
    pass


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef
):
    pass


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef,
        "And": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef,
    },
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef
):
    pass


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef,
    },
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef
):
    """
    - **MetricsConfiguration** *(dict) --*

      Specifies the metrics configuration.
      - **Id** *(string) --*

        The ID used to identify the metrics configuration.
    """


_ClientGetBucketMetricsConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseTypeDef",
    {
        "MetricsConfiguration": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseTypeDef(
    _ClientGetBucketMetricsConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **MetricsConfiguration** *(dict) --*

        Specifies the metrics configuration.
        - **Id** *(string) --*

          The ID used to identify the metrics configuration.
    """


_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef(
    _ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef(
    _ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef",
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


class ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef(
    _ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef(
    _ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef",
    {"Key": ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef},
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef(
    _ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef",
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


class ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef(
    _ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef",
    {"Key": ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef},
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef
):
    pass


_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef",
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


class ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef
):
    """
    - *(dict) --*

      A container for specifying the configuration for publication of messages to an Amazon Simple
      Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.
    """


_ClientGetBucketNotificationConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTypeDef",
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


class ClientGetBucketNotificationConfigurationResponseTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      A container for specifying the notification configuration of the bucket. If this element is
      empty, notifications are turned off for the bucket.
      - **TopicConfigurations** *(list) --*

        The topic to which notifications are sent and the events for which notifications are
        generated.
        - *(dict) --*

          A container for specifying the configuration for publication of messages to an Amazon
          Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
          - **Id** *(string) --*

            An optional unique identifier for configurations in a notification configuration. If you
            don't provide one, Amazon S3 will assign an ID.
    """


_ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef = TypedDict(
    "_ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef",
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


class ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef(
    _ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef
):
    pass


_ClientGetBucketNotificationResponseQueueConfigurationTypeDef = TypedDict(
    "_ClientGetBucketNotificationResponseQueueConfigurationTypeDef",
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


class ClientGetBucketNotificationResponseQueueConfigurationTypeDef(
    _ClientGetBucketNotificationResponseQueueConfigurationTypeDef
):
    pass


_ClientGetBucketNotificationResponseTopicConfigurationTypeDef = TypedDict(
    "_ClientGetBucketNotificationResponseTopicConfigurationTypeDef",
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


class ClientGetBucketNotificationResponseTopicConfigurationTypeDef(
    _ClientGetBucketNotificationResponseTopicConfigurationTypeDef
):
    """
    - **TopicConfiguration** *(dict) --*

      This data type is deprecated. A container for specifying the configuration for publication of
      messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects
      specified events.
      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.
    """


_ClientGetBucketNotificationResponseTypeDef = TypedDict(
    "_ClientGetBucketNotificationResponseTypeDef",
    {
        "TopicConfiguration": ClientGetBucketNotificationResponseTopicConfigurationTypeDef,
        "QueueConfiguration": ClientGetBucketNotificationResponseQueueConfigurationTypeDef,
        "CloudFunctionConfiguration": ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetBucketNotificationResponseTypeDef(_ClientGetBucketNotificationResponseTypeDef):
    """
    - *(dict) --*

      - **TopicConfiguration** *(dict) --*

        This data type is deprecated. A container for specifying the configuration for publication
        of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3
        detects specified events.
        - **Id** *(string) --*

          An optional unique identifier for configurations in a notification configuration. If you
          don't provide one, Amazon S3 will assign an ID.
    """


_ClientGetBucketPolicyResponseTypeDef = TypedDict(
    "_ClientGetBucketPolicyResponseTypeDef", {"Policy": str}, total=False
)


class ClientGetBucketPolicyResponseTypeDef(_ClientGetBucketPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(string) --*

        The bucket policy as a JSON document.
    """


_ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef = TypedDict(
    "_ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef", {"IsPublic": bool}, total=False
)


class ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef(
    _ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef
):
    """
    - **PolicyStatus** *(dict) --*

      The policy status for the specified bucket.
      - **IsPublic** *(boolean) --*

        The policy status for this bucket. ``TRUE`` indicates that this bucket is public. ``FALSE``
        indicates that the bucket is not public.
    """


_ClientGetBucketPolicyStatusResponseTypeDef = TypedDict(
    "_ClientGetBucketPolicyStatusResponseTypeDef",
    {"PolicyStatus": ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef},
    total=False,
)


class ClientGetBucketPolicyStatusResponseTypeDef(_ClientGetBucketPolicyStatusResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyStatus** *(dict) --*

        The policy status for the specified bucket.
        - **IsPublic** *(boolean) --*

          The policy status for this bucket. ``TRUE`` indicates that this bucket is public.
          ``FALSE`` indicates that the bucket is not public.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    {"Owner": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    {"ReplicaKmsKeyID": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    {"Minutes": int},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "EventThreshold": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef,
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    {"Minutes": int},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "Time": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef,
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef",
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


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef,
        "And": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef",
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


class ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef
):
    pass


_ClientGetBucketReplicationResponseReplicationConfigurationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": List[ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef],
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationTypeDef
):
    """
    - **ReplicationConfiguration** *(dict) --*

      A container for replication rules. You can add up to 1,000 rules. The maximum size of a
      replication configuration is 2 MB.
      - **Role** *(string) --*

        The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
        Amazon S3 assumes when replicating objects. For more information, see `How to Set Up
        Replication <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html>`__
        in the *Amazon Simple Storage Service Developer Guide* .
    """


_ClientGetBucketReplicationResponseTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseTypeDef",
    {"ReplicationConfiguration": ClientGetBucketReplicationResponseReplicationConfigurationTypeDef},
    total=False,
)


class ClientGetBucketReplicationResponseTypeDef(_ClientGetBucketReplicationResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationConfiguration** *(dict) --*

        A container for replication rules. You can add up to 1,000 rules. The maximum size of a
        replication configuration is 2 MB.
        - **Role** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
          Amazon S3 assumes when replicating objects. For more information, see `How to Set Up
          Replication
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html>`__ in the
          *Amazon Simple Storage Service Developer Guide* .
    """


_ClientGetBucketRequestPaymentResponseTypeDef = TypedDict(
    "_ClientGetBucketRequestPaymentResponseTypeDef",
    {"Payer": Literal["Requester", "BucketOwner"]},
    total=False,
)


class ClientGetBucketRequestPaymentResponseTypeDef(_ClientGetBucketRequestPaymentResponseTypeDef):
    """
    - *(dict) --*

      - **Payer** *(string) --*

        Specifies who pays for the download and request fees.
    """


_ClientGetBucketTaggingResponseTagSetTypeDef = TypedDict(
    "_ClientGetBucketTaggingResponseTagSetTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetBucketTaggingResponseTagSetTypeDef(_ClientGetBucketTaggingResponseTagSetTypeDef):
    """
    - *(dict) --*

      A container of a key value name pair.
      - **Key** *(string) --*

        Name of the tag.
    """


_ClientGetBucketTaggingResponseTypeDef = TypedDict(
    "_ClientGetBucketTaggingResponseTypeDef",
    {"TagSet": List[ClientGetBucketTaggingResponseTagSetTypeDef]},
    total=False,
)


class ClientGetBucketTaggingResponseTypeDef(_ClientGetBucketTaggingResponseTypeDef):
    """
    - *(dict) --*

      - **TagSet** *(list) --*

        Contains the tag set.
        - *(dict) --*

          A container of a key value name pair.
          - **Key** *(string) --*

            Name of the tag.
    """


_ClientGetBucketVersioningResponseTypeDef = TypedDict(
    "_ClientGetBucketVersioningResponseTypeDef",
    {"Status": Literal["Enabled", "Suspended"], "MFADelete": Literal["Enabled", "Disabled"]},
    total=False,
)


class ClientGetBucketVersioningResponseTypeDef(_ClientGetBucketVersioningResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The versioning state of the bucket.
    """


_ClientGetBucketWebsiteResponseErrorDocumentTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseErrorDocumentTypeDef", {"Key": str}, total=False
)


class ClientGetBucketWebsiteResponseErrorDocumentTypeDef(
    _ClientGetBucketWebsiteResponseErrorDocumentTypeDef
):
    pass


_ClientGetBucketWebsiteResponseIndexDocumentTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseIndexDocumentTypeDef", {"Suffix": str}, total=False
)


class ClientGetBucketWebsiteResponseIndexDocumentTypeDef(
    _ClientGetBucketWebsiteResponseIndexDocumentTypeDef
):
    pass


_ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": Literal["http", "https"]},
    total=False,
)


class ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef(
    _ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef
):
    """
    - **RedirectAllRequestsTo** *(dict) --*

      Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.
      - **HostName** *(string) --*

        Name of the host where requests are redirected.
    """


_ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)


class ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef(
    _ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef
):
    pass


_ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)


class ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef(
    _ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef
):
    pass


_ClientGetBucketWebsiteResponseRoutingRulesTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseRoutingRulesTypeDef",
    {
        "Condition": ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef,
        "Redirect": ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef,
    },
    total=False,
)


class ClientGetBucketWebsiteResponseRoutingRulesTypeDef(
    _ClientGetBucketWebsiteResponseRoutingRulesTypeDef
):
    pass


_ClientGetBucketWebsiteResponseTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseTypeDef",
    {
        "RedirectAllRequestsTo": ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef,
        "IndexDocument": ClientGetBucketWebsiteResponseIndexDocumentTypeDef,
        "ErrorDocument": ClientGetBucketWebsiteResponseErrorDocumentTypeDef,
        "RoutingRules": List[ClientGetBucketWebsiteResponseRoutingRulesTypeDef],
    },
    total=False,
)


class ClientGetBucketWebsiteResponseTypeDef(_ClientGetBucketWebsiteResponseTypeDef):
    """
    - *(dict) --*

      - **RedirectAllRequestsTo** *(dict) --*

        Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3
        bucket.
        - **HostName** *(string) --*

          Name of the host where requests are redirected.
    """


_ClientGetObjectAclResponseGrantsGranteeTypeDef = TypedDict(
    "_ClientGetObjectAclResponseGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ClientGetObjectAclResponseGrantsGranteeTypeDef(
    _ClientGetObjectAclResponseGrantsGranteeTypeDef
):
    pass


_ClientGetObjectAclResponseGrantsTypeDef = TypedDict(
    "_ClientGetObjectAclResponseGrantsTypeDef",
    {
        "Grantee": ClientGetObjectAclResponseGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ClientGetObjectAclResponseGrantsTypeDef(_ClientGetObjectAclResponseGrantsTypeDef):
    pass


_ClientGetObjectAclResponseOwnerTypeDef = TypedDict(
    "_ClientGetObjectAclResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ClientGetObjectAclResponseOwnerTypeDef(_ClientGetObjectAclResponseOwnerTypeDef):
    """
    - **Owner** *(dict) --*

      Container for the bucket owner's display name and ID.
      - **DisplayName** *(string) --*

        Container for the display name of the owner.
    """


_ClientGetObjectAclResponseTypeDef = TypedDict(
    "_ClientGetObjectAclResponseTypeDef",
    {
        "Owner": ClientGetObjectAclResponseOwnerTypeDef,
        "Grants": List[ClientGetObjectAclResponseGrantsTypeDef],
        "RequestCharged": str,
    },
    total=False,
)


class ClientGetObjectAclResponseTypeDef(_ClientGetObjectAclResponseTypeDef):
    """
    - *(dict) --*

      - **Owner** *(dict) --*

        Container for the bucket owner's display name and ID.
        - **DisplayName** *(string) --*

          Container for the display name of the owner.
    """


_ClientGetObjectLegalHoldResponseLegalHoldTypeDef = TypedDict(
    "_ClientGetObjectLegalHoldResponseLegalHoldTypeDef",
    {"Status": Literal["ON", "OFF"]},
    total=False,
)


class ClientGetObjectLegalHoldResponseLegalHoldTypeDef(
    _ClientGetObjectLegalHoldResponseLegalHoldTypeDef
):
    """
    - **LegalHold** *(dict) --*

      The current Legal Hold status for the specified object.
      - **Status** *(string) --*

        Indicates whether the specified object has a Legal Hold in place.
    """


_ClientGetObjectLegalHoldResponseTypeDef = TypedDict(
    "_ClientGetObjectLegalHoldResponseTypeDef",
    {"LegalHold": ClientGetObjectLegalHoldResponseLegalHoldTypeDef},
    total=False,
)


class ClientGetObjectLegalHoldResponseTypeDef(_ClientGetObjectLegalHoldResponseTypeDef):
    """
    - *(dict) --*

      - **LegalHold** *(dict) --*

        The current Legal Hold status for the specified object.
        - **Status** *(string) --*

          Indicates whether the specified object has a Legal Hold in place.
    """


_ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef = TypedDict(
    "_ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "Days": int, "Years": int},
    total=False,
)


class ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef(
    _ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef
):
    pass


_ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef = TypedDict(
    "_ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef",
    {
        "DefaultRetention": ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef
    },
    total=False,
)


class ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef(
    _ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef
):
    pass


_ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef = TypedDict(
    "_ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef,
    },
    total=False,
)


class ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef(
    _ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef
):
    """
    - **ObjectLockConfiguration** *(dict) --*

      The specified bucket's Object Lock configuration.
      - **ObjectLockEnabled** *(string) --*

        Indicates whether this bucket has an Object Lock configuration enabled.
    """


_ClientGetObjectLockConfigurationResponseTypeDef = TypedDict(
    "_ClientGetObjectLockConfigurationResponseTypeDef",
    {
        "ObjectLockConfiguration": ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef
    },
    total=False,
)


class ClientGetObjectLockConfigurationResponseTypeDef(
    _ClientGetObjectLockConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **ObjectLockConfiguration** *(dict) --*

        The specified bucket's Object Lock configuration.
        - **ObjectLockEnabled** *(string) --*

          Indicates whether this bucket has an Object Lock configuration enabled.
    """


_ClientGetObjectResponseTypeDef = TypedDict(
    "_ClientGetObjectResponseTypeDef",
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


class ClientGetObjectResponseTypeDef(_ClientGetObjectResponseTypeDef):
    """
    - *(dict) --*

      - **Body** (:class:`.StreamingBody`) --

        Object data.
    """


_ClientGetObjectRetentionResponseRetentionTypeDef = TypedDict(
    "_ClientGetObjectRetentionResponseRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "RetainUntilDate": datetime},
    total=False,
)


class ClientGetObjectRetentionResponseRetentionTypeDef(
    _ClientGetObjectRetentionResponseRetentionTypeDef
):
    """
    - **Retention** *(dict) --*

      The container element for an object's retention settings.
      - **Mode** *(string) --*

        Indicates the Retention mode for the specified object.
    """


_ClientGetObjectRetentionResponseTypeDef = TypedDict(
    "_ClientGetObjectRetentionResponseTypeDef",
    {"Retention": ClientGetObjectRetentionResponseRetentionTypeDef},
    total=False,
)


class ClientGetObjectRetentionResponseTypeDef(_ClientGetObjectRetentionResponseTypeDef):
    """
    - *(dict) --*

      - **Retention** *(dict) --*

        The container element for an object's retention settings.
        - **Mode** *(string) --*

          Indicates the Retention mode for the specified object.
    """


_ClientGetObjectTaggingResponseTagSetTypeDef = TypedDict(
    "_ClientGetObjectTaggingResponseTagSetTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetObjectTaggingResponseTagSetTypeDef(_ClientGetObjectTaggingResponseTagSetTypeDef):
    pass


_ClientGetObjectTaggingResponseTypeDef = TypedDict(
    "_ClientGetObjectTaggingResponseTypeDef",
    {"VersionId": str, "TagSet": List[ClientGetObjectTaggingResponseTagSetTypeDef]},
    total=False,
)


class ClientGetObjectTaggingResponseTypeDef(_ClientGetObjectTaggingResponseTypeDef):
    """
    - *(dict) --*

      - **VersionId** *(string) --*

        The versionId of the object for which you got the tagging information.
    """


_ClientGetObjectTorrentResponseTypeDef = TypedDict(
    "_ClientGetObjectTorrentResponseTypeDef",
    {"Body": StreamingBody, "RequestCharged": str},
    total=False,
)


class ClientGetObjectTorrentResponseTypeDef(_ClientGetObjectTorrentResponseTypeDef):
    """
    - *(dict) --*

      - **Body** (:class:`.StreamingBody`) --

        A Bencoded dictionary as defined by the BitTorrent specification
    """


_ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef = TypedDict(
    "_ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)


class ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef(
    _ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
):
    """
    - **PublicAccessBlockConfiguration** *(dict) --*

      The ``PublicAccessBlock`` configuration currently in effect for this Amazon S3 bucket.
      - **BlockPublicAcls** *(boolean) --*

        Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket
        and objects in this bucket. Setting this element to ``TRUE`` causes the following behavior:
        * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
        * PUT Object calls fail if the request includes a public ACL.
        * PUT Bucket calls fail if the request includes a public ACL.
        Enabling this setting doesn't affect existing policies or ACLs.
    """


_ClientGetPublicAccessBlockResponseTypeDef = TypedDict(
    "_ClientGetPublicAccessBlockResponseTypeDef",
    {
        "PublicAccessBlockConfiguration": ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
    },
    total=False,
)


class ClientGetPublicAccessBlockResponseTypeDef(_ClientGetPublicAccessBlockResponseTypeDef):
    """
    - *(dict) --*

      - **PublicAccessBlockConfiguration** *(dict) --*

        The ``PublicAccessBlock`` configuration currently in effect for this Amazon S3 bucket.
        - **BlockPublicAcls** *(boolean) --*

          Specifies whether Amazon S3 should block public access control lists (ACLs) for this
          bucket and objects in this bucket. Setting this element to ``TRUE`` causes the following
          behavior:
          * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
          * PUT Object calls fail if the request includes a public ACL.
          * PUT Bucket calls fail if the request includes a public ACL.
          Enabling this setting doesn't affect existing policies or ACLs.
    """


_ClientHeadObjectResponseTypeDef = TypedDict(
    "_ClientHeadObjectResponseTypeDef",
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


class ClientHeadObjectResponseTypeDef(_ClientHeadObjectResponseTypeDef):
    """
    - *(dict) --*

      - **DeleteMarker** *(boolean) --*

        Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
        false, this response header does not appear in the response.
    """


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef,
        "And": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef,
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef",
    {
        "Id": str,
        "Filter": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef,
        "StorageClassAnalysis": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef,
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef
):
    pass


_ClientListBucketAnalyticsConfigurationsResponseTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseTypeDef",
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


class ClientListBucketAnalyticsConfigurationsResponseTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **IsTruncated** *(boolean) --*

        Indicates whether the returned list of analytics configurations is complete. A value of true
        indicates that the list is not complete and the NextContinuationToken will be provided for a
        subsequent request.
    """


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef
):
    pass


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef
):
    pass


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef
):
    pass


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef",
    {
        "S3BucketDestination": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef
):
    pass


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef",
    {"Prefix": str},
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef
):
    pass


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef
):
    pass


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef",
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


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef
):
    pass


_ClientListBucketInventoryConfigurationsResponseTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseTypeDef",
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


class ClientListBucketInventoryConfigurationsResponseTypeDef(
    _ClientListBucketInventoryConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **ContinuationToken** *(string) --*

        If sent in the request, the marker that is used as a starting point for this inventory
        configuration list response.
    """


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef
):
    pass


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef
):
    pass


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef
):
    pass


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef,
        "And": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef,
    },
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef
):
    pass


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef",
    {
        "Id": str,
        "Filter": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef,
    },
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef
):
    pass


_ClientListBucketMetricsConfigurationsResponseTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseTypeDef",
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


class ClientListBucketMetricsConfigurationsResponseTypeDef(
    _ClientListBucketMetricsConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **IsTruncated** *(boolean) --*

        Indicates whether the returned list of metrics configurations is complete. A value of true
        indicates that the list is not complete and the NextContinuationToken will be provided for a
        subsequent request.
    """


_ClientListBucketsResponseBucketsTypeDef = TypedDict(
    "_ClientListBucketsResponseBucketsTypeDef", {"Name": str, "CreationDate": datetime}, total=False
)


class ClientListBucketsResponseBucketsTypeDef(_ClientListBucketsResponseBucketsTypeDef):
    """
    - *(dict) --*

      In terms of implementation, a Bucket is a resource. An Amazon S3 bucket name is globally
      unique, and the namespace is shared by all AWS accounts.
      - **Name** *(string) --*

        The name of the bucket.
    """


_ClientListBucketsResponseOwnerTypeDef = TypedDict(
    "_ClientListBucketsResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ClientListBucketsResponseOwnerTypeDef(_ClientListBucketsResponseOwnerTypeDef):
    pass


_ClientListBucketsResponseTypeDef = TypedDict(
    "_ClientListBucketsResponseTypeDef",
    {
        "Buckets": List[ClientListBucketsResponseBucketsTypeDef],
        "Owner": ClientListBucketsResponseOwnerTypeDef,
    },
    total=False,
)


class ClientListBucketsResponseTypeDef(_ClientListBucketsResponseTypeDef):
    """
    - *(dict) --*

      - **Buckets** *(list) --*

        The list of buckets owned by the requestor.
        - *(dict) --*

          In terms of implementation, a Bucket is a resource. An Amazon S3 bucket name is globally
          unique, and the namespace is shared by all AWS accounts.
          - **Name** *(string) --*

            The name of the bucket.
    """


_ClientListMultipartUploadsResponseCommonPrefixesTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ClientListMultipartUploadsResponseCommonPrefixesTypeDef(
    _ClientListMultipartUploadsResponseCommonPrefixesTypeDef
):
    pass


_ClientListMultipartUploadsResponseUploadsInitiatorTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseUploadsInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ClientListMultipartUploadsResponseUploadsInitiatorTypeDef(
    _ClientListMultipartUploadsResponseUploadsInitiatorTypeDef
):
    pass


_ClientListMultipartUploadsResponseUploadsOwnerTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseUploadsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListMultipartUploadsResponseUploadsOwnerTypeDef(
    _ClientListMultipartUploadsResponseUploadsOwnerTypeDef
):
    pass


_ClientListMultipartUploadsResponseUploadsTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseUploadsTypeDef",
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


class ClientListMultipartUploadsResponseUploadsTypeDef(
    _ClientListMultipartUploadsResponseUploadsTypeDef
):
    pass


_ClientListMultipartUploadsResponseTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseTypeDef",
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


class ClientListMultipartUploadsResponseTypeDef(_ClientListMultipartUploadsResponseTypeDef):
    """
    - *(dict) --*

      - **Bucket** *(string) --*

        Name of the bucket to which the multipart upload was initiated.
    """


_ClientListObjectVersionsResponseCommonPrefixesTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ClientListObjectVersionsResponseCommonPrefixesTypeDef(
    _ClientListObjectVersionsResponseCommonPrefixesTypeDef
):
    pass


_ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef(
    _ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef
):
    pass


_ClientListObjectVersionsResponseDeleteMarkersTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseDeleteMarkersTypeDef",
    {
        "Owner": ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)


class ClientListObjectVersionsResponseDeleteMarkersTypeDef(
    _ClientListObjectVersionsResponseDeleteMarkersTypeDef
):
    pass


_ClientListObjectVersionsResponseVersionsOwnerTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseVersionsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListObjectVersionsResponseVersionsOwnerTypeDef(
    _ClientListObjectVersionsResponseVersionsOwnerTypeDef
):
    pass


_ClientListObjectVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseVersionsTypeDef",
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


class ClientListObjectVersionsResponseVersionsTypeDef(
    _ClientListObjectVersionsResponseVersionsTypeDef
):
    pass


_ClientListObjectVersionsResponseTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseTypeDef",
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


class ClientListObjectVersionsResponseTypeDef(_ClientListObjectVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether Amazon S3 returned all of the results that satisfied the
        search criteria. If your results were truncated, you can make a follow-up paginated request
        using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in
        another request to return the rest of the results.
    """


_ClientListObjectsResponseCommonPrefixesTypeDef = TypedDict(
    "_ClientListObjectsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ClientListObjectsResponseCommonPrefixesTypeDef(
    _ClientListObjectsResponseCommonPrefixesTypeDef
):
    pass


_ClientListObjectsResponseContentsOwnerTypeDef = TypedDict(
    "_ClientListObjectsResponseContentsOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ClientListObjectsResponseContentsOwnerTypeDef(_ClientListObjectsResponseContentsOwnerTypeDef):
    pass


_ClientListObjectsResponseContentsTypeDef = TypedDict(
    "_ClientListObjectsResponseContentsTypeDef",
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


class ClientListObjectsResponseContentsTypeDef(_ClientListObjectsResponseContentsTypeDef):
    pass


_ClientListObjectsResponseTypeDef = TypedDict(
    "_ClientListObjectsResponseTypeDef",
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


class ClientListObjectsResponseTypeDef(_ClientListObjectsResponseTypeDef):
    """
    - *(dict) --*

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether Amazon S3 returned all of the results that satisfied the
        search criteria.
    """


_ClientListObjectsV2ResponseCommonPrefixesTypeDef = TypedDict(
    "_ClientListObjectsV2ResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ClientListObjectsV2ResponseCommonPrefixesTypeDef(
    _ClientListObjectsV2ResponseCommonPrefixesTypeDef
):
    pass


_ClientListObjectsV2ResponseContentsOwnerTypeDef = TypedDict(
    "_ClientListObjectsV2ResponseContentsOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ClientListObjectsV2ResponseContentsOwnerTypeDef(
    _ClientListObjectsV2ResponseContentsOwnerTypeDef
):
    pass


_ClientListObjectsV2ResponseContentsTypeDef = TypedDict(
    "_ClientListObjectsV2ResponseContentsTypeDef",
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


class ClientListObjectsV2ResponseContentsTypeDef(_ClientListObjectsV2ResponseContentsTypeDef):
    pass


_ClientListObjectsV2ResponseTypeDef = TypedDict(
    "_ClientListObjectsV2ResponseTypeDef",
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


class ClientListObjectsV2ResponseTypeDef(_ClientListObjectsV2ResponseTypeDef):
    """
    - *(dict) --*

      - **IsTruncated** *(boolean) --*

        Set to false if all of the results were returned. Set to true if more keys are available to
        return. If the number of results exceeds that specified by MaxKeys, all of the results might
        not be returned.
    """


_ClientListPartsResponseInitiatorTypeDef = TypedDict(
    "_ClientListPartsResponseInitiatorTypeDef", {"ID": str, "DisplayName": str}, total=False
)


class ClientListPartsResponseInitiatorTypeDef(_ClientListPartsResponseInitiatorTypeDef):
    pass


_ClientListPartsResponseOwnerTypeDef = TypedDict(
    "_ClientListPartsResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ClientListPartsResponseOwnerTypeDef(_ClientListPartsResponseOwnerTypeDef):
    pass


_ClientListPartsResponsePartsTypeDef = TypedDict(
    "_ClientListPartsResponsePartsTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)


class ClientListPartsResponsePartsTypeDef(_ClientListPartsResponsePartsTypeDef):
    pass


_ClientListPartsResponseTypeDef = TypedDict(
    "_ClientListPartsResponseTypeDef",
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


class ClientListPartsResponseTypeDef(_ClientListPartsResponseTypeDef):
    """
    - *(dict) --*

      - **AbortDate** *(datetime) --*

        If the bucket has a lifecycle rule configured with an action to abort incomplete multipart
        uploads and the prefix in the lifecycle rule matches the object name in the request, then
        the response includes this header indicating when the initiated multipart upload will become
        eligible for abort operation. For more information, see `Aborting Incomplete Multipart
        Uploads Using a Bucket Lifecycle Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
        .
        The response will also include the ``x-amz-abort-rule-id`` header that will provide the ID
        of the lifecycle configuration rule that defines this action.
    """


_ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef = TypedDict(
    "_ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef",
    {"Status": Literal["Enabled", "Suspended"]},
    total=False,
)


class ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef(
    _ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef
):
    """
    Container for setting the transfer acceleration state.
    - **Status** *(string) --*

      Specifies the transfer acceleration status of the bucket.
    """


_ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef(
    _ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef
):
    """
    - **Grantee** *(dict) --*

      The person being granted permissions.
      - **DisplayName** *(string) --*

        Screen name of the grantee.
    """


_ClientPutBucketAclAccessControlPolicyGrantsTypeDef = TypedDict(
    "_ClientPutBucketAclAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ClientPutBucketAclAccessControlPolicyGrantsTypeDef(
    _ClientPutBucketAclAccessControlPolicyGrantsTypeDef
):
    """
    - *(dict) --*

      Container for grant information.
      - **Grantee** *(dict) --*

        The person being granted permissions.
        - **DisplayName** *(string) --*

          Screen name of the grantee.
    """


_ClientPutBucketAclAccessControlPolicyOwnerTypeDef = TypedDict(
    "_ClientPutBucketAclAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientPutBucketAclAccessControlPolicyOwnerTypeDef(
    _ClientPutBucketAclAccessControlPolicyOwnerTypeDef
):
    pass


_ClientPutBucketAclAccessControlPolicyTypeDef = TypedDict(
    "_ClientPutBucketAclAccessControlPolicyTypeDef",
    {
        "Grants": List[ClientPutBucketAclAccessControlPolicyGrantsTypeDef],
        "Owner": ClientPutBucketAclAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)


class ClientPutBucketAclAccessControlPolicyTypeDef(_ClientPutBucketAclAccessControlPolicyTypeDef):
    """
    Contains the elements that set the ACL permissions for an object per grantee.
    - **Grants** *(list) --*

      A list of grants.
      - *(dict) --*

        Container for grant information.
        - **Grantee** *(dict) --*

          The person being granted permissions.
          - **DisplayName** *(string) --*

            Screen name of the grantee.
    """


_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef = TypedDict(
    "_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef(
    _ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef
):
    pass


_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef = TypedDict(
    "_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef(
    _ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef
):
    pass


_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef = TypedDict(
    "_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef(
    _ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef
):
    pass


_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef = TypedDict(
    "_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef,
        "And": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef,
    },
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef(
    _ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef
):
    pass


_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef(
    _ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
):
    pass


_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef(
    _ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef
):
    pass


_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef = TypedDict(
    "_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef(
    _ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
):
    pass


_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef = TypedDict(
    "_ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef(
    _ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef
):
    pass


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
    """
    The configuration and any analyses for the analytics filter.
    - **Id** *(string) --***[REQUIRED]**

      The ID that identifies the analytics configuration.
    """


_ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef = TypedDict(
    "_ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)


class ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef(
    _ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef
):
    """
    - *(dict) --*

      Specifies a cross-origin access rule for an Amazon S3 bucket.
      - **AllowedHeaders** *(list) --*

        Headers that are specified in the ``Access-Control-Request-Headers`` header. These headers
        are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request,
        Amazon S3 returns any requested headers that are allowed.
        - *(string) --*
    """


_ClientPutBucketCorsCORSConfigurationTypeDef = TypedDict(
    "_ClientPutBucketCorsCORSConfigurationTypeDef",
    {"CORSRules": List[ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef]},
)


class ClientPutBucketCorsCORSConfigurationTypeDef(_ClientPutBucketCorsCORSConfigurationTypeDef):
    """
    Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more
    information, see `Enabling Cross-Origin Resource Sharing
    <https://docs.aws.amazon.com/AmazonS3/latest/dev//cors.html>`__ in the *Amazon Simple Storage
    Service Developer Guide* .
    - **CORSRules** *(list) --***[REQUIRED]**

      A set of origins and methods (cross-origin access that you want to allow). You can add up to
      100 rules to the configuration.
      - *(dict) --*

        Specifies a cross-origin access rule for an Amazon S3 bucket.
        - **AllowedHeaders** *(list) --*

          Headers that are specified in the ``Access-Control-Request-Headers`` header. These headers
          are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request,
          Amazon S3 returns any requested headers that are allowed.
          - *(string) --*
    """


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
    """
    - **ApplyServerSideEncryptionByDefault** *(dict) --*

      Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT
      Object request doesn't specify any server-side encryption, this default encryption will be
      applied.
      - **SSEAlgorithm** *(string) --***[REQUIRED]**

        Server-side encryption algorithm to use for the default encryption.
    """


_ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef = TypedDict(
    "_ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
    },
    total=False,
)


class ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef(
    _ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef
):
    """
    - *(dict) --*

      Specifies the default server-side encryption configuration.
      - **ApplyServerSideEncryptionByDefault** *(dict) --*

        Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT
        Object request doesn't specify any server-side encryption, this default encryption will be
        applied.
        - **SSEAlgorithm** *(string) --***[REQUIRED]**

          Server-side encryption algorithm to use for the default encryption.
    """


_ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef = TypedDict(
    "_ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef",
    {"Rules": List[ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef]},
)


class ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef(
    _ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef
):
    """
    Specifies the default server-side-encryption configuration.
    - **Rules** *(list) --***[REQUIRED]**

      Container for information about a particular server-side encryption configuration rule.
      - *(dict) --*

        Specifies the default server-side encryption configuration.
        - **ApplyServerSideEncryptionByDefault** *(dict) --*

          Specifies the default server-side encryption to apply to new objects in the bucket. If a
          PUT Object request doesn't specify any server-side encryption, this default encryption
          will be applied.
          - **SSEAlgorithm** *(string) --***[REQUIRED]**

            Server-side encryption algorithm to use for the default encryption.
    """


_ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "_ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)


class ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef(
    _ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef
):
    pass


_ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "_ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)


class ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef(
    _ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef
):
    pass


_ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)


class ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef(
    _ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef
):
    """
    - **S3BucketDestination** *(dict) --***[REQUIRED]**

      Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
      inventory results are published.
      - **AccountId** *(string) --*

        The ID of the account that owns the destination bucket.
    """


_ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef = TypedDict(
    "_ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef",
    {
        "S3BucketDestination": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef
    },
)


class ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef(
    _ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef
):
    """
    - **Destination** *(dict) --***[REQUIRED]**

      Contains information about where to publish the inventory results.
      - **S3BucketDestination** *(dict) --***[REQUIRED]**

        Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
        inventory results are published.
        - **AccountId** *(string) --*

          The ID of the account that owns the destination bucket.
    """


_ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef = TypedDict(
    "_ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef",
    {"Prefix": str},
    total=False,
)


class ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef(
    _ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef
):
    pass


_ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef = TypedDict(
    "_ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)


class ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef(
    _ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef
):
    pass


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
    """
    Specifies the inventory configuration.
    - **Destination** *(dict) --***[REQUIRED]**

      Contains information about where to publish the inventory results.
      - **S3BucketDestination** *(dict) --***[REQUIRED]**

        Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
        inventory results are published.
        - **AccountId** *(string) --*

          The ID of the account that owns the destination bucket.
    """


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef
):
    pass


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef
):
    """
    - **Expiration** *(dict) --*

      Specifies the expiration for the lifecycle of the object in the form of date, days and,
      whether the object has a delete marker.
      - **Date** *(datetime) --*

        Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
        Format.
    """


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef
):
    pass


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef
):
    pass


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef
):
    pass


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef,
        "And": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef
):
    pass


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef
):
    pass


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef
):
    pass


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef
):
    pass


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef",
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


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef
):
    """
    - *(dict) --*

      A lifecycle rule for individual objects in an Amazon S3 bucket.
      - **Expiration** *(dict) --*

        Specifies the expiration for the lifecycle of the object in the form of date, days and,
        whether the object has a delete marker.
        - **Date** *(datetime) --*

          Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
          Format.
    """


_ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef = TypedDict(
    "_ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef",
    {"Rules": List[ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef]},
)


class ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef(
    _ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef
):
    """
    Container for lifecycle rules. You can add as many as 1,000 rules.
    - **Rules** *(list) --***[REQUIRED]**

      A lifecycle rule for individual objects in an Amazon S3 bucket.
      - *(dict) --*

        A lifecycle rule for individual objects in an Amazon S3 bucket.
        - **Expiration** *(dict) --*

          Specifies the expiration for the lifecycle of the object in the form of date, days and,
          whether the object has a delete marker.
          - **Date** *(datetime) --*

            Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
            Format.
    """


_ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "_ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)


class ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef(
    _ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef
):
    pass


_ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "_ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)


class ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef(
    _ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef
):
    """
    - **Expiration** *(dict) --*

      Specifies the expiration for the lifecycle of the object.
      - **Date** *(datetime) --*

        Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
        Format.
    """


_ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "_ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)


class ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef(
    _ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef
):
    pass


_ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "_ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef(
    _ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef
):
    pass


_ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef = TypedDict(
    "_ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)


class ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef(
    _ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef
):
    pass


_ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef = TypedDict(
    "_ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef",
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


class ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef(
    _ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef
):
    """
    - *(dict) --*

      Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
      lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__ in
      the *Amazon Simple Storage Service API Reference* .
      - **Expiration** *(dict) --*

        Specifies the expiration for the lifecycle of the object.
        - **Date** *(datetime) --*

          Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
          Format.
    """


_ClientPutBucketLifecycleLifecycleConfigurationTypeDef = TypedDict(
    "_ClientPutBucketLifecycleLifecycleConfigurationTypeDef",
    {"Rules": List[ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef]},
)


class ClientPutBucketLifecycleLifecycleConfigurationTypeDef(
    _ClientPutBucketLifecycleLifecycleConfigurationTypeDef
):
    """
    - **Rules** *(list) --***[REQUIRED]**

      Specifies lifecycle configuration rules for an Amazon S3 bucket.
      - *(dict) --*

        Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
        lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__
        in the *Amazon Simple Storage Service API Reference* .
        - **Expiration** *(dict) --*

          Specifies the expiration for the lifecycle of the object.
          - **Date** *(datetime) --*

            Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
            Format.
    """


_ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "_ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef(
    _ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef
):
    pass


_ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "_ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE"],
    },
    total=False,
)


class ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef(
    _ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef
):
    pass


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
    """
    - **LoggingEnabled** *(dict) --*

      Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys
      for a bucket. For more information, see `PUT Bucket logging
      <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html>`__ in the *Amazon
      Simple Storage Service API Reference* .
      - **TargetBucket** *(string) --***[REQUIRED]**

        Specifies the bucket where you want Amazon S3 to store server access logs. You can have your
        logs delivered to any bucket that you own, including the same bucket that is being logged.
        You can also configure multiple buckets to deliver their logs to the same target bucket. In
        this case, you should choose a different ``TargetPrefix`` for each source bucket so that the
        delivered log files can be distinguished by key.
    """


_ClientPutBucketLoggingBucketLoggingStatusTypeDef = TypedDict(
    "_ClientPutBucketLoggingBucketLoggingStatusTypeDef",
    {"LoggingEnabled": ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef},
    total=False,
)


class ClientPutBucketLoggingBucketLoggingStatusTypeDef(
    _ClientPutBucketLoggingBucketLoggingStatusTypeDef
):
    """
    Container for logging status information.
    - **LoggingEnabled** *(dict) --*

      Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys
      for a bucket. For more information, see `PUT Bucket logging
      <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html>`__ in the *Amazon
      Simple Storage Service API Reference* .
      - **TargetBucket** *(string) --***[REQUIRED]**

        Specifies the bucket where you want Amazon S3 to store server access logs. You can have your
        logs delivered to any bucket that you own, including the same bucket that is being logged.
        You can also configure multiple buckets to deliver their logs to the same target bucket. In
        this case, you should choose a different ``TargetPrefix`` for each source bucket so that the
        delivered log files can be distinguished by key.
    """


_ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef = TypedDict(
    "_ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef(
    _ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef
):
    pass


_ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef = TypedDict(
    "_ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef],
    },
    total=False,
)


class ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef(
    _ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef
):
    pass


_ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef = TypedDict(
    "_ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef(
    _ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef
):
    pass


_ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef = TypedDict(
    "_ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef,
        "And": ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef,
    },
    total=False,
)


class ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef(
    _ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef
):
    pass


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
    """
    Specifies the metrics configuration.
    - **Id** *(string) --***[REQUIRED]**

      The ID used to identify the metrics configuration.
    """


_ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef",
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


class ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef
    },
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef",
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


class ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef
    },
    total=False,
)


class ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef
):
    pass


_ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef",
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


class ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef
):
    """
    - *(dict) --*

      A container for specifying the configuration for publication of messages to an Amazon Simple
      Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.
    """


_ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef = TypedDict(
    "_ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef",
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


class ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef(
    _ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef
):
    """
    A container for specifying the notification configuration of the bucket. If this element is
    empty, notifications are turned off for the bucket.
    - **TopicConfigurations** *(list) --*

      The topic to which notifications are sent and the events for which notifications are
      generated.
      - *(dict) --*

        A container for specifying the configuration for publication of messages to an Amazon Simple
        Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
        - **Id** *(string) --*

          An optional unique identifier for configurations in a notification configuration. If you
          don't provide one, Amazon S3 will assign an ID.
    """


_ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef = TypedDict(
    "_ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef",
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


class ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef(
    _ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef
):
    pass


_ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef = TypedDict(
    "_ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef",
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


class ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef(
    _ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef
):
    pass


_ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef = TypedDict(
    "_ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef",
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


class ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef(
    _ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef
):
    """
    - **TopicConfiguration** *(dict) --*

      This data type is deprecated. A container for specifying the configuration for publication of
      messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects
      specified events.
      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.
    """


_ClientPutBucketNotificationNotificationConfigurationTypeDef = TypedDict(
    "_ClientPutBucketNotificationNotificationConfigurationTypeDef",
    {
        "TopicConfiguration": ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef,
        "QueueConfiguration": ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef,
        "CloudFunctionConfiguration": ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef,
    },
    total=False,
)


class ClientPutBucketNotificationNotificationConfigurationTypeDef(
    _ClientPutBucketNotificationNotificationConfigurationTypeDef
):
    """
    The container for the configuration.
    - **TopicConfiguration** *(dict) --*

      This data type is deprecated. A container for specifying the configuration for publication of
      messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects
      specified events.
      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.
    """


_ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    {"Owner": str},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    {"ReplicaKmsKeyID": str},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    {"Minutes": int},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "EventThreshold": ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef,
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    {"Minutes": int},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "Time": ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef,
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef",
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


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef],
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef,
        "And": ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef
):
    pass


_ClientPutBucketReplicationReplicationConfigurationRulesTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesTypeDef",
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


class ClientPutBucketReplicationReplicationConfigurationRulesTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesTypeDef
):
    pass


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
    """
    A container for replication rules. You can add up to 1,000 rules. The maximum size of a
    replication configuration is 2 MB.
    - **Role** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
      Amazon S3 assumes when replicating objects. For more information, see `How to Set Up
      Replication <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html>`__ in
      the *Amazon Simple Storage Service Developer Guide* .
    """


_ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef = TypedDict(
    "_ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef",
    {"Payer": Literal["Requester", "BucketOwner"]},
)


class ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef(
    _ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef
):
    """
    Container for Payer.
    - **Payer** *(string) --***[REQUIRED]**

      Specifies who pays for the download and request fees.
    """


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
    """
    - *(dict) --*

      A container of a key value name pair.
      - **Key** *(string) --***[REQUIRED]**

        Name of the tag.
    """


_ClientPutBucketTaggingTaggingTypeDef = TypedDict(
    "_ClientPutBucketTaggingTaggingTypeDef",
    {"TagSet": List[ClientPutBucketTaggingTaggingTagSetTypeDef]},
)


class ClientPutBucketTaggingTaggingTypeDef(_ClientPutBucketTaggingTaggingTypeDef):
    """
    Container for the ``TagSet`` and ``Tag`` elements.
    - **TagSet** *(list) --***[REQUIRED]**

      A collection for a set of tags
      - *(dict) --*

        A container of a key value name pair.
        - **Key** *(string) --***[REQUIRED]**

          Name of the tag.
    """


_ClientPutBucketVersioningVersioningConfigurationTypeDef = TypedDict(
    "_ClientPutBucketVersioningVersioningConfigurationTypeDef",
    {"MFADelete": Literal["Enabled", "Disabled"], "Status": Literal["Enabled", "Suspended"]},
    total=False,
)


class ClientPutBucketVersioningVersioningConfigurationTypeDef(
    _ClientPutBucketVersioningVersioningConfigurationTypeDef
):
    """
    Container for setting the versioning state.
    - **MFADelete** *(string) --*

      Specifies whether MFA delete is enabled in the bucket versioning configuration. This element
      is only returned if the bucket has been configured with MFA delete. If the bucket has never
      been so configured, this element is not returned.
    """


_ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef = TypedDict(
    "_ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef", {"Key": str}
)


class ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef(
    _ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef
):
    """
    - **ErrorDocument** *(dict) --*

      The name of the error document for the website.
      - **Key** *(string) --***[REQUIRED]**

        The object key name to use when a 4XX class error occurs.
    """


_ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef = TypedDict(
    "_ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef", {"Suffix": str}, total=False
)


class ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef(
    _ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef
):
    pass


_ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef = TypedDict(
    "_ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": Literal["http", "https"]},
    total=False,
)


class ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef(
    _ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef
):
    pass


_ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef = TypedDict(
    "_ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)


class ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef(
    _ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef
):
    pass


_ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef = TypedDict(
    "_ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)


class ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef(
    _ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef
):
    pass


_ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef = TypedDict(
    "_ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef",
    {
        "Condition": ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef,
        "Redirect": ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef,
    },
    total=False,
)


class ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef(
    _ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef
):
    pass


_ClientPutBucketWebsiteWebsiteConfigurationTypeDef = TypedDict(
    "_ClientPutBucketWebsiteWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef,
        "IndexDocument": ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef,
        "RedirectAllRequestsTo": ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef,
        "RoutingRules": List[ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef],
    },
    total=False,
)


class ClientPutBucketWebsiteWebsiteConfigurationTypeDef(
    _ClientPutBucketWebsiteWebsiteConfigurationTypeDef
):
    """
    Container for the request.
    - **ErrorDocument** *(dict) --*

      The name of the error document for the website.
      - **Key** *(string) --***[REQUIRED]**

        The object key name to use when a 4XX class error occurs.
    """


_ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef(
    _ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef
):
    """
    - **Grantee** *(dict) --*

      The person being granted permissions.
      - **DisplayName** *(string) --*

        Screen name of the grantee.
    """


_ClientPutObjectAclAccessControlPolicyGrantsTypeDef = TypedDict(
    "_ClientPutObjectAclAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ClientPutObjectAclAccessControlPolicyGrantsTypeDef(
    _ClientPutObjectAclAccessControlPolicyGrantsTypeDef
):
    """
    - *(dict) --*

      Container for grant information.
      - **Grantee** *(dict) --*

        The person being granted permissions.
        - **DisplayName** *(string) --*

          Screen name of the grantee.
    """


_ClientPutObjectAclAccessControlPolicyOwnerTypeDef = TypedDict(
    "_ClientPutObjectAclAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientPutObjectAclAccessControlPolicyOwnerTypeDef(
    _ClientPutObjectAclAccessControlPolicyOwnerTypeDef
):
    pass


_ClientPutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "_ClientPutObjectAclAccessControlPolicyTypeDef",
    {
        "Grants": List[ClientPutObjectAclAccessControlPolicyGrantsTypeDef],
        "Owner": ClientPutObjectAclAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)


class ClientPutObjectAclAccessControlPolicyTypeDef(_ClientPutObjectAclAccessControlPolicyTypeDef):
    """
    Contains the elements that set the ACL permissions for an object per grantee.
    - **Grants** *(list) --*

      A list of grants.
      - *(dict) --*

        Container for grant information.
        - **Grantee** *(dict) --*

          The person being granted permissions.
          - **DisplayName** *(string) --*

            Screen name of the grantee.
    """


_ClientPutObjectAclResponseTypeDef = TypedDict(
    "_ClientPutObjectAclResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientPutObjectAclResponseTypeDef(_ClientPutObjectAclResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectLegalHoldLegalHoldTypeDef = TypedDict(
    "_ClientPutObjectLegalHoldLegalHoldTypeDef", {"Status": Literal["ON", "OFF"]}, total=False
)


class ClientPutObjectLegalHoldLegalHoldTypeDef(_ClientPutObjectLegalHoldLegalHoldTypeDef):
    """
    Container element for the Legal Hold configuration you want to apply to the specified object.
    - **Status** *(string) --*

      Indicates whether the specified object has a Legal Hold in place.
    """


_ClientPutObjectLegalHoldResponseTypeDef = TypedDict(
    "_ClientPutObjectLegalHoldResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientPutObjectLegalHoldResponseTypeDef(_ClientPutObjectLegalHoldResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef = TypedDict(
    "_ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "Days": int, "Years": int},
    total=False,
)


class ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef(
    _ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef
):
    pass


_ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef = TypedDict(
    "_ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef",
    {
        "DefaultRetention": ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef
    },
    total=False,
)


class ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef(
    _ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef
):
    pass


_ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef = TypedDict(
    "_ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef,
    },
    total=False,
)


class ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef(
    _ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef
):
    """
    The Object Lock configuration that you want to apply to the specified bucket.
    - **ObjectLockEnabled** *(string) --*

      Indicates whether this bucket has an Object Lock configuration enabled.
    """


_ClientPutObjectLockConfigurationResponseTypeDef = TypedDict(
    "_ClientPutObjectLockConfigurationResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientPutObjectLockConfigurationResponseTypeDef(
    _ClientPutObjectLockConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectResponseTypeDef = TypedDict(
    "_ClientPutObjectResponseTypeDef",
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


class ClientPutObjectResponseTypeDef(_ClientPutObjectResponseTypeDef):
    """
    - *(dict) --*

      - **Expiration** *(string) --*

        If the expiration is configured for the object (see  PutBucketLifecycleConfiguration ), the
        response includes this header. It includes the expiry-date and rule-id key-value pairs that
        provide information about object expiration. The value of the rule-id is URL encoded.
    """


_ClientPutObjectRetentionResponseTypeDef = TypedDict(
    "_ClientPutObjectRetentionResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientPutObjectRetentionResponseTypeDef(_ClientPutObjectRetentionResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectRetentionRetentionTypeDef = TypedDict(
    "_ClientPutObjectRetentionRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "RetainUntilDate": datetime},
    total=False,
)


class ClientPutObjectRetentionRetentionTypeDef(_ClientPutObjectRetentionRetentionTypeDef):
    """
    The container element for the Object Retention configuration.
    - **Mode** *(string) --*

      Indicates the Retention mode for the specified object.
    """


_ClientPutObjectTaggingResponseTypeDef = TypedDict(
    "_ClientPutObjectTaggingResponseTypeDef", {"VersionId": str}, total=False
)


class ClientPutObjectTaggingResponseTypeDef(_ClientPutObjectTaggingResponseTypeDef):
    """
    - *(dict) --*

      - **VersionId** *(string) --*

        The versionId of the object the tag-set was added to.
    """


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
    """
    - *(dict) --*

      A container of a key value name pair.
      - **Key** *(string) --***[REQUIRED]**

        Name of the tag.
    """


_ClientPutObjectTaggingTaggingTypeDef = TypedDict(
    "_ClientPutObjectTaggingTaggingTypeDef",
    {"TagSet": List[ClientPutObjectTaggingTaggingTagSetTypeDef]},
)


class ClientPutObjectTaggingTaggingTypeDef(_ClientPutObjectTaggingTaggingTypeDef):
    """
    Container for the ``TagSet`` and ``Tag`` elements
    - **TagSet** *(list) --***[REQUIRED]**

      A collection for a set of tags
      - *(dict) --*

        A container of a key value name pair.
        - **Key** *(string) --***[REQUIRED]**

          Name of the tag.
    """


_ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef = TypedDict(
    "_ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)


class ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef(
    _ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef
):
    """
    The ``PublicAccessBlock`` configuration that you want to apply to this Amazon S3 bucket. You can
    enable the configuration options in any combination. For more information about when Amazon S3
    considers a bucket or object public, see `The Meaning of "Public"
    <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`__
    in the *Amazon Simple Storage Service Developer Guide* .
    - **BlockPublicAcls** *(boolean) --*

      Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket
      and objects in this bucket. Setting this element to ``TRUE`` causes the following behavior:
      * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
      * PUT Object calls fail if the request includes a public ACL.
      * PUT Bucket calls fail if the request includes a public ACL.
      Enabling this setting doesn't affect existing policies or ACLs.
    """


_ClientRestoreObjectResponseTypeDef = TypedDict(
    "_ClientRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)


class ClientRestoreObjectResponseTypeDef(_ClientRestoreObjectResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    {"Tier": Literal["Standard", "Bulk", "Expedited"]},
    total=False,
)


class ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef(
    _ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["AES256", "aws:kms"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {"TagSet": List[ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef]},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef",
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


class ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef
):
    pass


_ClientRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
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


class ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersTypeDef
):
    pass


_ClientRestoreObjectRestoreRequestTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestTypeDef",
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


class ClientRestoreObjectRestoreRequestTypeDef(_ClientRestoreObjectRestoreRequestTypeDef):
    """
    Container for restore job parameters.
    - **Days** *(integer) --*

      Lifetime of the active copy in days. Do not use with restores that specify ``OutputLocation``
      .
    """


_ClientSelectObjectContentInputSerializationCSVTypeDef = TypedDict(
    "_ClientSelectObjectContentInputSerializationCSVTypeDef",
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


class ClientSelectObjectContentInputSerializationCSVTypeDef(
    _ClientSelectObjectContentInputSerializationCSVTypeDef
):
    """
    - **CSV** *(dict) --*

      Describes the serialization of a CSV-encoded object.
      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values are:
        * ``NONE`` : First line is not a header.
        * ``IGNORE`` : First line is a header, but you can't use the header values to indicate the
        column in an expression. You can use column position (such as _1, _2, …) to indicate the
        column (``SELECT s._1 FROM OBJECT s`` ).
        * ``Use`` : First line is a header, and you can use the header value to identify a column in
        an expression (``SELECT "name" FROM OBJECT`` ).
    """


_ClientSelectObjectContentInputSerializationJSONTypeDef = TypedDict(
    "_ClientSelectObjectContentInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)


class ClientSelectObjectContentInputSerializationJSONTypeDef(
    _ClientSelectObjectContentInputSerializationJSONTypeDef
):
    pass


_ClientSelectObjectContentInputSerializationTypeDef = TypedDict(
    "_ClientSelectObjectContentInputSerializationTypeDef",
    {
        "CSV": ClientSelectObjectContentInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ClientSelectObjectContentInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)


class ClientSelectObjectContentInputSerializationTypeDef(
    _ClientSelectObjectContentInputSerializationTypeDef
):
    """
    Describes the format of the data in the object that is being queried.
    - **CSV** *(dict) --*

      Describes the serialization of a CSV-encoded object.
      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values are:
        * ``NONE`` : First line is not a header.
        * ``IGNORE`` : First line is a header, but you can't use the header values to indicate the
        column in an expression. You can use column position (such as _1, _2, …) to indicate the
        column (``SELECT s._1 FROM OBJECT s`` ).
        * ``Use`` : First line is a header, and you can use the header value to identify a column in
        an expression (``SELECT "name" FROM OBJECT`` ).
    """


_ClientSelectObjectContentOutputSerializationCSVTypeDef = TypedDict(
    "_ClientSelectObjectContentOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientSelectObjectContentOutputSerializationCSVTypeDef(
    _ClientSelectObjectContentOutputSerializationCSVTypeDef
):
    """
    - **CSV** *(dict) --*

      Describes the serialization of CSV-encoded Select results.
      - **QuoteFields** *(string) --*

        Indicates whether to use quotation marks around output fields.
        * ``ALWAYS`` : Always use quotation marks for output fields.
        * ``ASNEEDED`` : Use quotation marks for output fields when needed.
    """


_ClientSelectObjectContentOutputSerializationJSONTypeDef = TypedDict(
    "_ClientSelectObjectContentOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)


class ClientSelectObjectContentOutputSerializationJSONTypeDef(
    _ClientSelectObjectContentOutputSerializationJSONTypeDef
):
    pass


_ClientSelectObjectContentOutputSerializationTypeDef = TypedDict(
    "_ClientSelectObjectContentOutputSerializationTypeDef",
    {
        "CSV": ClientSelectObjectContentOutputSerializationCSVTypeDef,
        "JSON": ClientSelectObjectContentOutputSerializationJSONTypeDef,
    },
    total=False,
)


class ClientSelectObjectContentOutputSerializationTypeDef(
    _ClientSelectObjectContentOutputSerializationTypeDef
):
    """
    Describes the format of the data that you want Amazon S3 to return in response.
    - **CSV** *(dict) --*

      Describes the serialization of CSV-encoded Select results.
      - **QuoteFields** *(string) --*

        Indicates whether to use quotation marks around output fields.
        * ``ALWAYS`` : Always use quotation marks for output fields.
        * ``ASNEEDED`` : Use quotation marks for output fields when needed.
    """


_ClientSelectObjectContentRequestProgressTypeDef = TypedDict(
    "_ClientSelectObjectContentRequestProgressTypeDef", {"Enabled": bool}, total=False
)


class ClientSelectObjectContentRequestProgressTypeDef(
    _ClientSelectObjectContentRequestProgressTypeDef
):
    """
    Specifies if periodic request progress information should be enabled.
    - **Enabled** *(boolean) --*

      Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE.
      Default value: FALSE.
    """


_ClientSelectObjectContentResponseTypeDef = TypedDict(
    "_ClientSelectObjectContentResponseTypeDef", {"Payload": EventStream}, total=False
)


class ClientSelectObjectContentResponseTypeDef(_ClientSelectObjectContentResponseTypeDef):
    """
    - *(dict) --*

      - **Payload** (:class:`.EventStream`) --

        The array of results.
        - **Records** *(dict) --*

          The Records Event.
          - **Payload** *(bytes) --*

            The byte array of partial, one or more result records.
    """


_ClientSelectObjectContentScanRangeTypeDef = TypedDict(
    "_ClientSelectObjectContentScanRangeTypeDef", {"Start": int, "End": int}, total=False
)


class ClientSelectObjectContentScanRangeTypeDef(_ClientSelectObjectContentScanRangeTypeDef):
    """
    Specifies the byte range of the object to get the records from. A record is processed when its
    first byte is contained by the range. This parameter is optional, but when specified, it must
    not be empty. See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.

      ``ScanRange`` may be used in the following ways:
    """


_ClientUploadPartCopyCopySource1TypeDef = TypedDict(
    "_ClientUploadPartCopyCopySource1TypeDef",
    {"Bucket": str, "Key": str, "VersionId": str},
    total=False,
)


class ClientUploadPartCopyCopySource1TypeDef(_ClientUploadPartCopyCopySource1TypeDef):
    pass


_ClientUploadPartCopyResponseCopyPartResultTypeDef = TypedDict(
    "_ClientUploadPartCopyResponseCopyPartResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class ClientUploadPartCopyResponseCopyPartResultTypeDef(
    _ClientUploadPartCopyResponseCopyPartResultTypeDef
):
    pass


_ClientUploadPartCopyResponseTypeDef = TypedDict(
    "_ClientUploadPartCopyResponseTypeDef",
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


class ClientUploadPartCopyResponseTypeDef(_ClientUploadPartCopyResponseTypeDef):
    """
    - *(dict) --*

      - **CopySourceVersionId** *(string) --*

        The version of the source object that was copied, if you have enabled versioning on the
        source bucket.
    """


_ClientUploadPartResponseTypeDef = TypedDict(
    "_ClientUploadPartResponseTypeDef",
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


class ClientUploadPartResponseTypeDef(_ClientUploadPartResponseTypeDef):
    """
    - *(dict) --*

      - **ServerSideEncryption** *(string) --*

        The server-side encryption algorithm used when storing this object in Amazon S3 (for
        example, AES256, aws:kms).
    """


_ListMultipartUploadsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMultipartUploadsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMultipartUploadsPaginatePaginationConfigTypeDef(
    _ListMultipartUploadsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef(
    _ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef
):
    pass


_ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef(
    _ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef
):
    pass


_ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef(
    _ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef
):
    pass


_ListMultipartUploadsPaginateResponseUploadsTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseUploadsTypeDef",
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


class ListMultipartUploadsPaginateResponseUploadsTypeDef(
    _ListMultipartUploadsPaginateResponseUploadsTypeDef
):
    pass


_ListMultipartUploadsPaginateResponseTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseTypeDef",
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


class ListMultipartUploadsPaginateResponseTypeDef(_ListMultipartUploadsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Bucket** *(string) --*

        Name of the bucket to which the multipart upload was initiated.
    """


_ListObjectVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectVersionsPaginatePaginationConfigTypeDef(
    _ListObjectVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListObjectVersionsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ListObjectVersionsPaginateResponseCommonPrefixesTypeDef(
    _ListObjectVersionsPaginateResponseCommonPrefixesTypeDef
):
    pass


_ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef(
    _ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef
):
    pass


_ListObjectVersionsPaginateResponseDeleteMarkersTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseDeleteMarkersTypeDef",
    {
        "Owner": ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)


class ListObjectVersionsPaginateResponseDeleteMarkersTypeDef(
    _ListObjectVersionsPaginateResponseDeleteMarkersTypeDef
):
    pass


_ListObjectVersionsPaginateResponseVersionsOwnerTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseVersionsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListObjectVersionsPaginateResponseVersionsOwnerTypeDef(
    _ListObjectVersionsPaginateResponseVersionsOwnerTypeDef
):
    pass


_ListObjectVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseVersionsTypeDef",
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


class ListObjectVersionsPaginateResponseVersionsTypeDef(
    _ListObjectVersionsPaginateResponseVersionsTypeDef
):
    pass


_ListObjectVersionsPaginateResponseTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseTypeDef",
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


class ListObjectVersionsPaginateResponseTypeDef(_ListObjectVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether Amazon S3 returned all of the results that satisfied the
        search criteria. If your results were truncated, you can make a follow-up paginated request
        using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in
        another request to return the rest of the results.
    """


_ListObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectsPaginatePaginationConfigTypeDef(_ListObjectsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListObjectsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "_ListObjectsPaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ListObjectsPaginateResponseCommonPrefixesTypeDef(
    _ListObjectsPaginateResponseCommonPrefixesTypeDef
):
    pass


_ListObjectsPaginateResponseContentsOwnerTypeDef = TypedDict(
    "_ListObjectsPaginateResponseContentsOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ListObjectsPaginateResponseContentsOwnerTypeDef(
    _ListObjectsPaginateResponseContentsOwnerTypeDef
):
    pass


_ListObjectsPaginateResponseContentsTypeDef = TypedDict(
    "_ListObjectsPaginateResponseContentsTypeDef",
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


class ListObjectsPaginateResponseContentsTypeDef(_ListObjectsPaginateResponseContentsTypeDef):
    pass


_ListObjectsPaginateResponseTypeDef = TypedDict(
    "_ListObjectsPaginateResponseTypeDef",
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


class ListObjectsPaginateResponseTypeDef(_ListObjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether Amazon S3 returned all of the results that satisfied the
        search criteria.
    """


_ListObjectsV2PaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectsV2PaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectsV2PaginatePaginationConfigTypeDef(_ListObjectsV2PaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListObjectsV2PaginateResponseCommonPrefixesTypeDef = TypedDict(
    "_ListObjectsV2PaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ListObjectsV2PaginateResponseCommonPrefixesTypeDef(
    _ListObjectsV2PaginateResponseCommonPrefixesTypeDef
):
    pass


_ListObjectsV2PaginateResponseContentsOwnerTypeDef = TypedDict(
    "_ListObjectsV2PaginateResponseContentsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListObjectsV2PaginateResponseContentsOwnerTypeDef(
    _ListObjectsV2PaginateResponseContentsOwnerTypeDef
):
    pass


_ListObjectsV2PaginateResponseContentsTypeDef = TypedDict(
    "_ListObjectsV2PaginateResponseContentsTypeDef",
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


class ListObjectsV2PaginateResponseContentsTypeDef(_ListObjectsV2PaginateResponseContentsTypeDef):
    pass


_ListObjectsV2PaginateResponseTypeDef = TypedDict(
    "_ListObjectsV2PaginateResponseTypeDef",
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


class ListObjectsV2PaginateResponseTypeDef(_ListObjectsV2PaginateResponseTypeDef):
    """
    - *(dict) --*

      - **IsTruncated** *(boolean) --*

        Set to false if all of the results were returned. Set to true if more keys are available to
        return. If the number of results exceeds that specified by MaxKeys, all of the results might
        not be returned.
    """


_ListPartsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPartsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPartsPaginatePaginationConfigTypeDef(_ListPartsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPartsPaginateResponseInitiatorTypeDef = TypedDict(
    "_ListPartsPaginateResponseInitiatorTypeDef", {"ID": str, "DisplayName": str}, total=False
)


class ListPartsPaginateResponseInitiatorTypeDef(_ListPartsPaginateResponseInitiatorTypeDef):
    pass


_ListPartsPaginateResponseOwnerTypeDef = TypedDict(
    "_ListPartsPaginateResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ListPartsPaginateResponseOwnerTypeDef(_ListPartsPaginateResponseOwnerTypeDef):
    pass


_ListPartsPaginateResponsePartsTypeDef = TypedDict(
    "_ListPartsPaginateResponsePartsTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)


class ListPartsPaginateResponsePartsTypeDef(_ListPartsPaginateResponsePartsTypeDef):
    pass


_ListPartsPaginateResponseTypeDef = TypedDict(
    "_ListPartsPaginateResponseTypeDef",
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


class ListPartsPaginateResponseTypeDef(_ListPartsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **AbortDate** *(datetime) --*

        If the bucket has a lifecycle rule configured with an action to abort incomplete multipart
        uploads and the prefix in the lifecycle rule matches the object name in the request, then
        the response includes this header indicating when the initiated multipart upload will become
        eligible for abort operation. For more information, see `Aborting Incomplete Multipart
        Uploads Using a Bucket Lifecycle Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
        .
        The response will also include the ``x-amz-abort-rule-id`` header that will provide the ID
        of the lifecycle configuration rule that defines this action.
    """


_MultipartUploadAbortResponseTypeDef = TypedDict(
    "_MultipartUploadAbortResponseTypeDef", {"RequestCharged": str}, total=False
)


class MultipartUploadAbortResponseTypeDef(_MultipartUploadAbortResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_MultipartUploadCompleteMultipartUploadPartsTypeDef = TypedDict(
    "_MultipartUploadCompleteMultipartUploadPartsTypeDef",
    {"ETag": str, "PartNumber": int},
    total=False,
)


class MultipartUploadCompleteMultipartUploadPartsTypeDef(
    _MultipartUploadCompleteMultipartUploadPartsTypeDef
):
    """
    - *(dict) --*

      Details of the parts that were uploaded.
      - **ETag** *(string) --*

        Entity tag returned when the part was uploaded.
    """


_MultipartUploadCompleteMultipartUploadTypeDef = TypedDict(
    "_MultipartUploadCompleteMultipartUploadTypeDef",
    {"Parts": List[MultipartUploadCompleteMultipartUploadPartsTypeDef]},
    total=False,
)


class MultipartUploadCompleteMultipartUploadTypeDef(_MultipartUploadCompleteMultipartUploadTypeDef):
    """
    The container for the multipart upload request information.
    - **Parts** *(list) --*

      Array of CompletedPart data types.
      - *(dict) --*

        Details of the parts that were uploaded.
        - **ETag** *(string) --*

          Entity tag returned when the part was uploaded.
    """


_MultipartUploadPartCopyFromCopySource1TypeDef = TypedDict(
    "_MultipartUploadPartCopyFromCopySource1TypeDef",
    {"Bucket": str, "Key": str, "VersionId": str},
    total=False,
)


class MultipartUploadPartCopyFromCopySource1TypeDef(_MultipartUploadPartCopyFromCopySource1TypeDef):
    pass


_MultipartUploadPartCopyFromResponseCopyPartResultTypeDef = TypedDict(
    "_MultipartUploadPartCopyFromResponseCopyPartResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class MultipartUploadPartCopyFromResponseCopyPartResultTypeDef(
    _MultipartUploadPartCopyFromResponseCopyPartResultTypeDef
):
    pass


_MultipartUploadPartCopyFromResponseTypeDef = TypedDict(
    "_MultipartUploadPartCopyFromResponseTypeDef",
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


class MultipartUploadPartCopyFromResponseTypeDef(_MultipartUploadPartCopyFromResponseTypeDef):
    """
    - *(dict) --*

      - **CopySourceVersionId** *(string) --*

        The version of the source object that was copied, if you have enabled versioning on the
        source bucket.
    """


_MultipartUploadPartUploadResponseTypeDef = TypedDict(
    "_MultipartUploadPartUploadResponseTypeDef",
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


class MultipartUploadPartUploadResponseTypeDef(_MultipartUploadPartUploadResponseTypeDef):
    """
    - *(dict) --*

      - **ServerSideEncryption** *(string) --*

        The server-side encryption algorithm used when storing this object in Amazon S3 (for
        example, AES256, aws:kms).
    """


_ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef(
    _ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef
):
    """
    - **Grantee** *(dict) --*

      The person being granted permissions.
      - **DisplayName** *(string) --*

        Screen name of the grantee.
    """


_ObjectAclPutAccessControlPolicyGrantsTypeDef = TypedDict(
    "_ObjectAclPutAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ObjectAclPutAccessControlPolicyGrantsTypeDef(_ObjectAclPutAccessControlPolicyGrantsTypeDef):
    """
    - *(dict) --*

      Container for grant information.
      - **Grantee** *(dict) --*

        The person being granted permissions.
        - **DisplayName** *(string) --*

          Screen name of the grantee.
    """


_ObjectAclPutAccessControlPolicyOwnerTypeDef = TypedDict(
    "_ObjectAclPutAccessControlPolicyOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ObjectAclPutAccessControlPolicyOwnerTypeDef(_ObjectAclPutAccessControlPolicyOwnerTypeDef):
    pass


_ObjectAclPutAccessControlPolicyTypeDef = TypedDict(
    "_ObjectAclPutAccessControlPolicyTypeDef",
    {
        "Grants": List[ObjectAclPutAccessControlPolicyGrantsTypeDef],
        "Owner": ObjectAclPutAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)


class ObjectAclPutAccessControlPolicyTypeDef(_ObjectAclPutAccessControlPolicyTypeDef):
    """
    Contains the elements that set the ACL permissions for an object per grantee.
    - **Grants** *(list) --*

      A list of grants.
      - *(dict) --*

        Container for grant information.
        - **Grantee** *(dict) --*

          The person being granted permissions.
          - **DisplayName** *(string) --*

            Screen name of the grantee.
    """


_ObjectAclPutResponseTypeDef = TypedDict(
    "_ObjectAclPutResponseTypeDef", {"RequestCharged": str}, total=False
)


class ObjectAclPutResponseTypeDef(_ObjectAclPutResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ObjectCopyFromCopySource1TypeDef = TypedDict(
    "_ObjectCopyFromCopySource1TypeDef", {"Bucket": str, "Key": str, "VersionId": str}, total=False
)


class ObjectCopyFromCopySource1TypeDef(_ObjectCopyFromCopySource1TypeDef):
    pass


_ObjectCopyFromResponseCopyObjectResultTypeDef = TypedDict(
    "_ObjectCopyFromResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class ObjectCopyFromResponseCopyObjectResultTypeDef(_ObjectCopyFromResponseCopyObjectResultTypeDef):
    """
    - **CopyObjectResult** *(dict) --*

      Container for all response elements.
      - **ETag** *(string) --*

        Returns the ETag of the new object. The ETag reflects only changes to the contents of an
        object, not its metadata. The source and destination ETag is identical for a successfully
        copied object.
    """


_ObjectCopyFromResponseTypeDef = TypedDict(
    "_ObjectCopyFromResponseTypeDef",
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


class ObjectCopyFromResponseTypeDef(_ObjectCopyFromResponseTypeDef):
    """
    - *(dict) --*

      - **CopyObjectResult** *(dict) --*

        Container for all response elements.
        - **ETag** *(string) --*

          Returns the ETag of the new object. The ETag reflects only changes to the contents of an
          object, not its metadata. The source and destination ETag is identical for a successfully
          copied object.
    """


_ObjectDeleteResponseTypeDef = TypedDict(
    "_ObjectDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)


class ObjectDeleteResponseTypeDef(_ObjectDeleteResponseTypeDef):
    """
    - *(dict) --*

      - **DeleteMarker** *(boolean) --*

        Specifies whether the versioned object that was permanently deleted was (true) or was not
        (false) a delete marker.
    """


_ObjectExistsWaitWaiterConfigTypeDef = TypedDict(
    "_ObjectExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ObjectExistsWaitWaiterConfigTypeDef(_ObjectExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


_ObjectGetResponseTypeDef = TypedDict(
    "_ObjectGetResponseTypeDef",
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


class ObjectGetResponseTypeDef(_ObjectGetResponseTypeDef):
    """
    - *(dict) --*

      - **Body** (:class:`.StreamingBody`) --

        Object data.
    """


_ObjectNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "_ObjectNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ObjectNotExistsWaitWaiterConfigTypeDef(_ObjectNotExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


_ObjectPutResponseTypeDef = TypedDict(
    "_ObjectPutResponseTypeDef",
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


class ObjectPutResponseTypeDef(_ObjectPutResponseTypeDef):
    """
    - *(dict) --*

      - **Expiration** *(string) --*

        If the expiration is configured for the object (see  PutBucketLifecycleConfiguration ), the
        response includes this header. It includes the expiry-date and rule-id key-value pairs that
        provide information about object expiration. The value of the rule-id is URL encoded.
    """


_ObjectRestoreObjectResponseTypeDef = TypedDict(
    "_ObjectRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)


class ObjectRestoreObjectResponseTypeDef(_ObjectRestoreObjectResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    {"Tier": Literal["Standard", "Bulk", "Expedited"]},
    total=False,
)


class ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef(
    _ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["AES256", "aws:kms"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {"TagSet": List[ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef]},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef",
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


class ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
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


class ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersTypeDef
):
    pass


_ObjectRestoreObjectRestoreRequestTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestTypeDef",
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


class ObjectRestoreObjectRestoreRequestTypeDef(_ObjectRestoreObjectRestoreRequestTypeDef):
    """
    Container for restore job parameters.
    - **Days** *(integer) --*

      Lifetime of the active copy in days. Do not use with restores that specify ``OutputLocation``
      .
    """


_ObjectSummaryCopyFromCopySource1TypeDef = TypedDict(
    "_ObjectSummaryCopyFromCopySource1TypeDef",
    {"Bucket": str, "Key": str, "VersionId": str},
    total=False,
)


class ObjectSummaryCopyFromCopySource1TypeDef(_ObjectSummaryCopyFromCopySource1TypeDef):
    pass


_ObjectSummaryCopyFromResponseCopyObjectResultTypeDef = TypedDict(
    "_ObjectSummaryCopyFromResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class ObjectSummaryCopyFromResponseCopyObjectResultTypeDef(
    _ObjectSummaryCopyFromResponseCopyObjectResultTypeDef
):
    """
    - **CopyObjectResult** *(dict) --*

      Container for all response elements.
      - **ETag** *(string) --*

        Returns the ETag of the new object. The ETag reflects only changes to the contents of an
        object, not its metadata. The source and destination ETag is identical for a successfully
        copied object.
    """


_ObjectSummaryCopyFromResponseTypeDef = TypedDict(
    "_ObjectSummaryCopyFromResponseTypeDef",
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


class ObjectSummaryCopyFromResponseTypeDef(_ObjectSummaryCopyFromResponseTypeDef):
    """
    - *(dict) --*

      - **CopyObjectResult** *(dict) --*

        Container for all response elements.
        - **ETag** *(string) --*

          Returns the ETag of the new object. The ETag reflects only changes to the contents of an
          object, not its metadata. The source and destination ETag is identical for a successfully
          copied object.
    """


_ObjectSummaryDeleteResponseTypeDef = TypedDict(
    "_ObjectSummaryDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)


class ObjectSummaryDeleteResponseTypeDef(_ObjectSummaryDeleteResponseTypeDef):
    """
    - *(dict) --*

      - **DeleteMarker** *(boolean) --*

        Specifies whether the versioned object that was permanently deleted was (true) or was not
        (false) a delete marker.
    """


_ObjectSummaryGetResponseTypeDef = TypedDict(
    "_ObjectSummaryGetResponseTypeDef",
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


class ObjectSummaryGetResponseTypeDef(_ObjectSummaryGetResponseTypeDef):
    """
    - *(dict) --*

      - **Body** (:class:`.StreamingBody`) --

        Object data.
    """


_ObjectSummaryPutResponseTypeDef = TypedDict(
    "_ObjectSummaryPutResponseTypeDef",
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


class ObjectSummaryPutResponseTypeDef(_ObjectSummaryPutResponseTypeDef):
    """
    - *(dict) --*

      - **Expiration** *(string) --*

        If the expiration is configured for the object (see  PutBucketLifecycleConfiguration ), the
        response includes this header. It includes the expiry-date and rule-id key-value pairs that
        provide information about object expiration. The value of the rule-id is URL encoded.
    """


_ObjectSummaryRestoreObjectResponseTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)


class ObjectSummaryRestoreObjectResponseTypeDef(_ObjectSummaryRestoreObjectResponseTypeDef):
    """
    - *(dict) --*

      - **RequestCharged** *(string) --*

        If present, indicates that the requester was successfully charged for the request.
    """


_ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    {"Tier": Literal["Standard", "Bulk", "Expedited"]},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["AES256", "aws:kms"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {"TagSet": List[ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef]},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef",
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


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
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


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef
):
    pass


_ObjectSummaryRestoreObjectRestoreRequestTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestTypeDef",
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


class ObjectSummaryRestoreObjectRestoreRequestTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestTypeDef
):
    """
    Container for restore job parameters.
    - **Days** *(integer) --*

      Lifetime of the active copy in days. Do not use with restores that specify ``OutputLocation``
      .
    """


_ObjectVersionDeleteResponseTypeDef = TypedDict(
    "_ObjectVersionDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)


class ObjectVersionDeleteResponseTypeDef(_ObjectVersionDeleteResponseTypeDef):
    """
    - *(dict) --*

      - **DeleteMarker** *(boolean) --*

        Specifies whether the versioned object that was permanently deleted was (true) or was not
        (false) a delete marker.
    """


_ObjectVersionGetResponseTypeDef = TypedDict(
    "_ObjectVersionGetResponseTypeDef",
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


class ObjectVersionGetResponseTypeDef(_ObjectVersionGetResponseTypeDef):
    """
    - *(dict) --*

      - **Body** (:class:`.StreamingBody`) --

        Object data.
    """


_ObjectVersionHeadResponseTypeDef = TypedDict(
    "_ObjectVersionHeadResponseTypeDef",
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


class ObjectVersionHeadResponseTypeDef(_ObjectVersionHeadResponseTypeDef):
    """
    - *(dict) --*

      - **DeleteMarker** *(boolean) --*

        Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
        false, this response header does not appear in the response.
    """


_ObjectVersionsDeleteResponseDeletedTypeDef = TypedDict(
    "_ObjectVersionsDeleteResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)


class ObjectVersionsDeleteResponseDeletedTypeDef(_ObjectVersionsDeleteResponseDeletedTypeDef):
    """
    - *(dict) --*

      Information about the deleted object.
      - **Key** *(string) --*

        The name of the deleted object.
    """


_ObjectVersionsDeleteResponseErrorsTypeDef = TypedDict(
    "_ObjectVersionsDeleteResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)


class ObjectVersionsDeleteResponseErrorsTypeDef(_ObjectVersionsDeleteResponseErrorsTypeDef):
    pass


_ObjectVersionsDeleteResponseTypeDef = TypedDict(
    "_ObjectVersionsDeleteResponseTypeDef",
    {
        "Deleted": List[ObjectVersionsDeleteResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ObjectVersionsDeleteResponseErrorsTypeDef],
    },
    total=False,
)


class ObjectVersionsDeleteResponseTypeDef(_ObjectVersionsDeleteResponseTypeDef):
    """
    - *(dict) --*

      - **Deleted** *(list) --*

        Container element for a successful delete. It identifies the object that was successfully
        deleted.
        - *(dict) --*

          Information about the deleted object.
          - **Key** *(string) --*

            The name of the deleted object.
    """


_ObjectsDeleteResponseDeletedTypeDef = TypedDict(
    "_ObjectsDeleteResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)


class ObjectsDeleteResponseDeletedTypeDef(_ObjectsDeleteResponseDeletedTypeDef):
    """
    - *(dict) --*

      Information about the deleted object.
      - **Key** *(string) --*

        The name of the deleted object.
    """


_ObjectsDeleteResponseErrorsTypeDef = TypedDict(
    "_ObjectsDeleteResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)


class ObjectsDeleteResponseErrorsTypeDef(_ObjectsDeleteResponseErrorsTypeDef):
    pass


_ObjectsDeleteResponseTypeDef = TypedDict(
    "_ObjectsDeleteResponseTypeDef",
    {
        "Deleted": List[ObjectsDeleteResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ObjectsDeleteResponseErrorsTypeDef],
    },
    total=False,
)


class ObjectsDeleteResponseTypeDef(_ObjectsDeleteResponseTypeDef):
    """
    - *(dict) --*

      - **Deleted** *(list) --*

        Container element for a successful delete. It identifies the object that was successfully
        deleted.
        - *(dict) --*

          Information about the deleted object.
          - **Key** *(string) --*

            The name of the deleted object.
    """


_ServiceResourceCreateBucketCreateBucketConfigurationTypeDef = TypedDict(
    "_ServiceResourceCreateBucketCreateBucketConfigurationTypeDef",
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


class ServiceResourceCreateBucketCreateBucketConfigurationTypeDef(
    _ServiceResourceCreateBucketCreateBucketConfigurationTypeDef
):
    """
    The configuration information for the bucket.
    - **LocationConstraint** *(string) --*

      Specifies the Region where the bucket will be created. If you don't specify a Region, the
      bucket is created in the US East (N. Virginia) Region (us-east-1).
    """
