"Main interface for translate service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_translate.type_defs import (
    ListTerminologiesPaginatePaginationConfigTypeDef,
    ListTerminologiesPaginateResponseTypeDef,
)


__all__ = ("ListTerminologiesPaginator",)


class ListTerminologiesPaginator(Boto3Paginator):
    """
    Paginator for `list_terminologies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListTerminologiesPaginatePaginationConfigTypeDef = None
    ) -> ListTerminologiesPaginateResponseTypeDef:
        """
        [ListTerminologies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/translate.html#Translate.Paginator.ListTerminologies.paginate)
        """
