"Main interface for kinesis-video-archived-media service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kinesis_video_archived_media.type_defs import (
    ListFragmentsPaginateFragmentSelectorTypeDef,
    ListFragmentsPaginatePaginationConfigTypeDef,
    ListFragmentsPaginateResponseTypeDef,
)


__all__ = ("ListFragmentsPaginator",)


class ListFragmentsPaginator(Boto3Paginator):
    """
    Paginator for `list_fragments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StreamName: str,
        FragmentSelector: ListFragmentsPaginateFragmentSelectorTypeDef = None,
        PaginationConfig: ListFragmentsPaginatePaginationConfigTypeDef = None,
    ) -> ListFragmentsPaginateResponseTypeDef:
        """
        [ListFragments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments.paginate)
        """
