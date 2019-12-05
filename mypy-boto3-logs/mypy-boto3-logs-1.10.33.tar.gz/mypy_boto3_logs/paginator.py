"Main interface for logs service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_logs.type_defs import (
    DescribeDestinationsPaginatePaginationConfigTypeDef,
    DescribeDestinationsPaginateResponseTypeDef,
    DescribeExportTasksPaginatePaginationConfigTypeDef,
    DescribeExportTasksPaginateResponseTypeDef,
    DescribeLogGroupsPaginatePaginationConfigTypeDef,
    DescribeLogGroupsPaginateResponseTypeDef,
    DescribeLogStreamsPaginatePaginationConfigTypeDef,
    DescribeLogStreamsPaginateResponseTypeDef,
    DescribeMetricFiltersPaginatePaginationConfigTypeDef,
    DescribeMetricFiltersPaginateResponseTypeDef,
    DescribeQueriesPaginatePaginationConfigTypeDef,
    DescribeQueriesPaginateResponseTypeDef,
    DescribeResourcePoliciesPaginatePaginationConfigTypeDef,
    DescribeResourcePoliciesPaginateResponseTypeDef,
    DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef,
    DescribeSubscriptionFiltersPaginateResponseTypeDef,
    FilterLogEventsPaginatePaginationConfigTypeDef,
    FilterLogEventsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDestinationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeLogGroupsPaginator",
    "DescribeLogStreamsPaginator",
    "DescribeMetricFiltersPaginator",
    "DescribeQueriesPaginator",
    "DescribeResourcePoliciesPaginator",
    "DescribeSubscriptionFiltersPaginator",
    "FilterLogEventsPaginator",
)


class DescribeDestinationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_destinations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DestinationNamePrefix: str = None,
        PaginationConfig: DescribeDestinationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDestinationsPaginateResponseTypeDef:
        """
        [DescribeDestinations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations.paginate)
        """


class DescribeExportTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_export_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        taskId: str = None,
        statusCode: Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ] = None,
        PaginationConfig: DescribeExportTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeExportTasksPaginateResponseTypeDef:
        """
        [DescribeExportTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks.paginate)
        """


class DescribeLogGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_log_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupNamePrefix: str = None,
        PaginationConfig: DescribeLogGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLogGroupsPaginateResponseTypeDef:
        """
        [DescribeLogGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups.paginate)
        """


class DescribeLogStreamsPaginator(Boto3Paginator):
    """
    Paginator for `describe_log_streams`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: Literal["LogStreamName", "LastEventTime"] = None,
        descending: bool = None,
        PaginationConfig: DescribeLogStreamsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLogStreamsPaginateResponseTypeDef:
        """
        [DescribeLogStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams.paginate)
        """


class DescribeMetricFiltersPaginator(Boto3Paginator):
    """
    Paginator for `describe_metric_filters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        metricName: str = None,
        metricNamespace: str = None,
        PaginationConfig: DescribeMetricFiltersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMetricFiltersPaginateResponseTypeDef:
        """
        [DescribeMetricFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters.paginate)
        """


class DescribeQueriesPaginator(Boto3Paginator):
    """
    Paginator for `describe_queries`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str = None,
        status: Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"] = None,
        PaginationConfig: DescribeQueriesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeQueriesPaginateResponseTypeDef:
        """
        [DescribeQueries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries.paginate)
        """


class DescribeResourcePoliciesPaginator(Boto3Paginator):
    """
    Paginator for `describe_resource_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeResourcePoliciesPaginatePaginationConfigTypeDef = None
    ) -> DescribeResourcePoliciesPaginateResponseTypeDef:
        """
        [DescribeResourcePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies.paginate)
        """


class DescribeSubscriptionFiltersPaginator(Boto3Paginator):
    """
    Paginator for `describe_subscription_filters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        PaginationConfig: DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSubscriptionFiltersPaginateResponseTypeDef:
        """
        [DescribeSubscriptionFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters.paginate)
        """


class FilterLogEventsPaginator(Boto3Paginator):
    """
    Paginator for `filter_log_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        interleaved: bool = None,
        PaginationConfig: FilterLogEventsPaginatePaginationConfigTypeDef = None,
    ) -> FilterLogEventsPaginateResponseTypeDef:
        """
        [FilterLogEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents.paginate)
        """
