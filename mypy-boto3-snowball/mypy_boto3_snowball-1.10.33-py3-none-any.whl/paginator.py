"Main interface for snowball service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_snowball.type_defs import (
    DescribeAddressesPaginatePaginationConfigTypeDef,
    DescribeAddressesPaginateResponseTypeDef,
    ListClusterJobsPaginatePaginationConfigTypeDef,
    ListClusterJobsPaginateResponseTypeDef,
    ListClustersPaginatePaginationConfigTypeDef,
    ListClustersPaginateResponseTypeDef,
    ListCompatibleImagesPaginatePaginationConfigTypeDef,
    ListCompatibleImagesPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeAddressesPaginator",
    "ListClusterJobsPaginator",
    "ListClustersPaginator",
    "ListCompatibleImagesPaginator",
    "ListJobsPaginator",
)


class DescribeAddressesPaginator(Boto3Paginator):
    """
    Paginator for `describe_addresses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeAddressesPaginatePaginationConfigTypeDef = None
    ) -> DescribeAddressesPaginateResponseTypeDef:
        """
        [DescribeAddresses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses.paginate)
        """


class ListClusterJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_cluster_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: ListClusterJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListClusterJobsPaginateResponseTypeDef:
        """
        [ListClusterJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    Paginator for `list_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListClustersPaginatePaginationConfigTypeDef = None
    ) -> ListClustersPaginateResponseTypeDef:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/snowball.html#Snowball.Paginator.ListClusters.paginate)
        """


class ListCompatibleImagesPaginator(Boto3Paginator):
    """
    Paginator for `list_compatible_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListCompatibleImagesPaginatePaginationConfigTypeDef = None
    ) -> ListCompatibleImagesPaginateResponseTypeDef:
        """
        [ListCompatibleImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None
    ) -> ListJobsPaginateResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/snowball.html#Snowball.Paginator.ListJobs.paginate)
        """
