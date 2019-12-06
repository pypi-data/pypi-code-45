"Main interface for lightsail service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lightsail.type_defs import (
    GetActiveNamesPaginatePaginationConfigTypeDef,
    GetActiveNamesPaginateResponseTypeDef,
    GetBlueprintsPaginatePaginationConfigTypeDef,
    GetBlueprintsPaginateResponseTypeDef,
    GetBundlesPaginatePaginationConfigTypeDef,
    GetBundlesPaginateResponseTypeDef,
    GetCloudFormationStackRecordsPaginatePaginationConfigTypeDef,
    GetCloudFormationStackRecordsPaginateResponseTypeDef,
    GetDiskSnapshotsPaginatePaginationConfigTypeDef,
    GetDiskSnapshotsPaginateResponseTypeDef,
    GetDisksPaginatePaginationConfigTypeDef,
    GetDisksPaginateResponseTypeDef,
    GetDomainsPaginatePaginationConfigTypeDef,
    GetDomainsPaginateResponseTypeDef,
    GetExportSnapshotRecordsPaginatePaginationConfigTypeDef,
    GetExportSnapshotRecordsPaginateResponseTypeDef,
    GetInstanceSnapshotsPaginatePaginationConfigTypeDef,
    GetInstanceSnapshotsPaginateResponseTypeDef,
    GetInstancesPaginatePaginationConfigTypeDef,
    GetInstancesPaginateResponseTypeDef,
    GetKeyPairsPaginatePaginationConfigTypeDef,
    GetKeyPairsPaginateResponseTypeDef,
    GetLoadBalancersPaginatePaginationConfigTypeDef,
    GetLoadBalancersPaginateResponseTypeDef,
    GetOperationsPaginatePaginationConfigTypeDef,
    GetOperationsPaginateResponseTypeDef,
    GetRelationalDatabaseBlueprintsPaginatePaginationConfigTypeDef,
    GetRelationalDatabaseBlueprintsPaginateResponseTypeDef,
    GetRelationalDatabaseBundlesPaginatePaginationConfigTypeDef,
    GetRelationalDatabaseBundlesPaginateResponseTypeDef,
    GetRelationalDatabaseEventsPaginatePaginationConfigTypeDef,
    GetRelationalDatabaseEventsPaginateResponseTypeDef,
    GetRelationalDatabaseParametersPaginatePaginationConfigTypeDef,
    GetRelationalDatabaseParametersPaginateResponseTypeDef,
    GetRelationalDatabaseSnapshotsPaginatePaginationConfigTypeDef,
    GetRelationalDatabaseSnapshotsPaginateResponseTypeDef,
    GetRelationalDatabasesPaginatePaginationConfigTypeDef,
    GetRelationalDatabasesPaginateResponseTypeDef,
    GetStaticIpsPaginatePaginationConfigTypeDef,
    GetStaticIpsPaginateResponseTypeDef,
)


__all__ = (
    "GetActiveNamesPaginator",
    "GetBlueprintsPaginator",
    "GetBundlesPaginator",
    "GetCloudFormationStackRecordsPaginator",
    "GetDiskSnapshotsPaginator",
    "GetDisksPaginator",
    "GetDomainsPaginator",
    "GetExportSnapshotRecordsPaginator",
    "GetInstanceSnapshotsPaginator",
    "GetInstancesPaginator",
    "GetKeyPairsPaginator",
    "GetLoadBalancersPaginator",
    "GetOperationsPaginator",
    "GetRelationalDatabaseBlueprintsPaginator",
    "GetRelationalDatabaseBundlesPaginator",
    "GetRelationalDatabaseEventsPaginator",
    "GetRelationalDatabaseParametersPaginator",
    "GetRelationalDatabaseSnapshotsPaginator",
    "GetRelationalDatabasesPaginator",
    "GetStaticIpsPaginator",
)


class GetActiveNamesPaginator(Boto3Paginator):
    """
    Paginator for `get_active_names`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetActiveNamesPaginatePaginationConfigTypeDef = None
    ) -> GetActiveNamesPaginateResponseTypeDef:
        """
        [GetActiveNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames.paginate)
        """


class GetBlueprintsPaginator(Boto3Paginator):
    """
    Paginator for `get_blueprints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        includeInactive: bool = None,
        PaginationConfig: GetBlueprintsPaginatePaginationConfigTypeDef = None,
    ) -> GetBlueprintsPaginateResponseTypeDef:
        """
        [GetBlueprints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints.paginate)
        """


class GetBundlesPaginator(Boto3Paginator):
    """
    Paginator for `get_bundles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        includeInactive: bool = None,
        PaginationConfig: GetBundlesPaginatePaginationConfigTypeDef = None,
    ) -> GetBundlesPaginateResponseTypeDef:
        """
        [GetBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetBundles.paginate)
        """


class GetCloudFormationStackRecordsPaginator(Boto3Paginator):
    """
    Paginator for `get_cloud_formation_stack_records`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetCloudFormationStackRecordsPaginatePaginationConfigTypeDef = None
    ) -> GetCloudFormationStackRecordsPaginateResponseTypeDef:
        """
        [GetCloudFormationStackRecords.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords.paginate)
        """


class GetDiskSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `get_disk_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetDiskSnapshotsPaginatePaginationConfigTypeDef = None
    ) -> GetDiskSnapshotsPaginateResponseTypeDef:
        """
        [GetDiskSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots.paginate)
        """


class GetDisksPaginator(Boto3Paginator):
    """
    Paginator for `get_disks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetDisksPaginatePaginationConfigTypeDef = None
    ) -> GetDisksPaginateResponseTypeDef:
        """
        [GetDisks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDisks.paginate)
        """


class GetDomainsPaginator(Boto3Paginator):
    """
    Paginator for `get_domains`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetDomainsPaginatePaginationConfigTypeDef = None
    ) -> GetDomainsPaginateResponseTypeDef:
        """
        [GetDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDomains.paginate)
        """


class GetExportSnapshotRecordsPaginator(Boto3Paginator):
    """
    Paginator for `get_export_snapshot_records`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetExportSnapshotRecordsPaginatePaginationConfigTypeDef = None
    ) -> GetExportSnapshotRecordsPaginateResponseTypeDef:
        """
        [GetExportSnapshotRecords.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords.paginate)
        """


class GetInstanceSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `get_instance_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetInstanceSnapshotsPaginatePaginationConfigTypeDef = None
    ) -> GetInstanceSnapshotsPaginateResponseTypeDef:
        """
        [GetInstanceSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots.paginate)
        """


class GetInstancesPaginator(Boto3Paginator):
    """
    Paginator for `get_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetInstancesPaginatePaginationConfigTypeDef = None
    ) -> GetInstancesPaginateResponseTypeDef:
        """
        [GetInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetInstances.paginate)
        """


class GetKeyPairsPaginator(Boto3Paginator):
    """
    Paginator for `get_key_pairs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetKeyPairsPaginatePaginationConfigTypeDef = None
    ) -> GetKeyPairsPaginateResponseTypeDef:
        """
        [GetKeyPairs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs.paginate)
        """


class GetLoadBalancersPaginator(Boto3Paginator):
    """
    Paginator for `get_load_balancers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetLoadBalancersPaginatePaginationConfigTypeDef = None
    ) -> GetLoadBalancersPaginateResponseTypeDef:
        """
        [GetLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers.paginate)
        """


class GetOperationsPaginator(Boto3Paginator):
    """
    Paginator for `get_operations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetOperationsPaginatePaginationConfigTypeDef = None
    ) -> GetOperationsPaginateResponseTypeDef:
        """
        [GetOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetOperations.paginate)
        """


class GetRelationalDatabaseBlueprintsPaginator(Boto3Paginator):
    """
    Paginator for `get_relational_database_blueprints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: GetRelationalDatabaseBlueprintsPaginatePaginationConfigTypeDef = None,
    ) -> GetRelationalDatabaseBlueprintsPaginateResponseTypeDef:
        """
        [GetRelationalDatabaseBlueprints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints.paginate)
        """


class GetRelationalDatabaseBundlesPaginator(Boto3Paginator):
    """
    Paginator for `get_relational_database_bundles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetRelationalDatabaseBundlesPaginatePaginationConfigTypeDef = None
    ) -> GetRelationalDatabaseBundlesPaginateResponseTypeDef:
        """
        [GetRelationalDatabaseBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles.paginate)
        """


class GetRelationalDatabaseEventsPaginator(Boto3Paginator):
    """
    Paginator for `get_relational_database_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        relationalDatabaseName: str,
        durationInMinutes: int = None,
        PaginationConfig: GetRelationalDatabaseEventsPaginatePaginationConfigTypeDef = None,
    ) -> GetRelationalDatabaseEventsPaginateResponseTypeDef:
        """
        [GetRelationalDatabaseEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents.paginate)
        """


class GetRelationalDatabaseParametersPaginator(Boto3Paginator):
    """
    Paginator for `get_relational_database_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        relationalDatabaseName: str,
        PaginationConfig: GetRelationalDatabaseParametersPaginatePaginationConfigTypeDef = None,
    ) -> GetRelationalDatabaseParametersPaginateResponseTypeDef:
        """
        [GetRelationalDatabaseParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters.paginate)
        """


class GetRelationalDatabaseSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `get_relational_database_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetRelationalDatabaseSnapshotsPaginatePaginationConfigTypeDef = None
    ) -> GetRelationalDatabaseSnapshotsPaginateResponseTypeDef:
        """
        [GetRelationalDatabaseSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots.paginate)
        """


class GetRelationalDatabasesPaginator(Boto3Paginator):
    """
    Paginator for `get_relational_databases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetRelationalDatabasesPaginatePaginationConfigTypeDef = None
    ) -> GetRelationalDatabasesPaginateResponseTypeDef:
        """
        [GetRelationalDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases.paginate)
        """


class GetStaticIpsPaginator(Boto3Paginator):
    """
    Paginator for `get_static_ips`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetStaticIpsPaginatePaginationConfigTypeDef = None
    ) -> GetStaticIpsPaginateResponseTypeDef:
        """
        [GetStaticIps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps.paginate)
        """
