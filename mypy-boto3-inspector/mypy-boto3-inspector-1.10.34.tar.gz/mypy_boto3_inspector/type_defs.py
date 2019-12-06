"Main interface for inspector service type defs"
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


_RequiredClientAddAttributesToFindingsAttributesTypeDef = TypedDict(
    "_RequiredClientAddAttributesToFindingsAttributesTypeDef", {"key": str}
)
_OptionalClientAddAttributesToFindingsAttributesTypeDef = TypedDict(
    "_OptionalClientAddAttributesToFindingsAttributesTypeDef", {"value": str}, total=False
)


class ClientAddAttributesToFindingsAttributesTypeDef(
    _RequiredClientAddAttributesToFindingsAttributesTypeDef,
    _OptionalClientAddAttributesToFindingsAttributesTypeDef,
):
    pass


ClientAddAttributesToFindingsResponsefailedItemsTypeDef = TypedDict(
    "ClientAddAttributesToFindingsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientAddAttributesToFindingsResponseTypeDef = TypedDict(
    "ClientAddAttributesToFindingsResponseTypeDef",
    {"failedItems": Dict[str, ClientAddAttributesToFindingsResponsefailedItemsTypeDef]},
    total=False,
)

ClientCreateAssessmentTargetResponseTypeDef = TypedDict(
    "ClientCreateAssessmentTargetResponseTypeDef", {"assessmentTargetArn": str}, total=False
)

ClientCreateAssessmentTemplateResponseTypeDef = TypedDict(
    "ClientCreateAssessmentTemplateResponseTypeDef", {"assessmentTemplateArn": str}, total=False
)

_RequiredClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef = TypedDict(
    "_RequiredClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef", {"key": str}
)
_OptionalClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef = TypedDict(
    "_OptionalClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef",
    {"value": str},
    total=False,
)


class ClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef(
    _RequiredClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef,
    _OptionalClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef,
):
    pass


ClientCreateExclusionsPreviewResponseTypeDef = TypedDict(
    "ClientCreateExclusionsPreviewResponseTypeDef", {"previewToken": str}, total=False
)

_RequiredClientCreateResourceGroupResourceGroupTagsTypeDef = TypedDict(
    "_RequiredClientCreateResourceGroupResourceGroupTagsTypeDef", {"key": str}
)
_OptionalClientCreateResourceGroupResourceGroupTagsTypeDef = TypedDict(
    "_OptionalClientCreateResourceGroupResourceGroupTagsTypeDef", {"value": str}, total=False
)


class ClientCreateResourceGroupResourceGroupTagsTypeDef(
    _RequiredClientCreateResourceGroupResourceGroupTagsTypeDef,
    _OptionalClientCreateResourceGroupResourceGroupTagsTypeDef,
):
    pass


ClientCreateResourceGroupResponseTypeDef = TypedDict(
    "ClientCreateResourceGroupResponseTypeDef", {"resourceGroupArn": str}, total=False
)

ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef = TypedDict(
    "ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef",
    {
        "date": datetime,
        "event": Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        "message": str,
        "error": bool,
        "snsTopicArn": str,
        "snsPublishStatusCode": Literal[
            "SUCCESS", "TOPIC_DOES_NOT_EXIST", "ACCESS_DENIED", "INTERNAL_ERROR"
        ],
    },
    total=False,
)

ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef = TypedDict(
    "ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef",
    {
        "stateChangedAt": datetime,
        "state": Literal[
            "CREATED",
            "START_DATA_COLLECTION_PENDING",
            "START_DATA_COLLECTION_IN_PROGRESS",
            "COLLECTING_DATA",
            "STOP_DATA_COLLECTION_PENDING",
            "DATA_COLLECTED",
            "START_EVALUATING_RULES_PENDING",
            "EVALUATING_RULES",
            "FAILED",
            "ERROR",
            "COMPLETED",
            "COMPLETED_WITH_ERRORS",
            "CANCELED",
        ],
    },
    total=False,
)

ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef = TypedDict(
    "ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef = TypedDict(
    "ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTemplateArn": str,
        "state": Literal[
            "CREATED",
            "START_DATA_COLLECTION_PENDING",
            "START_DATA_COLLECTION_IN_PROGRESS",
            "COLLECTING_DATA",
            "STOP_DATA_COLLECTION_PENDING",
            "DATA_COLLECTED",
            "START_EVALUATING_RULES_PENDING",
            "EVALUATING_RULES",
            "FAILED",
            "ERROR",
            "COMPLETED",
            "COMPLETED_WITH_ERRORS",
            "CANCELED",
        ],
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List[
            ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef
        ],
        "createdAt": datetime,
        "startedAt": datetime,
        "completedAt": datetime,
        "stateChangedAt": datetime,
        "dataCollected": bool,
        "stateChanges": List[ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef],
        "notifications": List[
            ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef
        ],
        "findingCounts": Dict[str, int],
    },
    total=False,
)

ClientDescribeAssessmentRunsResponsefailedItemsTypeDef = TypedDict(
    "ClientDescribeAssessmentRunsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientDescribeAssessmentRunsResponseTypeDef = TypedDict(
    "ClientDescribeAssessmentRunsResponseTypeDef",
    {
        "assessmentRuns": List[ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef],
        "failedItems": Dict[str, ClientDescribeAssessmentRunsResponsefailedItemsTypeDef],
    },
    total=False,
)

ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef = TypedDict(
    "ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef",
    {
        "arn": str,
        "name": str,
        "resourceGroupArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef = TypedDict(
    "ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientDescribeAssessmentTargetsResponseTypeDef = TypedDict(
    "ClientDescribeAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargets": List[ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef],
        "failedItems": Dict[str, ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef],
    },
    total=False,
)

ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef = TypedDict(
    "ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef = TypedDict(
    "ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTargetArn": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List[
            ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef
        ],
        "lastAssessmentRunArn": str,
        "assessmentRunCount": int,
        "createdAt": datetime,
    },
    total=False,
)

ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef = TypedDict(
    "ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientDescribeAssessmentTemplatesResponseTypeDef = TypedDict(
    "ClientDescribeAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplates": List[
            ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef
        ],
        "failedItems": Dict[str, ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef],
    },
    total=False,
)

ClientDescribeCrossAccountAccessRoleResponseTypeDef = TypedDict(
    "ClientDescribeCrossAccountAccessRoleResponseTypeDef",
    {"roleArn": str, "valid": bool, "registeredAt": datetime},
    total=False,
)

ClientDescribeExclusionsResponseexclusionsattributesTypeDef = TypedDict(
    "ClientDescribeExclusionsResponseexclusionsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeExclusionsResponseexclusionsscopesTypeDef = TypedDict(
    "ClientDescribeExclusionsResponseexclusionsscopesTypeDef",
    {"key": Literal["INSTANCE_ID", "RULES_PACKAGE_ARN"], "value": str},
    total=False,
)

ClientDescribeExclusionsResponseexclusionsTypeDef = TypedDict(
    "ClientDescribeExclusionsResponseexclusionsTypeDef",
    {
        "arn": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List[ClientDescribeExclusionsResponseexclusionsscopesTypeDef],
        "attributes": List[ClientDescribeExclusionsResponseexclusionsattributesTypeDef],
    },
    total=False,
)

ClientDescribeExclusionsResponsefailedItemsTypeDef = TypedDict(
    "ClientDescribeExclusionsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientDescribeExclusionsResponseTypeDef = TypedDict(
    "ClientDescribeExclusionsResponseTypeDef",
    {
        "exclusions": Dict[str, ClientDescribeExclusionsResponseexclusionsTypeDef],
        "failedItems": Dict[str, ClientDescribeExclusionsResponsefailedItemsTypeDef],
    },
    total=False,
)

ClientDescribeFindingsResponsefailedItemsTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef",
    {"privateDnsName": str, "privateIpAddress": str},
    total=False,
)

ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef",
    {"groupName": str, "groupId": str},
    total=False,
)

ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef",
    {
        "networkInterfaceId": str,
        "subnetId": str,
        "vpcId": str,
        "privateDnsName": str,
        "privateIpAddress": str,
        "privateIpAddresses": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef
        ],
        "publicDnsName": str,
        "publicIp": str,
        "ipv6Addresses": List[str],
        "securityGroups": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeFindingsResponsefindingsassetAttributesTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsassetAttributesTypeDef",
    {
        "schemaVersion": int,
        "agentId": str,
        "autoScalingGroup": str,
        "amiId": str,
        "hostname": str,
        "ipv4Addresses": List[str],
        "tags": List[ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef],
        "networkInterfaces": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef
        ],
    },
    total=False,
)

ClientDescribeFindingsResponsefindingsattributesTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef",
    {"schemaVersion": int, "assessmentRunArn": str, "rulesPackageArn": str},
    total=False,
)

ClientDescribeFindingsResponsefindingsuserAttributesTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsuserAttributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeFindingsResponsefindingsTypeDef = TypedDict(
    "ClientDescribeFindingsResponsefindingsTypeDef",
    {
        "arn": str,
        "schemaVersion": int,
        "service": str,
        "serviceAttributes": ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef,
        "assetType": str,
        "assetAttributes": ClientDescribeFindingsResponsefindingsassetAttributesTypeDef,
        "id": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "severity": Literal["Low", "Medium", "High", "Informational", "Undefined"],
        "numericSeverity": float,
        "confidence": int,
        "indicatorOfCompromise": bool,
        "attributes": List[ClientDescribeFindingsResponsefindingsattributesTypeDef],
        "userAttributes": List[ClientDescribeFindingsResponsefindingsuserAttributesTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

ClientDescribeFindingsResponseTypeDef = TypedDict(
    "ClientDescribeFindingsResponseTypeDef",
    {
        "findings": List[ClientDescribeFindingsResponsefindingsTypeDef],
        "failedItems": Dict[str, ClientDescribeFindingsResponsefailedItemsTypeDef],
    },
    total=False,
)

ClientDescribeResourceGroupsResponsefailedItemsTypeDef = TypedDict(
    "ClientDescribeResourceGroupsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef = TypedDict(
    "ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeResourceGroupsResponseresourceGroupsTypeDef = TypedDict(
    "ClientDescribeResourceGroupsResponseresourceGroupsTypeDef",
    {
        "arn": str,
        "tags": List[ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef],
        "createdAt": datetime,
    },
    total=False,
)

ClientDescribeResourceGroupsResponseTypeDef = TypedDict(
    "ClientDescribeResourceGroupsResponseTypeDef",
    {
        "resourceGroups": List[ClientDescribeResourceGroupsResponseresourceGroupsTypeDef],
        "failedItems": Dict[str, ClientDescribeResourceGroupsResponsefailedItemsTypeDef],
    },
    total=False,
)

ClientDescribeRulesPackagesResponsefailedItemsTypeDef = TypedDict(
    "ClientDescribeRulesPackagesResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientDescribeRulesPackagesResponserulesPackagesTypeDef = TypedDict(
    "ClientDescribeRulesPackagesResponserulesPackagesTypeDef",
    {"arn": str, "name": str, "version": str, "provider": str, "description": str},
    total=False,
)

ClientDescribeRulesPackagesResponseTypeDef = TypedDict(
    "ClientDescribeRulesPackagesResponseTypeDef",
    {
        "rulesPackages": List[ClientDescribeRulesPackagesResponserulesPackagesTypeDef],
        "failedItems": Dict[str, ClientDescribeRulesPackagesResponsefailedItemsTypeDef],
    },
    total=False,
)

ClientGetAssessmentReportResponseTypeDef = TypedDict(
    "ClientGetAssessmentReportResponseTypeDef",
    {"status": Literal["WORK_IN_PROGRESS", "FAILED", "COMPLETED"], "url": str},
    total=False,
)

ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef = TypedDict(
    "ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef = TypedDict(
    "ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef",
    {"key": Literal["INSTANCE_ID", "RULES_PACKAGE_ARN"], "value": str},
    total=False,
)

ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef = TypedDict(
    "ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef",
    {
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List[ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef],
        "attributes": List[ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef],
    },
    total=False,
)

ClientGetExclusionsPreviewResponseTypeDef = TypedDict(
    "ClientGetExclusionsPreviewResponseTypeDef",
    {
        "previewStatus": Literal["WORK_IN_PROGRESS", "COMPLETED"],
        "exclusionPreviews": List[ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef = TypedDict(
    "ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)

ClientGetTelemetryMetadataResponseTypeDef = TypedDict(
    "ClientGetTelemetryMetadataResponseTypeDef",
    {"telemetryMetadata": List[ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef]},
    total=False,
)

_RequiredClientListAssessmentRunAgentsFilterTypeDef = TypedDict(
    "_RequiredClientListAssessmentRunAgentsFilterTypeDef",
    {"agentHealths": List[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]]},
)
_OptionalClientListAssessmentRunAgentsFilterTypeDef = TypedDict(
    "_OptionalClientListAssessmentRunAgentsFilterTypeDef",
    {
        "agentHealthCodes": List[
            Literal["IDLE", "RUNNING", "SHUTDOWN", "UNHEALTHY", "THROTTLED", "UNKNOWN"]
        ]
    },
    total=False,
)


class ClientListAssessmentRunAgentsFilterTypeDef(
    _RequiredClientListAssessmentRunAgentsFilterTypeDef,
    _OptionalClientListAssessmentRunAgentsFilterTypeDef,
):
    pass


ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef = TypedDict(
    "ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)

ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef = TypedDict(
    "ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "agentHealthCode": Literal[
            "IDLE", "RUNNING", "SHUTDOWN", "UNHEALTHY", "THROTTLED", "UNKNOWN"
        ],
        "agentHealthDetails": str,
        "autoScalingGroup": str,
        "telemetryMetadata": List[
            ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef
        ],
    },
    total=False,
)

ClientListAssessmentRunAgentsResponseTypeDef = TypedDict(
    "ClientListAssessmentRunAgentsResponseTypeDef",
    {
        "assessmentRunAgents": List[
            ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef = TypedDict(
    "ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)

ClientListAssessmentRunsFilterdurationRangeTypeDef = TypedDict(
    "ClientListAssessmentRunsFilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)

ClientListAssessmentRunsFilterstartTimeRangeTypeDef = TypedDict(
    "ClientListAssessmentRunsFilterstartTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)

ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef = TypedDict(
    "ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)

ClientListAssessmentRunsFilterTypeDef = TypedDict(
    "ClientListAssessmentRunsFilterTypeDef",
    {
        "namePattern": str,
        "states": List[
            Literal[
                "CREATED",
                "START_DATA_COLLECTION_PENDING",
                "START_DATA_COLLECTION_IN_PROGRESS",
                "COLLECTING_DATA",
                "STOP_DATA_COLLECTION_PENDING",
                "DATA_COLLECTED",
                "START_EVALUATING_RULES_PENDING",
                "EVALUATING_RULES",
                "FAILED",
                "ERROR",
                "COMPLETED",
                "COMPLETED_WITH_ERRORS",
                "CANCELED",
            ]
        ],
        "durationRange": ClientListAssessmentRunsFilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
        "startTimeRange": ClientListAssessmentRunsFilterstartTimeRangeTypeDef,
        "completionTimeRange": ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef,
        "stateChangeTimeRange": ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef,
    },
    total=False,
)

ClientListAssessmentRunsResponseTypeDef = TypedDict(
    "ClientListAssessmentRunsResponseTypeDef",
    {"assessmentRunArns": List[str], "nextToken": str},
    total=False,
)

ClientListAssessmentTargetsFilterTypeDef = TypedDict(
    "ClientListAssessmentTargetsFilterTypeDef", {"assessmentTargetNamePattern": str}, total=False
)

ClientListAssessmentTargetsResponseTypeDef = TypedDict(
    "ClientListAssessmentTargetsResponseTypeDef",
    {"assessmentTargetArns": List[str], "nextToken": str},
    total=False,
)

ClientListAssessmentTemplatesFilterdurationRangeTypeDef = TypedDict(
    "ClientListAssessmentTemplatesFilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)

ClientListAssessmentTemplatesFilterTypeDef = TypedDict(
    "ClientListAssessmentTemplatesFilterTypeDef",
    {
        "namePattern": str,
        "durationRange": ClientListAssessmentTemplatesFilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
    },
    total=False,
)

ClientListAssessmentTemplatesResponseTypeDef = TypedDict(
    "ClientListAssessmentTemplatesResponseTypeDef",
    {"assessmentTemplateArns": List[str], "nextToken": str},
    total=False,
)

ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef = TypedDict(
    "ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef",
    {
        "event": Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        "subscribedAt": datetime,
    },
    total=False,
)

ClientListEventSubscriptionsResponsesubscriptionsTypeDef = TypedDict(
    "ClientListEventSubscriptionsResponsesubscriptionsTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List[
            ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef
        ],
    },
    total=False,
)

ClientListEventSubscriptionsResponseTypeDef = TypedDict(
    "ClientListEventSubscriptionsResponseTypeDef",
    {
        "subscriptions": List[ClientListEventSubscriptionsResponsesubscriptionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListExclusionsResponseTypeDef = TypedDict(
    "ClientListExclusionsResponseTypeDef",
    {"exclusionArns": List[str], "nextToken": str},
    total=False,
)

ClientListFindingsFilterattributesTypeDef = TypedDict(
    "ClientListFindingsFilterattributesTypeDef", {"key": str, "value": str}, total=False
)

ClientListFindingsFiltercreationTimeRangeTypeDef = TypedDict(
    "ClientListFindingsFiltercreationTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)

ClientListFindingsFilteruserAttributesTypeDef = TypedDict(
    "ClientListFindingsFilteruserAttributesTypeDef", {"key": str, "value": str}, total=False
)

ClientListFindingsFilterTypeDef = TypedDict(
    "ClientListFindingsFilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[Literal["Low", "Medium", "High", "Informational", "Undefined"]],
        "rulesPackageArns": List[str],
        "attributes": List[ClientListFindingsFilterattributesTypeDef],
        "userAttributes": List[ClientListFindingsFilteruserAttributesTypeDef],
        "creationTimeRange": ClientListFindingsFiltercreationTimeRangeTypeDef,
    },
    total=False,
)

ClientListFindingsResponseTypeDef = TypedDict(
    "ClientListFindingsResponseTypeDef", {"findingArns": List[str], "nextToken": str}, total=False
)

ClientListRulesPackagesResponseTypeDef = TypedDict(
    "ClientListRulesPackagesResponseTypeDef",
    {"rulesPackageArns": List[str], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientPreviewAgentsResponseagentPreviewsTypeDef = TypedDict(
    "ClientPreviewAgentsResponseagentPreviewsTypeDef",
    {
        "hostname": str,
        "agentId": str,
        "autoScalingGroup": str,
        "agentHealth": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)

ClientPreviewAgentsResponseTypeDef = TypedDict(
    "ClientPreviewAgentsResponseTypeDef",
    {"agentPreviews": List[ClientPreviewAgentsResponseagentPreviewsTypeDef], "nextToken": str},
    total=False,
)

ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef = TypedDict(
    "ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)

ClientRemoveAttributesFromFindingsResponseTypeDef = TypedDict(
    "ClientRemoveAttributesFromFindingsResponseTypeDef",
    {"failedItems": Dict[str, ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef]},
    total=False,
)

_RequiredClientSetTagsForResourceTagsTypeDef = TypedDict(
    "_RequiredClientSetTagsForResourceTagsTypeDef", {"key": str}
)
_OptionalClientSetTagsForResourceTagsTypeDef = TypedDict(
    "_OptionalClientSetTagsForResourceTagsTypeDef", {"value": str}, total=False
)


class ClientSetTagsForResourceTagsTypeDef(
    _RequiredClientSetTagsForResourceTagsTypeDef, _OptionalClientSetTagsForResourceTagsTypeDef
):
    pass


ClientStartAssessmentRunResponseTypeDef = TypedDict(
    "ClientStartAssessmentRunResponseTypeDef", {"assessmentRunArn": str}, total=False
)

_RequiredListAssessmentRunAgentsPaginateFilterTypeDef = TypedDict(
    "_RequiredListAssessmentRunAgentsPaginateFilterTypeDef",
    {"agentHealths": List[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]]},
)
_OptionalListAssessmentRunAgentsPaginateFilterTypeDef = TypedDict(
    "_OptionalListAssessmentRunAgentsPaginateFilterTypeDef",
    {
        "agentHealthCodes": List[
            Literal["IDLE", "RUNNING", "SHUTDOWN", "UNHEALTHY", "THROTTLED", "UNKNOWN"]
        ]
    },
    total=False,
)


class ListAssessmentRunAgentsPaginateFilterTypeDef(
    _RequiredListAssessmentRunAgentsPaginateFilterTypeDef,
    _OptionalListAssessmentRunAgentsPaginateFilterTypeDef,
):
    pass


ListAssessmentRunAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssessmentRunAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef = TypedDict(
    "ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)

ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef = TypedDict(
    "ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "agentHealthCode": Literal[
            "IDLE", "RUNNING", "SHUTDOWN", "UNHEALTHY", "THROTTLED", "UNKNOWN"
        ],
        "agentHealthDetails": str,
        "autoScalingGroup": str,
        "telemetryMetadata": List[
            ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef
        ],
    },
    total=False,
)

ListAssessmentRunAgentsPaginateResponseTypeDef = TypedDict(
    "ListAssessmentRunAgentsPaginateResponseTypeDef",
    {
        "assessmentRunAgents": List[
            ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef = TypedDict(
    "ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)

ListAssessmentRunsPaginateFilterdurationRangeTypeDef = TypedDict(
    "ListAssessmentRunsPaginateFilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)

ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef = TypedDict(
    "ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)

ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef = TypedDict(
    "ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)

ListAssessmentRunsPaginateFilterTypeDef = TypedDict(
    "ListAssessmentRunsPaginateFilterTypeDef",
    {
        "namePattern": str,
        "states": List[
            Literal[
                "CREATED",
                "START_DATA_COLLECTION_PENDING",
                "START_DATA_COLLECTION_IN_PROGRESS",
                "COLLECTING_DATA",
                "STOP_DATA_COLLECTION_PENDING",
                "DATA_COLLECTED",
                "START_EVALUATING_RULES_PENDING",
                "EVALUATING_RULES",
                "FAILED",
                "ERROR",
                "COMPLETED",
                "COMPLETED_WITH_ERRORS",
                "CANCELED",
            ]
        ],
        "durationRange": ListAssessmentRunsPaginateFilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
        "startTimeRange": ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef,
        "completionTimeRange": ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef,
        "stateChangeTimeRange": ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef,
    },
    total=False,
)

ListAssessmentRunsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssessmentRunsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAssessmentRunsPaginateResponseTypeDef = TypedDict(
    "ListAssessmentRunsPaginateResponseTypeDef",
    {"assessmentRunArns": List[str], "NextToken": str},
    total=False,
)

ListAssessmentTargetsPaginateFilterTypeDef = TypedDict(
    "ListAssessmentTargetsPaginateFilterTypeDef", {"assessmentTargetNamePattern": str}, total=False
)

ListAssessmentTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssessmentTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAssessmentTargetsPaginateResponseTypeDef = TypedDict(
    "ListAssessmentTargetsPaginateResponseTypeDef",
    {"assessmentTargetArns": List[str], "NextToken": str},
    total=False,
)

ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef = TypedDict(
    "ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)

ListAssessmentTemplatesPaginateFilterTypeDef = TypedDict(
    "ListAssessmentTemplatesPaginateFilterTypeDef",
    {
        "namePattern": str,
        "durationRange": ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
    },
    total=False,
)

ListAssessmentTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssessmentTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAssessmentTemplatesPaginateResponseTypeDef = TypedDict(
    "ListAssessmentTemplatesPaginateResponseTypeDef",
    {"assessmentTemplateArns": List[str], "NextToken": str},
    total=False,
)

ListEventSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListEventSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef = TypedDict(
    "ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef",
    {
        "event": Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        "subscribedAt": datetime,
    },
    total=False,
)

ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef = TypedDict(
    "ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List[
            ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef
        ],
    },
    total=False,
)

ListEventSubscriptionsPaginateResponseTypeDef = TypedDict(
    "ListEventSubscriptionsPaginateResponseTypeDef",
    {
        "subscriptions": List[ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListExclusionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListExclusionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListExclusionsPaginateResponseTypeDef = TypedDict(
    "ListExclusionsPaginateResponseTypeDef",
    {"exclusionArns": List[str], "NextToken": str},
    total=False,
)

ListFindingsPaginateFilterattributesTypeDef = TypedDict(
    "ListFindingsPaginateFilterattributesTypeDef", {"key": str, "value": str}, total=False
)

ListFindingsPaginateFiltercreationTimeRangeTypeDef = TypedDict(
    "ListFindingsPaginateFiltercreationTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)

ListFindingsPaginateFilteruserAttributesTypeDef = TypedDict(
    "ListFindingsPaginateFilteruserAttributesTypeDef", {"key": str, "value": str}, total=False
)

ListFindingsPaginateFilterTypeDef = TypedDict(
    "ListFindingsPaginateFilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[Literal["Low", "Medium", "High", "Informational", "Undefined"]],
        "rulesPackageArns": List[str],
        "attributes": List[ListFindingsPaginateFilterattributesTypeDef],
        "userAttributes": List[ListFindingsPaginateFilteruserAttributesTypeDef],
        "creationTimeRange": ListFindingsPaginateFiltercreationTimeRangeTypeDef,
    },
    total=False,
)

ListFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "ListFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFindingsPaginateResponseTypeDef = TypedDict(
    "ListFindingsPaginateResponseTypeDef", {"findingArns": List[str], "NextToken": str}, total=False
)

ListRulesPackagesPaginatePaginationConfigTypeDef = TypedDict(
    "ListRulesPackagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRulesPackagesPaginateResponseTypeDef = TypedDict(
    "ListRulesPackagesPaginateResponseTypeDef",
    {"rulesPackageArns": List[str], "NextToken": str},
    total=False,
)

PreviewAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "PreviewAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

PreviewAgentsPaginateResponseagentPreviewsTypeDef = TypedDict(
    "PreviewAgentsPaginateResponseagentPreviewsTypeDef",
    {
        "hostname": str,
        "agentId": str,
        "autoScalingGroup": str,
        "agentHealth": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)

PreviewAgentsPaginateResponseTypeDef = TypedDict(
    "PreviewAgentsPaginateResponseTypeDef",
    {"agentPreviews": List[PreviewAgentsPaginateResponseagentPreviewsTypeDef], "NextToken": str},
    total=False,
)
