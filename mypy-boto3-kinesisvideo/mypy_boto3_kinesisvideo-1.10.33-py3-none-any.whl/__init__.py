"Main interface for kinesisvideo service"

from mypy_boto3_kinesisvideo.client import Client
from mypy_boto3_kinesisvideo.paginator import ListSignalingChannelsPaginator, ListStreamsPaginator


__all__ = ("Client", "ListSignalingChannelsPaginator", "ListStreamsPaginator")
