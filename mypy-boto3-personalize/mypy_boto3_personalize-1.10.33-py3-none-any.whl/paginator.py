"Main interface for personalize service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_personalize.type_defs import (
    ListBatchInferenceJobsPaginatePaginationConfigTypeDef,
    ListBatchInferenceJobsPaginateResponseTypeDef,
    ListCampaignsPaginatePaginationConfigTypeDef,
    ListCampaignsPaginateResponseTypeDef,
    ListDatasetGroupsPaginatePaginationConfigTypeDef,
    ListDatasetGroupsPaginateResponseTypeDef,
    ListDatasetImportJobsPaginatePaginationConfigTypeDef,
    ListDatasetImportJobsPaginateResponseTypeDef,
    ListDatasetsPaginatePaginationConfigTypeDef,
    ListDatasetsPaginateResponseTypeDef,
    ListEventTrackersPaginatePaginationConfigTypeDef,
    ListEventTrackersPaginateResponseTypeDef,
    ListRecipesPaginatePaginationConfigTypeDef,
    ListRecipesPaginateResponseTypeDef,
    ListSchemasPaginatePaginationConfigTypeDef,
    ListSchemasPaginateResponseTypeDef,
    ListSolutionVersionsPaginatePaginationConfigTypeDef,
    ListSolutionVersionsPaginateResponseTypeDef,
    ListSolutionsPaginatePaginationConfigTypeDef,
    ListSolutionsPaginateResponseTypeDef,
)


__all__ = (
    "ListBatchInferenceJobsPaginator",
    "ListCampaignsPaginator",
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListEventTrackersPaginator",
    "ListRecipesPaginator",
    "ListSchemasPaginator",
    "ListSolutionVersionsPaginator",
    "ListSolutionsPaginator",
)


class ListBatchInferenceJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_batch_inference_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        solutionVersionArn: str = None,
        PaginationConfig: ListBatchInferenceJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListBatchInferenceJobsPaginateResponseTypeDef:
        """
        [ListBatchInferenceJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs.paginate)
        """


class ListCampaignsPaginator(Boto3Paginator):
    """
    Paginator for `list_campaigns`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        solutionArn: str = None,
        PaginationConfig: ListCampaignsPaginatePaginationConfigTypeDef = None,
    ) -> ListCampaignsPaginateResponseTypeDef:
        """
        [ListCampaigns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListCampaigns.paginate)
        """


class ListDatasetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_dataset_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDatasetGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListDatasetGroupsPaginateResponseTypeDef:
        """
        [ListDatasetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups.paginate)
        """


class ListDatasetImportJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_dataset_import_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        datasetArn: str = None,
        PaginationConfig: ListDatasetImportJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListDatasetImportJobsPaginateResponseTypeDef:
        """
        [ListDatasetImportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs.paginate)
        """


class ListDatasetsPaginator(Boto3Paginator):
    """
    Paginator for `list_datasets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        datasetGroupArn: str = None,
        PaginationConfig: ListDatasetsPaginatePaginationConfigTypeDef = None,
    ) -> ListDatasetsPaginateResponseTypeDef:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListDatasets.paginate)
        """


class ListEventTrackersPaginator(Boto3Paginator):
    """
    Paginator for `list_event_trackers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        datasetGroupArn: str = None,
        PaginationConfig: ListEventTrackersPaginatePaginationConfigTypeDef = None,
    ) -> ListEventTrackersPaginateResponseTypeDef:
        """
        [ListEventTrackers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers.paginate)
        """


class ListRecipesPaginator(Boto3Paginator):
    """
    Paginator for `list_recipes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        recipeProvider: str = None,
        PaginationConfig: ListRecipesPaginatePaginationConfigTypeDef = None,
    ) -> ListRecipesPaginateResponseTypeDef:
        """
        [ListRecipes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListRecipes.paginate)
        """


class ListSchemasPaginator(Boto3Paginator):
    """
    Paginator for `list_schemas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSchemasPaginatePaginationConfigTypeDef = None
    ) -> ListSchemasPaginateResponseTypeDef:
        """
        [ListSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListSchemas.paginate)
        """


class ListSolutionVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_solution_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        solutionArn: str = None,
        PaginationConfig: ListSolutionVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListSolutionVersionsPaginateResponseTypeDef:
        """
        [ListSolutionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions.paginate)
        """


class ListSolutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_solutions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        datasetGroupArn: str = None,
        PaginationConfig: ListSolutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListSolutionsPaginateResponseTypeDef:
        """
        [ListSolutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/personalize.html#Personalize.Paginator.ListSolutions.paginate)
        """
