"Main interface for xray service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_xray.type_defs import (
    BatchGetTracesPaginatePaginationConfigTypeDef,
    BatchGetTracesPaginateResponseTypeDef,
    GetGroupsPaginatePaginationConfigTypeDef,
    GetGroupsPaginateResponseTypeDef,
    GetSamplingRulesPaginatePaginationConfigTypeDef,
    GetSamplingRulesPaginateResponseTypeDef,
    GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef,
    GetSamplingStatisticSummariesPaginateResponseTypeDef,
    GetServiceGraphPaginatePaginationConfigTypeDef,
    GetServiceGraphPaginateResponseTypeDef,
    GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef,
    GetTimeSeriesServiceStatisticsPaginateResponseTypeDef,
    GetTraceGraphPaginatePaginationConfigTypeDef,
    GetTraceGraphPaginateResponseTypeDef,
    GetTraceSummariesPaginatePaginationConfigTypeDef,
    GetTraceSummariesPaginateResponseTypeDef,
    GetTraceSummariesPaginateSamplingStrategyTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatchGetTracesPaginator",
    "GetGroupsPaginator",
    "GetSamplingRulesPaginator",
    "GetSamplingStatisticSummariesPaginator",
    "GetServiceGraphPaginator",
    "GetTimeSeriesServiceStatisticsPaginator",
    "GetTraceGraphPaginator",
    "GetTraceSummariesPaginator",
)


class BatchGetTracesPaginator(Boto3Paginator):
    """
    Paginator for `batch_get_traces`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TraceIds: List[str],
        PaginationConfig: BatchGetTracesPaginatePaginationConfigTypeDef = None,
    ) -> BatchGetTracesPaginateResponseTypeDef:
        """
        [BatchGetTraces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.BatchGetTraces.paginate)
        """


class GetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `get_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetGroupsPaginatePaginationConfigTypeDef = None
    ) -> GetGroupsPaginateResponseTypeDef:
        """
        [GetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetGroups.paginate)
        """


class GetSamplingRulesPaginator(Boto3Paginator):
    """
    Paginator for `get_sampling_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetSamplingRulesPaginatePaginationConfigTypeDef = None
    ) -> GetSamplingRulesPaginateResponseTypeDef:
        """
        [GetSamplingRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetSamplingRules.paginate)
        """


class GetSamplingStatisticSummariesPaginator(Boto3Paginator):
    """
    Paginator for `get_sampling_statistic_summaries`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef = None
    ) -> GetSamplingStatisticSummariesPaginateResponseTypeDef:
        """
        [GetSamplingStatisticSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries.paginate)
        """


class GetServiceGraphPaginator(Boto3Paginator):
    """
    Paginator for `get_service_graph`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        PaginationConfig: GetServiceGraphPaginatePaginationConfigTypeDef = None,
    ) -> GetServiceGraphPaginateResponseTypeDef:
        """
        [GetServiceGraph.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetServiceGraph.paginate)
        """


class GetTimeSeriesServiceStatisticsPaginator(Boto3Paginator):
    """
    Paginator for `get_time_series_service_statistics`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        PaginationConfig: GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef = None,
    ) -> GetTimeSeriesServiceStatisticsPaginateResponseTypeDef:
        """
        [GetTimeSeriesServiceStatistics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics.paginate)
        """


class GetTraceGraphPaginator(Boto3Paginator):
    """
    Paginator for `get_trace_graph`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TraceIds: List[str],
        PaginationConfig: GetTraceGraphPaginatePaginationConfigTypeDef = None,
    ) -> GetTraceGraphPaginateResponseTypeDef:
        """
        [GetTraceGraph.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetTraceGraph.paginate)
        """


class GetTraceSummariesPaginator(Boto3Paginator):
    """
    Paginator for `get_trace_summaries`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: Literal["TraceId", "Event"] = None,
        Sampling: bool = None,
        SamplingStrategy: GetTraceSummariesPaginateSamplingStrategyTypeDef = None,
        FilterExpression: str = None,
        PaginationConfig: GetTraceSummariesPaginatePaginationConfigTypeDef = None,
    ) -> GetTraceSummariesPaginateResponseTypeDef:
        """
        [GetTraceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetTraceSummaries.paginate)
        """
