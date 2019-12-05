"Main interface for iotanalytics service Paginators"
from __future__ import annotations

from datetime import datetime
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iotanalytics.type_defs import (
    ListChannelsPaginatePaginationConfigTypeDef,
    ListChannelsPaginateResponseTypeDef,
    ListDatasetContentsPaginatePaginationConfigTypeDef,
    ListDatasetContentsPaginateResponseTypeDef,
    ListDatasetsPaginatePaginationConfigTypeDef,
    ListDatasetsPaginateResponseTypeDef,
    ListDatastoresPaginatePaginationConfigTypeDef,
    ListDatastoresPaginateResponseTypeDef,
    ListPipelinesPaginatePaginationConfigTypeDef,
    ListPipelinesPaginateResponseTypeDef,
)


__all__ = (
    "ListChannelsPaginator",
    "ListDatasetContentsPaginator",
    "ListDatasetsPaginator",
    "ListDatastoresPaginator",
    "ListPipelinesPaginator",
)


class ListChannelsPaginator(Boto3Paginator):
    """
    Paginator for `list_channels`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListChannelsPaginatePaginationConfigTypeDef = None
    ) -> ListChannelsPaginateResponseTypeDef:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListChannels.paginate)
        """


class ListDatasetContentsPaginator(Boto3Paginator):
    """
    Paginator for `list_dataset_contents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        datasetName: str,
        scheduledOnOrAfter: datetime = None,
        scheduledBefore: datetime = None,
        PaginationConfig: ListDatasetContentsPaginatePaginationConfigTypeDef = None,
    ) -> ListDatasetContentsPaginateResponseTypeDef:
        """
        [ListDatasetContents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasetContents.paginate)
        """


class ListDatasetsPaginator(Boto3Paginator):
    """
    Paginator for `list_datasets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDatasetsPaginatePaginationConfigTypeDef = None
    ) -> ListDatasetsPaginateResponseTypeDef:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasets.paginate)
        """


class ListDatastoresPaginator(Boto3Paginator):
    """
    Paginator for `list_datastores`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDatastoresPaginatePaginationConfigTypeDef = None
    ) -> ListDatastoresPaginateResponseTypeDef:
        """
        [ListDatastores.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatastores.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    Paginator for `list_pipelines`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPipelinesPaginatePaginationConfigTypeDef = None
    ) -> ListPipelinesPaginateResponseTypeDef:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListPipelines.paginate)
        """
