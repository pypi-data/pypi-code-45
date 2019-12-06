"Main interface for health service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_health.type_defs import (
    DescribeAffectedEntitiesPaginateFilterTypeDef,
    DescribeAffectedEntitiesPaginatePaginationConfigTypeDef,
    DescribeAffectedEntitiesPaginateResponseTypeDef,
    DescribeEventAggregatesPaginateFilterTypeDef,
    DescribeEventAggregatesPaginatePaginationConfigTypeDef,
    DescribeEventAggregatesPaginateResponseTypeDef,
    DescribeEventTypesPaginateFilterTypeDef,
    DescribeEventTypesPaginatePaginationConfigTypeDef,
    DescribeEventTypesPaginateResponseTypeDef,
    DescribeEventsPaginateFilterTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeAffectedEntitiesPaginator",
    "DescribeEventAggregatesPaginator",
    "DescribeEventTypesPaginator",
    "DescribeEventsPaginator",
)


class DescribeAffectedEntitiesPaginator(Boto3Paginator):
    """
    Paginator for `describe_affected_entities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filter: DescribeAffectedEntitiesPaginateFilterTypeDef,
        locale: str = None,
        PaginationConfig: DescribeAffectedEntitiesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAffectedEntitiesPaginateResponseTypeDef:
        """
        [DescribeAffectedEntities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Paginator.DescribeAffectedEntities.paginate)
        """


class DescribeEventAggregatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_event_aggregates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        aggregateField: str,
        filter: DescribeEventAggregatesPaginateFilterTypeDef = None,
        PaginationConfig: DescribeEventAggregatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventAggregatesPaginateResponseTypeDef:
        """
        [DescribeEventAggregates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Paginator.DescribeEventAggregates.paginate)
        """


class DescribeEventTypesPaginator(Boto3Paginator):
    """
    Paginator for `describe_event_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filter: DescribeEventTypesPaginateFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: DescribeEventTypesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventTypesPaginateResponseTypeDef:
        """
        [DescribeEventTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Paginator.DescribeEventTypes.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filter: DescribeEventsPaginateFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Paginator.DescribeEvents.paginate)
        """
