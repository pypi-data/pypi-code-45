"Main interface for signer service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_signer.type_defs import (
    ListSigningJobsPaginatePaginationConfigTypeDef,
    ListSigningJobsPaginateResponseTypeDef,
    ListSigningPlatformsPaginatePaginationConfigTypeDef,
    ListSigningPlatformsPaginateResponseTypeDef,
    ListSigningProfilesPaginatePaginationConfigTypeDef,
    ListSigningProfilesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
)


class ListSigningJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_signing_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        status: Literal["InProgress", "Failed", "Succeeded"] = None,
        platformId: str = None,
        requestedBy: str = None,
        PaginationConfig: ListSigningJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListSigningJobsPaginateResponseTypeDef:
        """
        [ListSigningJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/signer.html#Signer.Paginator.ListSigningJobs.paginate)
        """


class ListSigningPlatformsPaginator(Boto3Paginator):
    """
    Paginator for `list_signing_platforms`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        PaginationConfig: ListSigningPlatformsPaginatePaginationConfigTypeDef = None,
    ) -> ListSigningPlatformsPaginateResponseTypeDef:
        """
        [ListSigningPlatforms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms.paginate)
        """


class ListSigningProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_signing_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        includeCanceled: bool = None,
        PaginationConfig: ListSigningProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListSigningProfilesPaginateResponseTypeDef:
        """
        [ListSigningProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/signer.html#Signer.Paginator.ListSigningProfiles.paginate)
        """
