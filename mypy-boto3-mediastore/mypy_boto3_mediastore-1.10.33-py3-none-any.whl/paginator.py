"Main interface for mediastore service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediastore.type_defs import (
    ListContainersPaginatePaginationConfigTypeDef,
    ListContainersPaginateResponseTypeDef,
)


__all__ = ("ListContainersPaginator",)


class ListContainersPaginator(Boto3Paginator):
    """
    Paginator for `list_containers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListContainersPaginatePaginationConfigTypeDef = None
    ) -> ListContainersPaginateResponseTypeDef:
        """
        [ListContainers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediastore.html#MediaStore.Paginator.ListContainers.paginate)
        """
