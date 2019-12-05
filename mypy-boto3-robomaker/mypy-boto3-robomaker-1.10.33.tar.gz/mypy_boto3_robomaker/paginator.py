"Main interface for robomaker service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_robomaker.type_defs import (
    ListDeploymentJobsPaginateFiltersTypeDef,
    ListDeploymentJobsPaginatePaginationConfigTypeDef,
    ListDeploymentJobsPaginateResponseTypeDef,
    ListFleetsPaginateFiltersTypeDef,
    ListFleetsPaginatePaginationConfigTypeDef,
    ListFleetsPaginateResponseTypeDef,
    ListRobotApplicationsPaginateFiltersTypeDef,
    ListRobotApplicationsPaginatePaginationConfigTypeDef,
    ListRobotApplicationsPaginateResponseTypeDef,
    ListRobotsPaginateFiltersTypeDef,
    ListRobotsPaginatePaginationConfigTypeDef,
    ListRobotsPaginateResponseTypeDef,
    ListSimulationApplicationsPaginateFiltersTypeDef,
    ListSimulationApplicationsPaginatePaginationConfigTypeDef,
    ListSimulationApplicationsPaginateResponseTypeDef,
    ListSimulationJobsPaginateFiltersTypeDef,
    ListSimulationJobsPaginatePaginationConfigTypeDef,
    ListSimulationJobsPaginateResponseTypeDef,
)


__all__ = (
    "ListDeploymentJobsPaginator",
    "ListFleetsPaginator",
    "ListRobotApplicationsPaginator",
    "ListRobotsPaginator",
    "ListSimulationApplicationsPaginator",
    "ListSimulationJobsPaginator",
)


class ListDeploymentJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[ListDeploymentJobsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListDeploymentJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentJobsPaginateResponseTypeDef:
        """
        [ListDeploymentJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs.paginate)
        """


class ListFleetsPaginator(Boto3Paginator):
    """
    Paginator for `list_fleets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[ListFleetsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListFleetsPaginatePaginationConfigTypeDef = None,
    ) -> ListFleetsPaginateResponseTypeDef:
        """
        [ListFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets.paginate)
        """


class ListRobotApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_robot_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        versionQualifier: str = None,
        filters: List[ListRobotApplicationsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListRobotApplicationsPaginatePaginationConfigTypeDef = None,
    ) -> ListRobotApplicationsPaginateResponseTypeDef:
        """
        [ListRobotApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications.paginate)
        """


class ListRobotsPaginator(Boto3Paginator):
    """
    Paginator for `list_robots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[ListRobotsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListRobotsPaginatePaginationConfigTypeDef = None,
    ) -> ListRobotsPaginateResponseTypeDef:
        """
        [ListRobots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots.paginate)
        """


class ListSimulationApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_simulation_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        versionQualifier: str = None,
        filters: List[ListSimulationApplicationsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListSimulationApplicationsPaginatePaginationConfigTypeDef = None,
    ) -> ListSimulationApplicationsPaginateResponseTypeDef:
        """
        [ListSimulationApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications.paginate)
        """


class ListSimulationJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_simulation_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[ListSimulationJobsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListSimulationJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListSimulationJobsPaginateResponseTypeDef:
        """
        [ListSimulationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs.paginate)
        """
