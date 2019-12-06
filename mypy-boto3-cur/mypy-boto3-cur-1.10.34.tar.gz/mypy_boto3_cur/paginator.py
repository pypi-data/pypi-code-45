"Main interface for cur service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cur.type_defs import (
    DescribeReportDefinitionsPaginatePaginationConfigTypeDef,
    DescribeReportDefinitionsPaginateResponseTypeDef,
)


__all__ = ("DescribeReportDefinitionsPaginator",)


class DescribeReportDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_report_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeReportDefinitionsPaginatePaginationConfigTypeDef = None
    ) -> DescribeReportDefinitionsPaginateResponseTypeDef:
        """
        [DescribeReportDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cur.html#CostandUsageReportService.Paginator.DescribeReportDefinitions.paginate)
        """
