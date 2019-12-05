"Main interface for schemas service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_schemas.type_defs import CodeBindingExistsWaitWaiterConfigTypeDef


__all__ = ("CodeBindingExistsWaiter",)


class CodeBindingExistsWaiter(Boto3Waiter):
    """
    Waiter for `code_binding_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Language: str,
        RegistryName: str,
        SchemaName: str,
        SchemaVersion: str = None,
        WaiterConfig: CodeBindingExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [code_binding_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/schemas.html#Schemas.Waiter.code_binding_exists.wait)
        """
