"Main interface for mgh service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mgh.type_defs import (
    ListCreatedArtifactsPaginatePaginationConfigTypeDef,
    ListCreatedArtifactsPaginateResponseTypeDef,
    ListDiscoveredResourcesPaginatePaginationConfigTypeDef,
    ListDiscoveredResourcesPaginateResponseTypeDef,
    ListMigrationTasksPaginatePaginationConfigTypeDef,
    ListMigrationTasksPaginateResponseTypeDef,
    ListProgressUpdateStreamsPaginatePaginationConfigTypeDef,
    ListProgressUpdateStreamsPaginateResponseTypeDef,
)


__all__ = (
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
)


class ListCreatedArtifactsPaginator(Boto3Paginator):
    """
    Paginator for `list_created_artifacts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: ListCreatedArtifactsPaginatePaginationConfigTypeDef = None,
    ) -> ListCreatedArtifactsPaginateResponseTypeDef:
        """
        [ListCreatedArtifacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts.paginate)
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_discovered_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: ListDiscoveredResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListDiscoveredResourcesPaginateResponseTypeDef:
        """
        [ListDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources.paginate)
        """


class ListMigrationTasksPaginator(Boto3Paginator):
    """
    Paginator for `list_migration_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceName: str = None,
        PaginationConfig: ListMigrationTasksPaginatePaginationConfigTypeDef = None,
    ) -> ListMigrationTasksPaginateResponseTypeDef:
        """
        [ListMigrationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks.paginate)
        """


class ListProgressUpdateStreamsPaginator(Boto3Paginator):
    """
    Paginator for `list_progress_update_streams`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListProgressUpdateStreamsPaginatePaginationConfigTypeDef = None
    ) -> ListProgressUpdateStreamsPaginateResponseTypeDef:
        """
        [ListProgressUpdateStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams.paginate)
        """
