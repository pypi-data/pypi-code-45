"Main interface for groundstation service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_groundstation.type_defs import (
    ListConfigsPaginatePaginationConfigTypeDef,
    ListConfigsPaginateResponseTypeDef,
    ListContactsPaginatePaginationConfigTypeDef,
    ListContactsPaginateResponseTypeDef,
    ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef,
    ListDataflowEndpointGroupsPaginateResponseTypeDef,
    ListGroundStationsPaginatePaginationConfigTypeDef,
    ListGroundStationsPaginateResponseTypeDef,
    ListMissionProfilesPaginatePaginationConfigTypeDef,
    ListMissionProfilesPaginateResponseTypeDef,
    ListSatellitesPaginatePaginationConfigTypeDef,
    ListSatellitesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListConfigsPaginator",
    "ListContactsPaginator",
    "ListDataflowEndpointGroupsPaginator",
    "ListGroundStationsPaginator",
    "ListMissionProfilesPaginator",
    "ListSatellitesPaginator",
)


class ListConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConfigsPaginatePaginationConfigTypeDef = None
    ) -> ListConfigsPaginateResponseTypeDef:
        """
        [ListConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs.paginate)
        """


class ListContactsPaginator(Boto3Paginator):
    """
    Paginator for `list_contacts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[
            Literal[
                "AVAILABLE",
                "AWS_CANCELLED",
                "CANCELLED",
                "COMPLETED",
                "FAILED",
                "FAILED_TO_SCHEDULE",
                "PASS",
                "POSTPASS",
                "PREPASS",
                "SCHEDULED",
                "SCHEDULING",
            ]
        ],
        groundStation: str = None,
        missionProfileArn: str = None,
        satelliteArn: str = None,
        PaginationConfig: ListContactsPaginatePaginationConfigTypeDef = None,
    ) -> ListContactsPaginateResponseTypeDef:
        """
        [ListContacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListContacts.paginate)
        """


class ListDataflowEndpointGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_dataflow_endpoint_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListDataflowEndpointGroupsPaginateResponseTypeDef:
        """
        [ListDataflowEndpointGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups.paginate)
        """


class ListGroundStationsPaginator(Boto3Paginator):
    """
    Paginator for `list_ground_stations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGroundStationsPaginatePaginationConfigTypeDef = None
    ) -> ListGroundStationsPaginateResponseTypeDef:
        """
        [ListGroundStations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations.paginate)
        """


class ListMissionProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_mission_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListMissionProfilesPaginatePaginationConfigTypeDef = None
    ) -> ListMissionProfilesPaginateResponseTypeDef:
        """
        [ListMissionProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles.paginate)
        """


class ListSatellitesPaginator(Boto3Paginator):
    """
    Paginator for `list_satellites`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSatellitesPaginatePaginationConfigTypeDef = None
    ) -> ListSatellitesPaginateResponseTypeDef:
        """
        [ListSatellites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites.paginate)
        """
