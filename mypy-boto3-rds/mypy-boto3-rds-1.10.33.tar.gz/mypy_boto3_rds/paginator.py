"Main interface for rds service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_rds.type_defs import (
    DescribeCertificatesPaginateFiltersTypeDef,
    DescribeCertificatesPaginatePaginationConfigTypeDef,
    DescribeCertificatesPaginateResponseTypeDef,
    DescribeCustomAvailabilityZonesPaginateFiltersTypeDef,
    DescribeCustomAvailabilityZonesPaginatePaginationConfigTypeDef,
    DescribeCustomAvailabilityZonesPaginateResponseTypeDef,
    DescribeDBClusterBacktracksPaginateFiltersTypeDef,
    DescribeDBClusterBacktracksPaginatePaginationConfigTypeDef,
    DescribeDBClusterBacktracksPaginateResponseTypeDef,
    DescribeDBClusterEndpointsPaginateFiltersTypeDef,
    DescribeDBClusterEndpointsPaginatePaginationConfigTypeDef,
    DescribeDBClusterEndpointsPaginateResponseTypeDef,
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
    DescribeDBInstanceAutomatedBackupsPaginateFiltersTypeDef,
    DescribeDBInstanceAutomatedBackupsPaginatePaginationConfigTypeDef,
    DescribeDBInstanceAutomatedBackupsPaginateResponseTypeDef,
    DescribeDBInstancesPaginateFiltersTypeDef,
    DescribeDBInstancesPaginatePaginationConfigTypeDef,
    DescribeDBInstancesPaginateResponseTypeDef,
    DescribeDBLogFilesPaginateFiltersTypeDef,
    DescribeDBLogFilesPaginatePaginationConfigTypeDef,
    DescribeDBLogFilesPaginateResponseTypeDef,
    DescribeDBParameterGroupsPaginateFiltersTypeDef,
    DescribeDBParameterGroupsPaginatePaginationConfigTypeDef,
    DescribeDBParameterGroupsPaginateResponseTypeDef,
    DescribeDBParametersPaginateFiltersTypeDef,
    DescribeDBParametersPaginatePaginationConfigTypeDef,
    DescribeDBParametersPaginateResponseTypeDef,
    DescribeDBProxiesPaginateFiltersTypeDef,
    DescribeDBProxiesPaginatePaginationConfigTypeDef,
    DescribeDBProxiesPaginateResponseTypeDef,
    DescribeDBProxyTargetGroupsPaginateFiltersTypeDef,
    DescribeDBProxyTargetGroupsPaginatePaginationConfigTypeDef,
    DescribeDBProxyTargetGroupsPaginateResponseTypeDef,
    DescribeDBProxyTargetsPaginateFiltersTypeDef,
    DescribeDBProxyTargetsPaginatePaginationConfigTypeDef,
    DescribeDBProxyTargetsPaginateResponseTypeDef,
    DescribeDBSecurityGroupsPaginateFiltersTypeDef,
    DescribeDBSecurityGroupsPaginatePaginationConfigTypeDef,
    DescribeDBSecurityGroupsPaginateResponseTypeDef,
    DescribeDBSnapshotsPaginateFiltersTypeDef,
    DescribeDBSnapshotsPaginatePaginationConfigTypeDef,
    DescribeDBSnapshotsPaginateResponseTypeDef,
    DescribeDBSubnetGroupsPaginateFiltersTypeDef,
    DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef,
    DescribeDBSubnetGroupsPaginateResponseTypeDef,
    DescribeEngineDefaultClusterParametersPaginateFiltersTypeDef,
    DescribeEngineDefaultClusterParametersPaginatePaginationConfigTypeDef,
    DescribeEngineDefaultClusterParametersPaginateResponseTypeDef,
    DescribeEngineDefaultParametersPaginateFiltersTypeDef,
    DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef,
    DescribeEngineDefaultParametersPaginateResponseTypeDef,
    DescribeEventSubscriptionsPaginateFiltersTypeDef,
    DescribeEventSubscriptionsPaginatePaginationConfigTypeDef,
    DescribeEventSubscriptionsPaginateResponseTypeDef,
    DescribeEventsPaginateFiltersTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeGlobalClustersPaginateFiltersTypeDef,
    DescribeGlobalClustersPaginatePaginationConfigTypeDef,
    DescribeGlobalClustersPaginateResponseTypeDef,
    DescribeInstallationMediaPaginateFiltersTypeDef,
    DescribeInstallationMediaPaginatePaginationConfigTypeDef,
    DescribeInstallationMediaPaginateResponseTypeDef,
    DescribeOptionGroupOptionsPaginateFiltersTypeDef,
    DescribeOptionGroupOptionsPaginatePaginationConfigTypeDef,
    DescribeOptionGroupOptionsPaginateResponseTypeDef,
    DescribeOptionGroupsPaginateFiltersTypeDef,
    DescribeOptionGroupsPaginatePaginationConfigTypeDef,
    DescribeOptionGroupsPaginateResponseTypeDef,
    DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef,
    DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef,
    DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef,
    DescribePendingMaintenanceActionsPaginateFiltersTypeDef,
    DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef,
    DescribePendingMaintenanceActionsPaginateResponseTypeDef,
    DescribeReservedDBInstancesOfferingsPaginateFiltersTypeDef,
    DescribeReservedDBInstancesOfferingsPaginatePaginationConfigTypeDef,
    DescribeReservedDBInstancesOfferingsPaginateResponseTypeDef,
    DescribeReservedDBInstancesPaginateFiltersTypeDef,
    DescribeReservedDBInstancesPaginatePaginationConfigTypeDef,
    DescribeReservedDBInstancesPaginateResponseTypeDef,
    DescribeSourceRegionsPaginateFiltersTypeDef,
    DescribeSourceRegionsPaginatePaginationConfigTypeDef,
    DescribeSourceRegionsPaginateResponseTypeDef,
    DownloadDBLogFilePortionPaginatePaginationConfigTypeDef,
    DownloadDBLogFilePortionPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeCustomAvailabilityZonesPaginator",
    "DescribeDBClusterBacktracksPaginator",
    "DescribeDBClusterEndpointsPaginator",
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstanceAutomatedBackupsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBLogFilesPaginator",
    "DescribeDBParameterGroupsPaginator",
    "DescribeDBParametersPaginator",
    "DescribeDBProxiesPaginator",
    "DescribeDBProxyTargetGroupsPaginator",
    "DescribeDBProxyTargetsPaginator",
    "DescribeDBSecurityGroupsPaginator",
    "DescribeDBSnapshotsPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEngineDefaultClusterParametersPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeGlobalClustersPaginator",
    "DescribeInstallationMediaPaginator",
    "DescribeOptionGroupOptionsPaginator",
    "DescribeOptionGroupsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
    "DescribeReservedDBInstancesPaginator",
    "DescribeReservedDBInstancesOfferingsPaginator",
    "DescribeSourceRegionsPaginator",
    "DownloadDBLogFilePortionPaginator",
)


class DescribeCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CertificateIdentifier: str = None,
        Filters: List[DescribeCertificatesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCertificatesPaginateResponseTypeDef:
        """
        [DescribeCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeCertificates.paginate)
        """


class DescribeCustomAvailabilityZonesPaginator(Boto3Paginator):
    """
    Paginator for `describe_custom_availability_zones`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CustomAvailabilityZoneId: str = None,
        Filters: List[DescribeCustomAvailabilityZonesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeCustomAvailabilityZonesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCustomAvailabilityZonesPaginateResponseTypeDef:
        """
        [DescribeCustomAvailabilityZones.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeCustomAvailabilityZones.paginate)
        """


class DescribeDBClusterBacktracksPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_cluster_backtracks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = None,
        Filters: List[DescribeDBClusterBacktracksPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBClusterBacktracksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBClusterBacktracksPaginateResponseTypeDef:
        """
        [DescribeDBClusterBacktracks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBClusterBacktracks.paginate)
        """


class DescribeDBClusterEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_cluster_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[DescribeDBClusterEndpointsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBClusterEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBClusterEndpointsPaginateResponseTypeDef:
        """
        [DescribeDBClusterEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBClusterEndpoints.paginate)
        """


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
        [DescribeDBClusterParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameterGroups.paginate)
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
        [DescribeDBClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameters.paginate)
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
        [DescribeDBClusterSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBClusterSnapshots.paginate)
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
        IncludeShared: bool = None,
        PaginationConfig: DescribeDBClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBClustersPaginateResponseTypeDef:
        """
        [DescribeDBClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBClusters.paginate)
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
        IncludeAll: bool = None,
        PaginationConfig: DescribeDBEngineVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBEngineVersionsPaginateResponseTypeDef:
        """
        [DescribeDBEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBEngineVersions.paginate)
        """


class DescribeDBInstanceAutomatedBackupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_instance_automated_backups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DbiResourceId: str = None,
        DBInstanceIdentifier: str = None,
        Filters: List[DescribeDBInstanceAutomatedBackupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBInstanceAutomatedBackupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBInstanceAutomatedBackupsPaginateResponseTypeDef:
        """
        [DescribeDBInstanceAutomatedBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups.paginate)
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
        [DescribeDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBInstances.paginate)
        """


class DescribeDBLogFilesPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_log_files`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: str = None,
        FileLastWritten: int = None,
        FileSize: int = None,
        Filters: List[DescribeDBLogFilesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBLogFilesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBLogFilesPaginateResponseTypeDef:
        """
        [DescribeDBLogFiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBLogFiles.paginate)
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
        [DescribeDBParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBParameterGroups.paginate)
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
        [DescribeDBParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBParameters.paginate)
        """


class DescribeDBProxiesPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_proxies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBProxyName: str = None,
        Filters: List[DescribeDBProxiesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBProxiesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBProxiesPaginateResponseTypeDef:
        """
        [DescribeDBProxies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBProxies.paginate)
        """


class DescribeDBProxyTargetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_proxy_target_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[DescribeDBProxyTargetGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBProxyTargetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBProxyTargetGroupsPaginateResponseTypeDef:
        """
        [DescribeDBProxyTargetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargetGroups.paginate)
        """


class DescribeDBProxyTargetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_proxy_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[DescribeDBProxyTargetsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBProxyTargetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBProxyTargetsPaginateResponseTypeDef:
        """
        [DescribeDBProxyTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargets.paginate)
        """


class DescribeDBSecurityGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_security_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBSecurityGroupName: str = None,
        Filters: List[DescribeDBSecurityGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBSecurityGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBSecurityGroupsPaginateResponseTypeDef:
        """
        [DescribeDBSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBSecurityGroups.paginate)
        """


class DescribeDBSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[DescribeDBSnapshotsPaginateFiltersTypeDef] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        PaginationConfig: DescribeDBSnapshotsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBSnapshotsPaginateResponseTypeDef:
        """
        [DescribeDBSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBSnapshots.paginate)
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
        [DescribeDBSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeDBSubnetGroups.paginate)
        """


class DescribeEngineDefaultClusterParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_engine_default_cluster_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[DescribeEngineDefaultClusterParametersPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEngineDefaultClusterParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEngineDefaultClusterParametersPaginateResponseTypeDef:
        """
        [DescribeEngineDefaultClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultClusterParameters.paginate)
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
        [DescribeEngineDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultParameters.paginate)
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
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeEventSubscriptions.paginate)
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
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeEvents.paginate)
        """


class DescribeGlobalClustersPaginator(Boto3Paginator):
    """
    Paginator for `describe_global_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalClusterIdentifier: str = None,
        Filters: List[DescribeGlobalClustersPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeGlobalClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeGlobalClustersPaginateResponseTypeDef:
        """
        [DescribeGlobalClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeGlobalClusters.paginate)
        """


class DescribeInstallationMediaPaginator(Boto3Paginator):
    """
    Paginator for `describe_installation_media`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstallationMediaId: str = None,
        Filters: List[DescribeInstallationMediaPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeInstallationMediaPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstallationMediaPaginateResponseTypeDef:
        """
        [DescribeInstallationMedia.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeInstallationMedia.paginate)
        """


class DescribeOptionGroupOptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_option_group_options`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EngineName: str,
        MajorEngineVersion: str = None,
        Filters: List[DescribeOptionGroupOptionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeOptionGroupOptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeOptionGroupOptionsPaginateResponseTypeDef:
        """
        [DescribeOptionGroupOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeOptionGroupOptions.paginate)
        """


class DescribeOptionGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_option_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OptionGroupName: str = None,
        Filters: List[DescribeOptionGroupsPaginateFiltersTypeDef] = None,
        EngineName: str = None,
        MajorEngineVersion: str = None,
        PaginationConfig: DescribeOptionGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeOptionGroupsPaginateResponseTypeDef:
        """
        [DescribeOptionGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeOptionGroups.paginate)
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
        [DescribeOrderableDBInstanceOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeOrderableDBInstanceOptions.paginate)
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
        [DescribePendingMaintenanceActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribePendingMaintenanceActions.paginate)
        """


class DescribeReservedDBInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_db_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedDBInstanceId: str = None,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        LeaseId: str = None,
        Filters: List[DescribeReservedDBInstancesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeReservedDBInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedDBInstancesPaginateResponseTypeDef:
        """
        [DescribeReservedDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstances.paginate)
        """


class DescribeReservedDBInstancesOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_db_instances_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        Filters: List[DescribeReservedDBInstancesOfferingsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeReservedDBInstancesOfferingsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedDBInstancesOfferingsPaginateResponseTypeDef:
        """
        [DescribeReservedDBInstancesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstancesOfferings.paginate)
        """


class DescribeSourceRegionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_source_regions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RegionName: str = None,
        Filters: List[DescribeSourceRegionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeSourceRegionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSourceRegionsPaginateResponseTypeDef:
        """
        [DescribeSourceRegions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DescribeSourceRegions.paginate)
        """


class DownloadDBLogFilePortionPaginator(Boto3Paginator):
    """
    Paginator for `download_db_log_file_portion`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        PaginationConfig: DownloadDBLogFilePortionPaginatePaginationConfigTypeDef = None,
    ) -> DownloadDBLogFilePortionPaginateResponseTypeDef:
        """
        [DownloadDBLogFilePortion.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rds.html#RDS.Paginator.DownloadDBLogFilePortion.paginate)
        """
