"Main interface for route53 service"

from mypy_boto3_route53.client import Client
from mypy_boto3_route53.paginator import (
    ListHealthChecksPaginator,
    ListHostedZonesPaginator,
    ListQueryLoggingConfigsPaginator,
    ListResourceRecordSetsPaginator,
    ListVPCAssociationAuthorizationsPaginator,
)
from mypy_boto3_route53.waiter import ResourceRecordSetsChangedWaiter


__all__ = (
    "Client",
    "ResourceRecordSetsChangedWaiter",
    "ListHealthChecksPaginator",
    "ListHostedZonesPaginator",
    "ListQueryLoggingConfigsPaginator",
    "ListResourceRecordSetsPaginator",
    "ListVPCAssociationAuthorizationsPaginator",
)
