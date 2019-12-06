"Main interface for codedeploy service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_codedeploy.type_defs import DeploymentSuccessfulWaitWaiterConfigTypeDef


__all__ = ("DeploymentSuccessfulWaiter",)


class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    Waiter for `deployment_successful` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, deploymentId: str, WaiterConfig: DeploymentSuccessfulWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [deployment_successful.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Waiter.deployment_successful.wait)
        """
