"Main interface for redshift service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_redshift.type_defs import (
    DescribeClusterDbRevisionsPaginatePaginationConfigTypeDef,
    DescribeClusterDbRevisionsPaginateResponseTypeDef,
    DescribeClusterParameterGroupsPaginatePaginationConfigTypeDef,
    DescribeClusterParameterGroupsPaginateResponseTypeDef,
    DescribeClusterParametersPaginatePaginationConfigTypeDef,
    DescribeClusterParametersPaginateResponseTypeDef,
    DescribeClusterSecurityGroupsPaginatePaginationConfigTypeDef,
    DescribeClusterSecurityGroupsPaginateResponseTypeDef,
    DescribeClusterSnapshotsPaginatePaginationConfigTypeDef,
    DescribeClusterSnapshotsPaginateResponseTypeDef,
    DescribeClusterSnapshotsPaginateSortingEntitiesTypeDef,
    DescribeClusterSubnetGroupsPaginatePaginationConfigTypeDef,
    DescribeClusterSubnetGroupsPaginateResponseTypeDef,
    DescribeClusterTracksPaginatePaginationConfigTypeDef,
    DescribeClusterTracksPaginateResponseTypeDef,
    DescribeClusterVersionsPaginatePaginationConfigTypeDef,
    DescribeClusterVersionsPaginateResponseTypeDef,
    DescribeClustersPaginatePaginationConfigTypeDef,
    DescribeClustersPaginateResponseTypeDef,
    DescribeDefaultClusterParametersPaginatePaginationConfigTypeDef,
    DescribeDefaultClusterParametersPaginateResponseTypeDef,
    DescribeEventSubscriptionsPaginatePaginationConfigTypeDef,
    DescribeEventSubscriptionsPaginateResponseTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeHsmClientCertificatesPaginatePaginationConfigTypeDef,
    DescribeHsmClientCertificatesPaginateResponseTypeDef,
    DescribeHsmConfigurationsPaginatePaginationConfigTypeDef,
    DescribeHsmConfigurationsPaginateResponseTypeDef,
    DescribeNodeConfigurationOptionsPaginateFiltersTypeDef,
    DescribeNodeConfigurationOptionsPaginatePaginationConfigTypeDef,
    DescribeNodeConfigurationOptionsPaginateResponseTypeDef,
    DescribeOrderableClusterOptionsPaginatePaginationConfigTypeDef,
    DescribeOrderableClusterOptionsPaginateResponseTypeDef,
    DescribeReservedNodeOfferingsPaginatePaginationConfigTypeDef,
    DescribeReservedNodeOfferingsPaginateResponseTypeDef,
    DescribeReservedNodesPaginatePaginationConfigTypeDef,
    DescribeReservedNodesPaginateResponseTypeDef,
    DescribeScheduledActionsPaginateFiltersTypeDef,
    DescribeScheduledActionsPaginatePaginationConfigTypeDef,
    DescribeScheduledActionsPaginateResponseTypeDef,
    DescribeSnapshotCopyGrantsPaginatePaginationConfigTypeDef,
    DescribeSnapshotCopyGrantsPaginateResponseTypeDef,
    DescribeSnapshotSchedulesPaginatePaginationConfigTypeDef,
    DescribeSnapshotSchedulesPaginateResponseTypeDef,
    DescribeTableRestoreStatusPaginatePaginationConfigTypeDef,
    DescribeTableRestoreStatusPaginateResponseTypeDef,
    DescribeTagsPaginatePaginationConfigTypeDef,
    DescribeTagsPaginateResponseTypeDef,
    GetReservedNodeExchangeOfferingsPaginatePaginationConfigTypeDef,
    GetReservedNodeExchangeOfferingsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeClusterDbRevisionsPaginator",
    "DescribeClusterParameterGroupsPaginator",
    "DescribeClusterParametersPaginator",
    "DescribeClusterSecurityGroupsPaginator",
    "DescribeClusterSnapshotsPaginator",
    "DescribeClusterSubnetGroupsPaginator",
    "DescribeClusterTracksPaginator",
    "DescribeClusterVersionsPaginator",
    "DescribeClustersPaginator",
    "DescribeDefaultClusterParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeHsmClientCertificatesPaginator",
    "DescribeHsmConfigurationsPaginator",
    "DescribeNodeConfigurationOptionsPaginator",
    "DescribeOrderableClusterOptionsPaginator",
    "DescribeReservedNodeOfferingsPaginator",
    "DescribeReservedNodesPaginator",
    "DescribeScheduledActionsPaginator",
    "DescribeSnapshotCopyGrantsPaginator",
    "DescribeSnapshotSchedulesPaginator",
    "DescribeTableRestoreStatusPaginator",
    "DescribeTagsPaginator",
    "GetReservedNodeExchangeOfferingsPaginator",
)


class DescribeClusterDbRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cluster_db_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterIdentifier: str = None,
        PaginationConfig: DescribeClusterDbRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClusterDbRevisionsPaginateResponseTypeDef:
        """
        [DescribeClusterDbRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions.paginate)
        """


class DescribeClusterParameterGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cluster_parameter_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParameterGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeClusterParameterGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClusterParameterGroupsPaginateResponseTypeDef:
        """
        [DescribeClusterParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups.paginate)
        """


class DescribeClusterParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_cluster_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: DescribeClusterParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClusterParametersPaginateResponseTypeDef:
        """
        [DescribeClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters.paginate)
        """


class DescribeClusterSecurityGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cluster_security_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterSecurityGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeClusterSecurityGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClusterSecurityGroupsPaginateResponseTypeDef:
        """
        [DescribeClusterSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups.paginate)
        """


class DescribeClusterSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cluster_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[DescribeClusterSnapshotsPaginateSortingEntitiesTypeDef] = None,
        PaginationConfig: DescribeClusterSnapshotsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClusterSnapshotsPaginateResponseTypeDef:
        """
        [DescribeClusterSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots.paginate)
        """


class DescribeClusterSubnetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cluster_subnet_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterSubnetGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeClusterSubnetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClusterSubnetGroupsPaginateResponseTypeDef:
        """
        [DescribeClusterSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups.paginate)
        """


class DescribeClusterTracksPaginator(Boto3Paginator):
    """
    Paginator for `describe_cluster_tracks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MaintenanceTrackName: str = None,
        PaginationConfig: DescribeClusterTracksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClusterTracksPaginateResponseTypeDef:
        """
        [DescribeClusterTracks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks.paginate)
        """


class DescribeClusterVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cluster_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        PaginationConfig: DescribeClusterVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClusterVersionsPaginateResponseTypeDef:
        """
        [DescribeClusterVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions.paginate)
        """


class DescribeClustersPaginator(Boto3Paginator):
    """
    Paginator for `describe_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClustersPaginateResponseTypeDef:
        """
        [DescribeClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeClusters.paginate)
        """


class DescribeDefaultClusterParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_default_cluster_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParameterGroupFamily: str,
        PaginationConfig: DescribeDefaultClusterParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDefaultClusterParametersPaginateResponseTypeDef:
        """
        [DescribeDefaultClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_event_subscriptions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubscriptionName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeEventSubscriptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventSubscriptionsPaginateResponseTypeDef:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions.paginate)
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
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeEvents.paginate)
        """


class DescribeHsmClientCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_hsm_client_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HsmClientCertificateIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeHsmClientCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeHsmClientCertificatesPaginateResponseTypeDef:
        """
        [DescribeHsmClientCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates.paginate)
        """


class DescribeHsmConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_hsm_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HsmConfigurationIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeHsmConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeHsmConfigurationsPaginateResponseTypeDef:
        """
        [DescribeHsmConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations.paginate)
        """


class DescribeNodeConfigurationOptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_node_configuration_options`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ActionType: Literal["restore-cluster", "recommend-node-config"],
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List[DescribeNodeConfigurationOptionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeNodeConfigurationOptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeNodeConfigurationOptionsPaginateResponseTypeDef:
        """
        [DescribeNodeConfigurationOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions.paginate)
        """


class DescribeOrderableClusterOptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_orderable_cluster_options`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterVersion: str = None,
        NodeType: str = None,
        PaginationConfig: DescribeOrderableClusterOptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeOrderableClusterOptionsPaginateResponseTypeDef:
        """
        [DescribeOrderableClusterOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions.paginate)
        """


class DescribeReservedNodeOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_node_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedNodeOfferingId: str = None,
        PaginationConfig: DescribeReservedNodeOfferingsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedNodeOfferingsPaginateResponseTypeDef:
        """
        [DescribeReservedNodeOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings.paginate)
        """


class DescribeReservedNodesPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_nodes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedNodeId: str = None,
        PaginationConfig: DescribeReservedNodesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedNodesPaginateResponseTypeDef:
        """
        [DescribeReservedNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes.paginate)
        """


class DescribeScheduledActionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_scheduled_actions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ScheduledActionName: str = None,
        TargetActionType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Active: bool = None,
        Filters: List[DescribeScheduledActionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeScheduledActionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeScheduledActionsPaginateResponseTypeDef:
        """
        [DescribeScheduledActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions.paginate)
        """


class DescribeSnapshotCopyGrantsPaginator(Boto3Paginator):
    """
    Paginator for `describe_snapshot_copy_grants`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SnapshotCopyGrantName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeSnapshotCopyGrantsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSnapshotCopyGrantsPaginateResponseTypeDef:
        """
        [DescribeSnapshotCopyGrants.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants.paginate)
        """


class DescribeSnapshotSchedulesPaginator(Boto3Paginator):
    """
    Paginator for `describe_snapshot_schedules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeSnapshotSchedulesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSnapshotSchedulesPaginateResponseTypeDef:
        """
        [DescribeSnapshotSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules.paginate)
        """


class DescribeTableRestoreStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_table_restore_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        PaginationConfig: DescribeTableRestoreStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTableRestoreStatusPaginateResponseTypeDef:
        """
        [DescribeTableRestoreStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    Paginator for `describe_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceName: str = None,
        ResourceType: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: DescribeTagsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTagsPaginateResponseTypeDef:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.DescribeTags.paginate)
        """


class GetReservedNodeExchangeOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `get_reserved_node_exchange_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedNodeId: str,
        PaginationConfig: GetReservedNodeExchangeOfferingsPaginatePaginationConfigTypeDef = None,
    ) -> GetReservedNodeExchangeOfferingsPaginateResponseTypeDef:
        """
        [GetReservedNodeExchangeOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings.paginate)
        """
