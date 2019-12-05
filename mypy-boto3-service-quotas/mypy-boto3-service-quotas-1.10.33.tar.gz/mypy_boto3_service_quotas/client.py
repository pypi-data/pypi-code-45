"Main interface for service-quotas service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_service_quotas.client as client_scope

# pylint: disable=import-self
import mypy_boto3_service_quotas.paginator as paginator_scope
from mypy_boto3_service_quotas.type_defs import (
    ClientGetAssociationForServiceQuotaTemplateResponseTypeDef,
    ClientGetAwsDefaultServiceQuotaResponseTypeDef,
    ClientGetRequestedServiceQuotaChangeResponseTypeDef,
    ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef,
    ClientGetServiceQuotaResponseTypeDef,
    ClientListAwsDefaultServiceQuotasResponseTypeDef,
    ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ClientListServiceQuotasResponseTypeDef,
    ClientListServicesResponseTypeDef,
    ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef,
    ClientRequestServiceQuotaIncreaseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [ServiceQuotas.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_service_quota_template(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.associate_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.associate_service_quota_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_service_quota_increase_request_from_template(
        self, ServiceCode: str, QuotaCode: str, AwsRegion: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_service_quota_increase_request_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.delete_service_quota_increase_request_from_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_service_quota_template(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.disassociate_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.disassociate_service_quota_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_association_for_service_quota_template(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAssociationForServiceQuotaTemplateResponseTypeDef:
        """
        [Client.get_association_for_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.get_association_for_service_quota_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_aws_default_service_quota(
        self, ServiceCode: str, QuotaCode: str
    ) -> ClientGetAwsDefaultServiceQuotaResponseTypeDef:
        """
        [Client.get_aws_default_service_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.get_aws_default_service_quota)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_requested_service_quota_change(
        self, RequestId: str
    ) -> ClientGetRequestedServiceQuotaChangeResponseTypeDef:
        """
        [Client.get_requested_service_quota_change documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.get_requested_service_quota_change)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_quota(
        self, ServiceCode: str, QuotaCode: str
    ) -> ClientGetServiceQuotaResponseTypeDef:
        """
        [Client.get_service_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.get_service_quota)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_quota_increase_request_from_template(
        self, ServiceCode: str, QuotaCode: str, AwsRegion: str
    ) -> ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef:
        """
        [Client.get_service_quota_increase_request_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.get_service_quota_increase_request_from_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aws_default_service_quotas(
        self, ServiceCode: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAwsDefaultServiceQuotasResponseTypeDef:
        """
        [Client.list_aws_default_service_quotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.list_aws_default_service_quotas)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_requested_service_quota_change_history(
        self,
        ServiceCode: str = None,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef:
        """
        [Client.list_requested_service_quota_change_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.list_requested_service_quota_change_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_requested_service_quota_change_history_by_quota(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef:
        """
        [Client.list_requested_service_quota_change_history_by_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.list_requested_service_quota_change_history_by_quota)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_service_quota_increase_requests_in_template(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef:
        """
        [Client.list_service_quota_increase_requests_in_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.list_service_quota_increase_requests_in_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_service_quotas(
        self, ServiceCode: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListServiceQuotasResponseTypeDef:
        """
        [Client.list_service_quotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.list_service_quotas)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_services(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListServicesResponseTypeDef:
        """
        [Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.list_services)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_service_quota_increase_request_into_template(
        self, QuotaCode: str, ServiceCode: str, AwsRegion: str, DesiredValue: float
    ) -> ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef:
        """
        [Client.put_service_quota_increase_request_into_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.put_service_quota_increase_request_into_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_service_quota_increase(
        self, ServiceCode: str, QuotaCode: str, DesiredValue: float
    ) -> ClientRequestServiceQuotaIncreaseResponseTypeDef:
        """
        [Client.request_service_quota_increase documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Client.request_service_quota_increase)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aws_default_service_quotas"]
    ) -> paginator_scope.ListAWSDefaultServiceQuotasPaginator:
        """
        [Paginator.ListAWSDefaultServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_requested_service_quota_change_history"]
    ) -> paginator_scope.ListRequestedServiceQuotaChangeHistoryPaginator:
        """
        [Paginator.ListRequestedServiceQuotaChangeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_requested_service_quota_change_history_by_quota"]
    ) -> paginator_scope.ListRequestedServiceQuotaChangeHistoryByQuotaPaginator:
        """
        [Paginator.ListRequestedServiceQuotaChangeHistoryByQuota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_service_quota_increase_requests_in_template"]
    ) -> paginator_scope.ListServiceQuotaIncreaseRequestsInTemplatePaginator:
        """
        [Paginator.ListServiceQuotaIncreaseRequestsInTemplate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_service_quotas"]
    ) -> paginator_scope.ListServiceQuotasPaginator:
        """
        [Paginator.ListServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_services"]
    ) -> paginator_scope.ListServicesPaginator:
        """
        [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices)
        """


class Exceptions:
    AWSServiceAccessNotEnabledException: Boto3ClientError
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    DependencyAccessDeniedException: Boto3ClientError
    IllegalArgumentException: Boto3ClientError
    InvalidPaginationTokenException: Boto3ClientError
    InvalidResourceStateException: Boto3ClientError
    NoAvailableOrganizationException: Boto3ClientError
    NoSuchResourceException: Boto3ClientError
    OrganizationNotInAllFeaturesModeException: Boto3ClientError
    QuotaExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ServiceException: Boto3ClientError
    ServiceQuotaTemplateNotInUseException: Boto3ClientError
    TemplatesNotAvailableInRegionException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
