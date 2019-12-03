"Main interface for service-quotas service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientGetAssociationForServiceQuotaTemplateResponseTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseTypeDef",
    "ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef",
    "ClientGetRequestedServiceQuotaChangeResponseTypeDef",
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef",
    "ClientGetServiceQuotaResponseQuotaPeriodTypeDef",
    "ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef",
    "ClientGetServiceQuotaResponseQuotaTypeDef",
    "ClientGetServiceQuotaResponseTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ClientListServiceQuotasResponseQuotasErrorReasonTypeDef",
    "ClientListServiceQuotasResponseQuotasPeriodTypeDef",
    "ClientListServiceQuotasResponseQuotasUsageMetricTypeDef",
    "ClientListServiceQuotasResponseQuotasTypeDef",
    "ClientListServiceQuotasResponseTypeDef",
    "ClientListServicesResponseServicesTypeDef",
    "ClientListServicesResponseTypeDef",
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef",
    "ClientRequestServiceQuotaIncreaseResponseTypeDef",
    "ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef",
    "ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef",
    "ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef",
    "ListServiceQuotasPaginatePaginationConfigTypeDef",
    "ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
    "ListServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    "ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    "ListServiceQuotasPaginateResponseQuotasTypeDef",
    "ListServiceQuotasPaginateResponseTypeDef",
    "ListServicesPaginatePaginationConfigTypeDef",
    "ListServicesPaginateResponseServicesTypeDef",
    "ListServicesPaginateResponseTypeDef",
)


_ClientGetAssociationForServiceQuotaTemplateResponseTypeDef = TypedDict(
    "_ClientGetAssociationForServiceQuotaTemplateResponseTypeDef",
    {"ServiceQuotaTemplateAssociationStatus": Literal["ASSOCIATED", "DISASSOCIATED"]},
    total=False,
)


class ClientGetAssociationForServiceQuotaTemplateResponseTypeDef(
    _ClientGetAssociationForServiceQuotaTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceQuotaTemplateAssociationStatus** *(string) --*

        Specifies whether the template is ``ASSOCIATED`` or ``DISASSOCIATED`` . If the template is
        ``ASSOCIATED`` , then it requests service quota increases for all new accounts created in
        your organization.
    """


_ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef",
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


class ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef
):
    pass


_ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)


class ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef
):
    pass


_ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef
):
    pass


_ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef",
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


class ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef
):
    """
    - **Quota** *(dict) --*

      Returns the  ServiceQuota object which contains all values for a quota.
      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.
    """


_ClientGetAwsDefaultServiceQuotaResponseTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseTypeDef",
    {"Quota": ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef},
    total=False,
)


class ClientGetAwsDefaultServiceQuotaResponseTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseTypeDef
):
    """
    - *(dict) --*

      - **Quota** *(dict) --*

        Returns the  ServiceQuota object which contains all values for a quota.
        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.
    """


_ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef = TypedDict(
    "_ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef",
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


class ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef(
    _ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef
):
    """
    - **RequestedQuota** *(dict) --*

      Returns the ``RequestedServiceQuotaChange`` object for the specific increase request.
      - **Id** *(string) --*

        The unique identifier of a requested service quota change.
    """


_ClientGetRequestedServiceQuotaChangeResponseTypeDef = TypedDict(
    "_ClientGetRequestedServiceQuotaChangeResponseTypeDef",
    {"RequestedQuota": ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef},
    total=False,
)


class ClientGetRequestedServiceQuotaChangeResponseTypeDef(
    _ClientGetRequestedServiceQuotaChangeResponseTypeDef
):
    """
    - *(dict) --*

      - **RequestedQuota** *(dict) --*

        Returns the ``RequestedServiceQuotaChange`` object for the specific increase request.
        - **Id** *(string) --*

          The unique identifier of a requested service quota change.
    """


_ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "_ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
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


class ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef(
    _ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
):
    """
    - **ServiceQuotaIncreaseRequestInTemplate** *(dict) --*

      This object contains the details about the quota increase request.
      - **ServiceCode** *(string) --*

        The code identifier for the AWS service specified in the increase request.
    """


_ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef = TypedDict(
    "_ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
    },
    total=False,
)


class ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef(
    _ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceQuotaIncreaseRequestInTemplate** *(dict) --*

        This object contains the details about the quota increase request.
        - **ServiceCode** *(string) --*

          The code identifier for the AWS service specified in the increase request.
    """


_ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef",
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


class ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef(
    _ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef
):
    pass


_ClientGetServiceQuotaResponseQuotaPeriodTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseQuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)


class ClientGetServiceQuotaResponseQuotaPeriodTypeDef(
    _ClientGetServiceQuotaResponseQuotaPeriodTypeDef
):
    pass


_ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef(
    _ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef
):
    pass


_ClientGetServiceQuotaResponseQuotaTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseQuotaTypeDef",
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


class ClientGetServiceQuotaResponseQuotaTypeDef(_ClientGetServiceQuotaResponseQuotaTypeDef):
    """
    - **Quota** *(dict) --*

      Returns the  ServiceQuota object which contains all values for a quota.
      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.
    """


_ClientGetServiceQuotaResponseTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseTypeDef",
    {"Quota": ClientGetServiceQuotaResponseQuotaTypeDef},
    total=False,
)


class ClientGetServiceQuotaResponseTypeDef(_ClientGetServiceQuotaResponseTypeDef):
    """
    - *(dict) --*

      - **Quota** *(dict) --*

        Returns the  ServiceQuota object which contains all values for a quota.
        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.
    """


_ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef",
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


class ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef
):
    pass


_ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)


class ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef
):
    pass


_ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef
):
    pass


_ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef",
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


class ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef
):
    pass


_ClientListAwsDefaultServiceQuotasResponseTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef]},
    total=False,
)


class ClientListAwsDefaultServiceQuotasResponseTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a
        previous request that indicates that there's more output available. In a subsequent call,
        set it to the value of the previous call's ``NextToken`` response to indicate where the
        output should continue from.
    """


_ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef = TypedDict(
    "_ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef",
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


class ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef(
    _ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef
):
    pass


_ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "_ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[
            ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef
        ],
    },
    total=False,
)


class ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef(
    _ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If present in the response, this value indicates there's more output available that what's
        included in the current response. This can occur even when the response includes no values
        at all, such as when you ask for a filtered view of a very long list. Use this value in the
        ``NextToken`` request parameter in a subsequent call to the operation to continue processing
        and get the next part of the output. You should repeat this until the ``NextToken`` response
        element comes back empty (as ``null`` ).
    """


_ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef = TypedDict(
    "_ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef",
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


class ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef(
    _ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef
):
    pass


_ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "_ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[
            ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef
        ],
    },
    total=False,
)


class ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef(
    _ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If present in the response, this value indicates there's more output available that what's
        included in the current response. This can occur even when the response includes no values
        at all, such as when you ask for a filtered view of a very long list. Use this value in the
        ``NextToken`` request parameter in a subsequent call to the operation to continue processing
        and get the next part of the output. You should repeat this until the ``NextToken`` response
        element comes back empty (as ``null`` ).
    """


_ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef = TypedDict(
    "_ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
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


class ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef(
    _ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
):
    """
    - *(dict) --*

      A structure that contains information about one service quota increase request.
      - **ServiceCode** *(string) --*

        The code identifier for the AWS service specified in the increase request.
    """


_ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "_ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef(
    _ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceQuotaIncreaseRequestInTemplateList** *(list) --*

        Returns the list of values of the quota increase request in the template.
        - *(dict) --*

          A structure that contains information about one service quota increase request.
          - **ServiceCode** *(string) --*

            The code identifier for the AWS service specified in the increase request.
    """


_ClientListServiceQuotasResponseQuotasErrorReasonTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseQuotasErrorReasonTypeDef",
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


class ClientListServiceQuotasResponseQuotasErrorReasonTypeDef(
    _ClientListServiceQuotasResponseQuotasErrorReasonTypeDef
):
    pass


_ClientListServiceQuotasResponseQuotasPeriodTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)


class ClientListServiceQuotasResponseQuotasPeriodTypeDef(
    _ClientListServiceQuotasResponseQuotasPeriodTypeDef
):
    pass


_ClientListServiceQuotasResponseQuotasUsageMetricTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ClientListServiceQuotasResponseQuotasUsageMetricTypeDef(
    _ClientListServiceQuotasResponseQuotasUsageMetricTypeDef
):
    pass


_ClientListServiceQuotasResponseQuotasTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseQuotasTypeDef",
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


class ClientListServiceQuotasResponseQuotasTypeDef(_ClientListServiceQuotasResponseQuotasTypeDef):
    pass


_ClientListServiceQuotasResponseTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ClientListServiceQuotasResponseQuotasTypeDef]},
    total=False,
)


class ClientListServiceQuotasResponseTypeDef(_ClientListServiceQuotasResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If present in the response, this value indicates there's more output available that what's
        included in the current response. This can occur even when the response includes no values
        at all, such as when you ask for a filtered view of a very long list. Use this value in the
        ``NextToken`` request parameter in a subsequent call to the operation to continue processing
        and get the next part of the output. You should repeat this until the ``NextToken`` response
        element comes back empty (as ``null`` ).
    """


_ClientListServicesResponseServicesTypeDef = TypedDict(
    "_ClientListServicesResponseServicesTypeDef",
    {"ServiceCode": str, "ServiceName": str},
    total=False,
)


class ClientListServicesResponseServicesTypeDef(_ClientListServicesResponseServicesTypeDef):
    pass


_ClientListServicesResponseTypeDef = TypedDict(
    "_ClientListServicesResponseTypeDef",
    {"NextToken": str, "Services": List[ClientListServicesResponseServicesTypeDef]},
    total=False,
)


class ClientListServicesResponseTypeDef(_ClientListServicesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If present in the response, this value indicates there's more output available that what's
        included in the current response. This can occur even when the response includes no values
        at all, such as when you ask for a filtered view of a very long list. Use this value in the
        ``NextToken`` request parameter in a subsequent call to the operation to continue processing
        and get the next part of the output. You should repeat this until the ``NextToken`` response
        element comes back empty (as ``null`` ).
    """


_ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "_ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
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


class ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef(
    _ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
):
    """
    - **ServiceQuotaIncreaseRequestInTemplate** *(dict) --*

      A structure that contains information about one service quota increase request.
      - **ServiceCode** *(string) --*

        The code identifier for the AWS service specified in the increase request.
    """


_ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef = TypedDict(
    "_ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
    },
    total=False,
)


class ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef(
    _ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceQuotaIncreaseRequestInTemplate** *(dict) --*

        A structure that contains information about one service quota increase request.
        - **ServiceCode** *(string) --*

          The code identifier for the AWS service specified in the increase request.
    """


_ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef = TypedDict(
    "_ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef",
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


class ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef(
    _ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef
):
    """
    - **RequestedQuota** *(dict) --*

      Returns a list of service quota requests.
      - **Id** *(string) --*

        The unique identifier of a requested service quota change.
    """


_ClientRequestServiceQuotaIncreaseResponseTypeDef = TypedDict(
    "_ClientRequestServiceQuotaIncreaseResponseTypeDef",
    {"RequestedQuota": ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef},
    total=False,
)


class ClientRequestServiceQuotaIncreaseResponseTypeDef(
    _ClientRequestServiceQuotaIncreaseResponseTypeDef
):
    """
    - *(dict) --*

      - **RequestedQuota** *(dict) --*

        Returns a list of service quota requests.
        - **Id** *(string) --*

          The unique identifier of a requested service quota change.
    """


_ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef(
    _ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
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


class ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef
):
    pass


_ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)


class ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef
):
    pass


_ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef
):
    pass


_ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef",
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


class ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef
):
    """
    - *(dict) --*

      A structure that contains the full set of details that define the service quota.
      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.
    """


_ListAWSDefaultServiceQuotasPaginateResponseTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseTypeDef",
    {"Quotas": List[ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef]},
    total=False,
)


class ListAWSDefaultServiceQuotasPaginateResponseTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Quotas** *(list) --*

        A list of the quotas in the account with the AWS default values.
        - *(dict) --*

          A structure that contains the full set of details that define the service quota.
          - **ServiceCode** *(string) --*

            Specifies the service that you want to use.
    """


_ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef(
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef",
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


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef(
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef
):
    """
    - *(dict) --*

      A structure that contains information about a requested change for a quota.
      - **Id** *(string) --*

        The unique identifier of a requested service quota change.
    """


_ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef",
    {
        "RequestedQuotas": List[
            ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef
        ]
    },
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef(
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **RequestedQuotas** *(list) --*

        Returns a list of service quota requests.
        - *(dict) --*

          A structure that contains information about a requested change for a quota.
          - **Id** *(string) --*

            The unique identifier of a requested service quota change.
    """


_ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef(
    _ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef",
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


class ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef(
    _ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef
):
    """
    - *(dict) --*

      A structure that contains information about a requested change for a quota.
      - **Id** *(string) --*

        The unique identifier of a requested service quota change.
    """


_ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef",
    {
        "RequestedQuotas": List[
            ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef
        ]
    },
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef(
    _ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **RequestedQuotas** *(list) --*

        Returns a list of service quota requests.
        - *(dict) --*

          A structure that contains information about a requested change for a quota.
          - **Id** *(string) --*

            The unique identifier of a requested service quota change.
    """


_ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef = TypedDict(
    "_ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef(
    _ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef = TypedDict(
    "_ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
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


class ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef(
    _ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
):
    """
    - *(dict) --*

      A structure that contains information about one service quota increase request.
      - **ServiceCode** *(string) --*

        The code identifier for the AWS service specified in the increase request.
    """


_ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef = TypedDict(
    "_ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
        ]
    },
    total=False,
)


class ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef(
    _ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceQuotaIncreaseRequestInTemplateList** *(list) --*

        Returns the list of values of the quota increase request in the template.
        - *(dict) --*

          A structure that contains information about one service quota increase request.
          - **ServiceCode** *(string) --*

            The code identifier for the AWS service specified in the increase request.
    """


_ListServiceQuotasPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServiceQuotasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServiceQuotasPaginatePaginationConfigTypeDef(
    _ListServiceQuotasPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
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


class ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef(
    _ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef
):
    pass


_ListServiceQuotasPaginateResponseQuotasPeriodTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)


class ListServiceQuotasPaginateResponseQuotasPeriodTypeDef(
    _ListServiceQuotasPaginateResponseQuotasPeriodTypeDef
):
    pass


_ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef(
    _ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef
):
    pass


_ListServiceQuotasPaginateResponseQuotasTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseQuotasTypeDef",
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


class ListServiceQuotasPaginateResponseQuotasTypeDef(
    _ListServiceQuotasPaginateResponseQuotasTypeDef
):
    """
    - *(dict) --*

      A structure that contains the full set of details that define the service quota.
      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.
    """


_ListServiceQuotasPaginateResponseTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseTypeDef",
    {"Quotas": List[ListServiceQuotasPaginateResponseQuotasTypeDef]},
    total=False,
)


class ListServiceQuotasPaginateResponseTypeDef(_ListServiceQuotasPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Quotas** *(list) --*

        The response information for a quota lists all attribute information for the quota.
        - *(dict) --*

          A structure that contains the full set of details that define the service quota.
          - **ServiceCode** *(string) --*

            Specifies the service that you want to use.
    """


_ListServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServicesPaginatePaginationConfigTypeDef(_ListServicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServicesPaginateResponseServicesTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesTypeDef",
    {"ServiceCode": str, "ServiceName": str},
    total=False,
)


class ListServicesPaginateResponseServicesTypeDef(_ListServicesPaginateResponseServicesTypeDef):
    """
    - *(dict) --*

      A structure that contains the ``ServiceName`` and ``ServiceCode`` . It does not include all
      details of the service quota. To get those values, use the  ListServiceQuotas operation.
      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.
    """


_ListServicesPaginateResponseTypeDef = TypedDict(
    "_ListServicesPaginateResponseTypeDef",
    {"Services": List[ListServicesPaginateResponseServicesTypeDef]},
    total=False,
)


class ListServicesPaginateResponseTypeDef(_ListServicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Services** *(list) --*

        Returns a list of services.
        - *(dict) --*

          A structure that contains the ``ServiceName`` and ``ServiceCode`` . It does not include
          all details of the service quota. To get those values, use the  ListServiceQuotas
          operation.
          - **ServiceCode** *(string) --*

            Specifies the service that you want to use.
    """
