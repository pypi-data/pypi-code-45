"Main interface for storagegateway service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_storagegateway.type_defs import (
    DescribeTapeArchivesPaginatePaginationConfigTypeDef,
    DescribeTapeArchivesPaginateResponseTypeDef,
    DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef,
    DescribeTapeRecoveryPointsPaginateResponseTypeDef,
    DescribeTapesPaginatePaginationConfigTypeDef,
    DescribeTapesPaginateResponseTypeDef,
    DescribeVTLDevicesPaginatePaginationConfigTypeDef,
    DescribeVTLDevicesPaginateResponseTypeDef,
    ListFileSharesPaginatePaginationConfigTypeDef,
    ListFileSharesPaginateResponseTypeDef,
    ListGatewaysPaginatePaginationConfigTypeDef,
    ListGatewaysPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListTapesPaginatePaginationConfigTypeDef,
    ListTapesPaginateResponseTypeDef,
    ListVolumesPaginatePaginationConfigTypeDef,
    ListVolumesPaginateResponseTypeDef,
)


__all__ = (
    "DescribeTapeArchivesPaginator",
    "DescribeTapeRecoveryPointsPaginator",
    "DescribeTapesPaginator",
    "DescribeVTLDevicesPaginator",
    "ListFileSharesPaginator",
    "ListGatewaysPaginator",
    "ListTagsForResourcePaginator",
    "ListTapesPaginator",
    "ListVolumesPaginator",
)


class DescribeTapeArchivesPaginator(Boto3Paginator):
    """
    Paginator for `describe_tape_archives`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TapeARNs: List[str] = None,
        PaginationConfig: DescribeTapeArchivesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTapeArchivesPaginateResponseTypeDef:
        """
        [DescribeTapeArchives.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives.paginate)
        """


class DescribeTapeRecoveryPointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_tape_recovery_points`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        PaginationConfig: DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTapeRecoveryPointsPaginateResponseTypeDef:
        """
        [DescribeTapeRecoveryPoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints.paginate)
        """


class DescribeTapesPaginator(Boto3Paginator):
    """
    Paginator for `describe_tapes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        TapeARNs: List[str] = None,
        PaginationConfig: DescribeTapesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTapesPaginateResponseTypeDef:
        """
        [DescribeTapes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes.paginate)
        """


class DescribeVTLDevicesPaginator(Boto3Paginator):
    """
    Paginator for `describe_vtl_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        PaginationConfig: DescribeVTLDevicesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVTLDevicesPaginateResponseTypeDef:
        """
        [DescribeVTLDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices.paginate)
        """


class ListFileSharesPaginator(Boto3Paginator):
    """
    Paginator for `list_file_shares`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str = None,
        PaginationConfig: ListFileSharesPaginatePaginationConfigTypeDef = None,
    ) -> ListFileSharesPaginateResponseTypeDef:
        """
        [ListFileShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares.paginate)
        """


class ListGatewaysPaginator(Boto3Paginator):
    """
    Paginator for `list_gateways`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGatewaysPaginatePaginationConfigTypeDef = None
    ) -> ListGatewaysPaginateResponseTypeDef:
        """
        [ListGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways.paginate)
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
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource.paginate)
        """


class ListTapesPaginator(Boto3Paginator):
    """
    Paginator for `list_tapes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TapeARNs: List[str] = None,
        PaginationConfig: ListTapesPaginatePaginationConfigTypeDef = None,
    ) -> ListTapesPaginateResponseTypeDef:
        """
        [ListTapes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes.paginate)
        """


class ListVolumesPaginator(Boto3Paginator):
    """
    Paginator for `list_volumes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str = None,
        PaginationConfig: ListVolumesPaginatePaginationConfigTypeDef = None,
    ) -> ListVolumesPaginateResponseTypeDef:
        """
        [ListVolumes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes.paginate)
        """
