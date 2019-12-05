"Main interface for acm service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_acm.type_defs import (
    ListCertificatesPaginateIncludesTypeDef,
    ListCertificatesPaginatePaginationConfigTypeDef,
    ListCertificatesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListCertificatesPaginator",)


class ListCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `list_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CertificateStatuses: List[
            Literal[
                "PENDING_VALIDATION",
                "ISSUED",
                "INACTIVE",
                "EXPIRED",
                "VALIDATION_TIMED_OUT",
                "REVOKED",
                "FAILED",
            ]
        ] = None,
        Includes: ListCertificatesPaginateIncludesTypeDef = None,
        PaginationConfig: ListCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> ListCertificatesPaginateResponseTypeDef:
        """
        [ListCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/acm.html#ACM.Paginator.ListCertificates.paginate)
        """
