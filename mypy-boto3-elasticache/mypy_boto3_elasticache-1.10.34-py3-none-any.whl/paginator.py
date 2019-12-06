"Main interface for elasticache service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elasticache.type_defs import (
    DescribeCacheClustersPaginatePaginationConfigTypeDef,
    DescribeCacheClustersPaginateResponseTypeDef,
    DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef,
    DescribeCacheEngineVersionsPaginateResponseTypeDef,
    DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef,
    DescribeCacheParameterGroupsPaginateResponseTypeDef,
    DescribeCacheParametersPaginatePaginationConfigTypeDef,
    DescribeCacheParametersPaginateResponseTypeDef,
    DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef,
    DescribeCacheSecurityGroupsPaginateResponseTypeDef,
    DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef,
    DescribeCacheSubnetGroupsPaginateResponseTypeDef,
    DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef,
    DescribeEngineDefaultParametersPaginateResponseTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeReplicationGroupsPaginatePaginationConfigTypeDef,
    DescribeReplicationGroupsPaginateResponseTypeDef,
    DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef,
    DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef,
    DescribeReservedCacheNodesPaginatePaginationConfigTypeDef,
    DescribeReservedCacheNodesPaginateResponseTypeDef,
    DescribeServiceUpdatesPaginatePaginationConfigTypeDef,
    DescribeServiceUpdatesPaginateResponseTypeDef,
    DescribeSnapshotsPaginatePaginationConfigTypeDef,
    DescribeSnapshotsPaginateResponseTypeDef,
    DescribeUpdateActionsPaginatePaginationConfigTypeDef,
    DescribeUpdateActionsPaginateResponseTypeDef,
    DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCacheClustersPaginator",
    "DescribeCacheEngineVersionsPaginator",
    "DescribeCacheParameterGroupsPaginator",
    "DescribeCacheParametersPaginator",
    "DescribeCacheSecurityGroupsPaginator",
    "DescribeCacheSubnetGroupsPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeReplicationGroupsPaginator",
    "DescribeReservedCacheNodesPaginator",
    "DescribeReservedCacheNodesOfferingsPaginator",
    "DescribeServiceUpdatesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeUpdateActionsPaginator",
)


class DescribeCacheClustersPaginator(Boto3Paginator):
    """
    Paginator for `describe_cache_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CacheClusterId: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        PaginationConfig: DescribeCacheClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCacheClustersPaginateResponseTypeDef:
        """
        [DescribeCacheClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters.paginate)
        """


class DescribeCacheEngineVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cache_engine_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        DefaultOnly: bool = None,
        PaginationConfig: DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCacheEngineVersionsPaginateResponseTypeDef:
        """
        [DescribeCacheEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions.paginate)
        """


class DescribeCacheParameterGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cache_parameter_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CacheParameterGroupName: str = None,
        PaginationConfig: DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCacheParameterGroupsPaginateResponseTypeDef:
        """
        [DescribeCacheParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups.paginate)
        """


class DescribeCacheParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_cache_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        PaginationConfig: DescribeCacheParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCacheParametersPaginateResponseTypeDef:
        """
        [DescribeCacheParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters.paginate)
        """


class DescribeCacheSecurityGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cache_security_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CacheSecurityGroupName: str = None,
        PaginationConfig: DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCacheSecurityGroupsPaginateResponseTypeDef:
        """
        [DescribeCacheSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups.paginate)
        """


class DescribeCacheSubnetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_cache_subnet_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CacheSubnetGroupName: str = None,
        PaginationConfig: DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCacheSubnetGroupsPaginateResponseTypeDef:
        """
        [DescribeCacheSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups.paginate)
        """


class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_engine_default_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CacheParameterGroupFamily: str,
        PaginationConfig: DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEngineDefaultParametersPaginateResponseTypeDef:
        """
        [DescribeEngineDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters.paginate)
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
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents.paginate)
        """


class DescribeReplicationGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReplicationGroupId: str = None,
        PaginationConfig: DescribeReplicationGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationGroupsPaginateResponseTypeDef:
        """
        [DescribeReplicationGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups.paginate)
        """


class DescribeReservedCacheNodesPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_cache_nodes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: DescribeReservedCacheNodesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedCacheNodesPaginateResponseTypeDef:
        """
        [DescribeReservedCacheNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes.paginate)
        """


class DescribeReservedCacheNodesOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `describe_reserved_cache_nodes_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef:
        """
        [DescribeReservedCacheNodesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings.paginate)
        """


class DescribeServiceUpdatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_service_updates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        PaginationConfig: DescribeServiceUpdatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeServiceUpdatesPaginateResponseTypeDef:
        """
        [DescribeServiceUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates.paginate)
        """


class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    Paginator for `describe_snapshots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        ShowNodeGroupConfig: bool = None,
        PaginationConfig: DescribeSnapshotsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSnapshotsPaginateResponseTypeDef:
        """
        [DescribeSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots.paginate)
        """


class DescribeUpdateActionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_update_actions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        ServiceUpdateTimeRange: DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef = None,
        UpdateActionStatus: List[
            Literal[
                "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
            ]
        ] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        PaginationConfig: DescribeUpdateActionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeUpdateActionsPaginateResponseTypeDef:
        """
        [DescribeUpdateActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions.paginate)
        """
