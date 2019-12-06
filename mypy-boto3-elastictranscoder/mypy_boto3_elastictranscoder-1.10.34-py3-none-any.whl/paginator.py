"Main interface for elastictranscoder service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elastictranscoder.type_defs import (
    ListJobsByPipelinePaginatePaginationConfigTypeDef,
    ListJobsByPipelinePaginateResponseTypeDef,
    ListJobsByStatusPaginatePaginationConfigTypeDef,
    ListJobsByStatusPaginateResponseTypeDef,
    ListPipelinesPaginatePaginationConfigTypeDef,
    ListPipelinesPaginateResponseTypeDef,
    ListPresetsPaginatePaginationConfigTypeDef,
    ListPresetsPaginateResponseTypeDef,
)


__all__ = (
    "ListJobsByPipelinePaginator",
    "ListJobsByStatusPaginator",
    "ListPipelinesPaginator",
    "ListPresetsPaginator",
)


class ListJobsByPipelinePaginator(Boto3Paginator):
    """
    Paginator for `list_jobs_by_pipeline`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PipelineId: str,
        Ascending: str = None,
        PaginationConfig: ListJobsByPipelinePaginatePaginationConfigTypeDef = None,
    ) -> ListJobsByPipelinePaginateResponseTypeDef:
        """
        [ListJobsByPipeline.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline.paginate)
        """


class ListJobsByStatusPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs_by_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Status: str,
        Ascending: str = None,
        PaginationConfig: ListJobsByStatusPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsByStatusPaginateResponseTypeDef:
        """
        [ListJobsByStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    Paginator for `list_pipelines`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Ascending: str = None,
        PaginationConfig: ListPipelinesPaginatePaginationConfigTypeDef = None,
    ) -> ListPipelinesPaginateResponseTypeDef:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines.paginate)
        """


class ListPresetsPaginator(Boto3Paginator):
    """
    Paginator for `list_presets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Ascending: str = None,
        PaginationConfig: ListPresetsPaginatePaginationConfigTypeDef = None,
    ) -> ListPresetsPaginateResponseTypeDef:
        """
        [ListPresets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets.paginate)
        """
