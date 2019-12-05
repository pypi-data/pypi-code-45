"Main interface for medialive service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_medialive.type_defs import (
    DescribeSchedulePaginatePaginationConfigTypeDef,
    DescribeSchedulePaginateResponseTypeDef,
    ListChannelsPaginatePaginationConfigTypeDef,
    ListChannelsPaginateResponseTypeDef,
    ListInputSecurityGroupsPaginatePaginationConfigTypeDef,
    ListInputSecurityGroupsPaginateResponseTypeDef,
    ListInputsPaginatePaginationConfigTypeDef,
    ListInputsPaginateResponseTypeDef,
    ListMultiplexProgramsPaginatePaginationConfigTypeDef,
    ListMultiplexProgramsPaginateResponseTypeDef,
    ListMultiplexesPaginatePaginationConfigTypeDef,
    ListMultiplexesPaginateResponseTypeDef,
    ListOfferingsPaginatePaginationConfigTypeDef,
    ListOfferingsPaginateResponseTypeDef,
    ListReservationsPaginatePaginationConfigTypeDef,
    ListReservationsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeSchedulePaginator",
    "ListChannelsPaginator",
    "ListInputSecurityGroupsPaginator",
    "ListInputsPaginator",
    "ListMultiplexProgramsPaginator",
    "ListMultiplexesPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
)


class DescribeSchedulePaginator(Boto3Paginator):
    """
    Paginator for `describe_schedule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChannelId: str,
        PaginationConfig: DescribeSchedulePaginatePaginationConfigTypeDef = None,
    ) -> DescribeSchedulePaginateResponseTypeDef:
        """
        [DescribeSchedule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule.paginate)
        """


class ListChannelsPaginator(Boto3Paginator):
    """
    Paginator for `list_channels`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListChannelsPaginatePaginationConfigTypeDef = None
    ) -> ListChannelsPaginateResponseTypeDef:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Paginator.ListChannels.paginate)
        """


class ListInputSecurityGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_input_security_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListInputSecurityGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListInputSecurityGroupsPaginateResponseTypeDef:
        """
        [ListInputSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups.paginate)
        """


class ListInputsPaginator(Boto3Paginator):
    """
    Paginator for `list_inputs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListInputsPaginatePaginationConfigTypeDef = None
    ) -> ListInputsPaginateResponseTypeDef:
        """
        [ListInputs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Paginator.ListInputs.paginate)
        """


class ListMultiplexProgramsPaginator(Boto3Paginator):
    """
    Paginator for `list_multiplex_programs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MultiplexId: str,
        PaginationConfig: ListMultiplexProgramsPaginatePaginationConfigTypeDef = None,
    ) -> ListMultiplexProgramsPaginateResponseTypeDef:
        """
        [ListMultiplexPrograms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms.paginate)
        """


class ListMultiplexesPaginator(Boto3Paginator):
    """
    Paginator for `list_multiplexes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListMultiplexesPaginatePaginationConfigTypeDef = None
    ) -> ListMultiplexesPaginateResponseTypeDef:
        """
        [ListMultiplexes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes.paginate)
        """


class ListOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `list_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChannelClass: str = None,
        ChannelConfiguration: str = None,
        Codec: str = None,
        Duration: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: ListOfferingsPaginatePaginationConfigTypeDef = None,
    ) -> ListOfferingsPaginateResponseTypeDef:
        """
        [ListOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Paginator.ListOfferings.paginate)
        """


class ListReservationsPaginator(Boto3Paginator):
    """
    Paginator for `list_reservations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChannelClass: str = None,
        Codec: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: ListReservationsPaginatePaginationConfigTypeDef = None,
    ) -> ListReservationsPaginateResponseTypeDef:
        """
        [ListReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/medialive.html#MediaLive.Paginator.ListReservations.paginate)
        """
