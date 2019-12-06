"Main interface for budgets service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_budgets.type_defs import (
    DescribeBudgetsPaginatePaginationConfigTypeDef,
    DescribeBudgetsPaginateResponseTypeDef,
    DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef,
    DescribeNotificationsForBudgetPaginateResponseTypeDef,
    DescribeSubscribersForNotificationPaginateNotificationTypeDef,
    DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef,
    DescribeSubscribersForNotificationPaginateResponseTypeDef,
)


__all__ = (
    "DescribeBudgetsPaginator",
    "DescribeNotificationsForBudgetPaginator",
    "DescribeSubscribersForNotificationPaginator",
)


class DescribeBudgetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_budgets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AccountId: str,
        PaginationConfig: DescribeBudgetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeBudgetsPaginateResponseTypeDef:
        """
        [DescribeBudgets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets.paginate)
        """


class DescribeNotificationsForBudgetPaginator(Boto3Paginator):
    """
    Paginator for `describe_notifications_for_budget`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        PaginationConfig: DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef = None,
    ) -> DescribeNotificationsForBudgetPaginateResponseTypeDef:
        """
        [DescribeNotificationsForBudget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget.paginate)
        """


class DescribeSubscribersForNotificationPaginator(Boto3Paginator):
    """
    Paginator for `describe_subscribers_for_notification`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: DescribeSubscribersForNotificationPaginateNotificationTypeDef,
        PaginationConfig: DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSubscribersForNotificationPaginateResponseTypeDef:
        """
        [DescribeSubscribersForNotification.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification.paginate)
        """
