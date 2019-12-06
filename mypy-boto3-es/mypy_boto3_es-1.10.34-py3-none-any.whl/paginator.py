"Main interface for es service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_es.type_defs import (
    DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef,
    DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef,
    DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef,
    DescribeReservedElasticsearchInstancesPaginateResponseTypeDef,
    GetUpgradeHistoryPaginatePaginationConfigTypeDef,
    GetUpgradeHistoryPaginateResponseTypeDef,
    ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef,
    ListElasticsearchInstanceTypesPaginateResponseTypeDef,
    ListElasticsearchVersionsPaginatePaginationConfigTypeDef,
    ListElasticsearchVersionsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeReservedElasticsearchInstanceOfferingsPaginator",
    "DescribeReservedElasticsearchInstancesPaginator",
    "GetUpgradeHistoryPaginator",
    "ListElasticsearchInstanceTypesPaginator",
    "ListElasticsearchVersionsPaginator",
)


class DescribeReservedElasticsearchInstanceOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_elasticsearch_instance_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        PaginationConfig: DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef:
        """
        [DescribeReservedElasticsearchInstanceOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings.paginate)
        """


class DescribeReservedElasticsearchInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_elasticsearch_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedElasticsearchInstanceId: str = None,
        PaginationConfig: DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedElasticsearchInstancesPaginateResponseTypeDef:
        """
        [DescribeReservedElasticsearchInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances.paginate)
        """


class GetUpgradeHistoryPaginator(Boto3Paginator):
    """
    Paginator for `get_upgrade_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DomainName: str,
        PaginationConfig: GetUpgradeHistoryPaginatePaginationConfigTypeDef = None,
    ) -> GetUpgradeHistoryPaginateResponseTypeDef:
        """
        [GetUpgradeHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory.paginate)
        """


class ListElasticsearchInstanceTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_elasticsearch_instance_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        PaginationConfig: ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListElasticsearchInstanceTypesPaginateResponseTypeDef:
        """
        [ListElasticsearchInstanceTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes.paginate)
        """


class ListElasticsearchVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_elasticsearch_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListElasticsearchVersionsPaginatePaginationConfigTypeDef = None
    ) -> ListElasticsearchVersionsPaginateResponseTypeDef:
        """
        [ListElasticsearchVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions.paginate)
        """
