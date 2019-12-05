"Main interface for mediastore-data service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediastore_data.type_defs import (
    ListItemsPaginatePaginationConfigTypeDef,
    ListItemsPaginateResponseTypeDef,
)


__all__ = ("ListItemsPaginator",)


class ListItemsPaginator(Boto3Paginator):
    """
    Paginator for `list_items`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Path: str = None, PaginationConfig: ListItemsPaginatePaginationConfigTypeDef = None
    ) -> ListItemsPaginateResponseTypeDef:
        """
        [ListItems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems.paginate)
        """
