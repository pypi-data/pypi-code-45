"Main interface for mediapackage-vod service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediapackage_vod.type_defs import (
    ListAssetsPaginatePaginationConfigTypeDef,
    ListAssetsPaginateResponseTypeDef,
    ListPackagingConfigurationsPaginatePaginationConfigTypeDef,
    ListPackagingConfigurationsPaginateResponseTypeDef,
    ListPackagingGroupsPaginatePaginationConfigTypeDef,
    ListPackagingGroupsPaginateResponseTypeDef,
)


__all__ = (
    "ListAssetsPaginator",
    "ListPackagingConfigurationsPaginator",
    "ListPackagingGroupsPaginator",
)


class ListAssetsPaginator(Boto3Paginator):
    """
    Paginator for `list_assets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PackagingGroupId: str = None,
        PaginationConfig: ListAssetsPaginatePaginationConfigTypeDef = None,
    ) -> ListAssetsPaginateResponseTypeDef:
        """
        [ListAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets.paginate)
        """


class ListPackagingConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_packaging_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PackagingGroupId: str = None,
        PaginationConfig: ListPackagingConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> ListPackagingConfigurationsPaginateResponseTypeDef:
        """
        [ListPackagingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations.paginate)
        """


class ListPackagingGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_packaging_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPackagingGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListPackagingGroupsPaginateResponseTypeDef:
        """
        [ListPackagingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups.paginate)
        """
