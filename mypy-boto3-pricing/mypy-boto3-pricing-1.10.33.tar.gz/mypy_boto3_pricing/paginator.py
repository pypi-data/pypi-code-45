"Main interface for pricing service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_pricing.type_defs import (
    DescribeServicesPaginatePaginationConfigTypeDef,
    DescribeServicesPaginateResponseTypeDef,
    GetAttributeValuesPaginatePaginationConfigTypeDef,
    GetAttributeValuesPaginateResponseTypeDef,
    GetProductsPaginateFiltersTypeDef,
    GetProductsPaginatePaginationConfigTypeDef,
    GetProductsPaginateResponseTypeDef,
)


__all__ = ("DescribeServicesPaginator", "GetAttributeValuesPaginator", "GetProductsPaginator")


class DescribeServicesPaginator(Boto3Paginator):
    """
    Paginator for `describe_services`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        FormatVersion: str = None,
        PaginationConfig: DescribeServicesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeServicesPaginateResponseTypeDef:
        """
        [DescribeServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/pricing.html#Pricing.Paginator.DescribeServices.paginate)
        """


class GetAttributeValuesPaginator(Boto3Paginator):
    """
    Paginator for `get_attribute_values`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str,
        AttributeName: str,
        PaginationConfig: GetAttributeValuesPaginatePaginationConfigTypeDef = None,
    ) -> GetAttributeValuesPaginateResponseTypeDef:
        """
        [GetAttributeValues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues.paginate)
        """


class GetProductsPaginator(Boto3Paginator):
    """
    Paginator for `get_products`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        Filters: List[GetProductsPaginateFiltersTypeDef] = None,
        FormatVersion: str = None,
        PaginationConfig: GetProductsPaginatePaginationConfigTypeDef = None,
    ) -> GetProductsPaginateResponseTypeDef:
        """
        [GetProducts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/pricing.html#Pricing.Paginator.GetProducts.paginate)
        """
