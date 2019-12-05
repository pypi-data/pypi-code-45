"Main interface for forecast service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_forecast.type_defs import (
    ListDatasetGroupsPaginatePaginationConfigTypeDef,
    ListDatasetGroupsPaginateResponseTypeDef,
    ListDatasetImportJobsPaginateFiltersTypeDef,
    ListDatasetImportJobsPaginatePaginationConfigTypeDef,
    ListDatasetImportJobsPaginateResponseTypeDef,
    ListDatasetsPaginatePaginationConfigTypeDef,
    ListDatasetsPaginateResponseTypeDef,
    ListForecastExportJobsPaginateFiltersTypeDef,
    ListForecastExportJobsPaginatePaginationConfigTypeDef,
    ListForecastExportJobsPaginateResponseTypeDef,
    ListForecastsPaginateFiltersTypeDef,
    ListForecastsPaginatePaginationConfigTypeDef,
    ListForecastsPaginateResponseTypeDef,
    ListPredictorsPaginateFiltersTypeDef,
    ListPredictorsPaginatePaginationConfigTypeDef,
    ListPredictorsPaginateResponseTypeDef,
)


__all__ = (
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListForecastExportJobsPaginator",
    "ListForecastsPaginator",
    "ListPredictorsPaginator",
)


class ListDatasetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_dataset_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDatasetGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListDatasetGroupsPaginateResponseTypeDef:
        """
        [ListDatasetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups.paginate)
        """


class ListDatasetImportJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_dataset_import_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListDatasetImportJobsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListDatasetImportJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListDatasetImportJobsPaginateResponseTypeDef:
        """
        [ListDatasetImportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs.paginate)
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
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/forecast.html#ForecastService.Paginator.ListDatasets.paginate)
        """


class ListForecastExportJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_forecast_export_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListForecastExportJobsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListForecastExportJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListForecastExportJobsPaginateResponseTypeDef:
        """
        [ListForecastExportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs.paginate)
        """


class ListForecastsPaginator(Boto3Paginator):
    """
    Paginator for `list_forecasts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListForecastsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListForecastsPaginatePaginationConfigTypeDef = None,
    ) -> ListForecastsPaginateResponseTypeDef:
        """
        [ListForecasts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/forecast.html#ForecastService.Paginator.ListForecasts.paginate)
        """


class ListPredictorsPaginator(Boto3Paginator):
    """
    Paginator for `list_predictors`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListPredictorsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListPredictorsPaginatePaginationConfigTypeDef = None,
    ) -> ListPredictorsPaginateResponseTypeDef:
        """
        [ListPredictors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/forecast.html#ForecastService.Paginator.ListPredictors.paginate)
        """
