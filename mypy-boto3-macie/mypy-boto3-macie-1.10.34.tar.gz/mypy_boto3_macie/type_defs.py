"Main interface for macie service type defs"
from __future__ import annotations

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


ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)

ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ClientAssociateS3ResourcesResponseTypeDef = TypedDict(
    "ClientAssociateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)

ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef = TypedDict(
    "ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)

_RequiredClientAssociateS3ResourcesS3ResourcesTypeDef = TypedDict(
    "_RequiredClientAssociateS3ResourcesS3ResourcesTypeDef", {"bucketName": str}
)
_OptionalClientAssociateS3ResourcesS3ResourcesTypeDef = TypedDict(
    "_OptionalClientAssociateS3ResourcesS3ResourcesTypeDef",
    {
        "prefix": str,
        "classificationType": ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)


class ClientAssociateS3ResourcesS3ResourcesTypeDef(
    _RequiredClientAssociateS3ResourcesS3ResourcesTypeDef,
    _OptionalClientAssociateS3ResourcesS3ResourcesTypeDef,
):
    pass


_RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef = TypedDict(
    "_RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef", {"bucketName": str}
)
_OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef = TypedDict(
    "_OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef",
    {"prefix": str},
    total=False,
)


class ClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef(
    _RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef,
    _OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef,
):
    pass


ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)

ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ClientDisassociateS3ResourcesResponseTypeDef = TypedDict(
    "ClientDisassociateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)

ClientListMemberAccountsResponsememberAccountsTypeDef = TypedDict(
    "ClientListMemberAccountsResponsememberAccountsTypeDef", {"accountId": str}, total=False
)

ClientListMemberAccountsResponseTypeDef = TypedDict(
    "ClientListMemberAccountsResponseTypeDef",
    {
        "memberAccounts": List[ClientListMemberAccountsResponsememberAccountsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef = TypedDict(
    "ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)

ClientListS3ResourcesResponses3ResourcesTypeDef = TypedDict(
    "ClientListS3ResourcesResponses3ResourcesTypeDef",
    {
        "bucketName": str,
        "prefix": str,
        "classificationType": ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)

ClientListS3ResourcesResponseTypeDef = TypedDict(
    "ClientListS3ResourcesResponseTypeDef",
    {"s3Resources": List[ClientListS3ResourcesResponses3ResourcesTypeDef], "nextToken": str},
    total=False,
)

ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)

ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ClientUpdateS3ResourcesResponseTypeDef = TypedDict(
    "ClientUpdateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)

ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef = TypedDict(
    "ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)

_RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef", {"bucketName": str}
)
_OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef",
    {
        "prefix": str,
        "classificationTypeUpdate": ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateS3ResourcesS3ResourcesUpdateTypeDef(
    _RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef,
    _OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef,
):
    pass


ListMemberAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "ListMemberAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListMemberAccountsPaginateResponsememberAccountsTypeDef = TypedDict(
    "ListMemberAccountsPaginateResponsememberAccountsTypeDef", {"accountId": str}, total=False
)

ListMemberAccountsPaginateResponseTypeDef = TypedDict(
    "ListMemberAccountsPaginateResponseTypeDef",
    {
        "memberAccounts": List[ListMemberAccountsPaginateResponsememberAccountsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListS3ResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "ListS3ResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef = TypedDict(
    "ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)

ListS3ResourcesPaginateResponses3ResourcesTypeDef = TypedDict(
    "ListS3ResourcesPaginateResponses3ResourcesTypeDef",
    {
        "bucketName": str,
        "prefix": str,
        "classificationType": ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)

ListS3ResourcesPaginateResponseTypeDef = TypedDict(
    "ListS3ResourcesPaginateResponseTypeDef",
    {"s3Resources": List[ListS3ResourcesPaginateResponses3ResourcesTypeDef], "NextToken": str},
    total=False,
)
