"Main interface for mediapackage service"

from mypy_boto3_mediapackage.client import Client
from mypy_boto3_mediapackage.paginator import (
    ListChannelsPaginator,
    ListHarvestJobsPaginator,
    ListOriginEndpointsPaginator,
)


__all__ = (
    "Client",
    "ListChannelsPaginator",
    "ListHarvestJobsPaginator",
    "ListOriginEndpointsPaginator",
)
