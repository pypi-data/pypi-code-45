"Main interface for dms service Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dms.type_defs import (
    DescribeCertificatesPaginateFiltersTypeDef,
    DescribeCertificatesPaginatePaginationConfigTypeDef,
    DescribeCertificatesPaginateResponseTypeDef,
    DescribeConnectionsPaginateFiltersTypeDef,
    DescribeConnectionsPaginatePaginationConfigTypeDef,
    DescribeConnectionsPaginateResponseTypeDef,
    DescribeEndpointTypesPaginateFiltersTypeDef,
    DescribeEndpointTypesPaginatePaginationConfigTypeDef,
    DescribeEndpointTypesPaginateResponseTypeDef,
    DescribeEndpointsPaginateFiltersTypeDef,
    DescribeEndpointsPaginatePaginationConfigTypeDef,
    DescribeEndpointsPaginateResponseTypeDef,
    DescribeEventSubscriptionsPaginateFiltersTypeDef,
    DescribeEventSubscriptionsPaginatePaginationConfigTypeDef,
    DescribeEventSubscriptionsPaginateResponseTypeDef,
    DescribeEventsPaginateFiltersTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef,
    DescribeOrderableReplicationInstancesPaginateResponseTypeDef,
    DescribeReplicationInstancesPaginateFiltersTypeDef,
    DescribeReplicationInstancesPaginatePaginationConfigTypeDef,
    DescribeReplicationInstancesPaginateResponseTypeDef,
    DescribeReplicationSubnetGroupsPaginateFiltersTypeDef,
    DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef,
    DescribeReplicationSubnetGroupsPaginateResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef,
    DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef,
    DescribeReplicationTasksPaginateFiltersTypeDef,
    DescribeReplicationTasksPaginatePaginationConfigTypeDef,
    DescribeReplicationTasksPaginateResponseTypeDef,
    DescribeSchemasPaginatePaginationConfigTypeDef,
    DescribeSchemasPaginateResponseTypeDef,
    DescribeTableStatisticsPaginateFiltersTypeDef,
    DescribeTableStatisticsPaginatePaginationConfigTypeDef,
    DescribeTableStatisticsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeConnectionsPaginator",
    "DescribeEndpointTypesPaginator",
    "DescribeEndpointsPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableReplicationInstancesPaginator",
    "DescribeReplicationInstancesPaginator",
    "DescribeReplicationSubnetGroupsPaginator",
    "DescribeReplicationTaskAssessmentResultsPaginator",
    "DescribeReplicationTasksPaginator",
    "DescribeSchemasPaginator",
    "DescribeTableStatisticsPaginator",
)


class DescribeCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeCertificatesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCertificatesPaginateResponseTypeDef:
        """
        [DescribeCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates.paginate)
        """


class DescribeConnectionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_connections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeConnectionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeConnectionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConnectionsPaginateResponseTypeDef:
        """
        [DescribeConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections.paginate)
        """


class DescribeEndpointTypesPaginator(Boto3Paginator):
    """
    Paginator for `describe_endpoint_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeEndpointTypesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEndpointTypesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEndpointTypesPaginateResponseTypeDef:
        """
        [DescribeEndpointTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes.paginate)
        """


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeEndpointsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEndpointsPaginateResponseTypeDef:
        """
        [DescribeEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_event_subscriptions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[DescribeEventSubscriptionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEventSubscriptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventSubscriptionsPaginateResponseTypeDef:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[DescribeEventsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents.paginate)
        """


class DescribeOrderableReplicationInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_orderable_replication_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeOrderableReplicationInstancesPaginateResponseTypeDef:
        """
        [DescribeOrderableReplicationInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances.paginate)
        """


class DescribeReplicationInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeReplicationInstancesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeReplicationInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationInstancesPaginateResponseTypeDef:
        """
        [DescribeReplicationInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances.paginate)
        """


class DescribeReplicationSubnetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_subnet_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeReplicationSubnetGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationSubnetGroupsPaginateResponseTypeDef:
        """
        [DescribeReplicationSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups.paginate)
        """


class DescribeReplicationTaskAssessmentResultsPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_task_assessment_results`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReplicationTaskArn: str = None,
        PaginationConfig: DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef:
        """
        [DescribeReplicationTaskAssessmentResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults.paginate)
        """


class DescribeReplicationTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeReplicationTasksPaginateFiltersTypeDef] = None,
        WithoutSettings: bool = None,
        PaginationConfig: DescribeReplicationTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationTasksPaginateResponseTypeDef:
        """
        [DescribeReplicationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks.paginate)
        """


class DescribeSchemasPaginator(Boto3Paginator):
    """
    Paginator for `describe_schemas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EndpointArn: str,
        PaginationConfig: DescribeSchemasPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSchemasPaginateResponseTypeDef:
        """
        [DescribeSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas.paginate)
        """


class DescribeTableStatisticsPaginator(Boto3Paginator):
    """
    Paginator for `describe_table_statistics`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReplicationTaskArn: str,
        Filters: List[DescribeTableStatisticsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeTableStatisticsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTableStatisticsPaginateResponseTypeDef:
        """
        [DescribeTableStatistics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics.paginate)
        """
