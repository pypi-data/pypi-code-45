"Main interface for efs service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_efs.type_defs import (
    DescribeFileSystemsPaginatePaginationConfigTypeDef,
    DescribeFileSystemsPaginateResponseTypeDef,
    DescribeMountTargetsPaginatePaginationConfigTypeDef,
    DescribeMountTargetsPaginateResponseTypeDef,
    DescribeTagsPaginatePaginationConfigTypeDef,
    DescribeTagsPaginateResponseTypeDef,
)


__all__ = ("DescribeFileSystemsPaginator", "DescribeMountTargetsPaginator", "DescribeTagsPaginator")


class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    Paginator for `describe_file_systems`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationToken: str = None,
        FileSystemId: str = None,
        PaginationConfig: DescribeFileSystemsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFileSystemsPaginateResponseTypeDef:
        """
        [DescribeFileSystems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/efs.html#EFS.Paginator.DescribeFileSystems.paginate)
        """


class DescribeMountTargetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_mount_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FileSystemId: str = None,
        MountTargetId: str = None,
        PaginationConfig: DescribeMountTargetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMountTargetsPaginateResponseTypeDef:
        """
        [DescribeMountTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/efs.html#EFS.Paginator.DescribeMountTargets.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    Paginator for `describe_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FileSystemId: str,
        PaginationConfig: DescribeTagsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTagsPaginateResponseTypeDef:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/efs.html#EFS.Paginator.DescribeTags.paginate)
        """
