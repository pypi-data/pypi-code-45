"Main interface for fsx service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_fsx.type_defs import (
    DescribeBackupsPaginateFiltersTypeDef,
    DescribeBackupsPaginatePaginationConfigTypeDef,
    DescribeBackupsPaginateResponseTypeDef,
    DescribeFileSystemsPaginatePaginationConfigTypeDef,
    DescribeFileSystemsPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
)


__all__ = (
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "ListTagsForResourcePaginator",
)


class DescribeBackupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_backups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BackupIds: List[str] = None,
        Filters: List[DescribeBackupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeBackupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeBackupsPaginateResponseTypeDef:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/fsx.html#FSx.Paginator.DescribeBackups.paginate)
        """


class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    Paginator for `describe_file_systems`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FileSystemIds: List[str] = None,
        PaginationConfig: DescribeFileSystemsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFileSystemsPaginateResponseTypeDef:
        """
        [DescribeFileSystems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceARN: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/fsx.html#FSx.Paginator.ListTagsForResource.paginate)
        """
