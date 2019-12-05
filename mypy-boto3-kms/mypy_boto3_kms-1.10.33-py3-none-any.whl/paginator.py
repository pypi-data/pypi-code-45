"Main interface for kms service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kms.type_defs import (
    ListAliasesPaginatePaginationConfigTypeDef,
    ListAliasesPaginateResponseTypeDef,
    ListGrantsPaginatePaginationConfigTypeDef,
    ListGrantsPaginateResponseTypeDef,
    ListKeyPoliciesPaginatePaginationConfigTypeDef,
    ListKeyPoliciesPaginateResponseTypeDef,
    ListKeysPaginatePaginationConfigTypeDef,
    ListKeysPaginateResponseTypeDef,
)


__all__ = (
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeysPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    Paginator for `list_aliases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, KeyId: str = None, PaginationConfig: ListAliasesPaginatePaginationConfigTypeDef = None
    ) -> ListAliasesPaginateResponseTypeDef:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kms.html#KMS.Paginator.ListAliases.paginate)
        """


class ListGrantsPaginator(Boto3Paginator):
    """
    Paginator for `list_grants`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, KeyId: str, PaginationConfig: ListGrantsPaginatePaginationConfigTypeDef = None
    ) -> ListGrantsPaginateResponseTypeDef:
        """
        [ListGrants.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kms.html#KMS.Paginator.ListGrants.paginate)
        """


class ListKeyPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_key_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, KeyId: str, PaginationConfig: ListKeyPoliciesPaginatePaginationConfigTypeDef = None
    ) -> ListKeyPoliciesPaginateResponseTypeDef:
        """
        [ListKeyPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kms.html#KMS.Paginator.ListKeyPolicies.paginate)
        """


class ListKeysPaginator(Boto3Paginator):
    """
    Paginator for `list_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListKeysPaginatePaginationConfigTypeDef = None
    ) -> ListKeysPaginateResponseTypeDef:
        """
        [ListKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kms.html#KMS.Paginator.ListKeys.paginate)
        """
