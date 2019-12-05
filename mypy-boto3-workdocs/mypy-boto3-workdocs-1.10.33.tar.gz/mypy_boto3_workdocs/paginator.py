"Main interface for workdocs service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_workdocs.type_defs import (
    DescribeActivitiesPaginatePaginationConfigTypeDef,
    DescribeActivitiesPaginateResponseTypeDef,
    DescribeCommentsPaginatePaginationConfigTypeDef,
    DescribeCommentsPaginateResponseTypeDef,
    DescribeDocumentVersionsPaginatePaginationConfigTypeDef,
    DescribeDocumentVersionsPaginateResponseTypeDef,
    DescribeFolderContentsPaginatePaginationConfigTypeDef,
    DescribeFolderContentsPaginateResponseTypeDef,
    DescribeGroupsPaginatePaginationConfigTypeDef,
    DescribeGroupsPaginateResponseTypeDef,
    DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef,
    DescribeNotificationSubscriptionsPaginateResponseTypeDef,
    DescribeResourcePermissionsPaginatePaginationConfigTypeDef,
    DescribeResourcePermissionsPaginateResponseTypeDef,
    DescribeRootFoldersPaginatePaginationConfigTypeDef,
    DescribeRootFoldersPaginateResponseTypeDef,
    DescribeUsersPaginatePaginationConfigTypeDef,
    DescribeUsersPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeActivitiesPaginator",
    "DescribeCommentsPaginator",
    "DescribeDocumentVersionsPaginator",
    "DescribeFolderContentsPaginator",
    "DescribeGroupsPaginator",
    "DescribeNotificationSubscriptionsPaginator",
    "DescribeResourcePermissionsPaginator",
    "DescribeRootFoldersPaginator",
    "DescribeUsersPaginator",
)


class DescribeActivitiesPaginator(Boto3Paginator):
    """
    Paginator for `describe_activities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        PaginationConfig: DescribeActivitiesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeActivitiesPaginateResponseTypeDef:
        """
        [DescribeActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities.paginate)
        """


class DescribeCommentsPaginator(Boto3Paginator):
    """
    Paginator for `describe_comments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        PaginationConfig: DescribeCommentsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCommentsPaginateResponseTypeDef:
        """
        [DescribeComments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments.paginate)
        """


class DescribeDocumentVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_document_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Include: str = None,
        Fields: str = None,
        PaginationConfig: DescribeDocumentVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDocumentVersionsPaginateResponseTypeDef:
        """
        [DescribeDocumentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions.paginate)
        """


class DescribeFolderContentsPaginator(Boto3Paginator):
    """
    Paginator for `describe_folder_contents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: Literal["DATE", "NAME"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Type: Literal["ALL", "DOCUMENT", "FOLDER"] = None,
        Include: str = None,
        PaginationConfig: DescribeFolderContentsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFolderContentsPaginateResponseTypeDef:
        """
        [DescribeFolderContents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents.paginate)
        """


class DescribeGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        PaginationConfig: DescribeGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeGroupsPaginateResponseTypeDef:
        """
        [DescribeGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups.paginate)
        """


class DescribeNotificationSubscriptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_notification_subscriptions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: DescribeNotificationSubscriptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeNotificationSubscriptionsPaginateResponseTypeDef:
        """
        [DescribeNotificationSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions.paginate)
        """


class DescribeResourcePermissionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_resource_permissions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        PaginationConfig: DescribeResourcePermissionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeResourcePermissionsPaginateResponseTypeDef:
        """
        [DescribeResourcePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions.paginate)
        """


class DescribeRootFoldersPaginator(Boto3Paginator):
    """
    Paginator for `describe_root_folders`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AuthenticationToken: str,
        PaginationConfig: DescribeRootFoldersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRootFoldersPaginateResponseTypeDef:
        """
        [DescribeRootFolders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders.paginate)
        """


class DescribeUsersPaginator(Boto3Paginator):
    """
    Paginator for `describe_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        UserIds: str = None,
        Query: str = None,
        Include: Literal["ALL", "ACTIVE_PENDING"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Sort: Literal[
            "USER_NAME", "FULL_NAME", "STORAGE_LIMIT", "USER_STATUS", "STORAGE_USED"
        ] = None,
        Fields: str = None,
        PaginationConfig: DescribeUsersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeUsersPaginateResponseTypeDef:
        """
        [DescribeUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers.paginate)
        """
