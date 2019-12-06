"Main interface for iam service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_iam.type_defs import (
    InstanceProfileExistsWaitWaiterConfigTypeDef,
    PolicyExistsWaitWaiterConfigTypeDef,
    RoleExistsWaitWaiterConfigTypeDef,
    UserExistsWaitWaiterConfigTypeDef,
)


__all__ = (
    "InstanceProfileExistsWaiter",
    "PolicyExistsWaiter",
    "RoleExistsWaiter",
    "UserExistsWaiter",
)


class InstanceProfileExistsWaiter(Boto3Waiter):
    """
    Waiter for `instance_profile_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        InstanceProfileName: str,
        WaiterConfig: InstanceProfileExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_profile_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Waiter.instance_profile_exists.wait)
        """


class PolicyExistsWaiter(Boto3Waiter):
    """
    Waiter for `policy_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, PolicyArn: str, WaiterConfig: PolicyExistsWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [policy_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Waiter.policy_exists.wait)
        """


class RoleExistsWaiter(Boto3Waiter):
    """
    Waiter for `role_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, RoleName: str, WaiterConfig: RoleExistsWaitWaiterConfigTypeDef = None) -> None:
        """
        [role_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Waiter.role_exists.wait)
        """


class UserExistsWaiter(Boto3Waiter):
    """
    Waiter for `user_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, UserName: str = None, WaiterConfig: UserExistsWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [user_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Waiter.user_exists.wait)
        """
