"Main interface for lambda service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_lambda.type_defs import (
    FunctionActiveWaitWaiterConfigTypeDef,
    FunctionExistsWaitWaiterConfigTypeDef,
    FunctionUpdatedWaitWaiterConfigTypeDef,
)


__all__ = ("FunctionActiveWaiter", "FunctionExistsWaiter", "FunctionUpdatedWaiter")


class FunctionActiveWaiter(Boto3Waiter):
    """
    Waiter for `function_active` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        FunctionName: str,
        Qualifier: str = None,
        WaiterConfig: FunctionActiveWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [function_active.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/lambda.html#Lambda.Waiter.function_active.wait)
        """


class FunctionExistsWaiter(Boto3Waiter):
    """
    Waiter for `function_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        FunctionName: str,
        Qualifier: str = None,
        WaiterConfig: FunctionExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [function_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/lambda.html#Lambda.Waiter.function_exists.wait)
        """


class FunctionUpdatedWaiter(Boto3Waiter):
    """
    Waiter for `function_updated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        FunctionName: str,
        Qualifier: str = None,
        WaiterConfig: FunctionUpdatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [function_updated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/lambda.html#Lambda.Waiter.function_updated.wait)
        """
