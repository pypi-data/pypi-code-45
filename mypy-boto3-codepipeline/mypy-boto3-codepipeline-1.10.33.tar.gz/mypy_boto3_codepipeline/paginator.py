"Main interface for codepipeline service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codepipeline.type_defs import (
    ListActionExecutionsPaginateFilterTypeDef,
    ListActionExecutionsPaginatePaginationConfigTypeDef,
    ListActionExecutionsPaginateResponseTypeDef,
    ListActionTypesPaginatePaginationConfigTypeDef,
    ListActionTypesPaginateResponseTypeDef,
    ListPipelineExecutionsPaginatePaginationConfigTypeDef,
    ListPipelineExecutionsPaginateResponseTypeDef,
    ListPipelinesPaginatePaginationConfigTypeDef,
    ListPipelinesPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListWebhooksPaginatePaginationConfigTypeDef,
    ListWebhooksPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListActionExecutionsPaginator",
    "ListActionTypesPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelinesPaginator",
    "ListTagsForResourcePaginator",
    "ListWebhooksPaginator",
)


class ListActionExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_action_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pipelineName: str,
        filter: ListActionExecutionsPaginateFilterTypeDef = None,
        PaginationConfig: ListActionExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListActionExecutionsPaginateResponseTypeDef:
        """
        [ListActionExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionExecutions.paginate)
        """


class ListActionTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_action_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        actionOwnerFilter: Literal["AWS", "ThirdParty", "Custom"] = None,
        PaginationConfig: ListActionTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListActionTypesPaginateResponseTypeDef:
        """
        [ListActionTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionTypes.paginate)
        """


class ListPipelineExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_pipeline_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pipelineName: str,
        PaginationConfig: ListPipelineExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListPipelineExecutionsPaginateResponseTypeDef:
        """
        [ListPipelineExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelineExecutions.paginate)
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
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelines.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codepipeline.html#CodePipeline.Paginator.ListTagsForResource.paginate)
        """


class ListWebhooksPaginator(Boto3Paginator):
    """
    Paginator for `list_webhooks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListWebhooksPaginatePaginationConfigTypeDef = None
    ) -> ListWebhooksPaginateResponseTypeDef:
        """
        [ListWebhooks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codepipeline.html#CodePipeline.Paginator.ListWebhooks.paginate)
        """
