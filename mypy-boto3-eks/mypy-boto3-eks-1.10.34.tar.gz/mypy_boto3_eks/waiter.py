"Main interface for eks service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_eks.type_defs import (
    ClusterActiveWaitWaiterConfigTypeDef,
    ClusterDeletedWaitWaiterConfigTypeDef,
    NodegroupActiveWaitWaiterConfigTypeDef,
    NodegroupDeletedWaitWaiterConfigTypeDef,
)


__all__ = (
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)


class ClusterActiveWaiter(Boto3Waiter):
    """
    Waiter for `cluster_active` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, name: str, WaiterConfig: ClusterActiveWaitWaiterConfigTypeDef = None) -> None:
        """
        [cluster_active.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/eks.html#EKS.Waiter.cluster_active.wait)
        """


class ClusterDeletedWaiter(Boto3Waiter):
    """
    Waiter for `cluster_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, name: str, WaiterConfig: ClusterDeletedWaitWaiterConfigTypeDef = None) -> None:
        """
        [cluster_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/eks.html#EKS.Waiter.cluster_deleted.wait)
        """


class NodegroupActiveWaiter(Boto3Waiter):
    """
    Waiter for `nodegroup_active` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        clusterName: str,
        nodegroupName: str,
        WaiterConfig: NodegroupActiveWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [nodegroup_active.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/eks.html#EKS.Waiter.nodegroup_active.wait)
        """


class NodegroupDeletedWaiter(Boto3Waiter):
    """
    Waiter for `nodegroup_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        clusterName: str,
        nodegroupName: str,
        WaiterConfig: NodegroupDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [nodegroup_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/eks.html#EKS.Waiter.nodegroup_deleted.wait)
        """
