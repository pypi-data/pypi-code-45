"Main interface for kinesisanalyticsv2 service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kinesisanalyticsv2.type_defs import (
    ListApplicationSnapshotsPaginatePaginationConfigTypeDef,
    ListApplicationSnapshotsPaginateResponseTypeDef,
    ListApplicationsPaginatePaginationConfigTypeDef,
    ListApplicationsPaginateResponseTypeDef,
)


__all__ = ("ListApplicationSnapshotsPaginator", "ListApplicationsPaginator")


class ListApplicationSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `list_application_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationName: str,
        PaginationConfig: ListApplicationSnapshotsPaginatePaginationConfigTypeDef = None,
    ) -> ListApplicationSnapshotsPaginateResponseTypeDef:
        """
        [ListApplicationSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots.paginate)
        """


class ListApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListApplicationsPaginatePaginationConfigTypeDef = None
    ) -> ListApplicationsPaginateResponseTypeDef:
        """
        [ListApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplications.paginate)
        """
