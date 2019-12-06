"Main interface for workdocs service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientActivateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "ClientActivateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientActivateUserResponseUserStorageTypeDef = TypedDict(
    "ClientActivateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientActivateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientActivateUserResponseUserTypeDef = TypedDict(
    "ClientActivateUserResponseUserTypeDef",
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

ClientActivateUserResponseTypeDef = TypedDict(
    "ClientActivateUserResponseTypeDef",
    {"User": ClientActivateUserResponseUserTypeDef},
    total=False,
)

ClientAddResourcePermissionsNotificationOptionsTypeDef = TypedDict(
    "ClientAddResourcePermissionsNotificationOptionsTypeDef",
    {"SendEmail": bool, "EmailMessage": str},
    total=False,
)

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
    pass


ClientAddResourcePermissionsResponseShareResultsTypeDef = TypedDict(
    "ClientAddResourcePermissionsResponseShareResultsTypeDef",
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

ClientAddResourcePermissionsResponseTypeDef = TypedDict(
    "ClientAddResourcePermissionsResponseTypeDef",
    {"ShareResults": List[ClientAddResourcePermissionsResponseShareResultsTypeDef]},
    total=False,
)

ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef = TypedDict(
    "ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientCreateCommentResponseCommentContributorStorageTypeDef = TypedDict(
    "ClientCreateCommentResponseCommentContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientCreateCommentResponseCommentContributorTypeDef = TypedDict(
    "ClientCreateCommentResponseCommentContributorTypeDef",
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

ClientCreateCommentResponseCommentTypeDef = TypedDict(
    "ClientCreateCommentResponseCommentTypeDef",
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

ClientCreateCommentResponseTypeDef = TypedDict(
    "ClientCreateCommentResponseTypeDef",
    {"Comment": ClientCreateCommentResponseCommentTypeDef},
    total=False,
)

ClientCreateFolderResponseMetadataTypeDef = TypedDict(
    "ClientCreateFolderResponseMetadataTypeDef",
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

ClientCreateFolderResponseTypeDef = TypedDict(
    "ClientCreateFolderResponseTypeDef",
    {"Metadata": ClientCreateFolderResponseMetadataTypeDef},
    total=False,
)

ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef = TypedDict(
    "ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)

ClientCreateNotificationSubscriptionResponseTypeDef = TypedDict(
    "ClientCreateNotificationSubscriptionResponseTypeDef",
    {"Subscription": ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef},
    total=False,
)

ClientCreateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "ClientCreateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientCreateUserResponseUserStorageTypeDef = TypedDict(
    "ClientCreateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientCreateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientCreateUserResponseUserTypeDef = TypedDict(
    "ClientCreateUserResponseUserTypeDef",
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

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"User": ClientCreateUserResponseUserTypeDef}, total=False
)

ClientCreateUserStorageRuleTypeDef = TypedDict(
    "ClientCreateUserStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef",
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

ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef,
        "CreatedTimestamp": datetime,
        "CommentStatus": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "RecipientId": str,
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef",
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

ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef",
    {
        "Users": List[ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef],
        "Groups": List[ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef],
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef",
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

ClientDescribeActivitiesResponseUserActivitiesTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesTypeDef",
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

ClientDescribeActivitiesResponseTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseTypeDef",
    {"UserActivities": List[ClientDescribeActivitiesResponseUserActivitiesTypeDef], "Marker": str},
    total=False,
)

ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef = TypedDict(
    "ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientDescribeCommentsResponseCommentsContributorStorageTypeDef = TypedDict(
    "ClientDescribeCommentsResponseCommentsContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientDescribeCommentsResponseCommentsContributorTypeDef = TypedDict(
    "ClientDescribeCommentsResponseCommentsContributorTypeDef",
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

ClientDescribeCommentsResponseCommentsTypeDef = TypedDict(
    "ClientDescribeCommentsResponseCommentsTypeDef",
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

ClientDescribeCommentsResponseTypeDef = TypedDict(
    "ClientDescribeCommentsResponseTypeDef",
    {"Comments": List[ClientDescribeCommentsResponseCommentsTypeDef], "Marker": str},
    total=False,
)

ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef = TypedDict(
    "ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef",
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

ClientDescribeDocumentVersionsResponseTypeDef = TypedDict(
    "ClientDescribeDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List[ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef",
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

ClientDescribeFolderContentsResponseDocumentsTypeDef = TypedDict(
    "ClientDescribeFolderContentsResponseDocumentsTypeDef",
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

ClientDescribeFolderContentsResponseFoldersTypeDef = TypedDict(
    "ClientDescribeFolderContentsResponseFoldersTypeDef",
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

ClientDescribeFolderContentsResponseTypeDef = TypedDict(
    "ClientDescribeFolderContentsResponseTypeDef",
    {
        "Folders": List[ClientDescribeFolderContentsResponseFoldersTypeDef],
        "Documents": List[ClientDescribeFolderContentsResponseDocumentsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeGroupsResponseGroupsTypeDef = TypedDict(
    "ClientDescribeGroupsResponseGroupsTypeDef", {"Id": str, "Name": str}, total=False
)

ClientDescribeGroupsResponseTypeDef = TypedDict(
    "ClientDescribeGroupsResponseTypeDef",
    {"Groups": List[ClientDescribeGroupsResponseGroupsTypeDef], "Marker": str},
    total=False,
)

ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef = TypedDict(
    "ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)

ClientDescribeNotificationSubscriptionsResponseTypeDef = TypedDict(
    "ClientDescribeNotificationSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List[ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef = TypedDict(
    "ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef",
    {
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Type": Literal["DIRECT", "INHERITED"],
    },
    total=False,
)

ClientDescribeResourcePermissionsResponsePrincipalsTypeDef = TypedDict(
    "ClientDescribeResourcePermissionsResponsePrincipalsTypeDef",
    {
        "Id": str,
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Roles": List[ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef],
    },
    total=False,
)

ClientDescribeResourcePermissionsResponseTypeDef = TypedDict(
    "ClientDescribeResourcePermissionsResponseTypeDef",
    {"Principals": List[ClientDescribeResourcePermissionsResponsePrincipalsTypeDef], "Marker": str},
    total=False,
)

ClientDescribeRootFoldersResponseFoldersTypeDef = TypedDict(
    "ClientDescribeRootFoldersResponseFoldersTypeDef",
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

ClientDescribeRootFoldersResponseTypeDef = TypedDict(
    "ClientDescribeRootFoldersResponseTypeDef",
    {"Folders": List[ClientDescribeRootFoldersResponseFoldersTypeDef], "Marker": str},
    total=False,
)

ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef = TypedDict(
    "ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientDescribeUsersResponseUsersStorageTypeDef = TypedDict(
    "ClientDescribeUsersResponseUsersStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientDescribeUsersResponseUsersTypeDef = TypedDict(
    "ClientDescribeUsersResponseUsersTypeDef",
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

ClientDescribeUsersResponseTypeDef = TypedDict(
    "ClientDescribeUsersResponseTypeDef",
    {
        "Users": List[ClientDescribeUsersResponseUsersTypeDef],
        "TotalNumberOfUsers": int,
        "Marker": str,
    },
    total=False,
)

ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientGetCurrentUserResponseUserStorageTypeDef = TypedDict(
    "ClientGetCurrentUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientGetCurrentUserResponseUserTypeDef = TypedDict(
    "ClientGetCurrentUserResponseUserTypeDef",
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

ClientGetCurrentUserResponseTypeDef = TypedDict(
    "ClientGetCurrentUserResponseTypeDef",
    {"User": ClientGetCurrentUserResponseUserTypeDef},
    total=False,
)

ClientGetDocumentPathResponsePathComponentsTypeDef = TypedDict(
    "ClientGetDocumentPathResponsePathComponentsTypeDef", {"Id": str, "Name": str}, total=False
)

ClientGetDocumentPathResponsePathTypeDef = TypedDict(
    "ClientGetDocumentPathResponsePathTypeDef",
    {"Components": List[ClientGetDocumentPathResponsePathComponentsTypeDef]},
    total=False,
)

ClientGetDocumentPathResponseTypeDef = TypedDict(
    "ClientGetDocumentPathResponseTypeDef",
    {"Path": ClientGetDocumentPathResponsePathTypeDef},
    total=False,
)

ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef = TypedDict(
    "ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef",
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

ClientGetDocumentResponseMetadataTypeDef = TypedDict(
    "ClientGetDocumentResponseMetadataTypeDef",
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

ClientGetDocumentResponseTypeDef = TypedDict(
    "ClientGetDocumentResponseTypeDef",
    {"Metadata": ClientGetDocumentResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)

ClientGetDocumentVersionResponseMetadataTypeDef = TypedDict(
    "ClientGetDocumentVersionResponseMetadataTypeDef",
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

ClientGetDocumentVersionResponseTypeDef = TypedDict(
    "ClientGetDocumentVersionResponseTypeDef",
    {"Metadata": ClientGetDocumentVersionResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)

ClientGetFolderPathResponsePathComponentsTypeDef = TypedDict(
    "ClientGetFolderPathResponsePathComponentsTypeDef", {"Id": str, "Name": str}, total=False
)

ClientGetFolderPathResponsePathTypeDef = TypedDict(
    "ClientGetFolderPathResponsePathTypeDef",
    {"Components": List[ClientGetFolderPathResponsePathComponentsTypeDef]},
    total=False,
)

ClientGetFolderPathResponseTypeDef = TypedDict(
    "ClientGetFolderPathResponseTypeDef",
    {"Path": ClientGetFolderPathResponsePathTypeDef},
    total=False,
)

ClientGetFolderResponseMetadataTypeDef = TypedDict(
    "ClientGetFolderResponseMetadataTypeDef",
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

ClientGetFolderResponseTypeDef = TypedDict(
    "ClientGetFolderResponseTypeDef",
    {"Metadata": ClientGetFolderResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)

ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef",
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

ClientGetResourcesResponseDocumentsTypeDef = TypedDict(
    "ClientGetResourcesResponseDocumentsTypeDef",
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

ClientGetResourcesResponseFoldersTypeDef = TypedDict(
    "ClientGetResourcesResponseFoldersTypeDef",
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

ClientGetResourcesResponseTypeDef = TypedDict(
    "ClientGetResourcesResponseTypeDef",
    {
        "Folders": List[ClientGetResourcesResponseFoldersTypeDef],
        "Documents": List[ClientGetResourcesResponseDocumentsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef = TypedDict(
    "ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef",
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

ClientInitiateDocumentVersionUploadResponseMetadataTypeDef = TypedDict(
    "ClientInitiateDocumentVersionUploadResponseMetadataTypeDef",
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

ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef = TypedDict(
    "ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef",
    {"UploadUrl": str, "SignedHeaders": Dict[str, str]},
    total=False,
)

ClientInitiateDocumentVersionUploadResponseTypeDef = TypedDict(
    "ClientInitiateDocumentVersionUploadResponseTypeDef",
    {
        "Metadata": ClientInitiateDocumentVersionUploadResponseMetadataTypeDef,
        "UploadMetadata": ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef,
    },
    total=False,
)

ClientUpdateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "ClientUpdateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientUpdateUserResponseUserStorageTypeDef = TypedDict(
    "ClientUpdateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientUpdateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientUpdateUserResponseUserTypeDef = TypedDict(
    "ClientUpdateUserResponseUserTypeDef",
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

ClientUpdateUserResponseTypeDef = TypedDict(
    "ClientUpdateUserResponseTypeDef", {"User": ClientUpdateUserResponseUserTypeDef}, total=False
)

ClientUpdateUserStorageRuleTypeDef = TypedDict(
    "ClientUpdateUserStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

DescribeActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef,
    },
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef",
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

DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": DescribeActivitiesPaginateResponseUserActivitiesCommentMetadataContributorTypeDef,
        "CreatedTimestamp": datetime,
        "CommentStatus": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "RecipientId": str,
    },
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesInitiatorTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesOriginalParentOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesOriginalParentTypeDef",
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

DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesParticipantsTypeDef",
    {
        "Users": List[DescribeActivitiesPaginateResponseUserActivitiesParticipantsUsersTypeDef],
        "Groups": List[DescribeActivitiesPaginateResponseUserActivitiesParticipantsGroupsTypeDef],
    },
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesResourceMetadataTypeDef",
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

DescribeActivitiesPaginateResponseUserActivitiesTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseUserActivitiesTypeDef",
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

DescribeActivitiesPaginateResponseTypeDef = TypedDict(
    "DescribeActivitiesPaginateResponseTypeDef",
    {
        "UserActivities": List[DescribeActivitiesPaginateResponseUserActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeCommentsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCommentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef = TypedDict(
    "DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef = TypedDict(
    "DescribeCommentsPaginateResponseCommentsContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeCommentsPaginateResponseCommentsContributorStorageStorageRuleTypeDef,
    },
    total=False,
)

DescribeCommentsPaginateResponseCommentsContributorTypeDef = TypedDict(
    "DescribeCommentsPaginateResponseCommentsContributorTypeDef",
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

DescribeCommentsPaginateResponseCommentsTypeDef = TypedDict(
    "DescribeCommentsPaginateResponseCommentsTypeDef",
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

DescribeCommentsPaginateResponseTypeDef = TypedDict(
    "DescribeCommentsPaginateResponseTypeDef",
    {"Comments": List[DescribeCommentsPaginateResponseCommentsTypeDef], "NextToken": str},
    total=False,
)

DescribeDocumentVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeDocumentVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef = TypedDict(
    "DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef",
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

DescribeDocumentVersionsPaginateResponseTypeDef = TypedDict(
    "DescribeDocumentVersionsPaginateResponseTypeDef",
    {
        "DocumentVersions": List[DescribeDocumentVersionsPaginateResponseDocumentVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeFolderContentsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeFolderContentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "DescribeFolderContentsPaginateResponseDocumentsLatestVersionMetadataTypeDef",
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

DescribeFolderContentsPaginateResponseDocumentsTypeDef = TypedDict(
    "DescribeFolderContentsPaginateResponseDocumentsTypeDef",
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

DescribeFolderContentsPaginateResponseFoldersTypeDef = TypedDict(
    "DescribeFolderContentsPaginateResponseFoldersTypeDef",
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

DescribeFolderContentsPaginateResponseTypeDef = TypedDict(
    "DescribeFolderContentsPaginateResponseTypeDef",
    {
        "Folders": List[DescribeFolderContentsPaginateResponseFoldersTypeDef],
        "Documents": List[DescribeFolderContentsPaginateResponseDocumentsTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "DescribeGroupsPaginateResponseGroupsTypeDef", {"Id": str, "Name": str}, total=False
)

DescribeGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeGroupsPaginateResponseTypeDef",
    {"Groups": List[DescribeGroupsPaginateResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)

DescribeNotificationSubscriptionsPaginateResponseTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsPaginateResponseTypeDef",
    {
        "Subscriptions": List[
            DescribeNotificationSubscriptionsPaginateResponseSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeResourcePermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeResourcePermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef = TypedDict(
    "DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef",
    {
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Type": Literal["DIRECT", "INHERITED"],
    },
    total=False,
)

DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef = TypedDict(
    "DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef",
    {
        "Id": str,
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Roles": List[DescribeResourcePermissionsPaginateResponsePrincipalsRolesTypeDef],
    },
    total=False,
)

DescribeResourcePermissionsPaginateResponseTypeDef = TypedDict(
    "DescribeResourcePermissionsPaginateResponseTypeDef",
    {
        "Principals": List[DescribeResourcePermissionsPaginateResponsePrincipalsTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeRootFoldersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeRootFoldersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeRootFoldersPaginateResponseFoldersTypeDef = TypedDict(
    "DescribeRootFoldersPaginateResponseFoldersTypeDef",
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

DescribeRootFoldersPaginateResponseTypeDef = TypedDict(
    "DescribeRootFoldersPaginateResponseTypeDef",
    {"Folders": List[DescribeRootFoldersPaginateResponseFoldersTypeDef], "NextToken": str},
    total=False,
)

DescribeUsersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef = TypedDict(
    "DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

DescribeUsersPaginateResponseUsersStorageTypeDef = TypedDict(
    "DescribeUsersPaginateResponseUsersStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": DescribeUsersPaginateResponseUsersStorageStorageRuleTypeDef,
    },
    total=False,
)

DescribeUsersPaginateResponseUsersTypeDef = TypedDict(
    "DescribeUsersPaginateResponseUsersTypeDef",
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

DescribeUsersPaginateResponseTypeDef = TypedDict(
    "DescribeUsersPaginateResponseTypeDef",
    {
        "Users": List[DescribeUsersPaginateResponseUsersTypeDef],
        "TotalNumberOfUsers": int,
        "NextToken": str,
    },
    total=False,
)
