"Main interface for support service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_support.type_defs import (
    DescribeCasesPaginatePaginationConfigTypeDef,
    DescribeCasesPaginateResponseTypeDef,
    DescribeCommunicationsPaginatePaginationConfigTypeDef,
    DescribeCommunicationsPaginateResponseTypeDef,
)


__all__ = ("DescribeCasesPaginator", "DescribeCommunicationsPaginator")


class DescribeCasesPaginator(Boto3Paginator):
    """
    Paginator for `describe_cases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        language: str = None,
        includeCommunications: bool = None,
        PaginationConfig: DescribeCasesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCasesPaginateResponseTypeDef:
        """
        [DescribeCases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/support.html#Support.Paginator.DescribeCases.paginate)
        """


class DescribeCommunicationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_communications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        PaginationConfig: DescribeCommunicationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCommunicationsPaginateResponseTypeDef:
        """
        [DescribeCommunications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/support.html#Support.Paginator.DescribeCommunications.paginate)
        """
