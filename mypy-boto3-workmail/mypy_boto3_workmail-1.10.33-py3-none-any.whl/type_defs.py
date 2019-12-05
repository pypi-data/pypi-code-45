"Main interface for workmail service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef", {"GroupId": str}, total=False
)

ClientCreateResourceResponseTypeDef = TypedDict(
    "ClientCreateResourceResponseTypeDef", {"ResourceId": str}, total=False
)

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"UserId": str}, total=False
)

ClientDescribeGroupResponseTypeDef = TypedDict(
    "ClientDescribeGroupResponseTypeDef",
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

ClientDescribeOrganizationResponseTypeDef = TypedDict(
    "ClientDescribeOrganizationResponseTypeDef",
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

ClientDescribeResourceResponseBookingOptionsTypeDef = TypedDict(
    "ClientDescribeResourceResponseBookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)

ClientDescribeResourceResponseTypeDef = TypedDict(
    "ClientDescribeResourceResponseTypeDef",
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

ClientDescribeUserResponseTypeDef = TypedDict(
    "ClientDescribeUserResponseTypeDef",
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

ClientGetMailboxDetailsResponseTypeDef = TypedDict(
    "ClientGetMailboxDetailsResponseTypeDef",
    {"MailboxQuota": int, "MailboxSize": float},
    total=False,
)

ClientListAliasesResponseTypeDef = TypedDict(
    "ClientListAliasesResponseTypeDef", {"Aliases": List[str], "NextToken": str}, total=False
)

ClientListGroupMembersResponseMembersTypeDef = TypedDict(
    "ClientListGroupMembersResponseMembersTypeDef",
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

ClientListGroupMembersResponseTypeDef = TypedDict(
    "ClientListGroupMembersResponseTypeDef",
    {"Members": List[ClientListGroupMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)

ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsResponseGroupsTypeDef",
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

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientListMailboxPermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientListMailboxPermissionsResponsePermissionsTypeDef",
    {
        "GranteeId": str,
        "GranteeType": Literal["GROUP", "USER"],
        "PermissionValues": List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    },
    total=False,
)

ClientListMailboxPermissionsResponseTypeDef = TypedDict(
    "ClientListMailboxPermissionsResponseTypeDef",
    {"Permissions": List[ClientListMailboxPermissionsResponsePermissionsTypeDef], "NextToken": str},
    total=False,
)

ClientListOrganizationsResponseOrganizationSummariesTypeDef = TypedDict(
    "ClientListOrganizationsResponseOrganizationSummariesTypeDef",
    {"OrganizationId": str, "Alias": str, "ErrorMessage": str, "State": str},
    total=False,
)

ClientListOrganizationsResponseTypeDef = TypedDict(
    "ClientListOrganizationsResponseTypeDef",
    {
        "OrganizationSummaries": List[ClientListOrganizationsResponseOrganizationSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListResourceDelegatesResponseDelegatesTypeDef = TypedDict(
    "ClientListResourceDelegatesResponseDelegatesTypeDef",
    {"Id": str, "Type": Literal["GROUP", "USER"]},
    total=False,
)

ClientListResourceDelegatesResponseTypeDef = TypedDict(
    "ClientListResourceDelegatesResponseTypeDef",
    {"Delegates": List[ClientListResourceDelegatesResponseDelegatesTypeDef], "NextToken": str},
    total=False,
)

ClientListResourcesResponseResourcesTypeDef = TypedDict(
    "ClientListResourcesResponseResourcesTypeDef",
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

ClientListResourcesResponseTypeDef = TypedDict(
    "ClientListResourcesResponseTypeDef",
    {"Resources": List[ClientListResourcesResponseResourcesTypeDef], "NextToken": str},
    total=False,
)

ClientListUsersResponseUsersTypeDef = TypedDict(
    "ClientListUsersResponseUsersTypeDef",
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

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)

ClientUpdateResourceBookingOptionsTypeDef = TypedDict(
    "ClientUpdateResourceBookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)

ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAliasesPaginateResponseTypeDef = TypedDict(
    "ListAliasesPaginateResponseTypeDef", {"Aliases": List[str]}, total=False
)

ListGroupMembersPaginatePaginationConfigTypeDef = TypedDict(
    "ListGroupMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListGroupMembersPaginateResponseMembersTypeDef = TypedDict(
    "ListGroupMembersPaginateResponseMembersTypeDef",
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

ListGroupMembersPaginateResponseTypeDef = TypedDict(
    "ListGroupMembersPaginateResponseTypeDef",
    {"Members": List[ListGroupMembersPaginateResponseMembersTypeDef]},
    total=False,
)

ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "ListGroupsPaginateResponseGroupsTypeDef",
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

ListGroupsPaginateResponseTypeDef = TypedDict(
    "ListGroupsPaginateResponseTypeDef",
    {"Groups": List[ListGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)

ListMailboxPermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListMailboxPermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListMailboxPermissionsPaginateResponsePermissionsTypeDef = TypedDict(
    "ListMailboxPermissionsPaginateResponsePermissionsTypeDef",
    {
        "GranteeId": str,
        "GranteeType": Literal["GROUP", "USER"],
        "PermissionValues": List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    },
    total=False,
)

ListMailboxPermissionsPaginateResponseTypeDef = TypedDict(
    "ListMailboxPermissionsPaginateResponseTypeDef",
    {"Permissions": List[ListMailboxPermissionsPaginateResponsePermissionsTypeDef]},
    total=False,
)

ListOrganizationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListOrganizationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListOrganizationsPaginateResponseOrganizationSummariesTypeDef = TypedDict(
    "ListOrganizationsPaginateResponseOrganizationSummariesTypeDef",
    {"OrganizationId": str, "Alias": str, "ErrorMessage": str, "State": str},
    total=False,
)

ListOrganizationsPaginateResponseTypeDef = TypedDict(
    "ListOrganizationsPaginateResponseTypeDef",
    {"OrganizationSummaries": List[ListOrganizationsPaginateResponseOrganizationSummariesTypeDef]},
    total=False,
)

ListResourceDelegatesPaginatePaginationConfigTypeDef = TypedDict(
    "ListResourceDelegatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResourceDelegatesPaginateResponseDelegatesTypeDef = TypedDict(
    "ListResourceDelegatesPaginateResponseDelegatesTypeDef",
    {"Id": str, "Type": Literal["GROUP", "USER"]},
    total=False,
)

ListResourceDelegatesPaginateResponseTypeDef = TypedDict(
    "ListResourceDelegatesPaginateResponseTypeDef",
    {"Delegates": List[ListResourceDelegatesPaginateResponseDelegatesTypeDef]},
    total=False,
)

ListResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "ListResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResourcesPaginateResponseResourcesTypeDef = TypedDict(
    "ListResourcesPaginateResponseResourcesTypeDef",
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

ListResourcesPaginateResponseTypeDef = TypedDict(
    "ListResourcesPaginateResponseTypeDef",
    {"Resources": List[ListResourcesPaginateResponseResourcesTypeDef]},
    total=False,
)

ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "ListUsersPaginateResponseUsersTypeDef",
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

ListUsersPaginateResponseTypeDef = TypedDict(
    "ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef]},
    total=False,
)
