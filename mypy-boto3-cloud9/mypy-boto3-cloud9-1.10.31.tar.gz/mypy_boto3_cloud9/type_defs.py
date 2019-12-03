"Main interface for cloud9 service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateEnvironmentEc2ResponseTypeDef",
    "ClientCreateEnvironmentMembershipResponsemembershipTypeDef",
    "ClientCreateEnvironmentMembershipResponseTypeDef",
    "ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef",
    "ClientDescribeEnvironmentMembershipsResponseTypeDef",
    "ClientDescribeEnvironmentStatusResponseTypeDef",
    "ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef",
    "ClientDescribeEnvironmentsResponseenvironmentsTypeDef",
    "ClientDescribeEnvironmentsResponseTypeDef",
    "ClientListEnvironmentsResponseTypeDef",
    "ClientUpdateEnvironmentMembershipResponsemembershipTypeDef",
    "ClientUpdateEnvironmentMembershipResponseTypeDef",
    "DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef",
    "DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef",
    "DescribeEnvironmentMembershipsPaginateResponseTypeDef",
    "ListEnvironmentsPaginatePaginationConfigTypeDef",
    "ListEnvironmentsPaginateResponseTypeDef",
)


_ClientCreateEnvironmentEc2ResponseTypeDef = TypedDict(
    "_ClientCreateEnvironmentEc2ResponseTypeDef", {"environmentId": str}, total=False
)


class ClientCreateEnvironmentEc2ResponseTypeDef(_ClientCreateEnvironmentEc2ResponseTypeDef):
    """
    - *(dict) --*

      - **environmentId** *(string) --*

        The ID of the environment that was created.
    """


_ClientCreateEnvironmentMembershipResponsemembershipTypeDef = TypedDict(
    "_ClientCreateEnvironmentMembershipResponsemembershipTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)


class ClientCreateEnvironmentMembershipResponsemembershipTypeDef(
    _ClientCreateEnvironmentMembershipResponsemembershipTypeDef
):
    """
    - **membership** *(dict) --*

      Information about the environment member that was added.
      - **permissions** *(string) --*

        The type of environment member permissions associated with this environment member.
        Available values include:
        * ``owner`` : Owns the environment.
        * ``read-only`` : Has read-only access to the environment.
        * ``read-write`` : Has read-write access to the environment.
    """


_ClientCreateEnvironmentMembershipResponseTypeDef = TypedDict(
    "_ClientCreateEnvironmentMembershipResponseTypeDef",
    {"membership": ClientCreateEnvironmentMembershipResponsemembershipTypeDef},
    total=False,
)


class ClientCreateEnvironmentMembershipResponseTypeDef(
    _ClientCreateEnvironmentMembershipResponseTypeDef
):
    """
    - *(dict) --*

      - **membership** *(dict) --*

        Information about the environment member that was added.
        - **permissions** *(string) --*

          The type of environment member permissions associated with this environment member.
          Available values include:
          * ``owner`` : Owns the environment.
          * ``read-only`` : Has read-only access to the environment.
          * ``read-write`` : Has read-write access to the environment.
    """


_ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)


class ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef(
    _ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef
):
    """
    - *(dict) --*

      Information about an environment member for an AWS Cloud9 development environment.
      - **permissions** *(string) --*

        The type of environment member permissions associated with this environment member.
        Available values include:
        * ``owner`` : Owns the environment.
        * ``read-only`` : Has read-only access to the environment.
        * ``read-write`` : Has read-write access to the environment.
    """


_ClientDescribeEnvironmentMembershipsResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentMembershipsResponseTypeDef",
    {
        "memberships": List[ClientDescribeEnvironmentMembershipsResponsemembershipsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeEnvironmentMembershipsResponseTypeDef(
    _ClientDescribeEnvironmentMembershipsResponseTypeDef
):
    """
    - *(dict) --*

      - **memberships** *(list) --*

        Information about the environment members for the environment.
        - *(dict) --*

          Information about an environment member for an AWS Cloud9 development environment.
          - **permissions** *(string) --*

            The type of environment member permissions associated with this environment member.
            Available values include:
            * ``owner`` : Owns the environment.
            * ``read-only`` : Has read-only access to the environment.
            * ``read-write`` : Has read-write access to the environment.
    """


_ClientDescribeEnvironmentStatusResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentStatusResponseTypeDef",
    {
        "status": Literal[
            "error", "creating", "connecting", "ready", "stopping", "stopped", "deleting"
        ],
        "message": str,
    },
    total=False,
)


class ClientDescribeEnvironmentStatusResponseTypeDef(
    _ClientDescribeEnvironmentStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **status** *(string) --*

        The status of the environment. Available values include:
        * ``connecting`` : The environment is connecting.
        * ``creating`` : The environment is being created.
        * ``deleting`` : The environment is being deleted.
        * ``error`` : The environment is in an error state.
        * ``ready`` : The environment is ready.
        * ``stopped`` : The environment is stopped.
        * ``stopping`` : The environment is stopping.
    """


_ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef",
    {
        "status": Literal["CREATING", "CREATED", "CREATE_FAILED", "DELETING", "DELETE_FAILED"],
        "reason": str,
        "failureResource": str,
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef(
    _ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef
):
    pass


_ClientDescribeEnvironmentsResponseenvironmentsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseenvironmentsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "type": Literal["ssh", "ec2"],
        "arn": str,
        "ownerArn": str,
        "lifecycle": ClientDescribeEnvironmentsResponseenvironmentslifecycleTypeDef,
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseenvironmentsTypeDef(
    _ClientDescribeEnvironmentsResponseenvironmentsTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Cloud9 development environment.
      - **id** *(string) --*

        The ID of the environment.
    """


_ClientDescribeEnvironmentsResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseTypeDef",
    {"environments": List[ClientDescribeEnvironmentsResponseenvironmentsTypeDef]},
    total=False,
)


class ClientDescribeEnvironmentsResponseTypeDef(_ClientDescribeEnvironmentsResponseTypeDef):
    """
    - *(dict) --*

      - **environments** *(list) --*

        Information about the environments that are returned.
        - *(dict) --*

          Information about an AWS Cloud9 development environment.
          - **id** *(string) --*

            The ID of the environment.
    """


_ClientListEnvironmentsResponseTypeDef = TypedDict(
    "_ClientListEnvironmentsResponseTypeDef",
    {"nextToken": str, "environmentIds": List[str]},
    total=False,
)


class ClientListEnvironmentsResponseTypeDef(_ClientListEnvironmentsResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        If there are more than 25 items in the list, only the first 25 items are returned, along
        with a unique string called a *next token* . To get the next batch of items in the list,
        call this operation again, adding the next token to the call.
    """


_ClientUpdateEnvironmentMembershipResponsemembershipTypeDef = TypedDict(
    "_ClientUpdateEnvironmentMembershipResponsemembershipTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)


class ClientUpdateEnvironmentMembershipResponsemembershipTypeDef(
    _ClientUpdateEnvironmentMembershipResponsemembershipTypeDef
):
    """
    - **membership** *(dict) --*

      Information about the environment member whose settings were changed.
      - **permissions** *(string) --*

        The type of environment member permissions associated with this environment member.
        Available values include:
        * ``owner`` : Owns the environment.
        * ``read-only`` : Has read-only access to the environment.
        * ``read-write`` : Has read-write access to the environment.
    """


_ClientUpdateEnvironmentMembershipResponseTypeDef = TypedDict(
    "_ClientUpdateEnvironmentMembershipResponseTypeDef",
    {"membership": ClientUpdateEnvironmentMembershipResponsemembershipTypeDef},
    total=False,
)


class ClientUpdateEnvironmentMembershipResponseTypeDef(
    _ClientUpdateEnvironmentMembershipResponseTypeDef
):
    """
    - *(dict) --*

      - **membership** *(dict) --*

        Information about the environment member whose settings were changed.
        - **permissions** *(string) --*

          The type of environment member permissions associated with this environment member.
          Available values include:
          * ``owner`` : Owns the environment.
          * ``read-only`` : Has read-only access to the environment.
          * ``read-write`` : Has read-write access to the environment.
    """


_DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef(
    _DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef = TypedDict(
    "_DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef",
    {
        "permissions": Literal["owner", "read-write", "read-only"],
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": datetime,
    },
    total=False,
)


class DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef(
    _DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef
):
    """
    - *(dict) --*

      Information about an environment member for an AWS Cloud9 development environment.
      - **permissions** *(string) --*

        The type of environment member permissions associated with this environment member.
        Available values include:
        * ``owner`` : Owns the environment.
        * ``read-only`` : Has read-only access to the environment.
        * ``read-write`` : Has read-write access to the environment.
    """


_DescribeEnvironmentMembershipsPaginateResponseTypeDef = TypedDict(
    "_DescribeEnvironmentMembershipsPaginateResponseTypeDef",
    {
        "memberships": List[DescribeEnvironmentMembershipsPaginateResponsemembershipsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeEnvironmentMembershipsPaginateResponseTypeDef(
    _DescribeEnvironmentMembershipsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **memberships** *(list) --*

        Information about the environment members for the environment.
        - *(dict) --*

          Information about an environment member for an AWS Cloud9 development environment.
          - **permissions** *(string) --*

            The type of environment member permissions associated with this environment member.
            Available values include:
            * ``owner`` : Owns the environment.
            * ``read-only`` : Has read-only access to the environment.
            * ``read-write`` : Has read-write access to the environment.
    """


_ListEnvironmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEnvironmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEnvironmentsPaginatePaginationConfigTypeDef(
    _ListEnvironmentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEnvironmentsPaginateResponseTypeDef = TypedDict(
    "_ListEnvironmentsPaginateResponseTypeDef",
    {"environmentIds": List[str], "NextToken": str},
    total=False,
)


class ListEnvironmentsPaginateResponseTypeDef(_ListEnvironmentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **environmentIds** *(list) --*

        The list of environment identifiers.
        - *(string) --*
    """
