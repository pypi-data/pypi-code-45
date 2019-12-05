"Main interface for mediatailor service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediatailor.type_defs import (
    ListPlaybackConfigurationsPaginatePaginationConfigTypeDef,
    ListPlaybackConfigurationsPaginateResponseTypeDef,
)


__all__ = ("ListPlaybackConfigurationsPaginator",)


class ListPlaybackConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_playback_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPlaybackConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> ListPlaybackConfigurationsPaginateResponseTypeDef:
        """
        [ListPlaybackConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations.paginate)
        """
