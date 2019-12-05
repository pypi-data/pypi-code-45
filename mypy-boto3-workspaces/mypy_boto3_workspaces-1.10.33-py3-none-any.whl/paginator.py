"Main interface for workspaces service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_workspaces.type_defs import (
    DescribeAccountModificationsPaginatePaginationConfigTypeDef,
    DescribeAccountModificationsPaginateResponseTypeDef,
    DescribeIpGroupsPaginatePaginationConfigTypeDef,
    DescribeIpGroupsPaginateResponseTypeDef,
    DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef,
    DescribeWorkspaceBundlesPaginateResponseTypeDef,
    DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef,
    DescribeWorkspaceDirectoriesPaginateResponseTypeDef,
    DescribeWorkspaceImagesPaginatePaginationConfigTypeDef,
    DescribeWorkspaceImagesPaginateResponseTypeDef,
    DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef,
    DescribeWorkspacesConnectionStatusPaginateResponseTypeDef,
    DescribeWorkspacesPaginatePaginationConfigTypeDef,
    DescribeWorkspacesPaginateResponseTypeDef,
    ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef,
    ListAvailableManagementCidrRangesPaginateResponseTypeDef,
)


__all__ = (
    "DescribeAccountModificationsPaginator",
    "DescribeIpGroupsPaginator",
    "DescribeWorkspaceBundlesPaginator",
    "DescribeWorkspaceDirectoriesPaginator",
    "DescribeWorkspaceImagesPaginator",
    "DescribeWorkspacesPaginator",
    "DescribeWorkspacesConnectionStatusPaginator",
    "ListAvailableManagementCidrRangesPaginator",
)


class DescribeAccountModificationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_account_modifications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeAccountModificationsPaginatePaginationConfigTypeDef = None
    ) -> DescribeAccountModificationsPaginateResponseTypeDef:
        """
        [DescribeAccountModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications.paginate)
        """


class DescribeIpGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_ip_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GroupIds: List[str] = None,
        PaginationConfig: DescribeIpGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeIpGroupsPaginateResponseTypeDef:
        """
        [DescribeIpGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups.paginate)
        """


class DescribeWorkspaceBundlesPaginator(Boto3Paginator):
    """
    Paginator for `describe_workspace_bundles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BundleIds: List[str] = None,
        Owner: str = None,
        PaginationConfig: DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspaceBundlesPaginateResponseTypeDef:
        """
        [DescribeWorkspaceBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles.paginate)
        """


class DescribeWorkspaceDirectoriesPaginator(Boto3Paginator):
    """
    Paginator for `describe_workspace_directories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryIds: List[str] = None,
        Limit: int = None,
        PaginationConfig: DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspaceDirectoriesPaginateResponseTypeDef:
        """
        [DescribeWorkspaceDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories.paginate)
        """


class DescribeWorkspaceImagesPaginator(Boto3Paginator):
    """
    Paginator for `describe_workspace_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ImageIds: List[str] = None,
        PaginationConfig: DescribeWorkspaceImagesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspaceImagesPaginateResponseTypeDef:
        """
        [DescribeWorkspaceImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages.paginate)
        """


class DescribeWorkspacesPaginator(Boto3Paginator):
    """
    Paginator for `describe_workspaces`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        PaginationConfig: DescribeWorkspacesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspacesPaginateResponseTypeDef:
        """
        [DescribeWorkspaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces.paginate)
        """


class DescribeWorkspacesConnectionStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_workspaces_connection_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkspaceIds: List[str] = None,
        PaginationConfig: DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspacesConnectionStatusPaginateResponseTypeDef:
        """
        [DescribeWorkspacesConnectionStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus.paginate)
        """


class ListAvailableManagementCidrRangesPaginator(Boto3Paginator):
    """
    Paginator for `list_available_management_cidr_ranges`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ManagementCidrRangeConstraint: str,
        PaginationConfig: ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef = None,
    ) -> ListAvailableManagementCidrRangesPaginateResponseTypeDef:
        """
        [ListAvailableManagementCidrRanges.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges.paginate)
        """
