"Main interface for codestar-notifications service"

from mypy_boto3_codestar_notifications.client import Client
from mypy_boto3_codestar_notifications.paginator import (
    ListEventTypesPaginator,
    ListNotificationRulesPaginator,
    ListTargetsPaginator,
)


__all__ = (
    "Client",
    "ListEventTypesPaginator",
    "ListNotificationRulesPaginator",
    "ListTargetsPaginator",
)
