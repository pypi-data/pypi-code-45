"Main interface for ds service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ds.type_defs import (
    DescribeDirectoriesPaginatePaginationConfigTypeDef,
    DescribeDirectoriesPaginateResponseTypeDef,
    DescribeDomainControllersPaginatePaginationConfigTypeDef,
    DescribeDomainControllersPaginateResponseTypeDef,
    DescribeSharedDirectoriesPaginatePaginationConfigTypeDef,
    DescribeSharedDirectoriesPaginateResponseTypeDef,
    DescribeSnapshotsPaginatePaginationConfigTypeDef,
    DescribeSnapshotsPaginateResponseTypeDef,
    DescribeTrustsPaginatePaginationConfigTypeDef,
    DescribeTrustsPaginateResponseTypeDef,
    ListIpRoutesPaginatePaginationConfigTypeDef,
    ListIpRoutesPaginateResponseTypeDef,
    ListLogSubscriptionsPaginatePaginationConfigTypeDef,
    ListLogSubscriptionsPaginateResponseTypeDef,
    ListSchemaExtensionsPaginatePaginationConfigTypeDef,
    ListSchemaExtensionsPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
)


__all__ = (
    "DescribeDirectoriesPaginator",
    "DescribeDomainControllersPaginator",
    "DescribeSharedDirectoriesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeTrustsPaginator",
    "ListIpRoutesPaginator",
    "ListLogSubscriptionsPaginator",
    "ListSchemaExtensionsPaginator",
    "ListTagsForResourcePaginator",
)


class DescribeDirectoriesPaginator(Boto3Paginator):
    """
    Paginator for `describe_directories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryIds: List[str] = None,
        PaginationConfig: DescribeDirectoriesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDirectoriesPaginateResponseTypeDef:
        """
        [DescribeDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories.paginate)
        """


class DescribeDomainControllersPaginator(Boto3Paginator):
    """
    Paginator for `describe_domain_controllers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        PaginationConfig: DescribeDomainControllersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDomainControllersPaginateResponseTypeDef:
        """
        [DescribeDomainControllers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers.paginate)
        """


class DescribeSharedDirectoriesPaginator(Boto3Paginator):
    """
    Paginator for `describe_shared_directories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        PaginationConfig: DescribeSharedDirectoriesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSharedDirectoriesPaginateResponseTypeDef:
        """
        [DescribeSharedDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories.paginate)
        """


class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `describe_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        PaginationConfig: DescribeSnapshotsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSnapshotsPaginateResponseTypeDef:
        """
        [DescribeSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots.paginate)
        """


class DescribeTrustsPaginator(Boto3Paginator):
    """
    Paginator for `describe_trusts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        PaginationConfig: DescribeTrustsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTrustsPaginateResponseTypeDef:
        """
        [DescribeTrusts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts.paginate)
        """


class ListIpRoutesPaginator(Boto3Paginator):
    """
    Paginator for `list_ip_routes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DirectoryId: str, PaginationConfig: ListIpRoutesPaginatePaginationConfigTypeDef = None
    ) -> ListIpRoutesPaginateResponseTypeDef:
        """
        [ListIpRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes.paginate)
        """


class ListLogSubscriptionsPaginator(Boto3Paginator):
    """
    Paginator for `list_log_subscriptions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryId: str = None,
        PaginationConfig: ListLogSubscriptionsPaginatePaginationConfigTypeDef = None,
    ) -> ListLogSubscriptionsPaginateResponseTypeDef:
        """
        [ListLogSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions.paginate)
        """


class ListSchemaExtensionsPaginator(Boto3Paginator):
    """
    Paginator for `list_schema_extensions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryId: str,
        PaginationConfig: ListSchemaExtensionsPaginatePaginationConfigTypeDef = None,
    ) -> ListSchemaExtensionsPaginateResponseTypeDef:
        """
        [ListSchemaExtensions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceId: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource.paginate)
        """
