"Main interface for cloud9 service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloud9.type_defs import (
    DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef,
    DescribeEnvironmentMembershipsPaginateResponseTypeDef,
    ListEnvironmentsPaginatePaginationConfigTypeDef,
    ListEnvironmentsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DescribeEnvironmentMembershipsPaginator", "ListEnvironmentsPaginator")


class DescribeEnvironmentMembershipsPaginator(Boto3Paginator):
    """
    Paginator for `describe_environment_memberships`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[Literal["owner", "read-write", "read-only"]] = None,
        PaginationConfig: DescribeEnvironmentMembershipsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEnvironmentMembershipsPaginateResponseTypeDef:
        """
        [DescribeEnvironmentMemberships.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships.paginate)
        """


class ListEnvironmentsPaginator(Boto3Paginator):
    """
    Paginator for `list_environments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListEnvironmentsPaginatePaginationConfigTypeDef = None
    ) -> ListEnvironmentsPaginateResponseTypeDef:
        """
        [ListEnvironments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments.paginate)
        """
