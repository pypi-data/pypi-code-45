"Main interface for iotthingsgraph service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iotthingsgraph.type_defs import (
    GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef,
    GetFlowTemplateRevisionsPaginateResponseTypeDef,
    GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef,
    GetSystemTemplateRevisionsPaginateResponseTypeDef,
    ListFlowExecutionMessagesPaginatePaginationConfigTypeDef,
    ListFlowExecutionMessagesPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    SearchEntitiesPaginateFiltersTypeDef,
    SearchEntitiesPaginatePaginationConfigTypeDef,
    SearchEntitiesPaginateResponseTypeDef,
    SearchFlowExecutionsPaginatePaginationConfigTypeDef,
    SearchFlowExecutionsPaginateResponseTypeDef,
    SearchFlowTemplatesPaginateFiltersTypeDef,
    SearchFlowTemplatesPaginatePaginationConfigTypeDef,
    SearchFlowTemplatesPaginateResponseTypeDef,
    SearchSystemInstancesPaginateFiltersTypeDef,
    SearchSystemInstancesPaginatePaginationConfigTypeDef,
    SearchSystemInstancesPaginateResponseTypeDef,
    SearchSystemTemplatesPaginateFiltersTypeDef,
    SearchSystemTemplatesPaginatePaginationConfigTypeDef,
    SearchSystemTemplatesPaginateResponseTypeDef,
    SearchThingsPaginatePaginationConfigTypeDef,
    SearchThingsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetFlowTemplateRevisionsPaginator",
    "GetSystemTemplateRevisionsPaginator",
    "ListFlowExecutionMessagesPaginator",
    "ListTagsForResourcePaginator",
    "SearchEntitiesPaginator",
    "SearchFlowExecutionsPaginator",
    "SearchFlowTemplatesPaginator",
    "SearchSystemInstancesPaginator",
    "SearchSystemTemplatesPaginator",
    "SearchThingsPaginator",
)


class GetFlowTemplateRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `get_flow_template_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        id: str,
        PaginationConfig: GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> GetFlowTemplateRevisionsPaginateResponseTypeDef:
        """
        [GetFlowTemplateRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions.paginate)
        """


class GetSystemTemplateRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `get_system_template_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        id: str,
        PaginationConfig: GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> GetSystemTemplateRevisionsPaginateResponseTypeDef:
        """
        [GetSystemTemplateRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions.paginate)
        """


class ListFlowExecutionMessagesPaginator(Boto3Paginator):
    """
    Paginator for `list_flow_execution_messages`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        flowExecutionId: str,
        PaginationConfig: ListFlowExecutionMessagesPaginatePaginationConfigTypeDef = None,
    ) -> ListFlowExecutionMessagesPaginateResponseTypeDef:
        """
        [ListFlowExecutionMessages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages.paginate)
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
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource.paginate)
        """


class SearchEntitiesPaginator(Boto3Paginator):
    """
    Paginator for `search_entities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        entityTypes: List[
            Literal[
                "DEVICE",
                "SERVICE",
                "DEVICE_MODEL",
                "CAPABILITY",
                "STATE",
                "ACTION",
                "EVENT",
                "PROPERTY",
                "MAPPING",
                "ENUM",
            ]
        ],
        filters: List[SearchEntitiesPaginateFiltersTypeDef] = None,
        namespaceVersion: int = None,
        PaginationConfig: SearchEntitiesPaginatePaginationConfigTypeDef = None,
    ) -> SearchEntitiesPaginateResponseTypeDef:
        """
        [SearchEntities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities.paginate)
        """


class SearchFlowExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `search_flow_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: SearchFlowExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> SearchFlowExecutionsPaginateResponseTypeDef:
        """
        [SearchFlowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions.paginate)
        """


class SearchFlowTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `search_flow_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[SearchFlowTemplatesPaginateFiltersTypeDef] = None,
        PaginationConfig: SearchFlowTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> SearchFlowTemplatesPaginateResponseTypeDef:
        """
        [SearchFlowTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates.paginate)
        """


class SearchSystemInstancesPaginator(Boto3Paginator):
    """
    Paginator for `search_system_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[SearchSystemInstancesPaginateFiltersTypeDef] = None,
        PaginationConfig: SearchSystemInstancesPaginatePaginationConfigTypeDef = None,
    ) -> SearchSystemInstancesPaginateResponseTypeDef:
        """
        [SearchSystemInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances.paginate)
        """


class SearchSystemTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `search_system_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[SearchSystemTemplatesPaginateFiltersTypeDef] = None,
        PaginationConfig: SearchSystemTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> SearchSystemTemplatesPaginateResponseTypeDef:
        """
        [SearchSystemTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates.paginate)
        """


class SearchThingsPaginator(Boto3Paginator):
    """
    Paginator for `search_things`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        entityId: str,
        namespaceVersion: int = None,
        PaginationConfig: SearchThingsPaginatePaginationConfigTypeDef = None,
    ) -> SearchThingsPaginateResponseTypeDef:
        """
        [SearchThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings.paginate)
        """
