"Main interface for sagemaker service Paginators"
from __future__ import annotations

from datetime import datetime
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_algorithms`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListAlgorithms>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only algorithms created after the specified time (timestamp).

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only algorithms created before the specified time (timestamp).

        :type NameContains: string
        :param NameContains:

          A string in the algorithm name. This filter returns only algorithms whose name contains
          the specified string.

        :type SortBy: string
        :param SortBy:

          The parameter by which to sort the results. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for the results. The default is ``Ascending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AlgorithmSummaryList': [
                    {
                        'AlgorithmName': 'string',
                        'AlgorithmArn': 'string',
                        'AlgorithmDescription': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'AlgorithmStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **AlgorithmSummaryList** *(list) --*

              >An array of ``AlgorithmSummary`` objects, each of which lists an algorithm.

              - *(dict) --*

                Provides summary information about an algorithm.

                - **AlgorithmName** *(string) --*

                  The name of the algorithm that is described by the summary.

                - **AlgorithmArn** *(string) --*

                  The Amazon Resource Name (ARN) of the algorithm.

                - **AlgorithmDescription** *(string) --*

                  A brief description of the algorithm.

                - **CreationTime** *(datetime) --*

                  A timestamp that shows when the algorithm was created.

                - **AlgorithmStatus** *(string) --*

                  The overall status of the algorithm.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_apps`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListApps>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortOrder='Ascending'|'Descending',
              SortBy='CreationTime',
              DomainIdEquals='string',
              UserProfileNameEquals='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortOrder: string
        :param SortOrder:

          The sort order for the results. The default is Ascending.

        :type SortBy: string
        :param SortBy:

          The parameter by which to sort the results. The default is CreationTime.

        :type DomainIdEquals: string
        :param DomainIdEquals:

          A parameter to search for the domain ID.

        :type UserProfileNameEquals: string
        :param UserProfileNameEquals:

          A parameter to search by user profile name.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Apps': [
                    {
                        'DomainId': 'string',
                        'UserProfileName': 'string',
                        'AppType': 'JupyterServer'|'KernelGateway'|'TensorBoard',
                        'AppName': 'string',
                        'Status': 'Deleted'|'Deleting'|'Failed'|'InService'|'Pending',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Apps** *(list) --*

              The list of apps.

              - *(dict) --*

                The app's details.

                - **DomainId** *(string) --*

                  The domain ID.

                - **UserProfileName** *(string) --*

                  The user profile name.

                - **AppType** *(string) --*

                  The type of app.

                - **AppName** *(string) --*

                  The name of the app.

                - **Status** *(string) --*

                  The status.

                - **CreationTime** *(datetime) --*

                  The creation time.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_auto_ml_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListAutoMLJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
              SortOrder='Ascending'|'Descending',
              SortBy='Name'|'CreationTime'|'Status',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          Request a list of jobs, using a filter for time.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          Request a list of jobs, using a filter for time.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          Request a list of jobs, using a filter for time.

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          Request a list of jobs, using a filter for time.

        :type NameContains: string
        :param NameContains:

          Request a list of jobs, using a search filter for name.

        :type StatusEquals: string
        :param StatusEquals:

          Request a list of jobs, using a filter for status.

        :type SortOrder: string
        :param SortOrder:

          The sort order for the results. The default is Descending.

        :type SortBy: string
        :param SortBy:

          The parameter by which to sort the results. The default is AutoMLJobName.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AutoMLJobSummaries': [
                    {
                        'AutoMLJobName': 'string',
                        'AutoMLJobArn': 'string',
                        'AutoMLJobStatus': 'Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
                        'AutoMLJobSecondaryStatus':
                        'Starting'|'AnalyzingData'|'FeatureEngineering'
                        |'ModelTuning'|'MaxCandidatesReached'|'Failed'|'Stopped'
                        |'MaxAutoMLJobRuntimeReached'|'Stopping'
                        |'CandidateDefinitionsGenerated',
                        'CreationTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'FailureReason': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **AutoMLJobSummaries** *(list) --*

              Returns a summary list of jobs.

              - *(dict) --*

                Provides a summary about a job.

                - **AutoMLJobName** *(string) --*

                  The name of the object you are requesting.

                - **AutoMLJobArn** *(string) --*

                  The ARN of the job.

                - **AutoMLJobStatus** *(string) --*

                  The job's status.

                - **AutoMLJobSecondaryStatus** *(string) --*

                  The job's secondary status.

                - **CreationTime** *(datetime) --*

                  When the job was created.

                - **EndTime** *(datetime) --*

                  The end time.

                - **LastModifiedTime** *(datetime) --*

                  When the job was last modified.

                - **FailureReason** *(string) --*

                  The failure reason.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_candidates_for_auto_ml_job`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListCandidatesForAutoMLJob>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              AutoMLJobName='string',
              StatusEquals='Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
              CandidateNameEquals='string',
              SortOrder='Ascending'|'Descending',
              SortBy='CreationTime'|'Status'|'FinalObjectiveMetricValue',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type AutoMLJobName: string
        :param AutoMLJobName: **[REQUIRED]**

          List the Candidates created for the job by providing the job's name.

        :type StatusEquals: string
        :param StatusEquals:

          List the Candidates for the job and filter by status.

        :type CandidateNameEquals: string
        :param CandidateNameEquals:

          List the Candidates for the job and filter by candidate name.

        :type SortOrder: string
        :param SortOrder:

          The sort order for the results. The default is Ascending.

        :type SortBy: string
        :param SortBy:

          The parameter by which to sort the results. The default is Descending.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Candidates': [
                    {
                        'CandidateName': 'string',
                        'FinalAutoMLJobObjectiveMetric': {
                            'Type': 'Maximize'|'Minimize',
                            'MetricName': 'Accuracy'|'MSE'|'F1'|'F1macro',
                            'Value': ...
                        },
                        'ObjectiveStatus': 'Succeeded'|'Pending'|'Failed',
                        'CandidateSteps': [
                            {
                                'CandidateStepType':
                                'AWS::SageMaker::TrainingJob'
                                |'AWS::SageMaker::TransformJob'
                                |'AWS::SageMaker::ProcessingJob',
                                'CandidateStepArn': 'string',
                                'CandidateStepName': 'string'
                            },
                        ],
                        'CandidateStatus': 'Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
                        'InferenceContainers': [
                            {
                                'Image': 'string',
                                'ModelDataUrl': 'string',
                                'Environment': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'CreationTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'FailureReason': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Candidates** *(list) --*

              Summaries about the Candidates.

              - *(dict) --*

                An AutoPilot job will return recommendations, or candidates. Each candidate has
                futher details about the steps involed, and the status.

                - **CandidateName** *(string) --*

                  The candidate name.

                - **FinalAutoMLJobObjectiveMetric** *(dict) --*

                  The candidate result from a job.

                  - **Type** *(string) --*

                    The metric type used.

                  - **MetricName** *(string) --*

                    The name of the metric.

                  - **Value** *(float) --*

                    The value of the metric.

                - **ObjectiveStatus** *(string) --*

                  The objective status.

                - **CandidateSteps** *(list) --*

                  The candidate's steps.

                  - *(dict) --*

                    Information about the steps for a Candidate, and what step it is working on.

                    - **CandidateStepType** *(string) --*

                      Whether the Candidate is at the transform, training, or processing step.

                    - **CandidateStepArn** *(string) --*

                      The ARN for the Candidate's step.

                    - **CandidateStepName** *(string) --*

                      The name for the Candidate's step.

                - **CandidateStatus** *(string) --*

                  The candidate's status.

                - **InferenceContainers** *(list) --*

                  The inference containers.

                  - *(dict) --*

                    A list of container definitions that describe the different containers that make
                    up one AutoML candidate. Refer to ContainerDefinition for more details.

                    - **Image** *(string) --*

                      The ECR path of the container. Refer to ContainerDefinition for more details.

                    - **ModelDataUrl** *(string) --*

                      The location of the model artifacts. Refer to ContainerDefinition for more
                      details.

                    - **Environment** *(dict) --*

                      Environment variables to set in the container. Refer to ContainerDefinition
                      for more details.

                      - *(string) --*

                        - *(string) --*

                - **CreationTime** *(datetime) --*

                  The creation time.

                - **EndTime** *(datetime) --*

                  The end time.

                - **LastModifiedTime** *(datetime) --*

                  The last modified time.

                - **FailureReason** *(string) --*

                  The failure reason.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_code_repositories`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListCodeRepositories>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              SortBy='Name'|'CreationTime'|'LastModifiedTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only Git repositories that were created after the specified time.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only Git repositories that were created before the specified time.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only Git repositories that were last modified after the specified
          time.

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only Git repositories that were last modified before the specified
          time.

        :type NameContains: string
        :param NameContains:

          A string in the Git repositories name. This filter returns only repositories whose name
          contains the specified string.

        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``Name`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CodeRepositorySummaryList': [
                    {
                        'CodeRepositoryName': 'string',
                        'CodeRepositoryArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'GitConfig': {
                            'RepositoryUrl': 'string',
                            'Branch': 'string',
                            'SecretArn': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **CodeRepositorySummaryList** *(list) --*

              Gets a list of summaries of the Git repositories. Each summary specifies the following
              values for the repository:

              * Name

              * Amazon Resource Name (ARN)

              * Creation time

              * Last modified time

              * Configuration information, including the URL location of the repository and the ARN
              of the AWS Secrets Manager secret that contains the credentials used to access the
              repository.

              - *(dict) --*

                Specifies summary information about a Git repository.

                - **CodeRepositoryName** *(string) --*

                  The name of the Git repository.

                - **CodeRepositoryArn** *(string) --*

                  The Amazon Resource Name (ARN) of the Git repository.

                - **CreationTime** *(datetime) --*

                  The date and time that the Git repository was created.

                - **LastModifiedTime** *(datetime) --*

                  The date and time that the Git repository was last modified.

                - **GitConfig** *(dict) --*

                  Configuration details for the Git repository, including the URL where it is
                  located and the ARN of the AWS Secrets Manager secret that contains the
                  credentials used to access the repository.

                  - **RepositoryUrl** *(string) --*

                    The URL where the Git repository is located.

                  - **Branch** *(string) --*

                    The default branch for the Git repository.

                  - **SecretArn** *(string) --*

                    The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains
                    the credentials used to access the git repository. The secret must have a
                    staging label of ``AWSCURRENT`` and must be in the following format:

                     ``{"username": *UserName* , "password": *Password* }``
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_compilation_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListCompilationJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns the model compilation jobs that were created after a specified time.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns the model compilation jobs that were created before a specified
          time.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns the model compilation jobs that were modified after a specified
          time.

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns the model compilation jobs that were modified before a specified
          time.

        :type NameContains: string
        :param NameContains:

          A filter that returns the model compilation jobs whose name contains a specified string.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that retrieves model compilation jobs with a specific
          DescribeCompilationJobResponse$CompilationJobStatus status.

        :type SortBy: string
        :param SortBy:

          The field by which to sort results. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CompilationJobSummaries': [
                    {
                        'CompilationJobName': 'string',
                        'CompilationJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'CompilationStartTime': datetime(2015, 1, 1),
                        'CompilationEndTime': datetime(2015, 1, 1),
                        'CompilationTargetDevice':
                        'lambda'|'ml_m4'|'ml_m5'|'ml_c4'|'ml_c5'|'ml_p2'|'ml_p3'
                        |'ml_inf1'|'jetson_tx1'|'jetson_tx2'|'jetson_nano'|'rasp3b'
                        |'deeplens'|'rk3399'|'rk3288'|'aisage'|'sbe_c'|'qcs605'
                        |'qcs603',
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'CompilationJobStatus':
                        'INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'
                        |'STOPPED'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **CompilationJobSummaries** *(list) --*

              An array of  CompilationJobSummary objects, each describing a model compilation job.

              - *(dict) --*

                A summary of a model compilation job.

                - **CompilationJobName** *(string) --*

                  The name of the model compilation job that you want a summary for.

                - **CompilationJobArn** *(string) --*

                  The Amazon Resource Name (ARN) of the model compilation job.

                - **CreationTime** *(datetime) --*

                  The time when the model compilation job was created.

                - **CompilationStartTime** *(datetime) --*

                  The time when the model compilation job started.

                - **CompilationEndTime** *(datetime) --*

                  The time when the model compilation job completed.

                - **CompilationTargetDevice** *(string) --*

                  The type of device that the model will run on after compilation has completed.

                - **LastModifiedTime** *(datetime) --*

                  The time when the model compilation job was last modified.

                - **CompilationJobStatus** *(string) --*

                  The status of the model compilation job.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_domains`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListDomains>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Domains': [
                    {
                        'DomainArn': 'string',
                        'DomainId': 'string',
                        'DomainName': 'string',
                        'Status': 'Deleting'|'Failed'|'InService'|'Pending',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'Url': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Domains** *(list) --*

              The list of domains.

              - *(dict) --*

                The domain's details.

                - **DomainArn** *(string) --*

                  The domain's Amazon Resource Name (ARN).

                - **DomainId** *(string) --*

                  The domain ID.

                - **DomainName** *(string) --*

                  The domain name.

                - **Status** *(string) --*

                  The status.

                - **CreationTime** *(datetime) --*

                  The creation time.

                - **LastModifiedTime** *(datetime) --*

                  The last modified time.

                - **Url** *(string) --*

                  The domain's URL.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_endpoint_configs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpointConfigs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Descending`` .

        :type NameContains: string
        :param NameContains:

          A string in the endpoint configuration name. This filter returns only endpoint
          configurations whose name contains the specified string.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only endpoint configurations created before the specified time
          (timestamp).

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only endpoint configurations with a creation time greater than or
          equal to the specified time (timestamp).

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EndpointConfigs': [
                    {
                        'EndpointConfigName': 'string',
                        'EndpointConfigArn': 'string',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **EndpointConfigs** *(list) --*

              An array of endpoint configurations.

              - *(dict) --*

                Provides summary information for an endpoint configuration.

                - **EndpointConfigName** *(string) --*

                  The name of the endpoint configuration.

                - **EndpointConfigArn** *(string) --*

                  The Amazon Resource Name (ARN) of the endpoint configuration.

                - **CreationTime** *(datetime) --*

                  A timestamp that shows when the endpoint configuration was created.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_endpoints`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpoints>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals=
                  'OutOfService'|'Creating'|'Updating'|'SystemUpdating'|'RollingBack'|'InService'
                  |'Deleting'|'Failed',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortBy: string
        :param SortBy:

          Sorts the list of results. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Descending`` .

        :type NameContains: string
        :param NameContains:

          A string in endpoint names. This filter returns only endpoints whose name contains the
          specified string.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only endpoints that were created before the specified time
          (timestamp).

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only endpoints with a creation time greater than or equal to the
          specified time (timestamp).

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only endpoints that were modified before the specified timestamp.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only endpoints that were modified after the specified timestamp.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that returns only endpoints with the specified status.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Endpoints': [
                    {
                        'EndpointName': 'string',
                        'EndpointArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'EndpointStatus':
                        'OutOfService'|'Creating'|'Updating'|'SystemUpdating'
                        |'RollingBack'|'InService'|'Deleting'|'Failed'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Endpoints** *(list) --*

              An array or endpoint objects.

              - *(dict) --*

                Provides summary information for an endpoint.

                - **EndpointName** *(string) --*

                  The name of the endpoint.

                - **EndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) of the endpoint.

                - **CreationTime** *(datetime) --*

                  A timestamp that shows when the endpoint was created.

                - **LastModifiedTime** *(datetime) --*

                  A timestamp that shows when the endpoint was last modified.

                - **EndpointStatus** *(string) --*

                  The status of the endpoint.

                  * ``OutOfService`` : Endpoint is not available to take incoming requests.

                  * ``Creating`` :  CreateEndpoint is executing.

                  * ``Updating`` :  UpdateEndpoint or  UpdateEndpointWeightsAndCapacities is
                  executing.

                  * ``SystemUpdating`` : Endpoint is undergoing maintenance and cannot be updated or
                  deleted or re-scaled until it has completed. This maintenance operation does not
                  change any customer-specified values such as VPC config, KMS encryption, model,
                  instance type, or instance count.

                  * ``RollingBack`` : Endpoint fails to scale up or down or change its variant
                  weight and is in the process of rolling back to its previous configuration. Once
                  the rollback completes, endpoint returns to an ``InService`` status. This
                  transitional status only applies to an endpoint that has autoscaling enabled and
                  is undergoing variant weight or capacity changes as part of an
                  UpdateEndpointWeightsAndCapacities call or when the
                  UpdateEndpointWeightsAndCapacities operation is called explicitly.

                  * ``InService`` : Endpoint is available to process incoming requests.

                  * ``Deleting`` :  DeleteEndpoint is executing.

                  * ``Failed`` : Endpoint could not be created, updated, or re-scaled. Use
                  DescribeEndpointOutput$FailureReason for information about the failure.
                  DeleteEndpoint is the only operation that can be performed on a failed endpoint.

                  To get a list of endpoints with a specified status, use the
                  ListEndpointsInput$StatusEquals filter.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_experiments`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListExperiments>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreatedAfter=datetime(2015, 1, 1),
              CreatedBefore=datetime(2015, 1, 1),
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreatedAfter: datetime
        :param CreatedAfter:

          A filter that returns only experiments created after the specified time.

        :type CreatedBefore: datetime
        :param CreatedBefore:

          A filter that returns only experiments created before the specified time.

        :type SortBy: string
        :param SortBy:

          The property used to sort results. The default value is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order. The default value is ``Descending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ExperimentSummaries': [
                    {
                        'ExperimentArn': 'string',
                        'ExperimentName': 'string',
                        'DisplayName': 'string',
                        'ExperimentSource': {
                            'SourceArn': 'string',
                            'SourceType': 'string'
                        },
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ExperimentSummaries** *(list) --*

              A list of the summaries of your experiments.

              - *(dict) --*

                A summary of the properties of an experiment. To get the complete set of properties,
                call the  DescribeExperiment API and provide the ``ExperimentName`` .

                - **ExperimentArn** *(string) --*

                  The Amazon Resource Name (ARN) of the experiment.

                - **ExperimentName** *(string) --*

                  The name of the experiment.

                - **DisplayName** *(string) --*

                  The name of the experiment as displayed. If ``DisplayName`` isn't specified,
                  ``ExperimentName`` is displayed.

                - **ExperimentSource** *(dict) --*

                  The source of the experiment.

                  - **SourceArn** *(string) --*

                    The Amazon Resource Name (ARN) of the source.

                  - **SourceType** *(string) --*

                    The source type.

                - **CreationTime** *(datetime) --*

                  When the experiment was created.

                - **LastModifiedTime** *(datetime) --*

                  When the experiment was last modified.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_flow_definitions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListFlowDefinitions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only flow definitions with a creation time greater than or equal to
          the specified timestamp.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only flow definitions that were created before the specified
          timestamp.

        :type SortOrder: string
        :param SortOrder:

          An optional value that specifies whether you want the results sorted in ``Ascending`` or
          ``Descending`` order.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FlowDefinitionSummaries': [
                    {
                        'FlowDefinitionName': 'string',
                        'FlowDefinitionArn': 'string',
                        'FlowDefinitionStatus':
                        'Initializing'|'Active'|'Failed'|'Deleting'|'Deleted',
                        'CreationTime': datetime(2015, 1, 1),
                        'FailureReason': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **FlowDefinitionSummaries** *(list) --*

              An array of objects describing the flow definitions.

              - *(dict) --*

                Contains summary information about the flow definition.

                - **FlowDefinitionName** *(string) --*

                  The name of the flow definition.

                - **FlowDefinitionArn** *(string) --*

                  The Amazon Resource Name (ARN) of the flow definition.

                - **FlowDefinitionStatus** *(string) --*

                  The status of the flow definition. Valid values:

                - **CreationTime** *(datetime) --*

                  The timestamp when SageMaker created the flow definition.

                - **FailureReason** *(string) --*

                  The reason why the flow definition creation failed. A failure reason is returned
                  only when the flow definition status is ``Failed`` .
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_human_task_uis`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListHumanTaskUis>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only human task user interfaces with a creation time greater than or
          equal to the specified timestamp.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only human task user interfaces that were created before the
          specified timestamp.

        :type SortOrder: string
        :param SortOrder:

          An optional value that specifies whether you want the results sorted in ``Ascending`` or
          ``Descending`` order.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HumanTaskUiSummaries': [
                    {
                        'HumanTaskUiName': 'string',
                        'HumanTaskUiArn': 'string',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **HumanTaskUiSummaries** *(list) --*

              An array of objects describing the human task user interfaces.

              - *(dict) --*

                Container for human task user interface information.

                - **HumanTaskUiName** *(string) --*

                  The name of the human task user interface.

                - **HumanTaskUiArn** *(string) --*

                  The Amazon Resource Name (ARN) of the human task user interface.

                - **CreationTime** *(datetime) --*

                  A timestamp when SageMaker created the human task user interface.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_hyper_parameter_tuning_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListHyperParameterTuningJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortBy='Name'|'Status'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              StatusEquals='Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``Name`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type NameContains: string
        :param NameContains:

          A string in the tuning job name. This filter returns only tuning jobs whose name contains
          the specified string.

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only tuning jobs that were created after the specified time.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only tuning jobs that were created before the specified time.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only tuning jobs that were modified after the specified time.

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only tuning jobs that were modified before the specified time.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that returns only tuning jobs with the specified status.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HyperParameterTuningJobSummaries': [
                    {
                        'HyperParameterTuningJobName': 'string',
                        'HyperParameterTuningJobArn': 'string',
                        'HyperParameterTuningJobStatus':
                        'Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
                        'Strategy': 'Bayesian'|'Random',
                        'CreationTime': datetime(2015, 1, 1),
                        'HyperParameterTuningEndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'TrainingJobStatusCounters': {
                            'Completed': 123,
                            'InProgress': 123,
                            'RetryableError': 123,
                            'NonRetryableError': 123,
                            'Stopped': 123
                        },
                        'ObjectiveStatusCounters': {
                            'Succeeded': 123,
                            'Pending': 123,
                            'Failed': 123
                        },
                        'ResourceLimits': {
                            'MaxNumberOfTrainingJobs': 123,
                            'MaxParallelTrainingJobs': 123
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **HyperParameterTuningJobSummaries** *(list) --*

              A list of  HyperParameterTuningJobSummary objects that describe the tuning jobs that
              the ``ListHyperParameterTuningJobs`` request returned.

              - *(dict) --*

                Provides summary information about a hyperparameter tuning job.

                - **HyperParameterTuningJobName** *(string) --*

                  The name of the tuning job.

                - **HyperParameterTuningJobArn** *(string) --*

                  The Amazon Resource Name (ARN) of the tuning job.

                - **HyperParameterTuningJobStatus** *(string) --*

                  The status of the tuning job.

                - **Strategy** *(string) --*

                  Specifies the search strategy hyperparameter tuning uses to choose which
                  hyperparameters to use for each iteration. Currently, the only valid value is
                  Bayesian.

                - **CreationTime** *(datetime) --*

                  The date and time that the tuning job was created.

                - **HyperParameterTuningEndTime** *(datetime) --*

                  The date and time that the tuning job ended.

                - **LastModifiedTime** *(datetime) --*

                  The date and time that the tuning job was modified.

                - **TrainingJobStatusCounters** *(dict) --*

                  The  TrainingJobStatusCounters object that specifies the numbers of training jobs,
                  categorized by status, that this tuning job launched.

                  - **Completed** *(integer) --*

                    The number of completed training jobs launched by the hyperparameter tuning job.

                  - **InProgress** *(integer) --*

                    The number of in-progress training jobs launched by a hyperparameter tuning job.

                  - **RetryableError** *(integer) --*

                    The number of training jobs that failed, but can be retried. A failed training
                    job can be retried only if it failed because an internal service error occurred.

                  - **NonRetryableError** *(integer) --*

                    The number of training jobs that failed and can't be retried. A failed training
                    job can't be retried if it failed because a client error occurred.

                  - **Stopped** *(integer) --*

                    The number of training jobs launched by a hyperparameter tuning job that were
                    manually stopped.

                - **ObjectiveStatusCounters** *(dict) --*

                  The  ObjectiveStatusCounters object that specifies the numbers of training jobs,
                  categorized by objective metric status, that this tuning job launched.

                  - **Succeeded** *(integer) --*

                    The number of training jobs whose final objective metric was evaluated by the
                    hyperparameter tuning job and used in the hyperparameter tuning process.

                  - **Pending** *(integer) --*

                    The number of training jobs that are in progress and pending evaluation of their
                    final objective metric.

                  - **Failed** *(integer) --*

                    The number of training jobs whose final objective metric was not evaluated and
                    used in the hyperparameter tuning process. This typically occurs when the
                    training job failed or did not emit an objective metric.

                - **ResourceLimits** *(dict) --*

                  The  ResourceLimits object that specifies the maximum number of training jobs and
                  parallel training jobs allowed for this tuning job.

                  - **MaxNumberOfTrainingJobs** *(integer) --*

                    The maximum number of training jobs that a hyperparameter tuning job can launch.

                  - **MaxParallelTrainingJobs** *(integer) --*

                    The maximum number of concurrent training jobs that a hyperparameter tuning job
                    can launch.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_labeling_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListLabelingJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only labeling jobs created after the specified time (timestamp).

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only labeling jobs created before the specified time (timestamp).

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only labeling jobs modified after the specified time (timestamp).

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only labeling jobs modified before the specified time (timestamp).

        :type NameContains: string
        :param NameContains:

          A string in the labeling job name. This filter returns only labeling jobs whose name
          contains the specified string.

        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type StatusEquals: string
        :param StatusEquals:

          A filter that retrieves only labeling jobs with a specific status.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LabelingJobSummaryList': [
                    {
                        'LabelingJobName': 'string',
                        'LabelingJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'LabelingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                        'LabelCounters': {
                            'TotalLabeled': 123,
                            'HumanLabeled': 123,
                            'MachineLabeled': 123,
                            'FailedNonRetryableError': 123,
                            'Unlabeled': 123
                        },
                        'WorkteamArn': 'string',
                        'PreHumanTaskLambdaArn': 'string',
                        'AnnotationConsolidationLambdaArn': 'string',
                        'FailureReason': 'string',
                        'LabelingJobOutput': {
                            'OutputDatasetS3Uri': 'string',
                            'FinalActiveLearningModelArn': 'string'
                        },
                        'InputConfig': {
                            'DataSource': {
                                'S3DataSource': {
                                    'ManifestS3Uri': 'string'
                                }
                            },
                            'DataAttributes': {
                                'ContentClassifiers': [
                                    'FreeOfPersonallyIdentifiableInformation'|'FreeOfAdultContent',
                                ]
                            }
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **LabelingJobSummaryList** *(list) --*

              An array of ``LabelingJobSummary`` objects, each describing a labeling job.

              - *(dict) --*

                Provides summary information about a labeling job.

                - **LabelingJobName** *(string) --*

                  The name of the labeling job.

                - **LabelingJobArn** *(string) --*

                  The Amazon Resource Name (ARN) assigned to the labeling job when it was created.

                - **CreationTime** *(datetime) --*

                  The date and time that the job was created (timestamp).

                - **LastModifiedTime** *(datetime) --*

                  The date and time that the job was last modified (timestamp).

                - **LabelingJobStatus** *(string) --*

                  The current status of the labeling job.

                - **LabelCounters** *(dict) --*

                  Counts showing the progress of the labeling job.

                  - **TotalLabeled** *(integer) --*

                    The total number of objects labeled.

                  - **HumanLabeled** *(integer) --*

                    The total number of objects labeled by a human worker.

                  - **MachineLabeled** *(integer) --*

                    The total number of objects labeled by automated data labeling.

                  - **FailedNonRetryableError** *(integer) --*

                    The total number of objects that could not be labeled due to an error.

                  - **Unlabeled** *(integer) --*

                    The total number of objects not yet labeled.

                - **WorkteamArn** *(string) --*

                  The Amazon Resource Name (ARN) of the work team assigned to the job.

                - **PreHumanTaskLambdaArn** *(string) --*

                  The Amazon Resource Name (ARN) of a Lambda function. The function is run before
                  each data object is sent to a worker.

                - **AnnotationConsolidationLambdaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the Lambda function used to consolidate the
                  annotations from individual workers into a label for a data object. For more
                  information, see `Annotation Consolidation
                  <https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html>`__
                  .

                - **FailureReason** *(string) --*

                  If the ``LabelingJobStatus`` field is ``Failed`` , this field contains a
                  description of the error.

                - **LabelingJobOutput** *(dict) --*

                  The location of the output produced by the labeling job.

                  - **OutputDatasetS3Uri** *(string) --*

                    The Amazon S3 bucket location of the manifest file for labeled data.

                  - **FinalActiveLearningModelArn** *(string) --*

                    The Amazon Resource Name (ARN) for the most recent Amazon SageMaker model
                    trained as part of automated data labeling.

                - **InputConfig** *(dict) --*

                  Input configuration for the labeling job.

                  - **DataSource** *(dict) --*

                    The location of the input data.

                    - **S3DataSource** *(dict) --*

                      The Amazon S3 location of the input data objects.

                      - **ManifestS3Uri** *(string) --*

                        The Amazon S3 location of the manifest file that describes the input data
                        objects.

                  - **DataAttributes** *(dict) --*

                    Attributes of the data specified by the customer.

                    - **ContentClassifiers** *(list) --*

                      Declares that your content is free of personally identifiable information or
                      adult content. Amazon SageMaker may restrict the Amazon Mechanical Turk
                      workers that can view your task based on this information.

                      - *(string) --*
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_labeling_jobs_for_workteam`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListLabelingJobsForWorkteam>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              WorkteamArn='string',
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              JobReferenceCodeContains='string',
              SortBy='CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type WorkteamArn: string
        :param WorkteamArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the work team for which you want to see labeling jobs
          for.

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only labeling jobs created after the specified time (timestamp).

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only labeling jobs created before the specified time (timestamp).

        :type JobReferenceCodeContains: string
        :param JobReferenceCodeContains:

          A filter the limits jobs to only the ones whose job reference code contains the specified
          string.

        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LabelingJobSummaryList': [
                    {
                        'LabelingJobName': 'string',
                        'JobReferenceCode': 'string',
                        'WorkRequesterAccountId': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LabelCounters': {
                            'HumanLabeled': 123,
                            'PendingHuman': 123,
                            'Total': 123
                        },
                        'NumberOfHumanWorkersPerDataObject': 123
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **LabelingJobSummaryList** *(list) --*

              An array of ``LabelingJobSummary`` objects, each describing a labeling job.

              - *(dict) --*

                Provides summary information for a work team.

                - **LabelingJobName** *(string) --*

                  The name of the labeling job that the work team is assigned to.

                - **JobReferenceCode** *(string) --*

                  A unique identifier for a labeling job. You can use this to refer to a specific
                  labeling job.

                - **WorkRequesterAccountId** *(string) --*

                - **CreationTime** *(datetime) --*

                  The date and time that the labeling job was created.

                - **LabelCounters** *(dict) --*

                  Provides information about the progress of a labeling job.

                  - **HumanLabeled** *(integer) --*

                    The total number of data objects labeled by a human worker.

                  - **PendingHuman** *(integer) --*

                    The total number of data objects that need to be labeled by a human worker.

                  - **Total** *(integer) --*

                    The total number of tasks in the labeling job.

                - **NumberOfHumanWorkersPerDataObject** *(integer) --*

                  The configured number of workers per data object.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_model_packages`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModelPackages>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only model packages created after the specified time (timestamp).

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only model packages created before the specified time (timestamp).

        :type NameContains: string
        :param NameContains:

          A string in the model package name. This filter returns only model packages whose name
          contains the specified string.

        :type SortBy: string
        :param SortBy:

          The parameter by which to sort the results. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for the results. The default is ``Ascending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ModelPackageSummaryList': [
                    {
                        'ModelPackageName': 'string',
                        'ModelPackageArn': 'string',
                        'ModelPackageDescription': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'ModelPackageStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ModelPackageSummaryList** *(list) --*

              An array of ``ModelPackageSummary`` objects, each of which lists a model package.

              - *(dict) --*

                Provides summary information about a model package.

                - **ModelPackageName** *(string) --*

                  The name of the model package.

                - **ModelPackageArn** *(string) --*

                  The Amazon Resource Name (ARN) of the model package.

                - **ModelPackageDescription** *(string) --*

                  A brief description of the model package.

                - **CreationTime** *(datetime) --*

                  A timestamp that shows when the model package was created.

                - **ModelPackageStatus** *(string) --*

                  The overall status of the model package.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_models`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModels>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortBy: string
        :param SortBy:

          Sorts the list of results. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Descending`` .

        :type NameContains: string
        :param NameContains:

          A string in the training job name. This filter returns only models in the training job
          whose name contains the specified string.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only models created before the specified time (timestamp).

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only models with a creation time greater than or equal to the
          specified time (timestamp).

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Models': [
                    {
                        'ModelName': 'string',
                        'ModelArn': 'string',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Models** *(list) --*

              An array of ``ModelSummary`` objects, each of which lists a model.

              - *(dict) --*

                Provides summary information about a model.

                - **ModelName** *(string) --*

                  The name of the model that you want a summary for.

                - **ModelArn** *(string) --*

                  The Amazon Resource Name (ARN) of the model.

                - **CreationTime** *(datetime) --*

                  A timestamp that indicates when the model was created.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_monitoring_executions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListMonitoringExecutions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              MonitoringScheduleName='string',
              EndpointName='string',
              SortBy='CreationTime'|'ScheduledTime'|'Status',
              SortOrder='Ascending'|'Descending',
              ScheduledTimeBefore=datetime(2015, 1, 1),
              ScheduledTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals=
                  'Pending'|'Completed'|'CompletedWithViolations'|'InProgress'|'Failed'|'Stopping'
                  |'Stopped',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type MonitoringScheduleName: string
        :param MonitoringScheduleName:

          Name of a specific schedule to fetch jobs for.

        :type EndpointName: string
        :param EndpointName:

          Name of a specific endpoint to fetch jobs for.

        :type SortBy: string
        :param SortBy:

          Whether to sort results by ``Status`` , ``CreationTime`` , ``ScheduledTime`` field. The
          default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          Whether to sort the results in ``Ascending`` or ``Descending`` order. The default is
          ``Descending`` .

        :type ScheduledTimeBefore: datetime
        :param ScheduledTimeBefore:

          Filter for jobs scheduled before a specified time.

        :type ScheduledTimeAfter: datetime
        :param ScheduledTimeAfter:

          Filter for jobs scheduled after a specified time.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only jobs created before a specified time.

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only jobs created after a specified time.

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only jobs modified after a specified time.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only jobs modified before a specified time.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that retrieves only jobs with a specific status.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MonitoringExecutionSummaries': [
                    {
                        'MonitoringScheduleName': 'string',
                        'ScheduledTime': datetime(2015, 1, 1),
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'MonitoringExecutionStatus':
                        'Pending'|'Completed'|'CompletedWithViolations'|'InProgress'
                        |'Failed'|'Stopping'|'Stopped',
                        'ProcessingJobArn': 'string',
                        'EndpointName': 'string',
                        'FailureReason': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **MonitoringExecutionSummaries** *(list) --*

              A JSON array in which each element is a summary for a monitoring execution.

              - *(dict) --*

                Summary of information about the last monitoring job to run.

                - **MonitoringScheduleName** *(string) --*

                  The name of the monitoring schedule.

                - **ScheduledTime** *(datetime) --*

                  The time the monitoring job was scheduled.

                - **CreationTime** *(datetime) --*

                  The time at which the monitoring job was created.

                - **LastModifiedTime** *(datetime) --*

                  A timestamp that indicates the last time the monitoring job was modified.

                - **MonitoringExecutionStatus** *(string) --*

                  The status of the monitoring job.

                - **ProcessingJobArn** *(string) --*

                  The Amazon Resource Name (ARN) of the monitoring job.

                - **EndpointName** *(string) --*

                  The name of teh endpoint used to run the monitoring job.

                - **FailureReason** *(string) --*

                  Contains the reason a monitoring job failed, if it failed.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_monitoring_schedules`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListMonitoringSchedules>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              EndpointName='string',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals='Pending'|'Failed'|'Scheduled'|'Stopped',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type EndpointName: string
        :param EndpointName:

          Name of a specific endpoint to fetch schedules for.

        :type SortBy: string
        :param SortBy:

          Whether to sort results by ``Status`` , ``CreationTime`` , ``ScheduledTime`` field. The
          default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          Whether to sort the results in ``Ascending`` or ``Descending`` order. The default is
          ``Descending`` .

        :type NameContains: string
        :param NameContains:

          Filter for monitoring schedules whose name contains a specified string.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only monitoring schedules created before a specified time.

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only monitoring schedules created after a specified time.

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only monitoring schedules modified before a specified time.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only monitoring schedules modified after a specified time.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that returns only monitoring schedules modified before a specified time.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MonitoringScheduleSummaries': [
                    {
                        'MonitoringScheduleName': 'string',
                        'MonitoringScheduleArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'MonitoringScheduleStatus': 'Pending'|'Failed'|'Scheduled'|'Stopped',
                        'EndpointName': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **MonitoringScheduleSummaries** *(list) --*

              A JSON array in which each element is a summary for a monitoring schedule.

              - *(dict) --*

                Summarizes the monitoring schedule.

                - **MonitoringScheduleName** *(string) --*

                  The name of the monitoring schedule.

                - **MonitoringScheduleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the monitoring schedule.

                - **CreationTime** *(datetime) --*

                  The creation time of the monitoring schedule.

                - **LastModifiedTime** *(datetime) --*

                  The last time the monitoring schedule was modified.

                - **MonitoringScheduleStatus** *(string) --*

                  The status of the monitoring schedule.

                - **EndpointName** *(string) --*

                  The name of the endpoint using the monitoring schedule.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_notebook_instance_lifecycle_configs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime'|'LastModifiedTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortBy: string
        :param SortBy:

          Sorts the list of results. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results.

        :type NameContains: string
        :param NameContains:

          A string in the lifecycle configuration name. This filter returns only lifecycle
          configurations whose name contains the specified string.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only lifecycle configurations that were created before the specified
          time (timestamp).

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only lifecycle configurations that were created after the specified
          time (timestamp).

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only lifecycle configurations that were modified before the
          specified time (timestamp).

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only lifecycle configurations that were modified after the specified
          time (timestamp).

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NotebookInstanceLifecycleConfigs': [
                    {
                        'NotebookInstanceLifecycleConfigName': 'string',
                        'NotebookInstanceLifecycleConfigArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NotebookInstanceLifecycleConfigs** *(list) --*

              An array of ``NotebookInstanceLifecycleConfiguration`` objects, each listing a
              lifecycle configuration.

              - *(dict) --*

                Provides a summary of a notebook instance lifecycle configuration.

                - **NotebookInstanceLifecycleConfigName** *(string) --*

                  The name of the lifecycle configuration.

                - **NotebookInstanceLifecycleConfigArn** *(string) --*

                  The Amazon Resource Name (ARN) of the lifecycle configuration.

                - **CreationTime** *(datetime) --*

                  A timestamp that tells when the lifecycle configuration was created.

                - **LastModifiedTime** *(datetime) --*

                  A timestamp that tells when the lifecycle configuration was last modified.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_notebook_instances`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstances>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals=
                  'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting'|'Updating',
              NotebookInstanceLifecycleConfigNameContains='string',
              DefaultCodeRepositoryContains='string',
              AdditionalCodeRepositoryEquals='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``Name`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results.

        :type NameContains: string
        :param NameContains:

          A string in the notebook instances' name. This filter returns only notebook instances
          whose name contains the specified string.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only notebook instances that were created before the specified time
          (timestamp).

        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only notebook instances that were created after the specified time
          (timestamp).

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only notebook instances that were modified before the specified time
          (timestamp).

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only notebook instances that were modified after the specified time
          (timestamp).

        :type StatusEquals: string
        :param StatusEquals:

          A filter that returns only notebook instances with the specified status.

        :type NotebookInstanceLifecycleConfigNameContains: string
        :param NotebookInstanceLifecycleConfigNameContains:

          A string in the name of a notebook instances lifecycle configuration associated with this
          notebook instance. This filter returns only notebook instances associated with a lifecycle
          configuration with a name that contains the specified string.

        :type DefaultCodeRepositoryContains: string
        :param DefaultCodeRepositoryContains:

          A string in the name or URL of a Git repository associated with this notebook instance.
          This filter returns only notebook instances associated with a git repository with a name
          that contains the specified string.

        :type AdditionalCodeRepositoryEquals: string
        :param AdditionalCodeRepositoryEquals:

          A filter that returns only notebook instances with associated with the specified git
          repository.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NotebookInstances': [
                    {
                        'NotebookInstanceName': 'string',
                        'NotebookInstanceArn': 'string',
                        'NotebookInstanceStatus':
                        'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'
                        |'Deleting'|'Updating',
                        'Url': 'string',
                        'InstanceType':
                        'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'
                        |'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'
                        |'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'
                        |'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'
                        |'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'
                        |'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'
                        |'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'
                        |'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'
                        |'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'
                        |'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'
                        |'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'
                        |'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'NotebookInstanceLifecycleConfigName': 'string',
                        'DefaultCodeRepository': 'string',
                        'AdditionalCodeRepositories': [
                            'string',
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NotebookInstances** *(list) --*

              An array of ``NotebookInstanceSummary`` objects, one for each notebook instance.

              - *(dict) --*

                Provides summary information for an Amazon SageMaker notebook instance.

                - **NotebookInstanceName** *(string) --*

                  The name of the notebook instance that you want a summary for.

                - **NotebookInstanceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the notebook instance.

                - **NotebookInstanceStatus** *(string) --*

                  The status of the notebook instance.

                - **Url** *(string) --*

                  The URL that you use to connect to the Jupyter instance running in your notebook
                  instance.

                - **InstanceType** *(string) --*

                  The type of ML compute instance that the notebook instance is running on.

                - **CreationTime** *(datetime) --*

                  A timestamp that shows when the notebook instance was created.

                - **LastModifiedTime** *(datetime) --*

                  A timestamp that shows when the notebook instance was last modified.

                - **NotebookInstanceLifecycleConfigName** *(string) --*

                  The name of a notebook instance lifecycle configuration associated with this
                  notebook instance.

                  For information about notebook instance lifestyle configurations, see `Step 2.1\\:
                  (Optional) Customize a Notebook Instance
                  <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__
                  .

                - **DefaultCodeRepository** *(string) --*

                  The Git repository associated with the notebook instance as its default code
                  repository. This can be either the name of a Git repository stored as a resource
                  in your account, or the URL of a Git repository in `AWS CodeCommit
                  <https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in
                  any other Git repository. When you open a notebook instance, it opens in the
                  directory that contains this repository. For more information, see `Associating
                  Git Repositories with Amazon SageMaker Notebook Instances
                  <https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .

                - **AdditionalCodeRepositories** *(list) --*

                  An array of up to three Git repositories associated with the notebook instance.
                  These can be either the names of Git repositories stored as resources in your
                  account, or the URL of Git repositories in `AWS CodeCommit
                  <https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in
                  any other Git repository. These repositories are cloned at the same level as the
                  default repository of your notebook instance. For more information, see
                  `Associating Git Repositories with Amazon SageMaker Notebook Instances
                  <https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .

                  - *(string) --*
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_processing_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListProcessingJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only processing jobs created after the specified time.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only processing jobs created after the specified time.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only processing jobs modified after the specified time.

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only processing jobs modified before the specified time.

        :type NameContains: string
        :param NameContains:

          A string in the processing job name. This filter returns only processing jobs whose name
          contains the specified string.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that retrieves only processing jobs with a specific status.

        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProcessingJobSummaries': [
                    {
                        'ProcessingJobName': 'string',
                        'ProcessingJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'ProcessingEndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'ProcessingJobStatus':
                        'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                        'FailureReason': 'string',
                        'ExitMessage': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ProcessingJobSummaries** *(list) --*

              An array of ``ProcessingJobSummary`` objects, each listing a processing job.

              - *(dict) --*

                Summary of information about a processing job.

                - **ProcessingJobName** *(string) --*

                  The name of the processing job.

                - **ProcessingJobArn** *(string) --*

                  The Amazon Resource Name (ARN) of the processing job..

                - **CreationTime** *(datetime) --*

                  The time at which the processing job was created.

                - **ProcessingEndTime** *(datetime) --*

                  The time at which the processing job completed.

                - **LastModifiedTime** *(datetime) --*

                  A timestamp that indicates the last time the processing job was modified.

                - **ProcessingJobStatus** *(string) --*

                  The status of the processing job.

                - **FailureReason** *(string) --*

                  A string, up to one KB in size, that contains the reason a processing job failed,
                  if it failed.

                - **ExitMessage** *(string) --*

                  An optional string, up to one KB in size, that contains metadata from the
                  processing container when the processing job exits.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_subscribed_workteams`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListSubscribedWorkteams>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              NameContains='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type NameContains: string
        :param NameContains:

          A string in the work team name. This filter returns only work teams whose name contains
          the specified string.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SubscribedWorkteams': [
                    {
                        'WorkteamArn': 'string',
                        'MarketplaceTitle': 'string',
                        'SellerName': 'string',
                        'MarketplaceDescription': 'string',
                        'ListingId': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **SubscribedWorkteams** *(list) --*

              An array of ``Workteam`` objects, each describing a work team.

              - *(dict) --*

                Describes a work team of a vendor that does the a labelling job.

                - **WorkteamArn** *(string) --*

                  The Amazon Resource Name (ARN) of the vendor that you have subscribed.

                - **MarketplaceTitle** *(string) --*

                  The title of the service provided by the vendor in the Amazon Marketplace.

                - **SellerName** *(string) --*

                  The name of the vendor in the Amazon Marketplace.

                - **MarketplaceDescription** *(string) --*

                  The description of the vendor from the Amazon Marketplace.

                - **ListingId** *(string) --*
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_tags`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTags>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ResourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              An array of ``Tag`` objects, each with a tag key and a value.

              - *(dict) --*

                Describes a tag.

                - **Key** *(string) --*

                  The tag key.

                - **Value** *(string) --*

                  The tag value.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_training_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only training jobs created after the specified time (timestamp).

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only training jobs created before the specified time (timestamp).

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only training jobs modified after the specified time (timestamp).

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only training jobs modified before the specified time (timestamp).

        :type NameContains: string
        :param NameContains:

          A string in the training job name. This filter returns only training jobs whose name
          contains the specified string.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that retrieves only training jobs with a specific status.

        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TrainingJobSummaries': [
                    {
                        'TrainingJobName': 'string',
                        'TrainingJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TrainingEndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **TrainingJobSummaries** *(list) --*

              An array of ``TrainingJobSummary`` objects, each listing a training job.

              - *(dict) --*

                Provides summary information about a training job.

                - **TrainingJobName** *(string) --*

                  The name of the training job that you want a summary for.

                - **TrainingJobArn** *(string) --*

                  The Amazon Resource Name (ARN) of the training job.

                - **CreationTime** *(datetime) --*

                  A timestamp that shows when the training job was created.

                - **TrainingEndTime** *(datetime) --*

                  A timestamp that shows when the training job ended. This field is set only if the
                  training job has one of the terminal statuses (``Completed`` , ``Failed`` , or
                  ``Stopped`` ).

                - **LastModifiedTime** *(datetime) --*

                  Timestamp when the training job was last modified.

                - **TrainingJobStatus** *(string) --*

                  The status of the training job.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobsForHyperParameterTuningJob>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              HyperParameterTuningJobName='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status'|'FinalObjectiveMetricValue',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]**

          The name of the tuning job whose training jobs you want to list.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that returns only training jobs with the specified status.

        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``Name`` .

          If the value of this field is ``FinalObjectiveMetricValue`` , any training jobs that did
          not return an objective metric are not listed.

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TrainingJobSummaries': [
                    {
                        'TrainingJobDefinitionName': 'string',
                        'TrainingJobName': 'string',
                        'TrainingJobArn': 'string',
                        'TuningJobName': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TrainingStartTime': datetime(2015, 1, 1),
                        'TrainingEndTime': datetime(2015, 1, 1),
                        'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                        'TunedHyperParameters': {
                            'string': 'string'
                        },
                        'FailureReason': 'string',
                        'FinalHyperParameterTuningJobObjectiveMetric': {
                            'Type': 'Maximize'|'Minimize',
                            'MetricName': 'string',
                            'Value': ...
                        },
                        'ObjectiveStatus': 'Succeeded'|'Pending'|'Failed'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **TrainingJobSummaries** *(list) --*

              A list of  TrainingJobSummary objects that describe the training jobs that the
              ``ListTrainingJobsForHyperParameterTuningJob`` request returned.

              - *(dict) --*

                Specifies summary information about a training job.

                - **TrainingJobDefinitionName** *(string) --*

                  The training job definition name.

                - **TrainingJobName** *(string) --*

                  The name of the training job.

                - **TrainingJobArn** *(string) --*

                  The Amazon Resource Name (ARN) of the training job.

                - **TuningJobName** *(string) --*

                  The HyperParameter tuning job that launched the training job.

                - **CreationTime** *(datetime) --*

                  The date and time that the training job was created.

                - **TrainingStartTime** *(datetime) --*

                  The date and time that the training job started.

                - **TrainingEndTime** *(datetime) --*

                  Specifies the time when the training job ends on training instances. You are
                  billed for the time interval between the value of ``TrainingStartTime`` and this
                  time. For successful jobs and stopped jobs, this is the time after model artifacts
                  are uploaded. For failed jobs, this is the time when Amazon SageMaker detects a
                  job failure.

                - **TrainingJobStatus** *(string) --*

                  The status of the training job.

                - **TunedHyperParameters** *(dict) --*

                  A list of the hyperparameters for which you specified ranges to search.

                  - *(string) --*

                    - *(string) --*

                - **FailureReason** *(string) --*

                  The reason that the training job failed.

                - **FinalHyperParameterTuningJobObjectiveMetric** *(dict) --*

                  The  FinalHyperParameterTuningJobObjectiveMetric object that specifies the value
                  of the objective metric of the tuning job that launched this training job.

                  - **Type** *(string) --*

                    Whether to minimize or maximize the objective metric. Valid values are Minimize
                    and Maximize.

                  - **MetricName** *(string) --*

                    The name of the objective metric.

                  - **Value** *(float) --*

                    The value of the objective metric.

                - **ObjectiveStatus** *(string) --*

                  The status of the objective metric for the training job:

                  * Succeeded: The final objective metric for the training job was evaluated by the
                  hyperparameter tuning job and used in the hyperparameter tuning process.

                  * Pending: The training job is in progress and evaluation of its final objective
                  metric is pending.

                  * Failed: The final objective metric for the training job was not evaluated, and
                  was not used in the hyperparameter tuning process. This typically occurs when the
                  training job failed or did not emit an objective metric.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_transform_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTransformJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:

          A filter that returns only transform jobs created after the specified time.

        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:

          A filter that returns only transform jobs created before the specified time.

        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:

          A filter that returns only transform jobs modified after the specified time.

        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:

          A filter that returns only transform jobs modified before the specified time.

        :type NameContains: string
        :param NameContains:

          A string in the transform job name. This filter returns only transform jobs whose name
          contains the specified string.

        :type StatusEquals: string
        :param StatusEquals:

          A filter that retrieves only transform jobs with a specific status.

        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Descending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TransformJobSummaries': [
                    {
                        'TransformJobName': 'string',
                        'TransformJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TransformEndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'TransformJobStatus':
                        'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                        'FailureReason': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **TransformJobSummaries** *(list) --*

              An array of ``TransformJobSummary`` objects.

              - *(dict) --*

                Provides a summary of a transform job. Multiple ``TransformJobSummary`` objects are
                returned as a list after in response to a  ListTransformJobs call.

                - **TransformJobName** *(string) --*

                  The name of the transform job.

                - **TransformJobArn** *(string) --*

                  The Amazon Resource Name (ARN) of the transform job.

                - **CreationTime** *(datetime) --*

                  A timestamp that shows when the transform Job was created.

                - **TransformEndTime** *(datetime) --*

                  Indicates when the transform job ends on compute instances. For successful jobs
                  and stopped jobs, this is the exact time recorded after the results are uploaded.
                  For failed jobs, this is when Amazon SageMaker detected that the job failed.

                - **LastModifiedTime** *(datetime) --*

                  Indicates when the transform job was last modified.

                - **TransformJobStatus** *(string) --*

                  The status of the transform job.

                - **FailureReason** *(string) --*

                  If the transform job failed, the reason it failed.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_trial_components`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrialComponents>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SourceArn='string',
              CreatedAfter=datetime(2015, 1, 1),
              CreatedBefore=datetime(2015, 1, 1),
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SourceArn: string
        :param SourceArn:

          A filter that returns only components that have the specified source Amazon Resource Name
          (ARN).

        :type CreatedAfter: datetime
        :param CreatedAfter:

          A filter that returns only components created after the specified time.

        :type CreatedBefore: datetime
        :param CreatedBefore:

          A filter that returns only components created before the specified time.

        :type SortBy: string
        :param SortBy:

          The property used to sort results. The default value is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order. The default value is ``Descending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TrialComponentSummaries': [
                    {
                        'TrialComponentName': 'string',
                        'TrialComponentArn': 'string',
                        'DisplayName': 'string',
                        'TrialComponentSource': {
                            'SourceArn': 'string',
                            'SourceType': 'string'
                        },
                        'Status': {
                            'PrimaryStatus': 'InProgress'|'Completed'|'Failed',
                            'Message': 'string'
                        },
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'CreationTime': datetime(2015, 1, 1),
                        'CreatedBy': {
                            'UserProfileArn': 'string',
                            'UserProfileName': 'string',
                            'DomainId': 'string'
                        },
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'LastModifiedBy': {
                            'UserProfileArn': 'string',
                            'UserProfileName': 'string',
                            'DomainId': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **TrialComponentSummaries** *(list) --*

              A list of the summaries of your trial components.

              - *(dict) --*

                A summary of the properties of a trial component. To get all the properties, call
                the  DescribeTrialComponent API and provide the ``TrialComponentName`` .

                - **TrialComponentName** *(string) --*

                  The name of the trial component.

                - **TrialComponentArn** *(string) --*

                  The ARN of the trial component.

                - **DisplayName** *(string) --*

                  The name of the component as displayed. If ``DisplayName`` isn't specified,
                  ``TrialComponentName`` is displayed.

                - **TrialComponentSource** *(dict) --*

                  The source of the trial component.

                  - **SourceArn** *(string) --*

                    The Amazon Resource Name (ARN) of the source.

                  - **SourceType** *(string) --*

                    The source job type.

                - **Status** *(dict) --*

                  The status of the component. States include:

                  * InProgress

                  * Completed

                  * Failed

                  - **PrimaryStatus** *(string) --*

                    The status of the trial component.

                  - **Message** *(string) --*

                    If the component failed, a message describing why.

                - **StartTime** *(datetime) --*

                  When the component started.

                - **EndTime** *(datetime) --*

                  When the component ended.

                - **CreationTime** *(datetime) --*

                  When the component was created.

                - **CreatedBy** *(dict) --*

                  Who created the component.

                  - **UserProfileArn** *(string) --*

                    The Amazon Resource Name (ARN) of the user's profile.

                  - **UserProfileName** *(string) --*

                    The name of the user's profile.

                  - **DomainId** *(string) --*

                    The domain associated with the user.

                - **LastModifiedTime** *(datetime) --*

                  When the component was last modified.

                - **LastModifiedBy** *(dict) --*

                  Who last modified the component.

                  - **UserProfileArn** *(string) --*

                    The Amazon Resource Name (ARN) of the user's profile.

                  - **UserProfileName** *(string) --*

                    The name of the user's profile.

                  - **DomainId** *(string) --*

                    The domain associated with the user.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_trials`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrials>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ExperimentName='string',
              CreatedAfter=datetime(2015, 1, 1),
              CreatedBefore=datetime(2015, 1, 1),
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ExperimentName: string
        :param ExperimentName:

          A filter that returns only trials that are part of the specified experiment.

        :type CreatedAfter: datetime
        :param CreatedAfter:

          A filter that returns only trials created after the specified time.

        :type CreatedBefore: datetime
        :param CreatedBefore:

          A filter that returns only trials created before the specified time.

        :type SortBy: string
        :param SortBy:

          The property used to sort results. The default value is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order. The default value is ``Descending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TrialSummaries': [
                    {
                        'TrialArn': 'string',
                        'TrialName': 'string',
                        'DisplayName': 'string',
                        'TrialSource': {
                            'SourceArn': 'string',
                            'SourceType': 'string'
                        },
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **TrialSummaries** *(list) --*

              A list of the summaries of your trials.

              - *(dict) --*

                A summary of the properties of a trial. To get the complete set of properties, call
                the  DescribeTrial API and provide the ``TrialName`` .

                - **TrialArn** *(string) --*

                  The Amazon Resource Name (ARN) of the trial.

                - **TrialName** *(string) --*

                  The name of the trial.

                - **DisplayName** *(string) --*

                  The name of the trial as displayed. If ``DisplayName`` isn't specified,
                  ``TrialName`` is displayed.

                - **TrialSource** *(dict) --*

                  The source of the trial.

                  - **SourceArn** *(string) --*

                    The Amazon Resource Name (ARN) of the source.

                  - **SourceType** *(string) --*

                    The source job type.

                - **CreationTime** *(datetime) --*

                  When the trial was created.

                - **LastModifiedTime** *(datetime) --*

                  When the trial was last modified.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_user_profiles`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListUserProfiles>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortOrder='Ascending'|'Descending',
              SortBy='CreationTime'|'LastModifiedTime',
              DomainIdEquals='string',
              UserProfileNameContains='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortOrder: string
        :param SortOrder:

          The sort order for the results. The default is Ascending.

        :type SortBy: string
        :param SortBy:

          The parameter by which to sort the results. The default is CreationTime.

        :type DomainIdEquals: string
        :param DomainIdEquals:

          A parameter by which to filter the results.

        :type UserProfileNameContains: string
        :param UserProfileNameContains:

          A parameter by which to filter the results.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserProfiles': [
                    {
                        'DomainId': 'string',
                        'UserProfileName': 'string',
                        'Status': 'Deleting'|'Failed'|'InService'|'Pending',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **UserProfiles** *(list) --*

              The list of user profiles.

              - *(dict) --*

                The user profile details.

                - **DomainId** *(string) --*

                  The domain ID.

                - **UserProfileName** *(string) --*

                  The user profile name.

                - **Status** *(string) --*

                  The status.

                - **CreationTime** *(datetime) --*

                  The creation time.

                - **LastModifiedTime** *(datetime) --*

                  The last modified time.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.list_workteams`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListWorkteams>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SortBy='Name'|'CreateDate',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SortBy: string
        :param SortBy:

          The field to sort results by. The default is ``CreationTime`` .

        :type SortOrder: string
        :param SortOrder:

          The sort order for results. The default is ``Ascending`` .

        :type NameContains: string
        :param NameContains:

          A string in the work team's name. This filter returns only work teams whose name contains
          the specified string.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Workteams': [
                    {
                        'WorkteamName': 'string',
                        'MemberDefinitions': [
                            {
                                'CognitoMemberDefinition': {
                                    'UserPool': 'string',
                                    'UserGroup': 'string',
                                    'ClientId': 'string'
                                }
                            },
                        ],
                        'WorkteamArn': 'string',
                        'ProductListingIds': [
                            'string',
                        ],
                        'Description': 'string',
                        'SubDomain': 'string',
                        'CreateDate': datetime(2015, 1, 1),
                        'LastUpdatedDate': datetime(2015, 1, 1),
                        'NotificationConfiguration': {
                            'NotificationTopicArn': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Workteams** *(list) --*

              An array of ``Workteam`` objects, each describing a work team.

              - *(dict) --*

                Provides details about a labeling work team.

                - **WorkteamName** *(string) --*

                  The name of the work team.

                - **MemberDefinitions** *(list) --*

                  The Amazon Cognito user groups that make up the work team.

                  - *(dict) --*

                    Defines the Amazon Cognito user group that is part of a work team.

                    - **CognitoMemberDefinition** *(dict) --*

                      The Amazon Cognito user group that is part of the work team.

                      - **UserPool** *(string) --*

                        An identifier for a user pool. The user pool must be in the same region as
                        the service that you are calling.

                      - **UserGroup** *(string) --*

                        An identifier for a user group.

                      - **ClientId** *(string) --*

                        An identifier for an application client. You must create the app client ID
                        using Amazon Cognito.

                - **WorkteamArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the work team.

                - **ProductListingIds** *(list) --*

                  The Amazon Marketplace identifier for a vendor's work team.

                  - *(string) --*

                - **Description** *(string) --*

                  A description of the work team.

                - **SubDomain** *(string) --*

                  The URI of the labeling job's user interface. Workers open this URI to start
                  labeling your data objects.

                - **CreateDate** *(datetime) --*

                  The date and time that the work team was created (timestamp).

                - **LastUpdatedDate** *(datetime) --*

                  The date and time that the work team was last updated (timestamp).

                - **NotificationConfiguration** *(dict) --*

                  Configures SNS notifications of available or expiring work items for work teams.

                  - **NotificationTopicArn** *(string) --*

                    The ARN for the SNS topic to which notifications should be published.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`SageMaker.Client.search`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/Search>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Resource='TrainingJob'|'Experiment'|'ExperimentTrial'|'ExperimentTrialComponent',
              SearchExpression={
                  'Filters': [
                      {
                          'Name': 'string',
                          'Operator':
                          'Equals'|'NotEquals'|'GreaterThan'
                          |'GreaterThanOrEqualTo'|'LessThan'|'LessThanOrEqualTo'
                          |'Contains'|'Exists'|'NotExists',
                          'Value': 'string'
                      },
                  ],
                  'NestedFilters': [
                      {
                          'NestedPropertyName': 'string',
                          'Filters': [
                              {
                                  'Name': 'string',
                                  'Operator':
                                  'Equals'|'NotEquals'|'GreaterThan'
                                  |'GreaterThanOrEqualTo'|'LessThan'
                                  |'LessThanOrEqualTo'|'Contains'|'Exists'
                                  |'NotExists',
                                  'Value': 'string'
                              },
                          ]
                      },
                  ],
                  'SubExpressions': [
                      {'... recursive ...'},
                  ],
                  'Operator': 'And'|'Or'
              },
              SortBy='string',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Resource: string
        :param Resource: **[REQUIRED]**

          The name of the Amazon SageMaker resource to search for. Currently, the only valid
          ``Resource`` value is ``TrainingJob`` .

        :type SearchExpression: dict
        :param SearchExpression:

          A Boolean conditional statement. Resource objects must satisfy this condition to be
          included in search results. You must provide at least one subexpression, filter, or nested
          filter. The maximum number of recursive ``SubExpressions`` , ``NestedFilters`` , and
          ``Filters`` that can be included in a ``SearchExpression`` object is 50.

          - **Filters** *(list) --*

            A list of filter objects.

            - *(dict) --*

              A conditional statement for a search expression that includes a resource property, a
              Boolean operator, and a value.

              If you don't specify an ``Operator`` and a ``Value`` , the filter searches for only
              the specified property. For example, defining a ``Filter`` for the ``FailureReason``
              for the ``TrainingJob``  ``Resource`` searches for training job objects that have a
              value in the ``FailureReason`` field.

              If you specify a ``Value`` , but not an ``Operator`` , Amazon SageMaker uses the
              equals operator as the default.

              In search, there are several property types:

                Metrics

              To define a metric filter, enter a value using the form ``"Metrics.<name>"`` , where
              ``<name>`` is a metric name. For example, the following filter searches for training
              jobs with an ``"accuracy"`` metric greater than ``"0.9"`` :

               ``{``

               ``"Name": "Metrics.accuracy",``

               ``"Operator": "GREATER_THAN",``

               ``"Value": "0.9"``

               ``}``

                HyperParameters

              To define a hyperparameter filter, enter a value with the form
              ``"HyperParameters.<name>"`` . Decimal hyperparameter values are treated as a decimal
              in a comparison if the specified ``Value`` is also a decimal value. If the specified
              ``Value`` is an integer, the decimal hyperparameter values are treated as integers.
              For example, the following filter is satisfied by training jobs with a
              ``"learning_rate"`` hyperparameter that is less than ``"0.5"`` :

               ``{``

               ``"Name": "HyperParameters.learning_rate",``

               ``"Operator": "LESS_THAN",``

               ``"Value": "0.5"``

               ``}``

                Tags

              To define a tag filter, enter a value with the form ``"Tags.<key>"`` .

              - **Name** *(string) --* **[REQUIRED]**

                A property name. For example, ``TrainingJobName`` . For the list of valid property
                names returned in a search result for each supported resource, see  TrainingJob
                properties. You must specify a valid property name for the resource.

              - **Operator** *(string) --*

                A Boolean binary operator that is used to evaluate the filter. The operator field
                contains one of the following values:

                  Equals

                The specified resource in ``Name`` equals the specified ``Value`` .

                  NotEquals

                The specified resource in ``Name`` does not equal the specified ``Value`` .

                  GreaterThan

                The specified resource in ``Name`` is greater than the specified ``Value`` . Not
                supported for text-based properties.

                  GreaterThanOrEqualTo

                The specified resource in ``Name`` is greater than or equal to the specified
                ``Value`` . Not supported for text-based properties.

                  LessThan

                The specified resource in ``Name`` is less than the specified ``Value`` . Not
                supported for text-based properties.

                  LessThanOrEqualTo

                The specified resource in ``Name`` is less than or equal to the specified ``Value``
                . Not supported for text-based properties.

                  Contains

                Only supported for text-based properties. The word-list of the property contains the
                specified ``Value`` . A ``SearchExpression`` can include only one ``Contains``
                operator.

                If you have specified a filter ``Value`` , the default is ``Equals`` .

              - **Value** *(string) --*

                A value used with ``Resource`` and ``Operator`` to determine if objects satisfy the
                filter's condition. For numerical properties, ``Value`` must be an integer or
                floating-point decimal. For timestamp properties, ``Value`` must be an ISO 8601
                date-time string of the following format: ``YYYY-mm-dd'T'HH:MM:SS`` .

          - **NestedFilters** *(list) --*

            A list of nested filter objects.

            - *(dict) --*

              Defines a list of ``NestedFilters`` objects. To satisfy the conditions specified in
              the ``NestedFilters`` call, a resource must satisfy the conditions of all of the
              filters.

              For example, you could define a ``NestedFilters`` using the training job's
              ``InputDataConfig`` property to filter on ``Channel`` objects.

              A ``NestedFilters`` object contains multiple filters. For example, to find all
              training jobs whose name contains ``train`` and that have ``cat/data`` in their
              ``S3Uri`` (specified in ``InputDataConfig`` ), you need to create a ``NestedFilters``
              object that specifies the ``InputDataConfig`` property with the following ``Filter``
              objects:

              * ``'{Name:"InputDataConfig.ChannelName", "Operator":"EQUALS", "Value":"train"}',``

              * ``'{Name:"InputDataConfig.DataSource.S3DataSource.S3Uri", "Operator":"CONTAINS",
              "Value":"cat/data"}'``

              - **NestedPropertyName** *(string) --* **[REQUIRED]**

                The name of the property to use in the nested filters. The value must match a listed
                property name, such as ``InputDataConfig`` .

              - **Filters** *(list) --* **[REQUIRED]**

                A list of filters. Each filter acts on a property. Filters must contain at least one
                ``Filters`` value. For example, a ``NestedFilters`` call might include a filter on
                the ``PropertyName`` parameter of the ``InputDataConfig`` property:
                ``InputDataConfig.DataSource.S3DataSource.S3Uri`` .

                - *(dict) --*

                  A conditional statement for a search expression that includes a resource property,
                  a Boolean operator, and a value.

                  If you don't specify an ``Operator`` and a ``Value`` , the filter searches for
                  only the specified property. For example, defining a ``Filter`` for the
                  ``FailureReason`` for the ``TrainingJob``  ``Resource`` searches for training job
                  objects that have a value in the ``FailureReason`` field.

                  If you specify a ``Value`` , but not an ``Operator`` , Amazon SageMaker uses the
                  equals operator as the default.

                  In search, there are several property types:

                    Metrics

                  To define a metric filter, enter a value using the form ``"Metrics.<name>"`` ,
                  where ``<name>`` is a metric name. For example, the following filter searches for
                  training jobs with an ``"accuracy"`` metric greater than ``"0.9"`` :

                   ``{``

                   ``"Name": "Metrics.accuracy",``

                   ``"Operator": "GREATER_THAN",``

                   ``"Value": "0.9"``

                   ``}``

                    HyperParameters

                  To define a hyperparameter filter, enter a value with the form
                  ``"HyperParameters.<name>"`` . Decimal hyperparameter values are treated as a
                  decimal in a comparison if the specified ``Value`` is also a decimal value. If the
                  specified ``Value`` is an integer, the decimal hyperparameter values are treated
                  as integers. For example, the following filter is satisfied by training jobs with
                  a ``"learning_rate"`` hyperparameter that is less than ``"0.5"`` :

                   ``{``

                   ``"Name": "HyperParameters.learning_rate",``

                   ``"Operator": "LESS_THAN",``

                   ``"Value": "0.5"``

                   ``}``

                    Tags

                  To define a tag filter, enter a value with the form ``"Tags.<key>"`` .

                  - **Name** *(string) --* **[REQUIRED]**

                    A property name. For example, ``TrainingJobName`` . For the list of valid
                    property names returned in a search result for each supported resource, see
                    TrainingJob properties. You must specify a valid property name for the resource.

                  - **Operator** *(string) --*

                    A Boolean binary operator that is used to evaluate the filter. The operator
                    field contains one of the following values:

                      Equals

                    The specified resource in ``Name`` equals the specified ``Value`` .

                      NotEquals

                    The specified resource in ``Name`` does not equal the specified ``Value`` .

                      GreaterThan

                    The specified resource in ``Name`` is greater than the specified ``Value`` . Not
                    supported for text-based properties.

                      GreaterThanOrEqualTo

                    The specified resource in ``Name`` is greater than or equal to the specified
                    ``Value`` . Not supported for text-based properties.

                      LessThan

                    The specified resource in ``Name`` is less than the specified ``Value`` . Not
                    supported for text-based properties.

                      LessThanOrEqualTo

                    The specified resource in ``Name`` is less than or equal to the specified
                    ``Value`` . Not supported for text-based properties.

                      Contains

                    Only supported for text-based properties. The word-list of the property contains
                    the specified ``Value`` . A ``SearchExpression`` can include only one
                    ``Contains`` operator.

                    If you have specified a filter ``Value`` , the default is ``Equals`` .

                  - **Value** *(string) --*

                    A value used with ``Resource`` and ``Operator`` to determine if objects satisfy
                    the filter's condition. For numerical properties, ``Value`` must be an integer
                    or floating-point decimal. For timestamp properties, ``Value`` must be an ISO
                    8601 date-time string of the following format: ``YYYY-mm-dd'T'HH:MM:SS`` .

          - **SubExpressions** *(list) --*

            A list of search expression objects.

            - *(dict) --*

              A multi-expression that searches for the specified resource or resources in a search.
              All resource objects that satisfy the expression's condition are included in the
              search results. You must specify at least one subexpression, filter, or nested filter.
              A ``SearchExpression`` can contain up to twenty elements.

              A ``SearchExpression`` contains the following components:

              * A list of ``Filter`` objects. Each filter defines a simple Boolean expression
              comprised of a resource property name, Boolean operator, and value. A
              ``SearchExpression`` can include only one ``Contains`` operator.

              * A list of ``NestedFilter`` objects. Each nested filter defines a list of Boolean
              expressions using a list of resource properties. A nested filter is satisfied if a
              single object in the list satisfies all Boolean expressions.

              * A list of ``SearchExpression`` objects. A search expression object can be nested in
              a list of search expression objects.

              * A Boolean operator: ``And`` or ``Or`` .

          - **Operator** *(string) --*

            A Boolean operator used to evaluate the search expression. If you want every conditional
            statement in all lists to be satisfied for the entire search expression to be true,
            specify ``And`` . If only a single conditional statement needs to be true for the entire
            search expression to be true, specify ``Or`` . The default value is ``And`` .

        :type SortBy: string
        :param SortBy:

          The name of the resource property used to sort the ``SearchResults`` . The default is
          ``LastModifiedTime`` .

        :type SortOrder: string
        :param SortOrder:

          How ``SearchResults`` are ordered. Valid values are ``Ascending`` or ``Descending`` . The
          default is ``Descending`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Results': [
                    {
                        'TrainingJob': {
                            'TrainingJobName': 'string',
                            'TrainingJobArn': 'string',
                            'TuningJobArn': 'string',
                            'LabelingJobArn': 'string',
                            'AutoMLJobArn': 'string',
                            'ModelArtifacts': {
                                'S3ModelArtifacts': 'string'
                            },
                            'TrainingJobStatus':
                            'InProgress'|'Completed'|'Failed'|'Stopping'
                            |'Stopped',
                            'SecondaryStatus':
                            'Starting'|'LaunchingMLInstances'
                            |'PreparingTrainingStack'|'Downloading'
                            |'DownloadingTrainingImage'|'Training'|'Uploading'
                            |'Stopping'|'Stopped'|'MaxRuntimeExceeded'
                            |'Completed'|'Failed'|'Interrupted'
                            |'MaxWaitTimeExceeded',
                            'FailureReason': 'string',
                            'HyperParameters': {
                                'string': 'string'
                            },
                            'AlgorithmSpecification': {
                                'TrainingImage': 'string',
                                'AlgorithmName': 'string',
                                'TrainingInputMode': 'Pipe'|'File',
                                'MetricDefinitions': [
                                    {
                                        'Name': 'string',
                                        'Regex': 'string'
                                    },
                                ],
                                'EnableSageMakerMetricsTimeSeries': True|False
                            },
                            'RoleArn': 'string',
                            'InputDataConfig': [
                                {
                                    'ChannelName': 'string',
                                    'DataSource': {
                                        'S3DataSource': {
                                            'S3DataType':
                                            'ManifestFile'
                                            |'S3Prefix'
                                            |'AugmentedManifestFile',
                                            'S3Uri': 'string',
                                            'S3DataDistributionType':
                                            'FullyReplicated'
                                            |'ShardedByS3Key',
                                            'AttributeNames': [
                                                'string',
                                            ]
                                        },
                                        'FileSystemDataSource': {
                                            'FileSystemId': 'string',
                                            'FileSystemAccessMode': 'rw'|'ro',
                                            'FileSystemType': 'EFS'|'FSxLustre',
                                            'DirectoryPath': 'string'
                                        }
                                    },
                                    'ContentType': 'string',
                                    'CompressionType': 'None'|'Gzip',
                                    'RecordWrapperType': 'None'|'RecordIO',
                                    'InputMode': 'Pipe'|'File',
                                    'ShuffleConfig': {
                                        'Seed': 123
                                    }
                                },
                            ],
                            'OutputDataConfig': {
                                'KmsKeyId': 'string',
                                'S3OutputPath': 'string'
                            },
                            'ResourceConfig': {
                                'InstanceType':
                                'ml.m4.xlarge'|'ml.m4.2xlarge'
                                |'ml.m4.4xlarge'|'ml.m4.10xlarge'
                                |'ml.m4.16xlarge'|'ml.m5.large'
                                |'ml.m5.xlarge'|'ml.m5.2xlarge'
                                |'ml.m5.4xlarge'|'ml.m5.12xlarge'
                                |'ml.m5.24xlarge'|'ml.c4.xlarge'
                                |'ml.c4.2xlarge'|'ml.c4.4xlarge'
                                |'ml.c4.8xlarge'|'ml.p2.xlarge'
                                |'ml.p2.8xlarge'|'ml.p2.16xlarge'
                                |'ml.p3.2xlarge'|'ml.p3.8xlarge'
                                |'ml.p3.16xlarge'|'ml.p3dn.24xlarge'
                                |'ml.c5.xlarge'|'ml.c5.2xlarge'
                                |'ml.c5.4xlarge'|'ml.c5.9xlarge'
                                |'ml.c5.18xlarge',
                                'InstanceCount': 123,
                                'VolumeSizeInGB': 123,
                                'VolumeKmsKeyId': 'string'
                            },
                            'VpcConfig': {
                                'SecurityGroupIds': [
                                    'string',
                                ],
                                'Subnets': [
                                    'string',
                                ]
                            },
                            'StoppingCondition': {
                                'MaxRuntimeInSeconds': 123,
                                'MaxWaitTimeInSeconds': 123
                            },
                            'CreationTime': datetime(2015, 1, 1),
                            'TrainingStartTime': datetime(2015, 1, 1),
                            'TrainingEndTime': datetime(2015, 1, 1),
                            'LastModifiedTime': datetime(2015, 1, 1),
                            'SecondaryStatusTransitions': [
                                {
                                    'Status':
                                    'Starting'|'LaunchingMLInstances'
                                    |'PreparingTrainingStack'
                                    |'Downloading'
                                    |'DownloadingTrainingImage'
                                    |'Training'|'Uploading'|'Stopping'
                                    |'Stopped'|'MaxRuntimeExceeded'
                                    |'Completed'|'Failed'|'Interrupted'
                                    |'MaxWaitTimeExceeded',
                                    'StartTime': datetime(2015, 1, 1),
                                    'EndTime': datetime(2015, 1, 1),
                                    'StatusMessage': 'string'
                                },
                            ],
                            'FinalMetricDataList': [
                                {
                                    'MetricName': 'string',
                                    'Value': ...,
                                    'Timestamp': datetime(2015, 1, 1)
                                },
                            ],
                            'EnableNetworkIsolation': True|False,
                            'EnableInterContainerTrafficEncryption': True|False,
                            'EnableManagedSpotTraining': True|False,
                            'CheckpointConfig': {
                                'S3Uri': 'string',
                                'LocalPath': 'string'
                            },
                            'TrainingTimeInSeconds': 123,
                            'BillableTimeInSeconds': 123,
                            'DebugHookConfig': {
                                'LocalPath': 'string',
                                'S3OutputPath': 'string',
                                'HookParameters': {
                                    'string': 'string'
                                },
                                'CollectionConfigurations': [
                                    {
                                        'CollectionName': 'string',
                                        'CollectionParameters': {
                                            'string': 'string'
                                        }
                                    },
                                ]
                            },
                            'ExperimentConfig': {
                                'ExperimentName': 'string',
                                'TrialName': 'string',
                                'TrialComponentDisplayName': 'string'
                            },
                            'DebugRuleConfigurations': [
                                {
                                    'RuleConfigurationName': 'string',
                                    'LocalPath': 'string',
                                    'S3OutputPath': 'string',
                                    'RuleEvaluatorImage': 'string',
                                    'InstanceType':
                                    'ml.t3.medium'|'ml.t3.large'
                                    |'ml.t3.xlarge'|'ml.t3.2xlarge'
                                    |'ml.m4.xlarge'|'ml.m4.2xlarge'
                                    |'ml.m4.4xlarge'|'ml.m4.10xlarge'
                                    |'ml.m4.16xlarge'|'ml.c4.xlarge'
                                    |'ml.c4.2xlarge'|'ml.c4.4xlarge'
                                    |'ml.c4.8xlarge'|'ml.p2.xlarge'
                                    |'ml.p2.8xlarge'|'ml.p2.16xlarge'
                                    |'ml.p3.2xlarge'|'ml.p3.8xlarge'
                                    |'ml.p3.16xlarge'|'ml.c5.xlarge'
                                    |'ml.c5.2xlarge'|'ml.c5.4xlarge'
                                    |'ml.c5.9xlarge'|'ml.c5.18xlarge'
                                    |'ml.m5.large'|'ml.m5.xlarge'
                                    |'ml.m5.2xlarge'|'ml.m5.4xlarge'
                                    |'ml.m5.12xlarge'|'ml.m5.24xlarge'
                                    |'ml.r5.large'|'ml.r5.xlarge'
                                    |'ml.r5.2xlarge'|'ml.r5.4xlarge'
                                    |'ml.r5.8xlarge'|'ml.r5.12xlarge'
                                    |'ml.r5.16xlarge'|'ml.r5.24xlarge',
                                    'VolumeSizeInGB': 123,
                                    'RuleParameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'TensorBoardOutputConfig': {
                                'LocalPath': 'string',
                                'S3OutputPath': 'string'
                            },
                            'DebugRuleEvaluationStatuses': [
                                {
                                    'RuleConfigurationName': 'string',
                                    'RuleEvaluationJobArn': 'string',
                                    'RuleEvaluationStatus':
                                    'InProgress'|'NoIssuesFound'
                                    |'IssuesFound'|'Error'|'Stopping'
                                    |'Stopped',
                                    'StatusDetails': 'string',
                                    'LastModifiedTime': datetime(2015, 1, 1)
                                },
                            ],
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'Experiment': {
                            'ExperimentName': 'string',
                            'ExperimentArn': 'string',
                            'DisplayName': 'string',
                            'Source': {
                                'SourceArn': 'string',
                                'SourceType': 'string'
                            },
                            'Description': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'CreatedBy': {
                                'UserProfileArn': 'string',
                                'UserProfileName': 'string',
                                'DomainId': 'string'
                            },
                            'LastModifiedTime': datetime(2015, 1, 1),
                            'LastModifiedBy': {
                                'UserProfileArn': 'string',
                                'UserProfileName': 'string',
                                'DomainId': 'string'
                            },
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'Trial': {
                            'TrialName': 'string',
                            'TrialArn': 'string',
                            'DisplayName': 'string',
                            'ExperimentName': 'string',
                            'Source': {
                                'SourceArn': 'string',
                                'SourceType': 'string'
                            },
                            'CreationTime': datetime(2015, 1, 1),
                            'CreatedBy': {
                                'UserProfileArn': 'string',
                                'UserProfileName': 'string',
                                'DomainId': 'string'
                            },
                            'LastModifiedTime': datetime(2015, 1, 1),
                            'LastModifiedBy': {
                                'UserProfileArn': 'string',
                                'UserProfileName': 'string',
                                'DomainId': 'string'
                            },
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'TrialComponentSummaries': [
                                {
                                    'TrialComponentName': 'string',
                                    'TrialComponentArn': 'string',
                                    'TrialComponentSource': {
                                        'SourceArn': 'string',
                                        'SourceType': 'string'
                                    },
                                    'CreationTime': datetime(2015, 1, 1),
                                    'CreatedBy': {
                                        'UserProfileArn': 'string',
                                        'UserProfileName': 'string',
                                        'DomainId': 'string'
                                    }
                                },
                            ]
                        },
                        'TrialComponent': {
                            'TrialComponentName': 'string',
                            'DisplayName': 'string',
                            'TrialComponentArn': 'string',
                            'Source': {
                                'SourceArn': 'string',
                                'SourceType': 'string'
                            },
                            'Status': {
                                'PrimaryStatus': 'InProgress'|'Completed'|'Failed',
                                'Message': 'string'
                            },
                            'StartTime': datetime(2015, 1, 1),
                            'EndTime': datetime(2015, 1, 1),
                            'CreationTime': datetime(2015, 1, 1),
                            'CreatedBy': {
                                'UserProfileArn': 'string',
                                'UserProfileName': 'string',
                                'DomainId': 'string'
                            },
                            'LastModifiedTime': datetime(2015, 1, 1),
                            'LastModifiedBy': {
                                'UserProfileArn': 'string',
                                'UserProfileName': 'string',
                                'DomainId': 'string'
                            },
                            'Parameters': {
                                'string': {
                                    'StringValue': 'string',
                                    'NumberValue': 123.0
                                }
                            },
                            'InputArtifacts': {
                                'string': {
                                    'MediaType': 'string',
                                    'Value': 'string'
                                }
                            },
                            'OutputArtifacts': {
                                'string': {
                                    'MediaType': 'string',
                                    'Value': 'string'
                                }
                            },
                            'Metrics': [
                                {
                                    'MetricName': 'string',
                                    'SourceArn': 'string',
                                    'TimeStamp': datetime(2015, 1, 1),
                                    'Max': 123.0,
                                    'Min': 123.0,
                                    'Last': 123.0,
                                    'Count': 123,
                                    'Avg': 123.0,
                                    'StdDev': 123.0
                                },
                            ],
                            'SourceDetail': {
                                'SourceArn': 'string',
                                'TrainingJob': {
                                    'TrainingJobName': 'string',
                                    'TrainingJobArn': 'string',
                                    'TuningJobArn': 'string',
                                    'LabelingJobArn': 'string',
                                    'AutoMLJobArn': 'string',
                                    'ModelArtifacts': {
                                        'S3ModelArtifacts': 'string'
                                    },
                                    'TrainingJobStatus':
                                    'InProgress'|'Completed'|'Failed'
                                    |'Stopping'|'Stopped',
                                    'SecondaryStatus':
                                    'Starting'|'LaunchingMLInstances'
                                    |'PreparingTrainingStack'
                                    |'Downloading'
                                    |'DownloadingTrainingImage'
                                    |'Training'|'Uploading'|'Stopping'
                                    |'Stopped'|'MaxRuntimeExceeded'
                                    |'Completed'|'Failed'|'Interrupted'
                                    |'MaxWaitTimeExceeded',
                                    'FailureReason': 'string',
                                    'HyperParameters': {
                                        'string': 'string'
                                    },
                                    'AlgorithmSpecification': {
                                        'TrainingImage': 'string',
                                        'AlgorithmName': 'string',
                                        'TrainingInputMode': 'Pipe'|'File',
                                        'MetricDefinitions': [
                                            {
                                                'Name': 'string',
                                                'Regex': 'string'
                                            },
                                        ],
                                        'EnableSageMakerMetricsTimeSeries': True|False
                                    },
                                    'RoleArn': 'string',
                                    'InputDataConfig': [
                                        {
                                            'ChannelName': 'string',
                                            'DataSource': {
                                                'S3DataSource': {
                                                    'S3DataType':
                                                    'ManifestFile'|'S3Prefix'
                                                    |'AugmentedManifestFile',
                                                    'S3Uri': 'string',
                                                    'S3DataDistributionType':
                                                    'FullyReplicated'
                                                    |'ShardedByS3Key',
                                                    'AttributeNames': [
                                                        'string',
                                                    ]
                                                },
                                                'FileSystemDataSource': {
                                                    'FileSystemId': 'string',
                                                    'FileSystemAccessMode': 'rw'|'ro',
                                                    'FileSystemType': 'EFS'|'FSxLustre',
                                                    'DirectoryPath': 'string'
                                                }
                                            },
                                            'ContentType': 'string',
                                            'CompressionType': 'None'|'Gzip',
                                            'RecordWrapperType': 'None'|'RecordIO',
                                            'InputMode': 'Pipe'|'File',
                                            'ShuffleConfig': {
                                                'Seed': 123
                                            }
                                        },
                                    ],
                                    'OutputDataConfig': {
                                        'KmsKeyId': 'string',
                                        'S3OutputPath': 'string'
                                    },
                                    'ResourceConfig': {
                                        'InstanceType':
                                        'ml.m4.xlarge'
                                        |'ml.m4.2xlarge'
                                        |'ml.m4.4xlarge'
                                        |'ml.m4.10xlarge'
                                        |'ml.m4.16xlarge'
                                        |'ml.m5.large'
                                        |'ml.m5.xlarge'
                                        |'ml.m5.2xlarge'
                                        |'ml.m5.4xlarge'
                                        |'ml.m5.12xlarge'
                                        |'ml.m5.24xlarge'
                                        |'ml.c4.xlarge'
                                        |'ml.c4.2xlarge'
                                        |'ml.c4.4xlarge'
                                        |'ml.c4.8xlarge'
                                        |'ml.p2.xlarge'
                                        |'ml.p2.8xlarge'
                                        |'ml.p2.16xlarge'
                                        |'ml.p3.2xlarge'
                                        |'ml.p3.8xlarge'
                                        |'ml.p3.16xlarge'
                                        |'ml.p3dn.24xlarge'
                                        |'ml.c5.xlarge'
                                        |'ml.c5.2xlarge'
                                        |'ml.c5.4xlarge'
                                        |'ml.c5.9xlarge'
                                        |'ml.c5.18xlarge',
                                        'InstanceCount': 123,
                                        'VolumeSizeInGB': 123,
                                        'VolumeKmsKeyId': 'string'
                                    },
                                    'VpcConfig': {
                                        'SecurityGroupIds': [
                                            'string',
                                        ],
                                        'Subnets': [
                                            'string',
                                        ]
                                    },
                                    'StoppingCondition': {
                                        'MaxRuntimeInSeconds': 123,
                                        'MaxWaitTimeInSeconds': 123
                                    },
                                    'CreationTime': datetime(2015, 1, 1),
                                    'TrainingStartTime': datetime(2015, 1, 1),
                                    'TrainingEndTime': datetime(2015, 1, 1),
                                    'LastModifiedTime': datetime(2015, 1, 1),
                                    'SecondaryStatusTransitions': [
                                        {
                                            'Status':
                                            'Starting'
                                            |'LaunchingMLInstances'|'PreparingTrainingStack'|'Downloading'|'DownloadingTrainingImage'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed'|'Interrupted'
                                            |'MaxWaitTimeExceeded',
                                            'StartTime': datetime(2015, 1, 1),
                                            'EndTime': datetime(2015, 1, 1),
                                            'StatusMessage': 'string'
                                        },
                                    ],
                                    'FinalMetricDataList': [
                                        {
                                            'MetricName': 'string',
                                            'Value': ...,
                                            'Timestamp': datetime(2015, 1, 1)
                                        },
                                    ],
                                    'EnableNetworkIsolation': True|False,
                                    'EnableInterContainerTrafficEncryption': True|False,
                                    'EnableManagedSpotTraining': True|False,
                                    'CheckpointConfig': {
                                        'S3Uri': 'string',
                                        'LocalPath': 'string'
                                    },
                                    'TrainingTimeInSeconds': 123,
                                    'BillableTimeInSeconds': 123,
                                    'DebugHookConfig': {
                                        'LocalPath': 'string',
                                        'S3OutputPath': 'string',
                                        'HookParameters': {
                                            'string': 'string'
                                        },
                                        'CollectionConfigurations': [
                                            {
                                                'CollectionName': 'string',
                                                'CollectionParameters': {
                                                    'string': 'string'
                                                }
                                            },
                                        ]
                                    },
                                    'ExperimentConfig': {
                                        'ExperimentName': 'string',
                                        'TrialName': 'string',
                                        'TrialComponentDisplayName': 'string'
                                    },
                                    'DebugRuleConfigurations': [
                                        {
                                            'RuleConfigurationName': 'string',
                                            'LocalPath': 'string',
                                            'S3OutputPath': 'string',
                                            'RuleEvaluatorImage': 'string',
                                            'InstanceType':
                                            'ml.t3.medium'
                                            |'ml.t3.large'
                                            |'ml.t3.xlarge'
                                            |'ml.t3.2xlarge'
                                            |'ml.m4.xlarge'
                                            |'ml.m4.2xlarge'
                                            |'ml.m4.4xlarge'
                                            |'ml.m4.10xlarge'
                                            |'ml.m4.16xlarge'
                                            |'ml.c4.xlarge'
                                            |'ml.c4.2xlarge'
                                            |'ml.c4.4xlarge'
                                            |'ml.c4.8xlarge'
                                            |'ml.p2.xlarge'
                                            |'ml.p2.8xlarge'
                                            |'ml.p2.16xlarge'
                                            |'ml.p3.2xlarge'
                                            |'ml.p3.8xlarge'
                                            |'ml.p3.16xlarge'
                                            |'ml.c5.xlarge'
                                            |'ml.c5.2xlarge'
                                            |'ml.c5.4xlarge'
                                            |'ml.c5.9xlarge'
                                            |'ml.c5.18xlarge'
                                            |'ml.m5.large'
                                            |'ml.m5.xlarge'
                                            |'ml.m5.2xlarge'
                                            |'ml.m5.4xlarge'
                                            |'ml.m5.12xlarge'
                                            |'ml.m5.24xlarge'
                                            |'ml.r5.large'
                                            |'ml.r5.xlarge'
                                            |'ml.r5.2xlarge'
                                            |'ml.r5.4xlarge'
                                            |'ml.r5.8xlarge'
                                            |'ml.r5.12xlarge'
                                            |'ml.r5.16xlarge'
                                            |'ml.r5.24xlarge',
                                            'VolumeSizeInGB': 123,
                                            'RuleParameters': {
                                                'string': 'string'
                                            }
                                        },
                                    ],
                                    'TensorBoardOutputConfig': {
                                        'LocalPath': 'string',
                                        'S3OutputPath': 'string'
                                    },
                                    'DebugRuleEvaluationStatuses': [
                                        {
                                            'RuleConfigurationName': 'string',
                                            'RuleEvaluationJobArn': 'string',
                                            'RuleEvaluationStatus':
                                            'InProgress'
                                            |'NoIssuesFound'
                                            |'IssuesFound'
                                            |'Error'|'Stopping'
                                            |'Stopped',
                                            'StatusDetails': 'string',
                                            'LastModifiedTime': datetime(2015, 1, 1)
                                        },
                                    ],
                                    'Tags': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                }
                            },
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'Parents': [
                                {
                                    'TrialName': 'string',
                                    'ExperimentName': 'string'
                                },
                            ]
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Results** *(list) --*

              A list of ``SearchResult`` objects.

              - *(dict) --*

                An individual search result record that contains a single resource object.

                - **TrainingJob** *(dict) --*

                  A ``TrainingJob`` object that is returned as part of a ``Search`` request.

                  - **TrainingJobName** *(string) --*

                    The name of the training job.

                  - **TrainingJobArn** *(string) --*

                    The Amazon Resource Name (ARN) of the training job.

                  - **TuningJobArn** *(string) --*

                    The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if
                    the training job was launched by a hyperparameter tuning job.

                  - **LabelingJobArn** *(string) --*

                    The Amazon Resource Name (ARN) of the labeling job.

                  - **AutoMLJobArn** *(string) --*

                    The Amazon Resource Name (ARN) of the job.

                  - **ModelArtifacts** *(dict) --*

                    Information about the Amazon S3 location that is configured for storing model
                    artifacts.

                    - **S3ModelArtifacts** *(string) --*

                      The path of the S3 object that contains the model artifacts. For example,
                      ``s3://bucket-name/keynameprefix/model.tar.gz`` .

                  - **TrainingJobStatus** *(string) --*

                    The status of the training job.

                    Training job statuses are:

                    * ``InProgress`` - The training is in progress.

                    * ``Completed`` - The training job has completed.

                    * ``Failed`` - The training job has failed. To see the reason for the failure,
                    see the ``FailureReason`` field in the response to a
                    ``DescribeTrainingJobResponse`` call.

                    * ``Stopping`` - The training job is stopping.

                    * ``Stopped`` - The training job has stopped.

                    For more detailed information, see ``SecondaryStatus`` .

                  - **SecondaryStatus** *(string) --*

                    Provides detailed information about the state of the training job. For detailed
                    information about the secondary status of the training job, see
                    ``StatusMessage`` under  SecondaryStatusTransition .

                    Amazon SageMaker provides primary statuses and secondary statuses that apply to
                    each of them:

                      InProgress

                    * ``Starting`` - Starting the training job.

                    * ``Downloading`` - An optional stage for algorithms that support ``File``
                    training input mode. It indicates that data is being downloaded to the ML
                    storage volumes.

                    * ``Training`` - Training is in progress.

                    * ``Uploading`` - Training is complete and the model artifacts are being
                    uploaded to the S3 location.

                      Completed

                    * ``Completed`` - The training job has completed.

                      Failed

                    * ``Failed`` - The training job has failed. The reason for the failure is
                    returned in the ``FailureReason`` field of ``DescribeTrainingJobResponse`` .

                      Stopped

                    * ``MaxRuntimeExceeded`` - The job stopped because it exceeded the maximum
                    allowed runtime.

                    * ``Stopped`` - The training job has stopped.

                      Stopping

                    * ``Stopping`` - Stopping the training job.

                    .. warning::

                      Valid values for ``SecondaryStatus`` are subject to change.

                    We no longer support the following secondary statuses:

                    * ``LaunchingMLInstances``

                    * ``PreparingTrainingStack``

                    * ``DownloadingTrainingImage``

                  - **FailureReason** *(string) --*

                    If the training job failed, the reason it failed.

                  - **HyperParameters** *(dict) --*

                    Algorithm-specific parameters.

                    - *(string) --*

                      - *(string) --*

                  - **AlgorithmSpecification** *(dict) --*

                    Information about the algorithm used for training, and algorithm metadata.

                    - **TrainingImage** *(string) --*

                      The registry path of the Docker image that contains the training algorithm.
                      For information about docker registry paths for built-in algorithms, see
                      `Algorithms Provided by Amazon SageMaker\\: Common Parameters
                      <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__
                      . Amazon SageMaker supports both ``registry/repository[:tag]`` and
                      ``registry/repository[@digest]`` image path formats. For more information, see
                      `Using Your Own Algorithms with Amazon SageMaker
                      <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .

                    - **AlgorithmName** *(string) --*

                      The name of the algorithm resource to use for the training job. This must be
                      an algorithm resource that you created or subscribe to on AWS Marketplace. If
                      you specify a value for this parameter, you can't specify a value for
                      ``TrainingImage`` .

                    - **TrainingInputMode** *(string) --*

                      The input mode that the algorithm supports. For the input modes that Amazon
                      SageMaker algorithms support, see `Algorithms
                      <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an
                      algorithm supports the ``File`` input mode, Amazon SageMaker downloads the
                      training data from S3 to the provisioned ML storage Volume, and mounts the
                      directory to docker volume for training container. If an algorithm supports
                      the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the
                      container.

                      In File mode, make sure you provision ML storage volume with sufficient
                      capacity to accommodate the data download from S3. In addition to the training
                      data, the ML storage volume also stores the output model. The algorithm
                      container use ML storage volume to also store intermediate information, if
                      any.

                      For distributed algorithms using File mode, training data is distributed
                      uniformly, and your training duration is predictable if the input data objects
                      size is approximately same. Amazon SageMaker does not split the files any
                      further for model training. If the object sizes are skewed, training won't be
                      optimal as the data distribution is also skewed where one host in a training
                      cluster is overloaded, thus becoming bottleneck in training.

                    - **MetricDefinitions** *(list) --*

                      A list of metric definition objects. Each object specifies the metric name and
                      regular expressions used to parse algorithm logs. Amazon SageMaker publishes
                      each metric to Amazon CloudWatch.

                      - *(dict) --*

                        Specifies a metric that the training algorithm writes to ``stderr`` or
                        ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined
                        metrics. You specify one metric that a hyperparameter tuning job uses as its
                        objective metric to choose the best training job.

                        - **Name** *(string) --*

                          The name of the metric.

                        - **Regex** *(string) --*

                          A regular expression that searches the output of a training job and gets
                          the value of the metric. For more information about using regular
                          expressions to define metrics, see `Defining Objective Metrics
                          <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__
                          .

                    - **EnableSageMakerMetricsTimeSeries** *(boolean) --*

                      To generate and save time-series metrics during training, set to ``true`` .
                      The default is ``false`` and time-series metrics aren't generated except in
                      the following cases:

                      * You use one of the Amazon SageMaker built-in algorithms

                      * You use one of the following prebuilt Amazon SageMaker Docker images:

                        * Tensorflow

                        * MXNet

                        * PyTorch

                      * You specify at least one  MetricDefinition

                  - **RoleArn** *(string) --*

                    The AWS Identity and Access Management (IAM) role configured for the training
                    job.

                  - **InputDataConfig** *(list) --*

                    An array of ``Channel`` objects that describes each data input channel.

                    - *(dict) --*

                      A channel is a named input source that training algorithms can consume.

                      - **ChannelName** *(string) --*

                        The name of the channel.

                      - **DataSource** *(dict) --*

                        The location of the channel data.

                        - **S3DataSource** *(dict) --*

                          The S3 location of the data source that is associated with a channel.

                          - **S3DataType** *(string) --*

                            If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix.
                            Amazon SageMaker uses all objects that match the specified key name
                            prefix for model training.

                            If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is
                            a manifest file containing a list of object keys that you want Amazon
                            SageMaker to use for model training.

                            If you choose ``AugmentedManifestFile`` , S3Uri identifies an object
                            that is an augmented manifest file in JSON lines format. This file
                            contains the data you want to use for model training.
                            ``AugmentedManifestFile`` can only be used if the Channel's input mode
                            is ``Pipe`` .

                          - **S3Uri** *(string) --*

                            Depending on the value specified for the ``S3DataType`` , identifies
                            either a key name prefix or a manifest. For example:

                            * A key name prefix might look like this:
                            ``s3://bucketname/exampleprefix`` .

                            * A manifest might look like this: ``s3://bucketname/example.manifest``
                            The manifest is an S3 object which is a JSON file with the following
                            format:  The preceding JSON matches the following ``s3Uris`` :   ``[
                            {"prefix": "s3://customer_bucket/some/prefix/"},``
                            ``"relative/path/to/custdata-1",``    ``"relative/path/custdata-2",``
                            ``...``    ``"relative/path/custdata-N"``    ``]``   The preceding JSON
                            matches the following ``s3Uris`` :
                            ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``
                            ``s3://customer_bucket/some/prefix/relative/path/custdata-2``    ``...``
                            ``s3://customer_bucket/some/prefix/relative/path/custdata-N``   The
                            complete set of ``s3uris`` in this manifest is the input data for the
                            channel for this datasource. The object that each ``s3uris`` points to
                            must be readable by the IAM role that Amazon SageMaker uses to perform
                            tasks on your behalf.

                          - **S3DataDistributionType** *(string) --*

                            If you want Amazon SageMaker to replicate the entire dataset on each ML
                            compute instance that is launched for model training, specify
                            ``FullyReplicated`` .

                            If you want Amazon SageMaker to replicate a subset of data on each ML
                            compute instance that is launched for model training, specify
                            ``ShardedByS3Key`` . If there are *n* ML compute instances launched for
                            a training job, each instance gets approximately 1/*n* of the number of
                            S3 objects. In this case, model training on each machine uses only the
                            subset of training data.

                            Don't choose more ML compute instances for training than available S3
                            objects. If you do, some nodes won't get any data and you will pay for
                            nodes that aren't getting any training data. This applies in both File
                            and Pipe modes. Keep this in mind when developing algorithms.

                            In distributed training, where you use multiple ML compute EC2
                            instances, you might choose ``ShardedByS3Key`` . If the algorithm
                            requires copying training data to the ML storage volume (when
                            ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the
                            number of objects.

                          - **AttributeNames** *(list) --*

                            A list of one or more attribute names to use that are found in a
                            specified augmented manifest file.

                            - *(string) --*

                        - **FileSystemDataSource** *(dict) --*

                          The file system that is associated with a channel.

                          - **FileSystemId** *(string) --*

                            The file system id.

                          - **FileSystemAccessMode** *(string) --*

                            The access mode of the mount of the directory associated with the
                            channel. A directory can be mounted either in ``ro`` (read-only) or
                            ``rw`` (read-write) mode.

                          - **FileSystemType** *(string) --*

                            The file system type.

                          - **DirectoryPath** *(string) --*

                            The full path to the directory to associate with the channel.

                      - **ContentType** *(string) --*

                        The MIME type of the data.

                      - **CompressionType** *(string) --*

                        If training data is compressed, the compression type. The default value is
                        ``None`` . ``CompressionType`` is used only in Pipe input mode. In File
                        mode, leave this field unset or set it to None.

                      - **RecordWrapperType** *(string) --*

                        Specify RecordIO as the value when input data is in raw format but the
                        training algorithm requires the RecordIO format. In this case, Amazon
                        SageMaker wraps each individual S3 object in a RecordIO record. If the input
                        data is already in RecordIO format, you don't need to set this attribute.
                        For more information, see `Create a Dataset Using RecordIO
                        <https://mxnet.apache.org/api/architecture/note_data_loading#data-format>`__
                        .

                        In File mode, leave this field unset or set it to None.

                      - **InputMode** *(string) --*

                        (Optional) The input mode to use for the data channel in a training job. If
                        you don't set a value for ``InputMode`` , Amazon SageMaker uses the value
                        set for ``TrainingInputMode`` . Use this parameter to override the
                        ``TrainingInputMode`` setting in a  AlgorithmSpecification request when you
                        have a channel that needs a different input mode from the training job's
                        general setting. To download the data from Amazon Simple Storage Service
                        (Amazon S3) to the provisioned ML storage volume, and mount the directory to
                        a Docker volume, use ``File`` input mode. To stream data directly from
                        Amazon S3 to the container, choose ``Pipe`` input mode.

                        To use a model for incremental training, choose ``File`` input model.

                      - **ShuffleConfig** *(dict) --*

                        A configuration for a shuffle option for input data in a channel. If you use
                        ``S3Prefix`` for ``S3DataType`` , this shuffles the results of the S3 key
                        prefix matches. If you use ``ManifestFile`` , the order of the S3 object
                        references in the ``ManifestFile`` is shuffled. If you use
                        ``AugmentedManifestFile`` , the order of the JSON lines in the
                        ``AugmentedManifestFile`` is shuffled. The shuffling order is determined
                        using the ``Seed`` value.

                        For Pipe input mode, shuffling is done at the start of every epoch. With
                        large datasets this ensures that the order of the training data is different
                        for each epoch, it helps reduce bias and possible overfitting. In a
                        multi-node training job when ShuffleConfig is combined with
                        ``S3DataDistributionType`` of ``ShardedByS3Key`` , the data is shuffled
                        across nodes so that the content sent to a particular node on the first
                        epoch might be sent to a different node on the second epoch.

                        - **Seed** *(integer) --*

                          Determines the shuffling order in ``ShuffleConfig`` value.

                  - **OutputDataConfig** *(dict) --*

                    The S3 path where model artifacts that you configured when creating the job are
                    stored. Amazon SageMaker creates subfolders for model artifacts.

                    - **KmsKeyId** *(string) --*

                      The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to
                      encrypt the model artifacts at rest using Amazon S3 server-side encryption.
                      The ``KmsKeyId`` can be any of the following formats:

                      * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                      * // Amazon Resource Name (ARN) of a KMS Key
                      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                      * // KMS Key Alias  ``"alias/ExampleAlias"``

                      * // Amazon Resource Name (ARN) of a KMS Key Alias
                      ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                      If you use a KMS key ID or an alias of your master key, the Amazon SageMaker
                      execution role must include permissions to call ``kms:Encrypt`` . If you don't
                      provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3
                      for your role's account. Amazon SageMaker uses server-side encryption with
                      KMS-managed keys for ``OutputDataConfig`` . If you use a bucket policy with an
                      ``s3:PutObject`` permission that only allows objects with server-side
                      encryption, set the condition key of ``s3:x-amz-server-side-encryption`` to
                      ``"aws:kms"`` . For more information, see `KMS-Managed Encryption Keys
                      <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__
                      in the *Amazon Simple Storage Service Developer Guide.*

                      The KMS key policy must grant permission to the IAM role that you specify in
                      your ``CreateTrainingJob`` , ``CreateTransformJob`` , or
                      ``CreateHyperParameterTuningJob`` requests. For more information, see `Using
                      Key Policies in AWS KMS
                      <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in
                      the *AWS Key Management Service Developer Guide* .

                    - **S3OutputPath** *(string) --*

                      Identifies the S3 path where you want Amazon SageMaker to store the model
                      artifacts. For example, ``s3://bucket-name/key-name-prefix`` .

                  - **ResourceConfig** *(dict) --*

                    Resources, including ML compute instances and ML storage volumes, that are
                    configured for model training.

                    - **InstanceType** *(string) --*

                      The ML compute instance type.

                    - **InstanceCount** *(integer) --*

                      The number of ML compute instances to use. For distributed training, provide a
                      value greater than 1.

                    - **VolumeSizeInGB** *(integer) --*

                      The size of the ML storage volume that you want to provision.

                      ML storage volumes store model artifacts and incremental states. Training
                      algorithms might also use the ML storage volume for scratch space. If you want
                      to store the training data in the ML storage volume, choose ``File`` as the
                      ``TrainingInputMode`` in the algorithm specification.

                      You must specify sufficient ML storage for your scenario.

                      .. note::

                        Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage
                        volume type.

                      .. note::

                        Certain Nitro-based instances include local storage with a fixed total size,
                        dependent on the instance type. When using these instances for training,
                        Amazon SageMaker mounts the local instance storage instead of Amazon EBS gp2
                        storage. You can't request a ``VolumeSizeInGB`` greater than the total size
                        of the local instance storage.

                        For a list of instance types that support local instance storage, including
                        the total size per instance type, see `Instance Store Volumes
                        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes>`__
                        .

                    - **VolumeKmsKeyId** *(string) --*

                      The AWS KMS key that Amazon SageMaker uses to encrypt data on the storage
                      volume attached to the ML compute instance(s) that run the training job.

                      .. note::

                        Certain Nitro-based instances include local storage, dependent on the
                        instance type. Local storage volumes are encrypted using a hardware module
                        on the instance. You can't request a ``VolumeKmsKeyId`` when using an
                        instance type with local storage.

                        For a list of instance types that support local instance storage, see
                        `Instance Store Volumes
                        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes>`__
                        .

                        For more information about local instance storage encryption, see `SSD
                        Instance Store Volumes
                        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html>`__
                        .

                      The ``VolumeKmsKeyId`` can be in any of the following formats:

                      * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                      * // Amazon Resource Name (ARN) of a KMS Key
                      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                  - **VpcConfig** *(dict) --*

                    A  VpcConfig object that specifies the VPC that this training job has access to.
                    For more information, see `Protect Training Jobs by Using an Amazon Virtual
                    Private Cloud
                    <https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .

                    - **SecurityGroupIds** *(list) --*

                      The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security
                      groups for the VPC that is specified in the ``Subnets`` field.

                      - *(string) --*

                    - **Subnets** *(list) --*

                      The ID of the subnets in the VPC to which you want to connect your training
                      job or model.

                      .. note::

                        Amazon EC2 P3 accelerated computing instances are not available in the c/d/e
                        availability zones of region us-east-1. If you want to create endpoints with
                        P3 instances in VPC mode in region us-east-1, create subnets in a/b/f
                        availability zones instead.

                      - *(string) --*

                  - **StoppingCondition** *(dict) --*

                    Specifies a limit to how long a model training job can run. When the job reaches
                    the time limit, Amazon SageMaker ends the training job. Use this API to cap
                    model training costs.

                    To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal,
                    which delays job termination for 120 seconds. Algorithms can use this 120-second
                    window to save the model artifacts, so the results of training are not lost.

                    - **MaxRuntimeInSeconds** *(integer) --*

                      The maximum length of time, in seconds, that the training or compilation job
                      can run. If job does not complete during this time, Amazon SageMaker ends the
                      job. If value is not specified, default value is 1 day. The maximum value is
                      28 days.

                    - **MaxWaitTimeInSeconds** *(integer) --*

                      The maximum length of time, in seconds, how long you are willing to wait for a
                      managed spot training job to complete. It is the amount of time spent waiting
                      for Spot capacity plus the amount of time the training job runs. It must be
                      equal to or greater than ``MaxRuntimeInSeconds`` .

                  - **CreationTime** *(datetime) --*

                    A timestamp that indicates when the training job was created.

                  - **TrainingStartTime** *(datetime) --*

                    Indicates the time when the training job starts on training instances. You are
                    billed for the time interval between this time and the value of
                    ``TrainingEndTime`` . The start time in CloudWatch Logs might be later than this
                    time. The difference is due to the time it takes to download the training data
                    and to the size of the training container.

                  - **TrainingEndTime** *(datetime) --*

                    Indicates the time when the training job ends on training instances. You are
                    billed for the time interval between the value of ``TrainingStartTime`` and this
                    time. For successful jobs and stopped jobs, this is the time after model
                    artifacts are uploaded. For failed jobs, this is the time when Amazon SageMaker
                    detects a job failure.

                  - **LastModifiedTime** *(datetime) --*

                    A timestamp that indicates when the status of the training job was last
                    modified.

                  - **SecondaryStatusTransitions** *(list) --*

                    A history of all of the secondary statuses that the training job has
                    transitioned through.

                    - *(dict) --*

                      An array element of  DescribeTrainingJobResponse$SecondaryStatusTransitions .
                      It provides additional details about a status that the training job has
                      transitioned through. A training job can be in one of several states, for
                      example, starting, downloading, training, or uploading. Within each state,
                      there are a number of intermediate states. For example, within the starting
                      state, Amazon SageMaker could be starting the training job or launching the ML
                      instances. These transitional states are referred to as the job's secondary
                      status.

                      - **Status** *(string) --*

                        Contains a secondary status information from a training job.

                        Status might be one of the following secondary statuses:

                          InProgress

                        * ``Starting`` - Starting the training job.

                        * ``Downloading`` - An optional stage for algorithms that support ``File``
                        training input mode. It indicates that data is being downloaded to the ML
                        storage volumes.

                        * ``Training`` - Training is in progress.

                        * ``Uploading`` - Training is complete and the model artifacts are being
                        uploaded to the S3 location.

                          Completed

                        * ``Completed`` - The training job has completed.

                          Failed

                        * ``Failed`` - The training job has failed. The reason for the failure is
                        returned in the ``FailureReason`` field of ``DescribeTrainingJobResponse`` .

                          Stopped

                        * ``MaxRuntimeExceeded`` - The job stopped because it exceeded the maximum
                        allowed runtime.

                        * ``Stopped`` - The training job has stopped.

                          Stopping

                        * ``Stopping`` - Stopping the training job.

                        We no longer support the following secondary statuses:

                        * ``LaunchingMLInstances``

                        * ``PreparingTrainingStack``

                        * ``DownloadingTrainingImage``

                      - **StartTime** *(datetime) --*

                        A timestamp that shows when the training job transitioned to the current
                        secondary status state.

                      - **EndTime** *(datetime) --*

                        A timestamp that shows when the training job transitioned out of this
                        secondary status state into another secondary status state or when the
                        training job has ended.

                      - **StatusMessage** *(string) --*

                        A detailed description of the progress within a secondary status.

                        Amazon SageMaker provides secondary statuses and status messages that apply
                        to each of them:

                          Starting

                        * Starting the training job.

                        * Launching requested ML instances.

                        * Insufficient capacity error from EC2 while launching instances, retrying!

                        * Launched instance was unhealthy, replacing it!

                        * Preparing the instances for training.

                          Training

                        * Downloading the training image.

                        * Training image download completed. Training in progress.

                        .. warning::

                          Status messages are subject to change. Therefore, we recommend not
                          including them in code that programmatically initiates actions. For
                          examples, don't use status messages in if statements.

                        To have an overview of your training job's progress, view
                        ``TrainingJobStatus`` and ``SecondaryStatus`` in  DescribeTrainingJob , and
                        ``StatusMessage`` together. For example, at the start of a training job, you
                        might see the following:

                        * ``TrainingJobStatus`` - InProgress

                        * ``SecondaryStatus`` - Training

                        * ``StatusMessage`` - Downloading the training image

                  - **FinalMetricDataList** *(list) --*

                    A list of final metric values that are set when the training job completes. Used
                    only if the training job was configured to use metrics.

                    - *(dict) --*

                      The name, value, and date and time of a metric that was emitted to Amazon
                      CloudWatch.

                      - **MetricName** *(string) --*

                        The name of the metric.

                      - **Value** *(float) --*

                        The value of the metric.

                      - **Timestamp** *(datetime) --*

                        The date and time that the algorithm emitted the metric.

                  - **EnableNetworkIsolation** *(boolean) --*

                    If the ``TrainingJob`` was created with network isolation, the value is set to
                    ``true`` . If network isolation is enabled, nodes can't communicate beyond the
                    VPC they run in.

                  - **EnableInterContainerTrafficEncryption** *(boolean) --*

                    To encrypt all communications between ML compute instances in distributed
                    training, choose ``True`` . Encryption provides greater security for distributed
                    training, but training might take longer. How long it takes depends on the
                    amount of communication between compute instances, especially if you use a deep
                    learning algorithm in distributed training.

                  - **EnableManagedSpotTraining** *(boolean) --*

                    When true, enables managed spot training using Amazon EC2 Spot instances to run
                    training jobs instead of on-demand instances. For more information, see
                    model-managed-spot-training .

                  - **CheckpointConfig** *(dict) --*

                    Contains information about the output location for managed spot training
                    checkpoint data.

                    - **S3Uri** *(string) --*

                      Identifies the S3 path where you want Amazon SageMaker to store checkpoints.
                      For example, ``s3://bucket-name/key-name-prefix`` .

                    - **LocalPath** *(string) --*

                      (Optional) The local directory where checkpoints are written. The default
                      directory is ``/opt/ml/checkpoints/`` .

                  - **TrainingTimeInSeconds** *(integer) --*

                    The training time in seconds.

                  - **BillableTimeInSeconds** *(integer) --*

                    The billable time in seconds.

                  - **DebugHookConfig** *(dict) --*

                    Configuration information for the debug hook parameters, collection
                    configuration, and storage paths.

                    - **LocalPath** *(string) --*

                      Path to local storage location for tensors. Defaults to
                      ``/opt/ml/output/tensors/`` .

                    - **S3OutputPath** *(string) --*

                      Path to Amazon S3 storage location for tensors.

                    - **HookParameters** *(dict) --*

                      Configuration information for the debug hook parameters.

                      - *(string) --*

                        - *(string) --*

                    - **CollectionConfigurations** *(list) --*

                      Configuration information for tensor collections.

                      - *(dict) --*

                        Configuration information for tensor collections.

                        - **CollectionName** *(string) --*

                          The name of the tensor collection.

                        - **CollectionParameters** *(dict) --*

                          Parameter values for the tensor collection. The allowed parameters are
                          ``"name"`` , ``"include_regex"`` , ``"reduction_config"`` ,
                          ``"save_config"`` , ``"tensor_names"`` , and ``"save_histogram"`` .

                          - *(string) --*

                            - *(string) --*

                  - **ExperimentConfig** *(dict) --*

                    Configuration for the experiment.

                    - **ExperimentName** *(string) --*

                      The name of the experiment.

                    - **TrialName** *(string) --*

                      The name of the trial.

                    - **TrialComponentDisplayName** *(string) --*

                      Display name for the trial component.

                  - **DebugRuleConfigurations** *(list) --*

                    Information about the debug rule configuration.

                    - *(dict) --*

                      Configuration information for debugging rules.

                      - **RuleConfigurationName** *(string) --*

                        The name of the rule configuration. It must be unique relative to other rule
                        configuration names.

                      - **LocalPath** *(string) --*

                        Path to local storage location for rules. Defaults to
                        ``/opt/ml/processing/output/rule/`` .

                      - **S3OutputPath** *(string) --*

                        Path to Amazon S3 storage location for rules.

                      - **RuleEvaluatorImage** *(string) --*

                        The Amazon Elastic Container (ECR) Image for the managed rule evaluation.

                      - **InstanceType** *(string) --*

                        The instance type to deploy for a training job.

                      - **VolumeSizeInGB** *(integer) --*

                        The size, in GB, of the ML storage volume attached to the notebook instance.

                      - **RuleParameters** *(dict) --*

                        Runtime configuration for rule container.

                        - *(string) --*

                          - *(string) --*

                  - **TensorBoardOutputConfig** *(dict) --*

                    Configuration of storage locations for TensorBoard output.

                    - **LocalPath** *(string) --*

                      Path to local storage location for tensorBoard output. Defaults to
                      ``/opt/ml/output/tensorboard`` .

                    - **S3OutputPath** *(string) --*

                      Path to Amazon S3 storage location for TensorBoard output.

                  - **DebugRuleEvaluationStatuses** *(list) --*

                    Information about the evaluation status of the rules for the training job.

                    - *(dict) --*

                      Information about the status of the rule evaluation.

                      - **RuleConfigurationName** *(string) --*

                        The name of the rule configuration

                      - **RuleEvaluationJobArn** *(string) --*

                        The Amazon Resource Name (ARN) of the rule evaluation job.

                      - **RuleEvaluationStatus** *(string) --*

                        Status of the rule evaluation.

                      - **StatusDetails** *(string) --*

                        Details from the rule evaluation.

                      - **LastModifiedTime** *(datetime) --*

                        Timestamp when the rule evaluation status was last modified.

                  - **Tags** *(list) --*

                    An array of key-value pairs. For more information, see `Using Cost Allocation
                    Tags
                    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__
                    in the *AWS Billing and Cost Management User Guide* .

                    - *(dict) --*

                      Describes a tag.

                      - **Key** *(string) --*

                        The tag key.

                      - **Value** *(string) --*

                        The tag value.

                - **Experiment** *(dict) --*

                  A summary of the properties of an experiment.

                  - **ExperimentName** *(string) --*

                    The name of the experiment.

                  - **ExperimentArn** *(string) --*

                    The Amazon Resource Name (ARN) of the experiment.

                  - **DisplayName** *(string) --*

                    The name of the experiment as displayed. If ``DisplayName`` isn't specified,
                    ``ExperimentName`` is displayed.

                  - **Source** *(dict) --*

                    The source of the experiment.

                    - **SourceArn** *(string) --*

                      The Amazon Resource Name (ARN) of the source.

                    - **SourceType** *(string) --*

                      The source type.

                  - **Description** *(string) --*

                    The description of the experiment.

                  - **CreationTime** *(datetime) --*

                    When the experiment was created.

                  - **CreatedBy** *(dict) --*

                    Information about the user who created or modified an experiment, trial, or
                    trial component.

                    - **UserProfileArn** *(string) --*

                      The Amazon Resource Name (ARN) of the user's profile.

                    - **UserProfileName** *(string) --*

                      The name of the user's profile.

                    - **DomainId** *(string) --*

                      The domain associated with the user.

                  - **LastModifiedTime** *(datetime) --*

                    When the experiment was last modified.

                  - **LastModifiedBy** *(dict) --*

                    Information about the user who created or modified an experiment, trial, or
                    trial component.

                    - **UserProfileArn** *(string) --*

                      The Amazon Resource Name (ARN) of the user's profile.

                    - **UserProfileName** *(string) --*

                      The name of the user's profile.

                    - **DomainId** *(string) --*

                      The domain associated with the user.

                  - **Tags** *(list) --*

                    The list of tags that are associated with the experiment. You can use  Search
                    API to search on the tags.

                    - *(dict) --*

                      Describes a tag.

                      - **Key** *(string) --*

                        The tag key.

                      - **Value** *(string) --*

                        The tag value.

                - **Trial** *(dict) --*

                  A summary of the properties of a trial.

                  - **TrialName** *(string) --*

                    The name of the trial.

                  - **TrialArn** *(string) --*

                    The Amazon Resource Name (ARN) of the trial.

                  - **DisplayName** *(string) --*

                    The name of the trial as displayed. If ``DisplayName`` isn't specified,
                    ``TrialName`` is displayed.

                  - **ExperimentName** *(string) --*

                    The name of the experiment the trial is part of.

                  - **Source** *(dict) --*

                    The source of the trial.

                    - **SourceArn** *(string) --*

                      The Amazon Resource Name (ARN) of the source.

                    - **SourceType** *(string) --*

                      The source job type.

                  - **CreationTime** *(datetime) --*

                    When the trial was created.

                  - **CreatedBy** *(dict) --*

                    Information about the user who created or modified an experiment, trial, or
                    trial component.

                    - **UserProfileArn** *(string) --*

                      The Amazon Resource Name (ARN) of the user's profile.

                    - **UserProfileName** *(string) --*

                      The name of the user's profile.

                    - **DomainId** *(string) --*

                      The domain associated with the user.

                  - **LastModifiedTime** *(datetime) --*

                    Who last modified the trial.

                  - **LastModifiedBy** *(dict) --*

                    Information about the user who created or modified an experiment, trial, or
                    trial component.

                    - **UserProfileArn** *(string) --*

                      The Amazon Resource Name (ARN) of the user's profile.

                    - **UserProfileName** *(string) --*

                      The name of the user's profile.

                    - **DomainId** *(string) --*

                      The domain associated with the user.

                  - **Tags** *(list) --*

                    The list of tags that are associated with the trial. You can use  Search API to
                    search on the tags.

                    - *(dict) --*

                      Describes a tag.

                      - **Key** *(string) --*

                        The tag key.

                      - **Value** *(string) --*

                        The tag value.

                  - **TrialComponentSummaries** *(list) --*

                    A list of the components associated with the trial. For each component, a
                    summary of the component's properties is included.

                    - *(dict) --*

                      A short summary of a trial component.

                      - **TrialComponentName** *(string) --*

                        The name of the trial component.

                      - **TrialComponentArn** *(string) --*

                        The Amazon Resource Name (ARN) of the trial component.

                      - **TrialComponentSource** *(dict) --*

                        The source of the trial component.

                        - **SourceArn** *(string) --*

                          The Amazon Resource Name (ARN) of the source.

                        - **SourceType** *(string) --*

                          The source job type.

                      - **CreationTime** *(datetime) --*

                        When the component was created.

                      - **CreatedBy** *(dict) --*

                        Information about the user who created or modified an experiment, trial, or
                        trial component.

                        - **UserProfileArn** *(string) --*

                          The Amazon Resource Name (ARN) of the user's profile.

                        - **UserProfileName** *(string) --*

                          The name of the user's profile.

                        - **DomainId** *(string) --*

                          The domain associated with the user.

                - **TrialComponent** *(dict) --*

                  A summary of the properties of a trial component.

                  - **TrialComponentName** *(string) --*

                    The name of the trial component.

                  - **DisplayName** *(string) --*

                    The name of the component as displayed. If ``DisplayName`` isn't specified,
                    ``TrialComponentName`` is displayed.

                  - **TrialComponentArn** *(string) --*

                    The Amazon Resource Name (ARN) of the trial component.

                  - **Source** *(dict) --*

                    The source of the trial component.

                    - **SourceArn** *(string) --*

                      The Amazon Resource Name (ARN) of the source.

                    - **SourceType** *(string) --*

                      The source job type.

                  - **Status** *(dict) --*

                    The status of the trial component.

                    - **PrimaryStatus** *(string) --*

                      The status of the trial component.

                    - **Message** *(string) --*

                      If the component failed, a message describing why.

                  - **StartTime** *(datetime) --*

                    When the component started.

                  - **EndTime** *(datetime) --*

                    When the component ended.

                  - **CreationTime** *(datetime) --*

                    When the component was created.

                  - **CreatedBy** *(dict) --*

                    Information about the user who created or modified an experiment, trial, or
                    trial component.

                    - **UserProfileArn** *(string) --*

                      The Amazon Resource Name (ARN) of the user's profile.

                    - **UserProfileName** *(string) --*

                      The name of the user's profile.

                    - **DomainId** *(string) --*

                      The domain associated with the user.

                  - **LastModifiedTime** *(datetime) --*

                    When the component was last modified.

                  - **LastModifiedBy** *(dict) --*

                    Information about the user who created or modified an experiment, trial, or
                    trial component.

                    - **UserProfileArn** *(string) --*

                      The Amazon Resource Name (ARN) of the user's profile.

                    - **UserProfileName** *(string) --*

                      The name of the user's profile.

                    - **DomainId** *(string) --*

                      The domain associated with the user.

                  - **Parameters** *(dict) --*

                    The hyperparameters of the component.

                    - *(string) --*

                      - *(dict) --*

                        The value of a hyperparameter. Only one of ``NumberValue`` or
                        ``StringValue`` can be specified.

                        This object is specified in the  CreateTrialComponent request.

                        - **StringValue** *(string) --*

                          The string value of a categorical hyperparameter. If you specify a value
                          for this parameter, you can't specify the ``NumberValue`` parameter.

                        - **NumberValue** *(float) --*

                          The numeric value of a numeric hyperparameter. If you specify a value for
                          this parameter, you can't specify the ``StringValue`` parameter.

                  - **InputArtifacts** *(dict) --*

                    The input artifacts of the component.

                    - *(string) --*

                      - *(dict) --*

                        Represents an input or output artifact of a trial component. You specify
                        ``TrialComponentArtifact`` as part of the ``InputArtifacts`` and
                        ``OutputArtifacts`` parameters in the  CreateTrialComponent request.

                        Examples of input artifacts are datasets, algorithms, hyperparameters,
                        source code, and instance types. Examples of output artifacts are metrics,
                        snapshots, logs, and images.

                        - **MediaType** *(string) --*

                          The media type of the artifact, which indicates the type of data in the
                          artifact file. The media type consists of a *type* and a *subtype*
                          concatenated with a slash (/) character, for example, text/csv,
                          image/jpeg, and s3/uri. The type specifies the category of the media. The
                          subtype specifies the kind of data.

                        - **Value** *(string) --*

                          The location of the artifact.

                  - **OutputArtifacts** *(dict) --*

                    The output artifacts of the component.

                    - *(string) --*

                      - *(dict) --*

                        Represents an input or output artifact of a trial component. You specify
                        ``TrialComponentArtifact`` as part of the ``InputArtifacts`` and
                        ``OutputArtifacts`` parameters in the  CreateTrialComponent request.

                        Examples of input artifacts are datasets, algorithms, hyperparameters,
                        source code, and instance types. Examples of output artifacts are metrics,
                        snapshots, logs, and images.

                        - **MediaType** *(string) --*

                          The media type of the artifact, which indicates the type of data in the
                          artifact file. The media type consists of a *type* and a *subtype*
                          concatenated with a slash (/) character, for example, text/csv,
                          image/jpeg, and s3/uri. The type specifies the category of the media. The
                          subtype specifies the kind of data.

                        - **Value** *(string) --*

                          The location of the artifact.

                  - **Metrics** *(list) --*

                    The metrics for the component.

                    - *(dict) --*

                      A summary of the metrics of a trial component.

                      - **MetricName** *(string) --*

                        The name of the metric.

                      - **SourceArn** *(string) --*

                        The Amazon Resource Name (ARN) of the source.

                      - **TimeStamp** *(datetime) --*

                        When the metric was last updated.

                      - **Max** *(float) --*

                        The maximum value of the metric.

                      - **Min** *(float) --*

                        The minimum value of the metric.

                      - **Last** *(float) --*

                        The most recent value of the metric.

                      - **Count** *(integer) --*

                        The number of samples used to generate the metric.

                      - **Avg** *(float) --*

                        The average value of the metric.

                      - **StdDev** *(float) --*

                        The standard deviation of the metric.

                  - **SourceDetail** *(dict) --*

                    The source of the trial component.>

                    - **SourceArn** *(string) --*

                      The Amazon Resource Name (ARN) of the source.

                    - **TrainingJob** *(dict) --*

                      Contains information about a training job.

                      - **TrainingJobName** *(string) --*

                        The name of the training job.

                      - **TrainingJobArn** *(string) --*

                        The Amazon Resource Name (ARN) of the training job.

                      - **TuningJobArn** *(string) --*

                        The Amazon Resource Name (ARN) of the associated hyperparameter tuning job
                        if the training job was launched by a hyperparameter tuning job.

                      - **LabelingJobArn** *(string) --*

                        The Amazon Resource Name (ARN) of the labeling job.

                      - **AutoMLJobArn** *(string) --*

                        The Amazon Resource Name (ARN) of the job.

                      - **ModelArtifacts** *(dict) --*

                        Information about the Amazon S3 location that is configured for storing
                        model artifacts.

                        - **S3ModelArtifacts** *(string) --*

                          The path of the S3 object that contains the model artifacts. For example,
                          ``s3://bucket-name/keynameprefix/model.tar.gz`` .

                      - **TrainingJobStatus** *(string) --*

                        The status of the training job.

                        Training job statuses are:

                        * ``InProgress`` - The training is in progress.

                        * ``Completed`` - The training job has completed.

                        * ``Failed`` - The training job has failed. To see the reason for the
                        failure, see the ``FailureReason`` field in the response to a
                        ``DescribeTrainingJobResponse`` call.

                        * ``Stopping`` - The training job is stopping.

                        * ``Stopped`` - The training job has stopped.

                        For more detailed information, see ``SecondaryStatus`` .

                      - **SecondaryStatus** *(string) --*

                        Provides detailed information about the state of the training job. For
                        detailed information about the secondary status of the training job, see
                        ``StatusMessage`` under  SecondaryStatusTransition .

                        Amazon SageMaker provides primary statuses and secondary statuses that apply
                        to each of them:

                          InProgress

                        * ``Starting`` - Starting the training job.

                        * ``Downloading`` - An optional stage for algorithms that support ``File``
                        training input mode. It indicates that data is being downloaded to the ML
                        storage volumes.

                        * ``Training`` - Training is in progress.

                        * ``Uploading`` - Training is complete and the model artifacts are being
                        uploaded to the S3 location.

                          Completed

                        * ``Completed`` - The training job has completed.

                          Failed

                        * ``Failed`` - The training job has failed. The reason for the failure is
                        returned in the ``FailureReason`` field of ``DescribeTrainingJobResponse`` .

                          Stopped

                        * ``MaxRuntimeExceeded`` - The job stopped because it exceeded the maximum
                        allowed runtime.

                        * ``Stopped`` - The training job has stopped.

                          Stopping

                        * ``Stopping`` - Stopping the training job.

                        .. warning::

                          Valid values for ``SecondaryStatus`` are subject to change.

                        We no longer support the following secondary statuses:

                        * ``LaunchingMLInstances``

                        * ``PreparingTrainingStack``

                        * ``DownloadingTrainingImage``

                      - **FailureReason** *(string) --*

                        If the training job failed, the reason it failed.

                      - **HyperParameters** *(dict) --*

                        Algorithm-specific parameters.

                        - *(string) --*

                          - *(string) --*

                      - **AlgorithmSpecification** *(dict) --*

                        Information about the algorithm used for training, and algorithm metadata.

                        - **TrainingImage** *(string) --*

                          The registry path of the Docker image that contains the training
                          algorithm. For information about docker registry paths for built-in
                          algorithms, see `Algorithms Provided by Amazon SageMaker\\: Common
                          Parameters
                          <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__
                          . Amazon SageMaker supports both ``registry/repository[:tag]`` and
                          ``registry/repository[@digest]`` image path formats. For more information,
                          see `Using Your Own Algorithms with Amazon SageMaker
                          <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__
                          .

                        - **AlgorithmName** *(string) --*

                          The name of the algorithm resource to use for the training job. This must
                          be an algorithm resource that you created or subscribe to on AWS
                          Marketplace. If you specify a value for this parameter, you can't specify
                          a value for ``TrainingImage`` .

                        - **TrainingInputMode** *(string) --*

                          The input mode that the algorithm supports. For the input modes that
                          Amazon SageMaker algorithms support, see `Algorithms
                          <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an
                          algorithm supports the ``File`` input mode, Amazon SageMaker downloads the
                          training data from S3 to the provisioned ML storage Volume, and mounts the
                          directory to docker volume for training container. If an algorithm
                          supports the ``Pipe`` input mode, Amazon SageMaker streams data directly
                          from S3 to the container.

                          In File mode, make sure you provision ML storage volume with sufficient
                          capacity to accommodate the data download from S3. In addition to the
                          training data, the ML storage volume also stores the output model. The
                          algorithm container use ML storage volume to also store intermediate
                          information, if any.

                          For distributed algorithms using File mode, training data is distributed
                          uniformly, and your training duration is predictable if the input data
                          objects size is approximately same. Amazon SageMaker does not split the
                          files any further for model training. If the object sizes are skewed,
                          training won't be optimal as the data distribution is also skewed where
                          one host in a training cluster is overloaded, thus becoming bottleneck in
                          training.

                        - **MetricDefinitions** *(list) --*

                          A list of metric definition objects. Each object specifies the metric name
                          and regular expressions used to parse algorithm logs. Amazon SageMaker
                          publishes each metric to Amazon CloudWatch.

                          - *(dict) --*

                            Specifies a metric that the training algorithm writes to ``stderr`` or
                            ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined
                            metrics. You specify one metric that a hyperparameter tuning job uses as
                            its objective metric to choose the best training job.

                            - **Name** *(string) --*

                              The name of the metric.

                            - **Regex** *(string) --*

                              A regular expression that searches the output of a training job and
                              gets the value of the metric. For more information about using regular
                              expressions to define metrics, see `Defining Objective Metrics
                              <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__
                              .

                        - **EnableSageMakerMetricsTimeSeries** *(boolean) --*

                          To generate and save time-series metrics during training, set to ``true``
                          . The default is ``false`` and time-series metrics aren't generated except
                          in the following cases:

                          * You use one of the Amazon SageMaker built-in algorithms

                          * You use one of the following prebuilt Amazon SageMaker Docker images:

                            * Tensorflow

                            * MXNet

                            * PyTorch

                          * You specify at least one  MetricDefinition

                      - **RoleArn** *(string) --*

                        The AWS Identity and Access Management (IAM) role configured for the
                        training job.

                      - **InputDataConfig** *(list) --*

                        An array of ``Channel`` objects that describes each data input channel.

                        - *(dict) --*

                          A channel is a named input source that training algorithms can consume.

                          - **ChannelName** *(string) --*

                            The name of the channel.

                          - **DataSource** *(dict) --*

                            The location of the channel data.

                            - **S3DataSource** *(dict) --*

                              The S3 location of the data source that is associated with a channel.

                              - **S3DataType** *(string) --*

                                If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix.
                                Amazon SageMaker uses all objects that match the specified key name
                                prefix for model training.

                                If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that
                                is a manifest file containing a list of object keys that you want
                                Amazon SageMaker to use for model training.

                                If you choose ``AugmentedManifestFile`` , S3Uri identifies an object
                                that is an augmented manifest file in JSON lines format. This file
                                contains the data you want to use for model training.
                                ``AugmentedManifestFile`` can only be used if the Channel's input
                                mode is ``Pipe`` .

                              - **S3Uri** *(string) --*

                                Depending on the value specified for the ``S3DataType`` , identifies
                                either a key name prefix or a manifest. For example:

                                * A key name prefix might look like this:
                                ``s3://bucketname/exampleprefix`` .

                                * A manifest might look like this:
                                ``s3://bucketname/example.manifest``   The manifest is an S3 object
                                which is a JSON file with the following format:  The preceding JSON
                                matches the following ``s3Uris`` :   ``[ {"prefix":
                                "s3://customer_bucket/some/prefix/"},``
                                ``"relative/path/to/custdata-1",``
                                ``"relative/path/custdata-2",``    ``...``
                                ``"relative/path/custdata-N"``    ``]``   The preceding JSON matches
                                the following ``s3Uris`` :
                                ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``
                                ``s3://customer_bucket/some/prefix/relative/path/custdata-2``
                                ``...``
                                ``s3://customer_bucket/some/prefix/relative/path/custdata-N``   The
                                complete set of ``s3uris`` in this manifest is the input data for
                                the channel for this datasource. The object that each ``s3uris``
                                points to must be readable by the IAM role that Amazon SageMaker
                                uses to perform tasks on your behalf.

                              - **S3DataDistributionType** *(string) --*

                                If you want Amazon SageMaker to replicate the entire dataset on each
                                ML compute instance that is launched for model training, specify
                                ``FullyReplicated`` .

                                If you want Amazon SageMaker to replicate a subset of data on each
                                ML compute instance that is launched for model training, specify
                                ``ShardedByS3Key`` . If there are *n* ML compute instances launched
                                for a training job, each instance gets approximately 1/*n* of the
                                number of S3 objects. In this case, model training on each machine
                                uses only the subset of training data.

                                Don't choose more ML compute instances for training than available
                                S3 objects. If you do, some nodes won't get any data and you will
                                pay for nodes that aren't getting any training data. This applies in
                                both File and Pipe modes. Keep this in mind when developing
                                algorithms.

                                In distributed training, where you use multiple ML compute EC2
                                instances, you might choose ``ShardedByS3Key`` . If the algorithm
                                requires copying training data to the ML storage volume (when
                                ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the
                                number of objects.

                              - **AttributeNames** *(list) --*

                                A list of one or more attribute names to use that are found in a
                                specified augmented manifest file.

                                - *(string) --*

                            - **FileSystemDataSource** *(dict) --*

                              The file system that is associated with a channel.

                              - **FileSystemId** *(string) --*

                                The file system id.

                              - **FileSystemAccessMode** *(string) --*

                                The access mode of the mount of the directory associated with the
                                channel. A directory can be mounted either in ``ro`` (read-only) or
                                ``rw`` (read-write) mode.

                              - **FileSystemType** *(string) --*

                                The file system type.

                              - **DirectoryPath** *(string) --*

                                The full path to the directory to associate with the channel.

                          - **ContentType** *(string) --*

                            The MIME type of the data.

                          - **CompressionType** *(string) --*

                            If training data is compressed, the compression type. The default value
                            is ``None`` . ``CompressionType`` is used only in Pipe input mode. In
                            File mode, leave this field unset or set it to None.

                          - **RecordWrapperType** *(string) --*

                            Specify RecordIO as the value when input data is in raw format but the
                            training algorithm requires the RecordIO format. In this case, Amazon
                            SageMaker wraps each individual S3 object in a RecordIO record. If the
                            input data is already in RecordIO format, you don't need to set this
                            attribute. For more information, see `Create a Dataset Using RecordIO
                            <https://mxnet.apache.org/api/architecture/note_data_loading#data-format>`__
                            .

                            In File mode, leave this field unset or set it to None.

                          - **InputMode** *(string) --*

                            (Optional) The input mode to use for the data channel in a training job.
                            If you don't set a value for ``InputMode`` , Amazon SageMaker uses the
                            value set for ``TrainingInputMode`` . Use this parameter to override the
                            ``TrainingInputMode`` setting in a  AlgorithmSpecification request when
                            you have a channel that needs a different input mode from the training
                            job's general setting. To download the data from Amazon Simple Storage
                            Service (Amazon S3) to the provisioned ML storage volume, and mount the
                            directory to a Docker volume, use ``File`` input mode. To stream data
                            directly from Amazon S3 to the container, choose ``Pipe`` input mode.

                            To use a model for incremental training, choose ``File`` input model.

                          - **ShuffleConfig** *(dict) --*

                            A configuration for a shuffle option for input data in a channel. If you
                            use ``S3Prefix`` for ``S3DataType`` , this shuffles the results of the
                            S3 key prefix matches. If you use ``ManifestFile`` , the order of the S3
                            object references in the ``ManifestFile`` is shuffled. If you use
                            ``AugmentedManifestFile`` , the order of the JSON lines in the
                            ``AugmentedManifestFile`` is shuffled. The shuffling order is determined
                            using the ``Seed`` value.

                            For Pipe input mode, shuffling is done at the start of every epoch. With
                            large datasets this ensures that the order of the training data is
                            different for each epoch, it helps reduce bias and possible overfitting.
                            In a multi-node training job when ShuffleConfig is combined with
                            ``S3DataDistributionType`` of ``ShardedByS3Key`` , the data is shuffled
                            across nodes so that the content sent to a particular node on the first
                            epoch might be sent to a different node on the second epoch.

                            - **Seed** *(integer) --*

                              Determines the shuffling order in ``ShuffleConfig`` value.

                      - **OutputDataConfig** *(dict) --*

                        The S3 path where model artifacts that you configured when creating the job
                        are stored. Amazon SageMaker creates subfolders for model artifacts.

                        - **KmsKeyId** *(string) --*

                          The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to
                          encrypt the model artifacts at rest using Amazon S3 server-side
                          encryption. The ``KmsKeyId`` can be any of the following formats:

                          * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                          * // Amazon Resource Name (ARN) of a KMS Key
                          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                          * // KMS Key Alias  ``"alias/ExampleAlias"``

                          * // Amazon Resource Name (ARN) of a KMS Key Alias
                          ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                          If you use a KMS key ID or an alias of your master key, the Amazon
                          SageMaker execution role must include permissions to call ``kms:Encrypt``
                          . If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS
                          key for Amazon S3 for your role's account. Amazon SageMaker uses
                          server-side encryption with KMS-managed keys for ``OutputDataConfig`` . If
                          you use a bucket policy with an ``s3:PutObject`` permission that only
                          allows objects with server-side encryption, set the condition key of
                          ``s3:x-amz-server-side-encryption`` to ``"aws:kms"`` . For more
                          information, see `KMS-Managed Encryption Keys
                          <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__
                          in the *Amazon Simple Storage Service Developer Guide.*

                          The KMS key policy must grant permission to the IAM role that you specify
                          in your ``CreateTrainingJob`` , ``CreateTransformJob`` , or
                          ``CreateHyperParameterTuningJob`` requests. For more information, see
                          `Using Key Policies in AWS KMS
                          <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__
                          in the *AWS Key Management Service Developer Guide* .

                        - **S3OutputPath** *(string) --*

                          Identifies the S3 path where you want Amazon SageMaker to store the model
                          artifacts. For example, ``s3://bucket-name/key-name-prefix`` .

                      - **ResourceConfig** *(dict) --*

                        Resources, including ML compute instances and ML storage volumes, that are
                        configured for model training.

                        - **InstanceType** *(string) --*

                          The ML compute instance type.

                        - **InstanceCount** *(integer) --*

                          The number of ML compute instances to use. For distributed training,
                          provide a value greater than 1.

                        - **VolumeSizeInGB** *(integer) --*

                          The size of the ML storage volume that you want to provision.

                          ML storage volumes store model artifacts and incremental states. Training
                          algorithms might also use the ML storage volume for scratch space. If you
                          want to store the training data in the ML storage volume, choose ``File``
                          as the ``TrainingInputMode`` in the algorithm specification.

                          You must specify sufficient ML storage for your scenario.

                          .. note::

                            Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage
                            volume type.

                          .. note::

                            Certain Nitro-based instances include local storage with a fixed total
                            size, dependent on the instance type. When using these instances for
                            training, Amazon SageMaker mounts the local instance storage instead of
                            Amazon EBS gp2 storage. You can't request a ``VolumeSizeInGB`` greater
                            than the total size of the local instance storage.

                            For a list of instance types that support local instance storage,
                            including the total size per instance type, see `Instance Store Volumes
                            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes>`__
                            .

                        - **VolumeKmsKeyId** *(string) --*

                          The AWS KMS key that Amazon SageMaker uses to encrypt data on the storage
                          volume attached to the ML compute instance(s) that run the training job.

                          .. note::

                            Certain Nitro-based instances include local storage, dependent on the
                            instance type. Local storage volumes are encrypted using a hardware
                            module on the instance. You can't request a ``VolumeKmsKeyId`` when
                            using an instance type with local storage.

                            For a list of instance types that support local instance storage, see
                            `Instance Store Volumes
                            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes>`__
                            .

                            For more information about local instance storage encryption, see `SSD
                            Instance Store Volumes
                            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html>`__
                            .

                          The ``VolumeKmsKeyId`` can be in any of the following formats:

                          * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                          * // Amazon Resource Name (ARN) of a KMS Key
                          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                      - **VpcConfig** *(dict) --*

                        A  VpcConfig object that specifies the VPC that this training job has access
                        to. For more information, see `Protect Training Jobs by Using an Amazon
                        Virtual Private Cloud
                        <https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .

                        - **SecurityGroupIds** *(list) --*

                          The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security
                          groups for the VPC that is specified in the ``Subnets`` field.

                          - *(string) --*

                        - **Subnets** *(list) --*

                          The ID of the subnets in the VPC to which you want to connect your
                          training job or model.

                          .. note::

                            Amazon EC2 P3 accelerated computing instances are not available in the
                            c/d/e availability zones of region us-east-1. If you want to create
                            endpoints with P3 instances in VPC mode in region us-east-1, create
                            subnets in a/b/f availability zones instead.

                          - *(string) --*

                      - **StoppingCondition** *(dict) --*

                        Specifies a limit to how long a model training job can run. When the job
                        reaches the time limit, Amazon SageMaker ends the training job. Use this API
                        to cap model training costs.

                        To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal,
                        which delays job termination for 120 seconds. Algorithms can use this
                        120-second window to save the model artifacts, so the results of training
                        are not lost.

                        - **MaxRuntimeInSeconds** *(integer) --*

                          The maximum length of time, in seconds, that the training or compilation
                          job can run. If job does not complete during this time, Amazon SageMaker
                          ends the job. If value is not specified, default value is 1 day. The
                          maximum value is 28 days.

                        - **MaxWaitTimeInSeconds** *(integer) --*

                          The maximum length of time, in seconds, how long you are willing to wait
                          for a managed spot training job to complete. It is the amount of time
                          spent waiting for Spot capacity plus the amount of time the training job
                          runs. It must be equal to or greater than ``MaxRuntimeInSeconds`` .

                      - **CreationTime** *(datetime) --*

                        A timestamp that indicates when the training job was created.

                      - **TrainingStartTime** *(datetime) --*

                        Indicates the time when the training job starts on training instances. You
                        are billed for the time interval between this time and the value of
                        ``TrainingEndTime`` . The start time in CloudWatch Logs might be later than
                        this time. The difference is due to the time it takes to download the
                        training data and to the size of the training container.

                      - **TrainingEndTime** *(datetime) --*

                        Indicates the time when the training job ends on training instances. You are
                        billed for the time interval between the value of ``TrainingStartTime`` and
                        this time. For successful jobs and stopped jobs, this is the time after
                        model artifacts are uploaded. For failed jobs, this is the time when Amazon
                        SageMaker detects a job failure.

                      - **LastModifiedTime** *(datetime) --*

                        A timestamp that indicates when the status of the training job was last
                        modified.

                      - **SecondaryStatusTransitions** *(list) --*

                        A history of all of the secondary statuses that the training job has
                        transitioned through.

                        - *(dict) --*

                          An array element of
                          DescribeTrainingJobResponse$SecondaryStatusTransitions . It provides
                          additional details about a status that the training job has transitioned
                          through. A training job can be in one of several states, for example,
                          starting, downloading, training, or uploading. Within each state, there
                          are a number of intermediate states. For example, within the starting
                          state, Amazon SageMaker could be starting the training job or launching
                          the ML instances. These transitional states are referred to as the job's
                          secondary status.

                          - **Status** *(string) --*

                            Contains a secondary status information from a training job.

                            Status might be one of the following secondary statuses:

                              InProgress

                            * ``Starting`` - Starting the training job.

                            * ``Downloading`` - An optional stage for algorithms that support
                            ``File`` training input mode. It indicates that data is being downloaded
                            to the ML storage volumes.

                            * ``Training`` - Training is in progress.

                            * ``Uploading`` - Training is complete and the model artifacts are being
                            uploaded to the S3 location.

                              Completed

                            * ``Completed`` - The training job has completed.

                              Failed

                            * ``Failed`` - The training job has failed. The reason for the failure
                            is returned in the ``FailureReason`` field of
                            ``DescribeTrainingJobResponse`` .

                              Stopped

                            * ``MaxRuntimeExceeded`` - The job stopped because it exceeded the
                            maximum allowed runtime.

                            * ``Stopped`` - The training job has stopped.

                              Stopping

                            * ``Stopping`` - Stopping the training job.

                            We no longer support the following secondary statuses:

                            * ``LaunchingMLInstances``

                            * ``PreparingTrainingStack``

                            * ``DownloadingTrainingImage``

                          - **StartTime** *(datetime) --*

                            A timestamp that shows when the training job transitioned to the current
                            secondary status state.

                          - **EndTime** *(datetime) --*

                            A timestamp that shows when the training job transitioned out of this
                            secondary status state into another secondary status state or when the
                            training job has ended.

                          - **StatusMessage** *(string) --*

                            A detailed description of the progress within a secondary status.

                            Amazon SageMaker provides secondary statuses and status messages that
                            apply to each of them:

                              Starting

                            * Starting the training job.

                            * Launching requested ML instances.

                            * Insufficient capacity error from EC2 while launching instances,
                            retrying!

                            * Launched instance was unhealthy, replacing it!

                            * Preparing the instances for training.

                              Training

                            * Downloading the training image.

                            * Training image download completed. Training in progress.

                            .. warning::

                              Status messages are subject to change. Therefore, we recommend not
                              including them in code that programmatically initiates actions. For
                              examples, don't use status messages in if statements.

                            To have an overview of your training job's progress, view
                            ``TrainingJobStatus`` and ``SecondaryStatus`` in  DescribeTrainingJob ,
                            and ``StatusMessage`` together. For example, at the start of a training
                            job, you might see the following:

                            * ``TrainingJobStatus`` - InProgress

                            * ``SecondaryStatus`` - Training

                            * ``StatusMessage`` - Downloading the training image

                      - **FinalMetricDataList** *(list) --*

                        A list of final metric values that are set when the training job completes.
                        Used only if the training job was configured to use metrics.

                        - *(dict) --*

                          The name, value, and date and time of a metric that was emitted to Amazon
                          CloudWatch.

                          - **MetricName** *(string) --*

                            The name of the metric.

                          - **Value** *(float) --*

                            The value of the metric.

                          - **Timestamp** *(datetime) --*

                            The date and time that the algorithm emitted the metric.

                      - **EnableNetworkIsolation** *(boolean) --*

                        If the ``TrainingJob`` was created with network isolation, the value is set
                        to ``true`` . If network isolation is enabled, nodes can't communicate
                        beyond the VPC they run in.

                      - **EnableInterContainerTrafficEncryption** *(boolean) --*

                        To encrypt all communications between ML compute instances in distributed
                        training, choose ``True`` . Encryption provides greater security for
                        distributed training, but training might take longer. How long it takes
                        depends on the amount of communication between compute instances, especially
                        if you use a deep learning algorithm in distributed training.

                      - **EnableManagedSpotTraining** *(boolean) --*

                        When true, enables managed spot training using Amazon EC2 Spot instances to
                        run training jobs instead of on-demand instances. For more information, see
                        model-managed-spot-training .

                      - **CheckpointConfig** *(dict) --*

                        Contains information about the output location for managed spot training
                        checkpoint data.

                        - **S3Uri** *(string) --*

                          Identifies the S3 path where you want Amazon SageMaker to store
                          checkpoints. For example, ``s3://bucket-name/key-name-prefix`` .

                        - **LocalPath** *(string) --*

                          (Optional) The local directory where checkpoints are written. The default
                          directory is ``/opt/ml/checkpoints/`` .

                      - **TrainingTimeInSeconds** *(integer) --*

                        The training time in seconds.

                      - **BillableTimeInSeconds** *(integer) --*

                        The billable time in seconds.

                      - **DebugHookConfig** *(dict) --*

                        Configuration information for the debug hook parameters, collection
                        configuration, and storage paths.

                        - **LocalPath** *(string) --*

                          Path to local storage location for tensors. Defaults to
                          ``/opt/ml/output/tensors/`` .

                        - **S3OutputPath** *(string) --*

                          Path to Amazon S3 storage location for tensors.

                        - **HookParameters** *(dict) --*

                          Configuration information for the debug hook parameters.

                          - *(string) --*

                            - *(string) --*

                        - **CollectionConfigurations** *(list) --*

                          Configuration information for tensor collections.

                          - *(dict) --*

                            Configuration information for tensor collections.

                            - **CollectionName** *(string) --*

                              The name of the tensor collection.

                            - **CollectionParameters** *(dict) --*

                              Parameter values for the tensor collection. The allowed parameters are
                              ``"name"`` , ``"include_regex"`` , ``"reduction_config"`` ,
                              ``"save_config"`` , ``"tensor_names"`` , and ``"save_histogram"`` .

                              - *(string) --*

                                - *(string) --*

                      - **ExperimentConfig** *(dict) --*

                        Configuration for the experiment.

                        - **ExperimentName** *(string) --*

                          The name of the experiment.

                        - **TrialName** *(string) --*

                          The name of the trial.

                        - **TrialComponentDisplayName** *(string) --*

                          Display name for the trial component.

                      - **DebugRuleConfigurations** *(list) --*

                        Information about the debug rule configuration.

                        - *(dict) --*

                          Configuration information for debugging rules.

                          - **RuleConfigurationName** *(string) --*

                            The name of the rule configuration. It must be unique relative to other
                            rule configuration names.

                          - **LocalPath** *(string) --*

                            Path to local storage location for rules. Defaults to
                            ``/opt/ml/processing/output/rule/`` .

                          - **S3OutputPath** *(string) --*

                            Path to Amazon S3 storage location for rules.

                          - **RuleEvaluatorImage** *(string) --*

                            The Amazon Elastic Container (ECR) Image for the managed rule
                            evaluation.

                          - **InstanceType** *(string) --*

                            The instance type to deploy for a training job.

                          - **VolumeSizeInGB** *(integer) --*

                            The size, in GB, of the ML storage volume attached to the notebook
                            instance.

                          - **RuleParameters** *(dict) --*

                            Runtime configuration for rule container.

                            - *(string) --*

                              - *(string) --*

                      - **TensorBoardOutputConfig** *(dict) --*

                        Configuration of storage locations for TensorBoard output.

                        - **LocalPath** *(string) --*

                          Path to local storage location for tensorBoard output. Defaults to
                          ``/opt/ml/output/tensorboard`` .

                        - **S3OutputPath** *(string) --*

                          Path to Amazon S3 storage location for TensorBoard output.

                      - **DebugRuleEvaluationStatuses** *(list) --*

                        Information about the evaluation status of the rules for the training job.

                        - *(dict) --*

                          Information about the status of the rule evaluation.

                          - **RuleConfigurationName** *(string) --*

                            The name of the rule configuration

                          - **RuleEvaluationJobArn** *(string) --*

                            The Amazon Resource Name (ARN) of the rule evaluation job.

                          - **RuleEvaluationStatus** *(string) --*

                            Status of the rule evaluation.

                          - **StatusDetails** *(string) --*

                            Details from the rule evaluation.

                          - **LastModifiedTime** *(datetime) --*

                            Timestamp when the rule evaluation status was last modified.

                      - **Tags** *(list) --*

                        An array of key-value pairs. For more information, see `Using Cost
                        Allocation Tags
                        <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__
                        in the *AWS Billing and Cost Management User Guide* .

                        - *(dict) --*

                          Describes a tag.

                          - **Key** *(string) --*

                            The tag key.

                          - **Value** *(string) --*

                            The tag value.

                  - **Tags** *(list) --*

                    The list of tags that are associated with the component. You can use  Search API
                    to search on the tags.

                    - *(dict) --*

                      Describes a tag.

                      - **Key** *(string) --*

                        The tag key.

                      - **Value** *(string) --*

                        The tag value.

                  - **Parents** *(list) --*

                    An array of the parents of the component. A parent is a trial the component is
                    associated with and the experiment the trial is part of. A component might not
                    have any parents.

                    - *(dict) --*

                      The trial that a trial component is associated with and the experiment the
                      trial is part of. A component might not be associated with a trial. A
                      component can be associated with multiple trials.

                      - **TrialName** *(string) --*

                        The name of the trial.

                      - **ExperimentName** *(string) --*

                        The name of the experiment.
        """
