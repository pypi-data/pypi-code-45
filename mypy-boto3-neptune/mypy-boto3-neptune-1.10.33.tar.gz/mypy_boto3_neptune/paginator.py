"Main interface for neptune service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_neptune.type_defs import (
    DescribeDBClusterParameterGroupsPaginateFiltersTypeDef,
    DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef,
    DescribeDBClusterParameterGroupsPaginateResponseTypeDef,
    DescribeDBClusterParametersPaginateFiltersTypeDef,
    DescribeDBClusterParametersPaginatePaginationConfigTypeDef,
    DescribeDBClusterParametersPaginateResponseTypeDef,
    DescribeDBClusterSnapshotsPaginateFiltersTypeDef,
    DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef,
    DescribeDBClusterSnapshotsPaginateResponseTypeDef,
    DescribeDBClustersPaginateFiltersTypeDef,
    DescribeDBClustersPaginatePaginationConfigTypeDef,
    DescribeDBClustersPaginateResponseTypeDef,
    DescribeDBEngineVersionsPaginateFiltersTypeDef,
    DescribeDBEngineVersionsPaginatePaginationConfigTypeDef,
    DescribeDBEngineVersionsPaginateResponseTypeDef,
    DescribeDBInstancesPaginateFiltersTypeDef,
    DescribeDBInstancesPaginatePaginationConfigTypeDef,
    DescribeDBInstancesPaginateResponseTypeDef,
    DescribeDBParameterGroupsPaginateFiltersTypeDef,
    DescribeDBParameterGroupsPaginatePaginationConfigTypeDef,
    DescribeDBParameterGroupsPaginateResponseTypeDef,
    DescribeDBParametersPaginateFiltersTypeDef,
    DescribeDBParametersPaginatePaginationConfigTypeDef,
    DescribeDBParametersPaginateResponseTypeDef,
    DescribeDBSubnetGroupsPaginateFiltersTypeDef,
    DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef,
    DescribeDBSubnetGroupsPaginateResponseTypeDef,
    DescribeEngineDefaultParametersPaginateFiltersTypeDef,
    DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef,
    DescribeEngineDefaultParametersPaginateResponseTypeDef,
    DescribeEventSubscriptionsPaginateFiltersTypeDef,
    DescribeEventSubscriptionsPaginatePaginationConfigTypeDef,
    DescribeEventSubscriptionsPaginateResponseTypeDef,
    DescribeEventsPaginateFiltersTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef,
    DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef,
    DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef,
    DescribePendingMaintenanceActionsPaginateFiltersTypeDef,
    DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef,
    DescribePendingMaintenanceActionsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBParameterGroupsPaginator",
    "DescribeDBParametersPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
)


class DescribeDBClusterParameterGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_cluster_parameter_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[DescribeDBClusterParameterGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBClusterParameterGroupsPaginateResponseTypeDef:
        """
        [DescribeDBClusterParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups.paginate)
        """


class DescribeDBClusterParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_cluster_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[DescribeDBClusterParametersPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBClusterParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBClusterParametersPaginateResponseTypeDef:
        """
        [DescribeDBClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters.paginate)
        """


class DescribeDBClusterSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_cluster_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DescribeDBClusterSnapshotsPaginateFiltersTypeDef] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        PaginationConfig: DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBClusterSnapshotsPaginateResponseTypeDef:
        """
        [DescribeDBClusterSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots.paginate)
        """


class DescribeDBClustersPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[DescribeDBClustersPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBClustersPaginateResponseTypeDef:
        """
        [DescribeDBClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters.paginate)
        """


class DescribeDBEngineVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_engine_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[DescribeDBEngineVersionsPaginateFiltersTypeDef] = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        PaginationConfig: DescribeDBEngineVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBEngineVersionsPaginateResponseTypeDef:
        """
        [DescribeDBEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions.paginate)
        """


class DescribeDBInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[DescribeDBInstancesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBInstancesPaginateResponseTypeDef:
        """
        [DescribeDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances.paginate)
        """


class DescribeDBParameterGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_parameter_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupName: str = None,
        Filters: List[DescribeDBParameterGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBParameterGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBParameterGroupsPaginateResponseTypeDef:
        """
        [DescribeDBParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups.paginate)
        """


class DescribeDBParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[DescribeDBParametersPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBParametersPaginateResponseTypeDef:
        """
        [DescribeDBParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters.paginate)
        """


class DescribeDBSubnetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_subnet_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[DescribeDBSubnetGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBSubnetGroupsPaginateResponseTypeDef:
        """
        [DescribeDBSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups.paginate)
        """


class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_engine_default_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[DescribeEngineDefaultParametersPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEngineDefaultParametersPaginateResponseTypeDef:
        """
        [DescribeEngineDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters.paginate)
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
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[DescribeEventsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeEvents.paginate)
        """


class DescribeOrderableDBInstanceOptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_orderable_db_instance_options`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef:
        """
        [DescribeOrderableDBInstanceOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        """


class DescribePendingMaintenanceActionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_pending_maintenance_actions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceIdentifier: str = None,
        Filters: List[DescribePendingMaintenanceActionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePendingMaintenanceActionsPaginateResponseTypeDef:
        """
        [DescribePendingMaintenanceActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions.paginate)
        """
