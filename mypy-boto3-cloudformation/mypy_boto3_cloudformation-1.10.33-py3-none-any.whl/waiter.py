"Main interface for cloudformation service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudformation.type_defs import (
    ChangeSetCreateCompleteWaitWaiterConfigTypeDef,
    StackCreateCompleteWaitWaiterConfigTypeDef,
    StackDeleteCompleteWaitWaiterConfigTypeDef,
    StackExistsWaitWaiterConfigTypeDef,
    StackImportCompleteWaitWaiterConfigTypeDef,
    StackUpdateCompleteWaitWaiterConfigTypeDef,
    TypeRegistrationCompleteWaitWaiterConfigTypeDef,
)


__all__ = (
    "ChangeSetCreateCompleteWaiter",
    "StackCreateCompleteWaiter",
    "StackDeleteCompleteWaiter",
    "StackExistsWaiter",
    "StackImportCompleteWaiter",
    "StackUpdateCompleteWaiter",
    "TypeRegistrationCompleteWaiter",
)


class ChangeSetCreateCompleteWaiter(Boto3Waiter):
    """
    Waiter for `change_set_create_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ChangeSetName: str,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: ChangeSetCreateCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [change_set_create_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.change_set_create_complete.wait)
        """


class StackCreateCompleteWaiter(Boto3Waiter):
    """
    Waiter for `stack_create_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackCreateCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [stack_create_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.stack_create_complete.wait)
        """


class StackDeleteCompleteWaiter(Boto3Waiter):
    """
    Waiter for `stack_delete_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackDeleteCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [stack_delete_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.stack_delete_complete.wait)
        """


class StackExistsWaiter(Boto3Waiter):
    """
    Waiter for `stack_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [stack_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.stack_exists.wait)
        """


class StackImportCompleteWaiter(Boto3Waiter):
    """
    Waiter for `stack_import_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackImportCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [stack_import_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.stack_import_complete.wait)
        """


class StackUpdateCompleteWaiter(Boto3Waiter):
    """
    Waiter for `stack_update_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: StackUpdateCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [stack_update_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.stack_update_complete.wait)
        """


class TypeRegistrationCompleteWaiter(Boto3Waiter):
    """
    Waiter for `type_registration_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        RegistrationToken: str,
        WaiterConfig: TypeRegistrationCompleteWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [type_registration_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.type_registration_complete.wait)
        """
