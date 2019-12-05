"Main interface for service-quotas service type defs"
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


ClientGetAssociationForServiceQuotaTemplateResponseTypeDef = TypedDict(
    "ClientGetAssociationForServiceQuotaTemplateResponseTypeDef",
    {"ServiceQuotaTemplateAssociationStatus": Literal["ASSOCIATED", "DISASSOCIATED"]},
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef,
        "Period": ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef,
        "ErrorReason": ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef,
    },
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseTypeDef",
    {"Quota": ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef},
    total=False,
)

ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef = TypedDict(
    "ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ClientGetRequestedServiceQuotaChangeResponseTypeDef = TypedDict(
    "ClientGetRequestedServiceQuotaChangeResponseTypeDef",
    {"RequestedQuota": ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef},
    total=False,
)

ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef = TypedDict(
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
    },
    total=False,
)

ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientGetServiceQuotaResponseQuotaPeriodTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseQuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ClientGetServiceQuotaResponseQuotaTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef,
        "Period": ClientGetServiceQuotaResponseQuotaPeriodTypeDef,
        "ErrorReason": ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef,
    },
    total=False,
)

ClientGetServiceQuotaResponseTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseTypeDef",
    {"Quota": ClientGetServiceQuotaResponseQuotaTypeDef},
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef,
        "Period": ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef,
        "ErrorReason": ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef]},
    total=False,
)

ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef = TypedDict(
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[
            ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef
        ],
    },
    total=False,
)

ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef = TypedDict(
    "ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[
            ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef
        ],
    },
    total=False,
)

ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef = TypedDict(
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListServiceQuotasResponseQuotasErrorReasonTypeDef = TypedDict(
    "ClientListServiceQuotasResponseQuotasErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientListServiceQuotasResponseQuotasPeriodTypeDef = TypedDict(
    "ClientListServiceQuotasResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ClientListServiceQuotasResponseQuotasUsageMetricTypeDef = TypedDict(
    "ClientListServiceQuotasResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ClientListServiceQuotasResponseQuotasTypeDef = TypedDict(
    "ClientListServiceQuotasResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientListServiceQuotasResponseQuotasUsageMetricTypeDef,
        "Period": ClientListServiceQuotasResponseQuotasPeriodTypeDef,
        "ErrorReason": ClientListServiceQuotasResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)

ClientListServiceQuotasResponseTypeDef = TypedDict(
    "ClientListServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ClientListServiceQuotasResponseQuotasTypeDef]},
    total=False,
)

ClientListServicesResponseServicesTypeDef = TypedDict(
    "ClientListServicesResponseServicesTypeDef",
    {"ServiceCode": str, "ServiceName": str},
    total=False,
)

ClientListServicesResponseTypeDef = TypedDict(
    "ClientListServicesResponseTypeDef",
    {"NextToken": str, "Services": List[ClientListServicesResponseServicesTypeDef]},
    total=False,
)

ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef = TypedDict(
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
    },
    total=False,
)

ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef = TypedDict(
    "ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ClientRequestServiceQuotaIncreaseResponseTypeDef = TypedDict(
    "ClientRequestServiceQuotaIncreaseResponseTypeDef",
    {"RequestedQuota": ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef},
    total=False,
)

ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef,
        "Period": ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef,
        "ErrorReason": ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)

ListAWSDefaultServiceQuotasPaginateResponseTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasPaginateResponseTypeDef",
    {"Quotas": List[ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef]},
    total=False,
)

ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef",
    {
        "RequestedQuotas": List[
            ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef
        ]
    },
    total=False,
)

ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef",
    {
        "RequestedQuotas": List[
            ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef
        ]
    },
    total=False,
)

ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
        ]
    },
    total=False,
)

ListServiceQuotasPaginatePaginationConfigTypeDef = TypedDict(
    "ListServiceQuotasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef = TypedDict(
    "ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ListServiceQuotasPaginateResponseQuotasPeriodTypeDef = TypedDict(
    "ListServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef = TypedDict(
    "ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ListServiceQuotasPaginateResponseQuotasTypeDef = TypedDict(
    "ListServiceQuotasPaginateResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef,
        "Period": ListServiceQuotasPaginateResponseQuotasPeriodTypeDef,
        "ErrorReason": ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)

ListServiceQuotasPaginateResponseTypeDef = TypedDict(
    "ListServiceQuotasPaginateResponseTypeDef",
    {"Quotas": List[ListServiceQuotasPaginateResponseQuotasTypeDef]},
    total=False,
)

ListServicesPaginatePaginationConfigTypeDef = TypedDict(
    "ListServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListServicesPaginateResponseServicesTypeDef = TypedDict(
    "ListServicesPaginateResponseServicesTypeDef",
    {"ServiceCode": str, "ServiceName": str},
    total=False,
)

ListServicesPaginateResponseTypeDef = TypedDict(
    "ListServicesPaginateResponseTypeDef",
    {"Services": List[ListServicesPaginateResponseServicesTypeDef]},
    total=False,
)
