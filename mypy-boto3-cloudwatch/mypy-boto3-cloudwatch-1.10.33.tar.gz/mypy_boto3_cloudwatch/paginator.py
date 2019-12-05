"Main interface for cloudwatch service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudwatch.type_defs import (
    DescribeAlarmHistoryPaginatePaginationConfigTypeDef,
    DescribeAlarmHistoryPaginateResponseTypeDef,
    DescribeAlarmsPaginatePaginationConfigTypeDef,
    DescribeAlarmsPaginateResponseTypeDef,
    GetMetricDataPaginateMetricDataQueriesTypeDef,
    GetMetricDataPaginatePaginationConfigTypeDef,
    GetMetricDataPaginateResponseTypeDef,
    ListDashboardsPaginatePaginationConfigTypeDef,
    ListDashboardsPaginateResponseTypeDef,
    ListMetricsPaginateDimensionsTypeDef,
    ListMetricsPaginatePaginationConfigTypeDef,
    ListMetricsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAlarmHistoryPaginator",
    "DescribeAlarmsPaginator",
    "GetMetricDataPaginator",
    "ListDashboardsPaginator",
    "ListMetricsPaginator",
)


class DescribeAlarmHistoryPaginator(Boto3Paginator):
    """
    Paginator for `describe_alarm_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AlarmName: str = None,
        HistoryItemType: Literal["ConfigurationUpdate", "StateUpdate", "Action"] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        PaginationConfig: DescribeAlarmHistoryPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAlarmHistoryPaginateResponseTypeDef:
        """
        [DescribeAlarmHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarmHistory.paginate)
        """


class DescribeAlarmsPaginator(Boto3Paginator):
    """
    Paginator for `describe_alarms`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"] = None,
        ActionPrefix: str = None,
        PaginationConfig: DescribeAlarmsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAlarmsPaginateResponseTypeDef:
        """
        [DescribeAlarms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarms.paginate)
        """


class GetMetricDataPaginator(Boto3Paginator):
    """
    Paginator for `get_metric_data`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MetricDataQueries: List[GetMetricDataPaginateMetricDataQueriesTypeDef],
        StartTime: datetime,
        EndTime: datetime,
        ScanBy: Literal["TimestampDescending", "TimestampAscending"] = None,
        PaginationConfig: GetMetricDataPaginatePaginationConfigTypeDef = None,
    ) -> GetMetricDataPaginateResponseTypeDef:
        """
        [GetMetricData.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudwatch.html#CloudWatch.Paginator.GetMetricData.paginate)
        """


class ListDashboardsPaginator(Boto3Paginator):
    """
    Paginator for `list_dashboards`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DashboardNamePrefix: str = None,
        PaginationConfig: ListDashboardsPaginatePaginationConfigTypeDef = None,
    ) -> ListDashboardsPaginateResponseTypeDef:
        """
        [ListDashboards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudwatch.html#CloudWatch.Paginator.ListDashboards.paginate)
        """


class ListMetricsPaginator(Boto3Paginator):
    """
    Paginator for `list_metrics`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[ListMetricsPaginateDimensionsTypeDef] = None,
        PaginationConfig: ListMetricsPaginatePaginationConfigTypeDef = None,
    ) -> ListMetricsPaginateResponseTypeDef:
        """
        [ListMetrics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudwatch.html#CloudWatch.Paginator.ListMetrics.paginate)
        """
