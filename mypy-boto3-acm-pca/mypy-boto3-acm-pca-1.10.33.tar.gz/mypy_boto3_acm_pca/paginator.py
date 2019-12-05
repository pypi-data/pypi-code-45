"Main interface for acm-pca service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_acm_pca.type_defs import (
    ListCertificateAuthoritiesPaginatePaginationConfigTypeDef,
    ListCertificateAuthoritiesPaginateResponseTypeDef,
    ListPermissionsPaginatePaginationConfigTypeDef,
    ListPermissionsPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
)


__all__ = ("ListCertificateAuthoritiesPaginator", "ListPermissionsPaginator", "ListTagsPaginator")


class ListCertificateAuthoritiesPaginator(Boto3Paginator):
    """
    Paginator for `list_certificate_authorities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListCertificateAuthoritiesPaginatePaginationConfigTypeDef = None
    ) -> ListCertificateAuthoritiesPaginateResponseTypeDef:
        """
        [ListCertificateAuthorities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities.paginate)
        """


class ListPermissionsPaginator(Boto3Paginator):
    """
    Paginator for `list_permissions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CertificateAuthorityArn: str,
        PaginationConfig: ListPermissionsPaginatePaginationConfigTypeDef = None,
    ) -> ListPermissionsPaginateResponseTypeDef:
        """
        [ListPermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CertificateAuthorityArn: str,
        PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None,
    ) -> ListTagsPaginateResponseTypeDef:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags.paginate)
        """
