"Main interface for support service"

from mypy_boto3_support.client import Client
from mypy_boto3_support.paginator import DescribeCasesPaginator, DescribeCommunicationsPaginator


__all__ = ("Client", "DescribeCasesPaginator", "DescribeCommunicationsPaginator")
