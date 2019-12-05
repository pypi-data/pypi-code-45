"Main interface for opsworkscm service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_opsworkscm.type_defs import NodeAssociatedWaitWaiterConfigTypeDef


__all__ = ("NodeAssociatedWaiter",)


class NodeAssociatedWaiter(Boto3Waiter):
    """
    Waiter for `node_associated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        NodeAssociationStatusToken: str,
        ServerName: str,
        WaiterConfig: NodeAssociatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [node_associated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworkscm.html#OpsWorksCM.Waiter.node_associated.wait)
        """
