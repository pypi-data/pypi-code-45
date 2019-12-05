"Main interface for sso service type defs"
from __future__ import annotations

import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGetRoleCredentialsResponseroleCredentialsTypeDef = TypedDict(
    "ClientGetRoleCredentialsResponseroleCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str, "expiration": int},
    total=False,
)

ClientGetRoleCredentialsResponseTypeDef = TypedDict(
    "ClientGetRoleCredentialsResponseTypeDef",
    {"roleCredentials": ClientGetRoleCredentialsResponseroleCredentialsTypeDef},
    total=False,
)

ClientListAccountRolesResponseroleListTypeDef = TypedDict(
    "ClientListAccountRolesResponseroleListTypeDef",
    {"roleName": str, "accountId": str},
    total=False,
)

ClientListAccountRolesResponseTypeDef = TypedDict(
    "ClientListAccountRolesResponseTypeDef",
    {"nextToken": str, "roleList": List[ClientListAccountRolesResponseroleListTypeDef]},
    total=False,
)

ClientListAccountsResponseaccountListTypeDef = TypedDict(
    "ClientListAccountsResponseaccountListTypeDef",
    {"accountId": str, "accountName": str, "emailAddress": str},
    total=False,
)

ClientListAccountsResponseTypeDef = TypedDict(
    "ClientListAccountsResponseTypeDef",
    {"nextToken": str, "accountList": List[ClientListAccountsResponseaccountListTypeDef]},
    total=False,
)

ListAccountRolesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAccountRolesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAccountRolesPaginateResponseroleListTypeDef = TypedDict(
    "ListAccountRolesPaginateResponseroleListTypeDef",
    {"roleName": str, "accountId": str},
    total=False,
)

ListAccountRolesPaginateResponseTypeDef = TypedDict(
    "ListAccountRolesPaginateResponseTypeDef",
    {"roleList": List[ListAccountRolesPaginateResponseroleListTypeDef], "NextToken": str},
    total=False,
)

ListAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAccountsPaginateResponseaccountListTypeDef = TypedDict(
    "ListAccountsPaginateResponseaccountListTypeDef",
    {"accountId": str, "accountName": str, "emailAddress": str},
    total=False,
)

ListAccountsPaginateResponseTypeDef = TypedDict(
    "ListAccountsPaginateResponseTypeDef",
    {"accountList": List[ListAccountsPaginateResponseaccountListTypeDef], "NextToken": str},
    total=False,
)
