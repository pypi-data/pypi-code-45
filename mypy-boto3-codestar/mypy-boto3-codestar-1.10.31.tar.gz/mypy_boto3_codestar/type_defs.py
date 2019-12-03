"Main interface for codestar service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientAssociateTeamMemberResponseTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientCreateProjectSourceCodedestinationcodeCommitTypeDef",
    "ClientCreateProjectSourceCodedestinationgitHubTypeDef",
    "ClientCreateProjectSourceCodedestinationTypeDef",
    "ClientCreateProjectSourceCodesources3TypeDef",
    "ClientCreateProjectSourceCodesourceTypeDef",
    "ClientCreateProjectSourceCodeTypeDef",
    "ClientCreateProjectToolchainsources3TypeDef",
    "ClientCreateProjectToolchainsourceTypeDef",
    "ClientCreateProjectToolchainTypeDef",
    "ClientCreateUserProfileResponseTypeDef",
    "ClientDeleteProjectResponseTypeDef",
    "ClientDeleteUserProfileResponseTypeDef",
    "ClientDescribeProjectResponsestatusTypeDef",
    "ClientDescribeProjectResponseTypeDef",
    "ClientDescribeUserProfileResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListResourcesResponseresourcesTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientListTagsForProjectResponseTypeDef",
    "ClientListTeamMembersResponseteamMembersTypeDef",
    "ClientListTeamMembersResponseTypeDef",
    "ClientListUserProfilesResponseuserProfilesTypeDef",
    "ClientListUserProfilesResponseTypeDef",
    "ClientTagProjectResponseTypeDef",
    "ClientUpdateTeamMemberResponseTypeDef",
    "ClientUpdateUserProfileResponseTypeDef",
    "ListProjectsPaginatePaginationConfigTypeDef",
    "ListProjectsPaginateResponseprojectsTypeDef",
    "ListProjectsPaginateResponseTypeDef",
    "ListResourcesPaginatePaginationConfigTypeDef",
    "ListResourcesPaginateResponseresourcesTypeDef",
    "ListResourcesPaginateResponseTypeDef",
    "ListTeamMembersPaginatePaginationConfigTypeDef",
    "ListTeamMembersPaginateResponseteamMembersTypeDef",
    "ListTeamMembersPaginateResponseTypeDef",
    "ListUserProfilesPaginatePaginationConfigTypeDef",
    "ListUserProfilesPaginateResponseuserProfilesTypeDef",
    "ListUserProfilesPaginateResponseTypeDef",
)


_ClientAssociateTeamMemberResponseTypeDef = TypedDict(
    "_ClientAssociateTeamMemberResponseTypeDef", {"clientRequestToken": str}, total=False
)


class ClientAssociateTeamMemberResponseTypeDef(_ClientAssociateTeamMemberResponseTypeDef):
    """
    - *(dict) --*

      - **clientRequestToken** *(string) --*

        The user- or system-generated token from the initial request that can be used to repeat the
        request.
    """


_ClientCreateProjectResponseTypeDef = TypedDict(
    "_ClientCreateProjectResponseTypeDef",
    {"id": str, "arn": str, "clientRequestToken": str, "projectTemplateId": str},
    total=False,
)


class ClientCreateProjectResponseTypeDef(_ClientCreateProjectResponseTypeDef):
    """
    - *(dict) --*

      - **id** *(string) --*

        The ID of the project.
    """


_ClientCreateProjectSourceCodedestinationcodeCommitTypeDef = TypedDict(
    "_ClientCreateProjectSourceCodedestinationcodeCommitTypeDef", {"name": str}, total=False
)


class ClientCreateProjectSourceCodedestinationcodeCommitTypeDef(
    _ClientCreateProjectSourceCodedestinationcodeCommitTypeDef
):
    pass


_ClientCreateProjectSourceCodedestinationgitHubTypeDef = TypedDict(
    "_ClientCreateProjectSourceCodedestinationgitHubTypeDef",
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


class ClientCreateProjectSourceCodedestinationgitHubTypeDef(
    _ClientCreateProjectSourceCodedestinationgitHubTypeDef
):
    pass


_ClientCreateProjectSourceCodedestinationTypeDef = TypedDict(
    "_ClientCreateProjectSourceCodedestinationTypeDef",
    {
        "codeCommit": ClientCreateProjectSourceCodedestinationcodeCommitTypeDef,
        "gitHub": ClientCreateProjectSourceCodedestinationgitHubTypeDef,
    },
    total=False,
)


class ClientCreateProjectSourceCodedestinationTypeDef(
    _ClientCreateProjectSourceCodedestinationTypeDef
):
    pass


_ClientCreateProjectSourceCodesources3TypeDef = TypedDict(
    "_ClientCreateProjectSourceCodesources3TypeDef",
    {"bucketName": str, "bucketKey": str},
    total=False,
)


class ClientCreateProjectSourceCodesources3TypeDef(_ClientCreateProjectSourceCodesources3TypeDef):
    """
    - **s3** *(dict) --***[REQUIRED]**

      Information about the Amazon S3 location where the source code files provided with the project
      request are stored.
      - **bucketName** *(string) --*

        The Amazon S3 bucket name where the source code files provided with the project request are
        stored.
    """


_ClientCreateProjectSourceCodesourceTypeDef = TypedDict(
    "_ClientCreateProjectSourceCodesourceTypeDef",
    {"s3": ClientCreateProjectSourceCodesources3TypeDef},
)


class ClientCreateProjectSourceCodesourceTypeDef(_ClientCreateProjectSourceCodesourceTypeDef):
    """
    - **source** *(dict) --***[REQUIRED]**

      The location where the source code files provided with the project request are stored. AWS
      CodeStar retrieves the files during project creation.
      - **s3** *(dict) --***[REQUIRED]**

        Information about the Amazon S3 location where the source code files provided with the
        project request are stored.
        - **bucketName** *(string) --*

          The Amazon S3 bucket name where the source code files provided with the project request
          are stored.
    """


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
    """
    - *(dict) --*

      Location and destination information about the source code files provided with the project
      request. The source code is uploaded to the new project source repository after project
      creation.
      - **source** *(dict) --***[REQUIRED]**

        The location where the source code files provided with the project request are stored. AWS
        CodeStar retrieves the files during project creation.
        - **s3** *(dict) --***[REQUIRED]**

          Information about the Amazon S3 location where the source code files provided with the
          project request are stored.
          - **bucketName** *(string) --*

            The Amazon S3 bucket name where the source code files provided with the project request
            are stored.
    """


_ClientCreateProjectToolchainsources3TypeDef = TypedDict(
    "_ClientCreateProjectToolchainsources3TypeDef",
    {"bucketName": str, "bucketKey": str},
    total=False,
)


class ClientCreateProjectToolchainsources3TypeDef(_ClientCreateProjectToolchainsources3TypeDef):
    """
    - **s3** *(dict) --***[REQUIRED]**

      The Amazon S3 bucket where the toolchain template file provided with the project request is
      stored.
      - **bucketName** *(string) --*

        The Amazon S3 bucket name where the source code files provided with the project request are
        stored.
    """


_ClientCreateProjectToolchainsourceTypeDef = TypedDict(
    "_ClientCreateProjectToolchainsourceTypeDef",
    {"s3": ClientCreateProjectToolchainsources3TypeDef},
)


class ClientCreateProjectToolchainsourceTypeDef(_ClientCreateProjectToolchainsourceTypeDef):
    """
    - **source** *(dict) --***[REQUIRED]**

      The Amazon S3 location where the toolchain template file provided with the project request is
      stored. AWS CodeStar retrieves the file during project creation.
      - **s3** *(dict) --***[REQUIRED]**

        The Amazon S3 bucket where the toolchain template file provided with the project request is
        stored.
        - **bucketName** *(string) --*

          The Amazon S3 bucket name where the source code files provided with the project request
          are stored.
    """


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
    """
    The name of the toolchain template file submitted with the project request. If this parameter is
    specified, the request must also include the sourceCode parameter.
    - **source** *(dict) --***[REQUIRED]**

      The Amazon S3 location where the toolchain template file provided with the project request is
      stored. AWS CodeStar retrieves the file during project creation.
      - **s3** *(dict) --***[REQUIRED]**

        The Amazon S3 bucket where the toolchain template file provided with the project request is
        stored.
        - **bucketName** *(string) --*

          The Amazon S3 bucket name where the source code files provided with the project request
          are stored.
    """


_ClientCreateUserProfileResponseTypeDef = TypedDict(
    "_ClientCreateUserProfileResponseTypeDef",
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


class ClientCreateUserProfileResponseTypeDef(_ClientCreateUserProfileResponseTypeDef):
    """
    - *(dict) --*

      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user in IAM.
    """


_ClientDeleteProjectResponseTypeDef = TypedDict(
    "_ClientDeleteProjectResponseTypeDef", {"stackId": str, "projectArn": str}, total=False
)


class ClientDeleteProjectResponseTypeDef(_ClientDeleteProjectResponseTypeDef):
    """
    - *(dict) --*

      - **stackId** *(string) --*

        The ID of the primary stack in AWS CloudFormation that will be deleted as part of deleting
        the project and its resources.
    """


_ClientDeleteUserProfileResponseTypeDef = TypedDict(
    "_ClientDeleteUserProfileResponseTypeDef", {"userArn": str}, total=False
)


class ClientDeleteUserProfileResponseTypeDef(_ClientDeleteUserProfileResponseTypeDef):
    """
    - *(dict) --*

      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user deleted from AWS CodeStar.
    """


_ClientDescribeProjectResponsestatusTypeDef = TypedDict(
    "_ClientDescribeProjectResponsestatusTypeDef", {"state": str, "reason": str}, total=False
)


class ClientDescribeProjectResponsestatusTypeDef(_ClientDescribeProjectResponsestatusTypeDef):
    pass


_ClientDescribeProjectResponseTypeDef = TypedDict(
    "_ClientDescribeProjectResponseTypeDef",
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


class ClientDescribeProjectResponseTypeDef(_ClientDescribeProjectResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The display name for the project.
    """


_ClientDescribeUserProfileResponseTypeDef = TypedDict(
    "_ClientDescribeUserProfileResponseTypeDef",
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


class ClientDescribeUserProfileResponseTypeDef(_ClientDescribeUserProfileResponseTypeDef):
    """
    - *(dict) --*

      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user.
    """


_ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientListProjectsResponseprojectsTypeDef", {"projectId": str, "projectArn": str}, total=False
)


class ClientListProjectsResponseprojectsTypeDef(_ClientListProjectsResponseprojectsTypeDef):
    """
    - *(dict) --*

      Information about the metadata for a project.
      - **projectId** *(string) --*

        The ID of the project.
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    - *(dict) --*

      - **projects** *(list) --*

        A list of projects.
        - *(dict) --*

          Information about the metadata for a project.
          - **projectId** *(string) --*

            The ID of the project.
    """


_ClientListResourcesResponseresourcesTypeDef = TypedDict(
    "_ClientListResourcesResponseresourcesTypeDef", {"id": str}, total=False
)


class ClientListResourcesResponseresourcesTypeDef(_ClientListResourcesResponseresourcesTypeDef):
    """
    - *(dict) --*

      Information about a resource for a project.
      - **id** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ClientListResourcesResponseTypeDef = TypedDict(
    "_ClientListResourcesResponseTypeDef",
    {"resources": List[ClientListResourcesResponseresourcesTypeDef], "nextToken": str},
    total=False,
)


class ClientListResourcesResponseTypeDef(_ClientListResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **resources** *(list) --*

        An array of resources associated with the project.
        - *(dict) --*

          Information about a resource for a project.
          - **id** *(string) --*

            The Amazon Resource Name (ARN) of the resource.
    """


_ClientListTagsForProjectResponseTypeDef = TypedDict(
    "_ClientListTagsForProjectResponseTypeDef",
    {"tags": Dict[str, str], "nextToken": str},
    total=False,
)


class ClientListTagsForProjectResponseTypeDef(_ClientListTagsForProjectResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        The tags for the project.
        - *(string) --*

          - *(string) --*
    """


_ClientListTeamMembersResponseteamMembersTypeDef = TypedDict(
    "_ClientListTeamMembersResponseteamMembersTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)


class ClientListTeamMembersResponseteamMembersTypeDef(
    _ClientListTeamMembersResponseteamMembersTypeDef
):
    """
    - *(dict) --*

      Information about a team member in a project.
      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user in IAM.
    """


_ClientListTeamMembersResponseTypeDef = TypedDict(
    "_ClientListTeamMembersResponseTypeDef",
    {"teamMembers": List[ClientListTeamMembersResponseteamMembersTypeDef], "nextToken": str},
    total=False,
)


class ClientListTeamMembersResponseTypeDef(_ClientListTeamMembersResponseTypeDef):
    """
    - *(dict) --*

      - **teamMembers** *(list) --*

        A list of team member objects for the project.
        - *(dict) --*

          Information about a team member in a project.
          - **userArn** *(string) --*

            The Amazon Resource Name (ARN) of the user in IAM.
    """


_ClientListUserProfilesResponseuserProfilesTypeDef = TypedDict(
    "_ClientListUserProfilesResponseuserProfilesTypeDef",
    {"userArn": str, "displayName": str, "emailAddress": str, "sshPublicKey": str},
    total=False,
)


class ClientListUserProfilesResponseuserProfilesTypeDef(
    _ClientListUserProfilesResponseuserProfilesTypeDef
):
    """
    - *(dict) --*

      Information about a user's profile in AWS CodeStar.
      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user in IAM.
    """


_ClientListUserProfilesResponseTypeDef = TypedDict(
    "_ClientListUserProfilesResponseTypeDef",
    {"userProfiles": List[ClientListUserProfilesResponseuserProfilesTypeDef], "nextToken": str},
    total=False,
)


class ClientListUserProfilesResponseTypeDef(_ClientListUserProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **userProfiles** *(list) --*

        All the user profiles configured in AWS CodeStar for an AWS account.
        - *(dict) --*

          Information about a user's profile in AWS CodeStar.
          - **userArn** *(string) --*

            The Amazon Resource Name (ARN) of the user in IAM.
    """


_ClientTagProjectResponseTypeDef = TypedDict(
    "_ClientTagProjectResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientTagProjectResponseTypeDef(_ClientTagProjectResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        The tags for the project.
        - *(string) --*

          - *(string) --*
    """


_ClientUpdateTeamMemberResponseTypeDef = TypedDict(
    "_ClientUpdateTeamMemberResponseTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)


class ClientUpdateTeamMemberResponseTypeDef(_ClientUpdateTeamMemberResponseTypeDef):
    """
    - *(dict) --*

      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user whose team membership attributes were updated.
    """


_ClientUpdateUserProfileResponseTypeDef = TypedDict(
    "_ClientUpdateUserProfileResponseTypeDef",
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


class ClientUpdateUserProfileResponseTypeDef(_ClientUpdateUserProfileResponseTypeDef):
    """
    - *(dict) --*

      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user in IAM.
    """


_ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProjectsPaginatePaginationConfigTypeDef(_ListProjectsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "_ListProjectsPaginateResponseprojectsTypeDef",
    {"projectId": str, "projectArn": str},
    total=False,
)


class ListProjectsPaginateResponseprojectsTypeDef(_ListProjectsPaginateResponseprojectsTypeDef):
    """
    - *(dict) --*

      Information about the metadata for a project.
      - **projectId** *(string) --*

        The ID of the project.
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **projects** *(list) --*

        A list of projects.
        - *(dict) --*

          Information about the metadata for a project.
          - **projectId** *(string) --*

            The ID of the project.
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


_ListResourcesPaginateResponseresourcesTypeDef = TypedDict(
    "_ListResourcesPaginateResponseresourcesTypeDef", {"id": str}, total=False
)


class ListResourcesPaginateResponseresourcesTypeDef(_ListResourcesPaginateResponseresourcesTypeDef):
    """
    - *(dict) --*

      Information about a resource for a project.
      - **id** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ListResourcesPaginateResponseTypeDef = TypedDict(
    "_ListResourcesPaginateResponseTypeDef",
    {"resources": List[ListResourcesPaginateResponseresourcesTypeDef], "NextToken": str},
    total=False,
)


class ListResourcesPaginateResponseTypeDef(_ListResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **resources** *(list) --*

        An array of resources associated with the project.
        - *(dict) --*

          Information about a resource for a project.
          - **id** *(string) --*

            The Amazon Resource Name (ARN) of the resource.
    """


_ListTeamMembersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTeamMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTeamMembersPaginatePaginationConfigTypeDef(
    _ListTeamMembersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTeamMembersPaginateResponseteamMembersTypeDef = TypedDict(
    "_ListTeamMembersPaginateResponseteamMembersTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)


class ListTeamMembersPaginateResponseteamMembersTypeDef(
    _ListTeamMembersPaginateResponseteamMembersTypeDef
):
    """
    - *(dict) --*

      Information about a team member in a project.
      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user in IAM.
    """


_ListTeamMembersPaginateResponseTypeDef = TypedDict(
    "_ListTeamMembersPaginateResponseTypeDef",
    {"teamMembers": List[ListTeamMembersPaginateResponseteamMembersTypeDef], "NextToken": str},
    total=False,
)


class ListTeamMembersPaginateResponseTypeDef(_ListTeamMembersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **teamMembers** *(list) --*

        A list of team member objects for the project.
        - *(dict) --*

          Information about a team member in a project.
          - **userArn** *(string) --*

            The Amazon Resource Name (ARN) of the user in IAM.
    """


_ListUserProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserProfilesPaginatePaginationConfigTypeDef(
    _ListUserProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUserProfilesPaginateResponseuserProfilesTypeDef = TypedDict(
    "_ListUserProfilesPaginateResponseuserProfilesTypeDef",
    {"userArn": str, "displayName": str, "emailAddress": str, "sshPublicKey": str},
    total=False,
)


class ListUserProfilesPaginateResponseuserProfilesTypeDef(
    _ListUserProfilesPaginateResponseuserProfilesTypeDef
):
    """
    - *(dict) --*

      Information about a user's profile in AWS CodeStar.
      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user in IAM.
    """


_ListUserProfilesPaginateResponseTypeDef = TypedDict(
    "_ListUserProfilesPaginateResponseTypeDef",
    {"userProfiles": List[ListUserProfilesPaginateResponseuserProfilesTypeDef], "NextToken": str},
    total=False,
)


class ListUserProfilesPaginateResponseTypeDef(_ListUserProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **userProfiles** *(list) --*

        All the user profiles configured in AWS CodeStar for an AWS account.
        - *(dict) --*

          Information about a user's profile in AWS CodeStar.
          - **userArn** *(string) --*

            The Amazon Resource Name (ARN) of the user in IAM.
    """
