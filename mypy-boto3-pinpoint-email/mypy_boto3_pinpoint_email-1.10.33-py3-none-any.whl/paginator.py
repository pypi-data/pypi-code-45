"Main interface for pinpoint-email service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_pinpoint_email.type_defs import (
    GetDedicatedIpsPaginatePaginationConfigTypeDef,
    GetDedicatedIpsPaginateResponseTypeDef,
    ListConfigurationSetsPaginatePaginationConfigTypeDef,
    ListConfigurationSetsPaginateResponseTypeDef,
    ListDedicatedIpPoolsPaginatePaginationConfigTypeDef,
    ListDedicatedIpPoolsPaginateResponseTypeDef,
    ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef,
    ListDeliverabilityTestReportsPaginateResponseTypeDef,
    ListEmailIdentitiesPaginatePaginationConfigTypeDef,
    ListEmailIdentitiesPaginateResponseTypeDef,
)


__all__ = (
    "GetDedicatedIpsPaginator",
    "ListConfigurationSetsPaginator",
    "ListDedicatedIpPoolsPaginator",
    "ListDeliverabilityTestReportsPaginator",
    "ListEmailIdentitiesPaginator",
)


class GetDedicatedIpsPaginator(Boto3Paginator):
    """
    Paginator for `get_dedicated_ips`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PoolName: str = None,
        PaginationConfig: GetDedicatedIpsPaginatePaginationConfigTypeDef = None,
    ) -> GetDedicatedIpsPaginateResponseTypeDef:
        """
        [GetDedicatedIps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps.paginate)
        """


class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_configuration_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConfigurationSetsPaginatePaginationConfigTypeDef = None
    ) -> ListConfigurationSetsPaginateResponseTypeDef:
        """
        [ListConfigurationSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets.paginate)
        """


class ListDedicatedIpPoolsPaginator(Boto3Paginator):
    """
    Paginator for `list_dedicated_ip_pools`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDedicatedIpPoolsPaginatePaginationConfigTypeDef = None
    ) -> ListDedicatedIpPoolsPaginateResponseTypeDef:
        """
        [ListDedicatedIpPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools.paginate)
        """


class ListDeliverabilityTestReportsPaginator(Boto3Paginator):
    """
    Paginator for `list_deliverability_test_reports`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef = None
    ) -> ListDeliverabilityTestReportsPaginateResponseTypeDef:
        """
        [ListDeliverabilityTestReports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports.paginate)
        """


class ListEmailIdentitiesPaginator(Boto3Paginator):
    """
    Paginator for `list_email_identities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListEmailIdentitiesPaginatePaginationConfigTypeDef = None
    ) -> ListEmailIdentitiesPaginateResponseTypeDef:
        """
        [ListEmailIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities.paginate)
        """
