"Main interface for serverlessrepo service"

from mypy_boto3_serverlessrepo.client import Client
from mypy_boto3_serverlessrepo.paginator import (
    ListApplicationDependenciesPaginator,
    ListApplicationVersionsPaginator,
    ListApplicationsPaginator,
)


__all__ = (
    "Client",
    "ListApplicationDependenciesPaginator",
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
)
