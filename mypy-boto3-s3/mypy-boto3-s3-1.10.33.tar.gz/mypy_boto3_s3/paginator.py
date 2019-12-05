"Main interface for s3 service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_s3.type_defs import (
    ListMultipartUploadsPaginatePaginationConfigTypeDef,
    ListMultipartUploadsPaginateResponseTypeDef,
    ListObjectVersionsPaginatePaginationConfigTypeDef,
    ListObjectVersionsPaginateResponseTypeDef,
    ListObjectsPaginatePaginationConfigTypeDef,
    ListObjectsPaginateResponseTypeDef,
    ListObjectsV2PaginatePaginationConfigTypeDef,
    ListObjectsV2PaginateResponseTypeDef,
    ListPartsPaginatePaginationConfigTypeDef,
    ListPartsPaginateResponseTypeDef,
)


__all__ = (
    "ListMultipartUploadsPaginator",
    "ListObjectVersionsPaginator",
    "ListObjectsPaginator",
    "ListObjectsV2Paginator",
    "ListPartsPaginator",
)


class ListMultipartUploadsPaginator(Boto3Paginator):
    """
    Paginator for `list_multipart_uploads`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        PaginationConfig: ListMultipartUploadsPaginatePaginationConfigTypeDef = None,
    ) -> ListMultipartUploadsPaginateResponseTypeDef:
        """
        [ListMultipartUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Paginator.ListMultipartUploads.paginate)
        """


class ListObjectVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_object_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        PaginationConfig: ListObjectVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListObjectVersionsPaginateResponseTypeDef:
        """
        [ListObjectVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Paginator.ListObjectVersions.paginate)
        """


class ListObjectsPaginator(Boto3Paginator):
    """
    Paginator for `list_objects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        RequestPayer: str = None,
        PaginationConfig: ListObjectsPaginatePaginationConfigTypeDef = None,
    ) -> ListObjectsPaginateResponseTypeDef:
        """
        [ListObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Paginator.ListObjects.paginate)
        """


class ListObjectsV2Paginator(Boto3Paginator):
    """
    Paginator for `list_objects_v2`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: str = None,
        PaginationConfig: ListObjectsV2PaginatePaginationConfigTypeDef = None,
    ) -> ListObjectsV2PaginateResponseTypeDef:
        """
        [ListObjectsV2.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Paginator.ListObjectsV2.paginate)
        """


class ListPartsPaginator(Boto3Paginator):
    """
    Paginator for `list_parts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: str = None,
        PaginationConfig: ListPartsPaginatePaginationConfigTypeDef = None,
    ) -> ListPartsPaginateResponseTypeDef:
        """
        [ListParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/s3.html#S3.Paginator.ListParts.paginate)
        """
