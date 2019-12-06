"Main interface for xray service"

from mypy_boto3_xray.client import Client
from mypy_boto3_xray.paginator import (
    BatchGetTracesPaginator,
    GetGroupsPaginator,
    GetSamplingRulesPaginator,
    GetSamplingStatisticSummariesPaginator,
    GetServiceGraphPaginator,
    GetTimeSeriesServiceStatisticsPaginator,
    GetTraceGraphPaginator,
    GetTraceSummariesPaginator,
)


__all__ = (
    "Client",
    "BatchGetTracesPaginator",
    "GetGroupsPaginator",
    "GetSamplingRulesPaginator",
    "GetSamplingStatisticSummariesPaginator",
    "GetServiceGraphPaginator",
    "GetTimeSeriesServiceStatisticsPaginator",
    "GetTraceGraphPaginator",
    "GetTraceSummariesPaginator",
)
