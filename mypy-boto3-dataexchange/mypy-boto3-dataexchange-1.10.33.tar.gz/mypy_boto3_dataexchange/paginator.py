"Main interface for dataexchange service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dataexchange.type_defs import (
    ListDataSetRevisionsPaginatePaginationConfigTypeDef,
    ListDataSetRevisionsPaginateResponseTypeDef,
    ListDataSetsPaginatePaginationConfigTypeDef,
    ListDataSetsPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
    ListRevisionAssetsPaginatePaginationConfigTypeDef,
    ListRevisionAssetsPaginateResponseTypeDef,
)


__all__ = (
    "ListDataSetRevisionsPaginator",
    "ListDataSetsPaginator",
    "ListJobsPaginator",
    "ListRevisionAssetsPaginator",
)


class ListDataSetRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `list_data_set_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DataSetId: str,
        PaginationConfig: ListDataSetRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> ListDataSetRevisionsPaginateResponseTypeDef:
        """
        [ListDataSetRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions.paginate)
        """


class ListDataSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_data_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Origin: str = None,
        PaginationConfig: ListDataSetsPaginatePaginationConfigTypeDef = None,
    ) -> ListDataSetsPaginateResponseTypeDef:
        """
        [ListDataSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DataSetId: str = None,
        RevisionId: str = None,
        PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsPaginateResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs.paginate)
        """


class ListRevisionAssetsPaginator(Boto3Paginator):
    """
    Paginator for `list_revision_assets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DataSetId: str,
        RevisionId: str,
        PaginationConfig: ListRevisionAssetsPaginatePaginationConfigTypeDef = None,
    ) -> ListRevisionAssetsPaginateResponseTypeDef:
        """
        [ListRevisionAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets.paginate)
        """
