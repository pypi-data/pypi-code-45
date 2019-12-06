"Main interface for kinesis service Paginators"
from __future__ import annotations

from datetime import datetime
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kinesis.type_defs import (
    DescribeStreamPaginatePaginationConfigTypeDef,
    DescribeStreamPaginateResponseTypeDef,
    ListShardsPaginatePaginationConfigTypeDef,
    ListShardsPaginateResponseTypeDef,
    ListStreamConsumersPaginatePaginationConfigTypeDef,
    ListStreamConsumersPaginateResponseTypeDef,
    ListStreamsPaginatePaginationConfigTypeDef,
    ListStreamsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeStreamPaginator",
    "ListShardsPaginator",
    "ListStreamConsumersPaginator",
    "ListStreamsPaginator",
)


class DescribeStreamPaginator(Boto3Paginator):
    """
    Paginator for `describe_stream`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StreamName: str,
        PaginationConfig: DescribeStreamPaginatePaginationConfigTypeDef = None,
    ) -> DescribeStreamPaginateResponseTypeDef:
        """
        [DescribeStream.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream.paginate)
        """


class ListShardsPaginator(Boto3Paginator):
    """
    Paginator for `list_shards`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StreamName: str = None,
        ExclusiveStartShardId: str = None,
        StreamCreationTimestamp: datetime = None,
        PaginationConfig: ListShardsPaginatePaginationConfigTypeDef = None,
    ) -> ListShardsPaginateResponseTypeDef:
        """
        [ListShards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kinesis.html#Kinesis.Paginator.ListShards.paginate)
        """


class ListStreamConsumersPaginator(Boto3Paginator):
    """
    Paginator for `list_stream_consumers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StreamARN: str,
        StreamCreationTimestamp: datetime = None,
        PaginationConfig: ListStreamConsumersPaginatePaginationConfigTypeDef = None,
    ) -> ListStreamConsumersPaginateResponseTypeDef:
        """
        [ListStreamConsumers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    Paginator for `list_streams`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListStreamsPaginatePaginationConfigTypeDef = None
    ) -> ListStreamsPaginateResponseTypeDef:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kinesis.html#Kinesis.Paginator.ListStreams.paginate)
        """
