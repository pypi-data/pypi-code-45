"Main interface for route53resolver service"

from mypy_boto3_route53resolver.client import Client
from mypy_boto3_route53resolver.paginator import ListTagsForResourcePaginator


__all__ = ("Client", "ListTagsForResourcePaginator")
