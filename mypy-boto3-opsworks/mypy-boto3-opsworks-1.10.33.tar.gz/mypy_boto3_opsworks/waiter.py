"Main interface for opsworks service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_opsworks.type_defs import (
    AppExistsWaitWaiterConfigTypeDef,
    DeploymentSuccessfulWaitWaiterConfigTypeDef,
    InstanceOnlineWaitWaiterConfigTypeDef,
    InstanceRegisteredWaitWaiterConfigTypeDef,
    InstanceStoppedWaitWaiterConfigTypeDef,
    InstanceTerminatedWaitWaiterConfigTypeDef,
)


__all__ = (
    "AppExistsWaiter",
    "DeploymentSuccessfulWaiter",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
)


class AppExistsWaiter(Boto3Waiter):
    """
    Waiter for `app_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        AppIds: List[str] = None,
        WaiterConfig: AppExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [app_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworks.html#OpsWorks.Waiter.app_exists.wait)
        """


class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    Waiter for `deployment_successful` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        AppId: str = None,
        DeploymentIds: List[str] = None,
        WaiterConfig: DeploymentSuccessfulWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [deployment_successful.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworks.html#OpsWorks.Waiter.deployment_successful.wait)
        """


class InstanceOnlineWaiter(Boto3Waiter):
    """
    Waiter for `instance_online` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: InstanceOnlineWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_online.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworks.html#OpsWorks.Waiter.instance_online.wait)
        """


class InstanceRegisteredWaiter(Boto3Waiter):
    """
    Waiter for `instance_registered` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: InstanceRegisteredWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_registered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworks.html#OpsWorks.Waiter.instance_registered.wait)
        """


class InstanceStoppedWaiter(Boto3Waiter):
    """
    Waiter for `instance_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: InstanceStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworks.html#OpsWorks.Waiter.instance_stopped.wait)
        """


class InstanceTerminatedWaiter(Boto3Waiter):
    """
    Waiter for `instance_terminated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: InstanceTerminatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_terminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworks.html#OpsWorks.Waiter.instance_terminated.wait)
        """
