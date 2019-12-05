"Main interface for support service type defs"
from __future__ import annotations

import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientAddAttachmentsToSetAttachmentsTypeDef = TypedDict(
    "ClientAddAttachmentsToSetAttachmentsTypeDef", {"fileName": str, "data": bytes}, total=False
)

ClientAddAttachmentsToSetResponseTypeDef = TypedDict(
    "ClientAddAttachmentsToSetResponseTypeDef",
    {"attachmentSetId": str, "expiryTime": str},
    total=False,
)

ClientAddCommunicationToCaseResponseTypeDef = TypedDict(
    "ClientAddCommunicationToCaseResponseTypeDef", {"result": bool}, total=False
)

ClientCreateCaseResponseTypeDef = TypedDict(
    "ClientCreateCaseResponseTypeDef", {"caseId": str}, total=False
)

ClientDescribeAttachmentResponseattachmentTypeDef = TypedDict(
    "ClientDescribeAttachmentResponseattachmentTypeDef",
    {"fileName": str, "data": bytes},
    total=False,
)

ClientDescribeAttachmentResponseTypeDef = TypedDict(
    "ClientDescribeAttachmentResponseTypeDef",
    {"attachment": ClientDescribeAttachmentResponseattachmentTypeDef},
    total=False,
)

ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef = TypedDict(
    "ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)

ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef = TypedDict(
    "ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)

ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef = TypedDict(
    "ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef",
    {
        "communications": List[
            ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeCasesResponsecasesTypeDef = TypedDict(
    "ClientDescribeCasesResponsecasesTypeDef",
    {
        "caseId": str,
        "displayId": str,
        "subject": str,
        "status": str,
        "serviceCode": str,
        "categoryCode": str,
        "severityCode": str,
        "submittedBy": str,
        "timeCreated": str,
        "recentCommunications": ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef,
        "ccEmailAddresses": List[str],
        "language": str,
    },
    total=False,
)

ClientDescribeCasesResponseTypeDef = TypedDict(
    "ClientDescribeCasesResponseTypeDef",
    {"cases": List[ClientDescribeCasesResponsecasesTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef = TypedDict(
    "ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)

ClientDescribeCommunicationsResponsecommunicationsTypeDef = TypedDict(
    "ClientDescribeCommunicationsResponsecommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)

ClientDescribeCommunicationsResponseTypeDef = TypedDict(
    "ClientDescribeCommunicationsResponseTypeDef",
    {
        "communications": List[ClientDescribeCommunicationsResponsecommunicationsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeServicesResponseservicescategoriesTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicescategoriesTypeDef",
    {"code": str, "name": str},
    total=False,
)

ClientDescribeServicesResponseservicesTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesTypeDef",
    {
        "code": str,
        "name": str,
        "categories": List[ClientDescribeServicesResponseservicescategoriesTypeDef],
    },
    total=False,
)

ClientDescribeServicesResponseTypeDef = TypedDict(
    "ClientDescribeServicesResponseTypeDef",
    {"services": List[ClientDescribeServicesResponseservicesTypeDef]},
    total=False,
)

ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef = TypedDict(
    "ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef",
    {"code": str, "name": str},
    total=False,
)

ClientDescribeSeverityLevelsResponseTypeDef = TypedDict(
    "ClientDescribeSeverityLevelsResponseTypeDef",
    {"severityLevels": List[ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef]},
    total=False,
)

ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef",
    {"checkId": str, "status": str, "millisUntilNextRefreshable": int},
    total=False,
)

ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    {"statuses": List[ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef]},
    total=False,
)

ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef",
    {"estimatedMonthlySavings": float, "estimatedPercentMonthlySavings": float},
    total=False,
)

ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef",
    {
        "costOptimizing": ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef
    },
    total=False,
)

ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef",
    {"status": str, "region": str, "resourceId": str, "isSuppressed": bool, "metadata": List[str]},
    total=False,
)

ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
    total=False,
)

ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef,
        "categorySpecificSummary": ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef,
        "flaggedResources": List[
            ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef
        ],
    },
    total=False,
)

ClientDescribeTrustedAdvisorCheckResultResponseTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckResultResponseTypeDef",
    {"result": ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef},
    total=False,
)

ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef",
    {"estimatedMonthlySavings": float, "estimatedPercentMonthlySavings": float},
    total=False,
)

ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef",
    {
        "costOptimizing": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef
    },
    total=False,
)

ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
    total=False,
)

ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "hasFlaggedResources": bool,
        "resourcesSummary": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef,
        "categorySpecificSummary": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef,
    },
    total=False,
)

ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    {"summaries": List[ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef]},
    total=False,
)

ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef",
    {"id": str, "name": str, "description": str, "category": str, "metadata": List[str]},
    total=False,
)

ClientDescribeTrustedAdvisorChecksResponseTypeDef = TypedDict(
    "ClientDescribeTrustedAdvisorChecksResponseTypeDef",
    {"checks": List[ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef]},
    total=False,
)

ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef = TypedDict(
    "ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef",
    {"checkId": str, "status": str, "millisUntilNextRefreshable": int},
    total=False,
)

ClientRefreshTrustedAdvisorCheckResponseTypeDef = TypedDict(
    "ClientRefreshTrustedAdvisorCheckResponseTypeDef",
    {"status": ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef},
    total=False,
)

ClientResolveCaseResponseTypeDef = TypedDict(
    "ClientResolveCaseResponseTypeDef",
    {"initialCaseStatus": str, "finalCaseStatus": str},
    total=False,
)

DescribeCasesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef = TypedDict(
    "DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)

DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef = TypedDict(
    "DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)

DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef = TypedDict(
    "DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef",
    {
        "communications": List[
            DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

DescribeCasesPaginateResponsecasesTypeDef = TypedDict(
    "DescribeCasesPaginateResponsecasesTypeDef",
    {
        "caseId": str,
        "displayId": str,
        "subject": str,
        "status": str,
        "serviceCode": str,
        "categoryCode": str,
        "severityCode": str,
        "submittedBy": str,
        "timeCreated": str,
        "recentCommunications": DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef,
        "ccEmailAddresses": List[str],
        "language": str,
    },
    total=False,
)

DescribeCasesPaginateResponseTypeDef = TypedDict(
    "DescribeCasesPaginateResponseTypeDef",
    {"cases": List[DescribeCasesPaginateResponsecasesTypeDef], "NextToken": str},
    total=False,
)

DescribeCommunicationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCommunicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef = TypedDict(
    "DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)

DescribeCommunicationsPaginateResponsecommunicationsTypeDef = TypedDict(
    "DescribeCommunicationsPaginateResponsecommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)

DescribeCommunicationsPaginateResponseTypeDef = TypedDict(
    "DescribeCommunicationsPaginateResponseTypeDef",
    {
        "communications": List[DescribeCommunicationsPaginateResponsecommunicationsTypeDef],
        "NextToken": str,
    },
    total=False,
)
