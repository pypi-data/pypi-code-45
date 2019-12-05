"Main interface for service-quotas service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_service_quotas.type_defs import (
    ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef,
    ListAWSDefaultServiceQuotasPaginateResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef,
    ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef,
    ListServiceQuotasPaginatePaginationConfigTypeDef,
    ListServiceQuotasPaginateResponseTypeDef,
    ListServicesPaginatePaginationConfigTypeDef,
    ListServicesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAWSDefaultServiceQuotasPaginator",
    "ListRequestedServiceQuotaChangeHistoryPaginator",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginator",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginator",
    "ListServiceQuotasPaginator",
    "ListServicesPaginator",
)


class ListAWSDefaultServiceQuotasPaginator(Boto3Paginator):
    """
    Paginator for `list_aws_default_service_quotas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str,
        PaginationConfig: ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef = None,
    ) -> ListAWSDefaultServiceQuotasPaginateResponseTypeDef:
        """
        [ListAWSDefaultServiceQuotas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas.paginate)
        """


class ListRequestedServiceQuotaChangeHistoryPaginator(Boto3Paginator):
    """
    Paginator for `list_requested_service_quota_change_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        PaginationConfig: ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef = None,
    ) -> ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef:
        """
        [ListRequestedServiceQuotaChangeHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory.paginate)
        """


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginator(Boto3Paginator):
    """
    Paginator for `list_requested_service_quota_change_history_by_quota`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        PaginationConfig: ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef = None,
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef:
        """
        [ListRequestedServiceQuotaChangeHistoryByQuota.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota.paginate)
        """


class ListServiceQuotaIncreaseRequestsInTemplatePaginator(Boto3Paginator):
    """
    Paginator for `list_service_quota_increase_requests_in_template`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        PaginationConfig: ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef = None,
    ) -> ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef:
        """
        [ListServiceQuotaIncreaseRequestsInTemplate.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate.paginate)
        """


class ListServiceQuotasPaginator(Boto3Paginator):
    """
    Paginator for `list_service_quotas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str,
        PaginationConfig: ListServiceQuotasPaginatePaginationConfigTypeDef = None,
    ) -> ListServiceQuotasPaginateResponseTypeDef:
        """
        [ListServiceQuotas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    Paginator for `list_services`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListServicesPaginatePaginationConfigTypeDef = None
    ) -> ListServicesPaginateResponseTypeDef:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices.paginate)
        """
