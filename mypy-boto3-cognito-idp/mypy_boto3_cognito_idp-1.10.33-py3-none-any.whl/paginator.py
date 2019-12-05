"Main interface for cognito-idp service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cognito_idp.type_defs import (
    AdminListGroupsForUserPaginatePaginationConfigTypeDef,
    AdminListGroupsForUserPaginateResponseTypeDef,
    AdminListUserAuthEventsPaginatePaginationConfigTypeDef,
    AdminListUserAuthEventsPaginateResponseTypeDef,
    ListGroupsPaginatePaginationConfigTypeDef,
    ListGroupsPaginateResponseTypeDef,
    ListIdentityProvidersPaginatePaginationConfigTypeDef,
    ListIdentityProvidersPaginateResponseTypeDef,
    ListResourceServersPaginatePaginationConfigTypeDef,
    ListResourceServersPaginateResponseTypeDef,
    ListUserPoolClientsPaginatePaginationConfigTypeDef,
    ListUserPoolClientsPaginateResponseTypeDef,
    ListUserPoolsPaginatePaginationConfigTypeDef,
    ListUserPoolsPaginateResponseTypeDef,
    ListUsersInGroupPaginatePaginationConfigTypeDef,
    ListUsersInGroupPaginateResponseTypeDef,
    ListUsersPaginatePaginationConfigTypeDef,
    ListUsersPaginateResponseTypeDef,
)


__all__ = (
    "AdminListGroupsForUserPaginator",
    "AdminListUserAuthEventsPaginator",
    "ListGroupsPaginator",
    "ListIdentityProvidersPaginator",
    "ListResourceServersPaginator",
    "ListUserPoolClientsPaginator",
    "ListUserPoolsPaginator",
    "ListUsersPaginator",
    "ListUsersInGroupPaginator",
)


class AdminListGroupsForUserPaginator(Boto3Paginator):
    """
    Paginator for `admin_list_groups_for_user`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Username: str,
        UserPoolId: str,
        PaginationConfig: AdminListGroupsForUserPaginatePaginationConfigTypeDef = None,
    ) -> AdminListGroupsForUserPaginateResponseTypeDef:
        """
        [AdminListGroupsForUser.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser.paginate)
        """


class AdminListUserAuthEventsPaginator(Boto3Paginator):
    """
    Paginator for `admin_list_user_auth_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        Username: str,
        PaginationConfig: AdminListUserAuthEventsPaginatePaginationConfigTypeDef = None,
    ) -> AdminListUserAuthEventsPaginateResponseTypeDef:
        """
        [AdminListUserAuthEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserPoolId: str, PaginationConfig: ListGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListGroupsPaginateResponseTypeDef:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups.paginate)
        """


class ListIdentityProvidersPaginator(Boto3Paginator):
    """
    Paginator for `list_identity_providers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: ListIdentityProvidersPaginatePaginationConfigTypeDef = None,
    ) -> ListIdentityProvidersPaginateResponseTypeDef:
        """
        [ListIdentityProviders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders.paginate)
        """


class ListResourceServersPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_servers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: ListResourceServersPaginatePaginationConfigTypeDef = None,
    ) -> ListResourceServersPaginateResponseTypeDef:
        """
        [ListResourceServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers.paginate)
        """


class ListUserPoolClientsPaginator(Boto3Paginator):
    """
    Paginator for `list_user_pool_clients`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: ListUserPoolClientsPaginatePaginationConfigTypeDef = None,
    ) -> ListUserPoolClientsPaginateResponseTypeDef:
        """
        [ListUserPoolClients.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients.paginate)
        """


class ListUserPoolsPaginator(Boto3Paginator):
    """
    Paginator for `list_user_pools`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListUserPoolsPaginatePaginationConfigTypeDef = None
    ) -> ListUserPoolsPaginateResponseTypeDef:
        """
        [ListUserPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    Paginator for `list_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Filter: str = None,
        PaginationConfig: ListUsersPaginatePaginationConfigTypeDef = None,
    ) -> ListUsersPaginateResponseTypeDef:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers.paginate)
        """


class ListUsersInGroupPaginator(Boto3Paginator):
    """
    Paginator for `list_users_in_group`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        GroupName: str,
        PaginationConfig: ListUsersInGroupPaginatePaginationConfigTypeDef = None,
    ) -> ListUsersInGroupPaginateResponseTypeDef:
        """
        [ListUsersInGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup.paginate)
        """
