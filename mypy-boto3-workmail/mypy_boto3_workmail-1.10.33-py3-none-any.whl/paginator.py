"Main interface for workmail service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_workmail.type_defs import (
    ListAliasesPaginatePaginationConfigTypeDef,
    ListAliasesPaginateResponseTypeDef,
    ListGroupMembersPaginatePaginationConfigTypeDef,
    ListGroupMembersPaginateResponseTypeDef,
    ListGroupsPaginatePaginationConfigTypeDef,
    ListGroupsPaginateResponseTypeDef,
    ListMailboxPermissionsPaginatePaginationConfigTypeDef,
    ListMailboxPermissionsPaginateResponseTypeDef,
    ListOrganizationsPaginatePaginationConfigTypeDef,
    ListOrganizationsPaginateResponseTypeDef,
    ListResourceDelegatesPaginatePaginationConfigTypeDef,
    ListResourceDelegatesPaginateResponseTypeDef,
    ListResourcesPaginatePaginationConfigTypeDef,
    ListResourcesPaginateResponseTypeDef,
    ListUsersPaginatePaginationConfigTypeDef,
    ListUsersPaginateResponseTypeDef,
)


__all__ = (
    "ListAliasesPaginator",
    "ListGroupMembersPaginator",
    "ListGroupsPaginator",
    "ListMailboxPermissionsPaginator",
    "ListOrganizationsPaginator",
    "ListResourceDelegatesPaginator",
    "ListResourcesPaginator",
    "ListUsersPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    Paginator for `list_aliases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OrganizationId: str,
        EntityId: str,
        PaginationConfig: ListAliasesPaginatePaginationConfigTypeDef = None,
    ) -> ListAliasesPaginateResponseTypeDef:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workmail.html#WorkMail.Paginator.ListAliases.paginate)
        """


class ListGroupMembersPaginator(Boto3Paginator):
    """
    Paginator for `list_group_members`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OrganizationId: str,
        GroupId: str,
        PaginationConfig: ListGroupMembersPaginatePaginationConfigTypeDef = None,
    ) -> ListGroupMembersPaginateResponseTypeDef:
        """
        [ListGroupMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: ListGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListGroupsPaginateResponseTypeDef:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workmail.html#WorkMail.Paginator.ListGroups.paginate)
        """


class ListMailboxPermissionsPaginator(Boto3Paginator):
    """
    Paginator for `list_mailbox_permissions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OrganizationId: str,
        EntityId: str,
        PaginationConfig: ListMailboxPermissionsPaginatePaginationConfigTypeDef = None,
    ) -> ListMailboxPermissionsPaginateResponseTypeDef:
        """
        [ListMailboxPermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions.paginate)
        """


class ListOrganizationsPaginator(Boto3Paginator):
    """
    Paginator for `list_organizations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListOrganizationsPaginatePaginationConfigTypeDef = None
    ) -> ListOrganizationsPaginateResponseTypeDef:
        """
        [ListOrganizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations.paginate)
        """


class ListResourceDelegatesPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_delegates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OrganizationId: str,
        ResourceId: str,
        PaginationConfig: ListResourceDelegatesPaginatePaginationConfigTypeDef = None,
    ) -> ListResourceDelegatesPaginateResponseTypeDef:
        """
        [ListResourceDelegates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates.paginate)
        """


class ListResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: ListResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListResourcesPaginateResponseTypeDef:
        """
        [ListResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workmail.html#WorkMail.Paginator.ListResources.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    Paginator for `list_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, PaginationConfig: ListUsersPaginatePaginationConfigTypeDef = None
    ) -> ListUsersPaginateResponseTypeDef:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workmail.html#WorkMail.Paginator.ListUsers.paginate)
        """
