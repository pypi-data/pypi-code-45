"Main interface for workmail service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateResourceResponseTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientDescribeGroupResponseTypeDef",
    "ClientDescribeOrganizationResponseTypeDef",
    "ClientDescribeResourceResponseBookingOptionsTypeDef",
    "ClientDescribeResourceResponseTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientGetMailboxDetailsResponseTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListGroupMembersResponseMembersTypeDef",
    "ClientListGroupMembersResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListMailboxPermissionsResponsePermissionsTypeDef",
    "ClientListMailboxPermissionsResponseTypeDef",
    "ClientListOrganizationsResponseOrganizationSummariesTypeDef",
    "ClientListOrganizationsResponseTypeDef",
    "ClientListResourceDelegatesResponseDelegatesTypeDef",
    "ClientListResourceDelegatesResponseTypeDef",
    "ClientListResourcesResponseResourcesTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientUpdateResourceBookingOptionsTypeDef",
    "ListAliasesPaginatePaginationConfigTypeDef",
    "ListAliasesPaginateResponseTypeDef",
    "ListGroupMembersPaginatePaginationConfigTypeDef",
    "ListGroupMembersPaginateResponseMembersTypeDef",
    "ListGroupMembersPaginateResponseTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "ListMailboxPermissionsPaginatePaginationConfigTypeDef",
    "ListMailboxPermissionsPaginateResponsePermissionsTypeDef",
    "ListMailboxPermissionsPaginateResponseTypeDef",
    "ListOrganizationsPaginatePaginationConfigTypeDef",
    "ListOrganizationsPaginateResponseOrganizationSummariesTypeDef",
    "ListOrganizationsPaginateResponseTypeDef",
    "ListResourceDelegatesPaginatePaginationConfigTypeDef",
    "ListResourceDelegatesPaginateResponseDelegatesTypeDef",
    "ListResourceDelegatesPaginateResponseTypeDef",
    "ListResourcesPaginatePaginationConfigTypeDef",
    "ListResourcesPaginateResponseResourcesTypeDef",
    "ListResourcesPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUsersTypeDef",
    "ListUsersPaginateResponseTypeDef",
)


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef", {"GroupId": str}, total=False
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    - *(dict) --*

      - **GroupId** *(string) --*

        The identifier of the group.
    """


_ClientCreateResourceResponseTypeDef = TypedDict(
    "_ClientCreateResourceResponseTypeDef", {"ResourceId": str}, total=False
)


class ClientCreateResourceResponseTypeDef(_ClientCreateResourceResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceId** *(string) --*

        The identifier of the new resource.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"UserId": str}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    - *(dict) --*

      - **UserId** *(string) --*

        The identifier for the new user.
    """


_ClientDescribeGroupResponseTypeDef = TypedDict(
    "_ClientDescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "Name": str,
        "Email": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientDescribeGroupResponseTypeDef(_ClientDescribeGroupResponseTypeDef):
    """
    - *(dict) --*

      - **GroupId** *(string) --*

        The identifier of the described group.
    """


_ClientDescribeOrganizationResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "Alias": str,
        "State": str,
        "DirectoryId": str,
        "DirectoryType": str,
        "DefaultMailDomain": str,
        "CompletedDate": datetime,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDescribeOrganizationResponseTypeDef(_ClientDescribeOrganizationResponseTypeDef):
    """
    - *(dict) --*

      - **OrganizationId** *(string) --*

        The identifier of an organization.
    """


_ClientDescribeResourceResponseBookingOptionsTypeDef = TypedDict(
    "_ClientDescribeResourceResponseBookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)


class ClientDescribeResourceResponseBookingOptionsTypeDef(
    _ClientDescribeResourceResponseBookingOptionsTypeDef
):
    pass


_ClientDescribeResourceResponseTypeDef = TypedDict(
    "_ClientDescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": Literal["ROOM", "EQUIPMENT"],
        "BookingOptions": ClientDescribeResourceResponseBookingOptionsTypeDef,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientDescribeResourceResponseTypeDef(_ClientDescribeResourceResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceId** *(string) --*

        The identifier of the described resource.
    """


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {
        "UserId": str,
        "Name": str,
        "Email": str,
        "DisplayName": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "UserRole": Literal["USER", "RESOURCE", "SYSTEM_USER"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    - *(dict) --*

      - **UserId** *(string) --*

        The identifier for the described user.
    """


_ClientGetMailboxDetailsResponseTypeDef = TypedDict(
    "_ClientGetMailboxDetailsResponseTypeDef",
    {"MailboxQuota": int, "MailboxSize": float},
    total=False,
)


class ClientGetMailboxDetailsResponseTypeDef(_ClientGetMailboxDetailsResponseTypeDef):
    """
    - *(dict) --*

      - **MailboxQuota** *(integer) --*

        The maximum allowed mailbox size, in MB, for the specified user.
    """


_ClientListAliasesResponseTypeDef = TypedDict(
    "_ClientListAliasesResponseTypeDef", {"Aliases": List[str], "NextToken": str}, total=False
)


class ClientListAliasesResponseTypeDef(_ClientListAliasesResponseTypeDef):
    """
    - *(dict) --*

      - **Aliases** *(list) --*

        The entity's paginated aliases.
        - *(string) --*
    """


_ClientListGroupMembersResponseMembersTypeDef = TypedDict(
    "_ClientListGroupMembersResponseMembersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": Literal["GROUP", "USER"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientListGroupMembersResponseMembersTypeDef(_ClientListGroupMembersResponseMembersTypeDef):
    """
    - *(dict) --*

      The representation of a user or group.
      - **Id** *(string) --*

        The identifier of the member.
    """


_ClientListGroupMembersResponseTypeDef = TypedDict(
    "_ClientListGroupMembersResponseTypeDef",
    {"Members": List[ClientListGroupMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)


class ClientListGroupMembersResponseTypeDef(_ClientListGroupMembersResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        The members associated to the group.
        - *(dict) --*

          The representation of a user or group.
          - **Id** *(string) --*

            The identifier of the member.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    - *(dict) --*

      The representation of an Amazon WorkMail group.
      - **Id** *(string) --*

        The identifier of the group.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The overview of groups for an organization.
        - *(dict) --*

          The representation of an Amazon WorkMail group.
          - **Id** *(string) --*

            The identifier of the group.
    """


_ClientListMailboxPermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientListMailboxPermissionsResponsePermissionsTypeDef",
    {
        "GranteeId": str,
        "GranteeType": Literal["GROUP", "USER"],
        "PermissionValues": List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    },
    total=False,
)


class ClientListMailboxPermissionsResponsePermissionsTypeDef(
    _ClientListMailboxPermissionsResponsePermissionsTypeDef
):
    """
    - *(dict) --*

      Permission granted to a user, group, or resource to access a certain aspect of another user,
      group, or resource mailbox.
      - **GranteeId** *(string) --*

        The identifier of the user, group, or resource to which the permissions are granted.
    """


_ClientListMailboxPermissionsResponseTypeDef = TypedDict(
    "_ClientListMailboxPermissionsResponseTypeDef",
    {"Permissions": List[ClientListMailboxPermissionsResponsePermissionsTypeDef], "NextToken": str},
    total=False,
)


class ClientListMailboxPermissionsResponseTypeDef(_ClientListMailboxPermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **Permissions** *(list) --*

        One page of the user, group, or resource mailbox permissions.
        - *(dict) --*

          Permission granted to a user, group, or resource to access a certain aspect of another
          user, group, or resource mailbox.
          - **GranteeId** *(string) --*

            The identifier of the user, group, or resource to which the permissions are granted.
    """


_ClientListOrganizationsResponseOrganizationSummariesTypeDef = TypedDict(
    "_ClientListOrganizationsResponseOrganizationSummariesTypeDef",
    {"OrganizationId": str, "Alias": str, "ErrorMessage": str, "State": str},
    total=False,
)


class ClientListOrganizationsResponseOrganizationSummariesTypeDef(
    _ClientListOrganizationsResponseOrganizationSummariesTypeDef
):
    """
    - *(dict) --*

      The representation of an organization.
      - **OrganizationId** *(string) --*

        The identifier associated with the organization.
    """


_ClientListOrganizationsResponseTypeDef = TypedDict(
    "_ClientListOrganizationsResponseTypeDef",
    {
        "OrganizationSummaries": List[ClientListOrganizationsResponseOrganizationSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListOrganizationsResponseTypeDef(_ClientListOrganizationsResponseTypeDef):
    """
    - *(dict) --*

      - **OrganizationSummaries** *(list) --*

        The overview of owned organizations presented as a list of organization summaries.
        - *(dict) --*

          The representation of an organization.
          - **OrganizationId** *(string) --*

            The identifier associated with the organization.
    """


_ClientListResourceDelegatesResponseDelegatesTypeDef = TypedDict(
    "_ClientListResourceDelegatesResponseDelegatesTypeDef",
    {"Id": str, "Type": Literal["GROUP", "USER"]},
    total=False,
)


class ClientListResourceDelegatesResponseDelegatesTypeDef(
    _ClientListResourceDelegatesResponseDelegatesTypeDef
):
    """
    - *(dict) --*

      The name of the attribute, which is one of the values defined in the UserAttribute
      enumeration.
      - **Id** *(string) --*

        The identifier for the user or group associated as the resource's delegate.
    """


_ClientListResourceDelegatesResponseTypeDef = TypedDict(
    "_ClientListResourceDelegatesResponseTypeDef",
    {"Delegates": List[ClientListResourceDelegatesResponseDelegatesTypeDef], "NextToken": str},
    total=False,
)


class ClientListResourceDelegatesResponseTypeDef(_ClientListResourceDelegatesResponseTypeDef):
    """
    - *(dict) --*

      - **Delegates** *(list) --*

        One page of the resource's delegates.
        - *(dict) --*

          The name of the attribute, which is one of the values defined in the UserAttribute
          enumeration.
          - **Id** *(string) --*

            The identifier for the user or group associated as the resource's delegate.
    """


_ClientListResourcesResponseResourcesTypeDef = TypedDict(
    "_ClientListResourcesResponseResourcesTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": Literal["ROOM", "EQUIPMENT"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientListResourcesResponseResourcesTypeDef(_ClientListResourcesResponseResourcesTypeDef):
    """
    - *(dict) --*

      The representation of a resource.
      - **Id** *(string) --*

        The identifier of the resource.
    """


_ClientListResourcesResponseTypeDef = TypedDict(
    "_ClientListResourcesResponseTypeDef",
    {"Resources": List[ClientListResourcesResponseResourcesTypeDef], "NextToken": str},
    total=False,
)


class ClientListResourcesResponseTypeDef(_ClientListResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **Resources** *(list) --*

        One page of the organization's resource representation.
        - *(dict) --*

          The representation of a resource.
          - **Id** *(string) --*

            The identifier of the resource.
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "UserRole": Literal["USER", "RESOURCE", "SYSTEM_USER"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    - *(dict) --*

      The representation of an Amazon WorkMail user.
      - **Id** *(string) --*

        The identifier of the user.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        The overview of users for an organization.
        - *(dict) --*

          The representation of an Amazon WorkMail user.
          - **Id** *(string) --*

            The identifier of the user.
    """


_ClientUpdateResourceBookingOptionsTypeDef = TypedDict(
    "_ClientUpdateResourceBookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)


class ClientUpdateResourceBookingOptionsTypeDef(_ClientUpdateResourceBookingOptionsTypeDef):
    """
    The resource's booking options to be updated.
    - **AutoAcceptRequests** *(boolean) --*

      The resource's ability to automatically reply to requests. If disabled, delegates must be
      associated to the resource.
    """


_ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAliasesPaginatePaginationConfigTypeDef(_ListAliasesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAliasesPaginateResponseTypeDef", {"Aliases": List[str]}, total=False
)


class ListAliasesPaginateResponseTypeDef(_ListAliasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Aliases** *(list) --*

        The entity's paginated aliases.
        - *(string) --*
    """


_ListGroupMembersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupMembersPaginatePaginationConfigTypeDef(
    _ListGroupMembersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupMembersPaginateResponseMembersTypeDef = TypedDict(
    "_ListGroupMembersPaginateResponseMembersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": Literal["GROUP", "USER"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ListGroupMembersPaginateResponseMembersTypeDef(
    _ListGroupMembersPaginateResponseMembersTypeDef
):
    """
    - *(dict) --*

      The representation of a user or group.
      - **Id** *(string) --*

        The identifier of the member.
    """


_ListGroupMembersPaginateResponseTypeDef = TypedDict(
    "_ListGroupMembersPaginateResponseTypeDef",
    {"Members": List[ListGroupMembersPaginateResponseMembersTypeDef]},
    total=False,
)


class ListGroupMembersPaginateResponseTypeDef(_ListGroupMembersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        The members associated to the group.
        - *(dict) --*

          The representation of a user or group.
          - **Id** *(string) --*

            The identifier of the member.
    """


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(_ListGroupsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    - *(dict) --*

      The representation of an Amazon WorkMail group.
      - **Id** *(string) --*

        The identifier of the group.
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {"Groups": List[ListGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The overview of groups for an organization.
        - *(dict) --*

          The representation of an Amazon WorkMail group.
          - **Id** *(string) --*

            The identifier of the group.
    """


_ListMailboxPermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMailboxPermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMailboxPermissionsPaginatePaginationConfigTypeDef(
    _ListMailboxPermissionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMailboxPermissionsPaginateResponsePermissionsTypeDef = TypedDict(
    "_ListMailboxPermissionsPaginateResponsePermissionsTypeDef",
    {
        "GranteeId": str,
        "GranteeType": Literal["GROUP", "USER"],
        "PermissionValues": List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    },
    total=False,
)


class ListMailboxPermissionsPaginateResponsePermissionsTypeDef(
    _ListMailboxPermissionsPaginateResponsePermissionsTypeDef
):
    """
    - *(dict) --*

      Permission granted to a user, group, or resource to access a certain aspect of another user,
      group, or resource mailbox.
      - **GranteeId** *(string) --*

        The identifier of the user, group, or resource to which the permissions are granted.
    """


_ListMailboxPermissionsPaginateResponseTypeDef = TypedDict(
    "_ListMailboxPermissionsPaginateResponseTypeDef",
    {"Permissions": List[ListMailboxPermissionsPaginateResponsePermissionsTypeDef]},
    total=False,
)


class ListMailboxPermissionsPaginateResponseTypeDef(_ListMailboxPermissionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Permissions** *(list) --*

        One page of the user, group, or resource mailbox permissions.
        - *(dict) --*

          Permission granted to a user, group, or resource to access a certain aspect of another
          user, group, or resource mailbox.
          - **GranteeId** *(string) --*

            The identifier of the user, group, or resource to which the permissions are granted.
    """


_ListOrganizationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOrganizationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOrganizationsPaginatePaginationConfigTypeDef(
    _ListOrganizationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOrganizationsPaginateResponseOrganizationSummariesTypeDef = TypedDict(
    "_ListOrganizationsPaginateResponseOrganizationSummariesTypeDef",
    {"OrganizationId": str, "Alias": str, "ErrorMessage": str, "State": str},
    total=False,
)


class ListOrganizationsPaginateResponseOrganizationSummariesTypeDef(
    _ListOrganizationsPaginateResponseOrganizationSummariesTypeDef
):
    """
    - *(dict) --*

      The representation of an organization.
      - **OrganizationId** *(string) --*

        The identifier associated with the organization.
    """


_ListOrganizationsPaginateResponseTypeDef = TypedDict(
    "_ListOrganizationsPaginateResponseTypeDef",
    {"OrganizationSummaries": List[ListOrganizationsPaginateResponseOrganizationSummariesTypeDef]},
    total=False,
)


class ListOrganizationsPaginateResponseTypeDef(_ListOrganizationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **OrganizationSummaries** *(list) --*

        The overview of owned organizations presented as a list of organization summaries.
        - *(dict) --*

          The representation of an organization.
          - **OrganizationId** *(string) --*

            The identifier associated with the organization.
    """


_ListResourceDelegatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceDelegatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceDelegatesPaginatePaginationConfigTypeDef(
    _ListResourceDelegatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourceDelegatesPaginateResponseDelegatesTypeDef = TypedDict(
    "_ListResourceDelegatesPaginateResponseDelegatesTypeDef",
    {"Id": str, "Type": Literal["GROUP", "USER"]},
    total=False,
)


class ListResourceDelegatesPaginateResponseDelegatesTypeDef(
    _ListResourceDelegatesPaginateResponseDelegatesTypeDef
):
    """
    - *(dict) --*

      The name of the attribute, which is one of the values defined in the UserAttribute
      enumeration.
      - **Id** *(string) --*

        The identifier for the user or group associated as the resource's delegate.
    """


_ListResourceDelegatesPaginateResponseTypeDef = TypedDict(
    "_ListResourceDelegatesPaginateResponseTypeDef",
    {"Delegates": List[ListResourceDelegatesPaginateResponseDelegatesTypeDef]},
    total=False,
)


class ListResourceDelegatesPaginateResponseTypeDef(_ListResourceDelegatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Delegates** *(list) --*

        One page of the resource's delegates.
        - *(dict) --*

          The name of the attribute, which is one of the values defined in the UserAttribute
          enumeration.
          - **Id** *(string) --*

            The identifier for the user or group associated as the resource's delegate.
    """


_ListResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourcesPaginatePaginationConfigTypeDef(_ListResourcesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourcesPaginateResponseResourcesTypeDef = TypedDict(
    "_ListResourcesPaginateResponseResourcesTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": Literal["ROOM", "EQUIPMENT"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ListResourcesPaginateResponseResourcesTypeDef(_ListResourcesPaginateResponseResourcesTypeDef):
    """
    - *(dict) --*

      The representation of a resource.
      - **Id** *(string) --*

        The identifier of the resource.
    """


_ListResourcesPaginateResponseTypeDef = TypedDict(
    "_ListResourcesPaginateResponseTypeDef",
    {"Resources": List[ListResourcesPaginateResponseResourcesTypeDef]},
    total=False,
)


class ListResourcesPaginateResponseTypeDef(_ListResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Resources** *(list) --*

        One page of the organization's resource representation.
        - *(dict) --*

          The representation of a resource.
          - **Id** *(string) --*

            The identifier of the resource.
    """


_ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersPaginatePaginationConfigTypeDef(_ListUsersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "UserRole": Literal["USER", "RESOURCE", "SYSTEM_USER"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class ListUsersPaginateResponseUsersTypeDef(_ListUsersPaginateResponseUsersTypeDef):
    """
    - *(dict) --*

      The representation of an Amazon WorkMail user.
      - **Id** *(string) --*

        The identifier of the user.
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef]},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        The overview of users for an organization.
        - *(dict) --*

          The representation of an Amazon WorkMail user.
          - **Id** *(string) --*

            The identifier of the user.
    """
