"Main interface for cloudhsm service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudhsm.type_defs import (
    ListHapgsPaginatePaginationConfigTypeDef,
    ListHapgsPaginateResponseTypeDef,
    ListHsmsPaginatePaginationConfigTypeDef,
    ListHsmsPaginateResponseTypeDef,
    ListLunaClientsPaginatePaginationConfigTypeDef,
    ListLunaClientsPaginateResponseTypeDef,
)


__all__ = ("ListHapgsPaginator", "ListHsmsPaginator", "ListLunaClientsPaginator")


class ListHapgsPaginator(Boto3Paginator):
    """
    Paginator for `list_hapgs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListHapgsPaginatePaginationConfigTypeDef = None
    ) -> ListHapgsPaginateResponseTypeDef:
        """
        [ListHapgs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs.paginate)
        """


class ListHsmsPaginator(Boto3Paginator):
    """
    Paginator for `list_hsms`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListHsmsPaginatePaginationConfigTypeDef = None
    ) -> ListHsmsPaginateResponseTypeDef:
        """
        [ListHsms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms.paginate)
        """


class ListLunaClientsPaginator(Boto3Paginator):
    """
    Paginator for `list_luna_clients`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListLunaClientsPaginatePaginationConfigTypeDef = None
    ) -> ListLunaClientsPaginateResponseTypeDef:
        """
        [ListLunaClients.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients.paginate)
        """
