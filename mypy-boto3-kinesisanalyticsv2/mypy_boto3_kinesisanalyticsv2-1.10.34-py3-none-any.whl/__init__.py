"Main interface for kinesisanalyticsv2 service"

from mypy_boto3_kinesisanalyticsv2.client import Client
from mypy_boto3_kinesisanalyticsv2.paginator import (
    ListApplicationSnapshotsPaginator,
    ListApplicationsPaginator,
)


__all__ = ("Client", "ListApplicationSnapshotsPaginator", "ListApplicationsPaginator")
