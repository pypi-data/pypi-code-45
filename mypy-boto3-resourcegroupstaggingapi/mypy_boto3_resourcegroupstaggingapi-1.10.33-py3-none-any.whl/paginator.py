"Main interface for resourcegroupstaggingapi service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    GetComplianceSummaryPaginatePaginationConfigTypeDef,
    GetComplianceSummaryPaginateResponseTypeDef,
    GetResourcesPaginatePaginationConfigTypeDef,
    GetResourcesPaginateResponseTypeDef,
    GetResourcesPaginateTagFiltersTypeDef,
    GetTagKeysPaginatePaginationConfigTypeDef,
    GetTagKeysPaginateResponseTypeDef,
    GetTagValuesPaginatePaginationConfigTypeDef,
    GetTagValuesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetComplianceSummaryPaginator",
    "GetResourcesPaginator",
    "GetTagKeysPaginator",
    "GetTagValuesPaginator",
)


class GetComplianceSummaryPaginator(Boto3Paginator):
    """
    Paginator for `get_compliance_summary`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[Literal["TARGET_ID", "REGION", "RESOURCE_TYPE"]] = None,
        PaginationConfig: GetComplianceSummaryPaginatePaginationConfigTypeDef = None,
    ) -> GetComplianceSummaryPaginateResponseTypeDef:
        """
        [GetComplianceSummary.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary.paginate)
        """


class GetResourcesPaginator(Boto3Paginator):
    """
    Paginator for `get_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TagFilters: List[GetResourcesPaginateTagFiltersTypeDef] = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
        PaginationConfig: GetResourcesPaginatePaginationConfigTypeDef = None,
    ) -> GetResourcesPaginateResponseTypeDef:
        """
        [GetResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources.paginate)
        """


class GetTagKeysPaginator(Boto3Paginator):
    """
    Paginator for `get_tag_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetTagKeysPaginatePaginationConfigTypeDef = None
    ) -> GetTagKeysPaginateResponseTypeDef:
        """
        [GetTagKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys.paginate)
        """


class GetTagValuesPaginator(Boto3Paginator):
    """
    Paginator for `get_tag_values`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Key: str, PaginationConfig: GetTagValuesPaginatePaginationConfigTypeDef = None
    ) -> GetTagValuesPaginateResponseTypeDef:
        """
        [GetTagValues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues.paginate)
        """
