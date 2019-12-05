"Main interface for discovery service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_discovery.type_defs import (
    DescribeAgentsPaginateFiltersTypeDef,
    DescribeAgentsPaginatePaginationConfigTypeDef,
    DescribeAgentsPaginateResponseTypeDef,
    DescribeContinuousExportsPaginatePaginationConfigTypeDef,
    DescribeContinuousExportsPaginateResponseTypeDef,
    DescribeExportConfigurationsPaginatePaginationConfigTypeDef,
    DescribeExportConfigurationsPaginateResponseTypeDef,
    DescribeExportTasksPaginateFiltersTypeDef,
    DescribeExportTasksPaginatePaginationConfigTypeDef,
    DescribeExportTasksPaginateResponseTypeDef,
    DescribeTagsPaginateFiltersTypeDef,
    DescribeTagsPaginatePaginationConfigTypeDef,
    DescribeTagsPaginateResponseTypeDef,
    ListConfigurationsPaginateFiltersTypeDef,
    ListConfigurationsPaginateOrderByTypeDef,
    ListConfigurationsPaginatePaginationConfigTypeDef,
    ListConfigurationsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAgentsPaginator",
    "DescribeContinuousExportsPaginator",
    "DescribeExportConfigurationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeTagsPaginator",
    "ListConfigurationsPaginator",
)


class DescribeAgentsPaginator(Boto3Paginator):
    """
    Paginator for `describe_agents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        agentIds: List[str] = None,
        filters: List[DescribeAgentsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeAgentsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAgentsPaginateResponseTypeDef:
        """
        [DescribeAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents.paginate)
        """


class DescribeContinuousExportsPaginator(Boto3Paginator):
    """
    Paginator for `describe_continuous_exports`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        exportIds: List[str] = None,
        PaginationConfig: DescribeContinuousExportsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeContinuousExportsPaginateResponseTypeDef:
        """
        [DescribeContinuousExports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports.paginate)
        """


class DescribeExportConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_export_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        exportIds: List[str] = None,
        PaginationConfig: DescribeExportConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeExportConfigurationsPaginateResponseTypeDef:
        """
        [DescribeExportConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations.paginate)
        """


class DescribeExportTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_export_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        exportIds: List[str] = None,
        filters: List[DescribeExportTasksPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeExportTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeExportTasksPaginateResponseTypeDef:
        """
        [DescribeExportTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    Paginator for `describe_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[DescribeTagsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeTagsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTagsPaginateResponseTypeDef:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags.paginate)
        """


class ListConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        configurationType: Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        filters: List[ListConfigurationsPaginateFiltersTypeDef] = None,
        orderBy: List[ListConfigurationsPaginateOrderByTypeDef] = None,
        PaginationConfig: ListConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> ListConfigurationsPaginateResponseTypeDef:
        """
        [ListConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations.paginate)
        """
