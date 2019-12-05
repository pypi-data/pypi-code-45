"Main interface for route53 service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_route53.type_defs import (
    ListHealthChecksPaginatePaginationConfigTypeDef,
    ListHealthChecksPaginateResponseTypeDef,
    ListHostedZonesPaginatePaginationConfigTypeDef,
    ListHostedZonesPaginateResponseTypeDef,
    ListQueryLoggingConfigsPaginatePaginationConfigTypeDef,
    ListQueryLoggingConfigsPaginateResponseTypeDef,
    ListResourceRecordSetsPaginatePaginationConfigTypeDef,
    ListResourceRecordSetsPaginateResponseTypeDef,
    ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef,
    ListVPCAssociationAuthorizationsPaginateResponseTypeDef,
)


__all__ = (
    "ListHealthChecksPaginator",
    "ListHostedZonesPaginator",
    "ListQueryLoggingConfigsPaginator",
    "ListResourceRecordSetsPaginator",
    "ListVPCAssociationAuthorizationsPaginator",
)


class ListHealthChecksPaginator(Boto3Paginator):
    """
    Paginator for `list_health_checks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListHealthChecksPaginatePaginationConfigTypeDef = None
    ) -> ListHealthChecksPaginateResponseTypeDef:
        """
        [ListHealthChecks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53.html#Route53.Paginator.ListHealthChecks.paginate)
        """


class ListHostedZonesPaginator(Boto3Paginator):
    """
    Paginator for `list_hosted_zones`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DelegationSetId: str = None,
        PaginationConfig: ListHostedZonesPaginatePaginationConfigTypeDef = None,
    ) -> ListHostedZonesPaginateResponseTypeDef:
        """
        [ListHostedZones.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53.html#Route53.Paginator.ListHostedZones.paginate)
        """


class ListQueryLoggingConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_query_logging_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HostedZoneId: str = None,
        PaginationConfig: ListQueryLoggingConfigsPaginatePaginationConfigTypeDef = None,
    ) -> ListQueryLoggingConfigsPaginateResponseTypeDef:
        """
        [ListQueryLoggingConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs.paginate)
        """


class ListResourceRecordSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_record_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HostedZoneId: str,
        PaginationConfig: ListResourceRecordSetsPaginatePaginationConfigTypeDef = None,
    ) -> ListResourceRecordSetsPaginateResponseTypeDef:
        """
        [ListResourceRecordSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets.paginate)
        """


class ListVPCAssociationAuthorizationsPaginator(Boto3Paginator):
    """
    Paginator for `list_vpc_association_authorizations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HostedZoneId: str,
        MaxResults: str = None,
        PaginationConfig: ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef = None,
    ) -> ListVPCAssociationAuthorizationsPaginateResponseTypeDef:
        """
        [ListVPCAssociationAuthorizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations.paginate)
        """
