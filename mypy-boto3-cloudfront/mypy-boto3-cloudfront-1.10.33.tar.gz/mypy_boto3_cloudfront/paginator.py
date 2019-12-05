"Main interface for cloudfront service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudfront.type_defs import (
    ListCloudFrontOriginAccessIdentitiesPaginatePaginationConfigTypeDef,
    ListCloudFrontOriginAccessIdentitiesPaginateResponseTypeDef,
    ListDistributionsPaginatePaginationConfigTypeDef,
    ListDistributionsPaginateResponseTypeDef,
    ListInvalidationsPaginatePaginationConfigTypeDef,
    ListInvalidationsPaginateResponseTypeDef,
    ListStreamingDistributionsPaginatePaginationConfigTypeDef,
    ListStreamingDistributionsPaginateResponseTypeDef,
)


__all__ = (
    "ListCloudFrontOriginAccessIdentitiesPaginator",
    "ListDistributionsPaginator",
    "ListInvalidationsPaginator",
    "ListStreamingDistributionsPaginator",
)


class ListCloudFrontOriginAccessIdentitiesPaginator(Boto3Paginator):
    """
    Paginator for `list_cloud_front_origin_access_identities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListCloudFrontOriginAccessIdentitiesPaginatePaginationConfigTypeDef = None,
    ) -> ListCloudFrontOriginAccessIdentitiesPaginateResponseTypeDef:
        """
        [ListCloudFrontOriginAccessIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities.paginate)
        """


class ListDistributionsPaginator(Boto3Paginator):
    """
    Paginator for `list_distributions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDistributionsPaginatePaginationConfigTypeDef = None
    ) -> ListDistributionsPaginateResponseTypeDef:
        """
        [ListDistributions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions.paginate)
        """


class ListInvalidationsPaginator(Boto3Paginator):
    """
    Paginator for `list_invalidations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DistributionId: str,
        PaginationConfig: ListInvalidationsPaginatePaginationConfigTypeDef = None,
    ) -> ListInvalidationsPaginateResponseTypeDef:
        """
        [ListInvalidations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations.paginate)
        """


class ListStreamingDistributionsPaginator(Boto3Paginator):
    """
    Paginator for `list_streaming_distributions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListStreamingDistributionsPaginatePaginationConfigTypeDef = None
    ) -> ListStreamingDistributionsPaginateResponseTypeDef:
        """
        [ListStreamingDistributions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions.paginate)
        """
