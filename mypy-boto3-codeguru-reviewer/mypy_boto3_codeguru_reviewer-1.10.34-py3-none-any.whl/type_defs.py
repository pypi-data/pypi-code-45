"Main interface for codeguru-reviewer service type defs"
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


ClientAssociateRepositoryRepositoryCodeCommitTypeDef = TypedDict(
    "ClientAssociateRepositoryRepositoryCodeCommitTypeDef", {"Name": str}
)

ClientAssociateRepositoryRepositoryTypeDef = TypedDict(
    "ClientAssociateRepositoryRepositoryTypeDef",
    {"CodeCommit": ClientAssociateRepositoryRepositoryCodeCommitTypeDef},
    total=False,
)

ClientAssociateRepositoryResponseRepositoryAssociationTypeDef = TypedDict(
    "ClientAssociateRepositoryResponseRepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
    },
    total=False,
)

ClientAssociateRepositoryResponseTypeDef = TypedDict(
    "ClientAssociateRepositoryResponseTypeDef",
    {"RepositoryAssociation": ClientAssociateRepositoryResponseRepositoryAssociationTypeDef},
    total=False,
)

ClientDescribeRepositoryAssociationResponseRepositoryAssociationTypeDef = TypedDict(
    "ClientDescribeRepositoryAssociationResponseRepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
    },
    total=False,
)

ClientDescribeRepositoryAssociationResponseTypeDef = TypedDict(
    "ClientDescribeRepositoryAssociationResponseTypeDef",
    {
        "RepositoryAssociation": ClientDescribeRepositoryAssociationResponseRepositoryAssociationTypeDef
    },
    total=False,
)

ClientDisassociateRepositoryResponseRepositoryAssociationTypeDef = TypedDict(
    "ClientDisassociateRepositoryResponseRepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
    },
    total=False,
)

ClientDisassociateRepositoryResponseTypeDef = TypedDict(
    "ClientDisassociateRepositoryResponseTypeDef",
    {"RepositoryAssociation": ClientDisassociateRepositoryResponseRepositoryAssociationTypeDef},
    total=False,
)

ClientListRepositoryAssociationsResponseRepositoryAssociationSummariesTypeDef = TypedDict(
    "ClientListRepositoryAssociationsResponseRepositoryAssociationSummariesTypeDef",
    {
        "AssociationArn": str,
        "LastUpdatedTimeStamp": datetime,
        "AssociationId": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
    },
    total=False,
)

ClientListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ClientListRepositoryAssociationsResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List[
            ClientListRepositoryAssociationsResponseRepositoryAssociationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListRepositoryAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListRepositoryAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRepositoryAssociationsPaginateResponseRepositoryAssociationSummariesTypeDef = TypedDict(
    "ListRepositoryAssociationsPaginateResponseRepositoryAssociationSummariesTypeDef",
    {
        "AssociationArn": str,
        "LastUpdatedTimeStamp": datetime,
        "AssociationId": str,
        "Name": str,
        "Owner": str,
        "ProviderType": Literal["CodeCommit", "GitHub"],
        "State": Literal["Associated", "Associating", "Failed", "Disassociating"],
    },
    total=False,
)

ListRepositoryAssociationsPaginateResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsPaginateResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List[
            ListRepositoryAssociationsPaginateResponseRepositoryAssociationSummariesTypeDef
        ]
    },
    total=False,
)
