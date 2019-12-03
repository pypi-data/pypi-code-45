"Main interface for sagemaker service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddTagsResponseTagsTypeDef",
    "ClientAddTagsResponseTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCreateAlgorithmInferenceSpecificationContainersTypeDef",
    "ClientCreateAlgorithmInferenceSpecificationTypeDef",
    "ClientCreateAlgorithmResponseTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef",
    "ClientCreateAlgorithmValidationSpecificationTypeDef",
    "ClientCreateCodeRepositoryGitConfigTypeDef",
    "ClientCreateCodeRepositoryResponseTypeDef",
    "ClientCreateCompilationJobInputConfigTypeDef",
    "ClientCreateCompilationJobOutputConfigTypeDef",
    "ClientCreateCompilationJobResponseTypeDef",
    "ClientCreateCompilationJobStoppingConditionTypeDef",
    "ClientCreateEndpointConfigProductionVariantsTypeDef",
    "ClientCreateEndpointConfigResponseTypeDef",
    "ClientCreateEndpointConfigTagsTypeDef",
    "ClientCreateEndpointResponseTypeDef",
    "ClientCreateEndpointTagsTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef",
    "ClientCreateHyperParameterTuningJobResponseTypeDef",
    "ClientCreateHyperParameterTuningJobTagsTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef",
    "ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef",
    "ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigTypeDef",
    "ClientCreateLabelingJobInputConfigDataAttributesTypeDef",
    "ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateLabelingJobInputConfigDataSourceTypeDef",
    "ClientCreateLabelingJobInputConfigTypeDef",
    "ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef",
    "ClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef",
    "ClientCreateLabelingJobOutputConfigTypeDef",
    "ClientCreateLabelingJobResponseTypeDef",
    "ClientCreateLabelingJobStoppingConditionsTypeDef",
    "ClientCreateLabelingJobTagsTypeDef",
    "ClientCreateModelContainersTypeDef",
    "ClientCreateModelPackageInferenceSpecificationContainersTypeDef",
    "ClientCreateModelPackageInferenceSpecificationTypeDef",
    "ClientCreateModelPackageResponseTypeDef",
    "ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef",
    "ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef",
    "ClientCreateModelPackageValidationSpecificationTypeDef",
    "ClientCreateModelPrimaryContainerTypeDef",
    "ClientCreateModelResponseTypeDef",
    "ClientCreateModelTagsTypeDef",
    "ClientCreateModelVpcConfigTypeDef",
    "ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef",
    "ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef",
    "ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef",
    "ClientCreateNotebookInstanceResponseTypeDef",
    "ClientCreateNotebookInstanceTagsTypeDef",
    "ClientCreatePresignedNotebookInstanceUrlResponseTypeDef",
    "ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientCreateTrainingJobAlgorithmSpecificationTypeDef",
    "ClientCreateTrainingJobCheckpointConfigTypeDef",
    "ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateTrainingJobInputDataConfigDataSourceTypeDef",
    "ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef",
    "ClientCreateTrainingJobInputDataConfigTypeDef",
    "ClientCreateTrainingJobOutputDataConfigTypeDef",
    "ClientCreateTrainingJobResourceConfigTypeDef",
    "ClientCreateTrainingJobResponseTypeDef",
    "ClientCreateTrainingJobStoppingConditionTypeDef",
    "ClientCreateTrainingJobTagsTypeDef",
    "ClientCreateTrainingJobVpcConfigTypeDef",
    "ClientCreateTransformJobDataProcessingTypeDef",
    "ClientCreateTransformJobResponseTypeDef",
    "ClientCreateTransformJobTagsTypeDef",
    "ClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef",
    "ClientCreateTransformJobTransformInputDataSourceTypeDef",
    "ClientCreateTransformJobTransformInputTypeDef",
    "ClientCreateTransformJobTransformOutputTypeDef",
    "ClientCreateTransformJobTransformResourcesTypeDef",
    "ClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientCreateWorkteamMemberDefinitionsTypeDef",
    "ClientCreateWorkteamNotificationConfigurationTypeDef",
    "ClientCreateWorkteamResponseTypeDef",
    "ClientCreateWorkteamTagsTypeDef",
    "ClientDeleteWorkteamResponseTypeDef",
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef",
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef",
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef",
    "ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef",
    "ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTypeDef",
    "ClientDescribeCodeRepositoryResponseGitConfigTypeDef",
    "ClientDescribeCodeRepositoryResponseTypeDef",
    "ClientDescribeCompilationJobResponseInputConfigTypeDef",
    "ClientDescribeCompilationJobResponseModelArtifactsTypeDef",
    "ClientDescribeCompilationJobResponseOutputConfigTypeDef",
    "ClientDescribeCompilationJobResponseStoppingConditionTypeDef",
    "ClientDescribeCompilationJobResponseTypeDef",
    "ClientDescribeEndpointConfigResponseProductionVariantsTypeDef",
    "ClientDescribeEndpointConfigResponseTypeDef",
    "ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef",
    "ClientDescribeEndpointResponseProductionVariantsTypeDef",
    "ClientDescribeEndpointResponseTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef",
    "ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef",
    "ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef",
    "ClientDescribeLabelingJobResponseInputConfigTypeDef",
    "ClientDescribeLabelingJobResponseLabelCountersTypeDef",
    "ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef",
    "ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef",
    "ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef",
    "ClientDescribeLabelingJobResponseOutputConfigTypeDef",
    "ClientDescribeLabelingJobResponseStoppingConditionsTypeDef",
    "ClientDescribeLabelingJobResponseTagsTypeDef",
    "ClientDescribeLabelingJobResponseTypeDef",
    "ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef",
    "ClientDescribeModelPackageResponseInferenceSpecificationTypeDef",
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef",
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef",
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef",
    "ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef",
    "ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationTypeDef",
    "ClientDescribeModelPackageResponseTypeDef",
    "ClientDescribeModelResponseContainersTypeDef",
    "ClientDescribeModelResponsePrimaryContainerTypeDef",
    "ClientDescribeModelResponseVpcConfigTypeDef",
    "ClientDescribeModelResponseTypeDef",
    "ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef",
    "ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef",
    "ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef",
    "ClientDescribeNotebookInstanceResponseTypeDef",
    "ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef",
    "ClientDescribeSubscribedWorkteamResponseTypeDef",
    "ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef",
    "ClientDescribeTrainingJobResponseCheckpointConfigTypeDef",
    "ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigTypeDef",
    "ClientDescribeTrainingJobResponseModelArtifactsTypeDef",
    "ClientDescribeTrainingJobResponseOutputDataConfigTypeDef",
    "ClientDescribeTrainingJobResponseResourceConfigTypeDef",
    "ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef",
    "ClientDescribeTrainingJobResponseStoppingConditionTypeDef",
    "ClientDescribeTrainingJobResponseVpcConfigTypeDef",
    "ClientDescribeTrainingJobResponseTypeDef",
    "ClientDescribeTransformJobResponseDataProcessingTypeDef",
    "ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef",
    "ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef",
    "ClientDescribeTransformJobResponseTransformInputTypeDef",
    "ClientDescribeTransformJobResponseTransformOutputTypeDef",
    "ClientDescribeTransformJobResponseTransformResourcesTypeDef",
    "ClientDescribeTransformJobResponseTypeDef",
    "ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef",
    "ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef",
    "ClientDescribeWorkteamResponseWorkteamTypeDef",
    "ClientDescribeWorkteamResponseTypeDef",
    "ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef",
    "ClientGetSearchSuggestionsResponseTypeDef",
    "ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef",
    "ClientGetSearchSuggestionsSuggestionQueryTypeDef",
    "ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef",
    "ClientListAlgorithmsResponseTypeDef",
    "ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef",
    "ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef",
    "ClientListCodeRepositoriesResponseTypeDef",
    "ClientListCompilationJobsResponseCompilationJobSummariesTypeDef",
    "ClientListCompilationJobsResponseTypeDef",
    "ClientListEndpointConfigsResponseEndpointConfigsTypeDef",
    "ClientListEndpointConfigsResponseTypeDef",
    "ClientListEndpointsResponseEndpointsTypeDef",
    "ClientListEndpointsResponseTypeDef",
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef",
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef",
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef",
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef",
    "ClientListHyperParameterTuningJobsResponseTypeDef",
    "ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef",
    "ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef",
    "ClientListLabelingJobsForWorkteamResponseTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef",
    "ClientListLabelingJobsResponseTypeDef",
    "ClientListModelPackagesResponseModelPackageSummaryListTypeDef",
    "ClientListModelPackagesResponseTypeDef",
    "ClientListModelsResponseModelsTypeDef",
    "ClientListModelsResponseTypeDef",
    "ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef",
    "ClientListNotebookInstanceLifecycleConfigsResponseTypeDef",
    "ClientListNotebookInstancesResponseNotebookInstancesTypeDef",
    "ClientListNotebookInstancesResponseTypeDef",
    "ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef",
    "ClientListSubscribedWorkteamsResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef",
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    "ClientListTrainingJobsResponseTrainingJobSummariesTypeDef",
    "ClientListTrainingJobsResponseTypeDef",
    "ClientListTransformJobsResponseTransformJobSummariesTypeDef",
    "ClientListTransformJobsResponseTypeDef",
    "ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef",
    "ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef",
    "ClientListWorkteamsResponseWorkteamsTypeDef",
    "ClientListWorkteamsResponseTypeDef",
    "ClientRenderUiTemplateResponseErrorsTypeDef",
    "ClientRenderUiTemplateResponseTypeDef",
    "ClientRenderUiTemplateTaskTypeDef",
    "ClientRenderUiTemplateUiTemplateTypeDef",
    "ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef",
    "ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef",
    "ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobResourceConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef",
    "ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef",
    "ClientSearchResponseResultsTrainingJobTagsTypeDef",
    "ClientSearchResponseResultsTrainingJobVpcConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobTypeDef",
    "ClientSearchResponseResultsTypeDef",
    "ClientSearchResponseTypeDef",
    "ClientSearchSearchExpressionFiltersTypeDef",
    "ClientSearchSearchExpressionNestedFiltersFiltersTypeDef",
    "ClientSearchSearchExpressionNestedFiltersTypeDef",
    "ClientSearchSearchExpressionTypeDef",
    "ClientUpdateCodeRepositoryGitConfigTypeDef",
    "ClientUpdateCodeRepositoryResponseTypeDef",
    "ClientUpdateEndpointResponseTypeDef",
    "ClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef",
    "ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef",
    "ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef",
    "ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef",
    "ClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientUpdateWorkteamMemberDefinitionsTypeDef",
    "ClientUpdateWorkteamNotificationConfigurationTypeDef",
    "ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef",
    "ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef",
    "ClientUpdateWorkteamResponseWorkteamTypeDef",
    "ClientUpdateWorkteamResponseTypeDef",
    "EndpointDeletedWaitWaiterConfigTypeDef",
    "EndpointInServiceWaitWaiterConfigTypeDef",
    "ListAlgorithmsPaginatePaginationConfigTypeDef",
    "ListAlgorithmsPaginateResponseAlgorithmSummaryListTypeDef",
    "ListAlgorithmsPaginateResponseTypeDef",
    "ListCodeRepositoriesPaginatePaginationConfigTypeDef",
    "ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListGitConfigTypeDef",
    "ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListTypeDef",
    "ListCodeRepositoriesPaginateResponseTypeDef",
    "ListCompilationJobsPaginatePaginationConfigTypeDef",
    "ListCompilationJobsPaginateResponseCompilationJobSummariesTypeDef",
    "ListCompilationJobsPaginateResponseTypeDef",
    "ListEndpointConfigsPaginatePaginationConfigTypeDef",
    "ListEndpointConfigsPaginateResponseEndpointConfigsTypeDef",
    "ListEndpointConfigsPaginateResponseTypeDef",
    "ListEndpointsPaginatePaginationConfigTypeDef",
    "ListEndpointsPaginateResponseEndpointsTypeDef",
    "ListEndpointsPaginateResponseTypeDef",
    "ListHyperParameterTuningJobsPaginatePaginationConfigTypeDef",
    "ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef",
    "ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef",
    "ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef",
    "ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTypeDef",
    "ListHyperParameterTuningJobsPaginateResponseTypeDef",
    "ListLabelingJobsForWorkteamPaginatePaginationConfigTypeDef",
    "ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListLabelCountersTypeDef",
    "ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListTypeDef",
    "ListLabelingJobsForWorkteamPaginateResponseTypeDef",
    "ListLabelingJobsPaginatePaginationConfigTypeDef",
    "ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef",
    "ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef",
    "ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceTypeDef",
    "ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigTypeDef",
    "ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelCountersTypeDef",
    "ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelingJobOutputTypeDef",
    "ListLabelingJobsPaginateResponseLabelingJobSummaryListTypeDef",
    "ListLabelingJobsPaginateResponseTypeDef",
    "ListModelPackagesPaginatePaginationConfigTypeDef",
    "ListModelPackagesPaginateResponseModelPackageSummaryListTypeDef",
    "ListModelPackagesPaginateResponseTypeDef",
    "ListModelsPaginatePaginationConfigTypeDef",
    "ListModelsPaginateResponseModelsTypeDef",
    "ListModelsPaginateResponseTypeDef",
    "ListNotebookInstanceLifecycleConfigsPaginatePaginationConfigTypeDef",
    "ListNotebookInstanceLifecycleConfigsPaginateResponseNotebookInstanceLifecycleConfigsTypeDef",
    "ListNotebookInstanceLifecycleConfigsPaginateResponseTypeDef",
    "ListNotebookInstancesPaginatePaginationConfigTypeDef",
    "ListNotebookInstancesPaginateResponseNotebookInstancesTypeDef",
    "ListNotebookInstancesPaginateResponseTypeDef",
    "ListSubscribedWorkteamsPaginatePaginationConfigTypeDef",
    "ListSubscribedWorkteamsPaginateResponseSubscribedWorkteamsTypeDef",
    "ListSubscribedWorkteamsPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagsTypeDef",
    "ListTagsPaginateResponseTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobPaginatePaginationConfigTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobPaginateResponseTypeDef",
    "ListTrainingJobsPaginatePaginationConfigTypeDef",
    "ListTrainingJobsPaginateResponseTrainingJobSummariesTypeDef",
    "ListTrainingJobsPaginateResponseTypeDef",
    "ListTransformJobsPaginatePaginationConfigTypeDef",
    "ListTransformJobsPaginateResponseTransformJobSummariesTypeDef",
    "ListTransformJobsPaginateResponseTypeDef",
    "ListWorkteamsPaginatePaginationConfigTypeDef",
    "ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsTypeDef",
    "ListWorkteamsPaginateResponseWorkteamsNotificationConfigurationTypeDef",
    "ListWorkteamsPaginateResponseWorkteamsTypeDef",
    "ListWorkteamsPaginateResponseTypeDef",
    "NotebookInstanceDeletedWaitWaiterConfigTypeDef",
    "NotebookInstanceInServiceWaitWaiterConfigTypeDef",
    "NotebookInstanceStoppedWaitWaiterConfigTypeDef",
    "SearchPaginatePaginationConfigTypeDef",
    "SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    "SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationTypeDef",
    "SearchPaginateResponseResultsTrainingJobFinalMetricDataListTypeDef",
    "SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    "SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceTypeDef",
    "SearchPaginateResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef",
    "SearchPaginateResponseResultsTrainingJobInputDataConfigTypeDef",
    "SearchPaginateResponseResultsTrainingJobModelArtifactsTypeDef",
    "SearchPaginateResponseResultsTrainingJobOutputDataConfigTypeDef",
    "SearchPaginateResponseResultsTrainingJobResourceConfigTypeDef",
    "SearchPaginateResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef",
    "SearchPaginateResponseResultsTrainingJobStoppingConditionTypeDef",
    "SearchPaginateResponseResultsTrainingJobTagsTypeDef",
    "SearchPaginateResponseResultsTrainingJobVpcConfigTypeDef",
    "SearchPaginateResponseResultsTrainingJobTypeDef",
    "SearchPaginateResponseResultsTypeDef",
    "SearchPaginateResponseTypeDef",
    "SearchPaginateSearchExpressionFiltersTypeDef",
    "SearchPaginateSearchExpressionNestedFiltersFiltersTypeDef",
    "SearchPaginateSearchExpressionNestedFiltersTypeDef",
    "SearchPaginateSearchExpressionTypeDef",
    "TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef",
    "TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef",
)


_ClientAddTagsResponseTagsTypeDef = TypedDict(
    "_ClientAddTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsResponseTagsTypeDef(_ClientAddTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --*

        The tag key.
    """


_ClientAddTagsResponseTypeDef = TypedDict(
    "_ClientAddTagsResponseTypeDef", {"Tags": List[ClientAddTagsResponseTagsTypeDef]}, total=False
)


class ClientAddTagsResponseTypeDef(_ClientAddTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        A list of tags associated with the Amazon SageMaker resource.
        - *(dict) --*

          Describes a tag.
          - **Key** *(string) --*

            The tag key.
    """


_RequiredClientAddTagsTagsTypeDef = TypedDict("_RequiredClientAddTagsTagsTypeDef", {"Key": str})
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreateAlgorithmInferenceSpecificationContainersTypeDef = TypedDict(
    "_ClientCreateAlgorithmInferenceSpecificationContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)


class ClientCreateAlgorithmInferenceSpecificationContainersTypeDef(
    _ClientCreateAlgorithmInferenceSpecificationContainersTypeDef
):
    """
    - *(dict) --*

      Describes the Docker container for the model package.
      - **ContainerHostname** *(string) --*

        The DNS host name for the Docker container.
    """


_RequiredClientCreateAlgorithmInferenceSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateAlgorithmInferenceSpecificationTypeDef",
    {"Containers": List[ClientCreateAlgorithmInferenceSpecificationContainersTypeDef]},
)
_OptionalClientCreateAlgorithmInferenceSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateAlgorithmInferenceSpecificationTypeDef",
    {
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)


class ClientCreateAlgorithmInferenceSpecificationTypeDef(
    _RequiredClientCreateAlgorithmInferenceSpecificationTypeDef,
    _OptionalClientCreateAlgorithmInferenceSpecificationTypeDef,
):
    """
    Specifies details about inference jobs that the algorithm runs, including the following:
    * The Amazon ECR paths of containers that contain the inference code and model artifacts.
    * The instance types that the algorithm supports for transform jobs and real-time endpoints used
    for inference.
    * The input and output content formats that the algorithm supports for inference.
    - **Containers** *(list) --***[REQUIRED]**

      The Amazon ECR registry path of the Docker image that contains the inference code.
      - *(dict) --*

        Describes the Docker container for the model package.
        - **ContainerHostname** *(string) --*

          The DNS host name for the Docker container.
    """


_ClientCreateAlgorithmResponseTypeDef = TypedDict(
    "_ClientCreateAlgorithmResponseTypeDef", {"AlgorithmArn": str}, total=False
)


class ClientCreateAlgorithmResponseTypeDef(_ClientCreateAlgorithmResponseTypeDef):
    """
    - *(dict) --*

      - **AlgorithmArn** *(string) --*

        The Amazon Resource Name (ARN) of the new algorithm.
    """


_ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef = TypedDict(
    "_ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef(
    _ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef
):
    pass


_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef(
    _ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef
):
    pass


_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef(
    _ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef
):
    pass


_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef = TypedDict(
    "_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef(
    _ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef
):
    pass


_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef = TypedDict(
    "_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef",
    {
        "IntegerParameterRangeSpecification": ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef,
        "ContinuousParameterRangeSpecification": ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef,
        "CategoricalParameterRangeSpecification": ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef,
    },
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef(
    _ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef
):
    pass


_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef = TypedDict(
    "_ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": Literal["Integer", "Continuous", "Categorical", "FreeText"],
        "Range": ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef,
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef(
    _ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef
):
    pass


_ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef = TypedDict(
    "_ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef(
    _ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef
):
    pass


_ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef = TypedDict(
    "_ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef",
    {
        "Name": str,
        "Description": str,
        "IsRequired": bool,
        "SupportedContentTypes": List[str],
        "SupportedCompressionTypes": List[Literal["None", "Gzip"]],
        "SupportedInputModes": List[Literal["Pipe", "File"]],
    },
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef(
    _ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef
):
    pass


_RequiredClientCreateAlgorithmTrainingSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateAlgorithmTrainingSpecificationTypeDef", {"TrainingImage": str}
)
_OptionalClientCreateAlgorithmTrainingSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateAlgorithmTrainingSpecificationTypeDef",
    {
        "TrainingImageDigest": str,
        "SupportedHyperParameters": List[
            ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef
        ],
        "SupportedTrainingInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.p3dn.24xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
            ]
        ],
        "SupportsDistributedTraining": bool,
        "MetricDefinitions": List[
            ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef
        ],
        "TrainingChannels": List[ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef],
        "SupportedTuningJobObjectiveMetrics": List[
            ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef
        ],
    },
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationTypeDef(
    _RequiredClientCreateAlgorithmTrainingSpecificationTypeDef,
    _OptionalClientCreateAlgorithmTrainingSpecificationTypeDef,
):
    """
    Specifies details about training jobs run by this algorithm, including the following:
    * The Amazon ECR path of the container and the version digest of the algorithm.
    * The hyperparameters that the algorithm supports.
    * The instance types that the algorithm supports for training.
    * Whether the algorithm supports distributed training.
    * The metrics that the algorithm emits to Amazon CloudWatch.
    * Which metrics that the algorithm emits can be used as the objective metric for hyperparameter
    tuning jobs.
    * The input channels that the algorithm supports for training data. For example, an algorithm
    might support ``train`` , ``validation`` , and ``test`` channels.
    - **TrainingImage** *(string) --***[REQUIRED]**

      The Amazon ECR registry path of the Docker image that contains the training algorithm.
    """


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": Literal["Pipe", "File"],
        "HyperParameters": Dict[str, str],
        "InputDataConfig": List[
            ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef
        ],
        "OutputDataConfig": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef,
        "ResourceConfig": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef,
        "StoppingCondition": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef,
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    {
        "DataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef,
        "TransformOutput": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef,
        "TransformResources": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef,
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef
):
    pass


_ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef = TypedDict(
    "_ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef,
        "TransformJobDefinition": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef,
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef(
    _ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef
):
    pass


_RequiredClientCreateAlgorithmValidationSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateAlgorithmValidationSpecificationTypeDef", {"ValidationRole": str}
)
_OptionalClientCreateAlgorithmValidationSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateAlgorithmValidationSpecificationTypeDef",
    {
        "ValidationProfiles": List[
            ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef
        ]
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationTypeDef(
    _RequiredClientCreateAlgorithmValidationSpecificationTypeDef,
    _OptionalClientCreateAlgorithmValidationSpecificationTypeDef,
):
    """
    Specifies configurations for one or more training jobs and that Amazon SageMaker runs to test
    the algorithm's training code and, optionally, one or more batch transform jobs that Amazon
    SageMaker runs to test the algorithm's inference code.
    - **ValidationRole** *(string) --***[REQUIRED]**

      The IAM roles that Amazon SageMaker uses to run the training jobs.
    """


_RequiredClientCreateCodeRepositoryGitConfigTypeDef = TypedDict(
    "_RequiredClientCreateCodeRepositoryGitConfigTypeDef", {"RepositoryUrl": str}
)
_OptionalClientCreateCodeRepositoryGitConfigTypeDef = TypedDict(
    "_OptionalClientCreateCodeRepositoryGitConfigTypeDef",
    {"Branch": str, "SecretArn": str},
    total=False,
)


class ClientCreateCodeRepositoryGitConfigTypeDef(
    _RequiredClientCreateCodeRepositoryGitConfigTypeDef,
    _OptionalClientCreateCodeRepositoryGitConfigTypeDef,
):
    """
    Specifies details about the repository, including the URL where the repository is located, the
    default branch, and credentials to use to access the repository.
    - **RepositoryUrl** *(string) --***[REQUIRED]**

      The URL where the Git repository is located.
    """


_ClientCreateCodeRepositoryResponseTypeDef = TypedDict(
    "_ClientCreateCodeRepositoryResponseTypeDef", {"CodeRepositoryArn": str}, total=False
)


class ClientCreateCodeRepositoryResponseTypeDef(_ClientCreateCodeRepositoryResponseTypeDef):
    """
    - *(dict) --*

      - **CodeRepositoryArn** *(string) --*

        The Amazon Resource Name (ARN) of the new repository.
    """


_RequiredClientCreateCompilationJobInputConfigTypeDef = TypedDict(
    "_RequiredClientCreateCompilationJobInputConfigTypeDef", {"S3Uri": str}
)
_OptionalClientCreateCompilationJobInputConfigTypeDef = TypedDict(
    "_OptionalClientCreateCompilationJobInputConfigTypeDef",
    {
        "DataInputConfig": str,
        "Framework": Literal["TENSORFLOW", "MXNET", "ONNX", "PYTORCH", "XGBOOST"],
    },
    total=False,
)


class ClientCreateCompilationJobInputConfigTypeDef(
    _RequiredClientCreateCompilationJobInputConfigTypeDef,
    _OptionalClientCreateCompilationJobInputConfigTypeDef,
):
    """
    Provides information about the location of input model artifacts, the name and shape of the
    expected data inputs, and the framework in which the model was trained.
    - **S3Uri** *(string) --***[REQUIRED]**

      The S3 path where the model artifacts, which result from model training, are stored. This path
      must point to a single gzip compressed tar archive (.tar.gz suffix).
    """


_RequiredClientCreateCompilationJobOutputConfigTypeDef = TypedDict(
    "_RequiredClientCreateCompilationJobOutputConfigTypeDef", {"S3OutputLocation": str}
)
_OptionalClientCreateCompilationJobOutputConfigTypeDef = TypedDict(
    "_OptionalClientCreateCompilationJobOutputConfigTypeDef",
    {
        "TargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "rasp3b",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
        ]
    },
    total=False,
)


class ClientCreateCompilationJobOutputConfigTypeDef(
    _RequiredClientCreateCompilationJobOutputConfigTypeDef,
    _OptionalClientCreateCompilationJobOutputConfigTypeDef,
):
    """
    Provides information about the output location for the compiled model and the target device the
    model runs on.
    - **S3OutputLocation** *(string) --***[REQUIRED]**

      Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For
      example, s3://bucket-name/key-name-prefix.
    """


_ClientCreateCompilationJobResponseTypeDef = TypedDict(
    "_ClientCreateCompilationJobResponseTypeDef", {"CompilationJobArn": str}, total=False
)


class ClientCreateCompilationJobResponseTypeDef(_ClientCreateCompilationJobResponseTypeDef):
    """
    - *(dict) --*

      - **CompilationJobArn** *(string) --*

        If the action is successful, the service sends back an HTTP 200 response. Amazon SageMaker
        returns the following data in JSON format:
        * ``CompilationJobArn`` : The Amazon Resource Name (ARN) of the compiled job.
    """


_ClientCreateCompilationJobStoppingConditionTypeDef = TypedDict(
    "_ClientCreateCompilationJobStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientCreateCompilationJobStoppingConditionTypeDef(
    _ClientCreateCompilationJobStoppingConditionTypeDef
):
    """
    Specifies a limit to how long a model compilation job can run. When the job reaches the time
    limit, Amazon SageMaker ends the compilation job. Use this API to cap model training costs.
    - **MaxRuntimeInSeconds** *(integer) --*

      The maximum length of time, in seconds, that the training or compilation job can run. If job
      does not complete during this time, Amazon SageMaker ends the job. If value is not specified,
      default value is 1 day. The maximum value is 28 days.
    """


_RequiredClientCreateEndpointConfigProductionVariantsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointConfigProductionVariantsTypeDef", {"VariantName": str}
)
_OptionalClientCreateEndpointConfigProductionVariantsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointConfigProductionVariantsTypeDef",
    {
        "ModelName": str,
        "InitialInstanceCount": int,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.24xlarge",
            "ml.c4.large",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.large",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.12xlarge",
            "ml.r5.24xlarge",
            "ml.r5d.large",
            "ml.r5d.xlarge",
            "ml.r5d.2xlarge",
            "ml.r5d.4xlarge",
            "ml.r5d.12xlarge",
            "ml.r5d.24xlarge",
        ],
        "InitialVariantWeight": Any,
        "AcceleratorType": Literal[
            "ml.eia1.medium",
            "ml.eia1.large",
            "ml.eia1.xlarge",
            "ml.eia2.medium",
            "ml.eia2.large",
            "ml.eia2.xlarge",
        ],
    },
    total=False,
)


class ClientCreateEndpointConfigProductionVariantsTypeDef(
    _RequiredClientCreateEndpointConfigProductionVariantsTypeDef,
    _OptionalClientCreateEndpointConfigProductionVariantsTypeDef,
):
    """
    - *(dict) --*

      Identifies a model that you want to host and the resources to deploy for hosting it. If you
      are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the
      models by specifying variant weights.
      - **VariantName** *(string) --***[REQUIRED]**

        The name of the production variant.
    """


_ClientCreateEndpointConfigResponseTypeDef = TypedDict(
    "_ClientCreateEndpointConfigResponseTypeDef", {"EndpointConfigArn": str}, total=False
)


class ClientCreateEndpointConfigResponseTypeDef(_ClientCreateEndpointConfigResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointConfigArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint configuration.
    """


_RequiredClientCreateEndpointConfigTagsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointConfigTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEndpointConfigTagsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointConfigTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEndpointConfigTagsTypeDef(
    _RequiredClientCreateEndpointConfigTagsTypeDef, _OptionalClientCreateEndpointConfigTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreateEndpointResponseTypeDef = TypedDict(
    "_ClientCreateEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)


class ClientCreateEndpointResponseTypeDef(_ClientCreateEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint.
    """


_RequiredClientCreateEndpointTagsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEndpointTagsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEndpointTagsTypeDef(
    _RequiredClientCreateEndpointTagsTypeDef, _OptionalClientCreateEndpointTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)


class ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef(
    _ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef(
    _ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef(
    _ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef(
    _ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List[
            ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef
        ],
        "CategoricalParameterRanges": List[
            ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef(
    _ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef",
    {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int},
    total=False,
)


class ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef(
    _ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef
):
    pass


_RequiredClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_RequiredClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef",
    {"Strategy": Literal["Bayesian", "Random"]},
)
_OptionalClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_OptionalClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef",
    {
        "HyperParameterTuningJobObjective": ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef,
        "ResourceLimits": ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef,
        "ParameterRanges": ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef,
        "TrainingJobEarlyStoppingType": Literal["Off", "Auto"],
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef(
    _RequiredClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef,
    _OptionalClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef,
):
    """
    The  HyperParameterTuningJobConfig object that describes the tuning job, including the search
    strategy, the objective metric used to evaluate training jobs, ranges of parameters to search,
    and resource limits for the tuning job. For more information, see  automatic-model-tuning
    - **Strategy** *(string) --***[REQUIRED]**

      Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use
      for the training job it launches. To use the Bayesian search stategy, set this to ``Bayesian``
      . To randomly search, set it to ``Random`` . For information about search strategies, see `How
      Hyperparameter Tuning Works
      <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html>`__
      .
    """


_ClientCreateHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobResponseTypeDef",
    {"HyperParameterTuningJobArn": str},
    total=False,
)


class ClientCreateHyperParameterTuningJobResponseTypeDef(
    _ClientCreateHyperParameterTuningJobResponseTypeDef
):
    """
    - *(dict) --*

      - **HyperParameterTuningJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the tuning job. Amazon SageMaker assigns an ARN to a
        hyperparameter tuning job when you create it.
    """


_RequiredClientCreateHyperParameterTuningJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateHyperParameterTuningJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateHyperParameterTuningJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateHyperParameterTuningJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateHyperParameterTuningJobTagsTypeDef(
    _RequiredClientCreateHyperParameterTuningJobTagsTypeDef,
    _OptionalClientCreateHyperParameterTuningJobTagsTypeDef,
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "AlgorithmName": str,
        "MetricDefinitions": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef",
    {
        "StaticHyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef
        ],
        "VpcConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef,
        "OutputDataConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef,
        "ResourceConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef,
        "StoppingCondition": ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef,
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef,
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef(
    _ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef
):
    """
    The  HyperParameterTrainingJobDefinition object that describes the training jobs that this
    tuning job launches, including static hyperparameters, input data configuration, output data
    configuration, resource configuration, and stopping condition.
    - **StaticHyperParameters** *(dict) --*

      Specifies the values of hyperparameters that do not change for the tuning job.
      - *(string) --*

        - *(string) --*
    """


_ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef",
    {"HyperParameterTuningJobName": str},
    total=False,
)


class ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef(
    _ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef
):
    pass


_ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef = TypedDict(
    "_ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef",
    {
        "ParentHyperParameterTuningJobs": List[
            ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef
        ],
        "WarmStartType": Literal["IdenticalDataAndAlgorithm", "TransferLearning"],
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef(
    _ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef
):
    """
    Specifies the configuration for starting the hyperparameter tuning job using one or more
    previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform
    which combinations of hyperparameters to search over in the new tuning job.
    All training jobs launched by the new hyperparameter tuning job are evaluated by using the
    objective metric. If you specify ``IDENTICAL_DATA_AND_ALGORITHM`` as the ``WarmStartType`` value
    for the warm start configuration, the training job that performs the best in the new tuning job
    is compared to the best training jobs from the parent tuning jobs. From these, the training job
    that performs the best as measured by the objective metric is returned as the overall best
    training job.
    .. note::

      All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter
      tuning jobs count against the limit of training jobs for the tuning job.
    """


_ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef = TypedDict(
    "_ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef",
    {"AnnotationConsolidationLambdaArn": str},
    total=False,
)


class ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef(
    _ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef
):
    pass


_ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef = TypedDict(
    "_ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    {"Dollars": int, "Cents": int, "TenthFractionsOfACent": int},
    total=False,
)


class ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef(
    _ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef
):
    pass


_ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef = TypedDict(
    "_ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef
    },
    total=False,
)


class ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef(
    _ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef
):
    pass


_ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef = TypedDict(
    "_ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef", {"UiTemplateS3Uri": str}, total=False
)


class ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef(
    _ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef
):
    pass


_RequiredClientCreateLabelingJobHumanTaskConfigTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobHumanTaskConfigTypeDef", {"WorkteamArn": str}
)
_OptionalClientCreateLabelingJobHumanTaskConfigTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobHumanTaskConfigTypeDef",
    {
        "UiConfig": ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef,
        "PreHumanTaskLambdaArn": str,
        "TaskKeywords": List[str],
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "TaskAvailabilityLifetimeInSeconds": int,
        "MaxConcurrentTaskCount": int,
        "AnnotationConsolidationConfig": ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef,
        "PublicWorkforceTaskPrice": ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef,
    },
    total=False,
)


class ClientCreateLabelingJobHumanTaskConfigTypeDef(
    _RequiredClientCreateLabelingJobHumanTaskConfigTypeDef,
    _OptionalClientCreateLabelingJobHumanTaskConfigTypeDef,
):
    """
    Configures the information required for human workers to complete a labeling task.
    - **WorkteamArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of the work team assigned to complete the tasks.
    """


_ClientCreateLabelingJobInputConfigDataAttributesTypeDef = TypedDict(
    "_ClientCreateLabelingJobInputConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)


class ClientCreateLabelingJobInputConfigDataAttributesTypeDef(
    _ClientCreateLabelingJobInputConfigDataAttributesTypeDef
):
    pass


_ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef", {"ManifestS3Uri": str}
)


class ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef(
    _ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef
):
    """
    - **S3DataSource** *(dict) --***[REQUIRED]**

      The Amazon S3 location of the input data objects.
      - **ManifestS3Uri** *(string) --***[REQUIRED]**

        The Amazon S3 location of the manifest file that describes the input data objects.
    """


_ClientCreateLabelingJobInputConfigDataSourceTypeDef = TypedDict(
    "_ClientCreateLabelingJobInputConfigDataSourceTypeDef",
    {"S3DataSource": ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef},
)


class ClientCreateLabelingJobInputConfigDataSourceTypeDef(
    _ClientCreateLabelingJobInputConfigDataSourceTypeDef
):
    """
    - **DataSource** *(dict) --***[REQUIRED]**

      The location of the input data.
      - **S3DataSource** *(dict) --***[REQUIRED]**

        The Amazon S3 location of the input data objects.
        - **ManifestS3Uri** *(string) --***[REQUIRED]**

          The Amazon S3 location of the manifest file that describes the input data objects.
    """


_RequiredClientCreateLabelingJobInputConfigTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobInputConfigTypeDef",
    {"DataSource": ClientCreateLabelingJobInputConfigDataSourceTypeDef},
)
_OptionalClientCreateLabelingJobInputConfigTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobInputConfigTypeDef",
    {"DataAttributes": ClientCreateLabelingJobInputConfigDataAttributesTypeDef},
    total=False,
)


class ClientCreateLabelingJobInputConfigTypeDef(
    _RequiredClientCreateLabelingJobInputConfigTypeDef,
    _OptionalClientCreateLabelingJobInputConfigTypeDef,
):
    """
    Input data for the labeling job, such as the Amazon S3 location of the data objects and the
    location of the manifest file that describes the data objects.
    - **DataSource** *(dict) --***[REQUIRED]**

      The location of the input data.
      - **S3DataSource** *(dict) --***[REQUIRED]**

        The Amazon S3 location of the input data objects.
        - **ManifestS3Uri** *(string) --***[REQUIRED]**

          The Amazon S3 location of the manifest file that describes the input data objects.
    """


_ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef = TypedDict(
    "_ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef",
    {"VolumeKmsKeyId": str},
    total=False,
)


class ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef(
    _ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef
):
    pass


_RequiredClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef",
    {"LabelingJobAlgorithmSpecificationArn": str},
)
_OptionalClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef",
    {
        "InitialActiveLearningModelArn": str,
        "LabelingJobResourceConfig": ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef,
    },
    total=False,
)


class ClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef(
    _RequiredClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef,
    _OptionalClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef,
):
    """
    Configures the information required to perform automated data labeling.
    - **LabelingJobAlgorithmSpecificationArn** *(string) --***[REQUIRED]**

      Specifies the Amazon Resource Name (ARN) of the algorithm used for auto-labeling. You must
      select one of the following ARNs:
      * *Image classification*    ``arn:aws:sagemaker:*region*
      :027400017018:labeling-job-algorithm-specification/image-classification``
      * *Text classification*    ``arn:aws:sagemaker:*region*
      :027400017018:labeling-job-algorithm-specification/text-classification``
      * *Object detection*    ``arn:aws:sagemaker:*region*
      :027400017018:labeling-job-algorithm-specification/object-detection``
      * *Semantic Segmentation*    ``arn:aws:sagemaker:*region*
      :027400017018:labeling-job-algorithm-specification/semantic-segmentation``
    """


_RequiredClientCreateLabelingJobOutputConfigTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobOutputConfigTypeDef", {"S3OutputPath": str}
)
_OptionalClientCreateLabelingJobOutputConfigTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobOutputConfigTypeDef", {"KmsKeyId": str}, total=False
)


class ClientCreateLabelingJobOutputConfigTypeDef(
    _RequiredClientCreateLabelingJobOutputConfigTypeDef,
    _OptionalClientCreateLabelingJobOutputConfigTypeDef,
):
    """
    The location of the output data and the AWS Key Management Service key ID for the key used to
    encrypt the output data, if any.
    - **S3OutputPath** *(string) --***[REQUIRED]**

      The Amazon S3 location to write output data.
    """


_ClientCreateLabelingJobResponseTypeDef = TypedDict(
    "_ClientCreateLabelingJobResponseTypeDef", {"LabelingJobArn": str}, total=False
)


class ClientCreateLabelingJobResponseTypeDef(_ClientCreateLabelingJobResponseTypeDef):
    """
    - *(dict) --*

      - **LabelingJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the labeling job. You use this ARN to identify the
        labeling job.
    """


_ClientCreateLabelingJobStoppingConditionsTypeDef = TypedDict(
    "_ClientCreateLabelingJobStoppingConditionsTypeDef",
    {"MaxHumanLabeledObjectCount": int, "MaxPercentageOfInputDatasetLabeled": int},
    total=False,
)


class ClientCreateLabelingJobStoppingConditionsTypeDef(
    _ClientCreateLabelingJobStoppingConditionsTypeDef
):
    """
    A set of conditions for stopping the labeling job. If any of the conditions are met, the job is
    automatically stopped. You can use these conditions to control the cost of data labeling.
    - **MaxHumanLabeledObjectCount** *(integer) --*

      The maximum number of objects that can be labeled by human workers.
    """


_RequiredClientCreateLabelingJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLabelingJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLabelingJobTagsTypeDef(
    _RequiredClientCreateLabelingJobTagsTypeDef, _OptionalClientCreateLabelingJobTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreateModelContainersTypeDef = TypedDict(
    "_ClientCreateModelContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)


class ClientCreateModelContainersTypeDef(_ClientCreateModelContainersTypeDef):
    """
    - *(dict) --*

      Describes the container, as part of model definition.
      - **ContainerHostname** *(string) --*

        This parameter is ignored for models that contain only a ``PrimaryContainer`` .
        When a ``ContainerDefinition`` is part of an inference pipeline, the value of ths parameter
        uniquely identifies the container for the purposes of logging and metrics. For information,
        see `Use Logs and Metrics to Monitor an Inference Pipeline
        <https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-logs-metrics.html>`__ .
        If you don't specify a value for this parameter for a ``ContainerDefinition`` that is part
        of an inference pipeline, a unique name is automatically assigned based on the position of
        the ``ContainerDefinition`` in the pipeline. If you specify a value for the
        ``ContainerHostName`` for any ``ContainerDefinition`` that is part of an inference pipeline,
        you must specify a value for the ``ContainerHostName`` parameter of every
        ``ContainerDefinition`` in that pipeline.
    """


_ClientCreateModelPackageInferenceSpecificationContainersTypeDef = TypedDict(
    "_ClientCreateModelPackageInferenceSpecificationContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)


class ClientCreateModelPackageInferenceSpecificationContainersTypeDef(
    _ClientCreateModelPackageInferenceSpecificationContainersTypeDef
):
    """
    - *(dict) --*

      Describes the Docker container for the model package.
      - **ContainerHostname** *(string) --*

        The DNS host name for the Docker container.
    """


_RequiredClientCreateModelPackageInferenceSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateModelPackageInferenceSpecificationTypeDef",
    {"Containers": List[ClientCreateModelPackageInferenceSpecificationContainersTypeDef]},
)
_OptionalClientCreateModelPackageInferenceSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateModelPackageInferenceSpecificationTypeDef",
    {
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)


class ClientCreateModelPackageInferenceSpecificationTypeDef(
    _RequiredClientCreateModelPackageInferenceSpecificationTypeDef,
    _OptionalClientCreateModelPackageInferenceSpecificationTypeDef,
):
    """
    Specifies details about inference jobs that can be run with models based on this model package,
    including the following:
    * The Amazon ECR paths of containers that contain the inference code and model artifacts.
    * The instance types that the model package supports for transform jobs and real-time endpoints
    used for inference.
    * The input and output content formats that the model package supports for inference.
    - **Containers** *(list) --***[REQUIRED]**

      The Amazon ECR registry path of the Docker image that contains the inference code.
      - *(dict) --*

        Describes the Docker container for the model package.
        - **ContainerHostname** *(string) --*

          The DNS host name for the Docker container.
    """


_ClientCreateModelPackageResponseTypeDef = TypedDict(
    "_ClientCreateModelPackageResponseTypeDef", {"ModelPackageArn": str}, total=False
)


class ClientCreateModelPackageResponseTypeDef(_ClientCreateModelPackageResponseTypeDef):
    """
    - *(dict) --*

      - **ModelPackageArn** *(string) --*

        The Amazon Resource Name (ARN) of the new model package.
    """


_ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef = TypedDict(
    "_ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef",
    {"ModelDataUrl": str, "AlgorithmName": str},
    total=False,
)


class ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef(
    _ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef
):
    """
    - *(dict) --*

      Specifies an algorithm that was used to create the model package. The algorithm must be either
      an algorithm resource in your Amazon SageMaker account or an algorithm in AWS Marketplace that
      you are subscribed to.
      - **ModelDataUrl** *(string) --*

        The Amazon S3 path where the model artifacts, which result from model training, are stored.
        This path must point to a single ``gzip`` compressed tar archive (``.tar.gz`` suffix).
    """


_ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef = TypedDict(
    "_ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef",
    {
        "SourceAlgorithms": List[
            ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef
        ]
    },
)


class ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef(
    _ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef
):
    """
    Details about the algorithm that was used to create the model package.
    - **SourceAlgorithms** *(list) --***[REQUIRED]**

      A list of the algorithms that were used to create a model package.
      - *(dict) --*

        Specifies an algorithm that was used to create the model package. The algorithm must be
        either an algorithm resource in your Amazon SageMaker account or an algorithm in AWS
        Marketplace that you are subscribed to.
        - **ModelDataUrl** *(string) --*

          The Amazon S3 path where the model artifacts, which result from model training, are
          stored. This path must point to a single ``gzip`` compressed tar archive (``.tar.gz``
          suffix).
    """


_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)


class ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef(
    _ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
):
    pass


_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef = TypedDict(
    "_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
    },
    total=False,
)


class ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef(
    _ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef
):
    pass


_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef = TypedDict(
    "_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    {
        "DataSource": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)


class ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef(
    _ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef
):
    pass


_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef = TypedDict(
    "_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)


class ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef(
    _ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef
):
    pass


_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef = TypedDict(
    "_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef(
    _ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef
):
    pass


_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef = TypedDict(
    "_ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef,
        "TransformOutput": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef,
        "TransformResources": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef,
    },
    total=False,
)


class ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef(
    _ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef
):
    pass


_ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef = TypedDict(
    "_ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef,
    },
    total=False,
)


class ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef(
    _ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef
):
    pass


_RequiredClientCreateModelPackageValidationSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateModelPackageValidationSpecificationTypeDef", {"ValidationRole": str}
)
_OptionalClientCreateModelPackageValidationSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateModelPackageValidationSpecificationTypeDef",
    {
        "ValidationProfiles": List[
            ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef
        ]
    },
    total=False,
)


class ClientCreateModelPackageValidationSpecificationTypeDef(
    _RequiredClientCreateModelPackageValidationSpecificationTypeDef,
    _OptionalClientCreateModelPackageValidationSpecificationTypeDef,
):
    """
    Specifies configurations for one or more transform jobs that Amazon SageMaker runs to test the
    model package.
    - **ValidationRole** *(string) --***[REQUIRED]**

      The IAM roles to be used for the validation of the model package.
    """


_ClientCreateModelPrimaryContainerTypeDef = TypedDict(
    "_ClientCreateModelPrimaryContainerTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)


class ClientCreateModelPrimaryContainerTypeDef(_ClientCreateModelPrimaryContainerTypeDef):
    """
    The location of the primary docker image containing inference code, associated artifacts, and
    custom environment map that the inference code uses when the model is deployed for predictions.
    - **ContainerHostname** *(string) --*

      This parameter is ignored for models that contain only a ``PrimaryContainer`` .
      When a ``ContainerDefinition`` is part of an inference pipeline, the value of ths parameter
      uniquely identifies the container for the purposes of logging and metrics. For information,
      see `Use Logs and Metrics to Monitor an Inference Pipeline
      <https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-logs-metrics.html>`__ . If
      you don't specify a value for this parameter for a ``ContainerDefinition`` that is part of an
      inference pipeline, a unique name is automatically assigned based on the position of the
      ``ContainerDefinition`` in the pipeline. If you specify a value for the ``ContainerHostName``
      for any ``ContainerDefinition`` that is part of an inference pipeline, you must specify a
      value for the ``ContainerHostName`` parameter of every ``ContainerDefinition`` in that
      pipeline.
    """


_ClientCreateModelResponseTypeDef = TypedDict(
    "_ClientCreateModelResponseTypeDef", {"ModelArn": str}, total=False
)


class ClientCreateModelResponseTypeDef(_ClientCreateModelResponseTypeDef):
    """
    - *(dict) --*

      - **ModelArn** *(string) --*

        The ARN of the model created in Amazon SageMaker.
    """


_RequiredClientCreateModelTagsTypeDef = TypedDict(
    "_RequiredClientCreateModelTagsTypeDef", {"Key": str}
)
_OptionalClientCreateModelTagsTypeDef = TypedDict(
    "_OptionalClientCreateModelTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateModelTagsTypeDef(
    _RequiredClientCreateModelTagsTypeDef, _OptionalClientCreateModelTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_RequiredClientCreateModelVpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateModelVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientCreateModelVpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateModelVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientCreateModelVpcConfigTypeDef(
    _RequiredClientCreateModelVpcConfigTypeDef, _OptionalClientCreateModelVpcConfigTypeDef
):
    """
    A `VpcConfig <https://docs.aws.amazon.com/sagemaker/latest/dg/API_VpcConfig.html>`__ object that
    specifies the VPC that you want your model to connect to. Control access to and from your model
    container by configuring the VPC. ``VpcConfig`` is used in hosting services and in batch
    transform. For more information, see `Protect Endpoints by Using an Amazon Virtual Private Cloud
    <https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html>`__ and `Protect Data in Batch
    Transform Jobs by Using an Amazon Virtual Private Cloud
    <https://docs.aws.amazon.com/sagemaker/latest/dg/batch-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC
      that is specified in the ``Subnets`` field.
      - *(string) --*
    """


_ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef = TypedDict(
    "_ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef", {"Content": str}, total=False
)


class ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef(
    _ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef
):
    """
    - *(dict) --*

      Contains the notebook instance lifecycle configuration script.
      Each lifecycle configuration script has a limit of 16384 characters.
      The value of the ``$PATH`` environment variable that is available to both scripts is
      ``/sbin:bin:/usr/sbin:/usr/bin`` .
      View CloudWatch Logs for notebook instance lifecycle configurations in log group
      ``/aws/sagemaker/NotebookInstances`` in log stream
      ``[notebook-instance-name]/[LifecycleConfigHook]`` .
      Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for
      longer than 5 minutes, it fails and the notebook instance is not created or started.
      For information about notebook instance lifestyle configurations, see `Step 2.1\\: (Optional)
      Customize a Notebook Instance
      <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
      - **Content** *(string) --*

        A base64-encoded string that contains a shell script for a notebook instance lifecycle
        configuration.
    """


_ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef = TypedDict(
    "_ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef", {"Content": str}, total=False
)


class ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef(
    _ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef
):
    """
    - *(dict) --*

      Contains the notebook instance lifecycle configuration script.
      Each lifecycle configuration script has a limit of 16384 characters.
      The value of the ``$PATH`` environment variable that is available to both scripts is
      ``/sbin:bin:/usr/sbin:/usr/bin`` .
      View CloudWatch Logs for notebook instance lifecycle configurations in log group
      ``/aws/sagemaker/NotebookInstances`` in log stream
      ``[notebook-instance-name]/[LifecycleConfigHook]`` .
      Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for
      longer than 5 minutes, it fails and the notebook instance is not created or started.
      For information about notebook instance lifestyle configurations, see `Step 2.1\\: (Optional)
      Customize a Notebook Instance
      <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
      - **Content** *(string) --*

        A base64-encoded string that contains a shell script for a notebook instance lifecycle
        configuration.
    """


_ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef = TypedDict(
    "_ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef",
    {"NotebookInstanceLifecycleConfigArn": str},
    total=False,
)


class ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef(
    _ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef
):
    """
    - *(dict) --*

      - **NotebookInstanceLifecycleConfigArn** *(string) --*

        The Amazon Resource Name (ARN) of the lifecycle configuration.
    """


_ClientCreateNotebookInstanceResponseTypeDef = TypedDict(
    "_ClientCreateNotebookInstanceResponseTypeDef", {"NotebookInstanceArn": str}, total=False
)


class ClientCreateNotebookInstanceResponseTypeDef(_ClientCreateNotebookInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **NotebookInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the notebook instance.
    """


_RequiredClientCreateNotebookInstanceTagsTypeDef = TypedDict(
    "_RequiredClientCreateNotebookInstanceTagsTypeDef", {"Key": str}
)
_OptionalClientCreateNotebookInstanceTagsTypeDef = TypedDict(
    "_OptionalClientCreateNotebookInstanceTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateNotebookInstanceTagsTypeDef(
    _RequiredClientCreateNotebookInstanceTagsTypeDef,
    _OptionalClientCreateNotebookInstanceTagsTypeDef,
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreatePresignedNotebookInstanceUrlResponseTypeDef = TypedDict(
    "_ClientCreatePresignedNotebookInstanceUrlResponseTypeDef", {"AuthorizedUrl": str}, total=False
)


class ClientCreatePresignedNotebookInstanceUrlResponseTypeDef(
    _ClientCreatePresignedNotebookInstanceUrlResponseTypeDef
):
    """
    - *(dict) --*

      - **AuthorizedUrl** *(string) --*

        A JSON object that contains the URL string.
    """


_ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "_ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)


class ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef(
    _ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
):
    pass


_ClientCreateTrainingJobAlgorithmSpecificationTypeDef = TypedDict(
    "_ClientCreateTrainingJobAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "MetricDefinitions": List[
            ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateTrainingJobAlgorithmSpecificationTypeDef(
    _ClientCreateTrainingJobAlgorithmSpecificationTypeDef
):
    """
    The registry path of the Docker image that contains the training algorithm and
    algorithm-specific metadata, including the input mode. For more information about algorithms
    provided by Amazon SageMaker, see `Algorithms
    <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . For information about
    providing your own algorithms, see `Using Your Own Algorithms with Amazon SageMaker
    <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
    - **TrainingImage** *(string) --*

      The registry path of the Docker image that contains the training algorithm. For information
      about docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon
      SageMaker\\: Common Parameters
      <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__
      . Amazon SageMaker supports both ``registry/repository[:tag]`` and
      ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own
      Algorithms with Amazon SageMaker
      <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
    """


_RequiredClientCreateTrainingJobCheckpointConfigTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobCheckpointConfigTypeDef", {"S3Uri": str}
)
_OptionalClientCreateTrainingJobCheckpointConfigTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobCheckpointConfigTypeDef", {"LocalPath": str}, total=False
)


class ClientCreateTrainingJobCheckpointConfigTypeDef(
    _RequiredClientCreateTrainingJobCheckpointConfigTypeDef,
    _OptionalClientCreateTrainingJobCheckpointConfigTypeDef,
):
    """
    Contains information about the output location for managed spot training checkpoint data.
    - **S3Uri** *(string) --***[REQUIRED]**

      Identifies the S3 path where you want Amazon SageMaker to store checkpoints. For example,
      ``s3://bucket-name/key-name-prefix`` .
    """


_ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "_ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)


class ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef(
    _ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef
):
    pass


_ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef(
    _ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientCreateTrainingJobInputDataConfigDataSourceTypeDef = TypedDict(
    "_ClientCreateTrainingJobInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)


class ClientCreateTrainingJobInputDataConfigDataSourceTypeDef(
    _ClientCreateTrainingJobInputDataConfigDataSourceTypeDef
):
    pass


_ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef = TypedDict(
    "_ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef", {"Seed": int}, total=False
)


class ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef(
    _ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef
):
    pass


_RequiredClientCreateTrainingJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobInputDataConfigTypeDef", {"ChannelName": str}
)
_OptionalClientCreateTrainingJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobInputDataConfigTypeDef",
    {
        "DataSource": ClientCreateTrainingJobInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class ClientCreateTrainingJobInputDataConfigTypeDef(
    _RequiredClientCreateTrainingJobInputDataConfigTypeDef,
    _OptionalClientCreateTrainingJobInputDataConfigTypeDef,
):
    """
    - *(dict) --*

      A channel is a named input source that training algorithms can consume.
      - **ChannelName** *(string) --***[REQUIRED]**

        The name of the channel.
    """


_ClientCreateTrainingJobOutputDataConfigTypeDef = TypedDict(
    "_ClientCreateTrainingJobOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)


class ClientCreateTrainingJobOutputDataConfigTypeDef(
    _ClientCreateTrainingJobOutputDataConfigTypeDef
):
    """
    Specifies the path to the S3 location where you want to store model artifacts. Amazon SageMaker
    creates subfolders for the artifacts.
    - **KmsKeyId** *(string) --*

      The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model
      artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the
      following formats:
      * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``
      * // Amazon Resource Name (ARN) of a KMS Key
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``
      * // KMS Key Alias  ``"alias/ExampleAlias"``
      * // Amazon Resource Name (ARN) of a KMS Key Alias
      ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
      If you use a KMS key ID or an alias of your master key, the Amazon SageMaker execution role
      must include permissions to call ``kms:Encrypt`` . If you don't provide a KMS key ID, Amazon
      SageMaker uses the default KMS key for Amazon S3 for your role's account. Amazon SageMaker
      uses server-side encryption with KMS-managed keys for ``OutputDataConfig`` . If you use a
      bucket policy with an ``s3:PutObject`` permission that only allows objects with server-side
      encryption, set the condition key of ``s3:x-amz-server-side-encryption`` to ``"aws:kms"`` .
      For more information, see `KMS-Managed Encryption Keys
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon
      Simple Storage Service Developer Guide.*
      The KMS key policy must grant permission to the IAM role that you specify in your
      ``CreateTrainingJob`` , ``CreateTransformJob`` , or ``CreateHyperParameterTuningJob``
      requests. For more information, see `Using Key Policies in AWS KMS
      <https://docs.aws.amazon.com/http:/docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__
      in the *AWS Key Management Service Developer Guide* .
    """


_RequiredClientCreateTrainingJobResourceConfigTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ]
    },
)
_OptionalClientCreateTrainingJobResourceConfigTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobResourceConfigTypeDef",
    {"InstanceCount": int, "VolumeSizeInGB": int, "VolumeKmsKeyId": str},
    total=False,
)


class ClientCreateTrainingJobResourceConfigTypeDef(
    _RequiredClientCreateTrainingJobResourceConfigTypeDef,
    _OptionalClientCreateTrainingJobResourceConfigTypeDef,
):
    """
    The resources, including the ML compute instances and ML storage volumes, to use for model
    training.
    ML storage volumes store model artifacts and incremental states. Training algorithms might also
    use ML storage volumes for scratch space. If you want Amazon SageMaker to use the ML storage
    volume to store the training data, choose ``File`` as the ``TrainingInputMode`` in the algorithm
    specification. For distributed training algorithms, specify an instance count greater than 1.
    - **InstanceType** *(string) --***[REQUIRED]**

      The ML compute instance type.
    """


_ClientCreateTrainingJobResponseTypeDef = TypedDict(
    "_ClientCreateTrainingJobResponseTypeDef", {"TrainingJobArn": str}, total=False
)


class ClientCreateTrainingJobResponseTypeDef(_ClientCreateTrainingJobResponseTypeDef):
    """
    - *(dict) --*

      - **TrainingJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the training job.
    """


_ClientCreateTrainingJobStoppingConditionTypeDef = TypedDict(
    "_ClientCreateTrainingJobStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientCreateTrainingJobStoppingConditionTypeDef(
    _ClientCreateTrainingJobStoppingConditionTypeDef
):
    """
    Specifies a limit to how long a model training job can run. When the job reaches the time limit,
    Amazon SageMaker ends the training job. Use this API to cap model training costs.
    To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal, which delays job
    termination for 120 seconds. Algorithms can use this 120-second window to save the model
    artifacts, so the results of training are not lost.
    - **MaxRuntimeInSeconds** *(integer) --*

      The maximum length of time, in seconds, that the training or compilation job can run. If job
      does not complete during this time, Amazon SageMaker ends the job. If value is not specified,
      default value is 1 day. The maximum value is 28 days.
    """


_RequiredClientCreateTrainingJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTrainingJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTrainingJobTagsTypeDef(
    _RequiredClientCreateTrainingJobTagsTypeDef, _OptionalClientCreateTrainingJobTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_RequiredClientCreateTrainingJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientCreateTrainingJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientCreateTrainingJobVpcConfigTypeDef(
    _RequiredClientCreateTrainingJobVpcConfigTypeDef,
    _OptionalClientCreateTrainingJobVpcConfigTypeDef,
):
    """
    A  VpcConfig object that specifies the VPC that you want your training job to connect to.
    Control access to and from your training container by configuring the VPC. For more information,
    see `Protect Training Jobs by Using an Amazon Virtual Private Cloud
    <https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
    - **SecurityGroupIds** *(list) --***[REQUIRED]**

      The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC
      that is specified in the ``Subnets`` field.
      - *(string) --*
    """


_ClientCreateTransformJobDataProcessingTypeDef = TypedDict(
    "_ClientCreateTransformJobDataProcessingTypeDef",
    {"InputFilter": str, "OutputFilter": str, "JoinSource": Literal["Input", "None"]},
    total=False,
)


class ClientCreateTransformJobDataProcessingTypeDef(_ClientCreateTransformJobDataProcessingTypeDef):
    """
    The data structure used to specify the data to be used for inference in a batch transform job
    and to associate the data that is relevant to the prediction results in the output. The input
    filter provided allows you to exclude input data that is not needed for inference in a batch
    transform job. The output filter provided allows you to include input data relevant to
    interpreting the predictions in the output from the job. For more information, see `Associate
    Prediction Results with their Corresponding Input Records
    <https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html>`__ .
    - **InputFilter** *(string) --*

      A `JSONPath
      <https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators>`__
      expression used to select a portion of the input data to pass to the algorithm. Use the
      ``InputFilter`` parameter to exclude fields, such as an ID column, from the input. If you want
      Amazon SageMaker to pass the entire input dataset to the algorithm, accept the default value
      ``$`` .
      Examples: ``"$"`` , ``"$[1:]"`` , ``"$.features"``
    """


_ClientCreateTransformJobResponseTypeDef = TypedDict(
    "_ClientCreateTransformJobResponseTypeDef", {"TransformJobArn": str}, total=False
)


class ClientCreateTransformJobResponseTypeDef(_ClientCreateTransformJobResponseTypeDef):
    """
    - *(dict) --*

      - **TransformJobArn** *(string) --*

        The Amazon Resource Name (ARN) of the transform job.
    """


_RequiredClientCreateTransformJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTransformJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTransformJobTagsTypeDef(
    _RequiredClientCreateTransformJobTagsTypeDef, _OptionalClientCreateTransformJobTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_RequiredClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"]},
)
_OptionalClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef(
    _RequiredClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef,
    _OptionalClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef,
):
    """
    - **S3DataSource** *(dict) --***[REQUIRED]**

      The S3 location of the data source that is associated with a channel.
      - **S3DataType** *(string) --***[REQUIRED]**

        If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses
        all objects with the specified key name prefix for batch transform.
        If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file
        containing a list of object keys that you want Amazon SageMaker to use for batch transform.
        The following values are compatible: ``ManifestFile`` , ``S3Prefix``
        The following value is not compatible: ``AugmentedManifestFile``
    """


_ClientCreateTransformJobTransformInputDataSourceTypeDef = TypedDict(
    "_ClientCreateTransformJobTransformInputDataSourceTypeDef",
    {"S3DataSource": ClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef},
)


class ClientCreateTransformJobTransformInputDataSourceTypeDef(
    _ClientCreateTransformJobTransformInputDataSourceTypeDef
):
    """
    - **DataSource** *(dict) --***[REQUIRED]**

      Describes the location of the channel data, which is, the S3 location of the input data that
      the model can consume.
      - **S3DataSource** *(dict) --***[REQUIRED]**

        The S3 location of the data source that is associated with a channel.
        - **S3DataType** *(string) --***[REQUIRED]**

          If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses
          all objects with the specified key name prefix for batch transform.
          If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file
          containing a list of object keys that you want Amazon SageMaker to use for batch
          transform.
          The following values are compatible: ``ManifestFile`` , ``S3Prefix``
          The following value is not compatible: ``AugmentedManifestFile``
    """


_RequiredClientCreateTransformJobTransformInputTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTransformInputTypeDef",
    {"DataSource": ClientCreateTransformJobTransformInputDataSourceTypeDef},
)
_OptionalClientCreateTransformJobTransformInputTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTransformInputTypeDef",
    {
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)


class ClientCreateTransformJobTransformInputTypeDef(
    _RequiredClientCreateTransformJobTransformInputTypeDef,
    _OptionalClientCreateTransformJobTransformInputTypeDef,
):
    """
    Describes the input source and the way the transform job consumes it.
    - **DataSource** *(dict) --***[REQUIRED]**

      Describes the location of the channel data, which is, the S3 location of the input data that
      the model can consume.
      - **S3DataSource** *(dict) --***[REQUIRED]**

        The S3 location of the data source that is associated with a channel.
        - **S3DataType** *(string) --***[REQUIRED]**

          If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses
          all objects with the specified key name prefix for batch transform.
          If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file
          containing a list of object keys that you want Amazon SageMaker to use for batch
          transform.
          The following values are compatible: ``ManifestFile`` , ``S3Prefix``
          The following value is not compatible: ``AugmentedManifestFile``
    """


_RequiredClientCreateTransformJobTransformOutputTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTransformOutputTypeDef", {"S3OutputPath": str}
)
_OptionalClientCreateTransformJobTransformOutputTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTransformOutputTypeDef",
    {"Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)


class ClientCreateTransformJobTransformOutputTypeDef(
    _RequiredClientCreateTransformJobTransformOutputTypeDef,
    _OptionalClientCreateTransformJobTransformOutputTypeDef,
):
    """
    Describes the results of the transform job.
    - **S3OutputPath** *(string) --***[REQUIRED]**

      The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job.
      For example, ``s3://bucket-name/key-name-prefix`` .
      For every S3 object used as input for the transform job, batch transform stores the
      transformed data with an .``out`` suffix in a corresponding subfolder in the location in the
      output prefix. For example, for the input data stored at
      ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` , batch transform stores the
      transformed data at ``s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out`` .
      Batch transform doesn't upload partially processed objects. For an input S3 object that
      contains multiple records, it creates an .``out`` file only if the transform job succeeds on
      the entire file. When the input contains multiple S3 objects, the batch transform job
      processes the listed S3 objects and uploads only the output for successfully processed
      objects. If any object fails in the transform job batch transform marks the job as failed to
      prompt investigation.
    """


_RequiredClientCreateTransformJobTransformResourcesTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ]
    },
)
_OptionalClientCreateTransformJobTransformResourcesTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTransformResourcesTypeDef",
    {"InstanceCount": int, "VolumeKmsKeyId": str},
    total=False,
)


class ClientCreateTransformJobTransformResourcesTypeDef(
    _RequiredClientCreateTransformJobTransformResourcesTypeDef,
    _OptionalClientCreateTransformJobTransformResourcesTypeDef,
):
    """
    Describes the resources, including ML instance types and ML instance count, to use for the
    transform job.
    - **InstanceType** *(string) --***[REQUIRED]**

      The ML compute instance type for the transform job. If you are using built-in algorithms to
      transform moderately sized datasets, we recommend using ml.m4.xlarge or ``ml.m5.large``
      instance types.
    """


_RequiredClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_RequiredClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str},
)
_OptionalClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_OptionalClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserGroup": str, "ClientId": str},
    total=False,
)


class ClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef(
    _RequiredClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef,
    _OptionalClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef,
):
    """
    - **CognitoMemberDefinition** *(dict) --*

      The Amazon Cognito user group that is part of the work team.
      - **UserPool** *(string) --***[REQUIRED]**

        An identifier for a user pool. The user pool must be in the same region as the service that
        you are calling.
    """


_ClientCreateWorkteamMemberDefinitionsTypeDef = TypedDict(
    "_ClientCreateWorkteamMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)


class ClientCreateWorkteamMemberDefinitionsTypeDef(_ClientCreateWorkteamMemberDefinitionsTypeDef):
    """
    - *(dict) --*

      Defines the Amazon Cognito user group that is part of a work team.
      - **CognitoMemberDefinition** *(dict) --*

        The Amazon Cognito user group that is part of the work team.
        - **UserPool** *(string) --***[REQUIRED]**

          An identifier for a user pool. The user pool must be in the same region as the service
          that you are calling.
    """


_ClientCreateWorkteamNotificationConfigurationTypeDef = TypedDict(
    "_ClientCreateWorkteamNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)


class ClientCreateWorkteamNotificationConfigurationTypeDef(
    _ClientCreateWorkteamNotificationConfigurationTypeDef
):
    """
    Configures notification of workers regarding available or expiring work items.
    - **NotificationTopicArn** *(string) --*

      The ARN for the SNS topic to which notifications should be published.
    """


_ClientCreateWorkteamResponseTypeDef = TypedDict(
    "_ClientCreateWorkteamResponseTypeDef", {"WorkteamArn": str}, total=False
)


class ClientCreateWorkteamResponseTypeDef(_ClientCreateWorkteamResponseTypeDef):
    """
    - *(dict) --*

      - **WorkteamArn** *(string) --*

        The Amazon Resource Name (ARN) of the work team. You can use this ARN to identify the work
        team.
    """


_RequiredClientCreateWorkteamTagsTypeDef = TypedDict(
    "_RequiredClientCreateWorkteamTagsTypeDef", {"Key": str}
)
_OptionalClientCreateWorkteamTagsTypeDef = TypedDict(
    "_OptionalClientCreateWorkteamTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateWorkteamTagsTypeDef(
    _RequiredClientCreateWorkteamTagsTypeDef, _OptionalClientCreateWorkteamTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientDeleteWorkteamResponseTypeDef = TypedDict(
    "_ClientDeleteWorkteamResponseTypeDef", {"Success": bool}, total=False
)


class ClientDeleteWorkteamResponseTypeDef(_ClientDeleteWorkteamResponseTypeDef):
    """
    - *(dict) --*

      - **Success** *(boolean) --*

        Returns ``true`` if the work team was successfully deleted; otherwise, returns ``false`` .
    """


_ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef",
    {
        "Name": str,
        "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"],
        "FailureReason": str,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef(
    _ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef
):
    pass


_ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef",
    {
        "Name": str,
        "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"],
        "FailureReason": str,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef(
    _ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef
):
    pass


_ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef",
    {
        "ValidationStatuses": List[
            ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef
        ],
        "ImageScanStatuses": List[
            ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef(
    _ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef
):
    pass


_ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef(
    _ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef
):
    pass


_ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef",
    {
        "Containers": List[ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef],
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)


class ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef(
    _ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef",
    {
        "IntegerParameterRangeSpecification": ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef,
        "ContinuousParameterRangeSpecification": ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef,
        "CategoricalParameterRangeSpecification": ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": Literal["Integer", "Continuous", "Categorical", "FreeText"],
        "Range": ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef,
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef",
    {
        "Name": str,
        "Description": str,
        "IsRequired": bool,
        "SupportedContentTypes": List[str],
        "SupportedCompressionTypes": List[Literal["None", "Gzip"]],
        "SupportedInputModes": List[Literal["Pipe", "File"]],
    },
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef",
    {
        "TrainingImage": str,
        "TrainingImageDigest": str,
        "SupportedHyperParameters": List[
            ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef
        ],
        "SupportedTrainingInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.p3dn.24xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
            ]
        ],
        "SupportsDistributedTraining": bool,
        "MetricDefinitions": List[
            ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef
        ],
        "TrainingChannels": List[
            ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef
        ],
        "SupportedTuningJobObjectiveMetrics": List[
            ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef(
    _ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": Literal["Pipe", "File"],
        "HyperParameters": Dict[str, str],
        "InputDataConfig": List[
            ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef
        ],
        "OutputDataConfig": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef,
        "ResourceConfig": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef,
        "StoppingCondition": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    {
        "DataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef,
        "TransformOutput": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef,
        "TransformResources": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef,
        "TransformJobDefinition": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef
):
    pass


_ClientDescribeAlgorithmResponseValidationSpecificationTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List[
            ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlgorithmResponseValidationSpecificationTypeDef(
    _ClientDescribeAlgorithmResponseValidationSpecificationTypeDef
):
    pass


_ClientDescribeAlgorithmResponseTypeDef = TypedDict(
    "_ClientDescribeAlgorithmResponseTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "TrainingSpecification": ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef,
        "InferenceSpecification": ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef,
        "ValidationSpecification": ClientDescribeAlgorithmResponseValidationSpecificationTypeDef,
        "AlgorithmStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
        "AlgorithmStatusDetails": ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef,
        "ProductId": str,
        "CertifyForMarketplace": bool,
    },
    total=False,
)


class ClientDescribeAlgorithmResponseTypeDef(_ClientDescribeAlgorithmResponseTypeDef):
    """
    - *(dict) --*

      - **AlgorithmName** *(string) --*

        The name of the algorithm being described.
    """


_ClientDescribeCodeRepositoryResponseGitConfigTypeDef = TypedDict(
    "_ClientDescribeCodeRepositoryResponseGitConfigTypeDef",
    {"RepositoryUrl": str, "Branch": str, "SecretArn": str},
    total=False,
)


class ClientDescribeCodeRepositoryResponseGitConfigTypeDef(
    _ClientDescribeCodeRepositoryResponseGitConfigTypeDef
):
    pass


_ClientDescribeCodeRepositoryResponseTypeDef = TypedDict(
    "_ClientDescribeCodeRepositoryResponseTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": ClientDescribeCodeRepositoryResponseGitConfigTypeDef,
    },
    total=False,
)


class ClientDescribeCodeRepositoryResponseTypeDef(_ClientDescribeCodeRepositoryResponseTypeDef):
    """
    - *(dict) --*

      - **CodeRepositoryName** *(string) --*

        The name of the Git repository.
    """


_ClientDescribeCompilationJobResponseInputConfigTypeDef = TypedDict(
    "_ClientDescribeCompilationJobResponseInputConfigTypeDef",
    {
        "S3Uri": str,
        "DataInputConfig": str,
        "Framework": Literal["TENSORFLOW", "MXNET", "ONNX", "PYTORCH", "XGBOOST"],
    },
    total=False,
)


class ClientDescribeCompilationJobResponseInputConfigTypeDef(
    _ClientDescribeCompilationJobResponseInputConfigTypeDef
):
    pass


_ClientDescribeCompilationJobResponseModelArtifactsTypeDef = TypedDict(
    "_ClientDescribeCompilationJobResponseModelArtifactsTypeDef",
    {"S3ModelArtifacts": str},
    total=False,
)


class ClientDescribeCompilationJobResponseModelArtifactsTypeDef(
    _ClientDescribeCompilationJobResponseModelArtifactsTypeDef
):
    pass


_ClientDescribeCompilationJobResponseOutputConfigTypeDef = TypedDict(
    "_ClientDescribeCompilationJobResponseOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
        "TargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "rasp3b",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
        ],
    },
    total=False,
)


class ClientDescribeCompilationJobResponseOutputConfigTypeDef(
    _ClientDescribeCompilationJobResponseOutputConfigTypeDef
):
    pass


_ClientDescribeCompilationJobResponseStoppingConditionTypeDef = TypedDict(
    "_ClientDescribeCompilationJobResponseStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientDescribeCompilationJobResponseStoppingConditionTypeDef(
    _ClientDescribeCompilationJobResponseStoppingConditionTypeDef
):
    pass


_ClientDescribeCompilationJobResponseTypeDef = TypedDict(
    "_ClientDescribeCompilationJobResponseTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CompilationJobStatus": Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ],
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "StoppingCondition": ClientDescribeCompilationJobResponseStoppingConditionTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ModelArtifacts": ClientDescribeCompilationJobResponseModelArtifactsTypeDef,
        "RoleArn": str,
        "InputConfig": ClientDescribeCompilationJobResponseInputConfigTypeDef,
        "OutputConfig": ClientDescribeCompilationJobResponseOutputConfigTypeDef,
    },
    total=False,
)


class ClientDescribeCompilationJobResponseTypeDef(_ClientDescribeCompilationJobResponseTypeDef):
    """
    - *(dict) --*

      - **CompilationJobName** *(string) --*

        The name of the model compilation job.
    """


_ClientDescribeEndpointConfigResponseProductionVariantsTypeDef = TypedDict(
    "_ClientDescribeEndpointConfigResponseProductionVariantsTypeDef",
    {
        "VariantName": str,
        "ModelName": str,
        "InitialInstanceCount": int,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.24xlarge",
            "ml.c4.large",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.large",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.12xlarge",
            "ml.r5.24xlarge",
            "ml.r5d.large",
            "ml.r5d.xlarge",
            "ml.r5d.2xlarge",
            "ml.r5d.4xlarge",
            "ml.r5d.12xlarge",
            "ml.r5d.24xlarge",
        ],
        "InitialVariantWeight": Any,
        "AcceleratorType": Literal[
            "ml.eia1.medium",
            "ml.eia1.large",
            "ml.eia1.xlarge",
            "ml.eia2.medium",
            "ml.eia2.large",
            "ml.eia2.xlarge",
        ],
    },
    total=False,
)


class ClientDescribeEndpointConfigResponseProductionVariantsTypeDef(
    _ClientDescribeEndpointConfigResponseProductionVariantsTypeDef
):
    pass


_ClientDescribeEndpointConfigResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointConfigResponseTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "ProductionVariants": List[ClientDescribeEndpointConfigResponseProductionVariantsTypeDef],
        "KmsKeyId": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeEndpointConfigResponseTypeDef(_ClientDescribeEndpointConfigResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointConfigName** *(string) --*

        Name of the Amazon SageMaker endpoint configuration.
    """


_ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef = TypedDict(
    "_ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef",
    {"SpecifiedImage": str, "ResolvedImage": str, "ResolutionTime": datetime},
    total=False,
)


class ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef(
    _ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef
):
    pass


_ClientDescribeEndpointResponseProductionVariantsTypeDef = TypedDict(
    "_ClientDescribeEndpointResponseProductionVariantsTypeDef",
    {
        "VariantName": str,
        "DeployedImages": List[
            ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef
        ],
        "CurrentWeight": Any,
        "DesiredWeight": Any,
        "CurrentInstanceCount": int,
        "DesiredInstanceCount": int,
    },
    total=False,
)


class ClientDescribeEndpointResponseProductionVariantsTypeDef(
    _ClientDescribeEndpointResponseProductionVariantsTypeDef
):
    pass


_ClientDescribeEndpointResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointResponseTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "ProductionVariants": List[ClientDescribeEndpointResponseProductionVariantsTypeDef],
        "EndpointStatus": Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ],
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientDescribeEndpointResponseTypeDef(_ClientDescribeEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointName** *(string) --*

        Name of the endpoint.
    """


_ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str, "Value": Any},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobName": str,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "TunedHyperParameters": Dict[str, str],
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef
        ],
        "CategoricalParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef",
    {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef",
    {
        "Strategy": Literal["Bayesian", "Random"],
        "HyperParameterTuningJobObjective": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef,
        "ResourceLimits": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef,
        "ParameterRanges": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef,
        "TrainingJobEarlyStoppingType": Literal["Off", "Auto"],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef",
    {"Succeeded": int, "Pending": int, "Failed": int},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str, "Value": Any},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobName": str,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "TunedHyperParameters": Dict[str, str],
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "AlgorithmName": str,
        "MetricDefinitions": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef",
    {
        "StaticHyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef
        ],
        "VpcConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef,
        "OutputDataConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef,
        "ResourceConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef,
        "StoppingCondition": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef,
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef,
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef",
    {"HyperParameterTuningJobName": str},
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef",
    {
        "ParentHyperParameterTuningJobs": List[
            ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef
        ],
        "WarmStartType": Literal["IdenticalDataAndAlgorithm", "TransferLearning"],
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef
):
    pass


_ClientDescribeHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_ClientDescribeHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef,
        "TrainingJobDefinition": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef,
        "HyperParameterTuningJobStatus": Literal[
            "Completed", "InProgress", "Failed", "Stopped", "Stopping"
        ],
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef,
        "BestTrainingJob": ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef,
        "OverallBestTrainingJob": ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef,
        "WarmStartConfig": ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef,
        "FailureReason": str,
    },
    total=False,
)


class ClientDescribeHyperParameterTuningJobResponseTypeDef(
    _ClientDescribeHyperParameterTuningJobResponseTypeDef
):
    """
    - *(dict) --*

      - **HyperParameterTuningJobName** *(string) --*

        The name of the tuning job.
    """


_ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef",
    {"AnnotationConsolidationLambdaArn": str},
    total=False,
)


class ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef(
    _ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef
):
    pass


_ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    {"Dollars": int, "Cents": int, "TenthFractionsOfACent": int},
    total=False,
)


class ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef(
    _ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef
):
    pass


_ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef
    },
    total=False,
)


class ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef(
    _ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef
):
    pass


_ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef",
    {"UiTemplateS3Uri": str},
    total=False,
)


class ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef(
    _ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef
):
    pass


_ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef",
    {
        "WorkteamArn": str,
        "UiConfig": ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef,
        "PreHumanTaskLambdaArn": str,
        "TaskKeywords": List[str],
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "TaskAvailabilityLifetimeInSeconds": int,
        "MaxConcurrentTaskCount": int,
        "AnnotationConsolidationConfig": ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef,
        "PublicWorkforceTaskPrice": ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef,
    },
    total=False,
)


class ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef(
    _ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef
):
    pass


_ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)


class ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef(
    _ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef
):
    pass


_ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef",
    {"ManifestS3Uri": str},
    total=False,
)


class ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef(
    _ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef",
    {"S3DataSource": ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef},
    total=False,
)


class ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef(
    _ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef
):
    pass


_ClientDescribeLabelingJobResponseInputConfigTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseInputConfigTypeDef",
    {
        "DataSource": ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef,
        "DataAttributes": ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef,
    },
    total=False,
)


class ClientDescribeLabelingJobResponseInputConfigTypeDef(
    _ClientDescribeLabelingJobResponseInputConfigTypeDef
):
    pass


_ClientDescribeLabelingJobResponseLabelCountersTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseLabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)


class ClientDescribeLabelingJobResponseLabelCountersTypeDef(
    _ClientDescribeLabelingJobResponseLabelCountersTypeDef
):
    pass


_ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef",
    {"VolumeKmsKeyId": str},
    total=False,
)


class ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef(
    _ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef
):
    pass


_ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef",
    {
        "LabelingJobAlgorithmSpecificationArn": str,
        "InitialActiveLearningModelArn": str,
        "LabelingJobResourceConfig": ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef,
    },
    total=False,
)


class ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef(
    _ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef
):
    pass


_ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef",
    {"OutputDatasetS3Uri": str, "FinalActiveLearningModelArn": str},
    total=False,
)


class ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef(
    _ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef
):
    pass


_ClientDescribeLabelingJobResponseOutputConfigTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseOutputConfigTypeDef",
    {"S3OutputPath": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeLabelingJobResponseOutputConfigTypeDef(
    _ClientDescribeLabelingJobResponseOutputConfigTypeDef
):
    pass


_ClientDescribeLabelingJobResponseStoppingConditionsTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseStoppingConditionsTypeDef",
    {"MaxHumanLabeledObjectCount": int, "MaxPercentageOfInputDatasetLabeled": int},
    total=False,
)


class ClientDescribeLabelingJobResponseStoppingConditionsTypeDef(
    _ClientDescribeLabelingJobResponseStoppingConditionsTypeDef
):
    pass


_ClientDescribeLabelingJobResponseTagsTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeLabelingJobResponseTagsTypeDef(_ClientDescribeLabelingJobResponseTagsTypeDef):
    pass


_ClientDescribeLabelingJobResponseTypeDef = TypedDict(
    "_ClientDescribeLabelingJobResponseTypeDef",
    {
        "LabelingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "LabelCounters": ClientDescribeLabelingJobResponseLabelCountersTypeDef,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "JobReferenceCode": str,
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "LabelAttributeName": str,
        "InputConfig": ClientDescribeLabelingJobResponseInputConfigTypeDef,
        "OutputConfig": ClientDescribeLabelingJobResponseOutputConfigTypeDef,
        "RoleArn": str,
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": ClientDescribeLabelingJobResponseStoppingConditionsTypeDef,
        "LabelingJobAlgorithmsConfig": ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef,
        "HumanTaskConfig": ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef,
        "Tags": List[ClientDescribeLabelingJobResponseTagsTypeDef],
        "LabelingJobOutput": ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef,
    },
    total=False,
)


class ClientDescribeLabelingJobResponseTypeDef(_ClientDescribeLabelingJobResponseTypeDef):
    """
    - *(dict) --*

      - **LabelingJobStatus** *(string) --*

        The processing status of the labeling job.
    """


_ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)


class ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef(
    _ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef
):
    pass


_ClientDescribeModelPackageResponseInferenceSpecificationTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseInferenceSpecificationTypeDef",
    {
        "Containers": List[
            ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef
        ],
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)


class ClientDescribeModelPackageResponseInferenceSpecificationTypeDef(
    _ClientDescribeModelPackageResponseInferenceSpecificationTypeDef
):
    pass


_ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef",
    {
        "Name": str,
        "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"],
        "FailureReason": str,
    },
    total=False,
)


class ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef(
    _ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef
):
    pass


_ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef",
    {
        "Name": str,
        "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"],
        "FailureReason": str,
    },
    total=False,
)


class ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef(
    _ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef
):
    pass


_ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef",
    {
        "ValidationStatuses": List[
            ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef
        ],
        "ImageScanStatuses": List[
            ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef(
    _ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef
):
    pass


_ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef",
    {"ModelDataUrl": str, "AlgorithmName": str},
    total=False,
)


class ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef(
    _ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef
):
    pass


_ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef",
    {
        "SourceAlgorithms": List[
            ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef(
    _ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef
):
    pass


_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)


class ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef(
    _ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
):
    pass


_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
    },
    total=False,
)


class ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef(
    _ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef
):
    pass


_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    {
        "DataSource": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)


class ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef(
    _ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef
):
    pass


_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)


class ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef(
    _ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef
):
    pass


_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef(
    _ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef
):
    pass


_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef,
        "TransformOutput": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef,
        "TransformResources": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef,
    },
    total=False,
)


class ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef(
    _ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef
):
    pass


_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef,
    },
    total=False,
)


class ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef(
    _ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef
):
    pass


_ClientDescribeModelPackageResponseValidationSpecificationTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List[
            ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeModelPackageResponseValidationSpecificationTypeDef(
    _ClientDescribeModelPackageResponseValidationSpecificationTypeDef
):
    pass


_ClientDescribeModelPackageResponseTypeDef = TypedDict(
    "_ClientDescribeModelPackageResponseTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": ClientDescribeModelPackageResponseInferenceSpecificationTypeDef,
        "SourceAlgorithmSpecification": ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef,
        "ValidationSpecification": ClientDescribeModelPackageResponseValidationSpecificationTypeDef,
        "ModelPackageStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
        "ModelPackageStatusDetails": ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef,
        "CertifyForMarketplace": bool,
    },
    total=False,
)


class ClientDescribeModelPackageResponseTypeDef(_ClientDescribeModelPackageResponseTypeDef):
    """
    - *(dict) --*

      - **ModelPackageName** *(string) --*

        The name of the model package being described.
    """


_ClientDescribeModelResponseContainersTypeDef = TypedDict(
    "_ClientDescribeModelResponseContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)


class ClientDescribeModelResponseContainersTypeDef(_ClientDescribeModelResponseContainersTypeDef):
    pass


_ClientDescribeModelResponsePrimaryContainerTypeDef = TypedDict(
    "_ClientDescribeModelResponsePrimaryContainerTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)


class ClientDescribeModelResponsePrimaryContainerTypeDef(
    _ClientDescribeModelResponsePrimaryContainerTypeDef
):
    pass


_ClientDescribeModelResponseVpcConfigTypeDef = TypedDict(
    "_ClientDescribeModelResponseVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeModelResponseVpcConfigTypeDef(_ClientDescribeModelResponseVpcConfigTypeDef):
    pass


_ClientDescribeModelResponseTypeDef = TypedDict(
    "_ClientDescribeModelResponseTypeDef",
    {
        "ModelName": str,
        "PrimaryContainer": ClientDescribeModelResponsePrimaryContainerTypeDef,
        "Containers": List[ClientDescribeModelResponseContainersTypeDef],
        "ExecutionRoleArn": str,
        "VpcConfig": ClientDescribeModelResponseVpcConfigTypeDef,
        "CreationTime": datetime,
        "ModelArn": str,
        "EnableNetworkIsolation": bool,
    },
    total=False,
)


class ClientDescribeModelResponseTypeDef(_ClientDescribeModelResponseTypeDef):
    """
    - *(dict) --*

      - **ModelName** *(string) --*

        Name of the Amazon SageMaker model.
    """


_ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef = TypedDict(
    "_ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef",
    {"Content": str},
    total=False,
)


class ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef(
    _ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef
):
    pass


_ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef = TypedDict(
    "_ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef",
    {"Content": str},
    total=False,
)


class ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef(
    _ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef
):
    pass


_ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef = TypedDict(
    "_ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": List[ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef],
        "OnStart": List[ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef(
    _ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef
):
    """
    - *(dict) --*

      - **NotebookInstanceLifecycleConfigArn** *(string) --*

        The Amazon Resource Name (ARN) of the lifecycle configuration.
    """


_ClientDescribeNotebookInstanceResponseTypeDef = TypedDict(
    "_ClientDescribeNotebookInstanceResponseTypeDef",
    {
        "NotebookInstanceArn": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ],
        "FailureReason": str,
        "Url": str,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ],
        "SubnetId": str,
        "SecurityGroups": List[str],
        "RoleArn": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DirectInternetAccess": Literal["Enabled", "Disabled"],
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[
            Literal[
                "ml.eia1.medium",
                "ml.eia1.large",
                "ml.eia1.xlarge",
                "ml.eia2.medium",
                "ml.eia2.large",
                "ml.eia2.xlarge",
            ]
        ],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": Literal["Enabled", "Disabled"],
    },
    total=False,
)


class ClientDescribeNotebookInstanceResponseTypeDef(_ClientDescribeNotebookInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **NotebookInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the notebook instance.
    """


_ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef = TypedDict(
    "_ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef",
    {
        "WorkteamArn": str,
        "MarketplaceTitle": str,
        "SellerName": str,
        "MarketplaceDescription": str,
        "ListingId": str,
    },
    total=False,
)


class ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef(
    _ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef
):
    """
    - **SubscribedWorkteam** *(dict) --*

      A ``Workteam`` instance that contains information about the work team.
      - **WorkteamArn** *(string) --*

        The Amazon Resource Name (ARN) of the vendor that you have subscribed.
    """


_ClientDescribeSubscribedWorkteamResponseTypeDef = TypedDict(
    "_ClientDescribeSubscribedWorkteamResponseTypeDef",
    {"SubscribedWorkteam": ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef},
    total=False,
)


class ClientDescribeSubscribedWorkteamResponseTypeDef(
    _ClientDescribeSubscribedWorkteamResponseTypeDef
):
    """
    - *(dict) --*

      - **SubscribedWorkteam** *(dict) --*

        A ``Workteam`` instance that contains information about the work team.
        - **WorkteamArn** *(string) --*

          The Amazon Resource Name (ARN) of the vendor that you have subscribed.
    """


_ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)


class ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef(
    _ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef
):
    pass


_ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "MetricDefinitions": List[
            ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef(
    _ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef
):
    pass


_ClientDescribeTrainingJobResponseCheckpointConfigTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)


class ClientDescribeTrainingJobResponseCheckpointConfigTypeDef(
    _ClientDescribeTrainingJobResponseCheckpointConfigTypeDef
):
    pass


_ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef",
    {"MetricName": str, "Value": Any, "Timestamp": datetime},
    total=False,
)


class ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef(
    _ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef
):
    pass


_ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)


class ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef(
    _ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef
):
    pass


_ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef(
    _ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)


class ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef(
    _ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef
):
    pass


_ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)


class ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef(
    _ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef
):
    pass


_ClientDescribeTrainingJobResponseInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class ClientDescribeTrainingJobResponseInputDataConfigTypeDef(
    _ClientDescribeTrainingJobResponseInputDataConfigTypeDef
):
    pass


_ClientDescribeTrainingJobResponseModelArtifactsTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseModelArtifactsTypeDef",
    {"S3ModelArtifacts": str},
    total=False,
)


class ClientDescribeTrainingJobResponseModelArtifactsTypeDef(
    _ClientDescribeTrainingJobResponseModelArtifactsTypeDef
):
    pass


_ClientDescribeTrainingJobResponseOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)


class ClientDescribeTrainingJobResponseOutputDataConfigTypeDef(
    _ClientDescribeTrainingJobResponseOutputDataConfigTypeDef
):
    pass


_ClientDescribeTrainingJobResponseResourceConfigTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientDescribeTrainingJobResponseResourceConfigTypeDef(
    _ClientDescribeTrainingJobResponseResourceConfigTypeDef
):
    pass


_ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef",
    {
        "Status": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)


class ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef(
    _ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef
):
    pass


_ClientDescribeTrainingJobResponseStoppingConditionTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientDescribeTrainingJobResponseStoppingConditionTypeDef(
    _ClientDescribeTrainingJobResponseStoppingConditionTypeDef
):
    pass


_ClientDescribeTrainingJobResponseVpcConfigTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeTrainingJobResponseVpcConfigTypeDef(
    _ClientDescribeTrainingJobResponseVpcConfigTypeDef
):
    pass


_ClientDescribeTrainingJobResponseTypeDef = TypedDict(
    "_ClientDescribeTrainingJobResponseTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "ModelArtifacts": ClientDescribeTrainingJobResponseModelArtifactsTypeDef,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[ClientDescribeTrainingJobResponseInputDataConfigTypeDef],
        "OutputDataConfig": ClientDescribeTrainingJobResponseOutputDataConfigTypeDef,
        "ResourceConfig": ClientDescribeTrainingJobResponseResourceConfigTypeDef,
        "VpcConfig": ClientDescribeTrainingJobResponseVpcConfigTypeDef,
        "StoppingCondition": ClientDescribeTrainingJobResponseStoppingConditionTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[
            ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef
        ],
        "FinalMetricDataList": List[ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientDescribeTrainingJobResponseCheckpointConfigTypeDef,
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
    },
    total=False,
)


class ClientDescribeTrainingJobResponseTypeDef(_ClientDescribeTrainingJobResponseTypeDef):
    """
    - *(dict) --*

      - **TrainingJobName** *(string) --*

        Name of the model training job.
    """


_ClientDescribeTransformJobResponseDataProcessingTypeDef = TypedDict(
    "_ClientDescribeTransformJobResponseDataProcessingTypeDef",
    {"InputFilter": str, "OutputFilter": str, "JoinSource": Literal["Input", "None"]},
    total=False,
)


class ClientDescribeTransformJobResponseDataProcessingTypeDef(
    _ClientDescribeTransformJobResponseDataProcessingTypeDef
):
    pass


_ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)


class ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef(
    _ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef
):
    pass


_ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef = TypedDict(
    "_ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef",
    {"S3DataSource": ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef},
    total=False,
)


class ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef(
    _ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef
):
    pass


_ClientDescribeTransformJobResponseTransformInputTypeDef = TypedDict(
    "_ClientDescribeTransformJobResponseTransformInputTypeDef",
    {
        "DataSource": ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)


class ClientDescribeTransformJobResponseTransformInputTypeDef(
    _ClientDescribeTransformJobResponseTransformInputTypeDef
):
    pass


_ClientDescribeTransformJobResponseTransformOutputTypeDef = TypedDict(
    "_ClientDescribeTransformJobResponseTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)


class ClientDescribeTransformJobResponseTransformOutputTypeDef(
    _ClientDescribeTransformJobResponseTransformOutputTypeDef
):
    pass


_ClientDescribeTransformJobResponseTransformResourcesTypeDef = TypedDict(
    "_ClientDescribeTransformJobResponseTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientDescribeTransformJobResponseTransformResourcesTypeDef(
    _ClientDescribeTransformJobResponseTransformResourcesTypeDef
):
    pass


_ClientDescribeTransformJobResponseTypeDef = TypedDict(
    "_ClientDescribeTransformJobResponseTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientDescribeTransformJobResponseTransformInputTypeDef,
        "TransformOutput": ClientDescribeTransformJobResponseTransformOutputTypeDef,
        "TransformResources": ClientDescribeTransformJobResponseTransformResourcesTypeDef,
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "DataProcessing": ClientDescribeTransformJobResponseDataProcessingTypeDef,
    },
    total=False,
)


class ClientDescribeTransformJobResponseTypeDef(_ClientDescribeTransformJobResponseTypeDef):
    """
    - *(dict) --*

      - **TransformJobName** *(string) --*

        The name of the transform job.
    """


_ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str, "UserGroup": str, "ClientId": str},
    total=False,
)


class ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef(
    _ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
):
    pass


_ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef = TypedDict(
    "_ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)


class ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef(
    _ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef
):
    pass


_ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef = TypedDict(
    "_ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)


class ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef(
    _ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef
):
    pass


_ClientDescribeWorkteamResponseWorkteamTypeDef = TypedDict(
    "_ClientDescribeWorkteamResponseWorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef],
        "WorkteamArn": str,
        "ProductListingIds": List[str],
        "Description": str,
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeWorkteamResponseWorkteamTypeDef(_ClientDescribeWorkteamResponseWorkteamTypeDef):
    """
    - **Workteam** *(dict) --*

      A ``Workteam`` instance that contains information about the work team.
      - **WorkteamName** *(string) --*

        The name of the work team.
    """


_ClientDescribeWorkteamResponseTypeDef = TypedDict(
    "_ClientDescribeWorkteamResponseTypeDef",
    {"Workteam": ClientDescribeWorkteamResponseWorkteamTypeDef},
    total=False,
)


class ClientDescribeWorkteamResponseTypeDef(_ClientDescribeWorkteamResponseTypeDef):
    """
    - *(dict) --*

      - **Workteam** *(dict) --*

        A ``Workteam`` instance that contains information about the work team.
        - **WorkteamName** *(string) --*

          The name of the work team.
    """


_ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef = TypedDict(
    "_ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef",
    {"PropertyName": str},
    total=False,
)


class ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef(
    _ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef
):
    """
    - *(dict) --*

      A property name returned from a ``GetSearchSuggestions`` call that specifies a value in the
      ``PropertyNameQuery`` field.
      - **PropertyName** *(string) --*

        A suggested property name based on what you entered in the search textbox in the Amazon
        SageMaker console.
    """


_ClientGetSearchSuggestionsResponseTypeDef = TypedDict(
    "_ClientGetSearchSuggestionsResponseTypeDef",
    {
        "PropertyNameSuggestions": List[
            ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef
        ]
    },
    total=False,
)


class ClientGetSearchSuggestionsResponseTypeDef(_ClientGetSearchSuggestionsResponseTypeDef):
    """
    - *(dict) --*

      - **PropertyNameSuggestions** *(list) --*

        A list of property names for a ``Resource`` that match a ``SuggestionQuery`` .
        - *(dict) --*

          A property name returned from a ``GetSearchSuggestions`` call that specifies a value in
          the ``PropertyNameQuery`` field.
          - **PropertyName** *(string) --*

            A suggested property name based on what you entered in the search textbox in the Amazon
            SageMaker console.
    """


_ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef = TypedDict(
    "_ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef", {"PropertyNameHint": str}
)


class ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef(
    _ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef
):
    """
    - **PropertyNameQuery** *(dict) --*

      A type of ``SuggestionQuery`` . Defines a property name hint. Only property names that match
      the specified hint are included in the response.
      - **PropertyNameHint** *(string) --***[REQUIRED]**

        Text that is part of a property's name. The property names of hyperparameter, metric, and
        tag key names that begin with the specified text in the ``PropertyNameHint`` .
    """


_ClientGetSearchSuggestionsSuggestionQueryTypeDef = TypedDict(
    "_ClientGetSearchSuggestionsSuggestionQueryTypeDef",
    {"PropertyNameQuery": ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef},
    total=False,
)


class ClientGetSearchSuggestionsSuggestionQueryTypeDef(
    _ClientGetSearchSuggestionsSuggestionQueryTypeDef
):
    """
    Limits the property names that are included in the response.
    - **PropertyNameQuery** *(dict) --*

      A type of ``SuggestionQuery`` . Defines a property name hint. Only property names that match
      the specified hint are included in the response.
      - **PropertyNameHint** *(string) --***[REQUIRED]**

        Text that is part of a property's name. The property names of hyperparameter, metric, and
        tag key names that begin with the specified text in the ``PropertyNameHint`` .
    """


_ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef = TypedDict(
    "_ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "AlgorithmStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
    total=False,
)


class ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef(
    _ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef
):
    """
    - *(dict) --*

      Provides summary information about an algorithm.
      - **AlgorithmName** *(string) --*

        The name of the algorithm that is described by the summary.
    """


_ClientListAlgorithmsResponseTypeDef = TypedDict(
    "_ClientListAlgorithmsResponseTypeDef",
    {
        "AlgorithmSummaryList": List[ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListAlgorithmsResponseTypeDef(_ClientListAlgorithmsResponseTypeDef):
    """
    - *(dict) --*

      - **AlgorithmSummaryList** *(list) --*

        >An array of ``AlgorithmSummary`` objects, each of which lists an algorithm.
        - *(dict) --*

          Provides summary information about an algorithm.
          - **AlgorithmName** *(string) --*

            The name of the algorithm that is described by the summary.
    """


_ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef = TypedDict(
    "_ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef",
    {"RepositoryUrl": str, "Branch": str, "SecretArn": str},
    total=False,
)


class ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef(
    _ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef
):
    pass


_ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef = TypedDict(
    "_ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef,
    },
    total=False,
)


class ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef(
    _ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef
):
    """
    - *(dict) --*

      Specifies summary information about a Git repository.
      - **CodeRepositoryName** *(string) --*

        The name of the Git repository.
    """


_ClientListCodeRepositoriesResponseTypeDef = TypedDict(
    "_ClientListCodeRepositoriesResponseTypeDef",
    {
        "CodeRepositorySummaryList": List[
            ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCodeRepositoriesResponseTypeDef(_ClientListCodeRepositoriesResponseTypeDef):
    """
    - *(dict) --*

      - **CodeRepositorySummaryList** *(list) --*

        Gets a list of summaries of the Git repositories. Each summary specifies the following
        values for the repository:
        * Name
        * Amazon Resource Name (ARN)
        * Creation time
        * Last modified time
        * Configuration information, including the URL location of the repository and the ARN of the
        AWS Secrets Manager secret that contains the credentials used to access the repository.
        - *(dict) --*

          Specifies summary information about a Git repository.
          - **CodeRepositoryName** *(string) --*

            The name of the Git repository.
    """


_ClientListCompilationJobsResponseCompilationJobSummariesTypeDef = TypedDict(
    "_ClientListCompilationJobsResponseCompilationJobSummariesTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "CompilationTargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "rasp3b",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
        ],
        "LastModifiedTime": datetime,
        "CompilationJobStatus": Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ],
    },
    total=False,
)


class ClientListCompilationJobsResponseCompilationJobSummariesTypeDef(
    _ClientListCompilationJobsResponseCompilationJobSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of a model compilation job.
      - **CompilationJobName** *(string) --*

        The name of the model compilation job that you want a summary for.
    """


_ClientListCompilationJobsResponseTypeDef = TypedDict(
    "_ClientListCompilationJobsResponseTypeDef",
    {
        "CompilationJobSummaries": List[
            ClientListCompilationJobsResponseCompilationJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCompilationJobsResponseTypeDef(_ClientListCompilationJobsResponseTypeDef):
    """
    - *(dict) --*

      - **CompilationJobSummaries** *(list) --*

        An array of  CompilationJobSummary objects, each describing a model compilation job.
        - *(dict) --*

          A summary of a model compilation job.
          - **CompilationJobName** *(string) --*

            The name of the model compilation job that you want a summary for.
    """


_ClientListEndpointConfigsResponseEndpointConfigsTypeDef = TypedDict(
    "_ClientListEndpointConfigsResponseEndpointConfigsTypeDef",
    {"EndpointConfigName": str, "EndpointConfigArn": str, "CreationTime": datetime},
    total=False,
)


class ClientListEndpointConfigsResponseEndpointConfigsTypeDef(
    _ClientListEndpointConfigsResponseEndpointConfigsTypeDef
):
    """
    - *(dict) --*

      Provides summary information for an endpoint configuration.
      - **EndpointConfigName** *(string) --*

        The name of the endpoint configuration.
    """


_ClientListEndpointConfigsResponseTypeDef = TypedDict(
    "_ClientListEndpointConfigsResponseTypeDef",
    {
        "EndpointConfigs": List[ClientListEndpointConfigsResponseEndpointConfigsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEndpointConfigsResponseTypeDef(_ClientListEndpointConfigsResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointConfigs** *(list) --*

        An array of endpoint configurations.
        - *(dict) --*

          Provides summary information for an endpoint configuration.
          - **EndpointConfigName** *(string) --*

            The name of the endpoint configuration.
    """


_ClientListEndpointsResponseEndpointsTypeDef = TypedDict(
    "_ClientListEndpointsResponseEndpointsTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ],
    },
    total=False,
)


class ClientListEndpointsResponseEndpointsTypeDef(_ClientListEndpointsResponseEndpointsTypeDef):
    """
    - *(dict) --*

      Provides summary information for an endpoint.
      - **EndpointName** *(string) --*

        The name of the endpoint.
    """


_ClientListEndpointsResponseTypeDef = TypedDict(
    "_ClientListEndpointsResponseTypeDef",
    {"Endpoints": List[ClientListEndpointsResponseEndpointsTypeDef], "NextToken": str},
    total=False,
)


class ClientListEndpointsResponseTypeDef(_ClientListEndpointsResponseTypeDef):
    """
    - *(dict) --*

      - **Endpoints** *(list) --*

        An array or endpoint objects.
        - *(dict) --*

          Provides summary information for an endpoint.
          - **EndpointName** *(string) --*

            The name of the endpoint.
    """


_ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef = TypedDict(
    "_ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef",
    {"Succeeded": int, "Pending": int, "Failed": int},
    total=False,
)


class ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef(
    _ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef
):
    pass


_ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef = TypedDict(
    "_ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef",
    {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int},
    total=False,
)


class ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef(
    _ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef
):
    pass


_ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef = TypedDict(
    "_ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)


class ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef(
    _ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef
):
    pass


_ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef = TypedDict(
    "_ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": Literal[
            "Completed", "InProgress", "Failed", "Stopped", "Stopping"
        ],
        "Strategy": Literal["Bayesian", "Random"],
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef,
        "ResourceLimits": ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef,
    },
    total=False,
)


class ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef(
    _ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef
):
    """
    - *(dict) --*

      Provides summary information about a hyperparameter tuning job.
      - **HyperParameterTuningJobName** *(string) --*

        The name of the tuning job.
    """


_ClientListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "_ClientListHyperParameterTuningJobsResponseTypeDef",
    {
        "HyperParameterTuningJobSummaries": List[
            ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListHyperParameterTuningJobsResponseTypeDef(
    _ClientListHyperParameterTuningJobsResponseTypeDef
):
    """
    - *(dict) --*

      - **HyperParameterTuningJobSummaries** *(list) --*

        A list of  HyperParameterTuningJobSummary objects that describe the tuning jobs that the
        ``ListHyperParameterTuningJobs`` request returned.
        - *(dict) --*

          Provides summary information about a hyperparameter tuning job.
          - **HyperParameterTuningJobName** *(string) --*

            The name of the tuning job.
    """


_ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef = TypedDict(
    "_ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef",
    {"HumanLabeled": int, "PendingHuman": int, "Total": int},
    total=False,
)


class ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef(
    _ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef
):
    pass


_ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef = TypedDict(
    "_ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef",
    {
        "LabelingJobName": str,
        "JobReferenceCode": str,
        "WorkRequesterAccountId": str,
        "CreationTime": datetime,
        "LabelCounters": ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef,
        "NumberOfHumanWorkersPerDataObject": int,
    },
    total=False,
)


class ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef(
    _ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef
):
    """
    - *(dict) --*

      Provides summary information for a work team.
      - **LabelingJobName** *(string) --*

        The name of the labeling job that the work team is assigned to.
    """


_ClientListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "_ClientListLabelingJobsForWorkteamResponseTypeDef",
    {
        "LabelingJobSummaryList": List[
            ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListLabelingJobsForWorkteamResponseTypeDef(
    _ClientListLabelingJobsForWorkteamResponseTypeDef
):
    """
    - *(dict) --*

      - **LabelingJobSummaryList** *(list) --*

        An array of ``LabelingJobSummary`` objects, each describing a labeling job.
        - *(dict) --*

          Provides summary information for a work team.
          - **LabelingJobName** *(string) --*

            The name of the labeling job that the work team is assigned to.
    """


_ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef = TypedDict(
    "_ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)


class ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef(
    _ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef
):
    pass


_ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef",
    {"ManifestS3Uri": str},
    total=False,
)


class ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef(
    _ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef = TypedDict(
    "_ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef
    },
    total=False,
)


class ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef(
    _ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef
):
    pass


_ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef = TypedDict(
    "_ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef",
    {
        "DataSource": ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef,
        "DataAttributes": ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef,
    },
    total=False,
)


class ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef(
    _ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef
):
    pass


_ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef = TypedDict(
    "_ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)


class ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef(
    _ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef
):
    pass


_ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef = TypedDict(
    "_ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef",
    {"OutputDatasetS3Uri": str, "FinalActiveLearningModelArn": str},
    total=False,
)


class ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef(
    _ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef
):
    pass


_ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef = TypedDict(
    "_ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "LabelCounters": ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef,
        "WorkteamArn": str,
        "PreHumanTaskLambdaArn": str,
        "AnnotationConsolidationLambdaArn": str,
        "FailureReason": str,
        "LabelingJobOutput": ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef,
        "InputConfig": ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef,
    },
    total=False,
)


class ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef(
    _ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef
):
    """
    - *(dict) --*

      Provides summary information about a labeling job.
      - **LabelingJobName** *(string) --*

        The name of the labeling job.
    """


_ClientListLabelingJobsResponseTypeDef = TypedDict(
    "_ClientListLabelingJobsResponseTypeDef",
    {
        "LabelingJobSummaryList": List[ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListLabelingJobsResponseTypeDef(_ClientListLabelingJobsResponseTypeDef):
    """
    - *(dict) --*

      - **LabelingJobSummaryList** *(list) --*

        An array of ``LabelingJobSummary`` objects, each describing a labeling job.
        - *(dict) --*

          Provides summary information about a labeling job.
          - **LabelingJobName** *(string) --*

            The name of the labeling job.
    """


_ClientListModelPackagesResponseModelPackageSummaryListTypeDef = TypedDict(
    "_ClientListModelPackagesResponseModelPackageSummaryListTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "ModelPackageStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
    total=False,
)


class ClientListModelPackagesResponseModelPackageSummaryListTypeDef(
    _ClientListModelPackagesResponseModelPackageSummaryListTypeDef
):
    """
    - *(dict) --*

      Provides summary information about a model package.
      - **ModelPackageName** *(string) --*

        The name of the model package.
    """


_ClientListModelPackagesResponseTypeDef = TypedDict(
    "_ClientListModelPackagesResponseTypeDef",
    {
        "ModelPackageSummaryList": List[
            ClientListModelPackagesResponseModelPackageSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListModelPackagesResponseTypeDef(_ClientListModelPackagesResponseTypeDef):
    """
    - *(dict) --*

      - **ModelPackageSummaryList** *(list) --*

        An array of ``ModelPackageSummary`` objects, each of which lists a model package.
        - *(dict) --*

          Provides summary information about a model package.
          - **ModelPackageName** *(string) --*

            The name of the model package.
    """


_ClientListModelsResponseModelsTypeDef = TypedDict(
    "_ClientListModelsResponseModelsTypeDef",
    {"ModelName": str, "ModelArn": str, "CreationTime": datetime},
    total=False,
)


class ClientListModelsResponseModelsTypeDef(_ClientListModelsResponseModelsTypeDef):
    """
    - *(dict) --*

      Provides summary information about a model.
      - **ModelName** *(string) --*

        The name of the model that you want a summary for.
    """


_ClientListModelsResponseTypeDef = TypedDict(
    "_ClientListModelsResponseTypeDef",
    {"Models": List[ClientListModelsResponseModelsTypeDef], "NextToken": str},
    total=False,
)


class ClientListModelsResponseTypeDef(_ClientListModelsResponseTypeDef):
    """
    - *(dict) --*

      - **Models** *(list) --*

        An array of ``ModelSummary`` objects, each of which lists a model.
        - *(dict) --*

          Provides summary information about a model.
          - **ModelName** *(string) --*

            The name of the model that you want a summary for.
    """


_ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef = TypedDict(
    "_ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceLifecycleConfigArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef(
    _ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef
):
    pass


_ClientListNotebookInstanceLifecycleConfigsResponseTypeDef = TypedDict(
    "_ClientListNotebookInstanceLifecycleConfigsResponseTypeDef",
    {
        "NextToken": str,
        "NotebookInstanceLifecycleConfigs": List[
            ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef
        ],
    },
    total=False,
)


class ClientListNotebookInstanceLifecycleConfigsResponseTypeDef(
    _ClientListNotebookInstanceLifecycleConfigsResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the response is truncated, Amazon SageMaker returns this token. To get the next set of
        lifecycle configurations, use it in the next request.
    """


_ClientListNotebookInstancesResponseNotebookInstancesTypeDef = TypedDict(
    "_ClientListNotebookInstancesResponseNotebookInstancesTypeDef",
    {
        "NotebookInstanceName": str,
        "NotebookInstanceArn": str,
        "NotebookInstanceStatus": Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ],
        "Url": str,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
    },
    total=False,
)


class ClientListNotebookInstancesResponseNotebookInstancesTypeDef(
    _ClientListNotebookInstancesResponseNotebookInstancesTypeDef
):
    pass


_ClientListNotebookInstancesResponseTypeDef = TypedDict(
    "_ClientListNotebookInstancesResponseTypeDef",
    {
        "NextToken": str,
        "NotebookInstances": List[ClientListNotebookInstancesResponseNotebookInstancesTypeDef],
    },
    total=False,
)


class ClientListNotebookInstancesResponseTypeDef(_ClientListNotebookInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the response to the previous ``ListNotebookInstances`` request was truncated, Amazon
        SageMaker returns this token. To retrieve the next set of notebook instances, use the token
        in the next request.
    """


_ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef = TypedDict(
    "_ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef",
    {
        "WorkteamArn": str,
        "MarketplaceTitle": str,
        "SellerName": str,
        "MarketplaceDescription": str,
        "ListingId": str,
    },
    total=False,
)


class ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef(
    _ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef
):
    """
    - *(dict) --*

      Describes a work team of a vendor that does the a labelling job.
      - **WorkteamArn** *(string) --*

        The Amazon Resource Name (ARN) of the vendor that you have subscribed.
    """


_ClientListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "_ClientListSubscribedWorkteamsResponseTypeDef",
    {
        "SubscribedWorkteams": List[
            ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSubscribedWorkteamsResponseTypeDef(_ClientListSubscribedWorkteamsResponseTypeDef):
    """
    - *(dict) --*

      - **SubscribedWorkteams** *(list) --*

        An array of ``Workteam`` objects, each describing a work team.
        - *(dict) --*

          Describes a work team of a vendor that does the a labelling job.
          - **WorkteamArn** *(string) --*

            The Amazon Resource Name (ARN) of the vendor that you have subscribed.
    """


_ClientListTagsResponseTagsTypeDef = TypedDict(
    "_ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagsTypeDef(_ClientListTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --*

        The tag key.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        An array of ``Tag`` objects, each with a tag key and a value.
        - *(dict) --*

          Describes a tag.
          - **Key** *(string) --*

            The tag key.
    """


_ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str, "Value": Any},
    total=False,
)


class ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef
):
    pass


_ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef = TypedDict(
    "_ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobName": str,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "TunedHyperParameters": Dict[str, str],
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)


class ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef(
    _ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef
):
    """
    - *(dict) --*

      Specifies summary information about a training job.
      - **TrainingJobName** *(string) --*

        The name of the training job.
    """


_ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {
        "TrainingJobSummaries": List[
            ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef(
    _ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef
):
    """
    - *(dict) --*

      - **TrainingJobSummaries** *(list) --*

        A list of  TrainingJobSummary objects that describe the training jobs that the
        ``ListTrainingJobsForHyperParameterTuningJob`` request returned.
        - *(dict) --*

          Specifies summary information about a training job.
          - **TrainingJobName** *(string) --*

            The name of the training job.
    """


_ClientListTrainingJobsResponseTrainingJobSummariesTypeDef = TypedDict(
    "_ClientListTrainingJobsResponseTrainingJobSummariesTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
    },
    total=False,
)


class ClientListTrainingJobsResponseTrainingJobSummariesTypeDef(
    _ClientListTrainingJobsResponseTrainingJobSummariesTypeDef
):
    """
    - *(dict) --*

      Provides summary information about a training job.
      - **TrainingJobName** *(string) --*

        The name of the training job that you want a summary for.
    """


_ClientListTrainingJobsResponseTypeDef = TypedDict(
    "_ClientListTrainingJobsResponseTypeDef",
    {
        "TrainingJobSummaries": List[ClientListTrainingJobsResponseTrainingJobSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTrainingJobsResponseTypeDef(_ClientListTrainingJobsResponseTypeDef):
    """
    - *(dict) --*

      - **TrainingJobSummaries** *(list) --*

        An array of ``TrainingJobSummary`` objects, each listing a training job.
        - *(dict) --*

          Provides summary information about a training job.
          - **TrainingJobName** *(string) --*

            The name of the training job that you want a summary for.
    """


_ClientListTransformJobsResponseTransformJobSummariesTypeDef = TypedDict(
    "_ClientListTransformJobsResponseTransformJobSummariesTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformEndTime": datetime,
        "LastModifiedTime": datetime,
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "FailureReason": str,
    },
    total=False,
)


class ClientListTransformJobsResponseTransformJobSummariesTypeDef(
    _ClientListTransformJobsResponseTransformJobSummariesTypeDef
):
    """
    - *(dict) --*

      Provides a summary of a transform job. Multiple ``TransformJobSummary`` objects are returned
      as a list after in response to a  ListTransformJobs call.
      - **TransformJobName** *(string) --*

        The name of the transform job.
    """


_ClientListTransformJobsResponseTypeDef = TypedDict(
    "_ClientListTransformJobsResponseTypeDef",
    {
        "TransformJobSummaries": List[ClientListTransformJobsResponseTransformJobSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTransformJobsResponseTypeDef(_ClientListTransformJobsResponseTypeDef):
    """
    - *(dict) --*

      - **TransformJobSummaries** *(list) --*

        An array of ``TransformJobSummary`` objects.
        - *(dict) --*

          Provides a summary of a transform job. Multiple ``TransformJobSummary`` objects are
          returned as a list after in response to a  ListTransformJobs call.
          - **TransformJobName** *(string) --*

            The name of the transform job.
    """


_ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str, "UserGroup": str, "ClientId": str},
    total=False,
)


class ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef(
    _ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef
):
    pass


_ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef = TypedDict(
    "_ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)


class ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef(
    _ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef
):
    pass


_ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef = TypedDict(
    "_ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)


class ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef(
    _ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef
):
    pass


_ClientListWorkteamsResponseWorkteamsTypeDef = TypedDict(
    "_ClientListWorkteamsResponseWorkteamsTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef],
        "WorkteamArn": str,
        "ProductListingIds": List[str],
        "Description": str,
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef,
    },
    total=False,
)


class ClientListWorkteamsResponseWorkteamsTypeDef(_ClientListWorkteamsResponseWorkteamsTypeDef):
    """
    - *(dict) --*

      Provides details about a labeling work team.
      - **WorkteamName** *(string) --*

        The name of the work team.
    """


_ClientListWorkteamsResponseTypeDef = TypedDict(
    "_ClientListWorkteamsResponseTypeDef",
    {"Workteams": List[ClientListWorkteamsResponseWorkteamsTypeDef], "NextToken": str},
    total=False,
)


class ClientListWorkteamsResponseTypeDef(_ClientListWorkteamsResponseTypeDef):
    """
    - *(dict) --*

      - **Workteams** *(list) --*

        An array of ``Workteam`` objects, each describing a work team.
        - *(dict) --*

          Provides details about a labeling work team.
          - **WorkteamName** *(string) --*

            The name of the work team.
    """


_ClientRenderUiTemplateResponseErrorsTypeDef = TypedDict(
    "_ClientRenderUiTemplateResponseErrorsTypeDef", {"Code": str, "Message": str}, total=False
)


class ClientRenderUiTemplateResponseErrorsTypeDef(_ClientRenderUiTemplateResponseErrorsTypeDef):
    pass


_ClientRenderUiTemplateResponseTypeDef = TypedDict(
    "_ClientRenderUiTemplateResponseTypeDef",
    {"RenderedContent": str, "Errors": List[ClientRenderUiTemplateResponseErrorsTypeDef]},
    total=False,
)


class ClientRenderUiTemplateResponseTypeDef(_ClientRenderUiTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **RenderedContent** *(string) --*

        A Liquid template that renders the HTML for the worker UI.
    """


_ClientRenderUiTemplateTaskTypeDef = TypedDict("_ClientRenderUiTemplateTaskTypeDef", {"Input": str})


class ClientRenderUiTemplateTaskTypeDef(_ClientRenderUiTemplateTaskTypeDef):
    """
    A ``RenderableTask`` object containing a representative task to render.
    - **Input** *(string) --***[REQUIRED]**

      A JSON object that contains values for the variables defined in the template. It is made
      available to the template under the substitution variable ``task.input`` . For example, if you
      define a variable ``task.input.text`` in your template, you can supply the variable in the
      JSON object as ``"text": "sample text"`` .
    """


_ClientRenderUiTemplateUiTemplateTypeDef = TypedDict(
    "_ClientRenderUiTemplateUiTemplateTypeDef", {"Content": str}
)


class ClientRenderUiTemplateUiTemplateTypeDef(_ClientRenderUiTemplateUiTemplateTypeDef):
    """
    A ``Template`` object containing the worker UI template to render.
    - **Content** *(string) --***[REQUIRED]**

      The content of the Liquid template for the worker user interface.
    """


_ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)


class ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef(
    _ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "MetricDefinitions": List[
            ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)


class ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef(
    _ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef",
    {"MetricName": str, "Value": Any, "Timestamp": datetime},
    total=False,
)


class ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef(
    _ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)


class ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef(
    _ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef(
    _ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)


class ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef(
    _ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)


class ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef(
    _ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef(
    _ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef",
    {"S3ModelArtifacts": str},
    total=False,
)


class ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef(
    _ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)


class ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef(
    _ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobResourceConfigTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientSearchResponseResultsTrainingJobResourceConfigTypeDef(
    _ClientSearchResponseResultsTrainingJobResourceConfigTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef",
    {
        "Status": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)


class ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef(
    _ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef(
    _ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobTagsTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientSearchResponseResultsTrainingJobTagsTypeDef(
    _ClientSearchResponseResultsTrainingJobTagsTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobVpcConfigTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientSearchResponseResultsTrainingJobVpcConfigTypeDef(
    _ClientSearchResponseResultsTrainingJobVpcConfigTypeDef
):
    pass


_ClientSearchResponseResultsTrainingJobTypeDef = TypedDict(
    "_ClientSearchResponseResultsTrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "ModelArtifacts": ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef],
        "OutputDataConfig": ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef,
        "ResourceConfig": ClientSearchResponseResultsTrainingJobResourceConfigTypeDef,
        "VpcConfig": ClientSearchResponseResultsTrainingJobVpcConfigTypeDef,
        "StoppingCondition": ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[
            ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef
        ],
        "FinalMetricDataList": List[
            ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef
        ],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "Tags": List[ClientSearchResponseResultsTrainingJobTagsTypeDef],
    },
    total=False,
)


class ClientSearchResponseResultsTrainingJobTypeDef(_ClientSearchResponseResultsTrainingJobTypeDef):
    """
    - **TrainingJob** *(dict) --*

      A ``TrainingJob`` object that is returned as part of a ``Search`` request.
      - **TrainingJobName** *(string) --*

        The name of the training job.
    """


_ClientSearchResponseResultsTypeDef = TypedDict(
    "_ClientSearchResponseResultsTypeDef",
    {"TrainingJob": ClientSearchResponseResultsTrainingJobTypeDef},
    total=False,
)


class ClientSearchResponseResultsTypeDef(_ClientSearchResponseResultsTypeDef):
    """
    - *(dict) --*

      An individual search result record that contains a single resource object.
      - **TrainingJob** *(dict) --*

        A ``TrainingJob`` object that is returned as part of a ``Search`` request.
        - **TrainingJobName** *(string) --*

          The name of the training job.
    """


_ClientSearchResponseTypeDef = TypedDict(
    "_ClientSearchResponseTypeDef",
    {"Results": List[ClientSearchResponseResultsTypeDef], "NextToken": str},
    total=False,
)


class ClientSearchResponseTypeDef(_ClientSearchResponseTypeDef):
    """
    - *(dict) --*

      - **Results** *(list) --*

        A list of ``SearchResult`` objects.
        - *(dict) --*

          An individual search result record that contains a single resource object.
          - **TrainingJob** *(dict) --*

            A ``TrainingJob`` object that is returned as part of a ``Search`` request.
            - **TrainingJobName** *(string) --*

              The name of the training job.
    """


_ClientSearchSearchExpressionFiltersTypeDef = TypedDict(
    "_ClientSearchSearchExpressionFiltersTypeDef",
    {
        "Name": str,
        "Operator": Literal[
            "Equals",
            "NotEquals",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "LessThan",
            "LessThanOrEqualTo",
            "Contains",
        ],
        "Value": str,
    },
    total=False,
)


class ClientSearchSearchExpressionFiltersTypeDef(_ClientSearchSearchExpressionFiltersTypeDef):
    """
    - *(dict) --*

      A conditional statement for a search expression that includes a resource property, a Boolean
      operator, and a value.
      If you don't specify an ``Operator`` and a ``Value`` , the filter searches for only the
      specified property. For example, defining a ``Filter`` for the ``FailureReason`` for the
      ``TrainingJob``  ``Resource`` searches for training job objects that have a value in the
      ``FailureReason`` field.
      If you specify a ``Value`` , but not an ``Operator`` , Amazon SageMaker uses the equals
      operator as the default.
      In search, there are several property types:

        Metrics
    """


_ClientSearchSearchExpressionNestedFiltersFiltersTypeDef = TypedDict(
    "_ClientSearchSearchExpressionNestedFiltersFiltersTypeDef",
    {
        "Name": str,
        "Operator": Literal[
            "Equals",
            "NotEquals",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "LessThan",
            "LessThanOrEqualTo",
            "Contains",
        ],
        "Value": str,
    },
    total=False,
)


class ClientSearchSearchExpressionNestedFiltersFiltersTypeDef(
    _ClientSearchSearchExpressionNestedFiltersFiltersTypeDef
):
    pass


_ClientSearchSearchExpressionNestedFiltersTypeDef = TypedDict(
    "_ClientSearchSearchExpressionNestedFiltersTypeDef",
    {
        "NestedPropertyName": str,
        "Filters": List[ClientSearchSearchExpressionNestedFiltersFiltersTypeDef],
    },
    total=False,
)


class ClientSearchSearchExpressionNestedFiltersTypeDef(
    _ClientSearchSearchExpressionNestedFiltersTypeDef
):
    pass


_ClientSearchSearchExpressionTypeDef = TypedDict(
    "_ClientSearchSearchExpressionTypeDef",
    {
        "Filters": List[ClientSearchSearchExpressionFiltersTypeDef],
        "NestedFilters": List[ClientSearchSearchExpressionNestedFiltersTypeDef],
        "SubExpressions": List[Any],
        "Operator": Literal["And", "Or"],
    },
    total=False,
)


class ClientSearchSearchExpressionTypeDef(_ClientSearchSearchExpressionTypeDef):
    """
    A Boolean conditional statement. Resource objects must satisfy this condition to be included in
    search results. You must provide at least one subexpression, filter, or nested filter. The
    maximum number of recursive ``SubExpressions`` , ``NestedFilters`` , and ``Filters`` that can be
    included in a ``SearchExpression`` object is 50.
    - **Filters** *(list) --*

      A list of filter objects.
      - *(dict) --*

        A conditional statement for a search expression that includes a resource property, a Boolean
        operator, and a value.
        If you don't specify an ``Operator`` and a ``Value`` , the filter searches for only the
        specified property. For example, defining a ``Filter`` for the ``FailureReason`` for the
        ``TrainingJob``  ``Resource`` searches for training job objects that have a value in the
        ``FailureReason`` field.
        If you specify a ``Value`` , but not an ``Operator`` , Amazon SageMaker uses the equals
        operator as the default.
        In search, there are several property types:

          Metrics
    """


_ClientUpdateCodeRepositoryGitConfigTypeDef = TypedDict(
    "_ClientUpdateCodeRepositoryGitConfigTypeDef", {"SecretArn": str}, total=False
)


class ClientUpdateCodeRepositoryGitConfigTypeDef(_ClientUpdateCodeRepositoryGitConfigTypeDef):
    """
    The configuration of the git repository, including the URL and the Amazon Resource Name (ARN) of
    the AWS Secrets Manager secret that contains the credentials used to access the repository. The
    secret must have a staging label of ``AWSCURRENT`` and must be in the following format:

      ``{"username": *UserName* , "password": *Password* }``
    """


_ClientUpdateCodeRepositoryResponseTypeDef = TypedDict(
    "_ClientUpdateCodeRepositoryResponseTypeDef", {"CodeRepositoryArn": str}, total=False
)


class ClientUpdateCodeRepositoryResponseTypeDef(_ClientUpdateCodeRepositoryResponseTypeDef):
    """
    - *(dict) --*

      - **CodeRepositoryArn** *(string) --*

        The ARN of the Git repository.
    """


_ClientUpdateEndpointResponseTypeDef = TypedDict(
    "_ClientUpdateEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)


class ClientUpdateEndpointResponseTypeDef(_ClientUpdateEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint.
    """


_RequiredClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef = TypedDict(
    "_RequiredClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef",
    {"VariantName": str},
)
_OptionalClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef = TypedDict(
    "_OptionalClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef",
    {"DesiredWeight": Any, "DesiredInstanceCount": int},
    total=False,
)


class ClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef(
    _RequiredClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef,
    _OptionalClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef,
):
    """
    - *(dict) --*

      Specifies weight and capacity values for a production variant.
      - **VariantName** *(string) --***[REQUIRED]**

        The name of the variant to update.
    """


_ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef = TypedDict(
    "_ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef", {"EndpointArn": str}, total=False
)


class ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef(
    _ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef
):
    """
    - *(dict) --*

      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) of the updated endpoint.
    """


_ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef = TypedDict(
    "_ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef", {"Content": str}, total=False
)


class ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef(
    _ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef
):
    """
    - *(dict) --*

      Contains the notebook instance lifecycle configuration script.
      Each lifecycle configuration script has a limit of 16384 characters.
      The value of the ``$PATH`` environment variable that is available to both scripts is
      ``/sbin:bin:/usr/sbin:/usr/bin`` .
      View CloudWatch Logs for notebook instance lifecycle configurations in log group
      ``/aws/sagemaker/NotebookInstances`` in log stream
      ``[notebook-instance-name]/[LifecycleConfigHook]`` .
      Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for
      longer than 5 minutes, it fails and the notebook instance is not created or started.
      For information about notebook instance lifestyle configurations, see `Step 2.1\\: (Optional)
      Customize a Notebook Instance
      <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
      - **Content** *(string) --*

        A base64-encoded string that contains a shell script for a notebook instance lifecycle
        configuration.
    """


_ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef = TypedDict(
    "_ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef", {"Content": str}, total=False
)


class ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef(
    _ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef
):
    """
    - *(dict) --*

      Contains the notebook instance lifecycle configuration script.
      Each lifecycle configuration script has a limit of 16384 characters.
      The value of the ``$PATH`` environment variable that is available to both scripts is
      ``/sbin:bin:/usr/sbin:/usr/bin`` .
      View CloudWatch Logs for notebook instance lifecycle configurations in log group
      ``/aws/sagemaker/NotebookInstances`` in log stream
      ``[notebook-instance-name]/[LifecycleConfigHook]`` .
      Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for
      longer than 5 minutes, it fails and the notebook instance is not created or started.
      For information about notebook instance lifestyle configurations, see `Step 2.1\\: (Optional)
      Customize a Notebook Instance
      <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
      - **Content** *(string) --*

        A base64-encoded string that contains a shell script for a notebook instance lifecycle
        configuration.
    """


_RequiredClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_RequiredClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str},
)
_OptionalClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_OptionalClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserGroup": str, "ClientId": str},
    total=False,
)


class ClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef(
    _RequiredClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef,
    _OptionalClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef,
):
    """
    - **CognitoMemberDefinition** *(dict) --*

      The Amazon Cognito user group that is part of the work team.
      - **UserPool** *(string) --***[REQUIRED]**

        An identifier for a user pool. The user pool must be in the same region as the service that
        you are calling.
    """


_ClientUpdateWorkteamMemberDefinitionsTypeDef = TypedDict(
    "_ClientUpdateWorkteamMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)


class ClientUpdateWorkteamMemberDefinitionsTypeDef(_ClientUpdateWorkteamMemberDefinitionsTypeDef):
    """
    - *(dict) --*

      Defines the Amazon Cognito user group that is part of a work team.
      - **CognitoMemberDefinition** *(dict) --*

        The Amazon Cognito user group that is part of the work team.
        - **UserPool** *(string) --***[REQUIRED]**

          An identifier for a user pool. The user pool must be in the same region as the service
          that you are calling.
    """


_ClientUpdateWorkteamNotificationConfigurationTypeDef = TypedDict(
    "_ClientUpdateWorkteamNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)


class ClientUpdateWorkteamNotificationConfigurationTypeDef(
    _ClientUpdateWorkteamNotificationConfigurationTypeDef
):
    """
    Configures SNS topic notifications for available or expiring work items
    - **NotificationTopicArn** *(string) --*

      The ARN for the SNS topic to which notifications should be published.
    """


_ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str, "UserGroup": str, "ClientId": str},
    total=False,
)


class ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef(
    _ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
):
    pass


_ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef = TypedDict(
    "_ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)


class ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef(
    _ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef
):
    pass


_ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef = TypedDict(
    "_ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)


class ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef(
    _ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef
):
    pass


_ClientUpdateWorkteamResponseWorkteamTypeDef = TypedDict(
    "_ClientUpdateWorkteamResponseWorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef],
        "WorkteamArn": str,
        "ProductListingIds": List[str],
        "Description": str,
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateWorkteamResponseWorkteamTypeDef(_ClientUpdateWorkteamResponseWorkteamTypeDef):
    """
    - **Workteam** *(dict) --*

      A ``Workteam`` object that describes the updated work team.
      - **WorkteamName** *(string) --*

        The name of the work team.
    """


_ClientUpdateWorkteamResponseTypeDef = TypedDict(
    "_ClientUpdateWorkteamResponseTypeDef",
    {"Workteam": ClientUpdateWorkteamResponseWorkteamTypeDef},
    total=False,
)


class ClientUpdateWorkteamResponseTypeDef(_ClientUpdateWorkteamResponseTypeDef):
    """
    - *(dict) --*

      - **Workteam** *(dict) --*

        A ``Workteam`` object that describes the updated work team.
        - **WorkteamName** *(string) --*

          The name of the work team.
    """


_EndpointDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_EndpointDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class EndpointDeletedWaitWaiterConfigTypeDef(_EndpointDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_EndpointInServiceWaitWaiterConfigTypeDef = TypedDict(
    "_EndpointInServiceWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class EndpointInServiceWaitWaiterConfigTypeDef(_EndpointInServiceWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ListAlgorithmsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAlgorithmsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAlgorithmsPaginatePaginationConfigTypeDef(_ListAlgorithmsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAlgorithmsPaginateResponseAlgorithmSummaryListTypeDef = TypedDict(
    "_ListAlgorithmsPaginateResponseAlgorithmSummaryListTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "AlgorithmStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
    total=False,
)


class ListAlgorithmsPaginateResponseAlgorithmSummaryListTypeDef(
    _ListAlgorithmsPaginateResponseAlgorithmSummaryListTypeDef
):
    """
    - *(dict) --*

      Provides summary information about an algorithm.
      - **AlgorithmName** *(string) --*

        The name of the algorithm that is described by the summary.
    """


_ListAlgorithmsPaginateResponseTypeDef = TypedDict(
    "_ListAlgorithmsPaginateResponseTypeDef",
    {"AlgorithmSummaryList": List[ListAlgorithmsPaginateResponseAlgorithmSummaryListTypeDef]},
    total=False,
)


class ListAlgorithmsPaginateResponseTypeDef(_ListAlgorithmsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **AlgorithmSummaryList** *(list) --*

        >An array of ``AlgorithmSummary`` objects, each of which lists an algorithm.
        - *(dict) --*

          Provides summary information about an algorithm.
          - **AlgorithmName** *(string) --*

            The name of the algorithm that is described by the summary.
    """


_ListCodeRepositoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCodeRepositoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCodeRepositoriesPaginatePaginationConfigTypeDef(
    _ListCodeRepositoriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListGitConfigTypeDef = TypedDict(
    "_ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListGitConfigTypeDef",
    {"RepositoryUrl": str, "Branch": str, "SecretArn": str},
    total=False,
)


class ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListGitConfigTypeDef(
    _ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListGitConfigTypeDef
):
    pass


_ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListTypeDef = TypedDict(
    "_ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListGitConfigTypeDef,
    },
    total=False,
)


class ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListTypeDef(
    _ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListTypeDef
):
    """
    - *(dict) --*

      Specifies summary information about a Git repository.
      - **CodeRepositoryName** *(string) --*

        The name of the Git repository.
    """


_ListCodeRepositoriesPaginateResponseTypeDef = TypedDict(
    "_ListCodeRepositoriesPaginateResponseTypeDef",
    {
        "CodeRepositorySummaryList": List[
            ListCodeRepositoriesPaginateResponseCodeRepositorySummaryListTypeDef
        ]
    },
    total=False,
)


class ListCodeRepositoriesPaginateResponseTypeDef(_ListCodeRepositoriesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **CodeRepositorySummaryList** *(list) --*

        Gets a list of summaries of the Git repositories. Each summary specifies the following
        values for the repository:
        * Name
        * Amazon Resource Name (ARN)
        * Creation time
        * Last modified time
        * Configuration information, including the URL location of the repository and the ARN of the
        AWS Secrets Manager secret that contains the credentials used to access the repository.
        - *(dict) --*

          Specifies summary information about a Git repository.
          - **CodeRepositoryName** *(string) --*

            The name of the Git repository.
    """


_ListCompilationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCompilationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCompilationJobsPaginatePaginationConfigTypeDef(
    _ListCompilationJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCompilationJobsPaginateResponseCompilationJobSummariesTypeDef = TypedDict(
    "_ListCompilationJobsPaginateResponseCompilationJobSummariesTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "CompilationTargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "rasp3b",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
        ],
        "LastModifiedTime": datetime,
        "CompilationJobStatus": Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ],
    },
    total=False,
)


class ListCompilationJobsPaginateResponseCompilationJobSummariesTypeDef(
    _ListCompilationJobsPaginateResponseCompilationJobSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of a model compilation job.
      - **CompilationJobName** *(string) --*

        The name of the model compilation job that you want a summary for.
    """


_ListCompilationJobsPaginateResponseTypeDef = TypedDict(
    "_ListCompilationJobsPaginateResponseTypeDef",
    {
        "CompilationJobSummaries": List[
            ListCompilationJobsPaginateResponseCompilationJobSummariesTypeDef
        ]
    },
    total=False,
)


class ListCompilationJobsPaginateResponseTypeDef(_ListCompilationJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **CompilationJobSummaries** *(list) --*

        An array of  CompilationJobSummary objects, each describing a model compilation job.
        - *(dict) --*

          A summary of a model compilation job.
          - **CompilationJobName** *(string) --*

            The name of the model compilation job that you want a summary for.
    """


_ListEndpointConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEndpointConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEndpointConfigsPaginatePaginationConfigTypeDef(
    _ListEndpointConfigsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEndpointConfigsPaginateResponseEndpointConfigsTypeDef = TypedDict(
    "_ListEndpointConfigsPaginateResponseEndpointConfigsTypeDef",
    {"EndpointConfigName": str, "EndpointConfigArn": str, "CreationTime": datetime},
    total=False,
)


class ListEndpointConfigsPaginateResponseEndpointConfigsTypeDef(
    _ListEndpointConfigsPaginateResponseEndpointConfigsTypeDef
):
    """
    - *(dict) --*

      Provides summary information for an endpoint configuration.
      - **EndpointConfigName** *(string) --*

        The name of the endpoint configuration.
    """


_ListEndpointConfigsPaginateResponseTypeDef = TypedDict(
    "_ListEndpointConfigsPaginateResponseTypeDef",
    {"EndpointConfigs": List[ListEndpointConfigsPaginateResponseEndpointConfigsTypeDef]},
    total=False,
)


class ListEndpointConfigsPaginateResponseTypeDef(_ListEndpointConfigsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **EndpointConfigs** *(list) --*

        An array of endpoint configurations.
        - *(dict) --*

          Provides summary information for an endpoint configuration.
          - **EndpointConfigName** *(string) --*

            The name of the endpoint configuration.
    """


_ListEndpointsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEndpointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEndpointsPaginatePaginationConfigTypeDef(_ListEndpointsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEndpointsPaginateResponseEndpointsTypeDef = TypedDict(
    "_ListEndpointsPaginateResponseEndpointsTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ],
    },
    total=False,
)


class ListEndpointsPaginateResponseEndpointsTypeDef(_ListEndpointsPaginateResponseEndpointsTypeDef):
    """
    - *(dict) --*

      Provides summary information for an endpoint.
      - **EndpointName** *(string) --*

        The name of the endpoint.
    """


_ListEndpointsPaginateResponseTypeDef = TypedDict(
    "_ListEndpointsPaginateResponseTypeDef",
    {"Endpoints": List[ListEndpointsPaginateResponseEndpointsTypeDef]},
    total=False,
)


class ListEndpointsPaginateResponseTypeDef(_ListEndpointsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Endpoints** *(list) --*

        An array or endpoint objects.
        - *(dict) --*

          Provides summary information for an endpoint.
          - **EndpointName** *(string) --*

            The name of the endpoint.
    """


_ListHyperParameterTuningJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHyperParameterTuningJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHyperParameterTuningJobsPaginatePaginationConfigTypeDef(
    _ListHyperParameterTuningJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef = TypedDict(
    "_ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef",
    {"Succeeded": int, "Pending": int, "Failed": int},
    total=False,
)


class ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef(
    _ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef
):
    pass


_ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef = TypedDict(
    "_ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef",
    {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int},
    total=False,
)


class ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef(
    _ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef
):
    pass


_ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef = TypedDict(
    "_ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)


class ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef(
    _ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef
):
    pass


_ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTypeDef = TypedDict(
    "_ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": Literal[
            "Completed", "InProgress", "Failed", "Stopped", "Stopping"
        ],
        "Strategy": Literal["Bayesian", "Random"],
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef,
        "ResourceLimits": ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef,
    },
    total=False,
)


class ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTypeDef(
    _ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTypeDef
):
    """
    - *(dict) --*

      Provides summary information about a hyperparameter tuning job.
      - **HyperParameterTuningJobName** *(string) --*

        The name of the tuning job.
    """


_ListHyperParameterTuningJobsPaginateResponseTypeDef = TypedDict(
    "_ListHyperParameterTuningJobsPaginateResponseTypeDef",
    {
        "HyperParameterTuningJobSummaries": List[
            ListHyperParameterTuningJobsPaginateResponseHyperParameterTuningJobSummariesTypeDef
        ]
    },
    total=False,
)


class ListHyperParameterTuningJobsPaginateResponseTypeDef(
    _ListHyperParameterTuningJobsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **HyperParameterTuningJobSummaries** *(list) --*

        A list of  HyperParameterTuningJobSummary objects that describe the tuning jobs that the
        ``ListHyperParameterTuningJobs`` request returned.
        - *(dict) --*

          Provides summary information about a hyperparameter tuning job.
          - **HyperParameterTuningJobName** *(string) --*

            The name of the tuning job.
    """


_ListLabelingJobsForWorkteamPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLabelingJobsForWorkteamPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLabelingJobsForWorkteamPaginatePaginationConfigTypeDef(
    _ListLabelingJobsForWorkteamPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListLabelCountersTypeDef = TypedDict(
    "_ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListLabelCountersTypeDef",
    {"HumanLabeled": int, "PendingHuman": int, "Total": int},
    total=False,
)


class ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListLabelCountersTypeDef(
    _ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListLabelCountersTypeDef
):
    pass


_ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListTypeDef = TypedDict(
    "_ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListTypeDef",
    {
        "LabelingJobName": str,
        "JobReferenceCode": str,
        "WorkRequesterAccountId": str,
        "CreationTime": datetime,
        "LabelCounters": ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListLabelCountersTypeDef,
        "NumberOfHumanWorkersPerDataObject": int,
    },
    total=False,
)


class ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListTypeDef(
    _ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListTypeDef
):
    """
    - *(dict) --*

      Provides summary information for a work team.
      - **LabelingJobName** *(string) --*

        The name of the labeling job that the work team is assigned to.
    """


_ListLabelingJobsForWorkteamPaginateResponseTypeDef = TypedDict(
    "_ListLabelingJobsForWorkteamPaginateResponseTypeDef",
    {
        "LabelingJobSummaryList": List[
            ListLabelingJobsForWorkteamPaginateResponseLabelingJobSummaryListTypeDef
        ]
    },
    total=False,
)


class ListLabelingJobsForWorkteamPaginateResponseTypeDef(
    _ListLabelingJobsForWorkteamPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **LabelingJobSummaryList** *(list) --*

        An array of ``LabelingJobSummary`` objects, each describing a labeling job.
        - *(dict) --*

          Provides summary information for a work team.
          - **LabelingJobName** *(string) --*

            The name of the labeling job that the work team is assigned to.
    """


_ListLabelingJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLabelingJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLabelingJobsPaginatePaginationConfigTypeDef(
    _ListLabelingJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef = TypedDict(
    "_ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)


class ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef(
    _ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef
):
    pass


_ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef",
    {"ManifestS3Uri": str},
    total=False,
)


class ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef(
    _ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef
):
    pass


_ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceTypeDef = TypedDict(
    "_ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceTypeDef",
    {
        "S3DataSource": ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef
    },
    total=False,
)


class ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceTypeDef(
    _ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceTypeDef
):
    pass


_ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigTypeDef = TypedDict(
    "_ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigTypeDef",
    {
        "DataSource": ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataSourceTypeDef,
        "DataAttributes": ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef,
    },
    total=False,
)


class ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigTypeDef(
    _ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigTypeDef
):
    pass


_ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelCountersTypeDef = TypedDict(
    "_ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)


class ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelCountersTypeDef(
    _ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelCountersTypeDef
):
    pass


_ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelingJobOutputTypeDef = TypedDict(
    "_ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelingJobOutputTypeDef",
    {"OutputDatasetS3Uri": str, "FinalActiveLearningModelArn": str},
    total=False,
)


class ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelingJobOutputTypeDef(
    _ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelingJobOutputTypeDef
):
    pass


_ListLabelingJobsPaginateResponseLabelingJobSummaryListTypeDef = TypedDict(
    "_ListLabelingJobsPaginateResponseLabelingJobSummaryListTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "LabelCounters": ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelCountersTypeDef,
        "WorkteamArn": str,
        "PreHumanTaskLambdaArn": str,
        "AnnotationConsolidationLambdaArn": str,
        "FailureReason": str,
        "LabelingJobOutput": ListLabelingJobsPaginateResponseLabelingJobSummaryListLabelingJobOutputTypeDef,
        "InputConfig": ListLabelingJobsPaginateResponseLabelingJobSummaryListInputConfigTypeDef,
    },
    total=False,
)


class ListLabelingJobsPaginateResponseLabelingJobSummaryListTypeDef(
    _ListLabelingJobsPaginateResponseLabelingJobSummaryListTypeDef
):
    """
    - *(dict) --*

      Provides summary information about a labeling job.
      - **LabelingJobName** *(string) --*

        The name of the labeling job.
    """


_ListLabelingJobsPaginateResponseTypeDef = TypedDict(
    "_ListLabelingJobsPaginateResponseTypeDef",
    {"LabelingJobSummaryList": List[ListLabelingJobsPaginateResponseLabelingJobSummaryListTypeDef]},
    total=False,
)


class ListLabelingJobsPaginateResponseTypeDef(_ListLabelingJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **LabelingJobSummaryList** *(list) --*

        An array of ``LabelingJobSummary`` objects, each describing a labeling job.
        - *(dict) --*

          Provides summary information about a labeling job.
          - **LabelingJobName** *(string) --*

            The name of the labeling job.
    """


_ListModelPackagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListModelPackagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListModelPackagesPaginatePaginationConfigTypeDef(
    _ListModelPackagesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListModelPackagesPaginateResponseModelPackageSummaryListTypeDef = TypedDict(
    "_ListModelPackagesPaginateResponseModelPackageSummaryListTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "ModelPackageStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
    total=False,
)


class ListModelPackagesPaginateResponseModelPackageSummaryListTypeDef(
    _ListModelPackagesPaginateResponseModelPackageSummaryListTypeDef
):
    """
    - *(dict) --*

      Provides summary information about a model package.
      - **ModelPackageName** *(string) --*

        The name of the model package.
    """


_ListModelPackagesPaginateResponseTypeDef = TypedDict(
    "_ListModelPackagesPaginateResponseTypeDef",
    {
        "ModelPackageSummaryList": List[
            ListModelPackagesPaginateResponseModelPackageSummaryListTypeDef
        ]
    },
    total=False,
)


class ListModelPackagesPaginateResponseTypeDef(_ListModelPackagesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ModelPackageSummaryList** *(list) --*

        An array of ``ModelPackageSummary`` objects, each of which lists a model package.
        - *(dict) --*

          Provides summary information about a model package.
          - **ModelPackageName** *(string) --*

            The name of the model package.
    """


_ListModelsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListModelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListModelsPaginatePaginationConfigTypeDef(_ListModelsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListModelsPaginateResponseModelsTypeDef = TypedDict(
    "_ListModelsPaginateResponseModelsTypeDef",
    {"ModelName": str, "ModelArn": str, "CreationTime": datetime},
    total=False,
)


class ListModelsPaginateResponseModelsTypeDef(_ListModelsPaginateResponseModelsTypeDef):
    """
    - *(dict) --*

      Provides summary information about a model.
      - **ModelName** *(string) --*

        The name of the model that you want a summary for.
    """


_ListModelsPaginateResponseTypeDef = TypedDict(
    "_ListModelsPaginateResponseTypeDef",
    {"Models": List[ListModelsPaginateResponseModelsTypeDef]},
    total=False,
)


class ListModelsPaginateResponseTypeDef(_ListModelsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Models** *(list) --*

        An array of ``ModelSummary`` objects, each of which lists a model.
        - *(dict) --*

          Provides summary information about a model.
          - **ModelName** *(string) --*

            The name of the model that you want a summary for.
    """


_ListNotebookInstanceLifecycleConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNotebookInstanceLifecycleConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNotebookInstanceLifecycleConfigsPaginatePaginationConfigTypeDef(
    _ListNotebookInstanceLifecycleConfigsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListNotebookInstanceLifecycleConfigsPaginateResponseNotebookInstanceLifecycleConfigsTypeDef = TypedDict(
    "_ListNotebookInstanceLifecycleConfigsPaginateResponseNotebookInstanceLifecycleConfigsTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceLifecycleConfigArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ListNotebookInstanceLifecycleConfigsPaginateResponseNotebookInstanceLifecycleConfigsTypeDef(
    _ListNotebookInstanceLifecycleConfigsPaginateResponseNotebookInstanceLifecycleConfigsTypeDef
):
    """
    - *(dict) --*

      Provides a summary of a notebook instance lifecycle configuration.
      - **NotebookInstanceLifecycleConfigName** *(string) --*

        The name of the lifecycle configuration.
    """


_ListNotebookInstanceLifecycleConfigsPaginateResponseTypeDef = TypedDict(
    "_ListNotebookInstanceLifecycleConfigsPaginateResponseTypeDef",
    {
        "NotebookInstanceLifecycleConfigs": List[
            ListNotebookInstanceLifecycleConfigsPaginateResponseNotebookInstanceLifecycleConfigsTypeDef
        ]
    },
    total=False,
)


class ListNotebookInstanceLifecycleConfigsPaginateResponseTypeDef(
    _ListNotebookInstanceLifecycleConfigsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **NotebookInstanceLifecycleConfigs** *(list) --*

        An array of ``NotebookInstanceLifecycleConfiguration`` objects, each listing a lifecycle
        configuration.
        - *(dict) --*

          Provides a summary of a notebook instance lifecycle configuration.
          - **NotebookInstanceLifecycleConfigName** *(string) --*

            The name of the lifecycle configuration.
    """


_ListNotebookInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNotebookInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNotebookInstancesPaginatePaginationConfigTypeDef(
    _ListNotebookInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListNotebookInstancesPaginateResponseNotebookInstancesTypeDef = TypedDict(
    "_ListNotebookInstancesPaginateResponseNotebookInstancesTypeDef",
    {
        "NotebookInstanceName": str,
        "NotebookInstanceArn": str,
        "NotebookInstanceStatus": Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ],
        "Url": str,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
    },
    total=False,
)


class ListNotebookInstancesPaginateResponseNotebookInstancesTypeDef(
    _ListNotebookInstancesPaginateResponseNotebookInstancesTypeDef
):
    """
    - *(dict) --*

      Provides summary information for an Amazon SageMaker notebook instance.
      - **NotebookInstanceName** *(string) --*

        The name of the notebook instance that you want a summary for.
    """


_ListNotebookInstancesPaginateResponseTypeDef = TypedDict(
    "_ListNotebookInstancesPaginateResponseTypeDef",
    {"NotebookInstances": List[ListNotebookInstancesPaginateResponseNotebookInstancesTypeDef]},
    total=False,
)


class ListNotebookInstancesPaginateResponseTypeDef(_ListNotebookInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NotebookInstances** *(list) --*

        An array of ``NotebookInstanceSummary`` objects, one for each notebook instance.
        - *(dict) --*

          Provides summary information for an Amazon SageMaker notebook instance.
          - **NotebookInstanceName** *(string) --*

            The name of the notebook instance that you want a summary for.
    """


_ListSubscribedWorkteamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscribedWorkteamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSubscribedWorkteamsPaginatePaginationConfigTypeDef(
    _ListSubscribedWorkteamsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSubscribedWorkteamsPaginateResponseSubscribedWorkteamsTypeDef = TypedDict(
    "_ListSubscribedWorkteamsPaginateResponseSubscribedWorkteamsTypeDef",
    {
        "WorkteamArn": str,
        "MarketplaceTitle": str,
        "SellerName": str,
        "MarketplaceDescription": str,
        "ListingId": str,
    },
    total=False,
)


class ListSubscribedWorkteamsPaginateResponseSubscribedWorkteamsTypeDef(
    _ListSubscribedWorkteamsPaginateResponseSubscribedWorkteamsTypeDef
):
    """
    - *(dict) --*

      Describes a work team of a vendor that does the a labelling job.
      - **WorkteamArn** *(string) --*

        The Amazon Resource Name (ARN) of the vendor that you have subscribed.
    """


_ListSubscribedWorkteamsPaginateResponseTypeDef = TypedDict(
    "_ListSubscribedWorkteamsPaginateResponseTypeDef",
    {
        "SubscribedWorkteams": List[
            ListSubscribedWorkteamsPaginateResponseSubscribedWorkteamsTypeDef
        ]
    },
    total=False,
)


class ListSubscribedWorkteamsPaginateResponseTypeDef(
    _ListSubscribedWorkteamsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SubscribedWorkteams** *(list) --*

        An array of ``Workteam`` objects, each describing a work team.
        - *(dict) --*

          Describes a work team of a vendor that does the a labelling job.
          - **WorkteamArn** *(string) --*

            The Amazon Resource Name (ARN) of the vendor that you have subscribed.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsPaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagsTypeDef(_ListTagsPaginateResponseTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --*

        The tag key.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"Tags": List[ListTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        An array of ``Tag`` objects, each with a tag key and a value.
        - *(dict) --*

          Describes a tag.
          - **Key** *(string) --*

            The tag key.
    """


_ListTrainingJobsForHyperParameterTuningJobPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTrainingJobsForHyperParameterTuningJobPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobPaginatePaginationConfigTypeDef(
    _ListTrainingJobsForHyperParameterTuningJobPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str, "Value": Any},
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef
):
    pass


_ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesTypeDef = TypedDict(
    "_ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobName": str,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "TunedHyperParameters": Dict[str, str],
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesTypeDef(
    _ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesTypeDef
):
    """
    - *(dict) --*

      Specifies summary information about a training job.
      - **TrainingJobName** *(string) --*

        The name of the training job.
    """


_ListTrainingJobsForHyperParameterTuningJobPaginateResponseTypeDef = TypedDict(
    "_ListTrainingJobsForHyperParameterTuningJobPaginateResponseTypeDef",
    {
        "TrainingJobSummaries": List[
            ListTrainingJobsForHyperParameterTuningJobPaginateResponseTrainingJobSummariesTypeDef
        ]
    },
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobPaginateResponseTypeDef(
    _ListTrainingJobsForHyperParameterTuningJobPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **TrainingJobSummaries** *(list) --*

        A list of  TrainingJobSummary objects that describe the training jobs that the
        ``ListTrainingJobsForHyperParameterTuningJob`` request returned.
        - *(dict) --*

          Specifies summary information about a training job.
          - **TrainingJobName** *(string) --*

            The name of the training job.
    """


_ListTrainingJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTrainingJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTrainingJobsPaginatePaginationConfigTypeDef(
    _ListTrainingJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTrainingJobsPaginateResponseTrainingJobSummariesTypeDef = TypedDict(
    "_ListTrainingJobsPaginateResponseTrainingJobSummariesTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
    },
    total=False,
)


class ListTrainingJobsPaginateResponseTrainingJobSummariesTypeDef(
    _ListTrainingJobsPaginateResponseTrainingJobSummariesTypeDef
):
    """
    - *(dict) --*

      Provides summary information about a training job.
      - **TrainingJobName** *(string) --*

        The name of the training job that you want a summary for.
    """


_ListTrainingJobsPaginateResponseTypeDef = TypedDict(
    "_ListTrainingJobsPaginateResponseTypeDef",
    {"TrainingJobSummaries": List[ListTrainingJobsPaginateResponseTrainingJobSummariesTypeDef]},
    total=False,
)


class ListTrainingJobsPaginateResponseTypeDef(_ListTrainingJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TrainingJobSummaries** *(list) --*

        An array of ``TrainingJobSummary`` objects, each listing a training job.
        - *(dict) --*

          Provides summary information about a training job.
          - **TrainingJobName** *(string) --*

            The name of the training job that you want a summary for.
    """


_ListTransformJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTransformJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTransformJobsPaginatePaginationConfigTypeDef(
    _ListTransformJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTransformJobsPaginateResponseTransformJobSummariesTypeDef = TypedDict(
    "_ListTransformJobsPaginateResponseTransformJobSummariesTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformEndTime": datetime,
        "LastModifiedTime": datetime,
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "FailureReason": str,
    },
    total=False,
)


class ListTransformJobsPaginateResponseTransformJobSummariesTypeDef(
    _ListTransformJobsPaginateResponseTransformJobSummariesTypeDef
):
    """
    - *(dict) --*

      Provides a summary of a transform job. Multiple ``TransformJobSummary`` objects are returned
      as a list after in response to a  ListTransformJobs call.
      - **TransformJobName** *(string) --*

        The name of the transform job.
    """


_ListTransformJobsPaginateResponseTypeDef = TypedDict(
    "_ListTransformJobsPaginateResponseTypeDef",
    {"TransformJobSummaries": List[ListTransformJobsPaginateResponseTransformJobSummariesTypeDef]},
    total=False,
)


class ListTransformJobsPaginateResponseTypeDef(_ListTransformJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TransformJobSummaries** *(list) --*

        An array of ``TransformJobSummary`` objects.
        - *(dict) --*

          Provides a summary of a transform job. Multiple ``TransformJobSummary`` objects are
          returned as a list after in response to a  ListTransformJobs call.
          - **TransformJobName** *(string) --*

            The name of the transform job.
    """


_ListWorkteamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListWorkteamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListWorkteamsPaginatePaginationConfigTypeDef(_ListWorkteamsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str, "UserGroup": str, "ClientId": str},
    total=False,
)


class ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef(
    _ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef
):
    pass


_ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsTypeDef = TypedDict(
    "_ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)


class ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsTypeDef(
    _ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsTypeDef
):
    pass


_ListWorkteamsPaginateResponseWorkteamsNotificationConfigurationTypeDef = TypedDict(
    "_ListWorkteamsPaginateResponseWorkteamsNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)


class ListWorkteamsPaginateResponseWorkteamsNotificationConfigurationTypeDef(
    _ListWorkteamsPaginateResponseWorkteamsNotificationConfigurationTypeDef
):
    pass


_ListWorkteamsPaginateResponseWorkteamsTypeDef = TypedDict(
    "_ListWorkteamsPaginateResponseWorkteamsTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[ListWorkteamsPaginateResponseWorkteamsMemberDefinitionsTypeDef],
        "WorkteamArn": str,
        "ProductListingIds": List[str],
        "Description": str,
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": ListWorkteamsPaginateResponseWorkteamsNotificationConfigurationTypeDef,
    },
    total=False,
)


class ListWorkteamsPaginateResponseWorkteamsTypeDef(_ListWorkteamsPaginateResponseWorkteamsTypeDef):
    """
    - *(dict) --*

      Provides details about a labeling work team.
      - **WorkteamName** *(string) --*

        The name of the work team.
    """


_ListWorkteamsPaginateResponseTypeDef = TypedDict(
    "_ListWorkteamsPaginateResponseTypeDef",
    {"Workteams": List[ListWorkteamsPaginateResponseWorkteamsTypeDef]},
    total=False,
)


class ListWorkteamsPaginateResponseTypeDef(_ListWorkteamsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Workteams** *(list) --*

        An array of ``Workteam`` objects, each describing a work team.
        - *(dict) --*

          Provides details about a labeling work team.
          - **WorkteamName** *(string) --*

            The name of the work team.
    """


_NotebookInstanceDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_NotebookInstanceDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class NotebookInstanceDeletedWaitWaiterConfigTypeDef(
    _NotebookInstanceDeletedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_NotebookInstanceInServiceWaitWaiterConfigTypeDef = TypedDict(
    "_NotebookInstanceInServiceWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class NotebookInstanceInServiceWaitWaiterConfigTypeDef(
    _NotebookInstanceInServiceWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_NotebookInstanceStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_NotebookInstanceStoppedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class NotebookInstanceStoppedWaitWaiterConfigTypeDef(
    _NotebookInstanceStoppedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_SearchPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchPaginatePaginationConfigTypeDef(_SearchPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)


class SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef(
    _SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "MetricDefinitions": List[
            SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)


class SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationTypeDef(
    _SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobFinalMetricDataListTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobFinalMetricDataListTypeDef",
    {"MetricName": str, "Value": Any, "Timestamp": datetime},
    total=False,
)


class SearchPaginateResponseResultsTrainingJobFinalMetricDataListTypeDef(
    _SearchPaginateResponseResultsTrainingJobFinalMetricDataListTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)


class SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef(
    _SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef(
    _SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)


class SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceTypeDef(
    _SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)


class SearchPaginateResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef(
    _SearchPaginateResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobInputDataConfigTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": SearchPaginateResponseResultsTrainingJobInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": SearchPaginateResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class SearchPaginateResponseResultsTrainingJobInputDataConfigTypeDef(
    _SearchPaginateResponseResultsTrainingJobInputDataConfigTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobModelArtifactsTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobModelArtifactsTypeDef",
    {"S3ModelArtifacts": str},
    total=False,
)


class SearchPaginateResponseResultsTrainingJobModelArtifactsTypeDef(
    _SearchPaginateResponseResultsTrainingJobModelArtifactsTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobOutputDataConfigTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)


class SearchPaginateResponseResultsTrainingJobOutputDataConfigTypeDef(
    _SearchPaginateResponseResultsTrainingJobOutputDataConfigTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobResourceConfigTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class SearchPaginateResponseResultsTrainingJobResourceConfigTypeDef(
    _SearchPaginateResponseResultsTrainingJobResourceConfigTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef",
    {
        "Status": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)


class SearchPaginateResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef(
    _SearchPaginateResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobStoppingConditionTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)


class SearchPaginateResponseResultsTrainingJobStoppingConditionTypeDef(
    _SearchPaginateResponseResultsTrainingJobStoppingConditionTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobTagsTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class SearchPaginateResponseResultsTrainingJobTagsTypeDef(
    _SearchPaginateResponseResultsTrainingJobTagsTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobVpcConfigTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class SearchPaginateResponseResultsTrainingJobVpcConfigTypeDef(
    _SearchPaginateResponseResultsTrainingJobVpcConfigTypeDef
):
    pass


_SearchPaginateResponseResultsTrainingJobTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "ModelArtifacts": SearchPaginateResponseResultsTrainingJobModelArtifactsTypeDef,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": SearchPaginateResponseResultsTrainingJobAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[SearchPaginateResponseResultsTrainingJobInputDataConfigTypeDef],
        "OutputDataConfig": SearchPaginateResponseResultsTrainingJobOutputDataConfigTypeDef,
        "ResourceConfig": SearchPaginateResponseResultsTrainingJobResourceConfigTypeDef,
        "VpcConfig": SearchPaginateResponseResultsTrainingJobVpcConfigTypeDef,
        "StoppingCondition": SearchPaginateResponseResultsTrainingJobStoppingConditionTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[
            SearchPaginateResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef
        ],
        "FinalMetricDataList": List[
            SearchPaginateResponseResultsTrainingJobFinalMetricDataListTypeDef
        ],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "Tags": List[SearchPaginateResponseResultsTrainingJobTagsTypeDef],
    },
    total=False,
)


class SearchPaginateResponseResultsTrainingJobTypeDef(
    _SearchPaginateResponseResultsTrainingJobTypeDef
):
    """
    - **TrainingJob** *(dict) --*

      A ``TrainingJob`` object that is returned as part of a ``Search`` request.
      - **TrainingJobName** *(string) --*

        The name of the training job.
    """


_SearchPaginateResponseResultsTypeDef = TypedDict(
    "_SearchPaginateResponseResultsTypeDef",
    {"TrainingJob": SearchPaginateResponseResultsTrainingJobTypeDef},
    total=False,
)


class SearchPaginateResponseResultsTypeDef(_SearchPaginateResponseResultsTypeDef):
    """
    - *(dict) --*

      An individual search result record that contains a single resource object.
      - **TrainingJob** *(dict) --*

        A ``TrainingJob`` object that is returned as part of a ``Search`` request.
        - **TrainingJobName** *(string) --*

          The name of the training job.
    """


_SearchPaginateResponseTypeDef = TypedDict(
    "_SearchPaginateResponseTypeDef",
    {"Results": List[SearchPaginateResponseResultsTypeDef]},
    total=False,
)


class SearchPaginateResponseTypeDef(_SearchPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Results** *(list) --*

        A list of ``SearchResult`` objects.
        - *(dict) --*

          An individual search result record that contains a single resource object.
          - **TrainingJob** *(dict) --*

            A ``TrainingJob`` object that is returned as part of a ``Search`` request.
            - **TrainingJobName** *(string) --*

              The name of the training job.
    """


_SearchPaginateSearchExpressionFiltersTypeDef = TypedDict(
    "_SearchPaginateSearchExpressionFiltersTypeDef",
    {
        "Name": str,
        "Operator": Literal[
            "Equals",
            "NotEquals",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "LessThan",
            "LessThanOrEqualTo",
            "Contains",
        ],
        "Value": str,
    },
    total=False,
)


class SearchPaginateSearchExpressionFiltersTypeDef(_SearchPaginateSearchExpressionFiltersTypeDef):
    """
    - *(dict) --*

      A conditional statement for a search expression that includes a resource property, a Boolean
      operator, and a value.
      If you don't specify an ``Operator`` and a ``Value`` , the filter searches for only the
      specified property. For example, defining a ``Filter`` for the ``FailureReason`` for the
      ``TrainingJob``  ``Resource`` searches for training job objects that have a value in the
      ``FailureReason`` field.
      If you specify a ``Value`` , but not an ``Operator`` , Amazon SageMaker uses the equals
      operator as the default.
      In search, there are several property types:

        Metrics
    """


_SearchPaginateSearchExpressionNestedFiltersFiltersTypeDef = TypedDict(
    "_SearchPaginateSearchExpressionNestedFiltersFiltersTypeDef",
    {
        "Name": str,
        "Operator": Literal[
            "Equals",
            "NotEquals",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "LessThan",
            "LessThanOrEqualTo",
            "Contains",
        ],
        "Value": str,
    },
    total=False,
)


class SearchPaginateSearchExpressionNestedFiltersFiltersTypeDef(
    _SearchPaginateSearchExpressionNestedFiltersFiltersTypeDef
):
    pass


_SearchPaginateSearchExpressionNestedFiltersTypeDef = TypedDict(
    "_SearchPaginateSearchExpressionNestedFiltersTypeDef",
    {
        "NestedPropertyName": str,
        "Filters": List[SearchPaginateSearchExpressionNestedFiltersFiltersTypeDef],
    },
    total=False,
)


class SearchPaginateSearchExpressionNestedFiltersTypeDef(
    _SearchPaginateSearchExpressionNestedFiltersTypeDef
):
    pass


_SearchPaginateSearchExpressionTypeDef = TypedDict(
    "_SearchPaginateSearchExpressionTypeDef",
    {
        "Filters": List[SearchPaginateSearchExpressionFiltersTypeDef],
        "NestedFilters": List[SearchPaginateSearchExpressionNestedFiltersTypeDef],
        "SubExpressions": List[Any],
        "Operator": Literal["And", "Or"],
    },
    total=False,
)


class SearchPaginateSearchExpressionTypeDef(_SearchPaginateSearchExpressionTypeDef):
    """
    A Boolean conditional statement. Resource objects must satisfy this condition to be included in
    search results. You must provide at least one subexpression, filter, or nested filter. The
    maximum number of recursive ``SubExpressions`` , ``NestedFilters`` , and ``Filters`` that can be
    included in a ``SearchExpression`` object is 50.
    - **Filters** *(list) --*

      A list of filter objects.
      - *(dict) --*

        A conditional statement for a search expression that includes a resource property, a Boolean
        operator, and a value.
        If you don't specify an ``Operator`` and a ``Value`` , the filter searches for only the
        specified property. For example, defining a ``Filter`` for the ``FailureReason`` for the
        ``TrainingJob``  ``Resource`` searches for training job objects that have a value in the
        ``FailureReason`` field.
        If you specify a ``Value`` , but not an ``Operator`` , Amazon SageMaker uses the equals
        operator as the default.
        In search, there are several property types:

          Metrics
    """


_TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef(
    _TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 120
    """


_TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef(
    _TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60
    """
