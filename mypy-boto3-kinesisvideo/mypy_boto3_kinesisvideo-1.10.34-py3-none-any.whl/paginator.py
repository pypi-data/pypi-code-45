"Main interface for kinesisvideo service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kinesisvideo.type_defs import (
    ListSignalingChannelsPaginateChannelNameConditionTypeDef,
    ListSignalingChannelsPaginatePaginationConfigTypeDef,
    ListSignalingChannelsPaginateResponseTypeDef,
    ListStreamsPaginatePaginationConfigTypeDef,
    ListStreamsPaginateResponseTypeDef,
    ListStreamsPaginateStreamNameConditionTypeDef,
)


__all__ = ("ListSignalingChannelsPaginator", "ListStreamsPaginator")


class ListSignalingChannelsPaginator(Boto3Paginator):
    """
    Paginator for `list_signaling_channels`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChannelNameCondition: ListSignalingChannelsPaginateChannelNameConditionTypeDef = None,
        PaginationConfig: ListSignalingChannelsPaginatePaginationConfigTypeDef = None,
    ) -> ListSignalingChannelsPaginateResponseTypeDef:
        """
        [ListSignalingChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    Paginator for `list_streams`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StreamNameCondition: ListStreamsPaginateStreamNameConditionTypeDef = None,
        PaginationConfig: ListStreamsPaginatePaginationConfigTypeDef = None,
    ) -> ListStreamsPaginateResponseTypeDef:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams.paginate)
        """
