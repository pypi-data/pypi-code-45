"Main interface for transfer service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_transfer.type_defs import (
    ListServersPaginatePaginationConfigTypeDef,
    ListServersPaginateResponseTypeDef,
)


__all__ = ("ListServersPaginator",)


class ListServersPaginator(Boto3Paginator):
    """
    Paginator for `list_servers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListServersPaginatePaginationConfigTypeDef = None
    ) -> ListServersPaginateResponseTypeDef:
        """
        [ListServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/transfer.html#Transfer.Paginator.ListServers.paginate)
        """
