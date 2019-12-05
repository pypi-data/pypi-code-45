"Main interface for datapipeline service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_datapipeline.type_defs import (
    DescribeObjectsPaginatePaginationConfigTypeDef,
    DescribeObjectsPaginateResponseTypeDef,
    ListPipelinesPaginatePaginationConfigTypeDef,
    ListPipelinesPaginateResponseTypeDef,
    QueryObjectsPaginatePaginationConfigTypeDef,
    QueryObjectsPaginateQueryTypeDef,
    QueryObjectsPaginateResponseTypeDef,
)


__all__ = ("DescribeObjectsPaginator", "ListPipelinesPaginator", "QueryObjectsPaginator")


class DescribeObjectsPaginator(Boto3Paginator):
    """
    Paginator for `describe_objects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pipelineId: str,
        objectIds: List[str],
        evaluateExpressions: bool = None,
        PaginationConfig: DescribeObjectsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeObjectsPaginateResponseTypeDef:
        """
        [DescribeObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    Paginator for `list_pipelines`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPipelinesPaginatePaginationConfigTypeDef = None
    ) -> ListPipelinesPaginateResponseTypeDef:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines.paginate)
        """


class QueryObjectsPaginator(Boto3Paginator):
    """
    Paginator for `query_objects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pipelineId: str,
        sphere: str,
        query: QueryObjectsPaginateQueryTypeDef = None,
        PaginationConfig: QueryObjectsPaginatePaginationConfigTypeDef = None,
    ) -> QueryObjectsPaginateResponseTypeDef:
        """
        [QueryObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects.paginate)
        """
