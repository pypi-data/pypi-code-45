"Main interface for mediapackage service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediapackage.type_defs import (
    ListChannelsPaginatePaginationConfigTypeDef,
    ListChannelsPaginateResponseTypeDef,
    ListHarvestJobsPaginatePaginationConfigTypeDef,
    ListHarvestJobsPaginateResponseTypeDef,
    ListOriginEndpointsPaginatePaginationConfigTypeDef,
    ListOriginEndpointsPaginateResponseTypeDef,
)


__all__ = ("ListChannelsPaginator", "ListHarvestJobsPaginator", "ListOriginEndpointsPaginator")


class ListChannelsPaginator(Boto3Paginator):
    """
    Paginator for `list_channels`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListChannelsPaginatePaginationConfigTypeDef = None
    ) -> ListChannelsPaginateResponseTypeDef:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels.paginate)
        """


class ListHarvestJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_harvest_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        PaginationConfig: ListHarvestJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListHarvestJobsPaginateResponseTypeDef:
        """
        [ListHarvestJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs.paginate)
        """


class ListOriginEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `list_origin_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChannelId: str = None,
        PaginationConfig: ListOriginEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> ListOriginEndpointsPaginateResponseTypeDef:
        """
        [ListOriginEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints.paginate)
        """
