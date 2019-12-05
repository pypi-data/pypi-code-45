"Main interface for mediaconnect service"

from mypy_boto3_mediaconnect.client import Client
from mypy_boto3_mediaconnect.paginator import ListEntitlementsPaginator, ListFlowsPaginator


__all__ = ("Client", "ListEntitlementsPaginator", "ListFlowsPaginator")
