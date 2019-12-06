"Main interface for elasticache service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elasticache.type_defs import (
    CacheClusterAvailableWaitWaiterConfigTypeDef,
    CacheClusterDeletedWaitWaiterConfigTypeDef,
    ReplicationGroupAvailableWaitWaiterConfigTypeDef,
    ReplicationGroupDeletedWaitWaiterConfigTypeDef,
)


__all__ = (
    "CacheClusterAvailableWaiter",
    "CacheClusterDeletedWaiter",
    "ReplicationGroupAvailableWaiter",
    "ReplicationGroupDeletedWaiter",
)


class CacheClusterAvailableWaiter(Boto3Waiter):
    """
    Waiter for `cache_cluster_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: CacheClusterAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [cache_cluster_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Waiter.cache_cluster_available.wait)
        """


class CacheClusterDeletedWaiter(Boto3Waiter):
    """
    Waiter for `cache_cluster_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: CacheClusterDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [cache_cluster_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Waiter.cache_cluster_deleted.wait)
        """


class ReplicationGroupAvailableWaiter(Boto3Waiter):
    """
    Waiter for `replication_group_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: ReplicationGroupAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [replication_group_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Waiter.replication_group_available.wait)
        """


class ReplicationGroupDeletedWaiter(Boto3Waiter):
    """
    Waiter for `replication_group_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: ReplicationGroupDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [replication_group_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticache.html#ElastiCache.Waiter.replication_group_deleted.wait)
        """
