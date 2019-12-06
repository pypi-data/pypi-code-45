"Main interface for iot service type defs"
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


ClientAssociateTargetsWithJobResponseTypeDef = TypedDict(
    "ClientAssociateTargetsWithJobResponseTypeDef",
    {"jobArn": str, "jobId": str, "description": str},
    total=False,
)

ClientCancelJobResponseTypeDef = TypedDict(
    "ClientCancelJobResponseTypeDef", {"jobArn": str, "jobId": str, "description": str}, total=False
)

ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "ClientCreateAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)

ClientCreateBillingGroupBillingGroupPropertiesTypeDef = TypedDict(
    "ClientCreateBillingGroupBillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)

ClientCreateBillingGroupResponseTypeDef = TypedDict(
    "ClientCreateBillingGroupResponseTypeDef",
    {"billingGroupName": str, "billingGroupArn": str, "billingGroupId": str},
    total=False,
)

ClientCreateBillingGroupTagsTypeDef = TypedDict(
    "ClientCreateBillingGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateCertificateFromCsrResponseTypeDef = TypedDict(
    "ClientCreateCertificateFromCsrResponseTypeDef",
    {"certificateArn": str, "certificateId": str, "certificatePem": str},
    total=False,
)

ClientCreateDomainConfigurationAuthorizerConfigTypeDef = TypedDict(
    "ClientCreateDomainConfigurationAuthorizerConfigTypeDef",
    {"defaultAuthorizerName": str, "allowAuthorizerOverride": bool},
    total=False,
)

ClientCreateDomainConfigurationResponseTypeDef = TypedDict(
    "ClientCreateDomainConfigurationResponseTypeDef",
    {"domainConfigurationName": str, "domainConfigurationArn": str},
    total=False,
)

ClientCreateDynamicThingGroupResponseTypeDef = TypedDict(
    "ClientCreateDynamicThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
    },
    total=False,
)

ClientCreateDynamicThingGroupTagsTypeDef = TypedDict(
    "ClientCreateDynamicThingGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)

ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef = TypedDict(
    "ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientCreateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)

_RequiredClientCreateJobAbortConfigcriteriaListTypeDef = TypedDict(
    "_RequiredClientCreateJobAbortConfigcriteriaListTypeDef",
    {"failureType": Literal["FAILED", "REJECTED", "TIMED_OUT", "ALL"]},
)
_OptionalClientCreateJobAbortConfigcriteriaListTypeDef = TypedDict(
    "_OptionalClientCreateJobAbortConfigcriteriaListTypeDef",
    {"action": str, "thresholdPercentage": float, "minNumberOfExecutedThings": int},
    total=False,
)


class ClientCreateJobAbortConfigcriteriaListTypeDef(
    _RequiredClientCreateJobAbortConfigcriteriaListTypeDef,
    _OptionalClientCreateJobAbortConfigcriteriaListTypeDef,
):
    pass


ClientCreateJobAbortConfigTypeDef = TypedDict(
    "ClientCreateJobAbortConfigTypeDef",
    {"criteriaList": List[ClientCreateJobAbortConfigcriteriaListTypeDef]},
)

ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)

ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientCreateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
    total=False,
)

ClientCreateJobJobExecutionsRolloutConfigTypeDef = TypedDict(
    "ClientCreateJobJobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientCreateJobJobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)

ClientCreateJobPresignedUrlConfigTypeDef = TypedDict(
    "ClientCreateJobPresignedUrlConfigTypeDef", {"roleArn": str, "expiresInSec": int}, total=False
)

ClientCreateJobResponseTypeDef = TypedDict(
    "ClientCreateJobResponseTypeDef", {"jobArn": str, "jobId": str, "description": str}, total=False
)

ClientCreateJobTagsTypeDef = TypedDict(
    "ClientCreateJobTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateJobTimeoutConfigTypeDef = TypedDict(
    "ClientCreateJobTimeoutConfigTypeDef", {"inProgressTimeoutInMinutes": int}, total=False
)

ClientCreateKeysAndCertificateResponsekeyPairTypeDef = TypedDict(
    "ClientCreateKeysAndCertificateResponsekeyPairTypeDef",
    {"PublicKey": str, "PrivateKey": str},
    total=False,
)

ClientCreateKeysAndCertificateResponseTypeDef = TypedDict(
    "ClientCreateKeysAndCertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "keyPair": ClientCreateKeysAndCertificateResponsekeyPairTypeDef,
    },
    total=False,
)

ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)

ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)

ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)

ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)

ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)

ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef", {"action": str}
)

ClientCreateMitigationActionActionParamsTypeDef = TypedDict(
    "ClientCreateMitigationActionActionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientCreateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientCreateMitigationActionActionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientCreateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientCreateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientCreateMitigationActionActionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientCreateMitigationActionActionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)

ClientCreateMitigationActionResponseTypeDef = TypedDict(
    "ClientCreateMitigationActionResponseTypeDef", {"actionArn": str, "actionId": str}, total=False
)

ClientCreateMitigationActionTagsTypeDef = TypedDict(
    "ClientCreateMitigationActionTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef",
    {"maximumPerMinute": int},
    total=False,
)

ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef",
    {"certificateName": str, "inlineDocument": str},
    total=False,
)

ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef",
    {"inlineDocument": bytes},
    total=False,
)

ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef",
    {
        "signature": ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef,
        "certificateChain": ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef,
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)

ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef",
    {"bucket": str, "prefix": str},
    total=False,
)

ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef",
    {
        "s3Destination": ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
    },
    total=False,
)

ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef",
    {"certificateArn": str, "platform": str, "certificatePathOnDevice": str},
    total=False,
)

ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": ClientCreateOtaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef,
        "signingProfileName": str,
        "destination": ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef,
    },
    total=False,
)

ClientCreateOtaUpdateFilescodeSigningTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilescodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": ClientCreateOtaUpdateFilescodeSigningstartSigningJobParameterTypeDef,
        "customCodeSigning": ClientCreateOtaUpdateFilescodeSigningcustomCodeSigningTypeDef,
    },
    total=False,
)

ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)

ClientCreateOtaUpdateFilesfileLocationstreamTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilesfileLocationstreamTypeDef",
    {"streamId": str, "fileId": int},
    total=False,
)

ClientCreateOtaUpdateFilesfileLocationTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilesfileLocationTypeDef",
    {
        "stream": ClientCreateOtaUpdateFilesfileLocationstreamTypeDef,
        "s3Location": ClientCreateOtaUpdateFilesfileLocations3LocationTypeDef,
    },
    total=False,
)

ClientCreateOtaUpdateFilesTypeDef = TypedDict(
    "ClientCreateOtaUpdateFilesTypeDef",
    {
        "fileName": str,
        "fileVersion": str,
        "fileLocation": ClientCreateOtaUpdateFilesfileLocationTypeDef,
        "codeSigning": ClientCreateOtaUpdateFilescodeSigningTypeDef,
        "attributes": Dict[str, str],
    },
    total=False,
)

ClientCreateOtaUpdateResponseTypeDef = TypedDict(
    "ClientCreateOtaUpdateResponseTypeDef",
    {
        "otaUpdateId": str,
        "awsIotJobId": str,
        "otaUpdateArn": str,
        "awsIotJobArn": str,
        "otaUpdateStatus": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ],
    },
    total=False,
)

ClientCreateOtaUpdateTagsTypeDef = TypedDict(
    "ClientCreateOtaUpdateTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreatePolicyResponseTypeDef = TypedDict(
    "ClientCreatePolicyResponseTypeDef",
    {"policyName": str, "policyArn": str, "policyDocument": str, "policyVersionId": str},
    total=False,
)

ClientCreatePolicyVersionResponseTypeDef = TypedDict(
    "ClientCreatePolicyVersionResponseTypeDef",
    {"policyArn": str, "policyDocument": str, "policyVersionId": str, "isDefaultVersion": bool},
    total=False,
)

ClientCreateProvisioningClaimResponsekeyPairTypeDef = TypedDict(
    "ClientCreateProvisioningClaimResponsekeyPairTypeDef",
    {"PublicKey": str, "PrivateKey": str},
    total=False,
)

ClientCreateProvisioningClaimResponseTypeDef = TypedDict(
    "ClientCreateProvisioningClaimResponseTypeDef",
    {
        "certificateId": str,
        "certificatePem": str,
        "keyPair": ClientCreateProvisioningClaimResponsekeyPairTypeDef,
        "expiration": datetime,
    },
    total=False,
)

ClientCreateProvisioningTemplateResponseTypeDef = TypedDict(
    "ClientCreateProvisioningTemplateResponseTypeDef",
    {"templateArn": str, "templateName": str, "defaultVersionId": int},
    total=False,
)

ClientCreateProvisioningTemplateTagsTypeDef = TypedDict(
    "ClientCreateProvisioningTemplateTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateProvisioningTemplateVersionResponseTypeDef = TypedDict(
    "ClientCreateProvisioningTemplateVersionResponseTypeDef",
    {"templateArn": str, "templateName": str, "versionId": int, "isDefaultVersion": bool},
    total=False,
)

ClientCreateRoleAliasResponseTypeDef = TypedDict(
    "ClientCreateRoleAliasResponseTypeDef", {"roleAlias": str, "roleAliasArn": str}, total=False
)

ClientCreateScheduledAuditResponseTypeDef = TypedDict(
    "ClientCreateScheduledAuditResponseTypeDef", {"scheduledAuditArn": str}, total=False
)

ClientCreateScheduledAuditTagsTypeDef = TypedDict(
    "ClientCreateScheduledAuditTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSecurityProfileAlertTargetsTypeDef = TypedDict(
    "ClientCreateSecurityProfileAlertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)

ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef = TypedDict(
    "ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientCreateSecurityProfileBehaviorscriteriaTypeDef = TypedDict(
    "ClientCreateSecurityProfileBehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientCreateSecurityProfileBehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientCreateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

_RequiredClientCreateSecurityProfileBehaviorsTypeDef = TypedDict(
    "_RequiredClientCreateSecurityProfileBehaviorsTypeDef", {"name": str}
)
_OptionalClientCreateSecurityProfileBehaviorsTypeDef = TypedDict(
    "_OptionalClientCreateSecurityProfileBehaviorsTypeDef",
    {"metric": str, "criteria": ClientCreateSecurityProfileBehaviorscriteriaTypeDef},
    total=False,
)


class ClientCreateSecurityProfileBehaviorsTypeDef(
    _RequiredClientCreateSecurityProfileBehaviorsTypeDef,
    _OptionalClientCreateSecurityProfileBehaviorsTypeDef,
):
    pass


ClientCreateSecurityProfileResponseTypeDef = TypedDict(
    "ClientCreateSecurityProfileResponseTypeDef",
    {"securityProfileName": str, "securityProfileArn": str},
    total=False,
)

ClientCreateSecurityProfileTagsTypeDef = TypedDict(
    "ClientCreateSecurityProfileTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateStreamFiless3LocationTypeDef = TypedDict(
    "ClientCreateStreamFiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)

ClientCreateStreamFilesTypeDef = TypedDict(
    "ClientCreateStreamFilesTypeDef",
    {"fileId": int, "s3Location": ClientCreateStreamFiless3LocationTypeDef},
    total=False,
)

ClientCreateStreamResponseTypeDef = TypedDict(
    "ClientCreateStreamResponseTypeDef",
    {"streamId": str, "streamArn": str, "description": str, "streamVersion": int},
    total=False,
)

ClientCreateStreamTagsTypeDef = TypedDict(
    "ClientCreateStreamTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateThingAttributePayloadTypeDef = TypedDict(
    "ClientCreateThingAttributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)

ClientCreateThingGroupResponseTypeDef = TypedDict(
    "ClientCreateThingGroupResponseTypeDef",
    {"thingGroupName": str, "thingGroupArn": str, "thingGroupId": str},
    total=False,
)

ClientCreateThingGroupTagsTypeDef = TypedDict(
    "ClientCreateThingGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)

ClientCreateThingGroupThingGroupPropertiesTypeDef = TypedDict(
    "ClientCreateThingGroupThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientCreateThingGroupThingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)

ClientCreateThingResponseTypeDef = TypedDict(
    "ClientCreateThingResponseTypeDef",
    {"thingName": str, "thingArn": str, "thingId": str},
    total=False,
)

ClientCreateThingTypeResponseTypeDef = TypedDict(
    "ClientCreateThingTypeResponseTypeDef",
    {"thingTypeName": str, "thingTypeArn": str, "thingTypeId": str},
    total=False,
)

ClientCreateThingTypeTagsTypeDef = TypedDict(
    "ClientCreateThingTypeTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateThingTypeThingTypePropertiesTypeDef = TypedDict(
    "ClientCreateThingTypeThingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)

ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef = TypedDict(
    "ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef",
    {"confirmationUrl": str},
)

ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef = TypedDict(
    "ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef",
    {
        "httpUrlConfiguration": ClientCreateTopicRuleDestinationDestinationConfigurationhttpUrlConfigurationTypeDef
    },
    total=False,
)

ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef = TypedDict(
    "ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef",
    {"confirmationUrl": str},
    total=False,
)

ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef = TypedDict(
    "ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef",
    {
        "arn": str,
        "status": Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"],
        "statusReason": str,
        "httpUrlProperties": ClientCreateTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef,
    },
    total=False,
)

ClientCreateTopicRuleDestinationResponseTypeDef = TypedDict(
    "ClientCreateTopicRuleDestinationResponseTypeDef",
    {"topicRuleDestination": ClientCreateTopicRuleDestinationResponsetopicRuleDestinationTypeDef},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef",
    {"sigv4": ClientCreateTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientCreateTopicRuleTopicRulePayloadactionshttpheadersTypeDef],
        "auth": ClientCreateTopicRuleTopicRulePayloadactionshttpauthTypeDef,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef", {"functionArn": str}, total=False
)

ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloadactionsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloadactionsTypeDef",
    {
        "dynamoDB": ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientCreateTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef,
        "lambda": ClientCreateTopicRuleTopicRulePayloadactionslambdaTypeDef,
        "sns": ClientCreateTopicRuleTopicRulePayloadactionssnsTypeDef,
        "sqs": ClientCreateTopicRuleTopicRulePayloadactionssqsTypeDef,
        "kinesis": ClientCreateTopicRuleTopicRulePayloadactionskinesisTypeDef,
        "republish": ClientCreateTopicRuleTopicRulePayloadactionsrepublishTypeDef,
        "s3": ClientCreateTopicRuleTopicRulePayloadactionss3TypeDef,
        "firehose": ClientCreateTopicRuleTopicRulePayloadactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientCreateTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientCreateTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientCreateTopicRuleTopicRulePayloadactionselasticsearchTypeDef,
        "salesforce": ClientCreateTopicRuleTopicRulePayloadactionssalesforceTypeDef,
        "iotAnalytics": ClientCreateTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef,
        "iotEvents": ClientCreateTopicRuleTopicRulePayloadactionsiotEventsTypeDef,
        "iotSiteWise": ClientCreateTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef,
        "stepFunctions": ClientCreateTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef,
        "http": ClientCreateTopicRuleTopicRulePayloadactionshttpTypeDef,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef",
    {"sigv4": ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientCreateTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef],
        "auth": ClientCreateTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)

ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef = TypedDict(
    "ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef",
    {
        "dynamoDB": ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientCreateTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef,
        "lambda": ClientCreateTopicRuleTopicRulePayloaderrorActionlambdaTypeDef,
        "sns": ClientCreateTopicRuleTopicRulePayloaderrorActionsnsTypeDef,
        "sqs": ClientCreateTopicRuleTopicRulePayloaderrorActionsqsTypeDef,
        "kinesis": ClientCreateTopicRuleTopicRulePayloaderrorActionkinesisTypeDef,
        "republish": ClientCreateTopicRuleTopicRulePayloaderrorActionrepublishTypeDef,
        "s3": ClientCreateTopicRuleTopicRulePayloaderrorActions3TypeDef,
        "firehose": ClientCreateTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientCreateTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientCreateTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef,
        "salesforce": ClientCreateTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef,
        "iotAnalytics": ClientCreateTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientCreateTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef,
        "iotSiteWise": ClientCreateTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef,
        "stepFunctions": ClientCreateTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef,
        "http": ClientCreateTopicRuleTopicRulePayloaderrorActionhttpTypeDef,
    },
    total=False,
)

_RequiredClientCreateTopicRuleTopicRulePayloadTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuleTopicRulePayloadTypeDef", {"sql": str}
)
_OptionalClientCreateTopicRuleTopicRulePayloadTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuleTopicRulePayloadTypeDef",
    {
        "description": str,
        "actions": List[ClientCreateTopicRuleTopicRulePayloadactionsTypeDef],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientCreateTopicRuleTopicRulePayloaderrorActionTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuleTopicRulePayloadTypeDef(
    _RequiredClientCreateTopicRuleTopicRulePayloadTypeDef,
    _OptionalClientCreateTopicRuleTopicRulePayloadTypeDef,
):
    pass


ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef = TypedDict(
    "ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef",
    {"enabled": bool},
    total=False,
)

ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef = TypedDict(
    "ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef",
    {"targetArn": str, "roleArn": str, "enabled": bool},
    total=False,
)

ClientDescribeAccountAuditConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeAccountAuditConfigurationResponseTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Dict[
            str,
            ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef,
        ],
        "auditCheckConfigurations": Dict[
            str, ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)

ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)

ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef = TypedDict(
    "ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)

ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)

ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef = TypedDict(
    "ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

ClientDescribeAuditFindingResponsefindingTypeDef = TypedDict(
    "ClientDescribeAuditFindingResponsefindingTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"],
        "nonCompliantResource": ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef,
        "relatedResources": List[ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)

ClientDescribeAuditFindingResponseTypeDef = TypedDict(
    "ClientDescribeAuditFindingResponseTypeDef",
    {"finding": ClientDescribeAuditFindingResponsefindingTypeDef},
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef",
    {"action": str},
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef",
    {
        "name": str,
        "id": str,
        "roleArn": str,
        "actionParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef,
    },
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef",
    {
        "totalFindingsCount": int,
        "failedFindingsCount": int,
        "succeededFindingsCount": int,
        "skippedFindingsCount": int,
        "canceledFindingsCount": int,
    },
    total=False,
)

ClientDescribeAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "ClientDescribeAuditMitigationActionsTaskResponseTypeDef",
    {
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
        "startTime": datetime,
        "endTime": datetime,
        "taskStatistics": Dict[
            str, ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef
        ],
        "target": ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef,
        "auditCheckToActionsMapping": Dict[str, List[str]],
        "actionsDefinition": List[
            ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef
        ],
    },
    total=False,
)

ClientDescribeAuditTaskResponseauditDetailsTypeDef = TypedDict(
    "ClientDescribeAuditTaskResponseauditDetailsTypeDef",
    {
        "checkRunStatus": Literal[
            "IN_PROGRESS",
            "WAITING_FOR_DATA_COLLECTION",
            "CANCELED",
            "COMPLETED_COMPLIANT",
            "COMPLETED_NON_COMPLIANT",
            "FAILED",
        ],
        "checkCompliant": bool,
        "totalResourcesCount": int,
        "nonCompliantResourcesCount": int,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

ClientDescribeAuditTaskResponsetaskStatisticsTypeDef = TypedDict(
    "ClientDescribeAuditTaskResponsetaskStatisticsTypeDef",
    {
        "totalChecks": int,
        "inProgressChecks": int,
        "waitingForDataCollectionChecks": int,
        "compliantChecks": int,
        "nonCompliantChecks": int,
        "failedChecks": int,
        "canceledChecks": int,
    },
    total=False,
)

ClientDescribeAuditTaskResponseTypeDef = TypedDict(
    "ClientDescribeAuditTaskResponseTypeDef",
    {
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
        "taskType": Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"],
        "taskStartTime": datetime,
        "taskStatistics": ClientDescribeAuditTaskResponsetaskStatisticsTypeDef,
        "scheduledAuditName": str,
        "auditDetails": Dict[str, ClientDescribeAuditTaskResponseauditDetailsTypeDef],
    },
    total=False,
)

ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef = TypedDict(
    "ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": Literal["ACTIVE", "INACTIVE"],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "signingDisabled": bool,
    },
    total=False,
)

ClientDescribeAuthorizerResponseTypeDef = TypedDict(
    "ClientDescribeAuthorizerResponseTypeDef",
    {"authorizerDescription": ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef},
    total=False,
)

ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef = TypedDict(
    "ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef",
    {"creationDate": datetime},
    total=False,
)

ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef = TypedDict(
    "ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)

ClientDescribeBillingGroupResponseTypeDef = TypedDict(
    "ClientDescribeBillingGroupResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupId": str,
        "billingGroupArn": str,
        "version": int,
        "billingGroupProperties": ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef,
        "billingGroupMetadata": ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef,
    },
    total=False,
)

ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef = TypedDict(
    "ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef",
    {"notBefore": datetime, "notAfter": datetime},
    total=False,
)

ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef = TypedDict(
    "ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal["ACTIVE", "INACTIVE"],
        "certificatePem": str,
        "ownedBy": str,
        "creationDate": datetime,
        "autoRegistrationStatus": Literal["ENABLE", "DISABLE"],
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "generationId": str,
        "validity": ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef,
    },
    total=False,
)

ClientDescribeCaCertificateResponseregistrationConfigTypeDef = TypedDict(
    "ClientDescribeCaCertificateResponseregistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)

ClientDescribeCaCertificateResponseTypeDef = TypedDict(
    "ClientDescribeCaCertificateResponseTypeDef",
    {
        "certificateDescription": ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef,
        "registrationConfig": ClientDescribeCaCertificateResponseregistrationConfigTypeDef,
    },
    total=False,
)

ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef = TypedDict(
    "ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef",
    {
        "transferMessage": str,
        "rejectReason": str,
        "transferDate": datetime,
        "acceptDate": datetime,
        "rejectDate": datetime,
    },
    total=False,
)

ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef = TypedDict(
    "ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef",
    {"notBefore": datetime, "notAfter": datetime},
    total=False,
)

ClientDescribeCertificateResponsecertificateDescriptionTypeDef = TypedDict(
    "ClientDescribeCertificateResponsecertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "caCertificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "certificatePem": str,
        "ownedBy": str,
        "previousOwnedBy": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "transferData": ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef,
        "generationId": str,
        "validity": ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef,
    },
    total=False,
)

ClientDescribeCertificateResponseTypeDef = TypedDict(
    "ClientDescribeCertificateResponseTypeDef",
    {"certificateDescription": ClientDescribeCertificateResponsecertificateDescriptionTypeDef},
    total=False,
)

ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef = TypedDict(
    "ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": Literal["ACTIVE", "INACTIVE"],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "signingDisabled": bool,
    },
    total=False,
)

ClientDescribeDefaultAuthorizerResponseTypeDef = TypedDict(
    "ClientDescribeDefaultAuthorizerResponseTypeDef",
    {"authorizerDescription": ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef},
    total=False,
)

ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef = TypedDict(
    "ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef",
    {"defaultAuthorizerName": str, "allowAuthorizerOverride": bool},
    total=False,
)

ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef = TypedDict(
    "ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef",
    {
        "serverCertificateArn": str,
        "serverCertificateStatus": Literal["INVALID", "VALID"],
        "serverCertificateStatusDetail": str,
    },
    total=False,
)

ClientDescribeDomainConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeDomainConfigurationResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "domainName": str,
        "serverCertificates": List[
            ClientDescribeDomainConfigurationResponseserverCertificatesTypeDef
        ],
        "authorizerConfig": ClientDescribeDomainConfigurationResponseauthorizerConfigTypeDef,
        "domainConfigurationStatus": Literal["ENABLED", "DISABLED"],
        "serviceType": Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"],
        "domainType": Literal["ENDPOINT", "AWS_MANAGED", "CUSTOMER_MANAGED"],
    },
    total=False,
)

ClientDescribeEndpointResponseTypeDef = TypedDict(
    "ClientDescribeEndpointResponseTypeDef", {"endpointAddress": str}, total=False
)

ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef = TypedDict(
    "ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDescribeEventConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeEventConfigurationsResponseTypeDef",
    {
        "eventConfigurations": Dict[
            str, ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef
        ],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

ClientDescribeIndexResponseTypeDef = TypedDict(
    "ClientDescribeIndexResponseTypeDef",
    {"indexName": str, "indexStatus": Literal["ACTIVE", "BUILDING", "REBUILDING"], "schema": str},
    total=False,
)

ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef = TypedDict(
    "ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef",
    {"detailsMap": Dict[str, str]},
    total=False,
)

ClientDescribeJobExecutionResponseexecutionTypeDef = TypedDict(
    "ClientDescribeJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "forceCanceled": bool,
        "statusDetails": ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef,
        "thingArn": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
        "versionNumber": int,
        "approximateSecondsBeforeTimedOut": int,
    },
    total=False,
)

ClientDescribeJobExecutionResponseTypeDef = TypedDict(
    "ClientDescribeJobExecutionResponseTypeDef",
    {"execution": ClientDescribeJobExecutionResponseexecutionTypeDef},
    total=False,
)

ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef = TypedDict(
    "ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef",
    {
        "failureType": Literal["FAILED", "REJECTED", "TIMED_OUT", "ALL"],
        "action": str,
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
    total=False,
)

ClientDescribeJobResponsejobabortConfigTypeDef = TypedDict(
    "ClientDescribeJobResponsejobabortConfigTypeDef",
    {"criteriaList": List[ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef]},
    total=False,
)

ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)

ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
    total=False,
)

ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef = TypedDict(
    "ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)

ClientDescribeJobResponsejobjobProcessDetailsTypeDef = TypedDict(
    "ClientDescribeJobResponsejobjobProcessDetailsTypeDef",
    {
        "processingTargets": List[str],
        "numberOfCanceledThings": int,
        "numberOfSucceededThings": int,
        "numberOfFailedThings": int,
        "numberOfRejectedThings": int,
        "numberOfQueuedThings": int,
        "numberOfInProgressThings": int,
        "numberOfRemovedThings": int,
        "numberOfTimedOutThings": int,
    },
    total=False,
)

ClientDescribeJobResponsejobpresignedUrlConfigTypeDef = TypedDict(
    "ClientDescribeJobResponsejobpresignedUrlConfigTypeDef",
    {"roleArn": str, "expiresInSec": int},
    total=False,
)

ClientDescribeJobResponsejobtimeoutConfigTypeDef = TypedDict(
    "ClientDescribeJobResponsejobtimeoutConfigTypeDef",
    {"inProgressTimeoutInMinutes": int},
    total=False,
)

ClientDescribeJobResponsejobTypeDef = TypedDict(
    "ClientDescribeJobResponsejobTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "targetSelection": Literal["CONTINUOUS", "SNAPSHOT"],
        "status": Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"],
        "forceCanceled": bool,
        "reasonCode": str,
        "comment": str,
        "targets": List[str],
        "description": str,
        "presignedUrlConfig": ClientDescribeJobResponsejobpresignedUrlConfigTypeDef,
        "jobExecutionsRolloutConfig": ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef,
        "abortConfig": ClientDescribeJobResponsejobabortConfigTypeDef,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
        "jobProcessDetails": ClientDescribeJobResponsejobjobProcessDetailsTypeDef,
        "timeoutConfig": ClientDescribeJobResponsejobtimeoutConfigTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseTypeDef = TypedDict(
    "ClientDescribeJobResponseTypeDef",
    {"documentSource": str, "job": ClientDescribeJobResponsejobTypeDef},
    total=False,
)

ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)

ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)

ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)

ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)

ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)

ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef",
    {"action": str},
    total=False,
)

ClientDescribeMitigationActionResponseactionParamsTypeDef = TypedDict(
    "ClientDescribeMitigationActionResponseactionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)

ClientDescribeMitigationActionResponseTypeDef = TypedDict(
    "ClientDescribeMitigationActionResponseTypeDef",
    {
        "actionName": str,
        "actionType": Literal[
            "UPDATE_DEVICE_CERTIFICATE",
            "UPDATE_CA_CERTIFICATE",
            "ADD_THINGS_TO_THING_GROUP",
            "REPLACE_DEFAULT_POLICY_VERSION",
            "ENABLE_IOT_LOGGING",
            "PUBLISH_FINDING_TO_SNS",
        ],
        "actionArn": str,
        "actionId": str,
        "roleArn": str,
        "actionParams": ClientDescribeMitigationActionResponseactionParamsTypeDef,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

ClientDescribeProvisioningTemplateResponseTypeDef = TypedDict(
    "ClientDescribeProvisioningTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "defaultVersionId": int,
        "templateBody": str,
        "enabled": bool,
        "provisioningRoleArn": str,
    },
    total=False,
)

ClientDescribeProvisioningTemplateVersionResponseTypeDef = TypedDict(
    "ClientDescribeProvisioningTemplateVersionResponseTypeDef",
    {"versionId": int, "creationDate": datetime, "templateBody": str, "isDefaultVersion": bool},
    total=False,
)

ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef = TypedDict(
    "ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "roleArn": str,
        "owner": str,
        "credentialDurationSeconds": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

ClientDescribeRoleAliasResponseTypeDef = TypedDict(
    "ClientDescribeRoleAliasResponseTypeDef",
    {"roleAliasDescription": ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef},
    total=False,
)

ClientDescribeScheduledAuditResponseTypeDef = TypedDict(
    "ClientDescribeScheduledAuditResponseTypeDef",
    {
        "frequency": Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        "dayOfMonth": str,
        "dayOfWeek": Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"],
        "targetCheckNames": List[str],
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
    },
    total=False,
)

ClientDescribeSecurityProfileResponsealertTargetsTypeDef = TypedDict(
    "ClientDescribeSecurityProfileResponsealertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)

ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef = TypedDict(
    "ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef = TypedDict(
    "ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

ClientDescribeSecurityProfileResponsebehaviorsTypeDef = TypedDict(
    "ClientDescribeSecurityProfileResponsebehaviorsTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef,
    },
    total=False,
)

ClientDescribeSecurityProfileResponseTypeDef = TypedDict(
    "ClientDescribeSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List[ClientDescribeSecurityProfileResponsebehaviorsTypeDef],
        "alertTargets": Dict[str, ClientDescribeSecurityProfileResponsealertTargetsTypeDef],
        "additionalMetricsToRetain": List[str],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef = TypedDict(
    "ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)

ClientDescribeStreamResponsestreamInfofilesTypeDef = TypedDict(
    "ClientDescribeStreamResponsestreamInfofilesTypeDef",
    {"fileId": int, "s3Location": ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef},
    total=False,
)

ClientDescribeStreamResponsestreamInfoTypeDef = TypedDict(
    "ClientDescribeStreamResponsestreamInfoTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
        "files": List[ClientDescribeStreamResponsestreamInfofilesTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "roleArn": str,
    },
    total=False,
)

ClientDescribeStreamResponseTypeDef = TypedDict(
    "ClientDescribeStreamResponseTypeDef",
    {"streamInfo": ClientDescribeStreamResponsestreamInfoTypeDef},
    total=False,
)

ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef = TypedDict(
    "ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)

ClientDescribeThingGroupResponsethingGroupMetadataTypeDef = TypedDict(
    "ClientDescribeThingGroupResponsethingGroupMetadataTypeDef",
    {
        "parentGroupName": str,
        "rootToParentThingGroups": List[
            ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef
        ],
        "creationDate": datetime,
    },
    total=False,
)

ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)

ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef = TypedDict(
    "ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)

ClientDescribeThingGroupResponseTypeDef = TypedDict(
    "ClientDescribeThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupArn": str,
        "version": int,
        "thingGroupProperties": ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef,
        "thingGroupMetadata": ClientDescribeThingGroupResponsethingGroupMetadataTypeDef,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "status": Literal["ACTIVE", "BUILDING", "REBUILDING"],
    },
    total=False,
)

ClientDescribeThingRegistrationTaskResponseTypeDef = TypedDict(
    "ClientDescribeThingRegistrationTaskResponseTypeDef",
    {
        "taskId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
        "status": Literal["InProgress", "Completed", "Failed", "Cancelled", "Cancelling"],
        "message": str,
        "successCount": int,
        "failureCount": int,
        "percentageProgress": int,
    },
    total=False,
)

ClientDescribeThingResponseTypeDef = TypedDict(
    "ClientDescribeThingResponseTypeDef",
    {
        "defaultClientId": str,
        "thingName": str,
        "thingId": str,
        "thingArn": str,
        "thingTypeName": str,
        "attributes": Dict[str, str],
        "version": int,
        "billingGroupName": str,
    },
    total=False,
)

ClientDescribeThingTypeResponsethingTypeMetadataTypeDef = TypedDict(
    "ClientDescribeThingTypeResponsethingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)

ClientDescribeThingTypeResponsethingTypePropertiesTypeDef = TypedDict(
    "ClientDescribeThingTypeResponsethingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)

ClientDescribeThingTypeResponseTypeDef = TypedDict(
    "ClientDescribeThingTypeResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeId": str,
        "thingTypeArn": str,
        "thingTypeProperties": ClientDescribeThingTypeResponsethingTypePropertiesTypeDef,
        "thingTypeMetadata": ClientDescribeThingTypeResponsethingTypeMetadataTypeDef,
    },
    total=False,
)

ClientGetCardinalityResponseTypeDef = TypedDict(
    "ClientGetCardinalityResponseTypeDef", {"cardinality": int}, total=False
)

ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef = TypedDict(
    "ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef",
    {"policyName": str, "policyArn": str, "policyDocument": str},
    total=False,
)

ClientGetEffectivePoliciesResponseTypeDef = TypedDict(
    "ClientGetEffectivePoliciesResponseTypeDef",
    {"effectivePolicies": List[ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef]},
    total=False,
)

ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)

ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)

ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef = TypedDict(
    "ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef",
    {
        "thingGroupIndexingMode": Literal["OFF", "ON"],
        "managedFields": List[
            ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)

ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)

ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)

ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef = TypedDict(
    "ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef",
    {
        "thingIndexingMode": Literal["OFF", "REGISTRY", "REGISTRY_AND_SHADOW"],
        "thingConnectivityIndexingMode": Literal["OFF", "STATUS"],
        "managedFields": List[
            ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)

ClientGetIndexingConfigurationResponseTypeDef = TypedDict(
    "ClientGetIndexingConfigurationResponseTypeDef",
    {
        "thingIndexingConfiguration": ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef,
        "thingGroupIndexingConfiguration": ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef,
    },
    total=False,
)

ClientGetJobDocumentResponseTypeDef = TypedDict(
    "ClientGetJobDocumentResponseTypeDef", {"document": str}, total=False
)

ClientGetLoggingOptionsResponseTypeDef = TypedDict(
    "ClientGetLoggingOptionsResponseTypeDef",
    {"roleArn": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef",
    {"maximumPerMinute": int},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef",
    {"code": str, "message": str},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef",
    {"certificateName": str, "inlineDocument": str},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef",
    {"inlineDocument": bytes},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef",
    {
        "signature": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef,
        "certificateChain": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef,
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef",
    {"bucket": str, "prefix": str},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef",
    {
        "s3Destination": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
    },
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef",
    {"certificateArn": str, "platform": str, "certificatePathOnDevice": str},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef,
        "signingProfileName": str,
        "destination": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef,
    },
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef,
        "customCodeSigning": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef,
    },
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef",
    {"streamId": str, "fileId": int},
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef",
    {
        "stream": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef,
        "s3Location": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef,
    },
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef",
    {
        "fileName": str,
        "fileVersion": str,
        "fileLocation": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef,
        "codeSigning": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef,
        "attributes": Dict[str, str],
    },
    total=False,
)

ClientGetOtaUpdateResponseotaUpdateInfoTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseotaUpdateInfoTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "description": str,
        "targets": List[str],
        "awsJobExecutionsRolloutConfig": ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef,
        "targetSelection": Literal["CONTINUOUS", "SNAPSHOT"],
        "otaUpdateFiles": List[ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef],
        "otaUpdateStatus": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ],
        "awsIotJobId": str,
        "awsIotJobArn": str,
        "errorInfo": ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef,
        "additionalParameters": Dict[str, str],
    },
    total=False,
)

ClientGetOtaUpdateResponseTypeDef = TypedDict(
    "ClientGetOtaUpdateResponseTypeDef",
    {"otaUpdateInfo": ClientGetOtaUpdateResponseotaUpdateInfoTypeDef},
    total=False,
)

ClientGetPercentilesResponsepercentilesTypeDef = TypedDict(
    "ClientGetPercentilesResponsepercentilesTypeDef",
    {"percent": float, "value": float},
    total=False,
)

ClientGetPercentilesResponseTypeDef = TypedDict(
    "ClientGetPercentilesResponseTypeDef",
    {"percentiles": List[ClientGetPercentilesResponsepercentilesTypeDef]},
    total=False,
)

ClientGetPolicyResponseTypeDef = TypedDict(
    "ClientGetPolicyResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "defaultVersionId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
    },
    total=False,
)

ClientGetPolicyVersionResponseTypeDef = TypedDict(
    "ClientGetPolicyVersionResponseTypeDef",
    {
        "policyArn": str,
        "policyName": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
    },
    total=False,
)

ClientGetRegistrationCodeResponseTypeDef = TypedDict(
    "ClientGetRegistrationCodeResponseTypeDef", {"registrationCode": str}, total=False
)

ClientGetStatisticsResponsestatisticsTypeDef = TypedDict(
    "ClientGetStatisticsResponsestatisticsTypeDef",
    {
        "count": int,
        "average": float,
        "sum": float,
        "minimum": float,
        "maximum": float,
        "sumOfSquares": float,
        "variance": float,
        "stdDeviation": float,
    },
    total=False,
)

ClientGetStatisticsResponseTypeDef = TypedDict(
    "ClientGetStatisticsResponseTypeDef",
    {"statistics": ClientGetStatisticsResponsestatisticsTypeDef},
    total=False,
)

ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef = TypedDict(
    "ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef",
    {"confirmationUrl": str},
    total=False,
)

ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef = TypedDict(
    "ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef",
    {
        "arn": str,
        "status": Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"],
        "statusReason": str,
        "httpUrlProperties": ClientGetTopicRuleDestinationResponsetopicRuleDestinationhttpUrlPropertiesTypeDef,
    },
    total=False,
)

ClientGetTopicRuleDestinationResponseTypeDef = TypedDict(
    "ClientGetTopicRuleDestinationResponseTypeDef",
    {"topicRuleDestination": ClientGetTopicRuleDestinationResponsetopicRuleDestinationTypeDef},
    total=False,
)

ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)

ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)

ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef", {"tableName": str}, total=False
)

ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef",
    {"roleArn": str, "putItem": ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef},
    total=False,
)

ClientGetTopicRuleResponseruleactionselasticsearchTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionsfirehoseTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionshttpauthTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionshttpauthTypeDef",
    {"sigv4": ClientGetTopicRuleResponseruleactionshttpauthsigv4TypeDef},
    total=False,
)

ClientGetTopicRuleResponseruleactionshttpheadersTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionshttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionshttpTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionshttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientGetTopicRuleResponseruleactionshttpheadersTypeDef],
        "auth": ClientGetTopicRuleResponseruleactionshttpauthTypeDef,
    },
    total=False,
)

ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionsiotEventsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsiotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)

ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)

ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientGetTopicRuleResponseruleactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)

ClientGetTopicRuleResponseruleactionskinesisTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionskinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionslambdaTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionslambdaTypeDef", {"functionArn": str}, total=False
)

ClientGetTopicRuleResponseruleactionsrepublishTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)

ClientGetTopicRuleResponseruleactionss3TypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionss3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)

ClientGetTopicRuleResponseruleactionssalesforceTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionssalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionssnsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionssnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)

ClientGetTopicRuleResponseruleactionssqsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)

ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)

ClientGetTopicRuleResponseruleactionsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleactionsTypeDef",
    {
        "dynamoDB": ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef,
        "lambda": ClientGetTopicRuleResponseruleactionslambdaTypeDef,
        "sns": ClientGetTopicRuleResponseruleactionssnsTypeDef,
        "sqs": ClientGetTopicRuleResponseruleactionssqsTypeDef,
        "kinesis": ClientGetTopicRuleResponseruleactionskinesisTypeDef,
        "republish": ClientGetTopicRuleResponseruleactionsrepublishTypeDef,
        "s3": ClientGetTopicRuleResponseruleactionss3TypeDef,
        "firehose": ClientGetTopicRuleResponseruleactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientGetTopicRuleResponseruleactionselasticsearchTypeDef,
        "salesforce": ClientGetTopicRuleResponseruleactionssalesforceTypeDef,
        "iotAnalytics": ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef,
        "iotEvents": ClientGetTopicRuleResponseruleactionsiotEventsTypeDef,
        "iotSiteWise": ClientGetTopicRuleResponseruleactionsiotSiteWiseTypeDef,
        "stepFunctions": ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef,
        "http": ClientGetTopicRuleResponseruleactionshttpTypeDef,
    },
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)

ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)

ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef",
    {"roleArn": str, "putItem": ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef",
    {"sigv4": ClientGetTopicRuleResponseruleerrorActionhttpauthsigv4TypeDef},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionhttpTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionhttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientGetTopicRuleResponseruleerrorActionhttpheadersTypeDef],
        "auth": ClientGetTopicRuleResponseruleerrorActionhttpauthTypeDef,
    },
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)

ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientGetTopicRuleResponseruleerrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef", {"functionArn": str}, total=False
)

ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActions3TypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActions3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionsnsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionsqsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)

ClientGetTopicRuleResponseruleerrorActionTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleerrorActionTypeDef",
    {
        "dynamoDB": ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef,
        "lambda": ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef,
        "sns": ClientGetTopicRuleResponseruleerrorActionsnsTypeDef,
        "sqs": ClientGetTopicRuleResponseruleerrorActionsqsTypeDef,
        "kinesis": ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef,
        "republish": ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef,
        "s3": ClientGetTopicRuleResponseruleerrorActions3TypeDef,
        "firehose": ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef,
        "salesforce": ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef,
        "iotAnalytics": ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef,
        "iotSiteWise": ClientGetTopicRuleResponseruleerrorActioniotSiteWiseTypeDef,
        "stepFunctions": ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef,
        "http": ClientGetTopicRuleResponseruleerrorActionhttpTypeDef,
    },
    total=False,
)

ClientGetTopicRuleResponseruleTypeDef = TypedDict(
    "ClientGetTopicRuleResponseruleTypeDef",
    {
        "ruleName": str,
        "sql": str,
        "description": str,
        "createdAt": datetime,
        "actions": List[ClientGetTopicRuleResponseruleactionsTypeDef],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientGetTopicRuleResponseruleerrorActionTypeDef,
    },
    total=False,
)

ClientGetTopicRuleResponseTypeDef = TypedDict(
    "ClientGetTopicRuleResponseTypeDef",
    {"ruleArn": str, "rule": ClientGetTopicRuleResponseruleTypeDef},
    total=False,
)

ClientGetV2LoggingOptionsResponseTypeDef = TypedDict(
    "ClientGetV2LoggingOptionsResponseTypeDef",
    {
        "roleArn": str,
        "defaultLogLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
        "disableAllLogs": bool,
    },
    total=False,
)

ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef = TypedDict(
    "ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef = TypedDict(
    "ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef = TypedDict(
    "ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef,
    },
    total=False,
)

ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef = TypedDict(
    "ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientListActiveViolationsResponseactiveViolationsTypeDef = TypedDict(
    "ClientListActiveViolationsResponseactiveViolationsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef,
        "lastViolationValue": ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef,
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)

ClientListActiveViolationsResponseTypeDef = TypedDict(
    "ClientListActiveViolationsResponseTypeDef",
    {
        "activeViolations": List[ClientListActiveViolationsResponseactiveViolationsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListAttachedPoliciesResponsepoliciesTypeDef = TypedDict(
    "ClientListAttachedPoliciesResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)

ClientListAttachedPoliciesResponseTypeDef = TypedDict(
    "ClientListAttachedPoliciesResponseTypeDef",
    {"policies": List[ClientListAttachedPoliciesResponsepoliciesTypeDef], "nextMarker": str},
    total=False,
)

ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)

ClientListAuditFindingsResourceIdentifierTypeDef = TypedDict(
    "ClientListAuditFindingsResourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsResourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)

ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)

ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)

ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef = TypedDict(
    "ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)

ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)

ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef = TypedDict(
    "ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

ClientListAuditFindingsResponsefindingsTypeDef = TypedDict(
    "ClientListAuditFindingsResponsefindingsTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"],
        "nonCompliantResource": ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef,
        "relatedResources": List[ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)

ClientListAuditFindingsResponseTypeDef = TypedDict(
    "ClientListAuditFindingsResponseTypeDef",
    {"findings": List[ClientListAuditFindingsResponsefindingsTypeDef], "nextToken": str},
    total=False,
)

ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef = TypedDict(
    "ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef",
    {
        "taskId": str,
        "findingId": str,
        "actionName": str,
        "actionId": str,
        "status": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED", "SKIPPED", "PENDING"],
        "startTime": datetime,
        "endTime": datetime,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

ClientListAuditMitigationActionsExecutionsResponseTypeDef = TypedDict(
    "ClientListAuditMitigationActionsExecutionsResponseTypeDef",
    {
        "actionsExecutions": List[
            ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListAuditMitigationActionsTasksResponsetasksTypeDef = TypedDict(
    "ClientListAuditMitigationActionsTasksResponsetasksTypeDef",
    {
        "taskId": str,
        "startTime": datetime,
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
    },
    total=False,
)

ClientListAuditMitigationActionsTasksResponseTypeDef = TypedDict(
    "ClientListAuditMitigationActionsTasksResponseTypeDef",
    {"tasks": List[ClientListAuditMitigationActionsTasksResponsetasksTypeDef], "nextToken": str},
    total=False,
)

ClientListAuditTasksResponsetasksTypeDef = TypedDict(
    "ClientListAuditTasksResponsetasksTypeDef",
    {
        "taskId": str,
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
        "taskType": Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"],
    },
    total=False,
)

ClientListAuditTasksResponseTypeDef = TypedDict(
    "ClientListAuditTasksResponseTypeDef",
    {"tasks": List[ClientListAuditTasksResponsetasksTypeDef], "nextToken": str},
    total=False,
)

ClientListAuthorizersResponseauthorizersTypeDef = TypedDict(
    "ClientListAuthorizersResponseauthorizersTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)

ClientListAuthorizersResponseTypeDef = TypedDict(
    "ClientListAuthorizersResponseTypeDef",
    {"authorizers": List[ClientListAuthorizersResponseauthorizersTypeDef], "nextMarker": str},
    total=False,
)

ClientListBillingGroupsResponsebillingGroupsTypeDef = TypedDict(
    "ClientListBillingGroupsResponsebillingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)

ClientListBillingGroupsResponseTypeDef = TypedDict(
    "ClientListBillingGroupsResponseTypeDef",
    {"billingGroups": List[ClientListBillingGroupsResponsebillingGroupsTypeDef], "nextToken": str},
    total=False,
)

ClientListCaCertificatesResponsecertificatesTypeDef = TypedDict(
    "ClientListCaCertificatesResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal["ACTIVE", "INACTIVE"],
        "creationDate": datetime,
    },
    total=False,
)

ClientListCaCertificatesResponseTypeDef = TypedDict(
    "ClientListCaCertificatesResponseTypeDef",
    {"certificates": List[ClientListCaCertificatesResponsecertificatesTypeDef], "nextMarker": str},
    total=False,
)

ClientListCertificatesByCaResponsecertificatesTypeDef = TypedDict(
    "ClientListCertificatesByCaResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "creationDate": datetime,
    },
    total=False,
)

ClientListCertificatesByCaResponseTypeDef = TypedDict(
    "ClientListCertificatesByCaResponseTypeDef",
    {
        "certificates": List[ClientListCertificatesByCaResponsecertificatesTypeDef],
        "nextMarker": str,
    },
    total=False,
)

ClientListCertificatesResponsecertificatesTypeDef = TypedDict(
    "ClientListCertificatesResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "creationDate": datetime,
    },
    total=False,
)

ClientListCertificatesResponseTypeDef = TypedDict(
    "ClientListCertificatesResponseTypeDef",
    {"certificates": List[ClientListCertificatesResponsecertificatesTypeDef], "nextMarker": str},
    total=False,
)

ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef = TypedDict(
    "ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "serviceType": Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"],
    },
    total=False,
)

ClientListDomainConfigurationsResponseTypeDef = TypedDict(
    "ClientListDomainConfigurationsResponseTypeDef",
    {
        "domainConfigurations": List[
            ClientListDomainConfigurationsResponsedomainConfigurationsTypeDef
        ],
        "nextMarker": str,
    },
    total=False,
)

ClientListIndicesResponseTypeDef = TypedDict(
    "ClientListIndicesResponseTypeDef", {"indexNames": List[str], "nextToken": str}, total=False
)

ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)

ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef = TypedDict(
    "ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)

ClientListJobExecutionsForJobResponseTypeDef = TypedDict(
    "ClientListJobExecutionsForJobResponseTypeDef",
    {
        "executionSummaries": List[ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)

ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef = TypedDict(
    "ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)

ClientListJobExecutionsForThingResponseTypeDef = TypedDict(
    "ClientListJobExecutionsForThingResponseTypeDef",
    {
        "executionSummaries": List[
            ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListJobsResponsejobsTypeDef = TypedDict(
    "ClientListJobsResponsejobsTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": Literal["CONTINUOUS", "SNAPSHOT"],
        "status": Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"jobs": List[ClientListJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)

ClientListMitigationActionsResponseactionIdentifiersTypeDef = TypedDict(
    "ClientListMitigationActionsResponseactionIdentifiersTypeDef",
    {"actionName": str, "actionArn": str, "creationDate": datetime},
    total=False,
)

ClientListMitigationActionsResponseTypeDef = TypedDict(
    "ClientListMitigationActionsResponseTypeDef",
    {
        "actionIdentifiers": List[ClientListMitigationActionsResponseactionIdentifiersTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListOtaUpdatesResponseotaUpdatesTypeDef = TypedDict(
    "ClientListOtaUpdatesResponseotaUpdatesTypeDef",
    {"otaUpdateId": str, "otaUpdateArn": str, "creationDate": datetime},
    total=False,
)

ClientListOtaUpdatesResponseTypeDef = TypedDict(
    "ClientListOtaUpdatesResponseTypeDef",
    {"otaUpdates": List[ClientListOtaUpdatesResponseotaUpdatesTypeDef], "nextToken": str},
    total=False,
)

ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef = TypedDict(
    "ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
    },
    total=False,
)

ClientListOutgoingCertificatesResponseTypeDef = TypedDict(
    "ClientListOutgoingCertificatesResponseTypeDef",
    {
        "outgoingCertificates": List[
            ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef
        ],
        "nextMarker": str,
    },
    total=False,
)

ClientListPoliciesResponsepoliciesTypeDef = TypedDict(
    "ClientListPoliciesResponsepoliciesTypeDef", {"policyName": str, "policyArn": str}, total=False
)

ClientListPoliciesResponseTypeDef = TypedDict(
    "ClientListPoliciesResponseTypeDef",
    {"policies": List[ClientListPoliciesResponsepoliciesTypeDef], "nextMarker": str},
    total=False,
)

ClientListPolicyPrincipalsResponseTypeDef = TypedDict(
    "ClientListPolicyPrincipalsResponseTypeDef",
    {"principals": List[str], "nextMarker": str},
    total=False,
)

ClientListPolicyVersionsResponsepolicyVersionsTypeDef = TypedDict(
    "ClientListPolicyVersionsResponsepolicyVersionsTypeDef",
    {"versionId": str, "isDefaultVersion": bool, "createDate": datetime},
    total=False,
)

ClientListPolicyVersionsResponseTypeDef = TypedDict(
    "ClientListPolicyVersionsResponseTypeDef",
    {"policyVersions": List[ClientListPolicyVersionsResponsepolicyVersionsTypeDef]},
    total=False,
)

ClientListPrincipalPoliciesResponsepoliciesTypeDef = TypedDict(
    "ClientListPrincipalPoliciesResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)

ClientListPrincipalPoliciesResponseTypeDef = TypedDict(
    "ClientListPrincipalPoliciesResponseTypeDef",
    {"policies": List[ClientListPrincipalPoliciesResponsepoliciesTypeDef], "nextMarker": str},
    total=False,
)

ClientListPrincipalThingsResponseTypeDef = TypedDict(
    "ClientListPrincipalThingsResponseTypeDef", {"things": List[str], "nextToken": str}, total=False
)

ClientListProvisioningTemplateVersionsResponseversionsTypeDef = TypedDict(
    "ClientListProvisioningTemplateVersionsResponseversionsTypeDef",
    {"versionId": int, "creationDate": datetime, "isDefaultVersion": bool},
    total=False,
)

ClientListProvisioningTemplateVersionsResponseTypeDef = TypedDict(
    "ClientListProvisioningTemplateVersionsResponseTypeDef",
    {
        "versions": List[ClientListProvisioningTemplateVersionsResponseversionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListProvisioningTemplatesResponsetemplatesTypeDef = TypedDict(
    "ClientListProvisioningTemplatesResponsetemplatesTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "enabled": bool,
    },
    total=False,
)

ClientListProvisioningTemplatesResponseTypeDef = TypedDict(
    "ClientListProvisioningTemplatesResponseTypeDef",
    {"templates": List[ClientListProvisioningTemplatesResponsetemplatesTypeDef], "nextToken": str},
    total=False,
)

ClientListRoleAliasesResponseTypeDef = TypedDict(
    "ClientListRoleAliasesResponseTypeDef",
    {"roleAliases": List[str], "nextMarker": str},
    total=False,
)

ClientListScheduledAuditsResponsescheduledAuditsTypeDef = TypedDict(
    "ClientListScheduledAuditsResponsescheduledAuditsTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        "dayOfMonth": str,
        "dayOfWeek": Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"],
    },
    total=False,
)

ClientListScheduledAuditsResponseTypeDef = TypedDict(
    "ClientListScheduledAuditsResponseTypeDef",
    {
        "scheduledAudits": List[ClientListScheduledAuditsResponsescheduledAuditsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef = TypedDict(
    "ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef",
    {"name": str, "arn": str},
    total=False,
)

ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef = TypedDict(
    "ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef",
    {"arn": str},
    total=False,
)

ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef = TypedDict(
    "ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef",
    {
        "securityProfileIdentifier": ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef,
        "target": ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef,
    },
    total=False,
)

ClientListSecurityProfilesForTargetResponseTypeDef = TypedDict(
    "ClientListSecurityProfilesForTargetResponseTypeDef",
    {
        "securityProfileTargetMappings": List[
            ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef = TypedDict(
    "ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef",
    {"name": str, "arn": str},
    total=False,
)

ClientListSecurityProfilesResponseTypeDef = TypedDict(
    "ClientListSecurityProfilesResponseTypeDef",
    {
        "securityProfileIdentifiers": List[
            ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListStreamsResponsestreamsTypeDef = TypedDict(
    "ClientListStreamsResponsestreamsTypeDef",
    {"streamId": str, "streamArn": str, "streamVersion": int, "description": str},
    total=False,
)

ClientListStreamsResponseTypeDef = TypedDict(
    "ClientListStreamsResponseTypeDef",
    {"streams": List[ClientListStreamsResponsestreamsTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)

ClientListTargetsForPolicyResponseTypeDef = TypedDict(
    "ClientListTargetsForPolicyResponseTypeDef",
    {"targets": List[str], "nextMarker": str},
    total=False,
)

ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef = TypedDict(
    "ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef",
    {"arn": str},
    total=False,
)

ClientListTargetsForSecurityProfileResponseTypeDef = TypedDict(
    "ClientListTargetsForSecurityProfileResponseTypeDef",
    {
        "securityProfileTargets": List[
            ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListThingGroupsForThingResponsethingGroupsTypeDef = TypedDict(
    "ClientListThingGroupsForThingResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)

ClientListThingGroupsForThingResponseTypeDef = TypedDict(
    "ClientListThingGroupsForThingResponseTypeDef",
    {
        "thingGroups": List[ClientListThingGroupsForThingResponsethingGroupsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListThingGroupsResponsethingGroupsTypeDef = TypedDict(
    "ClientListThingGroupsResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)

ClientListThingGroupsResponseTypeDef = TypedDict(
    "ClientListThingGroupsResponseTypeDef",
    {"thingGroups": List[ClientListThingGroupsResponsethingGroupsTypeDef], "nextToken": str},
    total=False,
)

ClientListThingPrincipalsResponseTypeDef = TypedDict(
    "ClientListThingPrincipalsResponseTypeDef", {"principals": List[str]}, total=False
)

ClientListThingRegistrationTaskReportsResponseTypeDef = TypedDict(
    "ClientListThingRegistrationTaskReportsResponseTypeDef",
    {"resourceLinks": List[str], "reportType": Literal["ERRORS", "RESULTS"], "nextToken": str},
    total=False,
)

ClientListThingRegistrationTasksResponseTypeDef = TypedDict(
    "ClientListThingRegistrationTasksResponseTypeDef",
    {"taskIds": List[str], "nextToken": str},
    total=False,
)

ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef = TypedDict(
    "ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)

ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef = TypedDict(
    "ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)

ClientListThingTypesResponsethingTypesTypeDef = TypedDict(
    "ClientListThingTypesResponsethingTypesTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef,
        "thingTypeMetadata": ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef,
    },
    total=False,
)

ClientListThingTypesResponseTypeDef = TypedDict(
    "ClientListThingTypesResponseTypeDef",
    {"thingTypes": List[ClientListThingTypesResponsethingTypesTypeDef], "nextToken": str},
    total=False,
)

ClientListThingsInBillingGroupResponseTypeDef = TypedDict(
    "ClientListThingsInBillingGroupResponseTypeDef",
    {"things": List[str], "nextToken": str},
    total=False,
)

ClientListThingsInThingGroupResponseTypeDef = TypedDict(
    "ClientListThingsInThingGroupResponseTypeDef",
    {"things": List[str], "nextToken": str},
    total=False,
)

ClientListThingsResponsethingsTypeDef = TypedDict(
    "ClientListThingsResponsethingsTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)

ClientListThingsResponseTypeDef = TypedDict(
    "ClientListThingsResponseTypeDef",
    {"things": List[ClientListThingsResponsethingsTypeDef], "nextToken": str},
    total=False,
)

ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef = TypedDict(
    "ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef",
    {"confirmationUrl": str},
    total=False,
)

ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef = TypedDict(
    "ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef",
    {
        "arn": str,
        "status": Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"],
        "statusReason": str,
        "httpUrlSummary": ClientListTopicRuleDestinationsResponsedestinationSummarieshttpUrlSummaryTypeDef,
    },
    total=False,
)

ClientListTopicRuleDestinationsResponseTypeDef = TypedDict(
    "ClientListTopicRuleDestinationsResponseTypeDef",
    {
        "destinationSummaries": List[
            ClientListTopicRuleDestinationsResponsedestinationSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListTopicRulesResponserulesTypeDef = TypedDict(
    "ClientListTopicRulesResponserulesTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)

ClientListTopicRulesResponseTypeDef = TypedDict(
    "ClientListTopicRulesResponseTypeDef",
    {"rules": List[ClientListTopicRulesResponserulesTypeDef], "nextToken": str},
    total=False,
)

ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef = TypedDict(
    "ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef",
    {"targetType": Literal["DEFAULT", "THING_GROUP"], "targetName": str},
    total=False,
)

ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef = TypedDict(
    "ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef",
    {
        "logTarget": ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef,
        "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
    },
    total=False,
)

ClientListV2LoggingLevelsResponseTypeDef = TypedDict(
    "ClientListV2LoggingLevelsResponseTypeDef",
    {
        "logTargetConfigurations": List[
            ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef = TypedDict(
    "ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef = TypedDict(
    "ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

ClientListViolationEventsResponseviolationEventsbehaviorTypeDef = TypedDict(
    "ClientListViolationEventsResponseviolationEventsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef,
    },
    total=False,
)

ClientListViolationEventsResponseviolationEventsmetricValueTypeDef = TypedDict(
    "ClientListViolationEventsResponseviolationEventsmetricValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientListViolationEventsResponseviolationEventsTypeDef = TypedDict(
    "ClientListViolationEventsResponseviolationEventsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ClientListViolationEventsResponseviolationEventsbehaviorTypeDef,
        "metricValue": ClientListViolationEventsResponseviolationEventsmetricValueTypeDef,
        "violationEventType": Literal["in-alarm", "alarm-cleared", "alarm-invalidated"],
        "violationEventTime": datetime,
    },
    total=False,
)

ClientListViolationEventsResponseTypeDef = TypedDict(
    "ClientListViolationEventsResponseTypeDef",
    {
        "violationEvents": List[ClientListViolationEventsResponseviolationEventsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientRegisterCaCertificateRegistrationConfigTypeDef = TypedDict(
    "ClientRegisterCaCertificateRegistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)

ClientRegisterCaCertificateResponseTypeDef = TypedDict(
    "ClientRegisterCaCertificateResponseTypeDef",
    {"certificateArn": str, "certificateId": str},
    total=False,
)

ClientRegisterCertificateResponseTypeDef = TypedDict(
    "ClientRegisterCertificateResponseTypeDef",
    {"certificateArn": str, "certificateId": str},
    total=False,
)

ClientRegisterThingResponseTypeDef = TypedDict(
    "ClientRegisterThingResponseTypeDef",
    {"certificatePem": str, "resourceArns": Dict[str, str]},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2putItemTypeDef,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef",
    {"sigv4": ClientReplaceTopicRuleTopicRulePayloadactionshttpauthsigv4TypeDef},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientReplaceTopicRuleTopicRulePayloadactionshttpheadersTypeDef],
        "auth": ClientReplaceTopicRuleTopicRulePayloadactionshttpauthTypeDef,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef", {"functionArn": str}, total=False
)

ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef",
    {
        "dynamoDB": ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientReplaceTopicRuleTopicRulePayloadactionsdynamoDBv2TypeDef,
        "lambda": ClientReplaceTopicRuleTopicRulePayloadactionslambdaTypeDef,
        "sns": ClientReplaceTopicRuleTopicRulePayloadactionssnsTypeDef,
        "sqs": ClientReplaceTopicRuleTopicRulePayloadactionssqsTypeDef,
        "kinesis": ClientReplaceTopicRuleTopicRulePayloadactionskinesisTypeDef,
        "republish": ClientReplaceTopicRuleTopicRulePayloadactionsrepublishTypeDef,
        "s3": ClientReplaceTopicRuleTopicRulePayloadactionss3TypeDef,
        "firehose": ClientReplaceTopicRuleTopicRulePayloadactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientReplaceTopicRuleTopicRulePayloadactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientReplaceTopicRuleTopicRulePayloadactionselasticsearchTypeDef,
        "salesforce": ClientReplaceTopicRuleTopicRulePayloadactionssalesforceTypeDef,
        "iotAnalytics": ClientReplaceTopicRuleTopicRulePayloadactionsiotAnalyticsTypeDef,
        "iotEvents": ClientReplaceTopicRuleTopicRulePayloadactionsiotEventsTypeDef,
        "iotSiteWise": ClientReplaceTopicRuleTopicRulePayloadactionsiotSiteWiseTypeDef,
        "stepFunctions": ClientReplaceTopicRuleTopicRulePayloadactionsstepFunctionsTypeDef,
        "http": ClientReplaceTopicRuleTopicRulePayloadactionshttpTypeDef,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": Literal["STRING", "NUMBER"],
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": Literal["STRING", "NUMBER"],
        "payloadField": str,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2putItemTypeDef,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef",
    {"signingRegion": str, "serviceName": str, "roleArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef",
    {"sigv4": ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthsigv4TypeDef},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef",
    {
        "url": str,
        "confirmationUrl": str,
        "headers": List[ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpheadersTypeDef],
        "auth": ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpauthTypeDef,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef",
    {"timeInSeconds": str, "offsetInNanos": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef",
    {"stringValue": str, "integerValue": str, "doubleValue": str, "booleanValue": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef",
    {
        "value": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesvalueTypeDef,
        "timestamp": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuestimestampTypeDef,
        "quality": str,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValues": List[
            ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriespropertyValuesTypeDef
        ],
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef",
    {
        "putAssetPropertyValueEntries": List[
            ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseputAssetPropertyValueEntriesTypeDef
        ],
        "roleArn": str,
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef",
    {"functionArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
        "cannedAcl": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "log-delivery-write",
        ],
    },
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": Literal["RAW", "JSON"]},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)

ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef = TypedDict(
    "ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef",
    {
        "dynamoDB": ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientReplaceTopicRuleTopicRulePayloaderrorActiondynamoDBv2TypeDef,
        "lambda": ClientReplaceTopicRuleTopicRulePayloaderrorActionlambdaTypeDef,
        "sns": ClientReplaceTopicRuleTopicRulePayloaderrorActionsnsTypeDef,
        "sqs": ClientReplaceTopicRuleTopicRulePayloaderrorActionsqsTypeDef,
        "kinesis": ClientReplaceTopicRuleTopicRulePayloaderrorActionkinesisTypeDef,
        "republish": ClientReplaceTopicRuleTopicRulePayloaderrorActionrepublishTypeDef,
        "s3": ClientReplaceTopicRuleTopicRulePayloaderrorActions3TypeDef,
        "firehose": ClientReplaceTopicRuleTopicRulePayloaderrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientReplaceTopicRuleTopicRulePayloaderrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientReplaceTopicRuleTopicRulePayloaderrorActionelasticsearchTypeDef,
        "salesforce": ClientReplaceTopicRuleTopicRulePayloaderrorActionsalesforceTypeDef,
        "iotAnalytics": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotEventsTypeDef,
        "iotSiteWise": ClientReplaceTopicRuleTopicRulePayloaderrorActioniotSiteWiseTypeDef,
        "stepFunctions": ClientReplaceTopicRuleTopicRulePayloaderrorActionstepFunctionsTypeDef,
        "http": ClientReplaceTopicRuleTopicRulePayloaderrorActionhttpTypeDef,
    },
    total=False,
)

_RequiredClientReplaceTopicRuleTopicRulePayloadTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuleTopicRulePayloadTypeDef", {"sql": str}
)
_OptionalClientReplaceTopicRuleTopicRulePayloadTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuleTopicRulePayloadTypeDef",
    {
        "description": str,
        "actions": List[ClientReplaceTopicRuleTopicRulePayloadactionsTypeDef],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientReplaceTopicRuleTopicRulePayloaderrorActionTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuleTopicRulePayloadTypeDef(
    _RequiredClientReplaceTopicRuleTopicRulePayloadTypeDef,
    _OptionalClientReplaceTopicRuleTopicRulePayloadTypeDef,
):
    pass


ClientSearchIndexResponsethingGroupsTypeDef = TypedDict(
    "ClientSearchIndexResponsethingGroupsTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupDescription": str,
        "attributes": Dict[str, str],
        "parentGroupNames": List[str],
    },
    total=False,
)

ClientSearchIndexResponsethingsconnectivityTypeDef = TypedDict(
    "ClientSearchIndexResponsethingsconnectivityTypeDef",
    {"connected": bool, "timestamp": int},
    total=False,
)

ClientSearchIndexResponsethingsTypeDef = TypedDict(
    "ClientSearchIndexResponsethingsTypeDef",
    {
        "thingName": str,
        "thingId": str,
        "thingTypeName": str,
        "thingGroupNames": List[str],
        "attributes": Dict[str, str],
        "shadow": str,
        "connectivity": ClientSearchIndexResponsethingsconnectivityTypeDef,
    },
    total=False,
)

ClientSearchIndexResponseTypeDef = TypedDict(
    "ClientSearchIndexResponseTypeDef",
    {
        "nextToken": str,
        "things": List[ClientSearchIndexResponsethingsTypeDef],
        "thingGroups": List[ClientSearchIndexResponsethingGroupsTypeDef],
    },
    total=False,
)

ClientSetDefaultAuthorizerResponseTypeDef = TypedDict(
    "ClientSetDefaultAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)

_RequiredClientSetLoggingOptionsLoggingOptionsPayloadTypeDef = TypedDict(
    "_RequiredClientSetLoggingOptionsLoggingOptionsPayloadTypeDef", {"roleArn": str}
)
_OptionalClientSetLoggingOptionsLoggingOptionsPayloadTypeDef = TypedDict(
    "_OptionalClientSetLoggingOptionsLoggingOptionsPayloadTypeDef",
    {"logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)


class ClientSetLoggingOptionsLoggingOptionsPayloadTypeDef(
    _RequiredClientSetLoggingOptionsLoggingOptionsPayloadTypeDef,
    _OptionalClientSetLoggingOptionsLoggingOptionsPayloadTypeDef,
):
    pass


_RequiredClientSetV2LoggingLevelLogTargetTypeDef = TypedDict(
    "_RequiredClientSetV2LoggingLevelLogTargetTypeDef",
    {"targetType": Literal["DEFAULT", "THING_GROUP"]},
)
_OptionalClientSetV2LoggingLevelLogTargetTypeDef = TypedDict(
    "_OptionalClientSetV2LoggingLevelLogTargetTypeDef", {"targetName": str}, total=False
)


class ClientSetV2LoggingLevelLogTargetTypeDef(
    _RequiredClientSetV2LoggingLevelLogTargetTypeDef,
    _OptionalClientSetV2LoggingLevelLogTargetTypeDef,
):
    pass


ClientStartAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "ClientStartAuditMitigationActionsTaskResponseTypeDef", {"taskId": str}, total=False
)

ClientStartAuditMitigationActionsTaskTargetTypeDef = TypedDict(
    "ClientStartAuditMitigationActionsTaskTargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)

ClientStartOnDemandAuditTaskResponseTypeDef = TypedDict(
    "ClientStartOnDemandAuditTaskResponseTypeDef", {"taskId": str}, total=False
)

ClientStartThingRegistrationTaskResponseTypeDef = TypedDict(
    "ClientStartThingRegistrationTaskResponseTypeDef", {"taskId": str}, total=False
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientTestAuthorizationAuthInfosTypeDef = TypedDict(
    "ClientTestAuthorizationAuthInfosTypeDef",
    {"actionType": Literal["PUBLISH", "SUBSCRIBE", "RECEIVE", "CONNECT"], "resources": List[str]},
    total=False,
)

ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)

ClientTestAuthorizationResponseauthResultsallowedTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsallowedTypeDef",
    {"policies": List[ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef]},
    total=False,
)

ClientTestAuthorizationResponseauthResultsauthInfoTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsauthInfoTypeDef",
    {"actionType": Literal["PUBLISH", "SUBSCRIBE", "RECEIVE", "CONNECT"], "resources": List[str]},
    total=False,
)

ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)

ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef",
    {"policies": List[ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef]},
    total=False,
)

ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)

ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef",
    {"policies": List[ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef]},
    total=False,
)

ClientTestAuthorizationResponseauthResultsdeniedTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsdeniedTypeDef",
    {
        "implicitDeny": ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef,
        "explicitDeny": ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef,
    },
    total=False,
)

ClientTestAuthorizationResponseauthResultsTypeDef = TypedDict(
    "ClientTestAuthorizationResponseauthResultsTypeDef",
    {
        "authInfo": ClientTestAuthorizationResponseauthResultsauthInfoTypeDef,
        "allowed": ClientTestAuthorizationResponseauthResultsallowedTypeDef,
        "denied": ClientTestAuthorizationResponseauthResultsdeniedTypeDef,
        "authDecision": Literal["ALLOWED", "EXPLICIT_DENY", "IMPLICIT_DENY"],
        "missingContextValues": List[str],
    },
    total=False,
)

ClientTestAuthorizationResponseTypeDef = TypedDict(
    "ClientTestAuthorizationResponseTypeDef",
    {"authResults": List[ClientTestAuthorizationResponseauthResultsTypeDef]},
    total=False,
)

ClientTestInvokeAuthorizerHttpContextTypeDef = TypedDict(
    "ClientTestInvokeAuthorizerHttpContextTypeDef",
    {"headers": Dict[str, str], "queryString": str},
    total=False,
)

ClientTestInvokeAuthorizerMqttContextTypeDef = TypedDict(
    "ClientTestInvokeAuthorizerMqttContextTypeDef",
    {"username": str, "password": bytes, "clientId": str},
    total=False,
)

ClientTestInvokeAuthorizerResponseTypeDef = TypedDict(
    "ClientTestInvokeAuthorizerResponseTypeDef",
    {
        "isAuthenticated": bool,
        "principalId": str,
        "policyDocuments": List[str],
        "refreshAfterInSeconds": int,
        "disconnectAfterInSeconds": int,
    },
    total=False,
)

ClientTestInvokeAuthorizerTlsContextTypeDef = TypedDict(
    "ClientTestInvokeAuthorizerTlsContextTypeDef", {"serverName": str}, total=False
)

ClientTransferCertificateResponseTypeDef = TypedDict(
    "ClientTransferCertificateResponseTypeDef", {"transferredCertificateArn": str}, total=False
)

ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef = TypedDict(
    "ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef",
    {"enabled": bool},
    total=False,
)

ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef = TypedDict(
    "ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef",
    {"targetArn": str, "roleArn": str, "enabled": bool},
    total=False,
)

ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "ClientUpdateAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)

ClientUpdateBillingGroupBillingGroupPropertiesTypeDef = TypedDict(
    "ClientUpdateBillingGroupBillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)

ClientUpdateBillingGroupResponseTypeDef = TypedDict(
    "ClientUpdateBillingGroupResponseTypeDef", {"version": int}, total=False
)

ClientUpdateCaCertificateRegistrationConfigTypeDef = TypedDict(
    "ClientUpdateCaCertificateRegistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)

ClientUpdateDomainConfigurationAuthorizerConfigTypeDef = TypedDict(
    "ClientUpdateDomainConfigurationAuthorizerConfigTypeDef",
    {"defaultAuthorizerName": str, "allowAuthorizerOverride": bool},
    total=False,
)

ClientUpdateDomainConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateDomainConfigurationResponseTypeDef",
    {"domainConfigurationName": str, "domainConfigurationArn": str},
    total=False,
)

ClientUpdateDynamicThingGroupResponseTypeDef = TypedDict(
    "ClientUpdateDynamicThingGroupResponseTypeDef", {"version": int}, total=False
)

ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)

ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef = TypedDict(
    "ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientUpdateDynamicThingGroupThingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)

ClientUpdateEventConfigurationsEventConfigurationsTypeDef = TypedDict(
    "ClientUpdateEventConfigurationsEventConfigurationsTypeDef", {"Enabled": bool}, total=False
)

ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)

ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)

_RequiredClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef",
    {"thingGroupIndexingMode": Literal["OFF", "ON"]},
)
_OptionalClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef",
    {
        "managedFields": List[
            ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef(
    _RequiredClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef,
    _OptionalClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef,
):
    pass


ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)

ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": Literal["Number", "String", "Boolean"]},
    total=False,
)

_RequiredClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef",
    {"thingIndexingMode": Literal["OFF", "REGISTRY", "REGISTRY_AND_SHADOW"]},
)
_OptionalClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef",
    {
        "thingConnectivityIndexingMode": Literal["OFF", "STATUS"],
        "managedFields": List[
            ClientUpdateIndexingConfigurationThingIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientUpdateIndexingConfigurationThingIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef(
    _RequiredClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef,
    _OptionalClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef,
):
    pass


_RequiredClientUpdateJobAbortConfigcriteriaListTypeDef = TypedDict(
    "_RequiredClientUpdateJobAbortConfigcriteriaListTypeDef",
    {"failureType": Literal["FAILED", "REJECTED", "TIMED_OUT", "ALL"]},
)
_OptionalClientUpdateJobAbortConfigcriteriaListTypeDef = TypedDict(
    "_OptionalClientUpdateJobAbortConfigcriteriaListTypeDef",
    {"action": str, "thresholdPercentage": float, "minNumberOfExecutedThings": int},
    total=False,
)


class ClientUpdateJobAbortConfigcriteriaListTypeDef(
    _RequiredClientUpdateJobAbortConfigcriteriaListTypeDef,
    _OptionalClientUpdateJobAbortConfigcriteriaListTypeDef,
):
    pass


ClientUpdateJobAbortConfigTypeDef = TypedDict(
    "ClientUpdateJobAbortConfigTypeDef",
    {"criteriaList": List[ClientUpdateJobAbortConfigcriteriaListTypeDef]},
)

ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)

ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientUpdateJobJobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
    total=False,
)

ClientUpdateJobJobExecutionsRolloutConfigTypeDef = TypedDict(
    "ClientUpdateJobJobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientUpdateJobJobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)

ClientUpdateJobPresignedUrlConfigTypeDef = TypedDict(
    "ClientUpdateJobPresignedUrlConfigTypeDef", {"roleArn": str, "expiresInSec": int}, total=False
)

ClientUpdateJobTimeoutConfigTypeDef = TypedDict(
    "ClientUpdateJobTimeoutConfigTypeDef", {"inProgressTimeoutInMinutes": int}, total=False
)

ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)

ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"]},
    total=False,
)

ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)

ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)

ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)

ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef", {"action": str}
)

ClientUpdateMitigationActionActionParamsTypeDef = TypedDict(
    "ClientUpdateMitigationActionActionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientUpdateMitigationActionActionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientUpdateMitigationActionActionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientUpdateMitigationActionActionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientUpdateMitigationActionActionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientUpdateMitigationActionActionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientUpdateMitigationActionActionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)

ClientUpdateMitigationActionResponseTypeDef = TypedDict(
    "ClientUpdateMitigationActionResponseTypeDef", {"actionArn": str, "actionId": str}, total=False
)

ClientUpdateRoleAliasResponseTypeDef = TypedDict(
    "ClientUpdateRoleAliasResponseTypeDef", {"roleAlias": str, "roleAliasArn": str}, total=False
)

ClientUpdateScheduledAuditResponseTypeDef = TypedDict(
    "ClientUpdateScheduledAuditResponseTypeDef", {"scheduledAuditArn": str}, total=False
)

ClientUpdateSecurityProfileAlertTargetsTypeDef = TypedDict(
    "ClientUpdateSecurityProfileAlertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)

ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef = TypedDict(
    "ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientUpdateSecurityProfileBehaviorscriteriaTypeDef = TypedDict(
    "ClientUpdateSecurityProfileBehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientUpdateSecurityProfileBehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientUpdateSecurityProfileBehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

_RequiredClientUpdateSecurityProfileBehaviorsTypeDef = TypedDict(
    "_RequiredClientUpdateSecurityProfileBehaviorsTypeDef", {"name": str}
)
_OptionalClientUpdateSecurityProfileBehaviorsTypeDef = TypedDict(
    "_OptionalClientUpdateSecurityProfileBehaviorsTypeDef",
    {"metric": str, "criteria": ClientUpdateSecurityProfileBehaviorscriteriaTypeDef},
    total=False,
)


class ClientUpdateSecurityProfileBehaviorsTypeDef(
    _RequiredClientUpdateSecurityProfileBehaviorsTypeDef,
    _OptionalClientUpdateSecurityProfileBehaviorsTypeDef,
):
    pass


ClientUpdateSecurityProfileResponsealertTargetsTypeDef = TypedDict(
    "ClientUpdateSecurityProfileResponsealertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)

ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef = TypedDict(
    "ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef = TypedDict(
    "ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

ClientUpdateSecurityProfileResponsebehaviorsTypeDef = TypedDict(
    "ClientUpdateSecurityProfileResponsebehaviorsTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef,
    },
    total=False,
)

ClientUpdateSecurityProfileResponseTypeDef = TypedDict(
    "ClientUpdateSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List[ClientUpdateSecurityProfileResponsebehaviorsTypeDef],
        "alertTargets": Dict[str, ClientUpdateSecurityProfileResponsealertTargetsTypeDef],
        "additionalMetricsToRetain": List[str],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

ClientUpdateStreamFiless3LocationTypeDef = TypedDict(
    "ClientUpdateStreamFiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)

ClientUpdateStreamFilesTypeDef = TypedDict(
    "ClientUpdateStreamFilesTypeDef",
    {"fileId": int, "s3Location": ClientUpdateStreamFiless3LocationTypeDef},
    total=False,
)

ClientUpdateStreamResponseTypeDef = TypedDict(
    "ClientUpdateStreamResponseTypeDef",
    {"streamId": str, "streamArn": str, "description": str, "streamVersion": int},
    total=False,
)

ClientUpdateThingAttributePayloadTypeDef = TypedDict(
    "ClientUpdateThingAttributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)

ClientUpdateThingGroupResponseTypeDef = TypedDict(
    "ClientUpdateThingGroupResponseTypeDef", {"version": int}, total=False
)

ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)

ClientUpdateThingGroupThingGroupPropertiesTypeDef = TypedDict(
    "ClientUpdateThingGroupThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientUpdateThingGroupThingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)

ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef = TypedDict(
    "ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef = TypedDict(
    "ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ClientValidateSecurityProfileBehaviorsBehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientValidateSecurityProfileBehaviorsBehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

_RequiredClientValidateSecurityProfileBehaviorsBehaviorsTypeDef = TypedDict(
    "_RequiredClientValidateSecurityProfileBehaviorsBehaviorsTypeDef", {"name": str}
)
_OptionalClientValidateSecurityProfileBehaviorsBehaviorsTypeDef = TypedDict(
    "_OptionalClientValidateSecurityProfileBehaviorsBehaviorsTypeDef",
    {"metric": str, "criteria": ClientValidateSecurityProfileBehaviorsBehaviorscriteriaTypeDef},
    total=False,
)


class ClientValidateSecurityProfileBehaviorsBehaviorsTypeDef(
    _RequiredClientValidateSecurityProfileBehaviorsBehaviorsTypeDef,
    _OptionalClientValidateSecurityProfileBehaviorsBehaviorsTypeDef,
):
    pass


ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef = TypedDict(
    "ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef",
    {"errorMessage": str},
    total=False,
)

ClientValidateSecurityProfileBehaviorsResponseTypeDef = TypedDict(
    "ClientValidateSecurityProfileBehaviorsResponseTypeDef",
    {
        "valid": bool,
        "validationErrors": List[
            ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef
        ],
    },
    total=False,
)

ListActiveViolationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListActiveViolationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef = TypedDict(
    "ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef = TypedDict(
    "ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef = TypedDict(
    "ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef,
    },
    total=False,
)

ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef = TypedDict(
    "ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ListActiveViolationsPaginateResponseactiveViolationsTypeDef = TypedDict(
    "ListActiveViolationsPaginateResponseactiveViolationsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef,
        "lastViolationValue": ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef,
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)

ListActiveViolationsPaginateResponseTypeDef = TypedDict(
    "ListActiveViolationsPaginateResponseTypeDef",
    {
        "activeViolations": List[ListActiveViolationsPaginateResponseactiveViolationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListAttachedPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAttachedPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAttachedPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "ListAttachedPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)

ListAttachedPoliciesPaginateResponseTypeDef = TypedDict(
    "ListAttachedPoliciesPaginateResponseTypeDef",
    {"policies": List[ListAttachedPoliciesPaginateResponsepoliciesTypeDef], "NextToken": str},
    total=False,
)

ListAuditFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAuditFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)

ListAuditFindingsPaginateResourceIdentifierTypeDef = TypedDict(
    "ListAuditFindingsPaginateResourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateResourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)

ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)

ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)

ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef = TypedDict(
    "ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)

ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
    },
    total=False,
)

ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef = TypedDict(
    "ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef",
    {
        "resourceType": Literal[
            "DEVICE_CERTIFICATE",
            "CA_CERTIFICATE",
            "IOT_POLICY",
            "COGNITO_IDENTITY_POOL",
            "CLIENT_ID",
            "ACCOUNT_SETTINGS",
            "ROLE_ALIAS",
            "IAM_ROLE",
        ],
        "resourceIdentifier": ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

ListAuditFindingsPaginateResponsefindingsTypeDef = TypedDict(
    "ListAuditFindingsPaginateResponsefindingsTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"],
        "nonCompliantResource": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef,
        "relatedResources": List[ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)

ListAuditFindingsPaginateResponseTypeDef = TypedDict(
    "ListAuditFindingsPaginateResponseTypeDef",
    {"findings": List[ListAuditFindingsPaginateResponsefindingsTypeDef], "NextToken": str},
    total=False,
)

ListAuditTasksPaginatePaginationConfigTypeDef = TypedDict(
    "ListAuditTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAuditTasksPaginateResponsetasksTypeDef = TypedDict(
    "ListAuditTasksPaginateResponsetasksTypeDef",
    {
        "taskId": str,
        "taskStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"],
        "taskType": Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"],
    },
    total=False,
)

ListAuditTasksPaginateResponseTypeDef = TypedDict(
    "ListAuditTasksPaginateResponseTypeDef",
    {"tasks": List[ListAuditTasksPaginateResponsetasksTypeDef], "NextToken": str},
    total=False,
)

ListAuthorizersPaginatePaginationConfigTypeDef = TypedDict(
    "ListAuthorizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAuthorizersPaginateResponseauthorizersTypeDef = TypedDict(
    "ListAuthorizersPaginateResponseauthorizersTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)

ListAuthorizersPaginateResponseTypeDef = TypedDict(
    "ListAuthorizersPaginateResponseTypeDef",
    {"authorizers": List[ListAuthorizersPaginateResponseauthorizersTypeDef], "NextToken": str},
    total=False,
)

ListBillingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListBillingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListBillingGroupsPaginateResponsebillingGroupsTypeDef = TypedDict(
    "ListBillingGroupsPaginateResponsebillingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)

ListBillingGroupsPaginateResponseTypeDef = TypedDict(
    "ListBillingGroupsPaginateResponseTypeDef",
    {
        "billingGroups": List[ListBillingGroupsPaginateResponsebillingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListCACertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "ListCACertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCACertificatesPaginateResponsecertificatesTypeDef = TypedDict(
    "ListCACertificatesPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal["ACTIVE", "INACTIVE"],
        "creationDate": datetime,
    },
    total=False,
)

ListCACertificatesPaginateResponseTypeDef = TypedDict(
    "ListCACertificatesPaginateResponseTypeDef",
    {"certificates": List[ListCACertificatesPaginateResponsecertificatesTypeDef], "NextToken": str},
    total=False,
)

ListCertificatesByCAPaginatePaginationConfigTypeDef = TypedDict(
    "ListCertificatesByCAPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCertificatesByCAPaginateResponsecertificatesTypeDef = TypedDict(
    "ListCertificatesByCAPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "creationDate": datetime,
    },
    total=False,
)

ListCertificatesByCAPaginateResponseTypeDef = TypedDict(
    "ListCertificatesByCAPaginateResponseTypeDef",
    {
        "certificates": List[ListCertificatesByCAPaginateResponsecertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "ListCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCertificatesPaginateResponsecertificatesTypeDef = TypedDict(
    "ListCertificatesPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
        "creationDate": datetime,
    },
    total=False,
)

ListCertificatesPaginateResponseTypeDef = TypedDict(
    "ListCertificatesPaginateResponseTypeDef",
    {"certificates": List[ListCertificatesPaginateResponsecertificatesTypeDef], "NextToken": str},
    total=False,
)

ListIndicesPaginatePaginationConfigTypeDef = TypedDict(
    "ListIndicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListIndicesPaginateResponseTypeDef = TypedDict(
    "ListIndicesPaginateResponseTypeDef", {"indexNames": List[str], "NextToken": str}, total=False
)

ListJobExecutionsForJobPaginatePaginationConfigTypeDef = TypedDict(
    "ListJobExecutionsForJobPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)

ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef = TypedDict(
    "ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)

ListJobExecutionsForJobPaginateResponseTypeDef = TypedDict(
    "ListJobExecutionsForJobPaginateResponseTypeDef",
    {
        "executionSummaries": List[
            ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListJobExecutionsForThingPaginatePaginationConfigTypeDef = TypedDict(
    "ListJobExecutionsForThingPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)

ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef = TypedDict(
    "ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)

ListJobExecutionsForThingPaginateResponseTypeDef = TypedDict(
    "ListJobExecutionsForThingPaginateResponseTypeDef",
    {
        "executionSummaries": List[
            ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListJobsPaginateResponsejobsTypeDef = TypedDict(
    "ListJobsPaginateResponsejobsTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": Literal["CONTINUOUS", "SNAPSHOT"],
        "status": Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)

ListJobsPaginateResponseTypeDef = TypedDict(
    "ListJobsPaginateResponseTypeDef",
    {"jobs": List[ListJobsPaginateResponsejobsTypeDef], "NextToken": str},
    total=False,
)

ListOTAUpdatesPaginatePaginationConfigTypeDef = TypedDict(
    "ListOTAUpdatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListOTAUpdatesPaginateResponseotaUpdatesTypeDef = TypedDict(
    "ListOTAUpdatesPaginateResponseotaUpdatesTypeDef",
    {"otaUpdateId": str, "otaUpdateArn": str, "creationDate": datetime},
    total=False,
)

ListOTAUpdatesPaginateResponseTypeDef = TypedDict(
    "ListOTAUpdatesPaginateResponseTypeDef",
    {"otaUpdates": List[ListOTAUpdatesPaginateResponseotaUpdatesTypeDef], "NextToken": str},
    total=False,
)

ListOutgoingCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "ListOutgoingCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef = TypedDict(
    "ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
    },
    total=False,
)

ListOutgoingCertificatesPaginateResponseTypeDef = TypedDict(
    "ListOutgoingCertificatesPaginateResponseTypeDef",
    {
        "outgoingCertificates": List[
            ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "ListPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)

ListPoliciesPaginateResponseTypeDef = TypedDict(
    "ListPoliciesPaginateResponseTypeDef",
    {"policies": List[ListPoliciesPaginateResponsepoliciesTypeDef], "NextToken": str},
    total=False,
)

ListPolicyPrincipalsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPolicyPrincipalsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPolicyPrincipalsPaginateResponseTypeDef = TypedDict(
    "ListPolicyPrincipalsPaginateResponseTypeDef",
    {"principals": List[str], "NextToken": str},
    total=False,
)

ListPrincipalPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListPrincipalPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPrincipalPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "ListPrincipalPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)

ListPrincipalPoliciesPaginateResponseTypeDef = TypedDict(
    "ListPrincipalPoliciesPaginateResponseTypeDef",
    {"policies": List[ListPrincipalPoliciesPaginateResponsepoliciesTypeDef], "NextToken": str},
    total=False,
)

ListPrincipalThingsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPrincipalThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPrincipalThingsPaginateResponseTypeDef = TypedDict(
    "ListPrincipalThingsPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)

ListRoleAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "ListRoleAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRoleAliasesPaginateResponseTypeDef = TypedDict(
    "ListRoleAliasesPaginateResponseTypeDef",
    {"roleAliases": List[str], "NextToken": str},
    total=False,
)

ListScheduledAuditsPaginatePaginationConfigTypeDef = TypedDict(
    "ListScheduledAuditsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef = TypedDict(
    "ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        "dayOfMonth": str,
        "dayOfWeek": Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"],
    },
    total=False,
)

ListScheduledAuditsPaginateResponseTypeDef = TypedDict(
    "ListScheduledAuditsPaginateResponseTypeDef",
    {
        "scheduledAudits": List[ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef = TypedDict(
    "ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef = TypedDict(
    "ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef",
    {"name": str, "arn": str},
    total=False,
)

ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef = TypedDict(
    "ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef",
    {"arn": str},
    total=False,
)

ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef = TypedDict(
    "ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef",
    {
        "securityProfileIdentifier": ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef,
        "target": ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef,
    },
    total=False,
)

ListSecurityProfilesForTargetPaginateResponseTypeDef = TypedDict(
    "ListSecurityProfilesForTargetPaginateResponseTypeDef",
    {
        "securityProfileTargetMappings": List[
            ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListSecurityProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "ListSecurityProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef = TypedDict(
    "ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef",
    {"name": str, "arn": str},
    total=False,
)

ListSecurityProfilesPaginateResponseTypeDef = TypedDict(
    "ListSecurityProfilesPaginateResponseTypeDef",
    {
        "securityProfileIdentifiers": List[
            ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "ListStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListStreamsPaginateResponsestreamsTypeDef = TypedDict(
    "ListStreamsPaginateResponsestreamsTypeDef",
    {"streamId": str, "streamArn": str, "streamVersion": int, "description": str},
    total=False,
)

ListStreamsPaginateResponseTypeDef = TypedDict(
    "ListStreamsPaginateResponseTypeDef",
    {"streams": List[ListStreamsPaginateResponsestreamsTypeDef], "NextToken": str},
    total=False,
)

ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "ListTagsForResourcePaginateResponsetagsTypeDef", {"Key": str, "Value": str}, total=False
)

ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)

ListTargetsForPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "ListTargetsForPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTargetsForPolicyPaginateResponseTypeDef = TypedDict(
    "ListTargetsForPolicyPaginateResponseTypeDef",
    {"targets": List[str], "NextToken": str},
    total=False,
)

ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef = TypedDict(
    "ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef = TypedDict(
    "ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef",
    {"arn": str},
    total=False,
)

ListTargetsForSecurityProfilePaginateResponseTypeDef = TypedDict(
    "ListTargetsForSecurityProfilePaginateResponseTypeDef",
    {
        "securityProfileTargets": List[
            ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListThingGroupsForThingPaginatePaginationConfigTypeDef = TypedDict(
    "ListThingGroupsForThingPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListThingGroupsForThingPaginateResponsethingGroupsTypeDef = TypedDict(
    "ListThingGroupsForThingPaginateResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)

ListThingGroupsForThingPaginateResponseTypeDef = TypedDict(
    "ListThingGroupsForThingPaginateResponseTypeDef",
    {
        "thingGroups": List[ListThingGroupsForThingPaginateResponsethingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListThingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListThingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListThingGroupsPaginateResponsethingGroupsTypeDef = TypedDict(
    "ListThingGroupsPaginateResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)

ListThingGroupsPaginateResponseTypeDef = TypedDict(
    "ListThingGroupsPaginateResponseTypeDef",
    {"thingGroups": List[ListThingGroupsPaginateResponsethingGroupsTypeDef], "NextToken": str},
    total=False,
)

ListThingRegistrationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "ListThingRegistrationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListThingRegistrationTasksPaginateResponseTypeDef = TypedDict(
    "ListThingRegistrationTasksPaginateResponseTypeDef",
    {"taskIds": List[str], "NextToken": str},
    total=False,
)

ListThingTypesPaginatePaginationConfigTypeDef = TypedDict(
    "ListThingTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef = TypedDict(
    "ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)

ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef = TypedDict(
    "ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)

ListThingTypesPaginateResponsethingTypesTypeDef = TypedDict(
    "ListThingTypesPaginateResponsethingTypesTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef,
        "thingTypeMetadata": ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef,
    },
    total=False,
)

ListThingTypesPaginateResponseTypeDef = TypedDict(
    "ListThingTypesPaginateResponseTypeDef",
    {"thingTypes": List[ListThingTypesPaginateResponsethingTypesTypeDef], "NextToken": str},
    total=False,
)

ListThingsInBillingGroupPaginatePaginationConfigTypeDef = TypedDict(
    "ListThingsInBillingGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListThingsInBillingGroupPaginateResponseTypeDef = TypedDict(
    "ListThingsInBillingGroupPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)

ListThingsInThingGroupPaginatePaginationConfigTypeDef = TypedDict(
    "ListThingsInThingGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListThingsInThingGroupPaginateResponseTypeDef = TypedDict(
    "ListThingsInThingGroupPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)

ListThingsPaginatePaginationConfigTypeDef = TypedDict(
    "ListThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListThingsPaginateResponsethingsTypeDef = TypedDict(
    "ListThingsPaginateResponsethingsTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)

ListThingsPaginateResponseTypeDef = TypedDict(
    "ListThingsPaginateResponseTypeDef",
    {"things": List[ListThingsPaginateResponsethingsTypeDef], "NextToken": str},
    total=False,
)

ListTopicRulesPaginatePaginationConfigTypeDef = TypedDict(
    "ListTopicRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTopicRulesPaginateResponserulesTypeDef = TypedDict(
    "ListTopicRulesPaginateResponserulesTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)

ListTopicRulesPaginateResponseTypeDef = TypedDict(
    "ListTopicRulesPaginateResponseTypeDef",
    {"rules": List[ListTopicRulesPaginateResponserulesTypeDef], "NextToken": str},
    total=False,
)

ListV2LoggingLevelsPaginatePaginationConfigTypeDef = TypedDict(
    "ListV2LoggingLevelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef = TypedDict(
    "ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef",
    {"targetType": Literal["DEFAULT", "THING_GROUP"], "targetName": str},
    total=False,
)

ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef = TypedDict(
    "ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef",
    {
        "logTarget": ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef,
        "logLevel": Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
    },
    total=False,
)

ListV2LoggingLevelsPaginateResponseTypeDef = TypedDict(
    "ListV2LoggingLevelsPaginateResponseTypeDef",
    {
        "logTargetConfigurations": List[
            ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListViolationEventsPaginatePaginationConfigTypeDef = TypedDict(
    "ListViolationEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)

ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef = TypedDict(
    "ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef = TypedDict(
    "ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": Literal[
            "less-than",
            "less-than-equals",
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "not-in-cidr-set",
            "in-port-set",
            "not-in-port-set",
        ],
        "value": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)

ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef = TypedDict(
    "ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef,
    },
    total=False,
)

ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef = TypedDict(
    "ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)

ListViolationEventsPaginateResponseviolationEventsTypeDef = TypedDict(
    "ListViolationEventsPaginateResponseviolationEventsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef,
        "metricValue": ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef,
        "violationEventType": Literal["in-alarm", "alarm-cleared", "alarm-invalidated"],
        "violationEventTime": datetime,
    },
    total=False,
)

ListViolationEventsPaginateResponseTypeDef = TypedDict(
    "ListViolationEventsPaginateResponseTypeDef",
    {
        "violationEvents": List[ListViolationEventsPaginateResponseviolationEventsTypeDef],
        "NextToken": str,
    },
    total=False,
)
