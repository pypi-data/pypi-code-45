"Main interface for glacier service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_glacier.type_defs import (
    VaultExistsWaitWaiterConfigTypeDef,
    VaultNotExistsWaitWaiterConfigTypeDef,
)


__all__ = ("VaultExistsWaiter", "VaultNotExistsWaiter")


class VaultExistsWaiter(Boto3Waiter):
    """
    Waiter for `vault_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        vaultName: str,
        accountId: str = None,
        WaiterConfig: VaultExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [vault_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glacier.html#Glacier.Waiter.vault_exists.wait)
        """


class VaultNotExistsWaiter(Boto3Waiter):
    """
    Waiter for `vault_not_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        vaultName: str,
        accountId: str = None,
        WaiterConfig: VaultNotExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [vault_not_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glacier.html#Glacier.Waiter.vault_not_exists.wait)
        """
