"Main interface for globalaccelerator service"

from mypy_boto3_globalaccelerator.client import Client
from mypy_boto3_globalaccelerator.paginator import (
    ListAcceleratorsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)


__all__ = (
    "Client",
    "ListAcceleratorsPaginator",
    "ListEndpointGroupsPaginator",
    "ListListenersPaginator",
)
