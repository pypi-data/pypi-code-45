"Main interface for ecr service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ecr.type_defs import (
    DescribeImageScanFindingsPaginateImageIdTypeDef,
    DescribeImageScanFindingsPaginatePaginationConfigTypeDef,
    DescribeImageScanFindingsPaginateResponseTypeDef,
    DescribeImagesPaginateFilterTypeDef,
    DescribeImagesPaginateImageIdsTypeDef,
    DescribeImagesPaginatePaginationConfigTypeDef,
    DescribeImagesPaginateResponseTypeDef,
    DescribeRepositoriesPaginatePaginationConfigTypeDef,
    DescribeRepositoriesPaginateResponseTypeDef,
    GetLifecyclePolicyPreviewPaginateFilterTypeDef,
    GetLifecyclePolicyPreviewPaginateImageIdsTypeDef,
    GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef,
    GetLifecyclePolicyPreviewPaginateResponseTypeDef,
    ListImagesPaginateFilterTypeDef,
    ListImagesPaginatePaginationConfigTypeDef,
    ListImagesPaginateResponseTypeDef,
)


__all__ = (
    "DescribeImageScanFindingsPaginator",
    "DescribeImagesPaginator",
    "DescribeRepositoriesPaginator",
    "GetLifecyclePolicyPreviewPaginator",
    "ListImagesPaginator",
)


class DescribeImageScanFindingsPaginator(Boto3Paginator):
    """
    Paginator for `describe_image_scan_findings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        imageId: DescribeImageScanFindingsPaginateImageIdTypeDef,
        registryId: str = None,
        PaginationConfig: DescribeImageScanFindingsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeImageScanFindingsPaginateResponseTypeDef:
        """
        [DescribeImageScanFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings.paginate)
        """


class DescribeImagesPaginator(Boto3Paginator):
    """
    Paginator for `describe_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[DescribeImagesPaginateImageIdsTypeDef] = None,
        filter: DescribeImagesPaginateFilterTypeDef = None,
        PaginationConfig: DescribeImagesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeImagesPaginateResponseTypeDef:
        """
        [DescribeImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecr.html#ECR.Paginator.DescribeImages.paginate)
        """


class DescribeRepositoriesPaginator(Boto3Paginator):
    """
    Paginator for `describe_repositories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        PaginationConfig: DescribeRepositoriesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRepositoriesPaginateResponseTypeDef:
        """
        [DescribeRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecr.html#ECR.Paginator.DescribeRepositories.paginate)
        """


class GetLifecyclePolicyPreviewPaginator(Boto3Paginator):
    """
    Paginator for `get_lifecycle_policy_preview`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[GetLifecyclePolicyPreviewPaginateImageIdsTypeDef] = None,
        filter: GetLifecyclePolicyPreviewPaginateFilterTypeDef = None,
        PaginationConfig: GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef = None,
    ) -> GetLifecyclePolicyPreviewPaginateResponseTypeDef:
        """
        [GetLifecyclePolicyPreview.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview.paginate)
        """


class ListImagesPaginator(Boto3Paginator):
    """
    Paginator for `list_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        filter: ListImagesPaginateFilterTypeDef = None,
        PaginationConfig: ListImagesPaginatePaginationConfigTypeDef = None,
    ) -> ListImagesPaginateResponseTypeDef:
        """
        [ListImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ecr.html#ECR.Paginator.ListImages.paginate)
        """
