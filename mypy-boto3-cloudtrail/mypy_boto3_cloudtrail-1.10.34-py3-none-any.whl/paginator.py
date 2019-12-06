"Main interface for cloudtrail service Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudtrail.type_defs import (
    ListPublicKeysPaginatePaginationConfigTypeDef,
    ListPublicKeysPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
    ListTrailsPaginatePaginationConfigTypeDef,
    ListTrailsPaginateResponseTypeDef,
    LookupEventsPaginateLookupAttributesTypeDef,
    LookupEventsPaginatePaginationConfigTypeDef,
    LookupEventsPaginateResponseTypeDef,
)


__all__ = (
    "ListPublicKeysPaginator",
    "ListTagsPaginator",
    "ListTrailsPaginator",
    "LookupEventsPaginator",
)


class ListPublicKeysPaginator(Boto3Paginator):
    """
    Paginator for `list_public_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: ListPublicKeysPaginatePaginationConfigTypeDef = None,
    ) -> ListPublicKeysPaginateResponseTypeDef:
        """
        [ListPublicKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceIdList: List[str],
        PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None,
    ) -> ListTagsPaginateResponseTypeDef:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags.paginate)
        """


class ListTrailsPaginator(Boto3Paginator):
    """
    Paginator for `list_trails`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListTrailsPaginatePaginationConfigTypeDef = None
    ) -> ListTrailsPaginateResponseTypeDef:
        """
        [ListTrails.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails.paginate)
        """


class LookupEventsPaginator(Boto3Paginator):
    """
    Paginator for `lookup_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LookupAttributes: List[LookupEventsPaginateLookupAttributesTypeDef] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventCategory: str = None,
        PaginationConfig: LookupEventsPaginatePaginationConfigTypeDef = None,
    ) -> LookupEventsPaginateResponseTypeDef:
        """
        [LookupEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents.paginate)
        """
