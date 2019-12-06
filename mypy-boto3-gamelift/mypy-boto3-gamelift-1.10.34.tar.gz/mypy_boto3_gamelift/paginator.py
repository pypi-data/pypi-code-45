"Main interface for gamelift service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_gamelift.type_defs import (
    DescribeFleetAttributesPaginatePaginationConfigTypeDef,
    DescribeFleetAttributesPaginateResponseTypeDef,
    DescribeFleetCapacityPaginatePaginationConfigTypeDef,
    DescribeFleetCapacityPaginateResponseTypeDef,
    DescribeFleetEventsPaginatePaginationConfigTypeDef,
    DescribeFleetEventsPaginateResponseTypeDef,
    DescribeFleetUtilizationPaginatePaginationConfigTypeDef,
    DescribeFleetUtilizationPaginateResponseTypeDef,
    DescribeGameSessionDetailsPaginatePaginationConfigTypeDef,
    DescribeGameSessionDetailsPaginateResponseTypeDef,
    DescribeGameSessionQueuesPaginatePaginationConfigTypeDef,
    DescribeGameSessionQueuesPaginateResponseTypeDef,
    DescribeGameSessionsPaginatePaginationConfigTypeDef,
    DescribeGameSessionsPaginateResponseTypeDef,
    DescribeInstancesPaginatePaginationConfigTypeDef,
    DescribeInstancesPaginateResponseTypeDef,
    DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef,
    DescribeMatchmakingConfigurationsPaginateResponseTypeDef,
    DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef,
    DescribeMatchmakingRuleSetsPaginateResponseTypeDef,
    DescribePlayerSessionsPaginatePaginationConfigTypeDef,
    DescribePlayerSessionsPaginateResponseTypeDef,
    DescribeScalingPoliciesPaginatePaginationConfigTypeDef,
    DescribeScalingPoliciesPaginateResponseTypeDef,
    ListAliasesPaginatePaginationConfigTypeDef,
    ListAliasesPaginateResponseTypeDef,
    ListBuildsPaginatePaginationConfigTypeDef,
    ListBuildsPaginateResponseTypeDef,
    ListFleetsPaginatePaginationConfigTypeDef,
    ListFleetsPaginateResponseTypeDef,
    SearchGameSessionsPaginatePaginationConfigTypeDef,
    SearchGameSessionsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeFleetAttributesPaginator",
    "DescribeFleetCapacityPaginator",
    "DescribeFleetEventsPaginator",
    "DescribeFleetUtilizationPaginator",
    "DescribeGameSessionDetailsPaginator",
    "DescribeGameSessionQueuesPaginator",
    "DescribeGameSessionsPaginator",
    "DescribeInstancesPaginator",
    "DescribeMatchmakingConfigurationsPaginator",
    "DescribeMatchmakingRuleSetsPaginator",
    "DescribePlayerSessionsPaginator",
    "DescribeScalingPoliciesPaginator",
    "ListAliasesPaginator",
    "ListBuildsPaginator",
    "ListFleetsPaginator",
    "SearchGameSessionsPaginator",
)


class DescribeFleetAttributesPaginator(Boto3Paginator):
    """
    Paginator for `describe_fleet_attributes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetIds: List[str] = None,
        PaginationConfig: DescribeFleetAttributesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFleetAttributesPaginateResponseTypeDef:
        """
        [DescribeFleetAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetAttributes.paginate)
        """


class DescribeFleetCapacityPaginator(Boto3Paginator):
    """
    Paginator for `describe_fleet_capacity`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetIds: List[str] = None,
        PaginationConfig: DescribeFleetCapacityPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFleetCapacityPaginateResponseTypeDef:
        """
        [DescribeFleetCapacity.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetCapacity.paginate)
        """


class DescribeFleetEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_fleet_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: DescribeFleetEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFleetEventsPaginateResponseTypeDef:
        """
        [DescribeFleetEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetEvents.paginate)
        """


class DescribeFleetUtilizationPaginator(Boto3Paginator):
    """
    Paginator for `describe_fleet_utilization`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetIds: List[str] = None,
        PaginationConfig: DescribeFleetUtilizationPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFleetUtilizationPaginateResponseTypeDef:
        """
        [DescribeFleetUtilization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetUtilization.paginate)
        """


class DescribeGameSessionDetailsPaginator(Boto3Paginator):
    """
    Paginator for `describe_game_session_details`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        PaginationConfig: DescribeGameSessionDetailsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeGameSessionDetailsPaginateResponseTypeDef:
        """
        [DescribeGameSessionDetails.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionDetails.paginate)
        """


class DescribeGameSessionQueuesPaginator(Boto3Paginator):
    """
    Paginator for `describe_game_session_queues`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: DescribeGameSessionQueuesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeGameSessionQueuesPaginateResponseTypeDef:
        """
        [DescribeGameSessionQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionQueues.paginate)
        """


class DescribeGameSessionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_game_sessions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        PaginationConfig: DescribeGameSessionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeGameSessionsPaginateResponseTypeDef:
        """
        [DescribeGameSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessions.paginate)
        """


class DescribeInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str,
        InstanceId: str = None,
        PaginationConfig: DescribeInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstancesPaginateResponseTypeDef:
        """
        [DescribeInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeInstances.paginate)
        """


class DescribeMatchmakingConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_matchmaking_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        RuleSetName: str = None,
        PaginationConfig: DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMatchmakingConfigurationsPaginateResponseTypeDef:
        """
        [DescribeMatchmakingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingConfigurations.paginate)
        """


class DescribeMatchmakingRuleSetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_matchmaking_rule_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMatchmakingRuleSetsPaginateResponseTypeDef:
        """
        [DescribeMatchmakingRuleSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingRuleSets.paginate)
        """


class DescribePlayerSessionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_player_sessions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GameSessionId: str = None,
        PlayerId: str = None,
        PlayerSessionId: str = None,
        PlayerSessionStatusFilter: str = None,
        PaginationConfig: DescribePlayerSessionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePlayerSessionsPaginateResponseTypeDef:
        """
        [DescribePlayerSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribePlayerSessions.paginate)
        """


class DescribeScalingPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `describe_scaling_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str,
        StatusFilter: Literal[
            "ACTIVE",
            "UPDATE_REQUESTED",
            "UPDATING",
            "DELETE_REQUESTED",
            "DELETING",
            "DELETED",
            "ERROR",
        ] = None,
        PaginationConfig: DescribeScalingPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeScalingPoliciesPaginateResponseTypeDef:
        """
        [DescribeScalingPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.DescribeScalingPolicies.paginate)
        """


class ListAliasesPaginator(Boto3Paginator):
    """
    Paginator for `list_aliases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RoutingStrategyType: Literal["SIMPLE", "TERMINAL"] = None,
        Name: str = None,
        PaginationConfig: ListAliasesPaginatePaginationConfigTypeDef = None,
    ) -> ListAliasesPaginateResponseTypeDef:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.ListAliases.paginate)
        """


class ListBuildsPaginator(Boto3Paginator):
    """
    Paginator for `list_builds`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Status: Literal["INITIALIZED", "READY", "FAILED"] = None,
        PaginationConfig: ListBuildsPaginatePaginationConfigTypeDef = None,
    ) -> ListBuildsPaginateResponseTypeDef:
        """
        [ListBuilds.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.ListBuilds.paginate)
        """


class ListFleetsPaginator(Boto3Paginator):
    """
    Paginator for `list_fleets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BuildId: str = None,
        ScriptId: str = None,
        PaginationConfig: ListFleetsPaginatePaginationConfigTypeDef = None,
    ) -> ListFleetsPaginateResponseTypeDef:
        """
        [ListFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.ListFleets.paginate)
        """


class SearchGameSessionsPaginator(Boto3Paginator):
    """
    Paginator for `search_game_sessions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str = None,
        AliasId: str = None,
        FilterExpression: str = None,
        SortExpression: str = None,
        PaginationConfig: SearchGameSessionsPaginatePaginationConfigTypeDef = None,
    ) -> SearchGameSessionsPaginateResponseTypeDef:
        """
        [SearchGameSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/gamelift.html#GameLift.Paginator.SearchGameSessions.paginate)
        """
