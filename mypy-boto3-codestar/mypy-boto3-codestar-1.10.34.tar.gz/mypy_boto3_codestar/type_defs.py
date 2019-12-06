"Main interface for codestar service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientAssociateTeamMemberResponseTypeDef = TypedDict(
    "ClientAssociateTeamMemberResponseTypeDef", {"clientRequestToken": str}, total=False
)

ClientCreateProjectResponseTypeDef = TypedDict(
    "ClientCreateProjectResponseTypeDef",
    {"id": str, "arn": str, "clientRequestToken": str, "projectTemplateId": str},
    total=False,
)

ClientCreateProjectSourceCodedestinationcodeCommitTypeDef = TypedDict(
    "ClientCreateProjectSourceCodedestinationcodeCommitTypeDef", {"name": str}, total=False
)

ClientCreateProjectSourceCodedestinationgitHubTypeDef = TypedDict(
    "ClientCreateProjectSourceCodedestinationgitHubTypeDef",
    {
        "name": str,
        "description": str,
        "type": str,
        "owner": str,
        "privateRepository": bool,
        "issuesEnabled": bool,
        "token": str,
    },
    total=False,
)

ClientCreateProjectSourceCodedestinationTypeDef = TypedDict(
    "ClientCreateProjectSourceCodedestinationTypeDef",
    {
        "codeCommit": ClientCreateProjectSourceCodedestinationcodeCommitTypeDef,
        "gitHub": ClientCreateProjectSourceCodedestinationgitHubTypeDef,
    },
    total=False,
)

ClientCreateProjectSourceCodesources3TypeDef = TypedDict(
    "ClientCreateProjectSourceCodesources3TypeDef",
    {"bucketName": str, "bucketKey": str},
    total=False,
)

ClientCreateProjectSourceCodesourceTypeDef = TypedDict(
    "ClientCreateProjectSourceCodesourceTypeDef",
    {"s3": ClientCreateProjectSourceCodesources3TypeDef},
)

_RequiredClientCreateProjectSourceCodeTypeDef = TypedDict(
    "_RequiredClientCreateProjectSourceCodeTypeDef",
    {"source": ClientCreateProjectSourceCodesourceTypeDef},
)
_OptionalClientCreateProjectSourceCodeTypeDef = TypedDict(
    "_OptionalClientCreateProjectSourceCodeTypeDef",
    {"destination": ClientCreateProjectSourceCodedestinationTypeDef},
    total=False,
)


class ClientCreateProjectSourceCodeTypeDef(
    _RequiredClientCreateProjectSourceCodeTypeDef, _OptionalClientCreateProjectSourceCodeTypeDef
):
    pass


ClientCreateProjectToolchainsources3TypeDef = TypedDict(
    "ClientCreateProjectToolchainsources3TypeDef",
    {"bucketName": str, "bucketKey": str},
    total=False,
)

ClientCreateProjectToolchainsourceTypeDef = TypedDict(
    "ClientCreateProjectToolchainsourceTypeDef", {"s3": ClientCreateProjectToolchainsources3TypeDef}
)

_RequiredClientCreateProjectToolchainTypeDef = TypedDict(
    "_RequiredClientCreateProjectToolchainTypeDef",
    {"source": ClientCreateProjectToolchainsourceTypeDef},
)
_OptionalClientCreateProjectToolchainTypeDef = TypedDict(
    "_OptionalClientCreateProjectToolchainTypeDef",
    {"roleArn": str, "stackParameters": Dict[str, str]},
    total=False,
)


class ClientCreateProjectToolchainTypeDef(
    _RequiredClientCreateProjectToolchainTypeDef, _OptionalClientCreateProjectToolchainTypeDef
):
    pass


ClientCreateUserProfileResponseTypeDef = TypedDict(
    "ClientCreateUserProfileResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)

ClientDeleteProjectResponseTypeDef = TypedDict(
    "ClientDeleteProjectResponseTypeDef", {"stackId": str, "projectArn": str}, total=False
)

ClientDeleteUserProfileResponseTypeDef = TypedDict(
    "ClientDeleteUserProfileResponseTypeDef", {"userArn": str}, total=False
)

ClientDescribeProjectResponsestatusTypeDef = TypedDict(
    "ClientDescribeProjectResponsestatusTypeDef", {"state": str, "reason": str}, total=False
)

ClientDescribeProjectResponseTypeDef = TypedDict(
    "ClientDescribeProjectResponseTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "description": str,
        "clientRequestToken": str,
        "createdTimeStamp": datetime,
        "stackId": str,
        "projectTemplateId": str,
        "status": ClientDescribeProjectResponsestatusTypeDef,
    },
    total=False,
)

ClientDescribeUserProfileResponseTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)

ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "ClientListProjectsResponseprojectsTypeDef", {"projectId": str, "projectArn": str}, total=False
)

ClientListProjectsResponseTypeDef = TypedDict(
    "ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)

ClientListResourcesResponseresourcesTypeDef = TypedDict(
    "ClientListResourcesResponseresourcesTypeDef", {"id": str}, total=False
)

ClientListResourcesResponseTypeDef = TypedDict(
    "ClientListResourcesResponseTypeDef",
    {"resources": List[ClientListResourcesResponseresourcesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForProjectResponseTypeDef = TypedDict(
    "ClientListTagsForProjectResponseTypeDef",
    {"tags": Dict[str, str], "nextToken": str},
    total=False,
)

ClientListTeamMembersResponseteamMembersTypeDef = TypedDict(
    "ClientListTeamMembersResponseteamMembersTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)

ClientListTeamMembersResponseTypeDef = TypedDict(
    "ClientListTeamMembersResponseTypeDef",
    {"teamMembers": List[ClientListTeamMembersResponseteamMembersTypeDef], "nextToken": str},
    total=False,
)

ClientListUserProfilesResponseuserProfilesTypeDef = TypedDict(
    "ClientListUserProfilesResponseuserProfilesTypeDef",
    {"userArn": str, "displayName": str, "emailAddress": str, "sshPublicKey": str},
    total=False,
)

ClientListUserProfilesResponseTypeDef = TypedDict(
    "ClientListUserProfilesResponseTypeDef",
    {"userProfiles": List[ClientListUserProfilesResponseuserProfilesTypeDef], "nextToken": str},
    total=False,
)

ClientTagProjectResponseTypeDef = TypedDict(
    "ClientTagProjectResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientUpdateTeamMemberResponseTypeDef = TypedDict(
    "ClientUpdateTeamMemberResponseTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)

ClientUpdateUserProfileResponseTypeDef = TypedDict(
    "ClientUpdateUserProfileResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)

ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "ListProjectsPaginateResponseprojectsTypeDef",
    {"projectId": str, "projectArn": str},
    total=False,
)

ListProjectsPaginateResponseTypeDef = TypedDict(
    "ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)

ListResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "ListResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResourcesPaginateResponseresourcesTypeDef = TypedDict(
    "ListResourcesPaginateResponseresourcesTypeDef", {"id": str}, total=False
)

ListResourcesPaginateResponseTypeDef = TypedDict(
    "ListResourcesPaginateResponseTypeDef",
    {"resources": List[ListResourcesPaginateResponseresourcesTypeDef], "NextToken": str},
    total=False,
)

ListTeamMembersPaginatePaginationConfigTypeDef = TypedDict(
    "ListTeamMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTeamMembersPaginateResponseteamMembersTypeDef = TypedDict(
    "ListTeamMembersPaginateResponseteamMembersTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)

ListTeamMembersPaginateResponseTypeDef = TypedDict(
    "ListTeamMembersPaginateResponseTypeDef",
    {"teamMembers": List[ListTeamMembersPaginateResponseteamMembersTypeDef], "NextToken": str},
    total=False,
)

ListUserProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "ListUserProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListUserProfilesPaginateResponseuserProfilesTypeDef = TypedDict(
    "ListUserProfilesPaginateResponseuserProfilesTypeDef",
    {"userArn": str, "displayName": str, "emailAddress": str, "sshPublicKey": str},
    total=False,
)

ListUserProfilesPaginateResponseTypeDef = TypedDict(
    "ListUserProfilesPaginateResponseTypeDef",
    {"userProfiles": List[ListUserProfilesPaginateResponseuserProfilesTypeDef], "NextToken": str},
    total=False,
)
