"Main interface for cloudhsmv2 service Paginators"
from __future__ import annotations

from typing import Dict, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudhsmv2.type_defs import (
    DescribeBackupsPaginatePaginationConfigTypeDef,
    DescribeBackupsPaginateResponseTypeDef,
    DescribeClustersPaginatePaginationConfigTypeDef,
    DescribeClustersPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
)


__all__ = ("DescribeBackupsPaginator", "DescribeClustersPaginator", "ListTagsPaginator")


class DescribeBackupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_backups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: Dict[str, List[str]] = None,
        SortAscending: bool = None,
        PaginationConfig: DescribeBackupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeBackupsPaginateResponseTypeDef:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups.paginate)
        """


class DescribeClustersPaginator(Boto3Paginator):
    """
    Paginator for `describe_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: Dict[str, List[str]] = None,
        PaginationConfig: DescribeClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClustersPaginateResponseTypeDef:
        """
        [DescribeClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceId: str, PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None
    ) -> ListTagsPaginateResponseTypeDef:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags.paginate)
        """
