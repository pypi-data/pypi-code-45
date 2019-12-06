"Main interface for budgets service"

from mypy_boto3_budgets.client import Client
from mypy_boto3_budgets.paginator import (
    DescribeBudgetsPaginator,
    DescribeNotificationsForBudgetPaginator,
    DescribeSubscribersForNotificationPaginator,
)


__all__ = (
    "Client",
    "DescribeBudgetsPaginator",
    "DescribeNotificationsForBudgetPaginator",
    "DescribeSubscribersForNotificationPaginator",
)
