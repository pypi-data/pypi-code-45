"Main interface for resource-groups service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_resource_groups.client as client_scope

# pylint: disable=import-self
import mypy_boto3_resource_groups.paginator as paginator_scope
from mypy_boto3_resource_groups.type_defs import (
    ClientCreateGroupResourceQueryTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientDeleteGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
from typing import overload
from mypy_boto3_resource_groups.type_defs import (
    ClientGetGroupQueryResponseTypeDef,
    ClientGetGroupResponseTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientListGroupResourcesFiltersTypeDef,
    ClientListGroupResourcesResponseTypeDef,
    ClientListGroupsFiltersTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientSearchResourcesResourceQueryTypeDef,
    ClientSearchResourcesResponseTypeDef,
    ClientTagResponseTypeDef,
    ClientUntagResponseTypeDef,
    ClientUpdateGroupQueryResourceQueryTypeDef,
    ClientUpdateGroupQueryResponseTypeDef,
    ClientUpdateGroupResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    """
    [ResourceGroups.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(
        self,
        Name: str,
        ResourceQuery: ClientCreateGroupResourceQueryTypeDef,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(self, GroupName: str) -> ClientDeleteGroupResponseTypeDef:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.delete_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group(self, GroupName: str) -> ClientGetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.get_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_query(self, GroupName: str) -> ClientGetGroupQueryResponseTypeDef:
        """
        [Client.get_group_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.get_group_query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tags(self, Arn: str) -> ClientGetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.get_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_resources(
        self,
        GroupName: str,
        Filters: List[ClientListGroupResourcesFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListGroupResourcesResponseTypeDef:
        """
        [Client.list_group_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.list_group_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_groups(
        self,
        Filters: List[ClientListGroupsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.list_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_resources(
        self,
        ResourceQuery: ClientSearchResourcesResourceQueryTypeDef,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientSearchResourcesResponseTypeDef:
        """
        [Client.search_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.search_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag(self, Arn: str, Tags: Dict[str, str]) -> ClientTagResponseTypeDef:
        """
        [Client.tag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.tag)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag(self, Arn: str, Keys: List[str]) -> ClientUntagResponseTypeDef:
        """
        [Client.untag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.untag)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group(
        self, GroupName: str, Description: str = None
    ) -> ClientUpdateGroupResponseTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.update_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group_query(
        self, GroupName: str, ResourceQuery: ClientUpdateGroupQueryResourceQueryTypeDef
    ) -> ClientUpdateGroupQueryResponseTypeDef:
        """
        [Client.update_group_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Client.update_group_query)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_group_resources"]
    ) -> paginator_scope.ListGroupResourcesPaginator:
        """
        [Paginator.ListGroupResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> paginator_scope.ListGroupsPaginator:
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_resources"]
    ) -> paginator_scope.SearchResourcesPaginator:
        """
        [Paginator.SearchResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    MethodNotAllowedException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
