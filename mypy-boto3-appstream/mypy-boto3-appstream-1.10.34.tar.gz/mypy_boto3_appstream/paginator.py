"Main interface for appstream service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_appstream.type_defs import (
    DescribeDirectoryConfigsPaginatePaginationConfigTypeDef,
    DescribeDirectoryConfigsPaginateResponseTypeDef,
    DescribeFleetsPaginatePaginationConfigTypeDef,
    DescribeFleetsPaginateResponseTypeDef,
    DescribeImageBuildersPaginatePaginationConfigTypeDef,
    DescribeImageBuildersPaginateResponseTypeDef,
    DescribeImagesPaginatePaginationConfigTypeDef,
    DescribeImagesPaginateResponseTypeDef,
    DescribeSessionsPaginatePaginationConfigTypeDef,
    DescribeSessionsPaginateResponseTypeDef,
    DescribeStacksPaginatePaginationConfigTypeDef,
    DescribeStacksPaginateResponseTypeDef,
    DescribeUserStackAssociationsPaginatePaginationConfigTypeDef,
    DescribeUserStackAssociationsPaginateResponseTypeDef,
    DescribeUsersPaginatePaginationConfigTypeDef,
    DescribeUsersPaginateResponseTypeDef,
    ListAssociatedFleetsPaginatePaginationConfigTypeDef,
    ListAssociatedFleetsPaginateResponseTypeDef,
    ListAssociatedStacksPaginatePaginationConfigTypeDef,
    ListAssociatedStacksPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDirectoryConfigsPaginator",
    "DescribeFleetsPaginator",
    "DescribeImageBuildersPaginator",
    "DescribeImagesPaginator",
    "DescribeSessionsPaginator",
    "DescribeStacksPaginator",
    "DescribeUserStackAssociationsPaginator",
    "DescribeUsersPaginator",
    "ListAssociatedFleetsPaginator",
    "ListAssociatedStacksPaginator",
)


class DescribeDirectoryConfigsPaginator(Boto3Paginator):
    """
    Paginator for `describe_directory_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryNames: List[str] = None,
        PaginationConfig: DescribeDirectoryConfigsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDirectoryConfigsPaginateResponseTypeDef:
        """
        [DescribeDirectoryConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs.paginate)
        """


class DescribeFleetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_fleets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: DescribeFleetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFleetsPaginateResponseTypeDef:
        """
        [DescribeFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeFleets.paginate)
        """


class DescribeImageBuildersPaginator(Boto3Paginator):
    """
    Paginator for `describe_image_builders`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: DescribeImageBuildersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeImageBuildersPaginateResponseTypeDef:
        """
        [DescribeImageBuilders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders.paginate)
        """


class DescribeImagesPaginator(Boto3Paginator):
    """
    Paginator for `describe_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: Literal["PUBLIC", "PRIVATE", "SHARED"] = None,
        PaginationConfig: DescribeImagesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeImagesPaginateResponseTypeDef:
        """
        [DescribeImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeImages.paginate)
        """


class DescribeSessionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_sessions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
        PaginationConfig: DescribeSessionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSessionsPaginateResponseTypeDef:
        """
        [DescribeSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeSessions.paginate)
        """


class DescribeStacksPaginator(Boto3Paginator):
    """
    Paginator for `describe_stacks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: DescribeStacksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeStacksPaginateResponseTypeDef:
        """
        [DescribeStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeStacks.paginate)
        """


class DescribeUserStackAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_user_stack_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
        PaginationConfig: DescribeUserStackAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeUserStackAssociationsPaginateResponseTypeDef:
        """
        [DescribeUserStackAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations.paginate)
        """


class DescribeUsersPaginator(Boto3Paginator):
    """
    Paginator for `describe_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"],
        PaginationConfig: DescribeUsersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeUsersPaginateResponseTypeDef:
        """
        [DescribeUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeUsers.paginate)
        """


class ListAssociatedFleetsPaginator(Boto3Paginator):
    """
    Paginator for `list_associated_fleets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackName: str,
        PaginationConfig: ListAssociatedFleetsPaginatePaginationConfigTypeDef = None,
    ) -> ListAssociatedFleetsPaginateResponseTypeDef:
        """
        [ListAssociatedFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets.paginate)
        """


class ListAssociatedStacksPaginator(Boto3Paginator):
    """
    Paginator for `list_associated_stacks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetName: str,
        PaginationConfig: ListAssociatedStacksPaginatePaginationConfigTypeDef = None,
    ) -> ListAssociatedStacksPaginateResponseTypeDef:
        """
        [ListAssociatedStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks.paginate)
        """
