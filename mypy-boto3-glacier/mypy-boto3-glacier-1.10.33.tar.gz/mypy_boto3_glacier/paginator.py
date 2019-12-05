"Main interface for glacier service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_glacier.type_defs import (
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
    ListMultipartUploadsPaginatePaginationConfigTypeDef,
    ListMultipartUploadsPaginateResponseTypeDef,
    ListPartsPaginatePaginationConfigTypeDef,
    ListPartsPaginateResponseTypeDef,
    ListVaultsPaginatePaginationConfigTypeDef,
    ListVaultsPaginateResponseTypeDef,
)


__all__ = (
    "ListJobsPaginator",
    "ListMultipartUploadsPaginator",
    "ListPartsPaginator",
    "ListVaultsPaginator",
)


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        vaultName: str,
        accountId: str = None,
        statuscode: str = None,
        completed: str = None,
        PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsPaginateResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Paginator.ListJobs.paginate)
        """


class ListMultipartUploadsPaginator(Boto3Paginator):
    """
    Paginator for `list_multipart_uploads`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        vaultName: str,
        accountId: str = None,
        PaginationConfig: ListMultipartUploadsPaginatePaginationConfigTypeDef = None,
    ) -> ListMultipartUploadsPaginateResponseTypeDef:
        """
        [ListMultipartUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads.paginate)
        """


class ListPartsPaginator(Boto3Paginator):
    """
    Paginator for `list_parts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        vaultName: str,
        uploadId: str,
        accountId: str = None,
        PaginationConfig: ListPartsPaginatePaginationConfigTypeDef = None,
    ) -> ListPartsPaginateResponseTypeDef:
        """
        [ListParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Paginator.ListParts.paginate)
        """


class ListVaultsPaginator(Boto3Paginator):
    """
    Paginator for `list_vaults`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        accountId: str = None,
        PaginationConfig: ListVaultsPaginatePaginationConfigTypeDef = None,
    ) -> ListVaultsPaginateResponseTypeDef:
        """
        [ListVaults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Paginator.ListVaults.paginate)
        """
