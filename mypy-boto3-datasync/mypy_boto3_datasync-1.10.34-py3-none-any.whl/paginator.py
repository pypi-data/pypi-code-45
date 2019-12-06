"Main interface for datasync service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_datasync.type_defs import (
    ListAgentsPaginatePaginationConfigTypeDef,
    ListAgentsPaginateResponseTypeDef,
    ListLocationsPaginatePaginationConfigTypeDef,
    ListLocationsPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListTaskExecutionsPaginatePaginationConfigTypeDef,
    ListTaskExecutionsPaginateResponseTypeDef,
    ListTasksPaginatePaginationConfigTypeDef,
    ListTasksPaginateResponseTypeDef,
)


__all__ = (
    "ListAgentsPaginator",
    "ListLocationsPaginator",
    "ListTagsForResourcePaginator",
    "ListTaskExecutionsPaginator",
    "ListTasksPaginator",
)


class ListAgentsPaginator(Boto3Paginator):
    """
    Paginator for `list_agents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListAgentsPaginatePaginationConfigTypeDef = None
    ) -> ListAgentsPaginateResponseTypeDef:
        """
        [ListAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/datasync.html#DataSync.Paginator.ListAgents.paginate)
        """


class ListLocationsPaginator(Boto3Paginator):
    """
    Paginator for `list_locations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListLocationsPaginatePaginationConfigTypeDef = None
    ) -> ListLocationsPaginateResponseTypeDef:
        """
        [ListLocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/datasync.html#DataSync.Paginator.ListLocations.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource.paginate)
        """


class ListTaskExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_task_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TaskArn: str = None,
        PaginationConfig: ListTaskExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListTaskExecutionsPaginateResponseTypeDef:
        """
        [ListTaskExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions.paginate)
        """


class ListTasksPaginator(Boto3Paginator):
    """
    Paginator for `list_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListTasksPaginatePaginationConfigTypeDef = None
    ) -> ListTasksPaginateResponseTypeDef:
        """
        [ListTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/datasync.html#DataSync.Paginator.ListTasks.paginate)
        """
