"Main interface for cloudwatch service"

from mypy_boto3_cloudwatch.client import Client
from mypy_boto3_cloudwatch.paginator import (
    DescribeAlarmHistoryPaginator,
    DescribeAlarmsPaginator,
    GetMetricDataPaginator,
    ListDashboardsPaginator,
    ListMetricsPaginator,
)
from mypy_boto3_cloudwatch.service_resource import ServiceResource
from mypy_boto3_cloudwatch.waiter import AlarmExistsWaiter


__all__ = (
    "Client",
    "ServiceResource",
    "AlarmExistsWaiter",
    "DescribeAlarmHistoryPaginator",
    "DescribeAlarmsPaginator",
    "GetMetricDataPaginator",
    "ListDashboardsPaginator",
    "ListMetricsPaginator",
)
