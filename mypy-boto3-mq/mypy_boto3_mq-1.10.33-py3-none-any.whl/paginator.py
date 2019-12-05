"Main interface for mq service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mq.type_defs import (
    ListBrokersPaginatePaginationConfigTypeDef,
    ListBrokersPaginateResponseTypeDef,
)


__all__ = ("ListBrokersPaginator",)


class ListBrokersPaginator(Boto3Paginator):
    """
    Paginator for `list_brokers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListBrokersPaginatePaginationConfigTypeDef = None
    ) -> ListBrokersPaginateResponseTypeDef:
        """
        [ListBrokers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mq.html#MQ.Paginator.ListBrokers.paginate)
        """
