"Main interface for sagemaker service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sagemaker.type_defs import (
    ListAlgorithmsPaginatePaginationConfigTypeDef,
    ListAlgorithmsPaginateResponseTypeDef,
    ListAppsPaginatePaginationConfigTypeDef,
    ListAppsPaginateResponseTypeDef,
    ListAutoMLJobsPaginatePaginationConfigTypeDef,
    ListAutoMLJobsPaginateResponseTypeDef,
    ListCandidatesForAutoMLJobPaginatePaginationConfigTypeDef,
    ListCandidatesForAutoMLJobPaginateResponseTypeDef,
    ListCodeRepositoriesPaginatePaginationConfigTypeDef,
    ListCodeRepositoriesPaginateResponseTypeDef,
    ListCompilationJobsPaginatePaginationConfigTypeDef,
    ListCompilationJobsPaginateResponseTypeDef,
    ListDomainsPaginatePaginationConfigTypeDef,
    ListDomainsPaginateResponseTypeDef,
    ListEndpointConfigsPaginatePaginationConfigTypeDef,
    ListEndpointConfigsPaginateResponseTypeDef,
    ListEndpointsPaginatePaginationConfigTypeDef,
    ListEndpointsPaginateResponseTypeDef,
    ListExperimentsPaginatePaginationConfigTypeDef,
    ListExperimentsPaginateResponseTypeDef,
    ListFlowDefinitionsPaginatePaginationConfigTypeDef,
    ListFlowDefinitionsPaginateResponseTypeDef,
    ListHumanTaskUisPaginatePaginationConfigTypeDef,
    ListHumanTaskUisPaginateResponseTypeDef,
    ListHyperParameterTuningJobsPaginatePaginationConfigTypeDef,
    ListHyperParameterTuningJobsPaginateResponseTypeDef,
    ListLabelingJobsForWorkteamPaginatePaginationConfigTypeDef,
    ListLabelingJobsForWorkteamPaginateResponseTypeDef,
    ListLabelingJobsPaginatePaginationConfigTypeDef,
    ListLabelingJobsPaginateResponseTypeDef,
    ListModelPackagesPaginatePaginationConfigTypeDef,
    ListModelPackagesPaginateResponseTypeDef,
    ListModelsPaginatePaginationConfigTypeDef,
    ListModelsPaginateResponseTypeDef,
    ListMonitoringExecutionsPaginatePaginationConfigTypeDef,
    ListMonitoringExecutionsPaginateResponseTypeDef,
    ListMonitoringSchedulesPaginatePaginationConfigTypeDef,
    ListMonitoringSchedulesPaginateResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsPaginatePaginationConfigTypeDef,
    ListNotebookInstanceLifecycleConfigsPaginateResponseTypeDef,
    ListNotebookInstancesPaginatePaginationConfigTypeDef,
    ListNotebookInstancesPaginateResponseTypeDef,
    ListProcessingJobsPaginatePaginationConfigTypeDef,
    ListProcessingJobsPaginateResponseTypeDef,
    ListSubscribedWorkteamsPaginatePaginationConfigTypeDef,
    ListSubscribedWorkteamsPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
    ListTrainingJobsForHyperParameterTuningJobPaginatePaginationConfigTypeDef,
    ListTrainingJobsForHyperParameterTuningJobPaginateResponseTypeDef,
    ListTrainingJobsPaginatePaginationConfigTypeDef,
    ListTrainingJobsPaginateResponseTypeDef,
    ListTransformJobsPaginatePaginationConfigTypeDef,
    ListTransformJobsPaginateResponseTypeDef,
    ListTrialComponentsPaginatePaginationConfigTypeDef,
    ListTrialComponentsPaginateResponseTypeDef,
    ListTrialsPaginatePaginationConfigTypeDef,
    ListTrialsPaginateResponseTypeDef,
    ListUserProfilesPaginatePaginationConfigTypeDef,
    ListUserProfilesPaginateResponseTypeDef,
    ListWorkteamsPaginatePaginationConfigTypeDef,
    ListWorkteamsPaginateResponseTypeDef,
    SearchPaginatePaginationConfigTypeDef,
    SearchPaginateResponseTypeDef,
    SearchPaginateSearchExpressionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAlgorithmsPaginator",
    "ListAppsPaginator",
    "ListAutoMLJobsPaginator",
    "ListCandidatesForAutoMLJobPaginator",
    "ListCodeRepositoriesPaginator",
    "ListCompilationJobsPaginator",
    "ListDomainsPaginator",
    "ListEndpointConfigsPaginator",
    "ListEndpointsPaginator",
    "ListExperimentsPaginator",
    "ListFlowDefinitionsPaginator",
    "ListHumanTaskUisPaginator",
    "ListHyperParameterTuningJobsPaginator",
    "ListLabelingJobsPaginator",
    "ListLabelingJobsForWorkteamPaginator",
    "ListModelPackagesPaginator",
    "ListModelsPaginator",
    "ListMonitoringExecutionsPaginator",
    "ListMonitoringSchedulesPaginator",
    "ListNotebookInstanceLifecycleConfigsPaginator",
    "ListNotebookInstancesPaginator",
    "ListProcessingJobsPaginator",
    "ListSubscribedWorkteamsPaginator",
    "ListTagsPaginator",
    "ListTrainingJobsPaginator",
    "ListTrainingJobsForHyperParameterTuningJobPaginator",
    "ListTransformJobsPaginator",
    "ListTrialComponentsPaginator",
    "ListTrialsPaginator",
    "ListUserProfilesPaginator",
    "ListWorkteamsPaginator",
    "SearchPaginator",
)


class ListAlgorithmsPaginator(Boto3Paginator):
    """
    Paginator for `list_algorithms`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListAlgorithmsPaginatePaginationConfigTypeDef = None,
    ) -> ListAlgorithmsPaginateResponseTypeDef:
        """
        [ListAlgorithms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms.paginate)
        """


class ListAppsPaginator(Boto3Paginator):
    """
    Paginator for `list_apps`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: str = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
        PaginationConfig: ListAppsPaginatePaginationConfigTypeDef = None,
    ) -> ListAppsPaginateResponseTypeDef:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListApps.paginate)
        """


class ListAutoMLJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_auto_ml_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        PaginationConfig: ListAutoMLJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListAutoMLJobsPaginateResponseTypeDef:
        """
        [ListAutoMLJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs.paginate)
        """


class ListCandidatesForAutoMLJobPaginator(Boto3Paginator):
    """
    Paginator for `list_candidates_for_auto_ml_job`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoMLJobName: str,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        CandidateNameEquals: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        PaginationConfig: ListCandidatesForAutoMLJobPaginatePaginationConfigTypeDef = None,
    ) -> ListCandidatesForAutoMLJobPaginateResponseTypeDef:
        """
        [ListCandidatesForAutoMLJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob.paginate)
        """


class ListCodeRepositoriesPaginator(Boto3Paginator):
    """
    Paginator for `list_code_repositories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListCodeRepositoriesPaginatePaginationConfigTypeDef = None,
    ) -> ListCodeRepositoriesPaginateResponseTypeDef:
        """
        [ListCodeRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories.paginate)
        """


class ListCompilationJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_compilation_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListCompilationJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListCompilationJobsPaginateResponseTypeDef:
        """
        [ListCompilationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs.paginate)
        """


class ListDomainsPaginator(Boto3Paginator):
    """
    Paginator for `list_domains`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDomainsPaginatePaginationConfigTypeDef = None
    ) -> ListDomainsPaginateResponseTypeDef:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains.paginate)
        """


class ListEndpointConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_endpoint_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: ListEndpointConfigsPaginatePaginationConfigTypeDef = None,
    ) -> ListEndpointConfigsPaginateResponseTypeDef:
        """
        [ListEndpointConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs.paginate)
        """


class ListEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `list_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ] = None,
        PaginationConfig: ListEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> ListEndpointsPaginateResponseTypeDef:
        """
        [ListEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints.paginate)
        """


class ListExperimentsPaginator(Boto3Paginator):
    """
    Paginator for `list_experiments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListExperimentsPaginatePaginationConfigTypeDef = None,
    ) -> ListExperimentsPaginateResponseTypeDef:
        """
        [ListExperiments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments.paginate)
        """


class ListFlowDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_flow_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListFlowDefinitionsPaginatePaginationConfigTypeDef = None,
    ) -> ListFlowDefinitionsPaginateResponseTypeDef:
        """
        [ListFlowDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions.paginate)
        """


class ListHumanTaskUisPaginator(Boto3Paginator):
    """
    Paginator for `list_human_task_uis`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListHumanTaskUisPaginatePaginationConfigTypeDef = None,
    ) -> ListHumanTaskUisPaginateResponseTypeDef:
        """
        [ListHumanTaskUis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis.paginate)
        """


class ListHyperParameterTuningJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_hyper_parameter_tuning_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "Status", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        PaginationConfig: ListHyperParameterTuningJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListHyperParameterTuningJobsPaginateResponseTypeDef:
        """
        [ListHyperParameterTuningJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs.paginate)
        """


class ListLabelingJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_labeling_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        PaginationConfig: ListLabelingJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListLabelingJobsPaginateResponseTypeDef:
        """
        [ListLabelingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs.paginate)
        """


class ListLabelingJobsForWorkteamPaginator(Boto3Paginator):
    """
    Paginator for `list_labeling_jobs_for_workteam`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkteamArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListLabelingJobsForWorkteamPaginatePaginationConfigTypeDef = None,
    ) -> ListLabelingJobsForWorkteamPaginateResponseTypeDef:
        """
        [ListLabelingJobsForWorkteam.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam.paginate)
        """


class ListModelPackagesPaginator(Boto3Paginator):
    """
    Paginator for `list_model_packages`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListModelPackagesPaginatePaginationConfigTypeDef = None,
    ) -> ListModelPackagesPaginateResponseTypeDef:
        """
        [ListModelPackages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages.paginate)
        """


class ListModelsPaginator(Boto3Paginator):
    """
    Paginator for `list_models`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: ListModelsPaginatePaginationConfigTypeDef = None,
    ) -> ListModelsPaginateResponseTypeDef:
        """
        [ListModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListModels.paginate)
        """


class ListMonitoringExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_monitoring_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: Literal["CreationTime", "ScheduledTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        ScheduledTimeBefore: datetime = None,
        ScheduledTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "Pending",
            "Completed",
            "CompletedWithViolations",
            "InProgress",
            "Failed",
            "Stopping",
            "Stopped",
        ] = None,
        PaginationConfig: ListMonitoringExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListMonitoringExecutionsPaginateResponseTypeDef:
        """
        [ListMonitoringExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions.paginate)
        """


class ListMonitoringSchedulesPaginator(Boto3Paginator):
    """
    Paginator for `list_monitoring_schedules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EndpointName: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal["Pending", "Failed", "Scheduled", "Stopped"] = None,
        PaginationConfig: ListMonitoringSchedulesPaginatePaginationConfigTypeDef = None,
    ) -> ListMonitoringSchedulesPaginateResponseTypeDef:
        """
        [ListMonitoringSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules.paginate)
        """


class ListNotebookInstanceLifecycleConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_notebook_instance_lifecycle_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        PaginationConfig: ListNotebookInstanceLifecycleConfigsPaginatePaginationConfigTypeDef = None,
    ) -> ListNotebookInstanceLifecycleConfigsPaginateResponseTypeDef:
        """
        [ListNotebookInstanceLifecycleConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs.paginate)
        """


class ListNotebookInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_notebook_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ] = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None,
        PaginationConfig: ListNotebookInstancesPaginatePaginationConfigTypeDef = None,
    ) -> ListNotebookInstancesPaginateResponseTypeDef:
        """
        [ListNotebookInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances.paginate)
        """


class ListProcessingJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_processing_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListProcessingJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListProcessingJobsPaginateResponseTypeDef:
        """
        [ListProcessingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs.paginate)
        """


class ListSubscribedWorkteamsPaginator(Boto3Paginator):
    """
    Paginator for `list_subscribed_workteams`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        NameContains: str = None,
        PaginationConfig: ListSubscribedWorkteamsPaginatePaginationConfigTypeDef = None,
    ) -> ListSubscribedWorkteamsPaginateResponseTypeDef:
        """
        [ListSubscribedWorkteams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceArn: str, PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None
    ) -> ListTagsPaginateResponseTypeDef:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListTags.paginate)
        """


class ListTrainingJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_training_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListTrainingJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListTrainingJobsPaginateResponseTypeDef:
        """
        [ListTrainingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs.paginate)
        """


class ListTrainingJobsForHyperParameterTuningJobPaginator(Boto3Paginator):
    """
    Paginator for `list_training_jobs_for_hyper_parameter_tuning_job`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HyperParameterTuningJobName: str,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListTrainingJobsForHyperParameterTuningJobPaginatePaginationConfigTypeDef = None,
    ) -> ListTrainingJobsForHyperParameterTuningJobPaginateResponseTypeDef:
        """
        [ListTrainingJobsForHyperParameterTuningJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob.paginate)
        """


class ListTransformJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_transform_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListTransformJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListTransformJobsPaginateResponseTypeDef:
        """
        [ListTransformJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs.paginate)
        """


class ListTrialComponentsPaginator(Boto3Paginator):
    """
    Paginator for `list_trial_components`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceArn: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListTrialComponentsPaginatePaginationConfigTypeDef = None,
    ) -> ListTrialComponentsPaginateResponseTypeDef:
        """
        [ListTrialComponents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents.paginate)
        """


class ListTrialsPaginator(Boto3Paginator):
    """
    Paginator for `list_trials`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ExperimentName: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: ListTrialsPaginatePaginationConfigTypeDef = None,
    ) -> ListTrialsPaginateResponseTypeDef:
        """
        [ListTrials.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials.paginate)
        """


class ListUserProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_user_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "LastModifiedTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
        PaginationConfig: ListUserProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListUserProfilesPaginateResponseTypeDef:
        """
        [ListUserProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles.paginate)
        """


class ListWorkteamsPaginator(Boto3Paginator):
    """
    Paginator for `list_workteams`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SortBy: Literal["Name", "CreateDate"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        PaginationConfig: ListWorkteamsPaginatePaginationConfigTypeDef = None,
    ) -> ListWorkteamsPaginateResponseTypeDef:
        """
        [ListWorkteams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams.paginate)
        """


class SearchPaginator(Boto3Paginator):
    """
    Paginator for `search`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Resource: Literal[
            "TrainingJob", "Experiment", "ExperimentTrial", "ExperimentTrialComponent"
        ],
        SearchExpression: SearchPaginateSearchExpressionTypeDef = None,
        SortBy: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: SearchPaginatePaginationConfigTypeDef = None,
    ) -> SearchPaginateResponseTypeDef:
        """
        [Search.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Paginator.Search.paginate)
        """
