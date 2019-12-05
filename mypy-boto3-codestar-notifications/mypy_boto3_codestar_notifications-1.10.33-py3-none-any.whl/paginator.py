"Main interface for codestar-notifications service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codestar_notifications.type_defs import (
    ListEventTypesPaginateFiltersTypeDef,
    ListEventTypesPaginatePaginationConfigTypeDef,
    ListEventTypesPaginateResponseTypeDef,
    ListNotificationRulesPaginateFiltersTypeDef,
    ListNotificationRulesPaginatePaginationConfigTypeDef,
    ListNotificationRulesPaginateResponseTypeDef,
    ListTargetsPaginateFiltersTypeDef,
    ListTargetsPaginatePaginationConfigTypeDef,
    ListTargetsPaginateResponseTypeDef,
)


__all__ = ("ListEventTypesPaginator", "ListNotificationRulesPaginator", "ListTargetsPaginator")


class ListEventTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_event_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListEventTypesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListEventTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListEventTypesPaginateResponseTypeDef:
        """
        [ListEventTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListEventTypes.paginate)
        """


class ListNotificationRulesPaginator(Boto3Paginator):
    """
    Paginator for `list_notification_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListNotificationRulesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListNotificationRulesPaginatePaginationConfigTypeDef = None,
    ) -> ListNotificationRulesPaginateResponseTypeDef:
        """
        [ListNotificationRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListNotificationRules.paginate)
        """


class ListTargetsPaginator(Boto3Paginator):
    """
    Paginator for `list_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListTargetsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListTargetsPaginatePaginationConfigTypeDef = None,
    ) -> ListTargetsPaginateResponseTypeDef:
        """
        [ListTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListTargets.paginate)
        """
