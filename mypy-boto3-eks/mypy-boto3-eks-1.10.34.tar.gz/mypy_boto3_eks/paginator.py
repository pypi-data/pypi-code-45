"Main interface for eks service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_eks.type_defs import (
    ListClustersPaginatePaginationConfigTypeDef,
    ListClustersPaginateResponseTypeDef,
    ListFargateProfilesPaginatePaginationConfigTypeDef,
    ListFargateProfilesPaginateResponseTypeDef,
    ListNodegroupsPaginatePaginationConfigTypeDef,
    ListNodegroupsPaginateResponseTypeDef,
    ListUpdatesPaginatePaginationConfigTypeDef,
    ListUpdatesPaginateResponseTypeDef,
)


__all__ = (
    "ListClustersPaginator",
    "ListFargateProfilesPaginator",
    "ListNodegroupsPaginator",
    "ListUpdatesPaginator",
)


class ListClustersPaginator(Boto3Paginator):
    """
    Paginator for `list_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListClustersPaginatePaginationConfigTypeDef = None
    ) -> ListClustersPaginateResponseTypeDef:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/eks.html#EKS.Paginator.ListClusters.paginate)
        """


class ListFargateProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_fargate_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        clusterName: str,
        PaginationConfig: ListFargateProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListFargateProfilesPaginateResponseTypeDef:
        """
        [ListFargateProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/eks.html#EKS.Paginator.ListFargateProfiles.paginate)
        """


class ListNodegroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_nodegroups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        clusterName: str,
        PaginationConfig: ListNodegroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListNodegroupsPaginateResponseTypeDef:
        """
        [ListNodegroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/eks.html#EKS.Paginator.ListNodegroups.paginate)
        """


class ListUpdatesPaginator(Boto3Paginator):
    """
    Paginator for `list_updates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        name: str,
        nodegroupName: str = None,
        PaginationConfig: ListUpdatesPaginatePaginationConfigTypeDef = None,
    ) -> ListUpdatesPaginateResponseTypeDef:
        """
        [ListUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/eks.html#EKS.Paginator.ListUpdates.paginate)
        """
