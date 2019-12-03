"Main interface for workdocs service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientActivateUserResponseUserStorageStorageRuleTypeDef",
    "ClientActivateUserResponseUserStorageTypeDef",
    "ClientActivateUserResponseUserTypeDef",
    "ClientActivateUserResponseTypeDef",
    "ClientAddResourcePermissionsNotificationOptionsTypeDef",
    "ClientAddResourcePermissionsPrincipalsTypeDef",
    "ClientAddResourcePermissionsResponseShareResultsTypeDef",
    "ClientAddResourcePermissionsResponseTypeDef",
    "ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef",
    "ClientCreateCommentResponseCommentContributorStorageTypeDef",
    "ClientCreateCommentResponseCommentContributorTypeDef",
    "ClientCreateCommentResponseCommentTypeDef",
    "ClientCreateCommentResponseTypeDef",
    "ClientCreateFolderResponseMetadataTypeDef",
    "ClientCreateFolderResponseTypeDef",
    "ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef",
    "ClientCreateNotificationSubscriptionResponseTypeDef",
    "ClientCreateUserResponseUserStorageStorageRuleTypeDef",
    "ClientCreateUserResponseUserStorageTypeDef",
    "ClientCreateUserResponseUserTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserStorageRuleTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesTypeDef",
    "ClientDescribeActivitiesResponseTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorStorageTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorTypeDef",
    "ClientDescribeCommentsResponseCommentsTypeDef",
    "ClientDescribeCommentsResponseTypeDef",
    "ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef",
    "ClientDescribeDocumentVersionsResponseTypeDef",
    "ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef",
    "ClientDescribeFolderContentsResponseDocumentsTypeDef",
    "ClientDescribeFolderContentsResponseFoldersTypeDef",
    "ClientDescribeFolderContentsResponseTypeDef",
    "ClientDescribeGroupsResponseGroupsTypeDef",
    "ClientDescribeGroupsResponseTypeDef",
    "ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef",
    "ClientDescribeNotificationSubscriptionsResponseTypeDef",
    "ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef",
    "ClientDescribeResourcePermissionsResponsePrincipalsTypeDef",
    "ClientDescribeResourcePermissionsResponseTypeDef",
    "ClientDescribeRootFoldersResponseFoldersTypeDef",
    "ClientDescribeRootFoldersResponseTypeDef",
    "ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef",
    "ClientDescribeUsersResponseUsersStorageTypeDef",
    "ClientDescribeUsersResponseUsersTypeDef",
    "ClientDescribeUsersResponseTypeDef",
    "ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef",
    "ClientGetCurrentUserResponseUserStorageTypeDef",
    "ClientGetCurrentUserResponseUserTypeDef",
    "ClientGetCurrentUserResponseTypeDef",
    "ClientGetDocumentPathResponsePathComponentsTypeDef",
    "ClientGetDocumentPathResponsePathTypeDef",
    "ClientGetDocumentPathResponseTypeDef",
    "ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef",
    "ClientGetDocumentResponseMetadataTypeDef",
    "ClientGetDocumentResponseTypeDef",
    "ClientGetDocumentVersionResponseMetadataTypeDef",
    "ClientGetDocumentVersionResponseTypeDef",
    "ClientGetFolderPathResponsePathComponentsTypeDef",
    "ClientGetFolderPathResponsePathTypeDef",
    "ClientGetFolderPathResponseTypeDef",
    "ClientGetFolderResponseMetadataTypeDef",
    "ClientGetFolderResponseTypeDef",
    "ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef",
    "ClientGetResourcesResponseDocumentsTypeDef",
    "ClientGetResourcesResponseFoldersTypeDef",
    "ClientGetResourcesResponseTypeDef",
    "ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseTypeDef",
    "ClientUpdateUserResponseUserStorageStorageRuleTypeDef",
    "ClientUpdateUserResponseUserStorageTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ClientUpdateUserStorageRuleTypeDef",
    "DescribeActivitiesPaginatePaginationConfigTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef",
    "DescribeActivitiesPaginateResponseUserActivitiesTypeDef",
    "DescribeActivitiesPaginateResponseTypeDef",
    "DescribeCommentsPaginatePaginationConfigTypeDef",
    "DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef",
    "DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef",
    "DescribeCommentsPaginateResponseCommentsContributorTypeDef",
    "DescribeCommentsPaginateResponseCommentsTypeDef",
    "DescribeCommentsPaginateResponseTypeDef",
    "DescribeDocumentVersionsPaginatePaginationConfigTypeDef",
    "DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef",
    "DescribeDocumentVersionsPaginateResponseTypeDef",
    "DescribeFolderContentsPaginatePaginationConfigTypeDef",
    "DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef",
    "DescribeFolderContentsPaginateResponseDocumentsTypeDef",
    "DescribeFolderContentsPaginateResponseFoldersTypeDef",
    "DescribeFolderContentsPaginateResponseTypeDef",
    "DescribeGroupsPaginatePaginationConfigTypeDef",
    "DescribeGroupsPaginateResponseGroupsTypeDef",
    "DescribeGroupsPaginateResponseTypeDef",
    "DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef",
    "DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef",
    "DescribeNotificationSubscriptionsPaginateResponseTypeDef",
    "DescribeResourcePermissionsPaginatePaginationConfigTypeDef",
    "DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef",
    "DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef",
    "DescribeResourcePermissionsPaginateResponseTypeDef",
    "DescribeRootFoldersPaginatePaginationConfigTypeDef",
    "DescribeRootFoldersPaginateResponseFoldersTypeDef",
    "DescribeRootFoldersPaginateResponseTypeDef",
    "DescribeUsersPaginatePaginationConfigTypeDef",
    "DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef",
    "DescribeUsersPaginateResponseUsersStorageTypeDef",
    "DescribeUsersPaginateResponseUsersTypeDef",
    "DescribeUsersPaginateResponseTypeDef",
)


_ClientActivateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "_ClientActivateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientActivateUserResponseUserStorageStorageRuleTypeDef(
    _ClientActivateUserResponseUserStorageStorageRuleTypeDef
):
    pass


_ClientActivateUserResponseUserStorageTypeDef = TypedDict(
    "_ClientActivateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientActivateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientActivateUserResponseUserStorageTypeDef(_ClientActivateUserResponseUserStorageTypeDef):
    pass


_ClientActivateUserResponseUserTypeDef = TypedDict(
    "_ClientActivateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientActivateUserResponseUserStorageTypeDef,
    },
    total=False,
)


class ClientActivateUserResponseUserTypeDef(_ClientActivateUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The user information.
      - **Id** *(string) --*

        The ID of the user.
    """


_ClientActivateUserResponseTypeDef = TypedDict(
    "_ClientActivateUserResponseTypeDef",
    {"User": ClientActivateUserResponseUserTypeDef},
    total=False,
)


class ClientActivateUserResponseTypeDef(_ClientActivateUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The user information.
        - **Id** *(string) --*

          The ID of the user.
    """


_ClientAddResourcePermissionsNotificationOptionsTypeDef = TypedDict(
    "_ClientAddResourcePermissionsNotificationOptionsTypeDef",
    {"SendEmail": bool, "EmailMessage": str},
    total=False,
)


class ClientAddResourcePermissionsNotificationOptionsTypeDef(
    _ClientAddResourcePermissionsNotificationOptionsTypeDef
):
    """
    The notification options.
    - **SendEmail** *(boolean) --*

      Boolean value to indicate an email notification should be sent to the receipients.
    """


_RequiredClientAddResourcePermissionsPrincipalsTypeDef = TypedDict(
    "_RequiredClientAddResourcePermissionsPrincipalsTypeDef", {"Id": str}
)
_OptionalClientAddResourcePermissionsPrincipalsTypeDef = TypedDict(
    "_OptionalClientAddResourcePermissionsPrincipalsTypeDef",
    {
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
    },
    total=False,
)


class ClientAddResourcePermissionsPrincipalsTypeDef(
    _RequiredClientAddResourcePermissionsPrincipalsTypeDef,
    _OptionalClientAddResourcePermissionsPrincipalsTypeDef,
):
    """
    - *(dict) --*

      Describes the recipient type and ID, if available.
      - **Id** *(string) --***[REQUIRED]**

        The ID of the recipient.
    """


_ClientAddResourcePermissionsResponseShareResultsTypeDef = TypedDict(
    "_ClientAddResourcePermissionsResponseShareResultsTypeDef",
    {
        "PrincipalId": str,
        "InviteePrincipalId": str,
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Status": Literal["SUCCESS", "FAILURE"],
        "ShareId": str,
        "StatusMessage": str,
    },
    total=False,
)


class ClientAddResourcePermissionsResponseShareResultsTypeDef(
    _ClientAddResourcePermissionsResponseShareResultsTypeDef
):
    """
    - *(dict) --*

      Describes the share results of a resource.
      - **PrincipalId** *(string) --*

        The ID of the principal.
    """


_ClientAddResourcePermissionsResponseTypeDef = TypedDict(
    "_ClientAddResourcePermissionsResponseTypeDef",
    {"ShareResults": List[ClientAddResourcePermissionsResponseShareResultsTypeDef]},
    total=False,
)


class ClientAddResourcePermissionsResponseTypeDef(_ClientAddResourcePermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **ShareResults** *(list) --*

        The share results.
        - *(dict) --*

          Describes the share results of a resource.
          - **PrincipalId** *(string) --*

            The ID of the principal.
    """


_ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef = TypedDict(
    "_ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef(
    _ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef
):
    pass


_ClientCreateCommentResponseCommentContributorStorageTypeDef = TypedDict(
    "_ClientCreateCommentResponseCommentContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientCreateCommentResponseCommentContributorStorageTypeDef(
    _ClientCreateCommentResponseCommentContributorStorageTypeDef
):
    pass


_ClientCreateCommentResponseCommentContributorTypeDef = TypedDict(
    "_ClientCreateCommentResponseCommentContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientCreateCommentResponseCommentContributorStorageTypeDef,
    },
    total=False,
)


class ClientCreateCommentResponseCommentContributorTypeDef(
    _ClientCreateCommentResponseCommentContributorTypeDef
):
    pass


_ClientCreateCommentResponseCommentTypeDef = TypedDict(
    "_ClientCreateCommentResponseCommentTypeDef",
    {
        "CommentId": str,
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": ClientCreateCommentResponseCommentContributorTypeDef,
        "CreatedTimestamp": datetime,
        "Status": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "RecipientId": str,
    },
    total=False,
)


class ClientCreateCommentResponseCommentTypeDef(_ClientCreateCommentResponseCommentTypeDef):
    """
    - **Comment** *(dict) --*

      The comment that has been created.
      - **CommentId** *(string) --*

        The ID of the comment.
    """


_ClientCreateCommentResponseTypeDef = TypedDict(
    "_ClientCreateCommentResponseTypeDef",
    {"Comment": ClientCreateCommentResponseCommentTypeDef},
    total=False,
)


class ClientCreateCommentResponseTypeDef(_ClientCreateCommentResponseTypeDef):
    """
    - *(dict) --*

      - **Comment** *(dict) --*

        The comment that has been created.
        - **CommentId** *(string) --*

          The ID of the comment.
    """


_ClientCreateFolderResponseMetadataTypeDef = TypedDict(
    "_ClientCreateFolderResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientCreateFolderResponseMetadataTypeDef(_ClientCreateFolderResponseMetadataTypeDef):
    """
    - **Metadata** *(dict) --*

      The metadata of the folder.
      - **Id** *(string) --*

        The ID of the folder.
    """


_ClientCreateFolderResponseTypeDef = TypedDict(
    "_ClientCreateFolderResponseTypeDef",
    {"Metadata": ClientCreateFolderResponseMetadataTypeDef},
    total=False,
)


class ClientCreateFolderResponseTypeDef(_ClientCreateFolderResponseTypeDef):
    """
    - *(dict) --*

      - **Metadata** *(dict) --*

        The metadata of the folder.
        - **Id** *(string) --*

          The ID of the folder.
    """


_ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef = TypedDict(
    "_ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)


class ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef(
    _ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef
):
    """
    - **Subscription** *(dict) --*

      The subscription.
      - **SubscriptionId** *(string) --*

        The ID of the subscription.
    """


_ClientCreateNotificationSubscriptionResponseTypeDef = TypedDict(
    "_ClientCreateNotificationSubscriptionResponseTypeDef",
    {"Subscription": ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef},
    total=False,
)


class ClientCreateNotificationSubscriptionResponseTypeDef(
    _ClientCreateNotificationSubscriptionResponseTypeDef
):
    """
    - *(dict) --*

      - **Subscription** *(dict) --*

        The subscription.
        - **SubscriptionId** *(string) --*

          The ID of the subscription.
    """


_ClientCreateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "_ClientCreateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientCreateUserResponseUserStorageStorageRuleTypeDef(
    _ClientCreateUserResponseUserStorageStorageRuleTypeDef
):
    pass


_ClientCreateUserResponseUserStorageTypeDef = TypedDict(
    "_ClientCreateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientCreateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientCreateUserResponseUserStorageTypeDef(_ClientCreateUserResponseUserStorageTypeDef):
    pass


_ClientCreateUserResponseUserTypeDef = TypedDict(
    "_ClientCreateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientCreateUserResponseUserStorageTypeDef,
    },
    total=False,
)


class ClientCreateUserResponseUserTypeDef(_ClientCreateUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The user information.
      - **Id** *(string) --*

        The ID of the user.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"User": ClientCreateUserResponseUserTypeDef}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The user information.
        - **Id** *(string) --*

          The ID of the user.
    """


_ClientCreateUserStorageRuleTypeDef = TypedDict(
    "_ClientCreateUserStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientCreateUserStorageRuleTypeDef(_ClientCreateUserStorageRuleTypeDef):
    """
    The amount of storage for the user.
    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.
    """


_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef,
        "CreatedTimestamp": datetime,
        "CommentStatus": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "RecipientId": str,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef",
    {
        "Type": Literal["FOLDER", "DOCUMENT"],
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef",
    {
        "Users": List[ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef],
        "Groups": List[ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef],
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef",
    {
        "Type": Literal["FOLDER", "DOCUMENT"],
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef
):
    pass


_ClientDescribeActivitiesResponseUserActivitiesTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseUserActivitiesTypeDef",
    {
        "Type": Literal[
            "DOCUMENT_CHECKED_IN",
            "DOCUMENT_CHECKED_OUT",
            "DOCUMENT_RENAMED",
            "DOCUMENT_VERSION_UPLOADED",
            "DOCUMENT_VERSION_DELETED",
            "DOCUMENT_VERSION_VIEWED",
            "DOCUMENT_VERSION_DOWNLOADED",
            "DOCUMENT_RECYCLED",
            "DOCUMENT_RESTORED",
            "DOCUMENT_REVERTED",
            "DOCUMENT_SHARED",
            "DOCUMENT_UNSHARED",
            "DOCUMENT_SHARE_PERMISSION_CHANGED",
            "DOCUMENT_SHAREABLE_LINK_CREATED",
            "DOCUMENT_SHAREABLE_LINK_REMOVED",
            "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
            "DOCUMENT_MOVED",
            "DOCUMENT_COMMENT_ADDED",
            "DOCUMENT_COMMENT_DELETED",
            "DOCUMENT_ANNOTATION_ADDED",
            "DOCUMENT_ANNOTATION_DELETED",
            "FOLDER_CREATED",
            "FOLDER_DELETED",
            "FOLDER_RENAMED",
            "FOLDER_RECYCLED",
            "FOLDER_RESTORED",
            "FOLDER_SHARED",
            "FOLDER_UNSHARED",
            "FOLDER_SHARE_PERMISSION_CHANGED",
            "FOLDER_SHAREABLE_LINK_CREATED",
            "FOLDER_SHAREABLE_LINK_REMOVED",
            "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
            "FOLDER_MOVED",
        ],
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef,
        "Participants": ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef,
        "ResourceMetadata": ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef,
        "OriginalParent": ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef,
        "CommentMetadata": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef,
    },
    total=False,
)


class ClientDescribeActivitiesResponseUserActivitiesTypeDef(
    _ClientDescribeActivitiesResponseUserActivitiesTypeDef
):
    """
    - *(dict) --*

      Describes the activity information.
      - **Type** *(string) --*

        The activity type.
    """


_ClientDescribeActivitiesResponseTypeDef = TypedDict(
    "_ClientDescribeActivitiesResponseTypeDef",
    {"UserActivities": List[ClientDescribeActivitiesResponseUserActivitiesTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeActivitiesResponseTypeDef(_ClientDescribeActivitiesResponseTypeDef):
    """
    - *(dict) --*

      - **UserActivities** *(list) --*

        The list of activities for the specified user and time period.
        - *(dict) --*

          Describes the activity information.
          - **Type** *(string) --*

            The activity type.
    """


_ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef(
    _ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef
):
    pass


_ClientDescribeCommentsResponseCommentsContributorStorageTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseCommentsContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientDescribeCommentsResponseCommentsContributorStorageTypeDef(
    _ClientDescribeCommentsResponseCommentsContributorStorageTypeDef
):
    pass


_ClientDescribeCommentsResponseCommentsContributorTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseCommentsContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientDescribeCommentsResponseCommentsContributorStorageTypeDef,
    },
    total=False,
)


class ClientDescribeCommentsResponseCommentsContributorTypeDef(
    _ClientDescribeCommentsResponseCommentsContributorTypeDef
):
    pass


_ClientDescribeCommentsResponseCommentsTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseCommentsTypeDef",
    {
        "CommentId": str,
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": ClientDescribeCommentsResponseCommentsContributorTypeDef,
        "CreatedTimestamp": datetime,
        "Status": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "RecipientId": str,
    },
    total=False,
)


class ClientDescribeCommentsResponseCommentsTypeDef(_ClientDescribeCommentsResponseCommentsTypeDef):
    """
    - *(dict) --*

      Describes a comment.
      - **CommentId** *(string) --*

        The ID of the comment.
    """


_ClientDescribeCommentsResponseTypeDef = TypedDict(
    "_ClientDescribeCommentsResponseTypeDef",
    {"Comments": List[ClientDescribeCommentsResponseCommentsTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeCommentsResponseTypeDef(_ClientDescribeCommentsResponseTypeDef):
    """
    - *(dict) --*

      - **Comments** *(list) --*

        The list of comments for the specified document version.
        - *(dict) --*

          Describes a comment.
          - **CommentId** *(string) --*

            The ID of the comment.
    """


_ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef = TypedDict(
    "_ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef(
    _ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef
):
    """
    - *(dict) --*

      Describes a version of a document.
      - **Id** *(string) --*

        The ID of the version.
    """


_ClientDescribeDocumentVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List[ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeDocumentVersionsResponseTypeDef(_ClientDescribeDocumentVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentVersions** *(list) --*

        The document versions.
        - *(dict) --*

          Describes a version of a document.
          - **Id** *(string) --*

            The ID of the version.
    """


_ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "_ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef(
    _ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef
):
    pass


_ClientDescribeFolderContentsResponseDocumentsTypeDef = TypedDict(
    "_ClientDescribeFolderContentsResponseDocumentsTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)


class ClientDescribeFolderContentsResponseDocumentsTypeDef(
    _ClientDescribeFolderContentsResponseDocumentsTypeDef
):
    pass


_ClientDescribeFolderContentsResponseFoldersTypeDef = TypedDict(
    "_ClientDescribeFolderContentsResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientDescribeFolderContentsResponseFoldersTypeDef(
    _ClientDescribeFolderContentsResponseFoldersTypeDef
):
    """
    - *(dict) --*

      Describes a folder.
      - **Id** *(string) --*

        The ID of the folder.
    """


_ClientDescribeFolderContentsResponseTypeDef = TypedDict(
    "_ClientDescribeFolderContentsResponseTypeDef",
    {
        "Folders": List[ClientDescribeFolderContentsResponseFoldersTypeDef],
        "Documents": List[ClientDescribeFolderContentsResponseDocumentsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeFolderContentsResponseTypeDef(_ClientDescribeFolderContentsResponseTypeDef):
    """
    - *(dict) --*

      - **Folders** *(list) --*

        The subfolders in the specified folder.
        - *(dict) --*

          Describes a folder.
          - **Id** *(string) --*

            The ID of the folder.
    """


_ClientDescribeGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientDescribeGroupsResponseGroupsTypeDef", {"Id": str, "Name": str}, total=False
)


class ClientDescribeGroupsResponseGroupsTypeDef(_ClientDescribeGroupsResponseGroupsTypeDef):
    """
    - *(dict) --*

      Describes the metadata of a user group.
      - **Id** *(string) --*

        The ID of the user group.
    """


_ClientDescribeGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeGroupsResponseTypeDef",
    {"Groups": List[ClientDescribeGroupsResponseGroupsTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeGroupsResponseTypeDef(_ClientDescribeGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The list of groups.
        - *(dict) --*

          Describes the metadata of a user group.
          - **Id** *(string) --*

            The ID of the user group.
    """


_ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef = TypedDict(
    "_ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)


class ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef(
    _ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef
):
    """
    - *(dict) --*

      Describes a subscription.
      - **SubscriptionId** *(string) --*

        The ID of the subscription.
    """


_ClientDescribeNotificationSubscriptionsResponseTypeDef = TypedDict(
    "_ClientDescribeNotificationSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List[ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeNotificationSubscriptionsResponseTypeDef(
    _ClientDescribeNotificationSubscriptionsResponseTypeDef
):
    """
    - *(dict) --*

      - **Subscriptions** *(list) --*

        The subscriptions.
        - *(dict) --*

          Describes a subscription.
          - **SubscriptionId** *(string) --*

            The ID of the subscription.
    """


_ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef = TypedDict(
    "_ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef",
    {
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Type": Literal["DIRECT", "INHERITED"],
    },
    total=False,
)


class ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef(
    _ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef
):
    pass


_ClientDescribeResourcePermissionsResponsePrincipalsTypeDef = TypedDict(
    "_ClientDescribeResourcePermissionsResponsePrincipalsTypeDef",
    {
        "Id": str,
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Roles": List[ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef],
    },
    total=False,
)


class ClientDescribeResourcePermissionsResponsePrincipalsTypeDef(
    _ClientDescribeResourcePermissionsResponsePrincipalsTypeDef
):
    """
    - *(dict) --*

      Describes a resource.
      - **Id** *(string) --*

        The ID of the resource.
    """


_ClientDescribeResourcePermissionsResponseTypeDef = TypedDict(
    "_ClientDescribeResourcePermissionsResponseTypeDef",
    {"Principals": List[ClientDescribeResourcePermissionsResponsePrincipalsTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeResourcePermissionsResponseTypeDef(
    _ClientDescribeResourcePermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **Principals** *(list) --*

        The principals.
        - *(dict) --*

          Describes a resource.
          - **Id** *(string) --*

            The ID of the resource.
    """


_ClientDescribeRootFoldersResponseFoldersTypeDef = TypedDict(
    "_ClientDescribeRootFoldersResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientDescribeRootFoldersResponseFoldersTypeDef(
    _ClientDescribeRootFoldersResponseFoldersTypeDef
):
    """
    - *(dict) --*

      Describes a folder.
      - **Id** *(string) --*

        The ID of the folder.
    """


_ClientDescribeRootFoldersResponseTypeDef = TypedDict(
    "_ClientDescribeRootFoldersResponseTypeDef",
    {"Folders": List[ClientDescribeRootFoldersResponseFoldersTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeRootFoldersResponseTypeDef(_ClientDescribeRootFoldersResponseTypeDef):
    """
    - *(dict) --*

      - **Folders** *(list) --*

        The user's special folders.
        - *(dict) --*

          Describes a folder.
          - **Id** *(string) --*

            The ID of the folder.
    """


_ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef = TypedDict(
    "_ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef(
    _ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef
):
    pass


_ClientDescribeUsersResponseUsersStorageTypeDef = TypedDict(
    "_ClientDescribeUsersResponseUsersStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientDescribeUsersResponseUsersStorageTypeDef(
    _ClientDescribeUsersResponseUsersStorageTypeDef
):
    pass


_ClientDescribeUsersResponseUsersTypeDef = TypedDict(
    "_ClientDescribeUsersResponseUsersTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientDescribeUsersResponseUsersStorageTypeDef,
    },
    total=False,
)


class ClientDescribeUsersResponseUsersTypeDef(_ClientDescribeUsersResponseUsersTypeDef):
    """
    - *(dict) --*

      Describes a user.
      - **Id** *(string) --*

        The ID of the user.
    """


_ClientDescribeUsersResponseTypeDef = TypedDict(
    "_ClientDescribeUsersResponseTypeDef",
    {
        "Users": List[ClientDescribeUsersResponseUsersTypeDef],
        "TotalNumberOfUsers": int,
        "Marker": str,
    },
    total=False,
)


class ClientDescribeUsersResponseTypeDef(_ClientDescribeUsersResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        The users.
        - *(dict) --*

          Describes a user.
          - **Id** *(string) --*

            The ID of the user.
    """


_ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "_ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef(
    _ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef
):
    pass


_ClientGetCurrentUserResponseUserStorageTypeDef = TypedDict(
    "_ClientGetCurrentUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientGetCurrentUserResponseUserStorageTypeDef(
    _ClientGetCurrentUserResponseUserStorageTypeDef
):
    pass


_ClientGetCurrentUserResponseUserTypeDef = TypedDict(
    "_ClientGetCurrentUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientGetCurrentUserResponseUserStorageTypeDef,
    },
    total=False,
)


class ClientGetCurrentUserResponseUserTypeDef(_ClientGetCurrentUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      Metadata of the user.
      - **Id** *(string) --*

        The ID of the user.
    """


_ClientGetCurrentUserResponseTypeDef = TypedDict(
    "_ClientGetCurrentUserResponseTypeDef",
    {"User": ClientGetCurrentUserResponseUserTypeDef},
    total=False,
)


class ClientGetCurrentUserResponseTypeDef(_ClientGetCurrentUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        Metadata of the user.
        - **Id** *(string) --*

          The ID of the user.
    """


_ClientGetDocumentPathResponsePathComponentsTypeDef = TypedDict(
    "_ClientGetDocumentPathResponsePathComponentsTypeDef", {"Id": str, "Name": str}, total=False
)


class ClientGetDocumentPathResponsePathComponentsTypeDef(
    _ClientGetDocumentPathResponsePathComponentsTypeDef
):
    """
    - *(dict) --*

      Describes the resource path.
      - **Id** *(string) --*

        The ID of the resource path.
    """


_ClientGetDocumentPathResponsePathTypeDef = TypedDict(
    "_ClientGetDocumentPathResponsePathTypeDef",
    {"Components": List[ClientGetDocumentPathResponsePathComponentsTypeDef]},
    total=False,
)


class ClientGetDocumentPathResponsePathTypeDef(_ClientGetDocumentPathResponsePathTypeDef):
    """
    - **Path** *(dict) --*

      The path information.
      - **Components** *(list) --*

        The components of the resource path.
        - *(dict) --*

          Describes the resource path.
          - **Id** *(string) --*

            The ID of the resource path.
    """


_ClientGetDocumentPathResponseTypeDef = TypedDict(
    "_ClientGetDocumentPathResponseTypeDef",
    {"Path": ClientGetDocumentPathResponsePathTypeDef},
    total=False,
)


class ClientGetDocumentPathResponseTypeDef(_ClientGetDocumentPathResponseTypeDef):
    """
    - *(dict) --*

      - **Path** *(dict) --*

        The path information.
        - **Components** *(list) --*

          The components of the resource path.
          - *(dict) --*

            Describes the resource path.
            - **Id** *(string) --*

              The ID of the resource path.
    """


_ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef = TypedDict(
    "_ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef(
    _ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef
):
    pass


_ClientGetDocumentResponseMetadataTypeDef = TypedDict(
    "_ClientGetDocumentResponseMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)


class ClientGetDocumentResponseMetadataTypeDef(_ClientGetDocumentResponseMetadataTypeDef):
    """
    - **Metadata** *(dict) --*

      The metadata details of the document.
      - **Id** *(string) --*

        The ID of the document.
    """


_ClientGetDocumentResponseTypeDef = TypedDict(
    "_ClientGetDocumentResponseTypeDef",
    {"Metadata": ClientGetDocumentResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)


class ClientGetDocumentResponseTypeDef(_ClientGetDocumentResponseTypeDef):
    """
    - *(dict) --*

      - **Metadata** *(dict) --*

        The metadata details of the document.
        - **Id** *(string) --*

          The ID of the document.
    """


_ClientGetDocumentVersionResponseMetadataTypeDef = TypedDict(
    "_ClientGetDocumentVersionResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientGetDocumentVersionResponseMetadataTypeDef(
    _ClientGetDocumentVersionResponseMetadataTypeDef
):
    """
    - **Metadata** *(dict) --*

      The version metadata.
      - **Id** *(string) --*

        The ID of the version.
    """


_ClientGetDocumentVersionResponseTypeDef = TypedDict(
    "_ClientGetDocumentVersionResponseTypeDef",
    {"Metadata": ClientGetDocumentVersionResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)


class ClientGetDocumentVersionResponseTypeDef(_ClientGetDocumentVersionResponseTypeDef):
    """
    - *(dict) --*

      - **Metadata** *(dict) --*

        The version metadata.
        - **Id** *(string) --*

          The ID of the version.
    """


_ClientGetFolderPathResponsePathComponentsTypeDef = TypedDict(
    "_ClientGetFolderPathResponsePathComponentsTypeDef", {"Id": str, "Name": str}, total=False
)


class ClientGetFolderPathResponsePathComponentsTypeDef(
    _ClientGetFolderPathResponsePathComponentsTypeDef
):
    """
    - *(dict) --*

      Describes the resource path.
      - **Id** *(string) --*

        The ID of the resource path.
    """


_ClientGetFolderPathResponsePathTypeDef = TypedDict(
    "_ClientGetFolderPathResponsePathTypeDef",
    {"Components": List[ClientGetFolderPathResponsePathComponentsTypeDef]},
    total=False,
)


class ClientGetFolderPathResponsePathTypeDef(_ClientGetFolderPathResponsePathTypeDef):
    """
    - **Path** *(dict) --*

      The path information.
      - **Components** *(list) --*

        The components of the resource path.
        - *(dict) --*

          Describes the resource path.
          - **Id** *(string) --*

            The ID of the resource path.
    """


_ClientGetFolderPathResponseTypeDef = TypedDict(
    "_ClientGetFolderPathResponseTypeDef",
    {"Path": ClientGetFolderPathResponsePathTypeDef},
    total=False,
)


class ClientGetFolderPathResponseTypeDef(_ClientGetFolderPathResponseTypeDef):
    """
    - *(dict) --*

      - **Path** *(dict) --*

        The path information.
        - **Components** *(list) --*

          The components of the resource path.
          - *(dict) --*

            Describes the resource path.
            - **Id** *(string) --*

              The ID of the resource path.
    """


_ClientGetFolderResponseMetadataTypeDef = TypedDict(
    "_ClientGetFolderResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientGetFolderResponseMetadataTypeDef(_ClientGetFolderResponseMetadataTypeDef):
    """
    - **Metadata** *(dict) --*

      The metadata of the folder.
      - **Id** *(string) --*

        The ID of the folder.
    """


_ClientGetFolderResponseTypeDef = TypedDict(
    "_ClientGetFolderResponseTypeDef",
    {"Metadata": ClientGetFolderResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)


class ClientGetFolderResponseTypeDef(_ClientGetFolderResponseTypeDef):
    """
    - *(dict) --*

      - **Metadata** *(dict) --*

        The metadata of the folder.
        - **Id** *(string) --*

          The ID of the folder.
    """


_ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "_ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef(
    _ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef
):
    pass


_ClientGetResourcesResponseDocumentsTypeDef = TypedDict(
    "_ClientGetResourcesResponseDocumentsTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)


class ClientGetResourcesResponseDocumentsTypeDef(_ClientGetResourcesResponseDocumentsTypeDef):
    pass


_ClientGetResourcesResponseFoldersTypeDef = TypedDict(
    "_ClientGetResourcesResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class ClientGetResourcesResponseFoldersTypeDef(_ClientGetResourcesResponseFoldersTypeDef):
    """
    - *(dict) --*

      Describes a folder.
      - **Id** *(string) --*

        The ID of the folder.
    """


_ClientGetResourcesResponseTypeDef = TypedDict(
    "_ClientGetResourcesResponseTypeDef",
    {
        "Folders": List[ClientGetResourcesResponseFoldersTypeDef],
        "Documents": List[ClientGetResourcesResponseDocumentsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientGetResourcesResponseTypeDef(_ClientGetResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **Folders** *(list) --*

        The folders in the specified folder.
        - *(dict) --*

          Describes a folder.
          - **Id** *(string) --*

            The ID of the folder.
    """


_ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef = TypedDict(
    "_ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef(
    _ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef
):
    pass


_ClientInitiateDocumentVersionUploadResponseMetadataTypeDef = TypedDict(
    "_ClientInitiateDocumentVersionUploadResponseMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)


class ClientInitiateDocumentVersionUploadResponseMetadataTypeDef(
    _ClientInitiateDocumentVersionUploadResponseMetadataTypeDef
):
    """
    - **Metadata** *(dict) --*

      The document metadata.
      - **Id** *(string) --*

        The ID of the document.
    """


_ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef = TypedDict(
    "_ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef",
    {"UploadUrl": str, "SignedHeaders": Dict[str, str]},
    total=False,
)


class ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef(
    _ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef
):
    pass


_ClientInitiateDocumentVersionUploadResponseTypeDef = TypedDict(
    "_ClientInitiateDocumentVersionUploadResponseTypeDef",
    {
        "Metadata": ClientInitiateDocumentVersionUploadResponseMetadataTypeDef,
        "UploadMetadata": ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef,
    },
    total=False,
)


class ClientInitiateDocumentVersionUploadResponseTypeDef(
    _ClientInitiateDocumentVersionUploadResponseTypeDef
):
    """
    - *(dict) --*

      - **Metadata** *(dict) --*

        The document metadata.
        - **Id** *(string) --*

          The ID of the document.
    """


_ClientUpdateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientUpdateUserResponseUserStorageStorageRuleTypeDef(
    _ClientUpdateUserResponseUserStorageStorageRuleTypeDef
):
    pass


_ClientUpdateUserResponseUserStorageTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientUpdateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)


class ClientUpdateUserResponseUserStorageTypeDef(_ClientUpdateUserResponseUserStorageTypeDef):
    pass


_ClientUpdateUserResponseUserTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientUpdateUserResponseUserStorageTypeDef,
    },
    total=False,
)


class ClientUpdateUserResponseUserTypeDef(_ClientUpdateUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The user information.
      - **Id** *(string) --*

        The ID of the user.
    """


_ClientUpdateUserResponseTypeDef = TypedDict(
    "_ClientUpdateUserResponseTypeDef", {"User": ClientUpdateUserResponseUserTypeDef}, total=False
)


class ClientUpdateUserResponseTypeDef(_ClientUpdateUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The user information.
        - **Id** *(string) --*

          The ID of the user.
    """


_ClientUpdateUserStorageRuleTypeDef = TypedDict(
    "_ClientUpdateUserStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class ClientUpdateUserStorageRuleTypeDef(_ClientUpdateUserStorageRuleTypeDef):
    """
    The amount of storage for the user.
    - **StorageAllocatedInBytes** *(integer) --*

      The amount of storage allocated, in bytes.
    """


_DescribeActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeActivitiesPaginatePaginationConfigTypeDef(
    _DescribeActivitiesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef,
        "CreatedTimestamp": datetime,
        "CommentStatus": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "RecipientId": str,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef",
    {
        "Type": Literal["FOLDER", "DOCUMENT"],
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef",
    {
        "Users": List[DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef],
        "Groups": List[DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef],
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef",
    {
        "Type": Literal["FOLDER", "DOCUMENT"],
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef
):
    pass


_DescribeActivitiesPaginateResponseUserActivitiesTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseUserActivitiesTypeDef",
    {
        "Type": Literal[
            "DOCUMENT_CHECKED_IN",
            "DOCUMENT_CHECKED_OUT",
            "DOCUMENT_RENAMED",
            "DOCUMENT_VERSION_UPLOADED",
            "DOCUMENT_VERSION_DELETED",
            "DOCUMENT_VERSION_VIEWED",
            "DOCUMENT_VERSION_DOWNLOADED",
            "DOCUMENT_RECYCLED",
            "DOCUMENT_RESTORED",
            "DOCUMENT_REVERTED",
            "DOCUMENT_SHARED",
            "DOCUMENT_UNSHARED",
            "DOCUMENT_SHARE_PERMISSION_CHANGED",
            "DOCUMENT_SHAREABLE_LINK_CREATED",
            "DOCUMENT_SHAREABLE_LINK_REMOVED",
            "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
            "DOCUMENT_MOVED",
            "DOCUMENT_COMMENT_ADDED",
            "DOCUMENT_COMMENT_DELETED",
            "DOCUMENT_ANNOTATION_ADDED",
            "DOCUMENT_ANNOTATION_DELETED",
            "FOLDER_CREATED",
            "FOLDER_DELETED",
            "FOLDER_RENAMED",
            "FOLDER_RECYCLED",
            "FOLDER_RESTORED",
            "FOLDER_SHARED",
            "FOLDER_UNSHARED",
            "FOLDER_SHARE_PERMISSION_CHANGED",
            "FOLDER_SHAREABLE_LINK_CREATED",
            "FOLDER_SHAREABLE_LINK_REMOVED",
            "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
            "FOLDER_MOVED",
        ],
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef,
        "Participants": DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef,
        "ResourceMetadata": DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef,
        "OriginalParent": DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef,
        "CommentMetadata": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseUserActivitiesTypeDef(
    _DescribeActivitiesPaginateResponseUserActivitiesTypeDef
):
    """
    - *(dict) --*

      Describes the activity information.
      - **Type** *(string) --*

        The activity type.
    """


_DescribeActivitiesPaginateResponseTypeDef = TypedDict(
    "_DescribeActivitiesPaginateResponseTypeDef",
    {
        "UserActivities": List[DescribeActivitiesPaginateResponseUserActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeActivitiesPaginateResponseTypeDef(_DescribeActivitiesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **UserActivities** *(list) --*

        The list of activities for the specified user and time period.
        - *(dict) --*

          Describes the activity information.
          - **Type** *(string) --*

            The activity type.
    """


_DescribeCommentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCommentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCommentsPaginatePaginationConfigTypeDef(
    _DescribeCommentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef(
    _DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef
):
    pass


_DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef,
    },
    total=False,
)


class DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef(
    _DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef
):
    pass


_DescribeCommentsPaginateResponseCommentsContributorTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseCommentsContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef,
    },
    total=False,
)


class DescribeCommentsPaginateResponseCommentsContributorTypeDef(
    _DescribeCommentsPaginateResponseCommentsContributorTypeDef
):
    pass


_DescribeCommentsPaginateResponseCommentsTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseCommentsTypeDef",
    {
        "CommentId": str,
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": DescribeCommentsPaginateResponseCommentsContributorTypeDef,
        "CreatedTimestamp": datetime,
        "Status": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "RecipientId": str,
    },
    total=False,
)


class DescribeCommentsPaginateResponseCommentsTypeDef(
    _DescribeCommentsPaginateResponseCommentsTypeDef
):
    """
    - *(dict) --*

      Describes a comment.
      - **CommentId** *(string) --*

        The ID of the comment.
    """


_DescribeCommentsPaginateResponseTypeDef = TypedDict(
    "_DescribeCommentsPaginateResponseTypeDef",
    {"Comments": List[DescribeCommentsPaginateResponseCommentsTypeDef], "NextToken": str},
    total=False,
)


class DescribeCommentsPaginateResponseTypeDef(_DescribeCommentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Comments** *(list) --*

        The list of comments for the specified document version.
        - *(dict) --*

          Describes a comment.
          - **CommentId** *(string) --*

            The ID of the comment.
    """


_DescribeDocumentVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDocumentVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDocumentVersionsPaginatePaginationConfigTypeDef(
    _DescribeDocumentVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef = TypedDict(
    "_DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef(
    _DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef
):
    """
    - *(dict) --*

      Describes a version of a document.
      - **Id** *(string) --*

        The ID of the version.
    """


_DescribeDocumentVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeDocumentVersionsPaginateResponseTypeDef",
    {
        "DocumentVersions": List[DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDocumentVersionsPaginateResponseTypeDef(
    _DescribeDocumentVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DocumentVersions** *(list) --*

        The document versions.
        - *(dict) --*

          Describes a version of a document.
          - **Id** *(string) --*

            The ID of the version.
    """


_DescribeFolderContentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFolderContentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFolderContentsPaginatePaginationConfigTypeDef(
    _DescribeFolderContentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "_DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)


class DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef(
    _DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef
):
    pass


_DescribeFolderContentsPaginateResponseDocumentsTypeDef = TypedDict(
    "_DescribeFolderContentsPaginateResponseDocumentsTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)


class DescribeFolderContentsPaginateResponseDocumentsTypeDef(
    _DescribeFolderContentsPaginateResponseDocumentsTypeDef
):
    pass


_DescribeFolderContentsPaginateResponseFoldersTypeDef = TypedDict(
    "_DescribeFolderContentsPaginateResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class DescribeFolderContentsPaginateResponseFoldersTypeDef(
    _DescribeFolderContentsPaginateResponseFoldersTypeDef
):
    """
    - *(dict) --*

      Describes a folder.
      - **Id** *(string) --*

        The ID of the folder.
    """


_DescribeFolderContentsPaginateResponseTypeDef = TypedDict(
    "_DescribeFolderContentsPaginateResponseTypeDef",
    {
        "Folders": List[DescribeFolderContentsPaginateResponseFoldersTypeDef],
        "Documents": List[DescribeFolderContentsPaginateResponseDocumentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeFolderContentsPaginateResponseTypeDef(_DescribeFolderContentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Folders** *(list) --*

        The subfolders in the specified folder.
        - *(dict) --*

          Describes a folder.
          - **Id** *(string) --*

            The ID of the folder.
    """


_DescribeGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGroupsPaginatePaginationConfigTypeDef(_DescribeGroupsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_DescribeGroupsPaginateResponseGroupsTypeDef", {"Id": str, "Name": str}, total=False
)


class DescribeGroupsPaginateResponseGroupsTypeDef(_DescribeGroupsPaginateResponseGroupsTypeDef):
    """
    - *(dict) --*

      Describes the metadata of a user group.
      - **Id** *(string) --*

        The ID of the user group.
    """


_DescribeGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeGroupsPaginateResponseTypeDef",
    {"Groups": List[DescribeGroupsPaginateResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class DescribeGroupsPaginateResponseTypeDef(_DescribeGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The list of groups.
        - *(dict) --*

          Describes the metadata of a user group.
          - **Id** *(string) --*

            The ID of the user group.
    """


_DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef(
    _DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef = TypedDict(
    "_DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)


class DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef(
    _DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef
):
    """
    - *(dict) --*

      Describes a subscription.
      - **SubscriptionId** *(string) --*

        The ID of the subscription.
    """


_DescribeNotificationSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeNotificationSubscriptionsPaginateResponseTypeDef",
    {
        "Subscriptions": List[
            DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeNotificationSubscriptionsPaginateResponseTypeDef(
    _DescribeNotificationSubscriptionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Subscriptions** *(list) --*

        The subscriptions.
        - *(dict) --*

          Describes a subscription.
          - **SubscriptionId** *(string) --*

            The ID of the subscription.
    """


_DescribeResourcePermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeResourcePermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeResourcePermissionsPaginatePaginationConfigTypeDef(
    _DescribeResourcePermissionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef = TypedDict(
    "_DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef",
    {
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Type": Literal["DIRECT", "INHERITED"],
    },
    total=False,
)


class DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef(
    _DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef
):
    pass


_DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef = TypedDict(
    "_DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef",
    {
        "Id": str,
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Roles": List[DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef],
    },
    total=False,
)


class DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef(
    _DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef
):
    """
    - *(dict) --*

      Describes a resource.
      - **Id** *(string) --*

        The ID of the resource.
    """


_DescribeResourcePermissionsPaginateResponseTypeDef = TypedDict(
    "_DescribeResourcePermissionsPaginateResponseTypeDef",
    {
        "Principals": List[DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeResourcePermissionsPaginateResponseTypeDef(
    _DescribeResourcePermissionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Principals** *(list) --*

        The principals.
        - *(dict) --*

          Describes a resource.
          - **Id** *(string) --*

            The ID of the resource.
    """


_DescribeRootFoldersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRootFoldersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeRootFoldersPaginatePaginationConfigTypeDef(
    _DescribeRootFoldersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeRootFoldersPaginateResponseFoldersTypeDef = TypedDict(
    "_DescribeRootFoldersPaginateResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)


class DescribeRootFoldersPaginateResponseFoldersTypeDef(
    _DescribeRootFoldersPaginateResponseFoldersTypeDef
):
    """
    - *(dict) --*

      Describes a folder.
      - **Id** *(string) --*

        The ID of the folder.
    """


_DescribeRootFoldersPaginateResponseTypeDef = TypedDict(
    "_DescribeRootFoldersPaginateResponseTypeDef",
    {"Folders": List[DescribeRootFoldersPaginateResponseFoldersTypeDef], "NextToken": str},
    total=False,
)


class DescribeRootFoldersPaginateResponseTypeDef(_DescribeRootFoldersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Folders** *(list) --*

        The user's special folders.
        - *(dict) --*

          Describes a folder.
          - **Id** *(string) --*

            The ID of the folder.
    """


_DescribeUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeUsersPaginatePaginationConfigTypeDef(_DescribeUsersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)


class DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef(
    _DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef
):
    pass


_DescribeUsersPaginateResponseUsersStorageTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseUsersStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef,
    },
    total=False,
)


class DescribeUsersPaginateResponseUsersStorageTypeDef(
    _DescribeUsersPaginateResponseUsersStorageTypeDef
):
    pass


_DescribeUsersPaginateResponseUsersTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseUsersTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": DescribeUsersPaginateResponseUsersStorageTypeDef,
    },
    total=False,
)


class DescribeUsersPaginateResponseUsersTypeDef(_DescribeUsersPaginateResponseUsersTypeDef):
    """
    - *(dict) --*

      Describes a user.
      - **Id** *(string) --*

        The ID of the user.
    """


_DescribeUsersPaginateResponseTypeDef = TypedDict(
    "_DescribeUsersPaginateResponseTypeDef",
    {
        "Users": List[DescribeUsersPaginateResponseUsersTypeDef],
        "TotalNumberOfUsers": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeUsersPaginateResponseTypeDef(_DescribeUsersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Users** *(list) --*

        The users.
        - *(dict) --*

          Describes a user.
          - **Id** *(string) --*

            The ID of the user.
    """
