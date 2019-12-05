"Main interface for rekognition service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_rekognition.type_defs import (
    DescribeProjectVersionsPaginatePaginationConfigTypeDef,
    DescribeProjectVersionsPaginateResponseTypeDef,
    DescribeProjectsPaginatePaginationConfigTypeDef,
    DescribeProjectsPaginateResponseTypeDef,
    ListCollectionsPaginatePaginationConfigTypeDef,
    ListCollectionsPaginateResponseTypeDef,
    ListFacesPaginatePaginationConfigTypeDef,
    ListFacesPaginateResponseTypeDef,
    ListStreamProcessorsPaginatePaginationConfigTypeDef,
    ListStreamProcessorsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListFacesPaginator",
    "ListStreamProcessorsPaginator",
)


class DescribeProjectVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_project_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        PaginationConfig: DescribeProjectVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeProjectVersionsPaginateResponseTypeDef:
        """
        [DescribeProjectVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions.paginate)
        """


class DescribeProjectsPaginator(Boto3Paginator):
    """
    Paginator for `describe_projects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeProjectsPaginatePaginationConfigTypeDef = None
    ) -> DescribeProjectsPaginateResponseTypeDef:
        """
        [DescribeProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects.paginate)
        """


class ListCollectionsPaginator(Boto3Paginator):
    """
    Paginator for `list_collections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListCollectionsPaginatePaginationConfigTypeDef = None
    ) -> ListCollectionsPaginateResponseTypeDef:
        """
        [ListCollections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rekognition.html#Rekognition.Paginator.ListCollections.paginate)
        """


class ListFacesPaginator(Boto3Paginator):
    """
    Paginator for `list_faces`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CollectionId: str, PaginationConfig: ListFacesPaginatePaginationConfigTypeDef = None
    ) -> ListFacesPaginateResponseTypeDef:
        """
        [ListFaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rekognition.html#Rekognition.Paginator.ListFaces.paginate)
        """


class ListStreamProcessorsPaginator(Boto3Paginator):
    """
    Paginator for `list_stream_processors`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListStreamProcessorsPaginatePaginationConfigTypeDef = None
    ) -> ListStreamProcessorsPaginateResponseTypeDef:
        """
        [ListStreamProcessors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors.paginate)
        """
